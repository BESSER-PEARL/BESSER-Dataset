from __future__ import annotations
from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class ResourceType(Enum):
    pass
class Enumeration(Enum):
    pass
class ScopeType(Enum):
    pass
class AllowType(Enum):
    pass
class CrudType(Enum):
    pass
class ApprovalType(Enum):
    pass

############################################
# Definition of Classes
############################################










class Permission:

    def __init__(self, Id: int, Name: str, Crud: CrudType, Allow: AllowType, Scope: ScopeType):
        self.Id = Id
        self.Name = Name
        self.Crud = Crud
        self.Allow = Allow
        self.Scope = Scope
        
        pass
    @property
    def Scope(self):
        return self.__Scope
    @Scope.setter
    def Scope(self, Scope: ScopeType):
        self.__Scope = Scope

    @property
    def Id(self):
        return self.__Id
    @Id.setter
    def Id(self, Id: int):
        self.__Id = Id

    @property
    def Crud(self):
        return self.__Crud
    @Crud.setter
    def Crud(self, Crud: CrudType):
        self.__Crud = Crud

    @property
    def Name(self):
        return self.__Name
    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def Allow(self):
        return self.__Allow
    @Allow.setter
    def Allow(self, Allow: AllowType):
        self.__Allow = Allow



class Resource:

    def __init__(self, Id: int, Name: str, Description: str, NumberAvailable: int, Type: ResourceType, Private: bool):
        self.Id = Id
        self.Name = Name
        self.Description = Description
        self.NumberAvailable = NumberAvailable
        self.Type = Type
        self.Private = Private
        
        pass
    @property
    def Id(self):
        return self.__Id
    @Id.setter
    def Id(self, Id: int):
        self.__Id = Id

    @property
    def Name(self):
        return self.__Name
    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def Description(self):
        return self.__Description
    @Description.setter
    def Description(self, Description: str):
        self.__Description = Description

    @property
    def Type(self):
        return self.__Type
    @Type.setter
    def Type(self, Type: ResourceType):
        self.__Type = Type

    @property
    def NumberAvailable(self):
        return self.__NumberAvailable
    @NumberAvailable.setter
    def NumberAvailable(self, NumberAvailable: int):
        self.__NumberAvailable = NumberAvailable

    @property
    def Private(self):
        return self.__Private
    @Private.setter
    def Private(self, Private: bool):
        self.__Private = Private



class Panel:

    def __init__(self, Id: int, Name: str, Submitter: User, Description: str, Scheduled: str, Length: int, PreBufferTime: int, PostBufferTime: int, Approval: ApprovalType, Resources: Resource, Private: bool, Panelists: User):
        self.Id = Id
        self.Name = Name
        self.Submitter = Submitter
        self.Description = Description
        self.Scheduled = Scheduled
        self.Length = Length
        self.PreBufferTime = PreBufferTime
        self.PostBufferTime = PostBufferTime
        self.Approval = Approval
        self.Resources = Resources
        self.Private = Private
        self.Panelists = Panelists
        
        pass
    @property
    def Name(self):
        return self.__Name
    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def Panelists(self):
        return self.__Panelists
    @Panelists.setter
    def Panelists(self, Panelists: User):
        self.__Panelists = Panelists

    @property
    def Private(self):
        return self.__Private
    @Private.setter
    def Private(self, Private: bool):
        self.__Private = Private

    @property
    def Scheduled(self):
        return self.__Scheduled
    @Scheduled.setter
    def Scheduled(self, Scheduled: str):
        self.__Scheduled = Scheduled

    @property
    def Approval(self):
        return self.__Approval
    @Approval.setter
    def Approval(self, Approval: ApprovalType):
        self.__Approval = Approval

    @property
    def Submitter(self):
        return self.__Submitter
    @Submitter.setter
    def Submitter(self, Submitter: User):
        self.__Submitter = Submitter

    @property
    def Id(self):
        return self.__Id
    @Id.setter
    def Id(self, Id: int):
        self.__Id = Id

    @property
    def Resources(self):
        return self.__Resources
    @Resources.setter
    def Resources(self, Resources: Resource):
        self.__Resources = Resources

    @property
    def Description(self):
        return self.__Description
    @Description.setter
    def Description(self, Description: str):
        self.__Description = Description

    @property
    def PostBufferTime(self):
        return self.__PostBufferTime
    @PostBufferTime.setter
    def PostBufferTime(self, PostBufferTime: int):
        self.__PostBufferTime = PostBufferTime

    @property
    def PreBufferTime(self):
        return self.__PreBufferTime
    @PreBufferTime.setter
    def PreBufferTime(self, PreBufferTime: int):
        self.__PreBufferTime = PreBufferTime

    @property
    def Length(self):
        return self.__Length
    @Length.setter
    def Length(self, Length: int):
        self.__Length = Length



