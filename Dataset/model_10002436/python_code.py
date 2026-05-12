from __future__ import annotations
from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class PublicityState(Enum):
    pass
class Date(Enum):
    pass
class ContentPagePublicityState(Enum):
    pass
class MediaType(Enum):
    pass
class Enumeration(Enum):
    pass
class VIDEO(Enum):
    pass

############################################
# Definition of Classes
############################################










class Address:

    def __init__(self, city: str, street: str, streetnumber: str, zipCode: str, country: str, contentPage29: "ContentPage" = None):
        self.city = city
        self.street = street
        self.streetnumber = streetnumber
        self.zipCode = zipCode
        self.country = country
        self.contentPage29 = contentPage29
        
        pass
    @property
    def street(self):
        return self.__street
    @street.setter
    def street(self, street: str):
        self.__street = street

    @property
    def city(self):
        return self.__city
    @city.setter
    def city(self, city: str):
        self.__city = city

    @property
    def country(self):
        return self.__country
    @country.setter
    def country(self, country: str):
        self.__country = country

    @property
    def streetnumber(self):
        return self.__streetnumber
    @streetnumber.setter
    def streetnumber(self, streetnumber: str):
        self.__streetnumber = streetnumber

    @property
    def zipCode(self):
        return self.__zipCode
    @zipCode.setter
    def zipCode(self, zipCode: str):
        self.__zipCode = zipCode

    @property
    def contentPage29(self):
        return self.__contentPage29
    @contentPage29.setter
    def contentPage29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Address__contentPage29", None)
        self.__contentPage29 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "address28"):
                opp_val = getattr(old_value, "address28", None)
                if opp_val == self:
                    setattr(old_value, "address28", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "address28"):
                opp_val = getattr(value, "address28", None)
                setattr(value, "address28", self)



