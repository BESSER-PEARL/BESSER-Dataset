from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class Attachment:

    pass
class Ranking:

    pass
class Extension:

    pass
class data_Attachment(Extension):

    def __init__(self, fileUrl: str, cachedFileUrl: str, cachedOnly: str, fileExtension: str, fileIdentifier: str, cachedFileName: str, noCache: str):
        self.fileUrl = fileUrl
        self.cachedFileUrl = cachedFileUrl
        self.cachedOnly = cachedOnly
        self.fileExtension = fileExtension
        self.fileIdentifier = fileIdentifier
        self.cachedFileName = cachedFileName
        self.noCache = noCache
        
    @property
    def noCache(self) -> str:
        return self.__noCache

    @noCache.setter
    def noCache(self, noCache: str):
        self.__noCache = noCache

    @property
    def fileIdentifier(self) -> str:
        return self.__fileIdentifier

    @fileIdentifier.setter
    def fileIdentifier(self, fileIdentifier: str):
        self.__fileIdentifier = fileIdentifier

    @property
    def cachedOnly(self) -> str:
        return self.__cachedOnly

    @cachedOnly.setter
    def cachedOnly(self, cachedOnly: str):
        self.__cachedOnly = cachedOnly

    @property
    def fileUrl(self) -> str:
        return self.__fileUrl

    @fileUrl.setter
    def fileUrl(self, fileUrl: str):
        self.__fileUrl = fileUrl

    @property
    def cachedFileName(self) -> str:
        return self.__cachedFileName

    @cachedFileName.setter
    def cachedFileName(self, cachedFileName: str):
        self.__cachedFileName = cachedFileName

    @property
    def fileExtension(self) -> str:
        return self.__fileExtension

    @fileExtension.setter
    def fileExtension(self, fileExtension: str):
        self.__fileExtension = fileExtension

    @property
    def cachedFileUrl(self) -> str:
        return self.__cachedFileUrl

    @cachedFileUrl.setter
    def cachedFileUrl(self, cachedFileUrl: str):
        self.__cachedFileUrl = cachedFileUrl

    def getOriginalFileUrl(self) -> str:
        # TODO: Implement getOriginalFileUrl method
        pass

    def reloadFile(self) -> str:
        # TODO: Implement reloadFile method
        pass

class MetaInformation:

    pass
class data_WebSite(MetaInformation):

    def __init__(self, adress: str, title: str, shortenedUrl: str):
        self.adress = adress
        self.title = title
        self.shortenedUrl = shortenedUrl
        
    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def adress(self) -> str:
        return self.__adress

    @adress.setter
    def adress(self, adress: str):
        self.__adress = adress

    @property
    def shortenedUrl(self) -> str:
        return self.__shortenedUrl

    @shortenedUrl.setter
    def shortenedUrl(self, shortenedUrl: str):
        self.__shortenedUrl = shortenedUrl