class Event:

    def __init__(self, Id: int, Name: str, Description: str, Date: str, Panels: Panel, Resources: Resource, Groups: Group):
        self.Id = Id
        self.Name = Name
        self.Description = Description
        self.Date = Date
        self.Panels = Panels
        self.Resources = Resources
        self.Groups = Groups
        
        pass
    @property
    def Date(self):
        return self.__Date
    @Date.setter
    def Date(self, Date: str):
        self.__Date = Date

    @property
    def Panels(self):
        return self.__Panels
    @Panels.setter
    def Panels(self, Panels: Panel):
        self.__Panels = Panels

    @property
    def Name(self):
        return self.__Name
    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def Id(self):
        return self.__Id
    @Id.setter
    def Id(self, Id: int):
        self.__Id = Id

    @property
    def Groups(self):
        return self.__Groups
    @Groups.setter
    def Groups(self, Groups: Group):
        self.__Groups = Groups

    @property
    def Description(self):
        return self.__Description
    @Description.setter
    def Description(self, Description: str):
        self.__Description = Description

    @property
    def Resources(self):
        return self.__Resources
    @Resources.setter
    def Resources(self, Resources: Resource):
        self.__Resources = Resources



class Group:

    def __init__(self, Id: int, Name: str, Users: User, Permissions: Permission, Scope: ScopeType, ScopeId: int):
        self.Id = Id
        self.Name = Name
        self.Users = Users
        self.Permissions = Permissions
        self.Scope = Scope
        self.ScopeId = ScopeId
        
        pass
    @property
    def ScopeId(self):
        return self.__ScopeId
    @ScopeId.setter
    def ScopeId(self, ScopeId: int):
        self.__ScopeId = ScopeId

    @property
    def Scope(self):
        return self.__Scope
    @Scope.setter
    def Scope(self, Scope: ScopeType):
        self.__Scope = Scope

    @property
    def Permissions(self):
        return self.__Permissions
    @Permissions.setter
    def Permissions(self, Permissions: Permission):
        self.__Permissions = Permissions

    @property
    def Name(self):
        return self.__Name
    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def Users(self):
        return self.__Users
    @Users.setter
    def Users(self, Users: User):
        self.__Users = Users

    @property
    def Id(self):
        return self.__Id
    @Id.setter
    def Id(self, Id: int):
        self.__Id = Id



class User:

    def __init__(self, UserName: str, UserHash: int, UserNameFull: str, EmailAddress: str, Password: str, Id: int, FirstName: str, LastName: str):
        self.UserName = UserName
        self.UserHash = UserHash
        self.UserNameFull = UserNameFull
        self.EmailAddress = EmailAddress
        self.Password = Password
        self.Id = Id
        self.FirstName = FirstName
        self.LastName = LastName
        
        pass
    @property
    def UserNameFull(self):
        return self.__UserNameFull
    @UserNameFull.setter
    def UserNameFull(self, UserNameFull: str):
        self.__UserNameFull = UserNameFull

    @property
    def LastName(self):
        return self.__LastName
    @LastName.setter
    def LastName(self, LastName: str):
        self.__LastName = LastName

    @property
    def UserName(self):
        return self.__UserName
    @UserName.setter
    def UserName(self, UserName: str):
        self.__UserName = UserName

    @property
    def FirstName(self):
        return self.__FirstName
    @FirstName.setter
    def FirstName(self, FirstName: str):
        self.__FirstName = FirstName

    @property
    def EmailAddress(self):
        return self.__EmailAddress
    @EmailAddress.setter
    def EmailAddress(self, EmailAddress: str):
        self.__EmailAddress = EmailAddress

    @property
    def Id(self):
        return self.__Id
    @Id.setter
    def Id(self, Id: int):
        self.__Id = Id

    @property
    def UserHash(self):
        return self.__UserHash
    @UserHash.setter
    def UserHash(self, UserHash: int):
        self.__UserHash = UserHash

    @property
    def Password(self):
        return self.__Password
    @Password.setter
    def Password(self, Password: str):
        self.__Password = Password



class Organization:

    def __init__(self, Id: int, Name: str, Description: str, Url: str, Groups: Group, Events: Event, Owners: User):
        self.Id = Id
        self.Name = Name
        self.Description = Description
        self.Url = Url
        self.Groups = Groups
        self.Events = Events
        self.Owners = Owners
        
        pass
    @property
    def Events(self):
        return self.__Events
    @Events.setter
    def Events(self, Events: Event):
        self.__Events = Events

    @property
    def Owners(self):
        return self.__Owners
    @Owners.setter
    def Owners(self, Owners: User):
        self.__Owners = Owners

    @property
    def Url(self):
        return self.__Url
    @Url.setter
    def Url(self, Url: str):
        self.__Url = Url

    @property
    def Name(self):
        return self.__Name
    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def Description(self):
        return self.__Description
    @Description.setter
    def Description(self, Description: str):
        self.__Description = Description

    @property
    def Groups(self):
        return self.__Groups
    @Groups.setter
    def Groups(self, Groups: Group):
        self.__Groups = Groups

    @property
    def Id(self):
        return self.__Id
    @Id.setter
    def Id(self, Id: int):
        self.__Id = Id