class Tag:

    def __init__(self, name: str, contentPage19: "ContentPage" = None, contentPage25: set["ContentPage"] = None):
        self.name = name
        self.contentPage19 = contentPage19
        self.contentPage25 = contentPage25 if contentPage25 is not None else set()
        
        pass
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def contentPage25(self):
        return self.__contentPage25
    @contentPage25.setter
    def contentPage25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Tag__contentPage25", None)
        self.__contentPage25 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "tag24"):
                    opp_val = getattr(item, "tag24", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "tag24"):
                    opp_val = getattr(item, "tag24", None)
                    
                    if opp_val is None:
                        setattr(item, "tag24", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def contentPage19(self):
        return self.__contentPage19
    @contentPage19.setter
    def contentPage19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Tag__contentPage19", None)
        self.__contentPage19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tag18"):
                opp_val = getattr(old_value, "tag18", None)
                if opp_val == self:
                    setattr(old_value, "tag18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tag18"):
                opp_val = getattr(value, "tag18", None)
                setattr(value, "tag18", self)



class ContentPage:

    def __init__(self, references: str, address: Address, date: Date, headline: str, tags: str, state: str, attribute: str, publishingDate: Date, expiryDate: Date, content1: str, priority: str, priorityExpiryDate: Date, title: str, active: bool, content: str, author: AdminUser, externalSource: str, media: Media, tag18: "Tag" = None, tag24: set["Tag"] = None, address28: "Address" = None, author30: "AdminUser" = None):
        self.references = references
        self.address = address
        self.date = date
        self.headline = headline
        self.tags = tags
        self.state = state
        self.attribute = attribute
        self.publishingDate = publishingDate
        self.expiryDate = expiryDate
        self.content1 = content1
        self.priority = priority
        self.priorityExpiryDate = priorityExpiryDate
        self.title = title
        self.active = active
        self.content = content
        self.author = author
        self.externalSource = externalSource
        self.media = media
        self.tag18 = tag18
        self.tag24 = tag24 if tag24 is not None else set()
        self.address28 = address28
        self.author30 = author30
        
        pass
    @property
    def publishingDate(self):
        return self.__publishingDate
    @publishingDate.setter
    def publishingDate(self, publishingDate: Date):
        self.__publishingDate = publishingDate

    @property
    def address(self):
        return self.__address
    @address.setter
    def address(self, address: Address):
        self.__address = address

    @property
    def references(self):
        return self.__references
    @references.setter
    def references(self, references: str):
        self.__references = references

    @property
    def tags(self):
        return self.__tags
    @tags.setter
    def tags(self, tags: str):
        self.__tags = tags

    @property
    def media(self):
        return self.__media
    @media.setter
    def media(self, media: Media):
        self.__media = media

    @property
    def externalSource(self):
        return self.__externalSource
    @externalSource.setter
    def externalSource(self, externalSource: str):
        self.__externalSource = externalSource

    @property
    def headline(self):
        return self.__headline
    @headline.setter
    def headline(self, headline: str):
        self.__headline = headline

    @property
    def content1(self):
        return self.__content1
    @content1.setter
    def content1(self, content1: str):
        self.__content1 = content1

    @property
    def expiryDate(self):
        return self.__expiryDate
    @expiryDate.setter
    def expiryDate(self, expiryDate: Date):
        self.__expiryDate = expiryDate

    @property
    def attribute(self):
        return self.__attribute
    @attribute.setter
    def attribute(self, attribute: str):
        self.__attribute = attribute

    @property
    def content(self):
        return self.__content
    @content.setter
    def content(self, content: str):
        self.__content = content

    @property
    def priorityExpiryDate(self):
        return self.__priorityExpiryDate
    @priorityExpiryDate.setter
    def priorityExpiryDate(self, priorityExpiryDate: Date):
        self.__priorityExpiryDate = priorityExpiryDate

    @property
    def author(self):
        return self.__author
    @author.setter
    def author(self, author: AdminUser):
        self.__author = author

    @property
    def active(self):
        return self.__active
    @active.setter
    def active(self, active: bool):
        self.__active = active

    @property
    def title(self):
        return self.__title
    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def date(self):
        return self.__date
    @date.setter
    def date(self, date: Date):
        self.__date = date

    @property
    def state(self):
        return self.__state
    @state.setter
    def state(self, state: str):
        self.__state = state

    @property
    def priority(self):
        return self.__priority
    @priority.setter
    def priority(self, priority: str):
        self.__priority = priority

    @property
    def address28(self):
        return self.__address28
    @address28.setter
    def address28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ContentPage__address28", None)
        self.__address28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "contentPage29"):
                opp_val = getattr(old_value, "contentPage29", None)
                if opp_val == self:
                    setattr(old_value, "contentPage29", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "contentPage29"):
                opp_val = getattr(value, "contentPage29", None)
                setattr(value, "contentPage29", self)

    @property
    def author30(self):
        return self.__author30
    @author30.setter
    def author30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ContentPage__author30", None)
        self.__author30 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "contentPage31"):
                opp_val = getattr(old_value, "contentPage31", None)
                if opp_val == self:
                    setattr(old_value, "contentPage31", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "contentPage31"):
                opp_val = getattr(value, "contentPage31", None)
                setattr(value, "contentPage31", self)

    @property
    def tag24(self):
        return self.__tag24
    @tag24.setter
    def tag24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ContentPage__tag24", None)
        self.__tag24 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "contentPage25"):
                    opp_val = getattr(item, "contentPage25", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "contentPage25"):
                    opp_val = getattr(item, "contentPage25", None)
                    
                    if opp_val is None:
                        setattr(item, "contentPage25", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def tag18(self):
        return self.__tag18
    @tag18.setter
    def tag18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ContentPage__tag18", None)
        self.__tag18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "contentPage19"):
                opp_val = getattr(old_value, "contentPage19", None)
                if opp_val == self:
                    setattr(old_value, "contentPage19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "contentPage19"):
                opp_val = getattr(value, "contentPage19", None)
                setattr(value, "contentPage19", self)



class Profile2:

    def __init__(self, username: str, name: str, firstName: str, email: str):
        self.username = username
        self.name = name
        self.firstName = firstName
        self.email = email
        
        pass
    @property
    def username(self):
        return self.__username
    @username.setter
    def username(self, username: str):
        self.__username = username

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def firstName(self):
        return self.__firstName
    @firstName.setter
    def firstName(self, firstName: str):
        self.__firstName = firstName

    @property
    def email(self):
        return self.__email
    @email.setter
    def email(self, email: str):
        self.__email = email



class AdminUser:

    def __init__(self, id: str, active: bool, password: str, roles: str, username: str, email: str, phone: str, contentPage31: "ContentPage" = None):
        self.id = id
        self.active = active
        self.password = password
        self.roles = roles
        self.username = username
        self.email = email
        self.phone = phone
        self.contentPage31 = contentPage31
        
        pass
    @property
    def active(self):
        return self.__active
    @active.setter
    def active(self, active: bool):
        self.__active = active

    @property
    def phone(self):
        return self.__phone
    @phone.setter
    def phone(self, phone: str):
        self.__phone = phone

    @property
    def roles(self):
        return self.__roles
    @roles.setter
    def roles(self, roles: str):
        self.__roles = roles

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def username(self):
        return self.__username
    @username.setter
    def username(self, username: str):
        self.__username = username

    @property
    def email(self):
        return self.__email
    @email.setter
    def email(self, email: str):
        self.__email = email

    @property
    def password(self):
        return self.__password
    @password.setter
    def password(self, password: str):
        self.__password = password

    @property
    def contentPage31(self):
        return self.__contentPage31
    @contentPage31.setter
    def contentPage31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_AdminUser__contentPage31", None)
        self.__contentPage31 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "author30"):
                opp_val = getattr(old_value, "author30", None)
                if opp_val == self:
                    setattr(old_value, "author30", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "author30"):
                opp_val = getattr(value, "author30", None)
                setattr(value, "author30", self)