class data_IndoorLocation(MetaInformation):

    def __init__(self, name: str, IndoorLocation: "data_Location" = None, indoorLocations: "data_Location" = None, IndoorLocation102: "data_IndoorLocation" = None, indoorLocations101: "data_IndoorLocation" = None, IndoorLocation105: "data_IndoorLocation" = None, parentIndoorLocation: set["data_IndoorLocation"] = None):
        self.name = name
        self.IndoorLocation = IndoorLocation
        self.indoorLocations = indoorLocations
        self.IndoorLocation102 = IndoorLocation102
        self.indoorLocations101 = indoorLocations101
        self.IndoorLocation105 = IndoorLocation105
        self.parentIndoorLocation = parentIndoorLocation if parentIndoorLocation is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def indoorLocations101(self):
        return self.__indoorLocations101

    @indoorLocations101.setter
    def indoorLocations101(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_data_IndoorLocation__indoorLocations101", None)
        self.__indoorLocations101 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "IndoorLocation102"):
                opp_val = getattr(old_value, "IndoorLocation102", None)
                if opp_val == self:
                    setattr(old_value, "IndoorLocation102", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "IndoorLocation102"):
                opp_val = getattr(value, "IndoorLocation102", None)
                setattr(value, "IndoorLocation102", self)

    @property
    def IndoorLocation105(self):
        return self.__IndoorLocation105

    @IndoorLocation105.setter
    def IndoorLocation105(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_data_IndoorLocation__IndoorLocation105", None)
        self.__IndoorLocation105 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "parentIndoorLocation"):
                opp_val = getattr(old_value, "parentIndoorLocation", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "parentIndoorLocation"):
                opp_val = getattr(value, "parentIndoorLocation", None)
                if opp_val is None:
                    setattr(value, "parentIndoorLocation", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def IndoorLocation(self):
        return self.__IndoorLocation

    @IndoorLocation.setter
    def IndoorLocation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_data_IndoorLocation__IndoorLocation", None)
        self.__IndoorLocation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "location"):
                opp_val = getattr(old_value, "location", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "location"):
                opp_val = getattr(value, "location", None)
                if opp_val is None:
                    setattr(value, "location", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def parentIndoorLocation(self):
        return self.__parentIndoorLocation

    @parentIndoorLocation.setter
    def parentIndoorLocation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_data_IndoorLocation__parentIndoorLocation", None)
        self.__parentIndoorLocation = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "IndoorLocation105"):
                    opp_val = getattr(item, "IndoorLocation105", None)
                    
                    if opp_val == self:
                        setattr(item, "IndoorLocation105", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "IndoorLocation105"):
                    opp_val = getattr(item, "IndoorLocation105", None)
                    
                    setattr(item, "IndoorLocation105", self)
                    

    @property
    def IndoorLocation102(self):
        return self.__IndoorLocation102

    @IndoorLocation102.setter
    def IndoorLocation102(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_data_IndoorLocation__IndoorLocation102", None)
        self.__IndoorLocation102 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "indoorLocations101"):
                opp_val = getattr(old_value, "indoorLocations101", None)
                if opp_val == self:
                    setattr(old_value, "indoorLocations101", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "indoorLocations101"):
                opp_val = getattr(value, "indoorLocations101", None)
                setattr(value, "indoorLocations101", self)

    @property
    def indoorLocations(self):
        return self.__indoorLocations

    @indoorLocations.setter
    def indoorLocations(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_data_IndoorLocation__indoorLocations", None)
        self.__indoorLocations = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Location"):
                opp_val = getattr(old_value, "Location", None)
                if opp_val == self:
                    setattr(old_value, "Location", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Location"):
                opp_val = getattr(value, "Location", None)
                setattr(value, "Location", self)

class data_Citation(MetaInformation):

    def __init__(self, citationData: str):
        self.citationData = citationData
        
    @property
    def citationData(self) -> str:
        return self.__citationData

    @citationData.setter
    def citationData(self, citationData: str):
        self.__citationData = citationData

class data_WebAccount(MetaInformation):

    def __init__(self, username: str, service: str):
        self.username = username
        self.service = service
        
    @property
    def username(self) -> str:
        return self.__username

    @username.setter
    def username(self, username: str):
        self.__username = username

    @property
    def service(self) -> str:
        return self.__service

    @service.setter
    def service(self, service: str):
        self.__service = service

class data_Email(MetaInformation):

    def __init__(self, adress: str):
        self.adress = adress
        
    @property
    def adress(self) -> str:
        return self.__adress

    @adress.setter
    def adress(self, adress: str):
        self.__adress = adress

class data_Location(MetaInformation):

    def __init__(self, street: str, houseNumber: str, zipCode: str, country: str, longitude: str, latitude: str, city: str, state: str, location: set["data_IndoorLocation"] = None, Location: "data_IndoorLocation" = None):
        self.street = street
        self.houseNumber = houseNumber
        self.zipCode = zipCode
        self.country = country
        self.longitude = longitude
        self.latitude = latitude
        self.city = city
        self.state = state
        self.location = location if location is not None else set()
        self.Location = Location
        
    @property
    def zipCode(self) -> str:
        return self.__zipCode

    @zipCode.setter
    def zipCode(self, zipCode: str):
        self.__zipCode = zipCode

    @property
    def longitude(self) -> str:
        return self.__longitude

    @longitude.setter
    def longitude(self, longitude: str):
        self.__longitude = longitude

    @property
    def country(self) -> str:
        return self.__country

    @country.setter
    def country(self, country: str):
        self.__country = country

    @property
    def houseNumber(self) -> str:
        return self.__houseNumber

    @houseNumber.setter
    def houseNumber(self, houseNumber: str):
        self.__houseNumber = houseNumber

    @property
    def city(self) -> str:
        return self.__city

    @city.setter
    def city(self, city: str):
        self.__city = city

    @property
    def latitude(self) -> str:
        return self.__latitude

    @latitude.setter
    def latitude(self, latitude: str):
        self.__latitude = latitude

    @property
    def state(self) -> str:
        return self.__state

    @state.setter
    def state(self, state: str):
        self.__state = state

    @property
    def street(self) -> str:
        return self.__street

    @street.setter
    def street(self, street: str):
        self.__street = street

    @property
    def Location(self):
        return self.__Location

    @Location.setter
    def Location(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_data_Location__Location", None)
        self.__Location = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "indoorLocations"):
                opp_val = getattr(old_value, "indoorLocations", None)
                if opp_val == self:
                    setattr(old_value, "indoorLocations", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "indoorLocations"):
                opp_val = getattr(value, "indoorLocations", None)
                setattr(value, "indoorLocations", self)

    @property
    def location(self):
        return self.__location

    @location.setter
    def location(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_data_Location__location", None)
        self.__location = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "IndoorLocation"):
                    opp_val = getattr(item, "IndoorLocation", None)
                    
                    if opp_val == self:
                        setattr(item, "IndoorLocation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "IndoorLocation"):
                    opp_val = getattr(item, "IndoorLocation", None)
                    
                    setattr(item, "IndoorLocation", self)
                    

class data_Event(MetaInformation):

    def __init__(self, date: date):
        self.date = date
        
    @property
    def date(self) -> date:
        return self.__date

    @date.setter
    def date(self, date: date):
        self.__date = date

    def getDatePrettyInLanguage(self, language: str) -> str:
        # TODO: Implement getDatePrettyInLanguage method
        pass

    def getDatePretty(self) -> str:
        # TODO: Implement getDatePretty method
        pass

class data_InstantMessenger(MetaInformation):

    def __init__(self, username: str):
        self.username = username
        
    @property
    def username(self) -> str:
        return self.__username

    @username.setter
    def username(self, username: str):
        self.__username = username

class data_Phone(MetaInformation):

    def __init__(self, areaCode: str, countryCode: str, number: str):
        self.areaCode = areaCode
        self.countryCode = countryCode
        self.number = number
        
    @property
    def countryCode(self) -> str:
        return self.__countryCode

    @countryCode.setter
    def countryCode(self, countryCode: str):
        self.__countryCode = countryCode

    @property
    def number(self) -> str:
        return self.__number

    @number.setter
    def number(self, number: str):
        self.__number = number

    @property
    def areaCode(self) -> str:
        return self.__areaCode

    @areaCode.setter
    def areaCode(self, areaCode: str):
        self.__areaCode = areaCode

class Classification:

    pass
class data_Item(ABC):

    def __init__(self, ident: str, uri: str, stringValue: str, lastModified: date, created: date, Item: "data_DataSet" = None, items: "data_DataSet" = None, Item50: "data_Item" = None, deleteOnDelete: set["data_Item"] = None, Item53: "data_Item" = None, forcedDeletedIfDeleted: set["data_Item"] = None, Item56: "data_Item" = None, forcedDeleteOnDelete: set["data_Item"] = None, metaTagged: set["data_MetaTag"] = None, identified: set["data_Identifier"] = None, Item47: "data_Item" = None, deletedIfDeleted: set["data_Item"] = None, Item80: "data_MetaTag" = None, Item107: "data_Identifier" = None):
        self.ident = ident
        self.uri = uri
        self.stringValue = stringValue
        self.lastModified = lastModified
        self.created = created
        self.Item = Item
        self.items = items
        self.Item50 = Item50
        self.deleteOnDelete = deleteOnDelete if deleteOnDelete is not None else set()
        self.Item53 = Item53
        self.forcedDeletedIfDeleted = forcedDeletedIfDeleted if forcedDeletedIfDeleted is not None else set()
        self.Item56 = Item56
        self.forcedDeleteOnDelete = forcedDeleteOnDelete if forcedDeleteOnDelete is not None else set()
        self.metaTagged = metaTagged if metaTagged is not None else set()
        self.identified = identified if identified is not None else set()
        self.Item47 = Item47
        self.deletedIfDeleted = deletedIfDeleted if deletedIfDeleted is not None else set()
        self.Item80 = Item80
        self.Item107 = Item107
        
    @property
    def stringValue(self) -> str:
        return self.__stringValue

    @stringValue.setter
    def stringValue(self, stringValue: str):
        self.__stringValue = stringValue

    @property
    def created(self) -> date:
        return self.__created

    @created.setter
    def created(self, created: date):
        self.__created = created

    @property
    def ident(self) -> str:
        return self.__ident

    @ident.setter
    def ident(self, ident: str):
        self.__ident = ident

    @property
    def uri(self) -> str:
        return self.__uri

    @uri.setter
    def uri(self, uri: str):
        self.__uri = uri

    @property
    def lastModified(self) -> date:
        return self.__lastModified

    @lastModified.setter
    def lastModified(self, lastModified: date):
        self.__lastModified = lastModified

    @property
    def identified(self):
        return self.__identified

    @identified.setter
    def identified(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_data_Item__identified", None)
        self.__identified = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Identifier"):
                    opp_val = getattr(item, "Identifier", None)
                    
                    if opp_val == self:
                        setattr(item, "Identifier", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Identifier"):
                    opp_val = getattr(item, "Identifier", None)
                    
                    setattr(item, "Identifier", self)
                    

    @property
    def items(self):
        return self.__items

    @items.setter
    def items(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_data_Item__items", None)
        self.__items = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DataSet"):
                opp_val = getattr(old_value, "DataSet", None)
                if opp_val == self:
                    setattr(old_value, "DataSet", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DataSet"):
                opp_val = getattr(value, "DataSet", None)
                setattr(value, "DataSet", self)

    @property
    def Item56(self):
        return self.__Item56

    @Item56.setter
    def Item56(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_data_Item__Item56", None)
        self.__Item56 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "forcedDeleteOnDelete"):
                opp_val = getattr(old_value, "forcedDeleteOnDelete", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "forcedDeleteOnDelete"):
                opp_val = getattr(value, "forcedDeleteOnDelete", None)
                if opp_val is None:
                    setattr(value, "forcedDeleteOnDelete", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def deleteOnDelete(self):
        return self.__deleteOnDelete

    @deleteOnDelete.setter
    def deleteOnDelete(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_data_Item__deleteOnDelete", None)
        self.__deleteOnDelete = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Item50"):
                    opp_val = getattr(item, "Item50", None)
                    
                    if opp_val == self:
                        setattr(item, "Item50", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Item50"):
                    opp_val = getattr(item, "Item50", None)
                    
                    setattr(item, "Item50", self)
                    

    @property
    def forcedDeletedIfDeleted(self):
        return self.__forcedDeletedIfDeleted

    @forcedDeletedIfDeleted.setter
    def forcedDeletedIfDeleted(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_data_Item__forcedDeletedIfDeleted", None)
        self.__forcedDeletedIfDeleted = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Item53"):
                    opp_val = getattr(item, "Item53", None)
                    
                    if opp_val == self:
                        setattr(item, "Item53", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Item53"):
                    opp_val = getattr(item, "Item53", None)
                    
                    setattr(item, "Item53", self)
                    

    @property
    def Item(self):
        return self.__Item

    @Item.setter
    def Item(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_data_Item__Item", None)
        self.__Item = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dataSet"):
                opp_val = getattr(old_value, "dataSet", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dataSet"):
                opp_val = getattr(value, "dataSet", None)
                if opp_val is None:
                    setattr(value, "dataSet", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def metaTagged(self):
        return self.__metaTagged

    @metaTagged.setter
    def metaTagged(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_data_Item__metaTagged", None)
        self.__metaTagged = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "MetaTag"):
                    opp_val = getattr(item, "MetaTag", None)
                    
                    if opp_val == self:
                        setattr(item, "MetaTag", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "MetaTag"):
                    opp_val = getattr(item, "MetaTag", None)
                    
                    setattr(item, "MetaTag", self)
                    

    @property
    def deletedIfDeleted(self):
        return self.__deletedIfDeleted

    @deletedIfDeleted.setter
    def deletedIfDeleted(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_data_Item__deletedIfDeleted", None)
        self.__deletedIfDeleted = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Item47"):
                    opp_val = getattr(item, "Item47", None)
                    
                    if opp_val == self:
                        setattr(item, "Item47", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Item47"):
                    opp_val = getattr(item, "Item47", None)
                    
                    setattr(item, "Item47", self)
                    

    @property
    def Item107(self):
        return self.__Item107

    @Item107.setter
    def Item107(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_data_Item__Item107", None)
        self.__Item107 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "identifiedBy"):
                opp_val = getattr(old_value, "identifiedBy", None)
                if opp_val == self:
                    setattr(old_value, "identifiedBy", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "identifiedBy"):
                opp_val = getattr(value, "identifiedBy", None)
                setattr(value, "identifiedBy", self)

    @property
    def Item80(self):
        return self.__Item80

    @Item80.setter
    def Item80(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_data_Item__Item80", None)
        self.__Item80 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "metaTags"):
                opp_val = getattr(old_value, "metaTags", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "metaTags"):
                opp_val = getattr(value, "metaTags", None)
                if opp_val is None:
                    setattr(value, "metaTags", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def forcedDeleteOnDelete(self):
        return self.__forcedDeleteOnDelete

    @forcedDeleteOnDelete.setter
    def forcedDeleteOnDelete(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_data_Item__forcedDeleteOnDelete", None)
        self.__forcedDeleteOnDelete = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Item56"):
                    opp_val = getattr(item, "Item56", None)
                    
                    if opp_val == self:
                        setattr(item, "Item56", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Item56"):
                    opp_val = getattr(item, "Item56", None)
                    
                    setattr(item, "Item56", self)
                    

    @property
    def Item50(self):
        return self.__Item50

    @Item50.setter
    def Item50(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_data_Item__Item50", None)
        self.__Item50 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "deleteOnDelete"):
                opp_val = getattr(old_value, "deleteOnDelete", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "deleteOnDelete"):
                opp_val = getattr(value, "deleteOnDelete", None)
                if opp_val is None:
                    setattr(value, "deleteOnDelete", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Item47(self):
        return self.__Item47

    @Item47.setter
    def Item47(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_data_Item__Item47", None)
        self.__Item47 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "deletedIfDeleted"):
                opp_val = getattr(old_value, "deletedIfDeleted", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "deletedIfDeleted"):
                opp_val = getattr(value, "deletedIfDeleted", None)
                if opp_val is None:
                    setattr(value, "deletedIfDeleted", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Item53(self):
        return self.__Item53

    @Item53.setter
    def Item53(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_data_Item__Item53", None)
        self.__Item53 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "forcedDeletedIfDeleted"):
                opp_val = getattr(old_value, "forcedDeletedIfDeleted", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "forcedDeletedIfDeleted"):
                opp_val = getattr(value, "forcedDeletedIfDeleted", None)
                if opp_val is None:
                    setattr(value, "forcedDeletedIfDeleted", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def identifyBy(self, key: str, value: str) -> str:
        # TODO: Implement identifyBy method
        pass

    def log(self, message: str):
        # TODO: Implement log method
        pass

    def delete(self):
        # TODO: Implement delete method
        pass

    def deleteOnDeleteOf(self, item: Item) -> Item:
        # TODO: Implement deleteOnDeleteOf method
        pass

    def update(self, item: Item) -> Item:
        # TODO: Implement update method
        pass

    def getCreatedPretty(self) -> str:
        # TODO: Implement getCreatedPretty method
        pass

    def getLastModifiedPrettyInLanguage(self, language: str) -> str:
        # TODO: Implement getLastModifiedPrettyInLanguage method
        pass

    def forceUpdate(self, item: Item) -> Item:
        # TODO: Implement forceUpdate method
        pass

    def matchesSearch(self, term: str) -> str:
        # TODO: Implement matchesSearch method
        pass

    def forceDeleteOnDeleteOf(self, item: Item) -> Item:
        # TODO: Implement forceDeleteOnDeleteOf method
        pass

    def getLastModifiedPretty(self) -> str:
        # TODO: Implement getLastModifiedPretty method
        pass

    def getIdentifier(self, key: str) -> str:
        # TODO: Implement getIdentifier method
        pass

    def getCreatedPrettyInLanguage(self, language: str) -> str:
        # TODO: Implement getCreatedPrettyInLanguage method
        pass

    def log(self, level: str, message: str):
        # TODO: Implement log method
        pass

    def metaTag(self, name: str) -> str:
        # TODO: Implement metaTag method
        pass

    def isEqualItem(self, item: Item) -> str:
        # TODO: Implement isEqualItem method
        pass

    def hasMetaTag(self, tag: str) -> str:
        # TODO: Implement hasMetaTag method
        pass

    def unMetaTag(self, name: str) -> str:
        # TODO: Implement unMetaTag method
        pass

    def deleteIfEmptyOnDelete(self):
        # TODO: Implement deleteIfEmptyOnDelete method
        pass

    def removeIdentifier(self, key: str) -> str:
        # TODO: Implement removeIdentifier method
        pass

class data_Mashup:

    pass
class data_DataSet:

    def __init__(self, cacheFileAttachements: str, lastModified: date, logLevel: str, identCounter: str, identPrefix: str, created: date, keepDeletedItemsList: str, cacheFolder: str, data_DataSet: "data_Mashup" = None, data_DataSet41: set["data_DeletedItem"] = None, dataSet: set["data_Item"] = None, DataSet: "data_Item" = None):
        self.cacheFileAttachements = cacheFileAttachements
        self.lastModified = lastModified
        self.logLevel = logLevel
        self.identCounter = identCounter
        self.identPrefix = identPrefix
        self.created = created
        self.keepDeletedItemsList = keepDeletedItemsList
        self.cacheFolder = cacheFolder
        self.data_DataSet = data_DataSet
        self.data_DataSet41 = data_DataSet41 if data_DataSet41 is not None else set()
        self.dataSet = dataSet if dataSet is not None else set()
        self.DataSet = DataSet
        
    @property
    def cacheFolder(self) -> str:
        return self.__cacheFolder

    @cacheFolder.setter
    def cacheFolder(self, cacheFolder: str):
        self.__cacheFolder = cacheFolder

    @property
    def cacheFileAttachements(self) -> str:
        return self.__cacheFileAttachements

    @cacheFileAttachements.setter
    def cacheFileAttachements(self, cacheFileAttachements: str):
        self.__cacheFileAttachements = cacheFileAttachements

    @property
    def identPrefix(self) -> str:
        return self.__identPrefix

    @identPrefix.setter
    def identPrefix(self, identPrefix: str):
        self.__identPrefix = identPrefix

    @property
    def keepDeletedItemsList(self) -> str:
        return self.__keepDeletedItemsList

    @keepDeletedItemsList.setter
    def keepDeletedItemsList(self, keepDeletedItemsList: str):
        self.__keepDeletedItemsList = keepDeletedItemsList

    @property
    def identCounter(self) -> str:
        return self.__identCounter

    @identCounter.setter
    def identCounter(self, identCounter: str):
        self.__identCounter = identCounter

    @property
    def lastModified(self) -> date:
        return self.__lastModified

    @lastModified.setter
    def lastModified(self, lastModified: date):
        self.__lastModified = lastModified

    @property
    def created(self) -> date:
        return self.__created

    @created.setter
    def created(self, created: date):
        self.__created = created

    @property
    def logLevel(self) -> str:
        return self.__logLevel

    @logLevel.setter
    def logLevel(self, logLevel: str):
        self.__logLevel = logLevel

    @property
    def data_DataSet41(self):
        return self.__data_DataSet41

    @data_DataSet41.setter
    def data_DataSet41(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_data_DataSet__data_DataSet41", None)
        self.__data_DataSet41 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "data_DeletedItem"):
                    opp_val = getattr(item, "data_DeletedItem", None)
                    
                    if opp_val == self:
                        setattr(item, "data_DeletedItem", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "data_DeletedItem"):
                    opp_val = getattr(item, "data_DeletedItem", None)
                    
                    setattr(item, "data_DeletedItem", self)
                    

    @property
    def dataSet(self):
        return self.__dataSet

    @dataSet.setter
    def dataSet(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_data_DataSet__dataSet", None)
        self.__dataSet = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Item"):
                    opp_val = getattr(item, "Item", None)
                    
                    if opp_val == self:
                        setattr(item, "Item", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Item"):
                    opp_val = getattr(item, "Item", None)
                    
                    setattr(item, "Item", self)
                    

    @property
    def DataSet(self):
        return self.__DataSet

    @DataSet.setter
    def DataSet(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_data_DataSet__DataSet", None)
        self.__DataSet = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "items"):
                opp_val = getattr(old_value, "items", None)
                if opp_val == self:
                    setattr(old_value, "items", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "items"):
                opp_val = getattr(value, "items", None)
                setattr(value, "items", self)

    @property
    def data_DataSet(self):
        return self.__data_DataSet

    @data_DataSet.setter
    def data_DataSet(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_data_DataSet__data_DataSet", None)
        self.__data_DataSet = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "data_Mashup"):
                opp_val = getattr(old_value, "data_Mashup", None)
                if opp_val == self:
                    setattr(old_value, "data_Mashup", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "data_Mashup"):
                opp_val = getattr(value, "data_Mashup", None)
                setattr(value, "data_Mashup", self)

    def getEventsAfter(self, date: date) -> str:
        # TODO: Implement getEventsAfter method
        pass

    def getItemsWithIdent(self, ident: str) -> Item:
        # TODO: Implement getItemsWithIdent method
        pass

    def getInformationObjectsWithOneOfTags(self, tags: str) -> InformationObject:
        # TODO: Implement getInformationObjectsWithOneOfTags method
        pass

    def getInformationObjectsWithAttachment(self, attachment: str) -> InformationObject:
        # TODO: Implement getInformationObjectsWithAttachment method
        pass

    def getTagsWithMoreThanXInformationObjects(self, x: str) -> str:
        # TODO: Implement getTagsWithMoreThanXInformationObjects method
        pass

    def getViewRankings(self) -> str:
        # TODO: Implement getViewRankings method
        pass

    def getContents(self) -> str:
        # TODO: Implement getContents method
        pass

    def getIdentsOfItemsDeletedSince(self, date: date) -> str:
        # TODO: Implement getIdentsOfItemsDeletedSince method
        pass

    def getBinaries(self) -> str:
        # TODO: Implement getBinaries method
        pass

    def getItemsExceptIdentifiersCreatedSince(self, date: date) -> Item:
        # TODO: Implement getItemsExceptIdentifiersCreatedSince method
        pass

    def getIdentifiersWithKey(self, key: str) -> str:
        # TODO: Implement getIdentifiersWithKey method
        pass

    def getOrganisationsWithName(self, name: str) -> str:
        # TODO: Implement getOrganisationsWithName method
        pass

    def getAttachmentsWithCachedFileName(self, cachedFileName: str) -> str:
        # TODO: Implement getAttachmentsWithCachedFileName method
        pass

    def getPersonsWithOneOfTags(self, tags: str) -> str:
        # TODO: Implement getPersonsWithOneOfTags method
        pass

    def getStarRankings(self) -> str:
        # TODO: Implement getStarRankings method
        pass

    def getRandomXContents(self, x: str) -> str:
        # TODO: Implement getRandomXContents method
        pass

    def getOrganisations(self) -> str:
        # TODO: Implement getOrganisations method
        pass

    def getCitations(self) -> str:
        # TODO: Implement getCitations method
        pass

    def getVideos(self) -> str:
        # TODO: Implement getVideos method
        pass

    def getIdentifierWithKeyValue(self, key: str, value: str) -> str:
        # TODO: Implement getIdentifierWithKeyValue method
        pass

    def getInformationObjectsWithAllMetaTags(self, tags: str) -> InformationObject:
        # TODO: Implement getInformationObjectsWithAllMetaTags method
        pass

    def getWebSites(self) -> str:
        # TODO: Implement getWebSites method
        pass

    def getClassifications(self) -> str:
        # TODO: Implement getClassifications method
        pass

    def getRankings(self) -> str:
        # TODO: Implement getRankings method
        pass

    def getDocuments(self) -> str:
        # TODO: Implement getDocuments method
        pass

    def getAttachments(self) -> str:
        # TODO: Implement getAttachments method
        pass

    def getOrganisationsWithOneOfCategories(self, categories: str) -> str:
        # TODO: Implement getOrganisationsWithOneOfCategories method
        pass

    def getIdentsOfExistingItems(self) -> str:
        # TODO: Implement getIdentsOfExistingItems method
        pass

    def getWebAccounts(self) -> str:
        # TODO: Implement getWebAccounts method
        pass

    def getItemsWithStringValue(self, stringValue: str) -> Item:
        # TODO: Implement getItemsWithStringValue method
        pass

    def getItemsExceptIdentifiers(self) -> Item:
        # TODO: Implement getItemsExceptIdentifiers method
        pass

    def getOrganisationWithIdent(self, ident: str) -> str:
        # TODO: Implement getOrganisationWithIdent method
        pass

    def getIndoorLocations(self) -> str:
        # TODO: Implement getIndoorLocations method
        pass

    def getInformationObjectsWithOneOfMetaTags(self, tags: str) -> InformationObject:
        # TODO: Implement getInformationObjectsWithOneOfMetaTags method
        pass

    def getAllOrganisations(self) -> str:
        # TODO: Implement getAllOrganisations method
        pass

    def getIndoorLocationWithIdentifier(self, key: str, value: str) -> str:
        # TODO: Implement getIndoorLocationWithIdentifier method
        pass

    def getRandomXInformationObjects(self, x: str) -> InformationObject:
        # TODO: Implement getRandomXInformationObjects method
        pass

    def log(self, message: str, level: str):
        # TODO: Implement log method
        pass

    def getLocations(self) -> str:
        # TODO: Implement getLocations method
        pass

    def getPhones(self) -> str:
        # TODO: Implement getPhones method
        pass

    def getAllContents(self) -> str:
        # TODO: Implement getAllContents method
        pass

    def getEvents(self) -> str:
        # TODO: Implement getEvents method
        pass

    def getContentsWithAllCategories(self, categories: str) -> str:
        # TODO: Implement getContentsWithAllCategories method
        pass

    def getInformationObjects(self) -> InformationObject:
        # TODO: Implement getInformationObjects method
        pass

    def getPersonsWithAllMetaTags(self, tags: str) -> str:
        # TODO: Implement getPersonsWithAllMetaTags method
        pass

    def hasEqualItem(self, item: Item) -> str:
        # TODO: Implement hasEqualItem method
        pass

    def getOrganisationsWithAllMetaTags(self, tags: str) -> str:
        # TODO: Implement getOrganisationsWithAllMetaTags method
        pass

    def forceAdd(self, item: Item) -> Item:
        # TODO: Implement forceAdd method
        pass

    def getItemsWithOneOfMetaTags(self, tags: str) -> Item:
        # TODO: Implement getItemsWithOneOfMetaTags method
        pass

    def getInstantMessengers(self) -> str:
        # TODO: Implement getInstantMessengers method
        pass

    def clearDeletedItemsList(self) -> str:
        # TODO: Implement clearDeletedItemsList method
        pass

    def getContentsWithName(self, name: str) -> str:
        # TODO: Implement getContentsWithName method
        pass

    def getMetaTags(self) -> str:
        # TODO: Implement getMetaTags method
        pass

    def getInformationObjectsWithAllTags(self, tags: str) -> InformationObject:
        # TODO: Implement getInformationObjectsWithAllTags method
        pass

    def add(self, item: Item) -> Item:
        # TODO: Implement add method
        pass

    def getInformationObjectsWithOneOfCategories(self, categories: str) -> InformationObject:
        # TODO: Implement getInformationObjectsWithOneOfCategories method
        pass

    def getEqualItems(self, item: Item) -> Item:
        # TODO: Implement getEqualItems method
        pass

    def getTags(self) -> str:
        # TODO: Implement getTags method
        pass

    def getItemsExceptIdentifiersModifiedSince(self, date: date) -> Item:
        # TODO: Implement getItemsExceptIdentifiersModifiedSince method
        pass

    def getImageWithIdentifier(self, key: str, value: str) -> str:
        # TODO: Implement getImageWithIdentifier method
        pass

    def getContentsWithAllMetaTags(self, tags: str) -> str:
        # TODO: Implement getContentsWithAllMetaTags method
        pass

    def getEventsBetweenDates(self, before: date, after: date) -> str:
        # TODO: Implement getEventsBetweenDates method
        pass

    def getOrganisationsWithOneOfMetaTags(self, tags: str) -> str:
        # TODO: Implement getOrganisationsWithOneOfMetaTags method
        pass

    def getMetaInformations(self) -> str:
        # TODO: Implement getMetaInformations method
        pass

    def getMetaTag(self, name: str) -> str:
        # TODO: Implement getMetaTag method
        pass

    def getImages(self) -> str:
        # TODO: Implement getImages method
        pass

    def getOrganisationsWithAllTags(self, tags: str) -> str:
        # TODO: Implement getOrganisationsWithAllTags method
        pass

    def getContentsWithAttachment(self, attachment: str) -> str:
        # TODO: Implement getContentsWithAttachment method
        pass

    def getOrganisationsWithAttachment(self, attachment: str) -> str:
        # TODO: Implement getOrganisationsWithAttachment method
        pass

    def getInformationObjectsModifiedSince(self, date: date) -> InformationObject:
        # TODO: Implement getInformationObjectsModifiedSince method
        pass

    def getIdentifiers(self) -> str:
        # TODO: Implement getIdentifiers method
        pass

    def getRandomXOrganisations(self, x: str) -> str:
        # TODO: Implement getRandomXOrganisations method
        pass

    def getPersonWithIdent(self, ident: str) -> str:
        # TODO: Implement getPersonWithIdent method
        pass

    def getRandomXPersons(self, x: str) -> str:
        # TODO: Implement getRandomXPersons method
        pass

    def getItemsCreatedSince(self, date: date) -> Item:
        # TODO: Implement getItemsCreatedSince method
        pass

    def reloadAllAttachmentFiles(self) -> str:
        # TODO: Implement reloadAllAttachmentFiles method
        pass

    def log(self, message: str):
        # TODO: Implement log method
        pass

    def getContentWithIdentifier(self, key: str, value: str) -> str:
        # TODO: Implement getContentWithIdentifier method
        pass

    def getContentsWithOneOfTags(self, tags: str) -> str:
        # TODO: Implement getContentsWithOneOfTags method
        pass

    def getDeletedItems(self) -> str:
        # TODO: Implement getDeletedItems method
        pass

    def getCategory(self, name: str) -> str:
        # TODO: Implement getCategory method
        pass

    def getExtensions(self) -> str:
        # TODO: Implement getExtensions method
        pass

    def getThumbRankings(self) -> str:
        # TODO: Implement getThumbRankings method
        pass

    def getItemsWithAllMetaTags(self, tags: str) -> Item:
        # TODO: Implement getItemsWithAllMetaTags method
        pass

    def getAllMetaTags(self) -> str:
        # TODO: Implement getAllMetaTags method
        pass

    def getItemsDeletedSince(self, date: date) -> str:
        # TODO: Implement getItemsDeletedSince method
        pass

    def getPersonsWithOneOfCategories(self, categories: str) -> str:
        # TODO: Implement getPersonsWithOneOfCategories method
        pass

    def getTag(self, name: str) -> str:
        # TODO: Implement getTag method
        pass

    def getOrganisationsWithOneOfTags(self, tags: str) -> str:
        # TODO: Implement getOrganisationsWithOneOfTags method
        pass

    def getAllCategories(self) -> str:
        # TODO: Implement getAllCategories method
        pass

    def searchByQuery(self, query: str) -> Item:
        # TODO: Implement searchByQuery method
        pass

    def getContentWithIdent(self, ident: str) -> str:
        # TODO: Implement getContentWithIdent method
        pass

    def getCategories(self) -> str:
        # TODO: Implement getCategories method
        pass

    def getLocationWithIdentifier(self, value: str, key: str) -> str:
        # TODO: Implement getLocationWithIdentifier method
        pass

    def getPersonsWithFirstName(self, firstname: str) -> str:
        # TODO: Implement getPersonsWithFirstName method
        pass

    def getAllPersons(self) -> str:
        # TODO: Implement getAllPersons method
        pass

    def getAllTags(self) -> str:
        # TODO: Implement getAllTags method
        pass

    def getPersons(self) -> str:
        # TODO: Implement getPersons method
        pass

    def getPersonsWithAllTags(self, tags: str) -> str:
        # TODO: Implement getPersonsWithAllTags method
        pass

    def getEmails(self) -> str:
        # TODO: Implement getEmails method
        pass

    def getPersonsWithOneOfMetaTags(self, tags: str) -> str:
        # TODO: Implement getPersonsWithOneOfMetaTags method
        pass

    def getPersonsWithLastname(self, lastname: str) -> str:
        # TODO: Implement getPersonsWithLastname method
        pass

    def getConnections(self) -> str:
        # TODO: Implement getConnections method
        pass

    def getSpicynodesRepresentation(self) -> str:
        # TODO: Implement getSpicynodesRepresentation method
        pass

    def getEventsBefore(self, date: date) -> str:
        # TODO: Implement getEventsBefore method
        pass

    def getItemsModifiedSince(self, date: date) -> Item:
        # TODO: Implement getItemsModifiedSince method
        pass

    def getOrganisationsWithAllCategories(self, categories: str) -> str:
        # TODO: Implement getOrganisationsWithAllCategories method
        pass

    def getCategoryWithSlug(self, slug: str) -> str:
        # TODO: Implement getCategoryWithSlug method
        pass

    def getPersonsWithAllCategories(self, categories: str) -> str:
        # TODO: Implement getPersonsWithAllCategories method
        pass

    def searchItems(self, term: str) -> Item:
        # TODO: Implement searchItems method
        pass

    def rebuildIndexes(self):
        # TODO: Implement rebuildIndexes method
        pass

    def getPersonsWithAttachment(self, attachment: str) -> str:
        # TODO: Implement getPersonsWithAttachment method
        pass

    def getTransformations(self) -> str:
        # TODO: Implement getTransformations method
        pass

    def getContentsWithOneOfMetaTags(self, tags: str) -> str:
        # TODO: Implement getContentsWithOneOfMetaTags method
        pass

    def getInformationObjectsWithAllCategories(self, categories: str) -> InformationObject:
        # TODO: Implement getInformationObjectsWithAllCategories method
        pass

    def getIdentsOfDeletedItems(self) -> str:
        # TODO: Implement getIdentsOfDeletedItems method
        pass

    def getOrganisationWithIdentifier(self, key: str, value: str) -> str:
        # TODO: Implement getOrganisationWithIdentifier method
        pass

    def getConnectionsBetweenInformationObjectsOfDifferentCategories(self) -> str:
        # TODO: Implement getConnectionsBetweenInformationObjectsOfDifferentCategories method
        pass

    def searchInformationObjects(self, term: str) -> InformationObject:
        # TODO: Implement searchInformationObjects method
        pass

    def getItemWithIdentifier(self, key: str, value: str) -> Item:
        # TODO: Implement getItemWithIdentifier method
        pass

    def getPersonsWithName(self, name: str) -> str:
        # TODO: Implement getPersonsWithName method
        pass

    def getContentsWithOneOfCategories(self, categories: str) -> str:
        # TODO: Implement getContentsWithOneOfCategories method
        pass

    def getAttachmentWithIdent(self, ident: str) -> str:
        # TODO: Implement getAttachmentWithIdent method
        pass

    def getAllConnections(self) -> str:
        # TODO: Implement getAllConnections method
        pass

    def getContentsWithAllTags(self, tags: str) -> str:
        # TODO: Implement getContentsWithAllTags method
        pass

    def getEmptyItemWithIdent(self, ident: str) -> Item:
        # TODO: Implement getEmptyItemWithIdent method
        pass

    def getPersonWithIdentifier(self, key: str, value: str) -> str:
        # TODO: Implement getPersonWithIdentifier method
        pass

class data_Video(Attachment):

    pass
class data_Transformation(Attachment):

    pass
class data_Document(Attachment):

    pass
class data_MetaInformation(Extension):

    pass
class data_Binary(Attachment):

    def __init__(self, bytes: str, data_Binary: "data_InformationObject" = None):
        self.bytes = bytes
        self.data_Binary = data_Binary
        
    @property
    def bytes(self) -> str:
        return self.__bytes

    @bytes.setter
    def bytes(self, bytes: str):
        self.__bytes = bytes

    @property
    def data_Binary(self):
        return self.__data_Binary

    @data_Binary.setter
    def data_Binary(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_data_Binary__data_Binary", None)
        self.__data_Binary = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "data_InformationObject21"):
                opp_val = getattr(old_value, "data_InformationObject21", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "data_InformationObject21"):
                opp_val = getattr(value, "data_InformationObject21", None)
                if opp_val is None:
                    setattr(value, "data_InformationObject21", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class data_Connection(Extension):

    pass
class data_ViewRanking(Ranking):

    pass
class data_ThumbRanking(Ranking):

    def __init__(self, ThumbRanking: "data_InformationObject" = None, thumbRankings: "data_InformationObject" = None):
        self.ThumbRanking = ThumbRanking
        self.thumbRankings = thumbRankings
        
    @property
    def ThumbRanking(self):
        return self.__ThumbRanking

    @ThumbRanking.setter
    def ThumbRanking(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_data_ThumbRanking__ThumbRanking", None)
        self.__ThumbRanking = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rankedInformationObject14"):
                opp_val = getattr(old_value, "rankedInformationObject14", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rankedInformationObject14"):
                opp_val = getattr(value, "rankedInformationObject14", None)
                if opp_val is None:
                    setattr(value, "rankedInformationObject14", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def thumbRankings(self):
        return self.__thumbRankings

    @thumbRankings.setter
    def thumbRankings(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_data_ThumbRanking__thumbRankings", None)
        self.__thumbRankings = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "InformationObject89"):
                opp_val = getattr(old_value, "InformationObject89", None)
                if opp_val == self:
                    setattr(old_value, "InformationObject89", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "InformationObject89"):
                opp_val = getattr(value, "InformationObject89", None)
                setattr(value, "InformationObject89", self)

    def isThumbDown(self) -> str:
        # TODO: Implement isThumbDown method
        pass

    def isThumbUp(self) -> str:
        # TODO: Implement isThumbUp method
        pass

class data_StarRanking(Ranking):

    def __init__(self, normalizedValue: str, StarRanking: "data_InformationObject" = None, starRankings: "data_InformationObject" = None):
        self.normalizedValue = normalizedValue
        self.StarRanking = StarRanking
        self.starRankings = starRankings
        
    @property
    def normalizedValue(self) -> str:
        return self.__normalizedValue

    @normalizedValue.setter
    def normalizedValue(self, normalizedValue: str):
        self.__normalizedValue = normalizedValue

    @property
    def starRankings(self):
        return self.__starRankings

    @starRankings.setter
    def starRankings(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_data_StarRanking__starRankings", None)
        self.__starRankings = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "InformationObject85"):
                opp_val = getattr(old_value, "InformationObject85", None)
                if opp_val == self:
                    setattr(old_value, "InformationObject85", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "InformationObject85"):
                opp_val = getattr(value, "InformationObject85", None)
                setattr(value, "InformationObject85", self)

    @property
    def StarRanking(self):
        return self.__StarRanking

    @StarRanking.setter
    def StarRanking(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_data_StarRanking__StarRanking", None)
        self.__StarRanking = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rankedInformationObject"):
                opp_val = getattr(old_value, "rankedInformationObject", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rankedInformationObject"):
                opp_val = getattr(value, "rankedInformationObject", None)
                if opp_val is None:
                    setattr(value, "rankedInformationObject", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class data_Image(Attachment):

    def __init__(self, width: str, height: str, data_Image: "data_InformationObject" = None):
        self.width = width
        self.height = height
        self.data_Image = data_Image
        
    @property
    def height(self) -> str:
        return self.__height

    @height.setter
    def height(self, height: str):
        self.__height = height

    @property
    def width(self) -> str:
        return self.__width

    @width.setter
    def width(self, width: str):
        self.__width = width

    @property
    def data_Image(self):
        return self.__data_Image

    @data_Image.setter
    def data_Image(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_data_Image__data_Image", None)
        self.__data_Image = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "data_InformationObject"):
                opp_val = getattr(old_value, "data_InformationObject", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "data_InformationObject"):
                opp_val = getattr(value, "data_InformationObject", None)
                if opp_val is None:
                    setattr(value, "data_InformationObject", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class data_Tag(Classification):

    pass
class data_Category(Classification):

    pass
class Item:

    pass
class data_Classification(Item):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    def getOrganisations(self) -> str:
        # TODO: Implement getOrganisations method
        pass

    def getContentsCount(self) -> str:
        # TODO: Implement getContentsCount method
        pass

    def getOrganisationsCount(self) -> str:
        # TODO: Implement getOrganisationsCount method
        pass

    def getContents(self) -> str:
        # TODO: Implement getContents method
        pass

    def getSlug(self) -> str:
        # TODO: Implement getSlug method
        pass

    def getCount(self) -> str:
        # TODO: Implement getCount method
        pass

    def getPersons(self) -> str:
        # TODO: Implement getPersons method
        pass

    def getPersonsCount(self) -> str:
        # TODO: Implement getPersonsCount method
        pass

class data_Identifier(Item):

    def __init__(self, key: str, value: str, Identifier: "data_Item" = None, identifiedBy: "data_Item" = None):
        self.key = key
        self.value = value
        self.Identifier = Identifier
        self.identifiedBy = identifiedBy
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def key(self) -> str:
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key

    @property
    def Identifier(self):
        return self.__Identifier

    @Identifier.setter
    def Identifier(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_data_Identifier__Identifier", None)
        self.__Identifier = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "identified"):
                opp_val = getattr(old_value, "identified", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "identified"):
                opp_val = getattr(value, "identified", None)
                if opp_val is None:
                    setattr(value, "identified", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def identifiedBy(self):
        return self.__identifiedBy

    @identifiedBy.setter
    def identifiedBy(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_data_Identifier__identifiedBy", None)
        self.__identifiedBy = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Item107"):
                opp_val = getattr(old_value, "Item107", None)
                if opp_val == self:
                    setattr(old_value, "Item107", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Item107"):
                opp_val = getattr(value, "Item107", None)
                setattr(value, "Item107", self)

class data_DeletedItem(Item):

    def __init__(self, deleted: date, identOfDeleted: str, data_DeletedItem: "data_DataSet" = None):
        self.deleted = deleted
        self.identOfDeleted = identOfDeleted
        self.data_DeletedItem = data_DeletedItem
        
    @property
    def deleted(self) -> date:
        return self.__deleted

    @deleted.setter
    def deleted(self, deleted: date):
        self.__deleted = deleted

    @property
    def identOfDeleted(self) -> str:
        return self.__identOfDeleted

    @identOfDeleted.setter
    def identOfDeleted(self, identOfDeleted: str):
        self.__identOfDeleted = identOfDeleted

    @property
    def data_DeletedItem(self):
        return self.__data_DeletedItem

    @data_DeletedItem.setter
    def data_DeletedItem(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_data_DeletedItem__data_DeletedItem", None)
        self.__data_DeletedItem = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "data_DataSet41"):
                opp_val = getattr(old_value, "data_DataSet41", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "data_DataSet41"):
                opp_val = getattr(value, "data_DataSet41", None)
                if opp_val is None:
                    setattr(value, "data_DataSet41", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class data_Extension(Item):

    def __init__(self):
        
    def tag(self, name: str) -> str:
        # TODO: Implement tag method
        pass

class data_MetaTag(Item):

    def __init__(self, name: str, MetaTag: "data_Item" = None, metaTags: set["data_Item"] = None):
        self.name = name
        self.MetaTag = MetaTag
        self.metaTags = metaTags if metaTags is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def MetaTag(self):
        return self.__MetaTag

    @MetaTag.setter
    def MetaTag(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_data_MetaTag__MetaTag", None)
        self.__MetaTag = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "metaTagged"):
                opp_val = getattr(old_value, "metaTagged", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "metaTagged"):
                opp_val = getattr(value, "metaTagged", None)
                if opp_val is None:
                    setattr(value, "metaTagged", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def metaTags(self):
        return self.__metaTags

    @metaTags.setter
    def metaTags(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_data_MetaTag__metaTags", None)
        self.__metaTags = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Item80"):
                    opp_val = getattr(item, "Item80", None)
                    
                    if opp_val == self:
                        setattr(item, "Item80", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Item80"):
                    opp_val = getattr(item, "Item80", None)
                    
                    setattr(item, "Item80", self)
                    

    def getInformationObjectsCount(self) -> str:
        # TODO: Implement getInformationObjectsCount method
        pass

    def getExtensions(self) -> str:
        # TODO: Implement getExtensions method
        pass

    def getCount(self) -> str:
        # TODO: Implement getCount method
        pass

    def getInformationObjects(self) -> InformationObject:
        # TODO: Implement getInformationObjects method
        pass

    def getWebAccounts(self) -> str:
        # TODO: Implement getWebAccounts method
        pass

class data_InformationObject(Item):

    def __init__(self, name: str, alternativeNames: str, verifiedName: str, categorized: set["data_Category"] = None, tagged: set["data_Tag"] = None, data_InformationObject: set["data_Image"] = None, rankedInformationObject: set["data_StarRanking"] = None, rankedInformationObject14: set["data_ThumbRanking"] = None, rankedInformationObject16: set["data_ViewRanking"] = None, from: set["data_Connection"] = None, to: set["data_Connection"] = None, data_InformationObject21: set["data_Binary"] = None, mainCategorized: "data_Category" = None, informationObjects: set["data_MetaInformation"] = None, InformationObject: "data_Category" = None, InformationObject66: "data_Category" = None, InformationObject68: "data_Tag" = None, InformationObject85: "data_StarRanking" = None, InformationObject87: "data_ViewRanking" = None, InformationObject89: "data_ThumbRanking" = None, InformationObject93: "data_Connection" = None, InformationObject95: "data_Connection" = None, InformationObject97: "data_MetaInformation" = None):
        self.name = name
        self.alternativeNames = alternativeNames
        self.verifiedName = verifiedName
        self.categorized = categorized if categorized is not None else set()
        self.tagged = tagged if tagged is not None else set()
        self.data_InformationObject = data_InformationObject if data_InformationObject is not None else set()
        self.rankedInformationObject = rankedInformationObject if rankedInformationObject is not None else set()
        self.rankedInformationObject14 = rankedInformationObject14 if rankedInformationObject14 is not None else set()
        self.rankedInformationObject16 = rankedInformationObject16 if rankedInformationObject16 is not None else set()
        self.from = from if from is not None else set()
        self.to = to if to is not None else set()
        self.data_InformationObject21 = data_InformationObject21 if data_InformationObject21 is not None else set()
        self.mainCategorized = mainCategorized
        self.informationObjects = informationObjects if informationObjects is not None else set()
        self.InformationObject = InformationObject
        self.InformationObject66 = InformationObject66
        self.InformationObject68 = InformationObject68
        self.InformationObject85 = InformationObject85
        self.InformationObject87 = InformationObject87
        self.InformationObject89 = InformationObject89
        self.InformationObject93 = InformationObject93
        self.InformationObject95 = InformationObject95
        self.InformationObject97 = InformationObject97
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def alternativeNames(self) -> str:
        return self.__alternativeNames

    @alternativeNames.setter
    def alternativeNames(self, alternativeNames: str):
        self.__alternativeNames = alternativeNames

    @property
    def verifiedName(self) -> str:
        return self.__verifiedName

    @verifiedName.setter
    def verifiedName(self, verifiedName: str):
        self.__verifiedName = verifiedName

    @property
    def InformationObject93(self):
        return self.__InformationObject93

    @InformationObject93.setter
    def InformationObject93(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_data_InformationObject__InformationObject93", None)
        self.__InformationObject93 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "connectedTo"):
                opp_val = getattr(old_value, "connectedTo", None)
                if opp_val == self:
                    setattr(old_value, "connectedTo", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "connectedTo"):
                opp_val = getattr(value, "connectedTo", None)
                setattr(value, "connectedTo", self)

    @property
    def rankedInformationObject(self):
        return self.__rankedInformationObject

    @rankedInformationObject.setter
    def rankedInformationObject(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_data_InformationObject__rankedInformationObject", None)
        self.__rankedInformationObject = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "StarRanking"):
                    opp_val = getattr(item, "StarRanking", None)
                    
                    if opp_val == self:
                        setattr(item, "StarRanking", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "StarRanking"):
                    opp_val = getattr(item, "StarRanking", None)
                    
                    setattr(item, "StarRanking", self)
                    

    @property
    def informationObjects(self):
        return self.__informationObjects

    @informationObjects.setter
    def informationObjects(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_data_InformationObject__informationObjects", None)
        self.__informationObjects = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "MetaInformation"):
                    opp_val = getattr(item, "MetaInformation", None)
                    
                    if opp_val == self:
                        setattr(item, "MetaInformation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "MetaInformation"):
                    opp_val = getattr(item, "MetaInformation", None)
                    
                    setattr(item, "MetaInformation", self)
                    

    @property
    def InformationObject89(self):
        return self.__InformationObject89

    @InformationObject89.setter
    def InformationObject89(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_data_InformationObject__InformationObject89", None)
        self.__InformationObject89 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "thumbRankings"):
                opp_val = getattr(old_value, "thumbRankings", None)
                if opp_val == self:
                    setattr(old_value, "thumbRankings", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "thumbRankings"):
                opp_val = getattr(value, "thumbRankings", None)
                setattr(value, "thumbRankings", self)

    @property
    def rankedInformationObject16(self):
        return self.__rankedInformationObject16

    @rankedInformationObject16.setter
    def rankedInformationObject16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_data_InformationObject__rankedInformationObject16", None)
        self.__rankedInformationObject16 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ViewRanking"):
                    opp_val = getattr(item, "ViewRanking", None)
                    
                    if opp_val == self:
                        setattr(item, "ViewRanking", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ViewRanking"):
                    opp_val = getattr(item, "ViewRanking", None)
                    
                    setattr(item, "ViewRanking", self)
                    

    @property
    def InformationObject(self):
        return self.__InformationObject

    @InformationObject.setter
    def InformationObject(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_data_InformationObject__InformationObject", None)
        self.__InformationObject = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "categories"):
                opp_val = getattr(old_value, "categories", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "categories"):
                opp_val = getattr(value, "categories", None)
                if opp_val is None:
                    setattr(value, "categories", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def InformationObject85(self):
        return self.__InformationObject85

    @InformationObject85.setter
    def InformationObject85(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_data_InformationObject__InformationObject85", None)
        self.__InformationObject85 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "starRankings"):
                opp_val = getattr(old_value, "starRankings", None)
                if opp_val == self:
                    setattr(old_value, "starRankings", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "starRankings"):
                opp_val = getattr(value, "starRankings", None)
                setattr(value, "starRankings", self)

    @property
    def from(self):
        return self.__from

    @from.setter
    def from(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_data_InformationObject__from", None)
        self.__from = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Connection"):
                    opp_val = getattr(item, "Connection", None)
                    
                    if opp_val == self:
                        setattr(item, "Connection", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Connection"):
                    opp_val = getattr(item, "Connection", None)
                    
                    setattr(item, "Connection", self)
                    

    @property
    def categorized(self):
        return self.__categorized

    @categorized.setter
    def categorized(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_data_InformationObject__categorized", None)
        self.__categorized = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Category"):
                    opp_val = getattr(item, "Category", None)
                    
                    if opp_val == self:
                        setattr(item, "Category", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Category"):
                    opp_val = getattr(item, "Category", None)
                    
                    setattr(item, "Category", self)
                    

    @property
    def InformationObject68(self):
        return self.__InformationObject68

    @InformationObject68.setter
    def InformationObject68(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_data_InformationObject__InformationObject68", None)
        self.__InformationObject68 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tags"):
                opp_val = getattr(old_value, "tags", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tags"):
                opp_val = getattr(value, "tags", None)
                if opp_val is None:
                    setattr(value, "tags", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def mainCategorized(self):
        return self.__mainCategorized

    @mainCategorized.setter
    def mainCategorized(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_data_InformationObject__mainCategorized", None)
        self.__mainCategorized = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Category23"):
                opp_val = getattr(old_value, "Category23", None)
                if opp_val == self:
                    setattr(old_value, "Category23", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Category23"):
                opp_val = getattr(value, "Category23", None)
                setattr(value, "Category23", self)

    @property
    def data_InformationObject21(self):
        return self.__data_InformationObject21

    @data_InformationObject21.setter
    def data_InformationObject21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_data_InformationObject__data_InformationObject21", None)
        self.__data_InformationObject21 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "data_Binary"):
                    opp_val = getattr(item, "data_Binary", None)
                    
                    if opp_val == self:
                        setattr(item, "data_Binary", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "data_Binary"):
                    opp_val = getattr(item, "data_Binary", None)
                    
                    setattr(item, "data_Binary", self)
                    

    @property
    def InformationObject66(self):
        return self.__InformationObject66

    @InformationObject66.setter
    def InformationObject66(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_data_InformationObject__InformationObject66", None)
        self.__InformationObject66 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mainCategory"):
                opp_val = getattr(old_value, "mainCategory", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mainCategory"):
                opp_val = getattr(value, "mainCategory", None)
                if opp_val is None:
                    setattr(value, "mainCategory", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def data_InformationObject(self):
        return self.__data_InformationObject

    @data_InformationObject.setter
    def data_InformationObject(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_data_InformationObject__data_InformationObject", None)
        self.__data_InformationObject = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "data_Image"):
                    opp_val = getattr(item, "data_Image", None)
                    
                    if opp_val == self:
                        setattr(item, "data_Image", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "data_Image"):
                    opp_val = getattr(item, "data_Image", None)
                    
                    setattr(item, "data_Image", self)
                    

    @property
    def InformationObject95(self):
        return self.__InformationObject95

    @InformationObject95.setter
    def InformationObject95(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_data_InformationObject__InformationObject95", None)
        self.__InformationObject95 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "connectedBy"):
                opp_val = getattr(old_value, "connectedBy", None)
                if opp_val == self:
                    setattr(old_value, "connectedBy", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "connectedBy"):
                opp_val = getattr(value, "connectedBy", None)
                setattr(value, "connectedBy", self)

    @property
    def InformationObject87(self):
        return self.__InformationObject87

    @InformationObject87.setter
    def InformationObject87(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_data_InformationObject__InformationObject87", None)
        self.__InformationObject87 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "viewRankings"):
                opp_val = getattr(old_value, "viewRankings", None)
                if opp_val == self:
                    setattr(old_value, "viewRankings", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "viewRankings"):
                opp_val = getattr(value, "viewRankings", None)
                setattr(value, "viewRankings", self)

    @property
    def to(self):
        return self.__to

    @to.setter
    def to(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_data_InformationObject__to", None)
        self.__to = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Connection19"):
                    opp_val = getattr(item, "Connection19", None)
                    
                    if opp_val == self:
                        setattr(item, "Connection19", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Connection19"):
                    opp_val = getattr(item, "Connection19", None)
                    
                    setattr(item, "Connection19", self)
                    

    @property
    def rankedInformationObject14(self):
        return self.__rankedInformationObject14

    @rankedInformationObject14.setter
    def rankedInformationObject14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_data_InformationObject__rankedInformationObject14", None)
        self.__rankedInformationObject14 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ThumbRanking"):
                    opp_val = getattr(item, "ThumbRanking", None)
                    
                    if opp_val == self:
                        setattr(item, "ThumbRanking", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ThumbRanking"):
                    opp_val = getattr(item, "ThumbRanking", None)
                    
                    setattr(item, "ThumbRanking", self)
                    

    @property
    def tagged(self):
        return self.__tagged

    @tagged.setter
    def tagged(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_data_InformationObject__tagged", None)
        self.__tagged = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Tag"):
                    opp_val = getattr(item, "Tag", None)
                    
                    if opp_val == self:
                        setattr(item, "Tag", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Tag"):
                    opp_val = getattr(item, "Tag", None)
                    
                    setattr(item, "Tag", self)
                    

    @property
    def InformationObject97(self):
        return self.__InformationObject97

    @InformationObject97.setter
    def InformationObject97(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_data_InformationObject__InformationObject97", None)
        self.__InformationObject97 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "metaInformations"):
                opp_val = getattr(old_value, "metaInformations", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "metaInformations"):
                opp_val = getattr(value, "metaInformations", None)
                if opp_val is None:
                    setattr(value, "metaInformations", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def categorize(self, name: str) -> str:
        # TODO: Implement categorize method
        pass

    def getInformationObjectsConnectedFrom(self) -> InformationObject:
        # TODO: Implement getInformationObjectsConnectedFrom method
        pass

    def addWebAccount(self, username: str) -> str:
        # TODO: Implement addWebAccount method
        pass

    def getConnectionsFrom(self, informationObject: InformationObject) -> str:
        # TODO: Implement getConnectionsFrom method
        pass

    def addCitation(self, citationData: str) -> str:
        # TODO: Implement addCitation method
        pass

    def getThumbsDownCount(self) -> str:
        # TODO: Implement getThumbsDownCount method
        pass

    def addEmailAddress(self, emailAdress: str) -> str:
        # TODO: Implement addEmailAddress method
        pass

    def getPersonsWithCommonTags(self) -> str:
        # TODO: Implement getPersonsWithCommonTags method
        pass

    def connectTo(self, informationObject: InformationObject) -> str:
        # TODO: Implement connectTo method
        pass

    def getConnectionsTo(self, informationObject: InformationObject) -> str:
        # TODO: Implement getConnectionsTo method
        pass

    def unCategorize(self, name: str) -> str:
        # TODO: Implement unCategorize method
        pass

    def tag(self, name: str) -> str:
        # TODO: Implement tag method
        pass

    def getAttachedImagesWithoutMetaTag(self, metaTag: str) -> str:
        # TODO: Implement getAttachedImagesWithoutMetaTag method
        pass

    def connectToWithValueAndMetaTag(self, metaTag: str, value: str, informationObject: InformationObject) -> str:
        # TODO: Implement connectToWithValueAndMetaTag method
        pass

    def getEmails(self) -> str:
        # TODO: Implement getEmails method
        pass

    def getIndoorLocations(self) -> str:
        # TODO: Implement getIndoorLocations method
        pass

    def addPhone(self, phoneNumber: str) -> str:
        # TODO: Implement addPhone method
        pass

    def getStarRanking(self) -> str:
        # TODO: Implement getStarRanking method
        pass

    def getAttachmentWithUrl(self, url: str) -> str:
        # TODO: Implement getAttachmentWithUrl method
        pass

    def getInformationObjectsConnected(self) -> InformationObject:
        # TODO: Implement getInformationObjectsConnected method
        pass

    def getContentsWithCommonTags(self) -> str:
        # TODO: Implement getContentsWithCommonTags method
        pass

    def getThumbsDown(self) -> str:
        # TODO: Implement getThumbsDown method
        pass

    def getConnectionsToWithMetaTag(self, metaTag: str, informationObject: InformationObject) -> str:
        # TODO: Implement getConnectionsToWithMetaTag method
        pass

    def getWebAccounts(self) -> str:
        # TODO: Implement getWebAccounts method
        pass

    def getWebSites(self) -> str:
        # TODO: Implement getWebSites method
        pass

    def getLocations(self) -> str:
        # TODO: Implement getLocations method
        pass

    def starRankWithMetaTag(self, metaTag: str, stars: str, ofStars: str) -> str:
        # TODO: Implement starRankWithMetaTag method
        pass

    def getInformationObjectsConnectedWithMetaTag(self, metaTag: str) -> InformationObject:
        # TODO: Implement getInformationObjectsConnectedWithMetaTag method
        pass

    def getAttachments(self) -> str:
        # TODO: Implement getAttachments method
        pass

    def getConnectionTo(self, informationObject: InformationObject, value: str) -> str:
        # TODO: Implement getConnectionTo method
        pass

    def extend(self, metaInformation: str) -> str:
        # TODO: Implement extend method
        pass

    def starRank(self, ofStars: str, stars: str) -> str:
        # TODO: Implement starRank method
        pass

    def addWebSite(self, url: str) -> str:
        # TODO: Implement addWebSite method
        pass

    def getAttachedImagesWithoutMetaTagName(self, metaTagName: str) -> str:
        # TODO: Implement getAttachedImagesWithoutMetaTagName method
        pass

    def getAttachedImageWithMetaTag(self, metaTag: str) -> str:
        # TODO: Implement getAttachedImageWithMetaTag method
        pass

    def addAlternativeName(self, name: str) -> str:
        # TODO: Implement addAlternativeName method
        pass

    def hasImages(self) -> str:
        # TODO: Implement hasImages method
        pass

    def getPhones(self) -> str:
        # TODO: Implement getPhones method
        pass

    def view(self) -> str:
        # TODO: Implement view method
        pass

    def getInformationObjectsConnectedFromWithMetaTag(self, metaTag: str) -> InformationObject:
        # TODO: Implement getInformationObjectsConnectedFromWithMetaTag method
        pass

    def getAttachedImageWithMetaTagName(self, metaTagName: str) -> str:
        # TODO: Implement getAttachedImageWithMetaTagName method
        pass

    def getSlugName(self) -> str:
        # TODO: Implement getSlugName method
        pass

    def getInstantMessengers(self) -> str:
        # TODO: Implement getInstantMessengers method
        pass

    def getInformationObjectsWithCommonTags(self) -> InformationObject:
        # TODO: Implement getInformationObjectsWithCommonTags method
        pass

    def getThumbsUp(self) -> str:
        # TODO: Implement getThumbsUp method
        pass

    def getOrganisationsWithCommonTags(self) -> str:
        # TODO: Implement getOrganisationsWithCommonTags method
        pass

    def getThumbsUpCount(self) -> str:
        # TODO: Implement getThumbsUpCount method
        pass

    def getInformationObjectsConnectedTo(self) -> InformationObject:
        # TODO: Implement getInformationObjectsConnectedTo method
        pass

    def getConnectionsFromWithMetaTag(self, informationObject: InformationObject, metaTag: str) -> str:
        # TODO: Implement getConnectionsFromWithMetaTag method
        pass

    def thumbsUp(self) -> str:
        # TODO: Implement thumbsUp method
        pass

    def getEvents(self) -> str:
        # TODO: Implement getEvents method
        pass

    def starRankWithMetaTagList(self, stars: str, metaTagList: str, ofStars: str) -> str:
        # TODO: Implement starRankWithMetaTagList method
        pass

    def addWebAccountForService(self, service: str, username: str) -> str:
        # TODO: Implement addWebAccountForService method
        pass

    def getViewsCount(self) -> str:
        # TODO: Implement getViewsCount method
        pass

    def getInformationObjectsConnectedToWithMetaTag(self, metaTag: str) -> InformationObject:
        # TODO: Implement getInformationObjectsConnectedToWithMetaTag method
        pass

    def thumbsDown(self) -> str:
        # TODO: Implement thumbsDown method
        pass

    def getThumbsCount(self) -> str:
        # TODO: Implement getThumbsCount method
        pass

    def connectToWithMetaTag(self, informationObject: InformationObject, metaTag: str) -> str:
        # TODO: Implement connectToWithMetaTag method
        pass

    def unTag(self, name: str) -> str:
        # TODO: Implement unTag method
        pass

    def getConnectionFrom(self, informationObject: InformationObject, value: str) -> str:
        # TODO: Implement getConnectionFrom method
        pass

    def getCitations(self) -> str:
        # TODO: Implement getCitations method
        pass

    def getAttachedImageWithUrl(self, url: str) -> str:
        # TODO: Implement getAttachedImageWithUrl method
        pass

    def attachImage(self, imageUrl: str) -> str:
        # TODO: Implement attachImage method
        pass

class data_Ranking(Extension):

    def __init__(self, date: date, Ranking: "data_Person" = None, ranked: "data_Person" = None):
        self.date = date
        self.Ranking = Ranking
        self.ranked = ranked
        
    @property
    def date(self) -> date:
        return self.__date

    @date.setter
    def date(self, date: date):
        self.__date = date

    @property
    def Ranking(self):
        return self.__Ranking

    @Ranking.setter
    def Ranking(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_data_Ranking__Ranking", None)
        self.__Ranking = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ranker"):
                opp_val = getattr(old_value, "ranker", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ranker"):
                opp_val = getattr(value, "ranker", None)
                if opp_val is None:
                    setattr(value, "ranker", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ranked(self):
        return self.__ranked

    @ranked.setter
    def ranked(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_data_Ranking__ranked", None)
        self.__ranked = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Person82"):
                opp_val = getattr(old_value, "Person82", None)
                if opp_val == self:
                    setattr(old_value, "Person82", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Person82"):
                opp_val = getattr(value, "Person82", None)
                setattr(value, "Person82", self)

class InformationObject:

    pass
class data_Content(InformationObject):

    def __init__(self, locale: str, Content: "data_Person" = None, Content5: "data_Person" = None, Content27: "data_Content" = None, parentContent: set["data_Content"] = None, contributed: set["data_Person"] = None, authored: "data_Person" = None, data_Content: set["data_Document"] = None, Content34: "data_Content" = None, contents: "data_Content" = None, transformed: set["data_Transformation"] = None, data_Content37: set["data_Video"] = None, Content91: "data_Transformation" = None):
        self.locale = locale
        self.Content = Content
        self.Content5 = Content5
        self.Content27 = Content27
        self.parentContent = parentContent if parentContent is not None else set()
        self.contributed = contributed if contributed is not None else set()
        self.authored = authored
        self.data_Content = data_Content if data_Content is not None else set()
        self.Content34 = Content34
        self.contents = contents
        self.transformed = transformed if transformed is not None else set()
        self.data_Content37 = data_Content37 if data_Content37 is not None else set()
        self.Content91 = Content91
        
    @property
    def locale(self) -> str:
        return self.__locale

    @locale.setter
    def locale(self, locale: str):
        self.__locale = locale

    @property
    def Content91(self):
        return self.__Content91

    @Content91.setter
    def Content91(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_data_Content__Content91", None)
        self.__Content91 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "transformations"):
                opp_val = getattr(old_value, "transformations", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "transformations"):
                opp_val = getattr(value, "transformations", None)
                if opp_val is None:
                    setattr(value, "transformations", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def contents(self):
        return self.__contents

    @contents.setter
    def contents(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_data_Content__contents", None)
        self.__contents = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Content34"):
                opp_val = getattr(old_value, "Content34", None)
                if opp_val == self:
                    setattr(old_value, "Content34", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Content34"):
                opp_val = getattr(value, "Content34", None)
                setattr(value, "Content34", self)

    @property
    def transformed(self):
        return self.__transformed

    @transformed.setter
    def transformed(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_data_Content__transformed", None)
        self.__transformed = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Transformation"):
                    opp_val = getattr(item, "Transformation", None)
                    
                    if opp_val == self:
                        setattr(item, "Transformation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Transformation"):
                    opp_val = getattr(item, "Transformation", None)
                    
                    setattr(item, "Transformation", self)
                    

    @property
    def Content34(self):
        return self.__Content34

    @Content34.setter
    def Content34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_data_Content__Content34", None)
        self.__Content34 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "contents"):
                opp_val = getattr(old_value, "contents", None)
                if opp_val == self:
                    setattr(old_value, "contents", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "contents"):
                opp_val = getattr(value, "contents", None)
                setattr(value, "contents", self)

    @property
    def Content27(self):
        return self.__Content27

    @Content27.setter
    def Content27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_data_Content__Content27", None)
        self.__Content27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "parentContent"):
                opp_val = getattr(old_value, "parentContent", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "parentContent"):
                opp_val = getattr(value, "parentContent", None)
                if opp_val is None:
                    setattr(value, "parentContent", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def contributed(self):
        return self.__contributed

    @contributed.setter
    def contributed(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_data_Content__contributed", None)
        self.__contributed = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Person"):
                    opp_val = getattr(item, "Person", None)
                    
                    if opp_val == self:
                        setattr(item, "Person", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Person"):
                    opp_val = getattr(item, "Person", None)
                    
                    setattr(item, "Person", self)
                    

    @property
    def Content(self):
        return self.__Content

    @Content.setter
    def Content(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_data_Content__Content", None)
        self.__Content = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "author"):
                opp_val = getattr(old_value, "author", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "author"):
                opp_val = getattr(value, "author", None)
                if opp_val is None:
                    setattr(value, "author", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def data_Content37(self):
        return self.__data_Content37

    @data_Content37.setter
    def data_Content37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_data_Content__data_Content37", None)
        self.__data_Content37 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "data_Video"):
                    opp_val = getattr(item, "data_Video", None)
                    
                    if opp_val == self:
                        setattr(item, "data_Video", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "data_Video"):
                    opp_val = getattr(item, "data_Video", None)
                    
                    setattr(item, "data_Video", self)
                    

    @property
    def Content5(self):
        return self.__Content5

    @Content5.setter
    def Content5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_data_Content__Content5", None)
        self.__Content5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "contributors"):
                opp_val = getattr(old_value, "contributors", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "contributors"):
                opp_val = getattr(value, "contributors", None)
                if opp_val is None:
                    setattr(value, "contributors", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def data_Content(self):
        return self.__data_Content

    @data_Content.setter
    def data_Content(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_data_Content__data_Content", None)
        self.__data_Content = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "data_Document"):
                    opp_val = getattr(item, "data_Document", None)
                    
                    if opp_val == self:
                        setattr(item, "data_Document", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "data_Document"):
                    opp_val = getattr(item, "data_Document", None)
                    
                    setattr(item, "data_Document", self)
                    

    @property
    def authored(self):
        return self.__authored

    @authored.setter
    def authored(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_data_Content__authored", None)
        self.__authored = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Person30"):
                opp_val = getattr(old_value, "Person30", None)
                if opp_val == self:
                    setattr(old_value, "Person30", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Person30"):
                opp_val = getattr(value, "Person30", None)
                setattr(value, "Person30", self)

    @property
    def parentContent(self):
        return self.__parentContent

    @parentContent.setter
    def parentContent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_data_Content__parentContent", None)
        self.__parentContent = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Content27"):
                    opp_val = getattr(item, "Content27", None)
                    
                    if opp_val == self:
                        setattr(item, "Content27", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Content27"):
                    opp_val = getattr(item, "Content27", None)
                    
                    setattr(item, "Content27", self)
                    

    def comment(self, comment: str) -> str:
        # TODO: Implement comment method
        pass

    def attachDocument(self, fileUrl: str) -> str:
        # TODO: Implement attachDocument method
        pass

    def addContributor(self, contributor: str) -> str:
        # TODO: Implement addContributor method
        pass

    def getOrganisations(self) -> str:
        # TODO: Implement getOrganisations method
        pass

    def getPersons(self) -> str:
        # TODO: Implement getPersons method
        pass

    def commentWithMetaTagList(self, comment: str, metaTagList: str) -> str:
        # TODO: Implement commentWithMetaTagList method
        pass

class data_Organisation(InformationObject):

    def __init__(self, Organisation: "data_Person" = None, Organisation2: "data_Person" = None, Organisation71: "data_Organisation" = None, organisations: "data_Organisation" = None, leaderOf: "data_Person" = None, participates: set["data_Person"] = None, Organisation78: "data_Organisation" = None, parentOrganisation: set["data_Organisation"] = None):
        self.Organisation = Organisation
        self.Organisation2 = Organisation2
        self.Organisation71 = Organisation71
        self.organisations = organisations
        self.leaderOf = leaderOf
        self.participates = participates if participates is not None else set()
        self.Organisation78 = Organisation78
        self.parentOrganisation = parentOrganisation if parentOrganisation is not None else set()
        
    @property
    def Organisation(self):
        return self.__Organisation

    @Organisation.setter
    def Organisation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_data_Organisation__Organisation", None)
        self.__Organisation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "leader"):
                opp_val = getattr(old_value, "leader", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "leader"):
                opp_val = getattr(value, "leader", None)
                if opp_val is None:
                    setattr(value, "leader", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def leaderOf(self):
        return self.__leaderOf

    @leaderOf.setter
    def leaderOf(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_data_Organisation__leaderOf", None)
        self.__leaderOf = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Person73"):
                opp_val = getattr(old_value, "Person73", None)
                if opp_val == self:
                    setattr(old_value, "Person73", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Person73"):
                opp_val = getattr(value, "Person73", None)
                setattr(value, "Person73", self)

    @property
    def Organisation2(self):
        return self.__Organisation2

    @Organisation2.setter
    def Organisation2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_data_Organisation__Organisation2", None)
        self.__Organisation2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "participants"):
                opp_val = getattr(old_value, "participants", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "participants"):
                opp_val = getattr(value, "participants", None)
                if opp_val is None:
                    setattr(value, "participants", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Organisation71(self):
        return self.__Organisation71

    @Organisation71.setter
    def Organisation71(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_data_Organisation__Organisation71", None)
        self.__Organisation71 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "organisations"):
                opp_val = getattr(old_value, "organisations", None)
                if opp_val == self:
                    setattr(old_value, "organisations", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "organisations"):
                opp_val = getattr(value, "organisations", None)
                setattr(value, "organisations", self)

    @property
    def participates(self):
        return self.__participates

    @participates.setter
    def participates(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_data_Organisation__participates", None)
        self.__participates = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Person75"):
                    opp_val = getattr(item, "Person75", None)
                    
                    if opp_val == self:
                        setattr(item, "Person75", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Person75"):
                    opp_val = getattr(item, "Person75", None)
                    
                    setattr(item, "Person75", self)
                    

    @property
    def Organisation78(self):
        return self.__Organisation78

    @Organisation78.setter
    def Organisation78(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_data_Organisation__Organisation78", None)
        self.__Organisation78 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "parentOrganisation"):
                opp_val = getattr(old_value, "parentOrganisation", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "parentOrganisation"):
                opp_val = getattr(value, "parentOrganisation", None)
                if opp_val is None:
                    setattr(value, "parentOrganisation", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def organisations(self):
        return self.__organisations

    @organisations.setter
    def organisations(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_data_Organisation__organisations", None)
        self.__organisations = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Organisation71"):
                opp_val = getattr(old_value, "Organisation71", None)
                if opp_val == self:
                    setattr(old_value, "Organisation71", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Organisation71"):
                opp_val = getattr(value, "Organisation71", None)
                setattr(value, "Organisation71", self)

    @property
    def parentOrganisation(self):
        return self.__parentOrganisation

    @parentOrganisation.setter
    def parentOrganisation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_data_Organisation__parentOrganisation", None)
        self.__parentOrganisation = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Organisation78"):
                    opp_val = getattr(item, "Organisation78", None)
                    
                    if opp_val == self:
                        setattr(item, "Organisation78", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Organisation78"):
                    opp_val = getattr(item, "Organisation78", None)
                    
                    setattr(item, "Organisation78", self)
                    

    def getPersons(self) -> str:
        # TODO: Implement getPersons method
        pass

    def addParticipant(self, participant: str) -> str:
        # TODO: Implement addParticipant method
        pass

    def getContents(self) -> str:
        # TODO: Implement getContents method
        pass

class data_Person(InformationObject):

    def __init__(self, lastname: str, firstname: str, dateOfBirth: date, title: str, leader: set["data_Organisation"] = None, participants: set["data_Organisation"] = None, author: set["data_Content"] = None, contributors: set["data_Content"] = None, data_Person: "data_Person" = None, data_Person6: set["data_Person"] = None, ranker: set["data_Ranking"] = None, Person: "data_Content" = None, Person30: "data_Content" = None, Person73: "data_Organisation" = None, Person75: "data_Organisation" = None, Person82: "data_Ranking" = None):
        self.lastname = lastname
        self.firstname = firstname
        self.dateOfBirth = dateOfBirth
        self.title = title
        self.leader = leader if leader is not None else set()
        self.participants = participants if participants is not None else set()
        self.author = author if author is not None else set()
        self.contributors = contributors if contributors is not None else set()
        self.data_Person = data_Person
        self.data_Person6 = data_Person6 if data_Person6 is not None else set()
        self.ranker = ranker if ranker is not None else set()
        self.Person = Person
        self.Person30 = Person30
        self.Person73 = Person73
        self.Person75 = Person75
        self.Person82 = Person82
        
    @property
    def firstname(self) -> str:
        return self.__firstname

    @firstname.setter
    def firstname(self, firstname: str):
        self.__firstname = firstname

    @property
    def lastname(self) -> str:
        return self.__lastname

    @lastname.setter
    def lastname(self, lastname: str):
        self.__lastname = lastname

    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def dateOfBirth(self) -> date:
        return self.__dateOfBirth

    @dateOfBirth.setter
    def dateOfBirth(self, dateOfBirth: date):
        self.__dateOfBirth = dateOfBirth

    @property
    def data_Person6(self):
        return self.__data_Person6

    @data_Person6.setter
    def data_Person6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_data_Person__data_Person6", None)
        self.__data_Person6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "data_Person"):
                    opp_val = getattr(item, "data_Person", None)
                    
                    if opp_val == self:
                        setattr(item, "data_Person", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "data_Person"):
                    opp_val = getattr(item, "data_Person", None)
                    
                    setattr(item, "data_Person", self)
                    

    @property
    def leader(self):
        return self.__leader

    @leader.setter
    def leader(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_data_Person__leader", None)
        self.__leader = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Organisation"):
                    opp_val = getattr(item, "Organisation", None)
                    
                    if opp_val == self:
                        setattr(item, "Organisation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Organisation"):
                    opp_val = getattr(item, "Organisation", None)
                    
                    setattr(item, "Organisation", self)
                    

    @property
    def participants(self):
        return self.__participants

    @participants.setter
    def participants(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_data_Person__participants", None)
        self.__participants = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Organisation2"):
                    opp_val = getattr(item, "Organisation2", None)
                    
                    if opp_val == self:
                        setattr(item, "Organisation2", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Organisation2"):
                    opp_val = getattr(item, "Organisation2", None)
                    
                    setattr(item, "Organisation2", self)
                    

    @property
    def author(self):
        return self.__author

    @author.setter
    def author(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_data_Person__author", None)
        self.__author = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Content"):
                    opp_val = getattr(item, "Content", None)
                    
                    if opp_val == self:
                        setattr(item, "Content", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Content"):
                    opp_val = getattr(item, "Content", None)
                    
                    setattr(item, "Content", self)
                    

    @property
    def contributors(self):
        return self.__contributors

    @contributors.setter
    def contributors(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_data_Person__contributors", None)
        self.__contributors = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Content5"):
                    opp_val = getattr(item, "Content5", None)
                    
                    if opp_val == self:
                        setattr(item, "Content5", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Content5"):
                    opp_val = getattr(item, "Content5", None)
                    
                    setattr(item, "Content5", self)
                    

    @property
    def Person82(self):
        return self.__Person82

    @Person82.setter
    def Person82(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_data_Person__Person82", None)
        self.__Person82 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ranked"):
                opp_val = getattr(old_value, "ranked", None)
                if opp_val == self:
                    setattr(old_value, "ranked", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ranked"):
                opp_val = getattr(value, "ranked", None)
                setattr(value, "ranked", self)

    @property
    def Person30(self):
        return self.__Person30

    @Person30.setter
    def Person30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_data_Person__Person30", None)
        self.__Person30 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "authored"):
                opp_val = getattr(old_value, "authored", None)
                if opp_val == self:
                    setattr(old_value, "authored", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "authored"):
                opp_val = getattr(value, "authored", None)
                setattr(value, "authored", self)

    @property
    def Person(self):
        return self.__Person

    @Person.setter
    def Person(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_data_Person__Person", None)
        self.__Person = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "contributed"):
                opp_val = getattr(old_value, "contributed", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "contributed"):
                opp_val = getattr(value, "contributed", None)
                if opp_val is None:
                    setattr(value, "contributed", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Person73(self):
        return self.__Person73

    @Person73.setter
    def Person73(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_data_Person__Person73", None)
        self.__Person73 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "leaderOf"):
                opp_val = getattr(old_value, "leaderOf", None)
                if opp_val == self:
                    setattr(old_value, "leaderOf", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "leaderOf"):
                opp_val = getattr(value, "leaderOf", None)
                setattr(value, "leaderOf", self)

    @property
    def data_Person(self):
        return self.__data_Person

    @data_Person.setter
    def data_Person(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_data_Person__data_Person", None)
        self.__data_Person = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "data_Person6"):
                opp_val = getattr(old_value, "data_Person6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "data_Person6"):
                opp_val = getattr(value, "data_Person6", None)
                if opp_val is None:
                    setattr(value, "data_Person6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ranker(self):
        return self.__ranker

    @ranker.setter
    def ranker(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_data_Person__ranker", None)
        self.__ranker = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Ranking"):
                    opp_val = getattr(item, "Ranking", None)
                    
                    if opp_val == self:
                        setattr(item, "Ranking", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Ranking"):
                    opp_val = getattr(item, "Ranking", None)
                    
                    setattr(item, "Ranking", self)
                    

    @property
    def Person75(self):
        return self.__Person75

    @Person75.setter
    def Person75(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_data_Person__Person75", None)
        self.__Person75 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "participates"):
                opp_val = getattr(old_value, "participates", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "participates"):
                opp_val = getattr(value, "participates", None)
                if opp_val is None:
                    setattr(value, "participates", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def getContents(self) -> str:
        # TODO: Implement getContents method
        pass

    def parseLastName(self) -> str:
        # TODO: Implement parseLastName method
        pass

    def addAuthoredContent(self, authoredContent: str) -> str:
        # TODO: Implement addAuthoredContent method
        pass

    def getOrganisations(self) -> str:
        # TODO: Implement getOrganisations method
        pass

    def parseFirstName(self) -> str:
        # TODO: Implement parseFirstName method
        pass

    def addContributedContent(self, contributedContent: str) -> str:
        # TODO: Implement addContributedContent method
        pass