class LogEntry:

    def __init__(self, objectType: str, objectId: str, time: str, _attr: str):
        self.objectType = objectType
        self.objectId = objectId
        self.time = time
        self._attr = _attr
        
        pass
    @property
    def objectId(self):
        return self.__objectId
    @objectId.setter
    def objectId(self, objectId: str):
        self.__objectId = objectId

    @property
    def _attr(self):
        return self.___attr
    @_attr.setter
    def _attr(self, _attr: str):
        self.___attr = _attr

    @property
    def objectType(self):
        return self.__objectType
    @objectType.setter
    def objectType(self, objectType: str):
        self.__objectType = objectType

    @property
    def time(self):
        return self.__time
    @time.setter
    def time(self, time: str):
        self.__time = time



class int2_Interface:

    pass


class Tenant:

    def __init__(self, id: str, name: str, abstractEntity15: set["AbstractEntity"] = None, abstractEntity26: set["AbstractEntity"] = None):
        self.id = id
        self.name = name
        self.abstractEntity15 = abstractEntity15 if abstractEntity15 is not None else set()
        self.abstractEntity26 = abstractEntity26 if abstractEntity26 is not None else set()
        
        pass
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def abstractEntity15(self):
        return self.__abstractEntity15
    @abstractEntity15.setter
    def abstractEntity15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Tenant__abstractEntity15", None)
        self.__abstractEntity15 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "tenant14"):
                    opp_val = getattr(item, "tenant14", None)
                    
                    if opp_val == self:
                        setattr(item, "tenant14", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "tenant14"):
                    opp_val = getattr(item, "tenant14", None)
                    
                    setattr(item, "tenant14", self)
                    

    @property
    def abstractEntity26(self):
        return self.__abstractEntity26
    @abstractEntity26.setter
    def abstractEntity26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Tenant__abstractEntity26", None)
        self.__abstractEntity26 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "tenant27"):
                    opp_val = getattr(item, "tenant27", None)
                    
                    if opp_val == self:
                        setattr(item, "tenant27", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "tenant27"):
                    opp_val = getattr(item, "tenant27", None)
                    
                    setattr(item, "tenant27", self)
                    



class Video:

    pass


class Image:

    pass


class Media:

    def __init__(self, mimetype: str, name: str, link: str, description: str, active: bool, filesize: int, mediaPool: MediaPool, mediaPool11: "MediaPool" = None, mediaPool13: "MediaPool" = None):
        self.mimetype = mimetype
        self.name = name
        self.link = link
        self.description = description
        self.active = active
        self.filesize = filesize
        self.mediaPool = mediaPool
        self.mediaPool11 = mediaPool11
        self.mediaPool13 = mediaPool13
        
        pass
    @property
    def link(self):
        return self.__link
    @link.setter
    def link(self, link: str):
        self.__link = link

    @property
    def filesize(self):
        return self.__filesize
    @filesize.setter
    def filesize(self, filesize: int):
        self.__filesize = filesize

    @property
    def active(self):
        return self.__active
    @active.setter
    def active(self, active: bool):
        self.__active = active

    @property
    def description(self):
        return self.__description
    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def mimetype(self):
        return self.__mimetype
    @mimetype.setter
    def mimetype(self, mimetype: str):
        self.__mimetype = mimetype

    @property
    def mediaPool(self):
        return self.__mediaPool
    @mediaPool.setter
    def mediaPool(self, mediaPool: MediaPool):
        self.__mediaPool = mediaPool

    @property
    def mediaPool11(self):
        return self.__mediaPool11
    @mediaPool11.setter
    def mediaPool11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Media__mediaPool11", None)
        self.__mediaPool11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "media10"):
                opp_val = getattr(old_value, "media10", None)
                if opp_val == self:
                    setattr(old_value, "media10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "media10"):
                opp_val = getattr(value, "media10", None)
                setattr(value, "media10", self)

    @property
    def mediaPool13(self):
        return self.__mediaPool13
    @mediaPool13.setter
    def mediaPool13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Media__mediaPool13", None)
        self.__mediaPool13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "assets12"):
                opp_val = getattr(old_value, "assets12", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "assets12"):
                opp_val = getattr(value, "assets12", None)
                if opp_val is None:
                    setattr(value, "assets12", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class MediaPool:

    def __init__(self, assets: str, name: str, media10: "Media" = None, assets12: set["Media"] = None, parent16: "MediaPool" = None, mediaPool17: "MediaPool" = None):
        self.assets = assets
        self.name = name
        self.media10 = media10
        self.assets12 = assets12 if assets12 is not None else set()
        self.parent16 = parent16
        self.mediaPool17 = mediaPool17
        
        pass
    @property
    def assets(self):
        return self.__assets
    @assets.setter
    def assets(self, assets: str):
        self.__assets = assets

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def parent16(self):
        return self.__parent16
    @parent16.setter
    def parent16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MediaPool__parent16", None)
        self.__parent16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mediaPool17"):
                opp_val = getattr(old_value, "mediaPool17", None)
                if opp_val == self:
                    setattr(old_value, "mediaPool17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mediaPool17"):
                opp_val = getattr(value, "mediaPool17", None)
                setattr(value, "mediaPool17", self)

    @property
    def mediaPool17(self):
        return self.__mediaPool17
    @mediaPool17.setter
    def mediaPool17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MediaPool__mediaPool17", None)
        self.__mediaPool17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "parent16"):
                opp_val = getattr(old_value, "parent16", None)
                if opp_val == self:
                    setattr(old_value, "parent16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "parent16"):
                opp_val = getattr(value, "parent16", None)
                setattr(value, "parent16", self)

    @property
    def media10(self):
        return self.__media10
    @media10.setter
    def media10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MediaPool__media10", None)
        self.__media10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mediaPool11"):
                opp_val = getattr(old_value, "mediaPool11", None)
                if opp_val == self:
                    setattr(old_value, "mediaPool11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mediaPool11"):
                opp_val = getattr(value, "mediaPool11", None)
                setattr(value, "mediaPool11", self)

    @property
    def assets12(self):
        return self.__assets12
    @assets12.setter
    def assets12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MediaPool__assets12", None)
        self.__assets12 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "mediaPool13"):
                    opp_val = getattr(item, "mediaPool13", None)
                    
                    if opp_val == self:
                        setattr(item, "mediaPool13", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "mediaPool13"):
                    opp_val = getattr(item, "mediaPool13", None)
                    
                    setattr(item, "mediaPool13", self)
                    



class Settings:

    def __init__(self, username: str, name: str, firstName: str, email: str, notificationChannels: str, user8: "User" = None, user21: "User" = None):
        self.username = username
        self.name = name
        self.firstName = firstName
        self.email = email
        self.notificationChannels = notificationChannels
        self.user8 = user8
        self.user21 = user21
        
        pass
    @property
    def email(self):
        return self.__email
    @email.setter
    def email(self, email: str):
        self.__email = email

    @property
    def username(self):
        return self.__username
    @username.setter
    def username(self, username: str):
        self.__username = username

    @property
    def notificationChannels(self):
        return self.__notificationChannels
    @notificationChannels.setter
    def notificationChannels(self, notificationChannels: str):
        self.__notificationChannels = notificationChannels

    @property
    def firstName(self):
        return self.__firstName
    @firstName.setter
    def firstName(self, firstName: str):
        self.__firstName = firstName

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def user8(self):
        return self.__user8
    @user8.setter
    def user8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Settings__user8", None)
        self.__user8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "settings9"):
                opp_val = getattr(old_value, "settings9", None)
                if opp_val == self:
                    setattr(old_value, "settings9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "settings9"):
                opp_val = getattr(value, "settings9", None)
                setattr(value, "settings9", self)

    @property
    def user21(self):
        return self.__user21
    @user21.setter
    def user21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Settings__user21", None)
        self.__user21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "settings20"):
                opp_val = getattr(old_value, "settings20", None)
                if opp_val == self:
                    setattr(old_value, "settings20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "settings20"):
                opp_val = getattr(value, "settings20", None)
                setattr(value, "settings20", self)



class AbstractEntity(ABC):

    def __init__(self, id: str, createdAt: Date, createdBy: User, modifiedAt: date, modifiedBy: User, tenant14: "Tenant" = None, tenant27: "Tenant" = None):
        self.id = id
        self.createdAt = createdAt
        self.createdBy = createdBy
        self.modifiedAt = modifiedAt
        self.modifiedBy = modifiedBy
        self.tenant14 = tenant14
        self.tenant27 = tenant27
        
        pass
    @property
    def createdBy(self):
        return self.__createdBy
    @createdBy.setter
    def createdBy(self, createdBy: User):
        self.__createdBy = createdBy

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def modifiedBy(self):
        return self.__modifiedBy
    @modifiedBy.setter
    def modifiedBy(self, modifiedBy: User):
        self.__modifiedBy = modifiedBy

    @property
    def createdAt(self):
        return self.__createdAt
    @createdAt.setter
    def createdAt(self, createdAt: Date):
        self.__createdAt = createdAt

    @property
    def modifiedAt(self):
        return self.__modifiedAt
    @modifiedAt.setter
    def modifiedAt(self, modifiedAt: date):
        self.__modifiedAt = modifiedAt

    @property
    def tenant27(self):
        return self.__tenant27
    @tenant27.setter
    def tenant27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_AbstractEntity__tenant27", None)
        self.__tenant27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "abstractEntity26"):
                opp_val = getattr(old_value, "abstractEntity26", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "abstractEntity26"):
                opp_val = getattr(value, "abstractEntity26", None)
                if opp_val is None:
                    setattr(value, "abstractEntity26", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def tenant14(self):
        return self.__tenant14
    @tenant14.setter
    def tenant14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_AbstractEntity__tenant14", None)
        self.__tenant14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "abstractEntity15"):
                opp_val = getattr(old_value, "abstractEntity15", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "abstractEntity15"):
                opp_val = getattr(value, "abstractEntity15", None)
                if opp_val is None:
                    setattr(value, "abstractEntity15", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Friend:

    pass


class Message:

    pass


class Group:

    pass


class Profile:

    def __init__(self, username: str, name: str, firstName: str, email: str, user1: "User" = None, user6: "User" = None, user23: "User" = None):
        self.username = username
        self.name = name
        self.firstName = firstName
        self.email = email
        self.user1 = user1
        self.user6 = user6
        self.user23 = user23
        
        pass
    @property
    def username(self):
        return self.__username
    @username.setter
    def username(self, username: str):
        self.__username = username

    @property
    def firstName(self):
        return self.__firstName
    @firstName.setter
    def firstName(self, firstName: str):
        self.__firstName = firstName

    @property
    def email(self):
        return self.__email
    @email.setter
    def email(self, email: str):
        self.__email = email

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def user1(self):
        return self.__user1
    @user1.setter
    def user1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Profile__user1", None)
        self.__user1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myprofile0"):
                opp_val = getattr(old_value, "myprofile0", None)
                if opp_val == self:
                    setattr(old_value, "myprofile0", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myprofile0"):
                opp_val = getattr(value, "myprofile0", None)
                setattr(value, "myprofile0", self)

    @property
    def user23(self):
        return self.__user23
    @user23.setter
    def user23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Profile__user23", None)
        self.__user23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "profile22"):
                opp_val = getattr(old_value, "profile22", None)
                if opp_val == self:
                    setattr(old_value, "profile22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "profile22"):
                opp_val = getattr(value, "profile22", None)
                setattr(value, "profile22", self)

    @property
    def user6(self):
        return self.__user6
    @user6.setter
    def user6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Profile__user6", None)
        self.__user6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "profile7"):
                opp_val = getattr(old_value, "profile7", None)
                if opp_val == self:
                    setattr(old_value, "profile7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "profile7"):
                opp_val = getattr(value, "profile7", None)
                setattr(value, "profile7", self)



class User:

    def __init__(self, userId: str, active: bool, password: str, myprofile0: "Profile" = None, group2: set["Group"] = None, message4: set["Message"] = None, profile7: "Profile" = None, settings9: "Settings" = None, settings20: "Settings" = None, profile22: "Profile" = None):
        self.userId = userId
        self.active = active
        self.password = password
        self.myprofile0 = myprofile0
        self.group2 = group2 if group2 is not None else set()
        self.message4 = message4 if message4 is not None else set()
        self.profile7 = profile7
        self.settings9 = settings9
        self.settings20 = settings20
        self.profile22 = profile22
        
        pass
    @property
    def active(self):
        return self.__active
    @active.setter
    def active(self, active: bool):
        self.__active = active

    @property
    def userId(self):
        return self.__userId
    @userId.setter
    def userId(self, userId: str):
        self.__userId = userId

    @property
    def password(self):
        return self.__password
    @password.setter
    def password(self, password: str):
        self.__password = password

    @property
    def profile7(self):
        return self.__profile7
    @profile7.setter
    def profile7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_User__profile7", None)
        self.__profile7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "user6"):
                opp_val = getattr(old_value, "user6", None)
                if opp_val == self:
                    setattr(old_value, "user6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "user6"):
                opp_val = getattr(value, "user6", None)
                setattr(value, "user6", self)

    @property
    def settings9(self):
        return self.__settings9
    @settings9.setter
    def settings9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_User__settings9", None)
        self.__settings9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "user8"):
                opp_val = getattr(old_value, "user8", None)
                if opp_val == self:
                    setattr(old_value, "user8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "user8"):
                opp_val = getattr(value, "user8", None)
                setattr(value, "user8", self)

    @property
    def message4(self):
        return self.__message4
    @message4.setter
    def message4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_User__message4", None)
        self.__message4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "user5"):
                    opp_val = getattr(item, "user5", None)
                    
                    if opp_val == self:
                        setattr(item, "user5", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "user5"):
                    opp_val = getattr(item, "user5", None)
                    
                    setattr(item, "user5", self)
                    

    @property
    def myprofile0(self):
        return self.__myprofile0
    @myprofile0.setter
    def myprofile0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_User__myprofile0", None)
        self.__myprofile0 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "user1"):
                opp_val = getattr(old_value, "user1", None)
                if opp_val == self:
                    setattr(old_value, "user1", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "user1"):
                opp_val = getattr(value, "user1", None)
                setattr(value, "user1", self)

    @property
    def group2(self):
        return self.__group2
    @group2.setter
    def group2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_User__group2", None)
        self.__group2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "user3"):
                    opp_val = getattr(item, "user3", None)
                    
                    if opp_val == self:
                        setattr(item, "user3", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "user3"):
                    opp_val = getattr(item, "user3", None)
                    
                    setattr(item, "user3", self)
                    

    @property
    def settings20(self):
        return self.__settings20
    @settings20.setter
    def settings20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_User__settings20", None)
        self.__settings20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "user21"):
                opp_val = getattr(old_value, "user21", None)
                if opp_val == self:
                    setattr(old_value, "user21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "user21"):
                opp_val = getattr(value, "user21", None)
                setattr(value, "user21", self)

    @property
    def profile22(self):
        return self.__profile22
    @profile22.setter
    def profile22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_User__profile22", None)
        self.__profile22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "user23"):
                opp_val = getattr(old_value, "user23", None)
                if opp_val == self:
                    setattr(old_value, "user23", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "user23"):
                opp_val = getattr(value, "user23", None)
                setattr(value, "user23", self)

