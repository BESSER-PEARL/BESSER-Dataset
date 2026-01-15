from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class lobj_InternalRef:

    def __init__(self, ref: str, file: str, reftype: str, id: str, lobj_InternalRef: "lobj_Precognition" = None, lobj_InternalRef199: "lobj_Language" = None):
        self.ref = ref
        self.file = file
        self.reftype = reftype
        self.id = id
        self.lobj_InternalRef = lobj_InternalRef
        self.lobj_InternalRef199 = lobj_InternalRef199
        
    @property
    def file(self) -> str:
        return self.__file

    @file.setter
    def file(self, file: str):
        self.__file = file

    @property
    def reftype(self) -> str:
        return self.__reftype

    @reftype.setter
    def reftype(self, reftype: str):
        self.__reftype = reftype

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def ref(self) -> str:
        return self.__ref

    @ref.setter
    def ref(self, ref: str):
        self.__ref = ref

    @property
    def lobj_InternalRef199(self):
        return self.__lobj_InternalRef199

    @lobj_InternalRef199.setter
    def lobj_InternalRef199(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lobj_InternalRef__lobj_InternalRef199", None)
        self.__lobj_InternalRef199 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lobj_Language200"):
                opp_val = getattr(old_value, "lobj_Language200", None)
                if opp_val == self:
                    setattr(old_value, "lobj_Language200", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lobj_Language200"):
                opp_val = getattr(value, "lobj_Language200", None)
                setattr(value, "lobj_Language200", self)

    @property
    def lobj_InternalRef(self):
        return self.__lobj_InternalRef

    @lobj_InternalRef.setter
    def lobj_InternalRef(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lobj_InternalRef__lobj_InternalRef", None)
        self.__lobj_InternalRef = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lobj_Precognition197"):
                opp_val = getattr(old_value, "lobj_Precognition197", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lobj_Precognition197"):
                opp_val = getattr(value, "lobj_Precognition197", None)
                if opp_val is None:
                    setattr(value, "lobj_Precognition197", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class lobj_Publisher:

    def __init__(self, publishername: str, id: str, lobj_Publisher: "lobj_Address" = None, lobj_Publisher190: "lobj_PublishInfo" = None):
        self.publishername = publishername
        self.id = id
        self.lobj_Publisher = lobj_Publisher
        self.lobj_Publisher190 = lobj_Publisher190
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def publishername(self) -> str:
        return self.__publishername

    @publishername.setter
    def publishername(self, publishername: str):
        self.__publishername = publishername

    @property
    def lobj_Publisher(self):
        return self.__lobj_Publisher

    @lobj_Publisher.setter
    def lobj_Publisher(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lobj_Publisher__lobj_Publisher", None)
        self.__lobj_Publisher = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lobj_Address187"):
                opp_val = getattr(old_value, "lobj_Address187", None)
                if opp_val == self:
                    setattr(old_value, "lobj_Address187", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lobj_Address187"):
                opp_val = getattr(value, "lobj_Address187", None)
                setattr(value, "lobj_Address187", self)

    @property
    def lobj_Publisher190(self):
        return self.__lobj_Publisher190

    @lobj_Publisher190.setter
    def lobj_Publisher190(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lobj_Publisher__lobj_Publisher190", None)
        self.__lobj_Publisher190 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lobj_PublishInfo189"):
                opp_val = getattr(old_value, "lobj_PublishInfo189", None)
                if opp_val == self:
                    setattr(old_value, "lobj_PublishInfo189", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lobj_PublishInfo189"):
                opp_val = getattr(value, "lobj_PublishInfo189", None)
                setattr(value, "lobj_PublishInfo189", self)

class lobj_Note:

    def __init__(self, date: date, noteAuthor: str, content: str, id: str, lobj_Note: "lobj_Sharednotes" = None):
        self.date = date
        self.noteAuthor = noteAuthor
        self.content = content
        self.id = id
        self.lobj_Note = lobj_Note
        
    @property
    def noteAuthor(self) -> str:
        return self.__noteAuthor

    @noteAuthor.setter
    def noteAuthor(self, noteAuthor: str):
        self.__noteAuthor = noteAuthor

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def content(self) -> str:
        return self.__content

    @content.setter
    def content(self, content: str):
        self.__content = content

    @property
    def date(self) -> date:
        return self.__date

    @date.setter
    def date(self, date: date):
        self.__date = date

    @property
    def lobj_Note(self):
        return self.__lobj_Note

    @lobj_Note.setter
    def lobj_Note(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lobj_Note__lobj_Note", None)
        self.__lobj_Note = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lobj_Sharednotes192"):
                opp_val = getattr(old_value, "lobj_Sharednotes192", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lobj_Sharednotes192"):
                opp_val = getattr(value, "lobj_Sharednotes192", None)
                if opp_val is None:
                    setattr(value, "lobj_Sharednotes192", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class lobj_AuthorizationTypes:

    def __init__(self, authType: str, authTypeDesc: str, readOnly: bool, id: str, lobj_AuthorizationTypes: "lobj_Userauthorization" = None, lobj_AuthorizationTypes218: "lobj_User" = None):
        self.authType = authType
        self.authTypeDesc = authTypeDesc
        self.readOnly = readOnly
        self.id = id
        self.lobj_AuthorizationTypes = lobj_AuthorizationTypes
        self.lobj_AuthorizationTypes218 = lobj_AuthorizationTypes218
        
    @property
    def authTypeDesc(self) -> str:
        return self.__authTypeDesc

    @authTypeDesc.setter
    def authTypeDesc(self, authTypeDesc: str):
        self.__authTypeDesc = authTypeDesc

    @property
    def authType(self) -> str:
        return self.__authType

    @authType.setter
    def authType(self, authType: str):
        self.__authType = authType

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def readOnly(self) -> bool:
        return self.__readOnly

    @readOnly.setter
    def readOnly(self, readOnly: bool):
        self.__readOnly = readOnly

    @property
    def lobj_AuthorizationTypes(self):
        return self.__lobj_AuthorizationTypes

    @lobj_AuthorizationTypes.setter
    def lobj_AuthorizationTypes(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lobj_AuthorizationTypes__lobj_AuthorizationTypes", None)
        self.__lobj_AuthorizationTypes = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lobj_Userauthorization182"):
                opp_val = getattr(old_value, "lobj_Userauthorization182", None)
                if opp_val == self:
                    setattr(old_value, "lobj_Userauthorization182", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lobj_Userauthorization182"):
                opp_val = getattr(value, "lobj_Userauthorization182", None)
                setattr(value, "lobj_Userauthorization182", self)

    @property
    def lobj_AuthorizationTypes218(self):
        return self.__lobj_AuthorizationTypes218

    @lobj_AuthorizationTypes218.setter
    def lobj_AuthorizationTypes218(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lobj_AuthorizationTypes__lobj_AuthorizationTypes218", None)
        self.__lobj_AuthorizationTypes218 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lobj_User217"):
                opp_val = getattr(old_value, "lobj_User217", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lobj_User217"):
                opp_val = getattr(value, "lobj_User217", None)
                if opp_val is None:
                    setattr(value, "lobj_User217", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class lobj_PublishInfo:

    def __init__(self, id: str, edition: str, pubdate: date, pubsnumber: str, releaseinfo: str, lobj_PublishInfo: "lobj_LuMeta" = None, lobj_PublishInfo189: "lobj_Publisher" = None, lobj_PublishInfo209: "lobj_ModuleMeta" = None):
        self.id = id
        self.edition = edition
        self.pubdate = pubdate
        self.pubsnumber = pubsnumber
        self.releaseinfo = releaseinfo
        self.lobj_PublishInfo = lobj_PublishInfo
        self.lobj_PublishInfo189 = lobj_PublishInfo189
        self.lobj_PublishInfo209 = lobj_PublishInfo209
        
    @property
    def releaseinfo(self) -> str:
        return self.__releaseinfo

    @releaseinfo.setter
    def releaseinfo(self, releaseinfo: str):
        self.__releaseinfo = releaseinfo

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def pubsnumber(self) -> str:
        return self.__pubsnumber

    @pubsnumber.setter
    def pubsnumber(self, pubsnumber: str):
        self.__pubsnumber = pubsnumber

    @property
    def pubdate(self) -> date:
        return self.__pubdate

    @pubdate.setter
    def pubdate(self, pubdate: date):
        self.__pubdate = pubdate

    @property
    def edition(self) -> str:
        return self.__edition

    @edition.setter
    def edition(self, edition: str):
        self.__edition = edition

    @property
    def lobj_PublishInfo209(self):
        return self.__lobj_PublishInfo209

    @lobj_PublishInfo209.setter
    def lobj_PublishInfo209(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lobj_PublishInfo__lobj_PublishInfo209", None)
        self.__lobj_PublishInfo209 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lobj_ModuleMeta208"):
                opp_val = getattr(old_value, "lobj_ModuleMeta208", None)
                if opp_val == self:
                    setattr(old_value, "lobj_ModuleMeta208", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lobj_ModuleMeta208"):
                opp_val = getattr(value, "lobj_ModuleMeta208", None)
                setattr(value, "lobj_ModuleMeta208", self)

    @property
    def lobj_PublishInfo189(self):
        return self.__lobj_PublishInfo189

    @lobj_PublishInfo189.setter
    def lobj_PublishInfo189(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lobj_PublishInfo__lobj_PublishInfo189", None)
        self.__lobj_PublishInfo189 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lobj_Publisher190"):
                opp_val = getattr(old_value, "lobj_Publisher190", None)
                if opp_val == self:
                    setattr(old_value, "lobj_Publisher190", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lobj_Publisher190"):
                opp_val = getattr(value, "lobj_Publisher190", None)
                setattr(value, "lobj_Publisher190", self)

    @property
    def lobj_PublishInfo(self):
        return self.__lobj_PublishInfo

    @lobj_PublishInfo.setter
    def lobj_PublishInfo(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lobj_PublishInfo__lobj_PublishInfo", None)
        self.__lobj_PublishInfo = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lobj_LuMeta174"):
                opp_val = getattr(old_value, "lobj_LuMeta174", None)
                if opp_val == self:
                    setattr(old_value, "lobj_LuMeta174", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lobj_LuMeta174"):
                opp_val = getattr(value, "lobj_LuMeta174", None)
                setattr(value, "lobj_LuMeta174", self)

class lobj_Precognition:

    def __init__(self, precog: str, id: str, lobj_Precognition: "lobj_DidacMeta" = None, lobj_Precognition197: set["lobj_InternalRef"] = None):
        self.precog = precog
        self.id = id
        self.lobj_Precognition = lobj_Precognition
        self.lobj_Precognition197 = lobj_Precognition197 if lobj_Precognition197 is not None else set()
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def precog(self) -> str:
        return self.__precog

    @precog.setter
    def precog(self, precog: str):
        self.__precog = precog

    @property
    def lobj_Precognition(self):
        return self.__lobj_Precognition

    @lobj_Precognition.setter
    def lobj_Precognition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lobj_Precognition__lobj_Precognition", None)
        self.__lobj_Precognition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lobj_DidacMeta163"):
                opp_val = getattr(old_value, "lobj_DidacMeta163", None)
                if opp_val == self:
                    setattr(old_value, "lobj_DidacMeta163", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lobj_DidacMeta163"):
                opp_val = getattr(value, "lobj_DidacMeta163", None)
                setattr(value, "lobj_DidacMeta163", self)

    @property
    def lobj_Precognition197(self):
        return self.__lobj_Precognition197

    @lobj_Precognition197.setter
    def lobj_Precognition197(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lobj_Precognition__lobj_Precognition197", None)
        self.__lobj_Precognition197 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "lobj_InternalRef"):
                    opp_val = getattr(item, "lobj_InternalRef", None)
                    
                    if opp_val == self:
                        setattr(item, "lobj_InternalRef", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "lobj_InternalRef"):
                    opp_val = getattr(item, "lobj_InternalRef", None)
                    
                    setattr(item, "lobj_InternalRef", self)
                    

class SimpleDidacMeta:

    pass
class lobj_DidacMeta(SimpleDidacMeta):

    def __init__(self, goal: str, lobj_DidacMeta: "lobj_CourseMeta" = None, lobj_DidacMeta163: "lobj_Precognition" = None, lobj_DidacMeta167: "lobj_LuMeta" = None, lobj_DidacMeta203: "lobj_ModuleMeta" = None):
        self.goal = goal
        self.lobj_DidacMeta = lobj_DidacMeta
        self.lobj_DidacMeta163 = lobj_DidacMeta163
        self.lobj_DidacMeta167 = lobj_DidacMeta167
        self.lobj_DidacMeta203 = lobj_DidacMeta203
        
    @property
    def goal(self) -> str:
        return self.__goal

    @goal.setter
    def goal(self, goal: str):
        self.__goal = goal

    @property
    def lobj_DidacMeta163(self):
        return self.__lobj_DidacMeta163

    @lobj_DidacMeta163.setter
    def lobj_DidacMeta163(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lobj_DidacMeta__lobj_DidacMeta163", None)
        self.__lobj_DidacMeta163 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lobj_Precognition"):
                opp_val = getattr(old_value, "lobj_Precognition", None)
                if opp_val == self:
                    setattr(old_value, "lobj_Precognition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lobj_Precognition"):
                opp_val = getattr(value, "lobj_Precognition", None)
                setattr(value, "lobj_Precognition", self)

    @property
    def lobj_DidacMeta203(self):
        return self.__lobj_DidacMeta203

    @lobj_DidacMeta203.setter
    def lobj_DidacMeta203(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lobj_DidacMeta__lobj_DidacMeta203", None)
        self.__lobj_DidacMeta203 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lobj_ModuleMeta202"):
                opp_val = getattr(old_value, "lobj_ModuleMeta202", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lobj_ModuleMeta202"):
                opp_val = getattr(value, "lobj_ModuleMeta202", None)
                if opp_val is None:
                    setattr(value, "lobj_ModuleMeta202", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def lobj_DidacMeta167(self):
        return self.__lobj_DidacMeta167

    @lobj_DidacMeta167.setter
    def lobj_DidacMeta167(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lobj_DidacMeta__lobj_DidacMeta167", None)
        self.__lobj_DidacMeta167 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lobj_LuMeta166"):
                opp_val = getattr(old_value, "lobj_LuMeta166", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lobj_LuMeta166"):
                opp_val = getattr(value, "lobj_LuMeta166", None)
                if opp_val is None:
                    setattr(value, "lobj_LuMeta166", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def lobj_DidacMeta(self):
        return self.__lobj_DidacMeta

    @lobj_DidacMeta.setter
    def lobj_DidacMeta(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lobj_DidacMeta__lobj_DidacMeta", None)
        self.__lobj_DidacMeta = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lobj_CourseMeta152"):
                opp_val = getattr(old_value, "lobj_CourseMeta152", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lobj_CourseMeta152"):
                opp_val = getattr(value, "lobj_CourseMeta152", None)
                if opp_val is None:
                    setattr(value, "lobj_CourseMeta152", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class lobj_Domain:

    def __init__(self, name: str, description: str, creationDate: date, serverURL: str, id: str, Domain: "lobj_Blocktype" = None, domains: set["lobj_Blocktype"] = None, lobj_Domain: "lobj_LuMeta" = None):
        self.name = name
        self.description = description
        self.creationDate = creationDate
        self.serverURL = serverURL
        self.id = id
        self.Domain = Domain
        self.domains = domains if domains is not None else set()
        self.lobj_Domain = lobj_Domain
        
    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def creationDate(self) -> date:
        return self.__creationDate

    @creationDate.setter
    def creationDate(self, creationDate: date):
        self.__creationDate = creationDate

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def serverURL(self) -> str:
        return self.__serverURL

    @serverURL.setter
    def serverURL(self, serverURL: str):
        self.__serverURL = serverURL

    @property
    def Domain(self):
        return self.__Domain

    @Domain.setter
    def Domain(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lobj_Domain__Domain", None)
        self.__Domain = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "blocktypes"):
                opp_val = getattr(old_value, "blocktypes", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "blocktypes"):
                opp_val = getattr(value, "blocktypes", None)
                if opp_val is None:
                    setattr(value, "blocktypes", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def lobj_Domain(self):
        return self.__lobj_Domain

    @lobj_Domain.setter
    def lobj_Domain(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lobj_Domain__lobj_Domain", None)
        self.__lobj_Domain = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lobj_LuMeta169"):
                opp_val = getattr(old_value, "lobj_LuMeta169", None)
                if opp_val == self:
                    setattr(old_value, "lobj_LuMeta169", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lobj_LuMeta169"):
                opp_val = getattr(value, "lobj_LuMeta169", None)
                setattr(value, "lobj_LuMeta169", self)

    @property
    def domains(self):
        return self.__domains

    @domains.setter
    def domains(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lobj_Domain__domains", None)
        self.__domains = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Blocktype"):
                    opp_val = getattr(item, "Blocktype", None)
                    
                    if opp_val == self:
                        setattr(item, "Blocktype", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Blocktype"):
                    opp_val = getattr(item, "Blocktype", None)
                    
                    setattr(item, "Blocktype", self)
                    

class lobj_Blocktype:

    def __init__(self, description: str, creationDate: date, name: str, styleRef: str, id: str, lobj_Blocktype: "lobj_BlockMeta" = None, blocktypes: set["lobj_Domain"] = None, Blocktype: "lobj_Domain" = None):
        self.description = description
        self.creationDate = creationDate
        self.name = name
        self.styleRef = styleRef
        self.id = id
        self.lobj_Blocktype = lobj_Blocktype
        self.blocktypes = blocktypes if blocktypes is not None else set()
        self.Blocktype = Blocktype
        
    @property
    def styleRef(self) -> str:
        return self.__styleRef

    @styleRef.setter
    def styleRef(self, styleRef: str):
        self.__styleRef = styleRef

    @property
    def creationDate(self) -> date:
        return self.__creationDate

    @creationDate.setter
    def creationDate(self, creationDate: date):
        self.__creationDate = creationDate

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def lobj_Blocktype(self):
        return self.__lobj_Blocktype

    @lobj_Blocktype.setter
    def lobj_Blocktype(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lobj_Blocktype__lobj_Blocktype", None)
        self.__lobj_Blocktype = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lobj_BlockMeta140"):
                opp_val = getattr(old_value, "lobj_BlockMeta140", None)
                if opp_val == self:
                    setattr(old_value, "lobj_BlockMeta140", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lobj_BlockMeta140"):
                opp_val = getattr(value, "lobj_BlockMeta140", None)
                setattr(value, "lobj_BlockMeta140", self)

    @property
    def Blocktype(self):
        return self.__Blocktype

    @Blocktype.setter
    def Blocktype(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lobj_Blocktype__Blocktype", None)
        self.__Blocktype = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domains"):
                opp_val = getattr(old_value, "domains", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domains"):
                opp_val = getattr(value, "domains", None)
                if opp_val is None:
                    setattr(value, "domains", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def blocktypes(self):
        return self.__blocktypes

    @blocktypes.setter
    def blocktypes(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lobj_Blocktype__blocktypes", None)
        self.__blocktypes = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Domain"):
                    opp_val = getattr(item, "Domain", None)
                    
                    if opp_val == self:
                        setattr(item, "Domain", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Domain"):
                    opp_val = getattr(item, "Domain", None)
                    
                    setattr(item, "Domain", self)
                    

class lobj_Person:

    def __init__(self, contrib: str, honorific: str, firstname: str, surname: str, personblurb: str, id: str, lobj_Person: "lobj_Author" = None, lobj_Person184: set["lobj_Affiliation"] = None):
        self.contrib = contrib
        self.honorific = honorific
        self.firstname = firstname
        self.surname = surname
        self.personblurb = personblurb
        self.id = id
        self.lobj_Person = lobj_Person
        self.lobj_Person184 = lobj_Person184 if lobj_Person184 is not None else set()
        
    @property
    def firstname(self) -> str:
        return self.__firstname

    @firstname.setter
    def firstname(self, firstname: str):
        self.__firstname = firstname

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def contrib(self) -> str:
        return self.__contrib

    @contrib.setter
    def contrib(self, contrib: str):
        self.__contrib = contrib

    @property
    def surname(self) -> str:
        return self.__surname

    @surname.setter
    def surname(self, surname: str):
        self.__surname = surname

    @property
    def honorific(self) -> str:
        return self.__honorific

    @honorific.setter
    def honorific(self, honorific: str):
        self.__honorific = honorific

    @property
    def personblurb(self) -> str:
        return self.__personblurb

    @personblurb.setter
    def personblurb(self, personblurb: str):
        self.__personblurb = personblurb

    @property
    def lobj_Person184(self):
        return self.__lobj_Person184

    @lobj_Person184.setter
    def lobj_Person184(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lobj_Person__lobj_Person184", None)
        self.__lobj_Person184 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "lobj_Affiliation185"):
                    opp_val = getattr(item, "lobj_Affiliation185", None)
                    
                    if opp_val == self:
                        setattr(item, "lobj_Affiliation185", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "lobj_Affiliation185"):
                    opp_val = getattr(item, "lobj_Affiliation185", None)
                    
                    setattr(item, "lobj_Affiliation185", self)
                    

    @property
    def lobj_Person(self):
        return self.__lobj_Person

    @lobj_Person.setter
    def lobj_Person(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lobj_Person__lobj_Person", None)
        self.__lobj_Person = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lobj_Author"):
                opp_val = getattr(old_value, "lobj_Author", None)
                if opp_val == self:
                    setattr(old_value, "lobj_Author", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lobj_Author"):
                opp_val = getattr(value, "lobj_Author", None)
                setattr(value, "lobj_Author", self)

class lobj_Author:

    def __init__(self, id: str, credittype: str, email: str, lobj_Author: "lobj_Person" = None, lobj_Author137: "lobj_Address" = None, lobj_Author172: "lobj_LuMeta" = None, lobj_Author206: "lobj_ModuleMeta" = None, lobj_Author215: "lobj_Source" = None):
        self.id = id
        self.credittype = credittype
        self.email = email
        self.lobj_Author = lobj_Author
        self.lobj_Author137 = lobj_Author137
        self.lobj_Author172 = lobj_Author172
        self.lobj_Author206 = lobj_Author206
        self.lobj_Author215 = lobj_Author215
        
    @property
    def credittype(self) -> str:
        return self.__credittype

    @credittype.setter
    def credittype(self, credittype: str):
        self.__credittype = credittype

    @property
    def email(self) -> str:
        return self.__email

    @email.setter
    def email(self, email: str):
        self.__email = email

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def lobj_Author137(self):
        return self.__lobj_Author137

    @lobj_Author137.setter
    def lobj_Author137(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lobj_Author__lobj_Author137", None)
        self.__lobj_Author137 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lobj_Address138"):
                opp_val = getattr(old_value, "lobj_Address138", None)
                if opp_val == self:
                    setattr(old_value, "lobj_Address138", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lobj_Address138"):
                opp_val = getattr(value, "lobj_Address138", None)
                setattr(value, "lobj_Address138", self)

    @property
    def lobj_Author172(self):
        return self.__lobj_Author172

    @lobj_Author172.setter
    def lobj_Author172(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lobj_Author__lobj_Author172", None)
        self.__lobj_Author172 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lobj_LuMeta171"):
                opp_val = getattr(old_value, "lobj_LuMeta171", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lobj_LuMeta171"):
                opp_val = getattr(value, "lobj_LuMeta171", None)
                if opp_val is None:
                    setattr(value, "lobj_LuMeta171", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def lobj_Author(self):
        return self.__lobj_Author

    @lobj_Author.setter
    def lobj_Author(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lobj_Author__lobj_Author", None)
        self.__lobj_Author = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lobj_Person"):
                opp_val = getattr(old_value, "lobj_Person", None)
                if opp_val == self:
                    setattr(old_value, "lobj_Person", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lobj_Person"):
                opp_val = getattr(value, "lobj_Person", None)
                setattr(value, "lobj_Person", self)

    @property
    def lobj_Author206(self):
        return self.__lobj_Author206

    @lobj_Author206.setter
    def lobj_Author206(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lobj_Author__lobj_Author206", None)
        self.__lobj_Author206 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lobj_ModuleMeta205"):
                opp_val = getattr(old_value, "lobj_ModuleMeta205", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lobj_ModuleMeta205"):
                opp_val = getattr(value, "lobj_ModuleMeta205", None)
                if opp_val is None:
                    setattr(value, "lobj_ModuleMeta205", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def lobj_Author215(self):
        return self.__lobj_Author215

    @lobj_Author215.setter
    def lobj_Author215(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lobj_Author__lobj_Author215", None)
        self.__lobj_Author215 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lobj_Source214"):
                opp_val = getattr(old_value, "lobj_Source214", None)
                if opp_val == self:
                    setattr(old_value, "lobj_Source214", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lobj_Source214"):
                opp_val = getattr(value, "lobj_Source214", None)
                setattr(value, "lobj_Source214", self)

class lobj_Affiliation:

    def __init__(self, shortaffil: str, jobtitle: str, orgname: str, orgdiv: str, id: str, lobj_Affiliation: "lobj_Address" = None, lobj_Affiliation185: "lobj_Person" = None):
        self.shortaffil = shortaffil
        self.jobtitle = jobtitle
        self.orgname = orgname
        self.orgdiv = orgdiv
        self.id = id
        self.lobj_Affiliation = lobj_Affiliation
        self.lobj_Affiliation185 = lobj_Affiliation185
        
    @property
    def orgname(self) -> str:
        return self.__orgname

    @orgname.setter
    def orgname(self, orgname: str):
        self.__orgname = orgname

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def jobtitle(self) -> str:
        return self.__jobtitle

    @jobtitle.setter
    def jobtitle(self, jobtitle: str):
        self.__jobtitle = jobtitle

    @property
    def orgdiv(self) -> str:
        return self.__orgdiv

    @orgdiv.setter
    def orgdiv(self, orgdiv: str):
        self.__orgdiv = orgdiv

    @property
    def shortaffil(self) -> str:
        return self.__shortaffil

    @shortaffil.setter
    def shortaffil(self, shortaffil: str):
        self.__shortaffil = shortaffil

    @property
    def lobj_Affiliation185(self):
        return self.__lobj_Affiliation185

    @lobj_Affiliation185.setter
    def lobj_Affiliation185(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lobj_Affiliation__lobj_Affiliation185", None)
        self.__lobj_Affiliation185 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lobj_Person184"):
                opp_val = getattr(old_value, "lobj_Person184", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lobj_Person184"):
                opp_val = getattr(value, "lobj_Person184", None)
                if opp_val is None:
                    setattr(value, "lobj_Person184", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def lobj_Affiliation(self):
        return self.__lobj_Affiliation

    @lobj_Affiliation.setter
    def lobj_Affiliation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lobj_Affiliation__lobj_Affiliation", None)
        self.__lobj_Affiliation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lobj_Address"):
                opp_val = getattr(old_value, "lobj_Address", None)
                if opp_val == self:
                    setattr(old_value, "lobj_Address", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lobj_Address"):
                opp_val = getattr(value, "lobj_Address", None)
                setattr(value, "lobj_Address", self)

class lobj_Address:

    def __init__(self, fax: str, email: str, otheraddr: str, street: str, postcode: str, city: str, state: str, country: str, phone: str, id: str, lobj_Address: "lobj_Affiliation" = None, lobj_Address138: "lobj_Author" = None, lobj_Address187: "lobj_Publisher" = None):
        self.fax = fax
        self.email = email
        self.otheraddr = otheraddr
        self.street = street
        self.postcode = postcode
        self.city = city
        self.state = state
        self.country = country
        self.phone = phone
        self.id = id
        self.lobj_Address = lobj_Address
        self.lobj_Address138 = lobj_Address138
        self.lobj_Address187 = lobj_Address187
        
    @property
    def fax(self) -> str:
        return self.__fax

    @fax.setter
    def fax(self, fax: str):
        self.__fax = fax

    @property
    def street(self) -> str:
        return self.__street

    @street.setter
    def street(self, street: str):
        self.__street = street

    @property
    def city(self) -> str:
        return self.__city

    @city.setter
    def city(self, city: str):
        self.__city = city

    @property
    def email(self) -> str:
        return self.__email

    @email.setter
    def email(self, email: str):
        self.__email = email

    @property
    def postcode(self) -> str:
        return self.__postcode

    @postcode.setter
    def postcode(self, postcode: str):
        self.__postcode = postcode

    @property
    def otheraddr(self) -> str:
        return self.__otheraddr

    @otheraddr.setter
    def otheraddr(self, otheraddr: str):
        self.__otheraddr = otheraddr

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def country(self) -> str:
        return self.__country

    @country.setter
    def country(self, country: str):
        self.__country = country

    @property
    def state(self) -> str:
        return self.__state

    @state.setter
    def state(self, state: str):
        self.__state = state

    @property
    def phone(self) -> str:
        return self.__phone

    @phone.setter
    def phone(self, phone: str):
        self.__phone = phone

    @property
    def lobj_Address(self):
        return self.__lobj_Address

    @lobj_Address.setter
    def lobj_Address(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lobj_Address__lobj_Address", None)
        self.__lobj_Address = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lobj_Affiliation"):
                opp_val = getattr(old_value, "lobj_Affiliation", None)
                if opp_val == self:
                    setattr(old_value, "lobj_Affiliation", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lobj_Affiliation"):
                opp_val = getattr(value, "lobj_Affiliation", None)
                setattr(value, "lobj_Affiliation", self)

    @property
    def lobj_Address187(self):
        return self.__lobj_Address187

    @lobj_Address187.setter
    def lobj_Address187(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lobj_Address__lobj_Address187", None)
        self.__lobj_Address187 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lobj_Publisher"):
                opp_val = getattr(old_value, "lobj_Publisher", None)
                if opp_val == self:
                    setattr(old_value, "lobj_Publisher", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lobj_Publisher"):
                opp_val = getattr(value, "lobj_Publisher", None)
                setattr(value, "lobj_Publisher", self)

    @property
    def lobj_Address138(self):
        return self.__lobj_Address138

    @lobj_Address138.setter
    def lobj_Address138(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lobj_Address__lobj_Address138", None)
        self.__lobj_Address138 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lobj_Author137"):
                opp_val = getattr(old_value, "lobj_Author137", None)
                if opp_val == self:
                    setattr(old_value, "lobj_Author137", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lobj_Author137"):
                opp_val = getattr(value, "lobj_Author137", None)
                setattr(value, "lobj_Author137", self)

class lobj_Edition:

    def __init__(self, status: str, editionCreationDate: date, editionNr: str, editedBy: str, version: str, lastVersionNumber: str, id: str, lobj_Edition: "lobj_AccessControl" = None):
        self.status = status
        self.editionCreationDate = editionCreationDate
        self.editionNr = editionNr
        self.editedBy = editedBy
        self.version = version
        self.lastVersionNumber = lastVersionNumber
        self.id = id
        self.lobj_Edition = lobj_Edition
        
    @property
    def editionCreationDate(self) -> date:
        return self.__editionCreationDate

    @editionCreationDate.setter
    def editionCreationDate(self, editionCreationDate: date):
        self.__editionCreationDate = editionCreationDate

    @property
    def version(self) -> str:
        return self.__version

    @version.setter
    def version(self, version: str):
        self.__version = version

    @property
    def editedBy(self) -> str:
        return self.__editedBy

    @editedBy.setter
    def editedBy(self, editedBy: str):
        self.__editedBy = editedBy

    @property
    def lastVersionNumber(self) -> str:
        return self.__lastVersionNumber

    @lastVersionNumber.setter
    def lastVersionNumber(self, lastVersionNumber: str):
        self.__lastVersionNumber = lastVersionNumber

    @property
    def status(self) -> str:
        return self.__status

    @status.setter
    def status(self, status: str):
        self.__status = status

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def editionNr(self) -> str:
        return self.__editionNr

    @editionNr.setter
    def editionNr(self, editionNr: str):
        self.__editionNr = editionNr

    @property
    def lobj_Edition(self):
        return self.__lobj_Edition

    @lobj_Edition.setter
    def lobj_Edition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lobj_Edition__lobj_Edition", None)
        self.__lobj_Edition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lobj_AccessControl133"):
                opp_val = getattr(old_value, "lobj_AccessControl133", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lobj_AccessControl133"):
                opp_val = getattr(value, "lobj_AccessControl133", None)
                if opp_val is None:
                    setattr(value, "lobj_AccessControl133", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class lobj_Userauthorization:

    def __init__(self, id: str, lobj_Userauthorization: "lobj_AccessControl" = None, lobj_Userauthorization179: "lobj_User" = None, lobj_Userauthorization182: "lobj_AuthorizationTypes" = None):
        self.id = id
        self.lobj_Userauthorization = lobj_Userauthorization
        self.lobj_Userauthorization179 = lobj_Userauthorization179
        self.lobj_Userauthorization182 = lobj_Userauthorization182
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def lobj_Userauthorization179(self):
        return self.__lobj_Userauthorization179

    @lobj_Userauthorization179.setter
    def lobj_Userauthorization179(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lobj_Userauthorization__lobj_Userauthorization179", None)
        self.__lobj_Userauthorization179 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lobj_User180"):
                opp_val = getattr(old_value, "lobj_User180", None)
                if opp_val == self:
                    setattr(old_value, "lobj_User180", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lobj_User180"):
                opp_val = getattr(value, "lobj_User180", None)
                setattr(value, "lobj_User180", self)

    @property
    def lobj_Userauthorization(self):
        return self.__lobj_Userauthorization

    @lobj_Userauthorization.setter
    def lobj_Userauthorization(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lobj_Userauthorization__lobj_Userauthorization", None)
        self.__lobj_Userauthorization = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lobj_AccessControl131"):
                opp_val = getattr(old_value, "lobj_AccessControl131", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lobj_AccessControl131"):
                opp_val = getattr(value, "lobj_AccessControl131", None)
                if opp_val is None:
                    setattr(value, "lobj_AccessControl131", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def lobj_Userauthorization182(self):
        return self.__lobj_Userauthorization182

    @lobj_Userauthorization182.setter
    def lobj_Userauthorization182(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lobj_Userauthorization__lobj_Userauthorization182", None)
        self.__lobj_Userauthorization182 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lobj_AuthorizationTypes"):
                opp_val = getattr(old_value, "lobj_AuthorizationTypes", None)
                if opp_val == self:
                    setattr(old_value, "lobj_AuthorizationTypes", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lobj_AuthorizationTypes"):
                opp_val = getattr(value, "lobj_AuthorizationTypes", None)
                setattr(value, "lobj_AuthorizationTypes", self)

class lobj_Sharednotes:

    def __init__(self, id: str, lobj_Sharednotes: "lobj_AccessControl" = None, lobj_Sharednotes192: set["lobj_Note"] = None):
        self.id = id
        self.lobj_Sharednotes = lobj_Sharednotes
        self.lobj_Sharednotes192 = lobj_Sharednotes192 if lobj_Sharednotes192 is not None else set()
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def lobj_Sharednotes(self):
        return self.__lobj_Sharednotes

    @lobj_Sharednotes.setter
    def lobj_Sharednotes(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lobj_Sharednotes__lobj_Sharednotes", None)
        self.__lobj_Sharednotes = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lobj_AccessControl129"):
                opp_val = getattr(old_value, "lobj_AccessControl129", None)
                if opp_val == self:
                    setattr(old_value, "lobj_AccessControl129", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lobj_AccessControl129"):
                opp_val = getattr(value, "lobj_AccessControl129", None)
                setattr(value, "lobj_AccessControl129", self)

    @property
    def lobj_Sharednotes192(self):
        return self.__lobj_Sharednotes192

    @lobj_Sharednotes192.setter
    def lobj_Sharednotes192(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lobj_Sharednotes__lobj_Sharednotes192", None)
        self.__lobj_Sharednotes192 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "lobj_Note"):
                    opp_val = getattr(item, "lobj_Note", None)
                    
                    if opp_val == self:
                        setattr(item, "lobj_Note", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "lobj_Note"):
                    opp_val = getattr(item, "lobj_Note", None)
                    
                    setattr(item, "lobj_Note", self)
                    

class lobj_User:

    def __init__(self, entryasxml: str, languagenr: str, notificationprofileasxml: str, loginname: str, password: str, firstname: str, lastname: str, matriculationnr: str, scn: str, icqnumber: str, icqpassword: str, id: str, dossierasxml: str, photo: str, onlinestatus: str, onlinedate: date, datafilter: str, inchatsince: date, contchatdate: date, chatroomnr: str, fromext: str, lastlogindate: date, currlogindate: date, lastcoursematerialnr: str, lastcoursematerialviewnr: str, authenticateldap: str, photochanged: str, lobj_User127: "lobj_AccessControl" = None, lobj_User: "lobj_AccessControl" = None, lobj_User124: "lobj_AccessControl" = None, lobj_User155: "lobj_CourseMeta" = None, lobj_User180: "lobj_Userauthorization" = None, lobj_User217: set["lobj_AuthorizationTypes"] = None):
        self.entryasxml = entryasxml
        self.languagenr = languagenr
        self.notificationprofileasxml = notificationprofileasxml
        self.loginname = loginname
        self.password = password
        self.firstname = firstname
        self.lastname = lastname
        self.matriculationnr = matriculationnr
        self.scn = scn
        self.icqnumber = icqnumber
        self.icqpassword = icqpassword
        self.id = id
        self.dossierasxml = dossierasxml
        self.photo = photo
        self.onlinestatus = onlinestatus
        self.onlinedate = onlinedate
        self.datafilter = datafilter
        self.inchatsince = inchatsince
        self.contchatdate = contchatdate
        self.chatroomnr = chatroomnr
        self.fromext = fromext
        self.lastlogindate = lastlogindate
        self.currlogindate = currlogindate
        self.lastcoursematerialnr = lastcoursematerialnr
        self.lastcoursematerialviewnr = lastcoursematerialviewnr
        self.authenticateldap = authenticateldap
        self.photochanged = photochanged
        self.lobj_User127 = lobj_User127
        self.lobj_User = lobj_User
        self.lobj_User124 = lobj_User124
        self.lobj_User155 = lobj_User155
        self.lobj_User180 = lobj_User180
        self.lobj_User217 = lobj_User217 if lobj_User217 is not None else set()
        
    @property
    def languagenr(self) -> str:
        return self.__languagenr

    @languagenr.setter
    def languagenr(self, languagenr: str):
        self.__languagenr = languagenr

    @property
    def currlogindate(self) -> date:
        return self.__currlogindate

    @currlogindate.setter
    def currlogindate(self, currlogindate: date):
        self.__currlogindate = currlogindate

    @property
    def photochanged(self) -> str:
        return self.__photochanged

    @photochanged.setter
    def photochanged(self, photochanged: str):
        self.__photochanged = photochanged

    @property
    def lastname(self) -> str:
        return self.__lastname

    @lastname.setter
    def lastname(self, lastname: str):
        self.__lastname = lastname

    @property
    def fromext(self) -> str:
        return self.__fromext

    @fromext.setter
    def fromext(self, fromext: str):
        self.__fromext = fromext

    @property
    def scn(self) -> str:
        return self.__scn

    @scn.setter
    def scn(self, scn: str):
        self.__scn = scn

    @property
    def datafilter(self) -> str:
        return self.__datafilter

    @datafilter.setter
    def datafilter(self, datafilter: str):
        self.__datafilter = datafilter

    @property
    def firstname(self) -> str:
        return self.__firstname

    @firstname.setter
    def firstname(self, firstname: str):
        self.__firstname = firstname

    @property
    def icqnumber(self) -> str:
        return self.__icqnumber

    @icqnumber.setter
    def icqnumber(self, icqnumber: str):
        self.__icqnumber = icqnumber

    @property
    def onlinestatus(self) -> str:
        return self.__onlinestatus

    @onlinestatus.setter
    def onlinestatus(self, onlinestatus: str):
        self.__onlinestatus = onlinestatus

    @property
    def lastcoursematerialviewnr(self) -> str:
        return self.__lastcoursematerialviewnr

    @lastcoursematerialviewnr.setter
    def lastcoursematerialviewnr(self, lastcoursematerialviewnr: str):
        self.__lastcoursematerialviewnr = lastcoursematerialviewnr

    @property
    def dossierasxml(self) -> str:
        return self.__dossierasxml

    @dossierasxml.setter
    def dossierasxml(self, dossierasxml: str):
        self.__dossierasxml = dossierasxml

    @property
    def notificationprofileasxml(self) -> str:
        return self.__notificationprofileasxml

    @notificationprofileasxml.setter
    def notificationprofileasxml(self, notificationprofileasxml: str):
        self.__notificationprofileasxml = notificationprofileasxml

    @property
    def authenticateldap(self) -> str:
        return self.__authenticateldap

    @authenticateldap.setter
    def authenticateldap(self, authenticateldap: str):
        self.__authenticateldap = authenticateldap

    @property
    def loginname(self) -> str:
        return self.__loginname

    @loginname.setter
    def loginname(self, loginname: str):
        self.__loginname = loginname

    @property
    def matriculationnr(self) -> str:
        return self.__matriculationnr

    @matriculationnr.setter
    def matriculationnr(self, matriculationnr: str):
        self.__matriculationnr = matriculationnr

    @property
    def photo(self) -> str:
        return self.__photo

    @photo.setter
    def photo(self, photo: str):
        self.__photo = photo

    @property
    def icqpassword(self) -> str:
        return self.__icqpassword

    @icqpassword.setter
    def icqpassword(self, icqpassword: str):
        self.__icqpassword = icqpassword

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def onlinedate(self) -> date:
        return self.__onlinedate

    @onlinedate.setter
    def onlinedate(self, onlinedate: date):
        self.__onlinedate = onlinedate

    @property
    def lastcoursematerialnr(self) -> str:
        return self.__lastcoursematerialnr

    @lastcoursematerialnr.setter
    def lastcoursematerialnr(self, lastcoursematerialnr: str):
        self.__lastcoursematerialnr = lastcoursematerialnr

    @property
    def entryasxml(self) -> str:
        return self.__entryasxml

    @entryasxml.setter
    def entryasxml(self, entryasxml: str):
        self.__entryasxml = entryasxml

    @property
    def contchatdate(self) -> date:
        return self.__contchatdate

    @contchatdate.setter
    def contchatdate(self, contchatdate: date):
        self.__contchatdate = contchatdate

    @property
    def inchatsince(self) -> date:
        return self.__inchatsince

    @inchatsince.setter
    def inchatsince(self, inchatsince: date):
        self.__inchatsince = inchatsince

    @property
    def password(self) -> str:
        return self.__password

    @password.setter
    def password(self, password: str):
        self.__password = password

    @property
    def lastlogindate(self) -> date:
        return self.__lastlogindate

    @lastlogindate.setter
    def lastlogindate(self, lastlogindate: date):
        self.__lastlogindate = lastlogindate

    @property
    def chatroomnr(self) -> str:
        return self.__chatroomnr

    @chatroomnr.setter
    def chatroomnr(self, chatroomnr: str):
        self.__chatroomnr = chatroomnr

    @property
    def lobj_User(self):
        return self.__lobj_User

    @lobj_User.setter
    def lobj_User(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lobj_User__lobj_User", None)
        self.__lobj_User = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lobj_AccessControl121"):
                opp_val = getattr(old_value, "lobj_AccessControl121", None)
                if opp_val == self:
                    setattr(old_value, "lobj_AccessControl121", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lobj_AccessControl121"):
                opp_val = getattr(value, "lobj_AccessControl121", None)
                setattr(value, "lobj_AccessControl121", self)

    @property
    def lobj_User127(self):
        return self.__lobj_User127

    @lobj_User127.setter
    def lobj_User127(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lobj_User__lobj_User127", None)
        self.__lobj_User127 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lobj_AccessControl126"):
                opp_val = getattr(old_value, "lobj_AccessControl126", None)
                if opp_val == self:
                    setattr(old_value, "lobj_AccessControl126", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lobj_AccessControl126"):
                opp_val = getattr(value, "lobj_AccessControl126", None)
                setattr(value, "lobj_AccessControl126", self)

    @property
    def lobj_User124(self):
        return self.__lobj_User124

    @lobj_User124.setter
    def lobj_User124(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lobj_User__lobj_User124", None)
        self.__lobj_User124 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lobj_AccessControl123"):
                opp_val = getattr(old_value, "lobj_AccessControl123", None)
                if opp_val == self:
                    setattr(old_value, "lobj_AccessControl123", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lobj_AccessControl123"):
                opp_val = getattr(value, "lobj_AccessControl123", None)
                setattr(value, "lobj_AccessControl123", self)

    @property
    def lobj_User180(self):
        return self.__lobj_User180

    @lobj_User180.setter
    def lobj_User180(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lobj_User__lobj_User180", None)
        self.__lobj_User180 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lobj_Userauthorization179"):
                opp_val = getattr(old_value, "lobj_Userauthorization179", None)
                if opp_val == self:
                    setattr(old_value, "lobj_Userauthorization179", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lobj_Userauthorization179"):
                opp_val = getattr(value, "lobj_Userauthorization179", None)
                setattr(value, "lobj_Userauthorization179", self)

    @property
    def lobj_User217(self):
        return self.__lobj_User217

    @lobj_User217.setter
    def lobj_User217(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lobj_User__lobj_User217", None)
        self.__lobj_User217 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "lobj_AuthorizationTypes218"):
                    opp_val = getattr(item, "lobj_AuthorizationTypes218", None)
                    
                    if opp_val == self:
                        setattr(item, "lobj_AuthorizationTypes218", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "lobj_AuthorizationTypes218"):
                    opp_val = getattr(item, "lobj_AuthorizationTypes218", None)
                    
                    setattr(item, "lobj_AuthorizationTypes218", self)
                    

    @property
    def lobj_User155(self):
        return self.__lobj_User155

    @lobj_User155.setter
    def lobj_User155(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lobj_User__lobj_User155", None)
        self.__lobj_User155 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lobj_CourseMeta154"):
                opp_val = getattr(old_value, "lobj_CourseMeta154", None)
                if opp_val == self:
                    setattr(old_value, "lobj_CourseMeta154", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lobj_CourseMeta154"):
                opp_val = getattr(value, "lobj_CourseMeta154", None)
                setattr(value, "lobj_CourseMeta154", self)

class lobj_ResrcFiletype:

    def __init__(self, filetypeExtension: str, filetypeDesc: str, image: bool, applet: bool, filetypeImageSmall: str, filetypeImageBif: str, id: str, lobj_ResrcFiletype: "lobj_ResrcFile" = None, lobj_ResrcFiletype119: "lobj_BlockAudiofile" = None):
        self.filetypeExtension = filetypeExtension
        self.filetypeDesc = filetypeDesc
        self.image = image
        self.applet = applet
        self.filetypeImageSmall = filetypeImageSmall
        self.filetypeImageBif = filetypeImageBif
        self.id = id
        self.lobj_ResrcFiletype = lobj_ResrcFiletype
        self.lobj_ResrcFiletype119 = lobj_ResrcFiletype119
        
    @property
    def filetypeDesc(self) -> str:
        return self.__filetypeDesc

    @filetypeDesc.setter
    def filetypeDesc(self, filetypeDesc: str):
        self.__filetypeDesc = filetypeDesc

    @property
    def filetypeImageBif(self) -> str:
        return self.__filetypeImageBif

    @filetypeImageBif.setter
    def filetypeImageBif(self, filetypeImageBif: str):
        self.__filetypeImageBif = filetypeImageBif

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def applet(self) -> bool:
        return self.__applet

    @applet.setter
    def applet(self, applet: bool):
        self.__applet = applet

    @property
    def filetypeExtension(self) -> str:
        return self.__filetypeExtension

    @filetypeExtension.setter
    def filetypeExtension(self, filetypeExtension: str):
        self.__filetypeExtension = filetypeExtension

    @property
    def filetypeImageSmall(self) -> str:
        return self.__filetypeImageSmall

    @filetypeImageSmall.setter
    def filetypeImageSmall(self, filetypeImageSmall: str):
        self.__filetypeImageSmall = filetypeImageSmall

    @property
    def image(self) -> bool:
        return self.__image

    @image.setter
    def image(self, image: bool):
        self.__image = image

    @property
    def lobj_ResrcFiletype119(self):
        return self.__lobj_ResrcFiletype119

    @lobj_ResrcFiletype119.setter
    def lobj_ResrcFiletype119(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lobj_ResrcFiletype__lobj_ResrcFiletype119", None)
        self.__lobj_ResrcFiletype119 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lobj_BlockAudiofile118"):
                opp_val = getattr(old_value, "lobj_BlockAudiofile118", None)
                if opp_val == self:
                    setattr(old_value, "lobj_BlockAudiofile118", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lobj_BlockAudiofile118"):
                opp_val = getattr(value, "lobj_BlockAudiofile118", None)
                setattr(value, "lobj_BlockAudiofile118", self)

    @property
    def lobj_ResrcFiletype(self):
        return self.__lobj_ResrcFiletype

    @lobj_ResrcFiletype.setter
    def lobj_ResrcFiletype(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lobj_ResrcFiletype__lobj_ResrcFiletype", None)
        self.__lobj_ResrcFiletype = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lobj_ResrcFile110"):
                opp_val = getattr(old_value, "lobj_ResrcFile110", None)
                if opp_val == self:
                    setattr(old_value, "lobj_ResrcFile110", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lobj_ResrcFile110"):
                opp_val = getattr(value, "lobj_ResrcFile110", None)
                setattr(value, "lobj_ResrcFile110", self)

class Node:

    pass
class lobj_LuNode(Node):

    pass
class lobj_ThemeNode(Node):

    pass
class lobj_SimpleDidacMeta:

    def __init__(self, id: str, title: str, description: str, keywords: str, lobj_SimpleDidacMeta: "lobj_Theme" = None, lobj_SimpleDidacMeta143: "lobj_BlockMeta" = None, lobj_SimpleDidacMeta160: "lobj_Language" = None):
        self.id = id
        self.title = title
        self.description = description
        self.keywords = keywords
        self.lobj_SimpleDidacMeta = lobj_SimpleDidacMeta
        self.lobj_SimpleDidacMeta143 = lobj_SimpleDidacMeta143
        self.lobj_SimpleDidacMeta160 = lobj_SimpleDidacMeta160
        
    @property
    def keywords(self) -> str:
        return self.__keywords

    @keywords.setter
    def keywords(self, keywords: str):
        self.__keywords = keywords

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def lobj_SimpleDidacMeta(self):
        return self.__lobj_SimpleDidacMeta

    @lobj_SimpleDidacMeta.setter
    def lobj_SimpleDidacMeta(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lobj_SimpleDidacMeta__lobj_SimpleDidacMeta", None)
        self.__lobj_SimpleDidacMeta = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lobj_Theme"):
                opp_val = getattr(old_value, "lobj_Theme", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lobj_Theme"):
                opp_val = getattr(value, "lobj_Theme", None)
                if opp_val is None:
                    setattr(value, "lobj_Theme", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def lobj_SimpleDidacMeta143(self):
        return self.__lobj_SimpleDidacMeta143

    @lobj_SimpleDidacMeta143.setter
    def lobj_SimpleDidacMeta143(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lobj_SimpleDidacMeta__lobj_SimpleDidacMeta143", None)
        self.__lobj_SimpleDidacMeta143 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lobj_BlockMeta142"):
                opp_val = getattr(old_value, "lobj_BlockMeta142", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lobj_BlockMeta142"):
                opp_val = getattr(value, "lobj_BlockMeta142", None)
                if opp_val is None:
                    setattr(value, "lobj_BlockMeta142", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def lobj_SimpleDidacMeta160(self):
        return self.__lobj_SimpleDidacMeta160

    @lobj_SimpleDidacMeta160.setter
    def lobj_SimpleDidacMeta160(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lobj_SimpleDidacMeta__lobj_SimpleDidacMeta160", None)
        self.__lobj_SimpleDidacMeta160 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lobj_Language161"):
                opp_val = getattr(old_value, "lobj_Language161", None)
                if opp_val == self:
                    setattr(old_value, "lobj_Language161", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lobj_Language161"):
                opp_val = getattr(value, "lobj_Language161", None)
                setattr(value, "lobj_Language161", self)

class lobj_Node(ABC):

    def __init__(self, visible: bool, id: str, lobj_Node: "lobj_Module" = None, lobj_Node103: "lobj_ThemeNode" = None):
        self.visible = visible
        self.id = id
        self.lobj_Node = lobj_Node
        self.lobj_Node103 = lobj_Node103
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def visible(self) -> bool:
        return self.__visible

    @visible.setter
    def visible(self, visible: bool):
        self.__visible = visible

    @property
    def lobj_Node(self):
        return self.__lobj_Node

    @lobj_Node.setter
    def lobj_Node(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lobj_Node__lobj_Node", None)
        self.__lobj_Node = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lobj_Module70"):
                opp_val = getattr(old_value, "lobj_Module70", None)
                if opp_val == self:
                    setattr(old_value, "lobj_Module70", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lobj_Module70"):
                opp_val = getattr(value, "lobj_Module70", None)
                setattr(value, "lobj_Module70", self)

    @property
    def lobj_Node103(self):
        return self.__lobj_Node103

    @lobj_Node103.setter
    def lobj_Node103(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lobj_Node__lobj_Node103", None)
        self.__lobj_Node103 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lobj_ThemeNode102"):
                opp_val = getattr(old_value, "lobj_ThemeNode102", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lobj_ThemeNode102"):
                opp_val = getattr(value, "lobj_ThemeNode102", None)
                if opp_val is None:
                    setattr(value, "lobj_ThemeNode102", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class lobj_Item:

    def __init__(self, luRef: str, id: str, lobj_Item: set["lobj_CorrBlock"] = None, lobj_Item42: "lobj_Item" = None, lobj_Item40: set["lobj_Item"] = None, lobj_Item52: "lobj_LearningUnit" = None):
        self.luRef = luRef
        self.id = id
        self.lobj_Item = lobj_Item if lobj_Item is not None else set()
        self.lobj_Item42 = lobj_Item42
        self.lobj_Item40 = lobj_Item40 if lobj_Item40 is not None else set()
        self.lobj_Item52 = lobj_Item52
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def luRef(self) -> str:
        return self.__luRef

    @luRef.setter
    def luRef(self, luRef: str):
        self.__luRef = luRef

    @property
    def lobj_Item42(self):
        return self.__lobj_Item42

    @lobj_Item42.setter
    def lobj_Item42(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lobj_Item__lobj_Item42", None)
        self.__lobj_Item42 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lobj_Item40"):
                opp_val = getattr(old_value, "lobj_Item40", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lobj_Item40"):
                opp_val = getattr(value, "lobj_Item40", None)
                if opp_val is None:
                    setattr(value, "lobj_Item40", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def lobj_Item52(self):
        return self.__lobj_Item52

    @lobj_Item52.setter
    def lobj_Item52(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lobj_Item__lobj_Item52", None)
        self.__lobj_Item52 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lobj_LearningUnit51"):
                opp_val = getattr(old_value, "lobj_LearningUnit51", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lobj_LearningUnit51"):
                opp_val = getattr(value, "lobj_LearningUnit51", None)
                if opp_val is None:
                    setattr(value, "lobj_LearningUnit51", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def lobj_Item40(self):
        return self.__lobj_Item40

    @lobj_Item40.setter
    def lobj_Item40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lobj_Item__lobj_Item40", None)
        self.__lobj_Item40 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "lobj_Item42"):
                    opp_val = getattr(item, "lobj_Item42", None)
                    
                    if opp_val == self:
                        setattr(item, "lobj_Item42", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "lobj_Item42"):
                    opp_val = getattr(item, "lobj_Item42", None)
                    
                    setattr(item, "lobj_Item42", self)
                    

    @property
    def lobj_Item(self):
        return self.__lobj_Item

    @lobj_Item.setter
    def lobj_Item(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lobj_Item__lobj_Item", None)
        self.__lobj_Item = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "lobj_CorrBlock39"):
                    opp_val = getattr(item, "lobj_CorrBlock39", None)
                    
                    if opp_val == self:
                        setattr(item, "lobj_CorrBlock39", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "lobj_CorrBlock39"):
                    opp_val = getattr(item, "lobj_CorrBlock39", None)
                    
                    setattr(item, "lobj_CorrBlock39", self)
                    

class lobj_Coursetype:

    def __init__(self, id: str, title: str, description: str, lobj_Coursetype: "lobj_Course" = None, lobj_Coursetype194: "lobj_Language" = None):
        self.id = id
        self.title = title
        self.description = description
        self.lobj_Coursetype = lobj_Coursetype
        self.lobj_Coursetype194 = lobj_Coursetype194
        
    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def lobj_Coursetype(self):
        return self.__lobj_Coursetype

    @lobj_Coursetype.setter
    def lobj_Coursetype(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lobj_Coursetype__lobj_Coursetype", None)
        self.__lobj_Coursetype = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lobj_Course35"):
                opp_val = getattr(old_value, "lobj_Course35", None)
                if opp_val == self:
                    setattr(old_value, "lobj_Course35", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lobj_Course35"):
                opp_val = getattr(value, "lobj_Course35", None)
                setattr(value, "lobj_Course35", self)

    @property
    def lobj_Coursetype194(self):
        return self.__lobj_Coursetype194

    @lobj_Coursetype194.setter
    def lobj_Coursetype194(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lobj_Coursetype__lobj_Coursetype194", None)
        self.__lobj_Coursetype194 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lobj_Language195"):
                opp_val = getattr(old_value, "lobj_Language195", None)
                if opp_val == self:
                    setattr(old_value, "lobj_Language195", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lobj_Language195"):
                opp_val = getattr(value, "lobj_Language195", None)
                setattr(value, "lobj_Language195", self)

class lobj_PresentationBlock:

    def __init__(self, id: str, lod: int, rendering: str, lobj_PresentationBlock: "lobj_CorrBlock" = None, lobj_PresentationBlock97: "lobj_Block" = None):
        self.id = id
        self.lod = lod
        self.rendering = rendering
        self.lobj_PresentationBlock = lobj_PresentationBlock
        self.lobj_PresentationBlock97 = lobj_PresentationBlock97
        
    @property
    def rendering(self) -> str:
        return self.__rendering

    @rendering.setter
    def rendering(self, rendering: str):
        self.__rendering = rendering

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def lod(self) -> int:
        return self.__lod

    @lod.setter
    def lod(self, lod: int):
        self.__lod = lod

    @property
    def lobj_PresentationBlock97(self):
        return self.__lobj_PresentationBlock97

    @lobj_PresentationBlock97.setter
    def lobj_PresentationBlock97(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lobj_PresentationBlock__lobj_PresentationBlock97", None)
        self.__lobj_PresentationBlock97 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lobj_Block98"):
                opp_val = getattr(old_value, "lobj_Block98", None)
                if opp_val == self:
                    setattr(old_value, "lobj_Block98", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lobj_Block98"):
                opp_val = getattr(value, "lobj_Block98", None)
                setattr(value, "lobj_Block98", self)

    @property
    def lobj_PresentationBlock(self):
        return self.__lobj_PresentationBlock

    @lobj_PresentationBlock.setter
    def lobj_PresentationBlock(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lobj_PresentationBlock__lobj_PresentationBlock", None)
        self.__lobj_PresentationBlock = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lobj_CorrBlock"):
                opp_val = getattr(old_value, "lobj_CorrBlock", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lobj_CorrBlock"):
                opp_val = getattr(value, "lobj_CorrBlock", None)
                if opp_val is None:
                    setattr(value, "lobj_CorrBlock", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class lobj_CorrBlock:

    def __init__(self, id: str, lobj_CorrBlock: set["lobj_PresentationBlock"] = None, lobj_CorrBlock27: set["lobj_TitleMeta"] = None, lobj_CorrBlock39: "lobj_Item" = None):
        self.id = id
        self.lobj_CorrBlock = lobj_CorrBlock if lobj_CorrBlock is not None else set()
        self.lobj_CorrBlock27 = lobj_CorrBlock27 if lobj_CorrBlock27 is not None else set()
        self.lobj_CorrBlock39 = lobj_CorrBlock39
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def lobj_CorrBlock(self):
        return self.__lobj_CorrBlock

    @lobj_CorrBlock.setter
    def lobj_CorrBlock(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lobj_CorrBlock__lobj_CorrBlock", None)
        self.__lobj_CorrBlock = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "lobj_PresentationBlock"):
                    opp_val = getattr(item, "lobj_PresentationBlock", None)
                    
                    if opp_val == self:
                        setattr(item, "lobj_PresentationBlock", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "lobj_PresentationBlock"):
                    opp_val = getattr(item, "lobj_PresentationBlock", None)
                    
                    setattr(item, "lobj_PresentationBlock", self)
                    

    @property
    def lobj_CorrBlock39(self):
        return self.__lobj_CorrBlock39

    @lobj_CorrBlock39.setter
    def lobj_CorrBlock39(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lobj_CorrBlock__lobj_CorrBlock39", None)
        self.__lobj_CorrBlock39 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lobj_Item"):
                opp_val = getattr(old_value, "lobj_Item", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lobj_Item"):
                opp_val = getattr(value, "lobj_Item", None)
                if opp_val is None:
                    setattr(value, "lobj_Item", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def lobj_CorrBlock27(self):
        return self.__lobj_CorrBlock27

    @lobj_CorrBlock27.setter
    def lobj_CorrBlock27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lobj_CorrBlock__lobj_CorrBlock27", None)
        self.__lobj_CorrBlock27 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "lobj_TitleMeta28"):
                    opp_val = getattr(item, "lobj_TitleMeta28", None)
                    
                    if opp_val == self:
                        setattr(item, "lobj_TitleMeta28", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "lobj_TitleMeta28"):
                    opp_val = getattr(item, "lobj_TitleMeta28", None)
                    
                    setattr(item, "lobj_TitleMeta28", self)
                    

class lobj_TitleMeta:

    def __init__(self, title: str, id: str, lobj_TitleMeta: "lobj_Category" = None, lobj_TitleMeta28: "lobj_CorrBlock" = None, lobj_TitleMeta149: "lobj_Language" = None):
        self.title = title
        self.id = id
        self.lobj_TitleMeta = lobj_TitleMeta
        self.lobj_TitleMeta28 = lobj_TitleMeta28
        self.lobj_TitleMeta149 = lobj_TitleMeta149
        
    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def lobj_TitleMeta149(self):
        return self.__lobj_TitleMeta149

    @lobj_TitleMeta149.setter
    def lobj_TitleMeta149(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lobj_TitleMeta__lobj_TitleMeta149", None)
        self.__lobj_TitleMeta149 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lobj_Language150"):
                opp_val = getattr(old_value, "lobj_Language150", None)
                if opp_val == self:
                    setattr(old_value, "lobj_Language150", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lobj_Language150"):
                opp_val = getattr(value, "lobj_Language150", None)
                setattr(value, "lobj_Language150", self)

    @property
    def lobj_TitleMeta(self):
        return self.__lobj_TitleMeta

    @lobj_TitleMeta.setter
    def lobj_TitleMeta(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lobj_TitleMeta__lobj_TitleMeta", None)
        self.__lobj_TitleMeta = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lobj_Category"):
                opp_val = getattr(old_value, "lobj_Category", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lobj_Category"):
                opp_val = getattr(value, "lobj_Category", None)
                if opp_val is None:
                    setattr(value, "lobj_Category", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def lobj_TitleMeta28(self):
        return self.__lobj_TitleMeta28

    @lobj_TitleMeta28.setter
    def lobj_TitleMeta28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lobj_TitleMeta__lobj_TitleMeta28", None)
        self.__lobj_TitleMeta28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lobj_CorrBlock27"):
                opp_val = getattr(old_value, "lobj_CorrBlock27", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lobj_CorrBlock27"):
                opp_val = getattr(value, "lobj_CorrBlock27", None)
                if opp_val is None:
                    setattr(value, "lobj_CorrBlock27", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class AbstractContent:

    pass
class lobj_Source:

    def __init__(self, title: str, subtitle: str, publishedIn: str, publishedBy: str, publishDate: str, pp: str, id: str, lobj_Source: "lobj_AbstractContent" = None, lobj_Source113: "lobj_ResrcFile" = None, lobj_Source214: "lobj_Author" = None):
        self.title = title
        self.subtitle = subtitle
        self.publishedIn = publishedIn
        self.publishedBy = publishedBy
        self.publishDate = publishDate
        self.pp = pp
        self.id = id
        self.lobj_Source = lobj_Source
        self.lobj_Source113 = lobj_Source113
        self.lobj_Source214 = lobj_Source214
        
    @property
    def publishedBy(self) -> str:
        return self.__publishedBy

    @publishedBy.setter
    def publishedBy(self, publishedBy: str):
        self.__publishedBy = publishedBy

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def publishedIn(self) -> str:
        return self.__publishedIn

    @publishedIn.setter
    def publishedIn(self, publishedIn: str):
        self.__publishedIn = publishedIn

    @property
    def publishDate(self) -> str:
        return self.__publishDate

    @publishDate.setter
    def publishDate(self, publishDate: str):
        self.__publishDate = publishDate

    @property
    def pp(self) -> str:
        return self.__pp

    @pp.setter
    def pp(self, pp: str):
        self.__pp = pp

    @property
    def subtitle(self) -> str:
        return self.__subtitle

    @subtitle.setter
    def subtitle(self, subtitle: str):
        self.__subtitle = subtitle

    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def lobj_Source(self):
        return self.__lobj_Source

    @lobj_Source.setter
    def lobj_Source(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lobj_Source__lobj_Source", None)
        self.__lobj_Source = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lobj_AbstractContent8"):
                opp_val = getattr(old_value, "lobj_AbstractContent8", None)
                if opp_val == self:
                    setattr(old_value, "lobj_AbstractContent8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lobj_AbstractContent8"):
                opp_val = getattr(value, "lobj_AbstractContent8", None)
                setattr(value, "lobj_AbstractContent8", self)

    @property
    def lobj_Source113(self):
        return self.__lobj_Source113

    @lobj_Source113.setter
    def lobj_Source113(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lobj_Source__lobj_Source113", None)
        self.__lobj_Source113 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lobj_ResrcFile112"):
                opp_val = getattr(old_value, "lobj_ResrcFile112", None)
                if opp_val == self:
                    setattr(old_value, "lobj_ResrcFile112", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lobj_ResrcFile112"):
                opp_val = getattr(value, "lobj_ResrcFile112", None)
                setattr(value, "lobj_ResrcFile112", self)

    @property
    def lobj_Source214(self):
        return self.__lobj_Source214

    @lobj_Source214.setter
    def lobj_Source214(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lobj_Source__lobj_Source214", None)
        self.__lobj_Source214 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lobj_Author215"):
                opp_val = getattr(old_value, "lobj_Author215", None)
                if opp_val == self:
                    setattr(old_value, "lobj_Author215", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lobj_Author215"):
                opp_val = getattr(value, "lobj_Author215", None)
                setattr(value, "lobj_Author215", self)

class lobj_Language:

    def __init__(self, language: str, code: str, lobj_Language: "lobj_AbstractContent" = None, lobj_Language146: "lobj_BlockMeta" = None, lobj_Language150: "lobj_TitleMeta" = None, lobj_Language158: "lobj_CourseMeta" = None, lobj_Language161: "lobj_SimpleDidacMeta" = None, lobj_Language177: "lobj_LuMeta" = None, lobj_Language195: "lobj_Coursetype" = None, lobj_Language200: "lobj_InternalRef" = None, lobj_Language212: "lobj_ModuleMeta" = None):
        self.language = language
        self.code = code
        self.lobj_Language = lobj_Language
        self.lobj_Language146 = lobj_Language146
        self.lobj_Language150 = lobj_Language150
        self.lobj_Language158 = lobj_Language158
        self.lobj_Language161 = lobj_Language161
        self.lobj_Language177 = lobj_Language177
        self.lobj_Language195 = lobj_Language195
        self.lobj_Language200 = lobj_Language200
        self.lobj_Language212 = lobj_Language212
        
    @property
    def language(self) -> str:
        return self.__language

    @language.setter
    def language(self, language: str):
        self.__language = language

    @property
    def code(self) -> str:
        return self.__code

    @code.setter
    def code(self, code: str):
        self.__code = code

    @property
    def lobj_Language161(self):
        return self.__lobj_Language161

    @lobj_Language161.setter
    def lobj_Language161(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lobj_Language__lobj_Language161", None)
        self.__lobj_Language161 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lobj_SimpleDidacMeta160"):
                opp_val = getattr(old_value, "lobj_SimpleDidacMeta160", None)
                if opp_val == self:
                    setattr(old_value, "lobj_SimpleDidacMeta160", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lobj_SimpleDidacMeta160"):
                opp_val = getattr(value, "lobj_SimpleDidacMeta160", None)
                setattr(value, "lobj_SimpleDidacMeta160", self)

    @property
    def lobj_Language150(self):
        return self.__lobj_Language150

    @lobj_Language150.setter
    def lobj_Language150(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lobj_Language__lobj_Language150", None)
        self.__lobj_Language150 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lobj_TitleMeta149"):
                opp_val = getattr(old_value, "lobj_TitleMeta149", None)
                if opp_val == self:
                    setattr(old_value, "lobj_TitleMeta149", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lobj_TitleMeta149"):
                opp_val = getattr(value, "lobj_TitleMeta149", None)
                setattr(value, "lobj_TitleMeta149", self)

    @property
    def lobj_Language177(self):
        return self.__lobj_Language177

    @lobj_Language177.setter
    def lobj_Language177(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lobj_Language__lobj_Language177", None)
        self.__lobj_Language177 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lobj_LuMeta176"):
                opp_val = getattr(old_value, "lobj_LuMeta176", None)
                if opp_val == self:
                    setattr(old_value, "lobj_LuMeta176", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lobj_LuMeta176"):
                opp_val = getattr(value, "lobj_LuMeta176", None)
                setattr(value, "lobj_LuMeta176", self)

    @property
    def lobj_Language158(self):
        return self.__lobj_Language158

    @lobj_Language158.setter
    def lobj_Language158(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lobj_Language__lobj_Language158", None)
        self.__lobj_Language158 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lobj_CourseMeta157"):
                opp_val = getattr(old_value, "lobj_CourseMeta157", None)
                if opp_val == self:
                    setattr(old_value, "lobj_CourseMeta157", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lobj_CourseMeta157"):
                opp_val = getattr(value, "lobj_CourseMeta157", None)
                setattr(value, "lobj_CourseMeta157", self)

    @property
    def lobj_Language200(self):
        return self.__lobj_Language200

    @lobj_Language200.setter
    def lobj_Language200(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lobj_Language__lobj_Language200", None)
        self.__lobj_Language200 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lobj_InternalRef199"):
                opp_val = getattr(old_value, "lobj_InternalRef199", None)
                if opp_val == self:
                    setattr(old_value, "lobj_InternalRef199", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lobj_InternalRef199"):
                opp_val = getattr(value, "lobj_InternalRef199", None)
                setattr(value, "lobj_InternalRef199", self)

    @property
    def lobj_Language146(self):
        return self.__lobj_Language146

    @lobj_Language146.setter
    def lobj_Language146(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lobj_Language__lobj_Language146", None)
        self.__lobj_Language146 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lobj_BlockMeta145"):
                opp_val = getattr(old_value, "lobj_BlockMeta145", None)
                if opp_val == self:
                    setattr(old_value, "lobj_BlockMeta145", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lobj_BlockMeta145"):
                opp_val = getattr(value, "lobj_BlockMeta145", None)
                setattr(value, "lobj_BlockMeta145", self)

    @property
    def lobj_Language212(self):
        return self.__lobj_Language212

    @lobj_Language212.setter
    def lobj_Language212(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lobj_Language__lobj_Language212", None)
        self.__lobj_Language212 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lobj_ModuleMeta211"):
                opp_val = getattr(old_value, "lobj_ModuleMeta211", None)
                if opp_val == self:
                    setattr(old_value, "lobj_ModuleMeta211", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lobj_ModuleMeta211"):
                opp_val = getattr(value, "lobj_ModuleMeta211", None)
                setattr(value, "lobj_ModuleMeta211", self)

    @property
    def lobj_Language(self):
        return self.__lobj_Language

    @lobj_Language.setter
    def lobj_Language(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lobj_Language__lobj_Language", None)
        self.__lobj_Language = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lobj_AbstractContent"):
                opp_val = getattr(old_value, "lobj_AbstractContent", None)
                if opp_val == self:
                    setattr(old_value, "lobj_AbstractContent", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lobj_AbstractContent"):
                opp_val = getattr(value, "lobj_AbstractContent", None)
                setattr(value, "lobj_AbstractContent", self)

    @property
    def lobj_Language195(self):
        return self.__lobj_Language195

    @lobj_Language195.setter
    def lobj_Language195(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lobj_Language__lobj_Language195", None)
        self.__lobj_Language195 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lobj_Coursetype194"):
                opp_val = getattr(old_value, "lobj_Coursetype194", None)
                if opp_val == self:
                    setattr(old_value, "lobj_Coursetype194", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lobj_Coursetype194"):
                opp_val = getattr(value, "lobj_Coursetype194", None)
                setattr(value, "lobj_Coursetype194", self)

class Block:

    pass
class lobj_HypertextBlock(Block):

    pass
class lobj_AccessControl:

    def __init__(self, lastStatusChange: date, lastModified: date, status: str, globalAccess: bool, id: str, lobj_AccessControl: "lobj_Block" = None, lobj_AccessControl21: "lobj_BlockFolder" = None, lobj_AccessControl49: "lobj_LearningUnit" = None, lobj_AccessControl63: "lobj_LuFolder" = None, lobj_AccessControl73: "lobj_Module" = None, lobj_AccessControl84: "lobj_ModuleFolder" = None, lobj_AccessControl92: "lobj_ResrcFolder" = None, lobj_AccessControl108: "lobj_ResrcFile" = None, lobj_AccessControl126: "lobj_User" = None, lobj_AccessControl121: "lobj_User" = None, lobj_AccessControl123: "lobj_User" = None, lobj_AccessControl129: "lobj_Sharednotes" = None, lobj_AccessControl131: set["lobj_Userauthorization"] = None, lobj_AccessControl133: set["lobj_Edition"] = None):
        self.lastStatusChange = lastStatusChange
        self.lastModified = lastModified
        self.status = status
        self.globalAccess = globalAccess
        self.id = id
        self.lobj_AccessControl = lobj_AccessControl
        self.lobj_AccessControl21 = lobj_AccessControl21
        self.lobj_AccessControl49 = lobj_AccessControl49
        self.lobj_AccessControl63 = lobj_AccessControl63
        self.lobj_AccessControl73 = lobj_AccessControl73
        self.lobj_AccessControl84 = lobj_AccessControl84
        self.lobj_AccessControl92 = lobj_AccessControl92
        self.lobj_AccessControl108 = lobj_AccessControl108
        self.lobj_AccessControl126 = lobj_AccessControl126
        self.lobj_AccessControl121 = lobj_AccessControl121
        self.lobj_AccessControl123 = lobj_AccessControl123
        self.lobj_AccessControl129 = lobj_AccessControl129
        self.lobj_AccessControl131 = lobj_AccessControl131 if lobj_AccessControl131 is not None else set()
        self.lobj_AccessControl133 = lobj_AccessControl133 if lobj_AccessControl133 is not None else set()
        
    @property
    def status(self) -> str:
        return self.__status

    @status.setter
    def status(self, status: str):
        self.__status = status

    @property
    def lastModified(self) -> date:
        return self.__lastModified

    @lastModified.setter
    def lastModified(self, lastModified: date):
        self.__lastModified = lastModified

    @property
    def globalAccess(self) -> bool:
        return self.__globalAccess

    @globalAccess.setter
    def globalAccess(self, globalAccess: bool):
        self.__globalAccess = globalAccess

    @property
    def lastStatusChange(self) -> date:
        return self.__lastStatusChange

    @lastStatusChange.setter
    def lastStatusChange(self, lastStatusChange: date):
        self.__lastStatusChange = lastStatusChange

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def lobj_AccessControl(self):
        return self.__lobj_AccessControl

    @lobj_AccessControl.setter
    def lobj_AccessControl(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lobj_AccessControl__lobj_AccessControl", None)
        self.__lobj_AccessControl = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lobj_Block4"):
                opp_val = getattr(old_value, "lobj_Block4", None)
                if opp_val == self:
                    setattr(old_value, "lobj_Block4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lobj_Block4"):
                opp_val = getattr(value, "lobj_Block4", None)
                setattr(value, "lobj_Block4", self)

    @property
    def lobj_AccessControl92(self):
        return self.__lobj_AccessControl92

    @lobj_AccessControl92.setter
    def lobj_AccessControl92(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lobj_AccessControl__lobj_AccessControl92", None)
        self.__lobj_AccessControl92 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lobj_ResrcFolder91"):
                opp_val = getattr(old_value, "lobj_ResrcFolder91", None)
                if opp_val == self:
                    setattr(old_value, "lobj_ResrcFolder91", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lobj_ResrcFolder91"):
                opp_val = getattr(value, "lobj_ResrcFolder91", None)
                setattr(value, "lobj_ResrcFolder91", self)

    @property
    def lobj_AccessControl121(self):
        return self.__lobj_AccessControl121

    @lobj_AccessControl121.setter
    def lobj_AccessControl121(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lobj_AccessControl__lobj_AccessControl121", None)
        self.__lobj_AccessControl121 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lobj_User"):
                opp_val = getattr(old_value, "lobj_User", None)
                if opp_val == self:
                    setattr(old_value, "lobj_User", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lobj_User"):
                opp_val = getattr(value, "lobj_User", None)
                setattr(value, "lobj_User", self)

    @property
    def lobj_AccessControl49(self):
        return self.__lobj_AccessControl49

    @lobj_AccessControl49.setter
    def lobj_AccessControl49(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lobj_AccessControl__lobj_AccessControl49", None)
        self.__lobj_AccessControl49 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lobj_LearningUnit48"):
                opp_val = getattr(old_value, "lobj_LearningUnit48", None)
                if opp_val == self:
                    setattr(old_value, "lobj_LearningUnit48", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lobj_LearningUnit48"):
                opp_val = getattr(value, "lobj_LearningUnit48", None)
                setattr(value, "lobj_LearningUnit48", self)

    @property
    def lobj_AccessControl133(self):
        return self.__lobj_AccessControl133

    @lobj_AccessControl133.setter
    def lobj_AccessControl133(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lobj_AccessControl__lobj_AccessControl133", None)
        self.__lobj_AccessControl133 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "lobj_Edition"):
                    opp_val = getattr(item, "lobj_Edition", None)
                    
                    if opp_val == self:
                        setattr(item, "lobj_Edition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "lobj_Edition"):
                    opp_val = getattr(item, "lobj_Edition", None)
                    
                    setattr(item, "lobj_Edition", self)
                    

    @property
    def lobj_AccessControl84(self):
        return self.__lobj_AccessControl84

    @lobj_AccessControl84.setter
    def lobj_AccessControl84(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lobj_AccessControl__lobj_AccessControl84", None)
        self.__lobj_AccessControl84 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lobj_ModuleFolder83"):
                opp_val = getattr(old_value, "lobj_ModuleFolder83", None)
                if opp_val == self:
                    setattr(old_value, "lobj_ModuleFolder83", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lobj_ModuleFolder83"):
                opp_val = getattr(value, "lobj_ModuleFolder83", None)
                setattr(value, "lobj_ModuleFolder83", self)

    @property
    def lobj_AccessControl126(self):
        return self.__lobj_AccessControl126

    @lobj_AccessControl126.setter
    def lobj_AccessControl126(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lobj_AccessControl__lobj_AccessControl126", None)
        self.__lobj_AccessControl126 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lobj_User127"):
                opp_val = getattr(old_value, "lobj_User127", None)
                if opp_val == self:
                    setattr(old_value, "lobj_User127", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lobj_User127"):
                opp_val = getattr(value, "lobj_User127", None)
                setattr(value, "lobj_User127", self)

    @property
    def lobj_AccessControl123(self):
        return self.__lobj_AccessControl123

    @lobj_AccessControl123.setter
    def lobj_AccessControl123(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lobj_AccessControl__lobj_AccessControl123", None)
        self.__lobj_AccessControl123 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lobj_User124"):
                opp_val = getattr(old_value, "lobj_User124", None)
                if opp_val == self:
                    setattr(old_value, "lobj_User124", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lobj_User124"):
                opp_val = getattr(value, "lobj_User124", None)
                setattr(value, "lobj_User124", self)

    @property
    def lobj_AccessControl131(self):
        return self.__lobj_AccessControl131

    @lobj_AccessControl131.setter
    def lobj_AccessControl131(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lobj_AccessControl__lobj_AccessControl131", None)
        self.__lobj_AccessControl131 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "lobj_Userauthorization"):
                    opp_val = getattr(item, "lobj_Userauthorization", None)
                    
                    if opp_val == self:
                        setattr(item, "lobj_Userauthorization", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "lobj_Userauthorization"):
                    opp_val = getattr(item, "lobj_Userauthorization", None)
                    
                    setattr(item, "lobj_Userauthorization", self)
                    

    @property
    def lobj_AccessControl63(self):
        return self.__lobj_AccessControl63

    @lobj_AccessControl63.setter
    def lobj_AccessControl63(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lobj_AccessControl__lobj_AccessControl63", None)
        self.__lobj_AccessControl63 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lobj_LuFolder62"):
                opp_val = getattr(old_value, "lobj_LuFolder62", None)
                if opp_val == self:
                    setattr(old_value, "lobj_LuFolder62", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lobj_LuFolder62"):
                opp_val = getattr(value, "lobj_LuFolder62", None)
                setattr(value, "lobj_LuFolder62", self)

    @property
    def lobj_AccessControl108(self):
        return self.__lobj_AccessControl108

    @lobj_AccessControl108.setter
    def lobj_AccessControl108(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lobj_AccessControl__lobj_AccessControl108", None)
        self.__lobj_AccessControl108 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lobj_ResrcFile107"):
                opp_val = getattr(old_value, "lobj_ResrcFile107", None)
                if opp_val == self:
                    setattr(old_value, "lobj_ResrcFile107", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lobj_ResrcFile107"):
                opp_val = getattr(value, "lobj_ResrcFile107", None)
                setattr(value, "lobj_ResrcFile107", self)

    @property
    def lobj_AccessControl73(self):
        return self.__lobj_AccessControl73

    @lobj_AccessControl73.setter
    def lobj_AccessControl73(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lobj_AccessControl__lobj_AccessControl73", None)
        self.__lobj_AccessControl73 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lobj_Module72"):
                opp_val = getattr(old_value, "lobj_Module72", None)
                if opp_val == self:
                    setattr(old_value, "lobj_Module72", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lobj_Module72"):
                opp_val = getattr(value, "lobj_Module72", None)
                setattr(value, "lobj_Module72", self)

    @property
    def lobj_AccessControl21(self):
        return self.__lobj_AccessControl21

    @lobj_AccessControl21.setter
    def lobj_AccessControl21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lobj_AccessControl__lobj_AccessControl21", None)
        self.__lobj_AccessControl21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lobj_BlockFolder20"):
                opp_val = getattr(old_value, "lobj_BlockFolder20", None)
                if opp_val == self:
                    setattr(old_value, "lobj_BlockFolder20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lobj_BlockFolder20"):
                opp_val = getattr(value, "lobj_BlockFolder20", None)
                setattr(value, "lobj_BlockFolder20", self)

    @property
    def lobj_AccessControl129(self):
        return self.__lobj_AccessControl129

    @lobj_AccessControl129.setter
    def lobj_AccessControl129(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lobj_AccessControl__lobj_AccessControl129", None)
        self.__lobj_AccessControl129 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lobj_Sharednotes"):
                opp_val = getattr(old_value, "lobj_Sharednotes", None)
                if opp_val == self:
                    setattr(old_value, "lobj_Sharednotes", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lobj_Sharednotes"):
                opp_val = getattr(value, "lobj_Sharednotes", None)
                setattr(value, "lobj_Sharednotes", self)

class lobj_ExternalMetadata:

    def __init__(self, ref: str, file: str, id: str, lobj_ExternalMetadata: "lobj_Block" = None, lobj_ExternalMetadata33: "lobj_Course" = None, lobj_ExternalMetadata46: "lobj_LearningUnit" = None, lobj_ExternalMetadata68: "lobj_Module" = None):
        self.ref = ref
        self.file = file
        self.id = id
        self.lobj_ExternalMetadata = lobj_ExternalMetadata
        self.lobj_ExternalMetadata33 = lobj_ExternalMetadata33
        self.lobj_ExternalMetadata46 = lobj_ExternalMetadata46
        self.lobj_ExternalMetadata68 = lobj_ExternalMetadata68
        
    @property
    def ref(self) -> str:
        return self.__ref

    @ref.setter
    def ref(self, ref: str):
        self.__ref = ref

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def file(self) -> str:
        return self.__file

    @file.setter
    def file(self, file: str):
        self.__file = file

    @property
    def lobj_ExternalMetadata68(self):
        return self.__lobj_ExternalMetadata68

    @lobj_ExternalMetadata68.setter
    def lobj_ExternalMetadata68(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lobj_ExternalMetadata__lobj_ExternalMetadata68", None)
        self.__lobj_ExternalMetadata68 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lobj_Module67"):
                opp_val = getattr(old_value, "lobj_Module67", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lobj_Module67"):
                opp_val = getattr(value, "lobj_Module67", None)
                if opp_val is None:
                    setattr(value, "lobj_Module67", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def lobj_ExternalMetadata33(self):
        return self.__lobj_ExternalMetadata33

    @lobj_ExternalMetadata33.setter
    def lobj_ExternalMetadata33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lobj_ExternalMetadata__lobj_ExternalMetadata33", None)
        self.__lobj_ExternalMetadata33 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lobj_Course32"):
                opp_val = getattr(old_value, "lobj_Course32", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lobj_Course32"):
                opp_val = getattr(value, "lobj_Course32", None)
                if opp_val is None:
                    setattr(value, "lobj_Course32", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def lobj_ExternalMetadata46(self):
        return self.__lobj_ExternalMetadata46

    @lobj_ExternalMetadata46.setter
    def lobj_ExternalMetadata46(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lobj_ExternalMetadata__lobj_ExternalMetadata46", None)
        self.__lobj_ExternalMetadata46 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lobj_LearningUnit45"):
                opp_val = getattr(old_value, "lobj_LearningUnit45", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lobj_LearningUnit45"):
                opp_val = getattr(value, "lobj_LearningUnit45", None)
                if opp_val is None:
                    setattr(value, "lobj_LearningUnit45", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def lobj_ExternalMetadata(self):
        return self.__lobj_ExternalMetadata

    @lobj_ExternalMetadata.setter
    def lobj_ExternalMetadata(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lobj_ExternalMetadata__lobj_ExternalMetadata", None)
        self.__lobj_ExternalMetadata = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lobj_Block2"):
                opp_val = getattr(old_value, "lobj_Block2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lobj_Block2"):
                opp_val = getattr(value, "lobj_Block2", None)
                if opp_val is None:
                    setattr(value, "lobj_Block2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class LearningObject:

    pass
class lobj_Category(LearningObject):

    pass
class lobj_FolderMeta(LearningObject):

    def __init__(self, title: str, description: str, creationDate: date, lobj_FolderMeta: "lobj_BlockFolder" = None, lobj_FolderMeta54: "lobj_LuFolder" = None, lobj_FolderMeta86: "lobj_ResrcFolder" = None, lobj_FolderMeta75: "lobj_ModuleFolder" = None):
        self.title = title
        self.description = description
        self.creationDate = creationDate
        self.lobj_FolderMeta = lobj_FolderMeta
        self.lobj_FolderMeta54 = lobj_FolderMeta54
        self.lobj_FolderMeta86 = lobj_FolderMeta86
        self.lobj_FolderMeta75 = lobj_FolderMeta75
        
    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def creationDate(self) -> date:
        return self.__creationDate

    @creationDate.setter
    def creationDate(self, creationDate: date):
        self.__creationDate = creationDate

    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def lobj_FolderMeta75(self):
        return self.__lobj_FolderMeta75

    @lobj_FolderMeta75.setter
    def lobj_FolderMeta75(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lobj_FolderMeta__lobj_FolderMeta75", None)
        self.__lobj_FolderMeta75 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lobj_ModuleFolder"):
                opp_val = getattr(old_value, "lobj_ModuleFolder", None)
                if opp_val == self:
                    setattr(old_value, "lobj_ModuleFolder", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lobj_ModuleFolder"):
                opp_val = getattr(value, "lobj_ModuleFolder", None)
                setattr(value, "lobj_ModuleFolder", self)

    @property
    def lobj_FolderMeta(self):
        return self.__lobj_FolderMeta

    @lobj_FolderMeta.setter
    def lobj_FolderMeta(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lobj_FolderMeta__lobj_FolderMeta", None)
        self.__lobj_FolderMeta = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lobj_BlockFolder"):
                opp_val = getattr(old_value, "lobj_BlockFolder", None)
                if opp_val == self:
                    setattr(old_value, "lobj_BlockFolder", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lobj_BlockFolder"):
                opp_val = getattr(value, "lobj_BlockFolder", None)
                setattr(value, "lobj_BlockFolder", self)

    @property
    def lobj_FolderMeta54(self):
        return self.__lobj_FolderMeta54

    @lobj_FolderMeta54.setter
    def lobj_FolderMeta54(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lobj_FolderMeta__lobj_FolderMeta54", None)
        self.__lobj_FolderMeta54 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lobj_LuFolder"):
                opp_val = getattr(old_value, "lobj_LuFolder", None)
                if opp_val == self:
                    setattr(old_value, "lobj_LuFolder", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lobj_LuFolder"):
                opp_val = getattr(value, "lobj_LuFolder", None)
                setattr(value, "lobj_LuFolder", self)

    @property
    def lobj_FolderMeta86(self):
        return self.__lobj_FolderMeta86

    @lobj_FolderMeta86.setter
    def lobj_FolderMeta86(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lobj_FolderMeta__lobj_FolderMeta86", None)
        self.__lobj_FolderMeta86 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lobj_ResrcFolder"):
                opp_val = getattr(old_value, "lobj_ResrcFolder", None)
                if opp_val == self:
                    setattr(old_value, "lobj_ResrcFolder", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lobj_ResrcFolder"):
                opp_val = getattr(value, "lobj_ResrcFolder", None)
                setattr(value, "lobj_ResrcFolder", self)

class lobj_BlockAudiofile(LearningObject):

    def __init__(self, originalextension: str, filesize: int, resrcHref: str, file: str, lobj_BlockAudiofile: "lobj_HypertextContent" = None, lobj_BlockAudiofile118: "lobj_ResrcFiletype" = None):
        self.originalextension = originalextension
        self.filesize = filesize
        self.resrcHref = resrcHref
        self.file = file
        self.lobj_BlockAudiofile = lobj_BlockAudiofile
        self.lobj_BlockAudiofile118 = lobj_BlockAudiofile118
        
    @property
    def originalextension(self) -> str:
        return self.__originalextension

    @originalextension.setter
    def originalextension(self, originalextension: str):
        self.__originalextension = originalextension

    @property
    def filesize(self) -> int:
        return self.__filesize

    @filesize.setter
    def filesize(self, filesize: int):
        self.__filesize = filesize

    @property
    def resrcHref(self) -> str:
        return self.__resrcHref

    @resrcHref.setter
    def resrcHref(self, resrcHref: str):
        self.__resrcHref = resrcHref

    @property
    def file(self) -> str:
        return self.__file

    @file.setter
    def file(self, file: str):
        self.__file = file

    @property
    def lobj_BlockAudiofile118(self):
        return self.__lobj_BlockAudiofile118

    @lobj_BlockAudiofile118.setter
    def lobj_BlockAudiofile118(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lobj_BlockAudiofile__lobj_BlockAudiofile118", None)
        self.__lobj_BlockAudiofile118 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lobj_ResrcFiletype119"):
                opp_val = getattr(old_value, "lobj_ResrcFiletype119", None)
                if opp_val == self:
                    setattr(old_value, "lobj_ResrcFiletype119", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lobj_ResrcFiletype119"):
                opp_val = getattr(value, "lobj_ResrcFiletype119", None)
                setattr(value, "lobj_ResrcFiletype119", self)

    @property
    def lobj_BlockAudiofile(self):
        return self.__lobj_BlockAudiofile

    @lobj_BlockAudiofile.setter
    def lobj_BlockAudiofile(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lobj_BlockAudiofile__lobj_BlockAudiofile", None)
        self.__lobj_BlockAudiofile = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lobj_HypertextContent10"):
                opp_val = getattr(old_value, "lobj_HypertextContent10", None)
                if opp_val == self:
                    setattr(old_value, "lobj_HypertextContent10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lobj_HypertextContent10"):
                opp_val = getattr(value, "lobj_HypertextContent10", None)
                setattr(value, "lobj_HypertextContent10", self)

class lobj_LuFolder(LearningObject):

    pass
class lobj_CourseMeta(LearningObject):

    def __init__(self, fromext: str, hours: int, lvanr: str, columnfilterasxml: str, creationDate: date, lobj_CourseMeta: "lobj_Course" = None, lobj_CourseMeta152: set["lobj_DidacMeta"] = None, lobj_CourseMeta154: "lobj_User" = None, lobj_CourseMeta157: "lobj_Language" = None):
        self.fromext = fromext
        self.hours = hours
        self.lvanr = lvanr
        self.columnfilterasxml = columnfilterasxml
        self.creationDate = creationDate
        self.lobj_CourseMeta = lobj_CourseMeta
        self.lobj_CourseMeta152 = lobj_CourseMeta152 if lobj_CourseMeta152 is not None else set()
        self.lobj_CourseMeta154 = lobj_CourseMeta154
        self.lobj_CourseMeta157 = lobj_CourseMeta157
        
    @property
    def columnfilterasxml(self) -> str:
        return self.__columnfilterasxml

    @columnfilterasxml.setter
    def columnfilterasxml(self, columnfilterasxml: str):
        self.__columnfilterasxml = columnfilterasxml

    @property
    def hours(self) -> int:
        return self.__hours

    @hours.setter
    def hours(self, hours: int):
        self.__hours = hours

    @property
    def lvanr(self) -> str:
        return self.__lvanr

    @lvanr.setter
    def lvanr(self, lvanr: str):
        self.__lvanr = lvanr

    @property
    def creationDate(self) -> date:
        return self.__creationDate

    @creationDate.setter
    def creationDate(self, creationDate: date):
        self.__creationDate = creationDate

    @property
    def fromext(self) -> str:
        return self.__fromext

    @fromext.setter
    def fromext(self, fromext: str):
        self.__fromext = fromext

    @property
    def lobj_CourseMeta157(self):
        return self.__lobj_CourseMeta157

    @lobj_CourseMeta157.setter
    def lobj_CourseMeta157(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lobj_CourseMeta__lobj_CourseMeta157", None)
        self.__lobj_CourseMeta157 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lobj_Language158"):
                opp_val = getattr(old_value, "lobj_Language158", None)
                if opp_val == self:
                    setattr(old_value, "lobj_Language158", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lobj_Language158"):
                opp_val = getattr(value, "lobj_Language158", None)
                setattr(value, "lobj_Language158", self)

    @property
    def lobj_CourseMeta154(self):
        return self.__lobj_CourseMeta154

    @lobj_CourseMeta154.setter
    def lobj_CourseMeta154(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lobj_CourseMeta__lobj_CourseMeta154", None)
        self.__lobj_CourseMeta154 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lobj_User155"):
                opp_val = getattr(old_value, "lobj_User155", None)
                if opp_val == self:
                    setattr(old_value, "lobj_User155", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lobj_User155"):
                opp_val = getattr(value, "lobj_User155", None)
                setattr(value, "lobj_User155", self)

    @property
    def lobj_CourseMeta152(self):
        return self.__lobj_CourseMeta152

    @lobj_CourseMeta152.setter
    def lobj_CourseMeta152(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lobj_CourseMeta__lobj_CourseMeta152", None)
        self.__lobj_CourseMeta152 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "lobj_DidacMeta"):
                    opp_val = getattr(item, "lobj_DidacMeta", None)
                    
                    if opp_val == self:
                        setattr(item, "lobj_DidacMeta", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "lobj_DidacMeta"):
                    opp_val = getattr(item, "lobj_DidacMeta", None)
                    
                    setattr(item, "lobj_DidacMeta", self)
                    

    @property
    def lobj_CourseMeta(self):
        return self.__lobj_CourseMeta

    @lobj_CourseMeta.setter
    def lobj_CourseMeta(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lobj_CourseMeta__lobj_CourseMeta", None)
        self.__lobj_CourseMeta = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lobj_Course30"):
                opp_val = getattr(old_value, "lobj_Course30", None)
                if opp_val == self:
                    setattr(old_value, "lobj_Course30", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lobj_Course30"):
                opp_val = getattr(value, "lobj_Course30", None)
                setattr(value, "lobj_Course30", self)

class lobj_ModuleFolder(LearningObject):

    pass
class lobj_LearningUnit(LearningObject):

    def __init__(self, treeAsXml: str, luFile: str, lobj_LearningUnit: "lobj_LuMeta" = None, lobj_LearningUnit45: set["lobj_ExternalMetadata"] = None, lobj_LearningUnit48: "lobj_AccessControl" = None, lobj_LearningUnit51: set["lobj_Item"] = None, lobj_LearningUnit60: "lobj_LuFolder" = None, lobj_LearningUnit105: "lobj_LuNode" = None):
        self.treeAsXml = treeAsXml
        self.luFile = luFile
        self.lobj_LearningUnit = lobj_LearningUnit
        self.lobj_LearningUnit45 = lobj_LearningUnit45 if lobj_LearningUnit45 is not None else set()
        self.lobj_LearningUnit48 = lobj_LearningUnit48
        self.lobj_LearningUnit51 = lobj_LearningUnit51 if lobj_LearningUnit51 is not None else set()
        self.lobj_LearningUnit60 = lobj_LearningUnit60
        self.lobj_LearningUnit105 = lobj_LearningUnit105
        
    @property
    def luFile(self) -> str:
        return self.__luFile

    @luFile.setter
    def luFile(self, luFile: str):
        self.__luFile = luFile

    @property
    def treeAsXml(self) -> str:
        return self.__treeAsXml

    @treeAsXml.setter
    def treeAsXml(self, treeAsXml: str):
        self.__treeAsXml = treeAsXml

    @property
    def lobj_LearningUnit51(self):
        return self.__lobj_LearningUnit51

    @lobj_LearningUnit51.setter
    def lobj_LearningUnit51(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lobj_LearningUnit__lobj_LearningUnit51", None)
        self.__lobj_LearningUnit51 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "lobj_Item52"):
                    opp_val = getattr(item, "lobj_Item52", None)
                    
                    if opp_val == self:
                        setattr(item, "lobj_Item52", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "lobj_Item52"):
                    opp_val = getattr(item, "lobj_Item52", None)
                    
                    setattr(item, "lobj_Item52", self)
                    

    @property
    def lobj_LearningUnit60(self):
        return self.__lobj_LearningUnit60

    @lobj_LearningUnit60.setter
    def lobj_LearningUnit60(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lobj_LearningUnit__lobj_LearningUnit60", None)
        self.__lobj_LearningUnit60 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lobj_LuFolder59"):
                opp_val = getattr(old_value, "lobj_LuFolder59", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lobj_LuFolder59"):
                opp_val = getattr(value, "lobj_LuFolder59", None)
                if opp_val is None:
                    setattr(value, "lobj_LuFolder59", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def lobj_LearningUnit(self):
        return self.__lobj_LearningUnit

    @lobj_LearningUnit.setter
    def lobj_LearningUnit(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lobj_LearningUnit__lobj_LearningUnit", None)
        self.__lobj_LearningUnit = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lobj_LuMeta"):
                opp_val = getattr(old_value, "lobj_LuMeta", None)
                if opp_val == self:
                    setattr(old_value, "lobj_LuMeta", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lobj_LuMeta"):
                opp_val = getattr(value, "lobj_LuMeta", None)
                setattr(value, "lobj_LuMeta", self)

    @property
    def lobj_LearningUnit105(self):
        return self.__lobj_LearningUnit105

    @lobj_LearningUnit105.setter
    def lobj_LearningUnit105(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lobj_LearningUnit__lobj_LearningUnit105", None)
        self.__lobj_LearningUnit105 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lobj_LuNode"):
                opp_val = getattr(old_value, "lobj_LuNode", None)
                if opp_val == self:
                    setattr(old_value, "lobj_LuNode", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lobj_LuNode"):
                opp_val = getattr(value, "lobj_LuNode", None)
                setattr(value, "lobj_LuNode", self)

    @property
    def lobj_LearningUnit45(self):
        return self.__lobj_LearningUnit45

    @lobj_LearningUnit45.setter
    def lobj_LearningUnit45(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lobj_LearningUnit__lobj_LearningUnit45", None)
        self.__lobj_LearningUnit45 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "lobj_ExternalMetadata46"):
                    opp_val = getattr(item, "lobj_ExternalMetadata46", None)
                    
                    if opp_val == self:
                        setattr(item, "lobj_ExternalMetadata46", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "lobj_ExternalMetadata46"):
                    opp_val = getattr(item, "lobj_ExternalMetadata46", None)
                    
                    setattr(item, "lobj_ExternalMetadata46", self)
                    

    @property
    def lobj_LearningUnit48(self):
        return self.__lobj_LearningUnit48

    @lobj_LearningUnit48.setter
    def lobj_LearningUnit48(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lobj_LearningUnit__lobj_LearningUnit48", None)
        self.__lobj_LearningUnit48 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lobj_AccessControl49"):
                opp_val = getattr(old_value, "lobj_AccessControl49", None)
                if opp_val == self:
                    setattr(old_value, "lobj_AccessControl49", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lobj_AccessControl49"):
                opp_val = getattr(value, "lobj_AccessControl49", None)
                setattr(value, "lobj_AccessControl49", self)

class lobj_ResrcMeta(LearningObject):

    def __init__(self, filename: str, parameters: str, height: int, width: int, creationDate: date, lastModified: date, title: str, description: str, keywords: str, lobj_ResrcMeta: "lobj_ResrcFile" = None):
        self.filename = filename
        self.parameters = parameters
        self.height = height
        self.width = width
        self.creationDate = creationDate
        self.lastModified = lastModified
        self.title = title
        self.description = description
        self.keywords = keywords
        self.lobj_ResrcMeta = lobj_ResrcMeta
        
    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def parameters(self) -> str:
        return self.__parameters

    @parameters.setter
    def parameters(self, parameters: str):
        self.__parameters = parameters

    @property
    def creationDate(self) -> date:
        return self.__creationDate

    @creationDate.setter
    def creationDate(self, creationDate: date):
        self.__creationDate = creationDate

    @property
    def lastModified(self) -> date:
        return self.__lastModified

    @lastModified.setter
    def lastModified(self, lastModified: date):
        self.__lastModified = lastModified

    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def filename(self) -> str:
        return self.__filename

    @filename.setter
    def filename(self, filename: str):
        self.__filename = filename

    @property
    def keywords(self) -> str:
        return self.__keywords

    @keywords.setter
    def keywords(self, keywords: str):
        self.__keywords = keywords

    @property
    def height(self) -> int:
        return self.__height

    @height.setter
    def height(self, height: int):
        self.__height = height

    @property
    def width(self) -> int:
        return self.__width

    @width.setter
    def width(self, width: int):
        self.__width = width

    @property
    def lobj_ResrcMeta(self):
        return self.__lobj_ResrcMeta

    @lobj_ResrcMeta.setter
    def lobj_ResrcMeta(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lobj_ResrcMeta__lobj_ResrcMeta", None)
        self.__lobj_ResrcMeta = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lobj_ResrcFile116"):
                opp_val = getattr(old_value, "lobj_ResrcFile116", None)
                if opp_val == self:
                    setattr(old_value, "lobj_ResrcFile116", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lobj_ResrcFile116"):
                opp_val = getattr(value, "lobj_ResrcFile116", None)
                setattr(value, "lobj_ResrcFile116", self)

class lobj_BlockMeta(LearningObject):

    def __init__(self, lod: str, rendering: str, creationDate: date, lastModified: date, lobj_BlockMeta: "lobj_Block" = None, lobj_BlockMeta140: "lobj_Blocktype" = None, lobj_BlockMeta142: set["lobj_SimpleDidacMeta"] = None, lobj_BlockMeta145: "lobj_Language" = None):
        self.lod = lod
        self.rendering = rendering
        self.creationDate = creationDate
        self.lastModified = lastModified
        self.lobj_BlockMeta = lobj_BlockMeta
        self.lobj_BlockMeta140 = lobj_BlockMeta140
        self.lobj_BlockMeta142 = lobj_BlockMeta142 if lobj_BlockMeta142 is not None else set()
        self.lobj_BlockMeta145 = lobj_BlockMeta145
        
    @property
    def lod(self) -> str:
        return self.__lod

    @lod.setter
    def lod(self, lod: str):
        self.__lod = lod

    @property
    def creationDate(self) -> date:
        return self.__creationDate

    @creationDate.setter
    def creationDate(self, creationDate: date):
        self.__creationDate = creationDate

    @property
    def rendering(self) -> str:
        return self.__rendering

    @rendering.setter
    def rendering(self, rendering: str):
        self.__rendering = rendering

    @property
    def lastModified(self) -> date:
        return self.__lastModified

    @lastModified.setter
    def lastModified(self, lastModified: date):
        self.__lastModified = lastModified

    @property
    def lobj_BlockMeta142(self):
        return self.__lobj_BlockMeta142

    @lobj_BlockMeta142.setter
    def lobj_BlockMeta142(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lobj_BlockMeta__lobj_BlockMeta142", None)
        self.__lobj_BlockMeta142 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "lobj_SimpleDidacMeta143"):
                    opp_val = getattr(item, "lobj_SimpleDidacMeta143", None)
                    
                    if opp_val == self:
                        setattr(item, "lobj_SimpleDidacMeta143", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "lobj_SimpleDidacMeta143"):
                    opp_val = getattr(item, "lobj_SimpleDidacMeta143", None)
                    
                    setattr(item, "lobj_SimpleDidacMeta143", self)
                    

    @property
    def lobj_BlockMeta145(self):
        return self.__lobj_BlockMeta145

    @lobj_BlockMeta145.setter
    def lobj_BlockMeta145(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lobj_BlockMeta__lobj_BlockMeta145", None)
        self.__lobj_BlockMeta145 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lobj_Language146"):
                opp_val = getattr(old_value, "lobj_Language146", None)
                if opp_val == self:
                    setattr(old_value, "lobj_Language146", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lobj_Language146"):
                opp_val = getattr(value, "lobj_Language146", None)
                setattr(value, "lobj_Language146", self)

    @property
    def lobj_BlockMeta(self):
        return self.__lobj_BlockMeta

    @lobj_BlockMeta.setter
    def lobj_BlockMeta(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lobj_BlockMeta__lobj_BlockMeta", None)
        self.__lobj_BlockMeta = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lobj_Block"):
                opp_val = getattr(old_value, "lobj_Block", None)
                if opp_val == self:
                    setattr(old_value, "lobj_Block", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lobj_Block"):
                opp_val = getattr(value, "lobj_Block", None)
                setattr(value, "lobj_Block", self)

    @property
    def lobj_BlockMeta140(self):
        return self.__lobj_BlockMeta140

    @lobj_BlockMeta140.setter
    def lobj_BlockMeta140(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lobj_BlockMeta__lobj_BlockMeta140", None)
        self.__lobj_BlockMeta140 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lobj_Blocktype"):
                opp_val = getattr(old_value, "lobj_Blocktype", None)
                if opp_val == self:
                    setattr(old_value, "lobj_Blocktype", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lobj_Blocktype"):
                opp_val = getattr(value, "lobj_Blocktype", None)
                setattr(value, "lobj_Blocktype", self)

class lobj_ModuleMeta(LearningObject):

    def __init__(self, creationDate: date, lobj_ModuleMeta: "lobj_Module" = None, lobj_ModuleMeta202: set["lobj_DidacMeta"] = None, lobj_ModuleMeta205: set["lobj_Author"] = None, lobj_ModuleMeta208: "lobj_PublishInfo" = None, lobj_ModuleMeta211: "lobj_Language" = None):
        self.creationDate = creationDate
        self.lobj_ModuleMeta = lobj_ModuleMeta
        self.lobj_ModuleMeta202 = lobj_ModuleMeta202 if lobj_ModuleMeta202 is not None else set()
        self.lobj_ModuleMeta205 = lobj_ModuleMeta205 if lobj_ModuleMeta205 is not None else set()
        self.lobj_ModuleMeta208 = lobj_ModuleMeta208
        self.lobj_ModuleMeta211 = lobj_ModuleMeta211
        
    @property
    def creationDate(self) -> date:
        return self.__creationDate

    @creationDate.setter
    def creationDate(self, creationDate: date):
        self.__creationDate = creationDate

    @property
    def lobj_ModuleMeta211(self):
        return self.__lobj_ModuleMeta211

    @lobj_ModuleMeta211.setter
    def lobj_ModuleMeta211(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lobj_ModuleMeta__lobj_ModuleMeta211", None)
        self.__lobj_ModuleMeta211 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lobj_Language212"):
                opp_val = getattr(old_value, "lobj_Language212", None)
                if opp_val == self:
                    setattr(old_value, "lobj_Language212", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lobj_Language212"):
                opp_val = getattr(value, "lobj_Language212", None)
                setattr(value, "lobj_Language212", self)

    @property
    def lobj_ModuleMeta205(self):
        return self.__lobj_ModuleMeta205

    @lobj_ModuleMeta205.setter
    def lobj_ModuleMeta205(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lobj_ModuleMeta__lobj_ModuleMeta205", None)
        self.__lobj_ModuleMeta205 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "lobj_Author206"):
                    opp_val = getattr(item, "lobj_Author206", None)
                    
                    if opp_val == self:
                        setattr(item, "lobj_Author206", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "lobj_Author206"):
                    opp_val = getattr(item, "lobj_Author206", None)
                    
                    setattr(item, "lobj_Author206", self)
                    

    @property
    def lobj_ModuleMeta(self):
        return self.__lobj_ModuleMeta

    @lobj_ModuleMeta.setter
    def lobj_ModuleMeta(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lobj_ModuleMeta__lobj_ModuleMeta", None)
        self.__lobj_ModuleMeta = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lobj_Module65"):
                opp_val = getattr(old_value, "lobj_Module65", None)
                if opp_val == self:
                    setattr(old_value, "lobj_Module65", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lobj_Module65"):
                opp_val = getattr(value, "lobj_Module65", None)
                setattr(value, "lobj_Module65", self)

    @property
    def lobj_ModuleMeta208(self):
        return self.__lobj_ModuleMeta208

    @lobj_ModuleMeta208.setter
    def lobj_ModuleMeta208(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lobj_ModuleMeta__lobj_ModuleMeta208", None)
        self.__lobj_ModuleMeta208 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lobj_PublishInfo209"):
                opp_val = getattr(old_value, "lobj_PublishInfo209", None)
                if opp_val == self:
                    setattr(old_value, "lobj_PublishInfo209", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lobj_PublishInfo209"):
                opp_val = getattr(value, "lobj_PublishInfo209", None)
                setattr(value, "lobj_PublishInfo209", self)

    @property
    def lobj_ModuleMeta202(self):
        return self.__lobj_ModuleMeta202

    @lobj_ModuleMeta202.setter
    def lobj_ModuleMeta202(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lobj_ModuleMeta__lobj_ModuleMeta202", None)
        self.__lobj_ModuleMeta202 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "lobj_DidacMeta203"):
                    opp_val = getattr(item, "lobj_DidacMeta203", None)
                    
                    if opp_val == self:
                        setattr(item, "lobj_DidacMeta203", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "lobj_DidacMeta203"):
                    opp_val = getattr(item, "lobj_DidacMeta203", None)
                    
                    setattr(item, "lobj_DidacMeta203", self)
                    

class lobj_LuMeta(LearningObject):

    def __init__(self, creationDate: date, lobj_LuMeta: "lobj_LearningUnit" = None, lobj_LuMeta176: "lobj_Language" = None, lobj_LuMeta166: set["lobj_DidacMeta"] = None, lobj_LuMeta169: "lobj_Domain" = None, lobj_LuMeta171: set["lobj_Author"] = None, lobj_LuMeta174: "lobj_PublishInfo" = None):
        self.creationDate = creationDate
        self.lobj_LuMeta = lobj_LuMeta
        self.lobj_LuMeta176 = lobj_LuMeta176
        self.lobj_LuMeta166 = lobj_LuMeta166 if lobj_LuMeta166 is not None else set()
        self.lobj_LuMeta169 = lobj_LuMeta169
        self.lobj_LuMeta171 = lobj_LuMeta171 if lobj_LuMeta171 is not None else set()
        self.lobj_LuMeta174 = lobj_LuMeta174
        
    @property
    def creationDate(self) -> date:
        return self.__creationDate

    @creationDate.setter
    def creationDate(self, creationDate: date):
        self.__creationDate = creationDate

    @property
    def lobj_LuMeta(self):
        return self.__lobj_LuMeta

    @lobj_LuMeta.setter
    def lobj_LuMeta(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lobj_LuMeta__lobj_LuMeta", None)
        self.__lobj_LuMeta = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lobj_LearningUnit"):
                opp_val = getattr(old_value, "lobj_LearningUnit", None)
                if opp_val == self:
                    setattr(old_value, "lobj_LearningUnit", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lobj_LearningUnit"):
                opp_val = getattr(value, "lobj_LearningUnit", None)
                setattr(value, "lobj_LearningUnit", self)

    @property
    def lobj_LuMeta169(self):
        return self.__lobj_LuMeta169

    @lobj_LuMeta169.setter
    def lobj_LuMeta169(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lobj_LuMeta__lobj_LuMeta169", None)
        self.__lobj_LuMeta169 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lobj_Domain"):
                opp_val = getattr(old_value, "lobj_Domain", None)
                if opp_val == self:
                    setattr(old_value, "lobj_Domain", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lobj_Domain"):
                opp_val = getattr(value, "lobj_Domain", None)
                setattr(value, "lobj_Domain", self)

    @property
    def lobj_LuMeta171(self):
        return self.__lobj_LuMeta171

    @lobj_LuMeta171.setter
    def lobj_LuMeta171(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lobj_LuMeta__lobj_LuMeta171", None)
        self.__lobj_LuMeta171 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "lobj_Author172"):
                    opp_val = getattr(item, "lobj_Author172", None)
                    
                    if opp_val == self:
                        setattr(item, "lobj_Author172", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "lobj_Author172"):
                    opp_val = getattr(item, "lobj_Author172", None)
                    
                    setattr(item, "lobj_Author172", self)
                    

    @property
    def lobj_LuMeta166(self):
        return self.__lobj_LuMeta166

    @lobj_LuMeta166.setter
    def lobj_LuMeta166(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lobj_LuMeta__lobj_LuMeta166", None)
        self.__lobj_LuMeta166 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "lobj_DidacMeta167"):
                    opp_val = getattr(item, "lobj_DidacMeta167", None)
                    
                    if opp_val == self:
                        setattr(item, "lobj_DidacMeta167", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "lobj_DidacMeta167"):
                    opp_val = getattr(item, "lobj_DidacMeta167", None)
                    
                    setattr(item, "lobj_DidacMeta167", self)
                    

    @property
    def lobj_LuMeta174(self):
        return self.__lobj_LuMeta174

    @lobj_LuMeta174.setter
    def lobj_LuMeta174(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lobj_LuMeta__lobj_LuMeta174", None)
        self.__lobj_LuMeta174 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lobj_PublishInfo"):
                opp_val = getattr(old_value, "lobj_PublishInfo", None)
                if opp_val == self:
                    setattr(old_value, "lobj_PublishInfo", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lobj_PublishInfo"):
                opp_val = getattr(value, "lobj_PublishInfo", None)
                setattr(value, "lobj_PublishInfo", self)

    @property
    def lobj_LuMeta176(self):
        return self.__lobj_LuMeta176

    @lobj_LuMeta176.setter
    def lobj_LuMeta176(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lobj_LuMeta__lobj_LuMeta176", None)
        self.__lobj_LuMeta176 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lobj_Language177"):
                opp_val = getattr(old_value, "lobj_Language177", None)
                if opp_val == self:
                    setattr(old_value, "lobj_Language177", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lobj_Language177"):
                opp_val = getattr(value, "lobj_Language177", None)
                setattr(value, "lobj_Language177", self)

class lobj_AbstractContent(LearningObject):

    def __init__(self, heading: str, lobj_AbstractContent: "lobj_Language" = None, lobj_AbstractContent8: "lobj_Source" = None):
        self.heading = heading
        self.lobj_AbstractContent = lobj_AbstractContent
        self.lobj_AbstractContent8 = lobj_AbstractContent8
        
    @property
    def heading(self) -> str:
        return self.__heading

    @heading.setter
    def heading(self, heading: str):
        self.__heading = heading

    @property
    def lobj_AbstractContent8(self):
        return self.__lobj_AbstractContent8

    @lobj_AbstractContent8.setter
    def lobj_AbstractContent8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lobj_AbstractContent__lobj_AbstractContent8", None)
        self.__lobj_AbstractContent8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lobj_Source"):
                opp_val = getattr(old_value, "lobj_Source", None)
                if opp_val == self:
                    setattr(old_value, "lobj_Source", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lobj_Source"):
                opp_val = getattr(value, "lobj_Source", None)
                setattr(value, "lobj_Source", self)

    @property
    def lobj_AbstractContent(self):
        return self.__lobj_AbstractContent

    @lobj_AbstractContent.setter
    def lobj_AbstractContent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lobj_AbstractContent__lobj_AbstractContent", None)
        self.__lobj_AbstractContent = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lobj_Language"):
                opp_val = getattr(old_value, "lobj_Language", None)
                if opp_val == self:
                    setattr(old_value, "lobj_Language", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lobj_Language"):
                opp_val = getattr(value, "lobj_Language", None)
                setattr(value, "lobj_Language", self)

class lobj_Course(LearningObject):

    def __init__(self, outlineAsXml: str, lobj_Course: "lobj_Category" = None, lobj_Course35: "lobj_Coursetype" = None, lobj_Course30: "lobj_CourseMeta" = None, lobj_Course32: set["lobj_ExternalMetadata"] = None, lobj_Course37: set["lobj_Module"] = None):
        self.outlineAsXml = outlineAsXml
        self.lobj_Course = lobj_Course
        self.lobj_Course35 = lobj_Course35
        self.lobj_Course30 = lobj_Course30
        self.lobj_Course32 = lobj_Course32 if lobj_Course32 is not None else set()
        self.lobj_Course37 = lobj_Course37 if lobj_Course37 is not None else set()
        
    @property
    def outlineAsXml(self) -> str:
        return self.__outlineAsXml

    @outlineAsXml.setter
    def outlineAsXml(self, outlineAsXml: str):
        self.__outlineAsXml = outlineAsXml

    @property
    def lobj_Course30(self):
        return self.__lobj_Course30

    @lobj_Course30.setter
    def lobj_Course30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lobj_Course__lobj_Course30", None)
        self.__lobj_Course30 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lobj_CourseMeta"):
                opp_val = getattr(old_value, "lobj_CourseMeta", None)
                if opp_val == self:
                    setattr(old_value, "lobj_CourseMeta", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lobj_CourseMeta"):
                opp_val = getattr(value, "lobj_CourseMeta", None)
                setattr(value, "lobj_CourseMeta", self)

    @property
    def lobj_Course35(self):
        return self.__lobj_Course35

    @lobj_Course35.setter
    def lobj_Course35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lobj_Course__lobj_Course35", None)
        self.__lobj_Course35 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lobj_Coursetype"):
                opp_val = getattr(old_value, "lobj_Coursetype", None)
                if opp_val == self:
                    setattr(old_value, "lobj_Coursetype", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lobj_Coursetype"):
                opp_val = getattr(value, "lobj_Coursetype", None)
                setattr(value, "lobj_Coursetype", self)

    @property
    def lobj_Course32(self):
        return self.__lobj_Course32

    @lobj_Course32.setter
    def lobj_Course32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lobj_Course__lobj_Course32", None)
        self.__lobj_Course32 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "lobj_ExternalMetadata33"):
                    opp_val = getattr(item, "lobj_ExternalMetadata33", None)
                    
                    if opp_val == self:
                        setattr(item, "lobj_ExternalMetadata33", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "lobj_ExternalMetadata33"):
                    opp_val = getattr(item, "lobj_ExternalMetadata33", None)
                    
                    setattr(item, "lobj_ExternalMetadata33", self)
                    

    @property
    def lobj_Course(self):
        return self.__lobj_Course

    @lobj_Course.setter
    def lobj_Course(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lobj_Course__lobj_Course", None)
        self.__lobj_Course = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lobj_Category24"):
                opp_val = getattr(old_value, "lobj_Category24", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lobj_Category24"):
                opp_val = getattr(value, "lobj_Category24", None)
                if opp_val is None:
                    setattr(value, "lobj_Category24", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def lobj_Course37(self):
        return self.__lobj_Course37

    @lobj_Course37.setter
    def lobj_Course37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lobj_Course__lobj_Course37", None)
        self.__lobj_Course37 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "lobj_Module"):
                    opp_val = getattr(item, "lobj_Module", None)
                    
                    if opp_val == self:
                        setattr(item, "lobj_Module", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "lobj_Module"):
                    opp_val = getattr(item, "lobj_Module", None)
                    
                    setattr(item, "lobj_Module", self)
                    

class lobj_BlockFolder(LearningObject):

    pass
class lobj_ResrcFile(LearningObject):

    def __init__(self, filesize: int, resrcHref: str, file: str, file_tn: str, originalextension: str, ResrcFile: "lobj_HypertextContent" = None, lobj_ResrcFile: "lobj_ResrcFolder" = None, lobj_ResrcFile107: "lobj_AccessControl" = None, lobj_ResrcFile110: "lobj_ResrcFiletype" = None, lobj_ResrcFile112: "lobj_Source" = None, resrcFile: set["lobj_HypertextContent"] = None, lobj_ResrcFile116: "lobj_ResrcMeta" = None):
        self.filesize = filesize
        self.resrcHref = resrcHref
        self.file = file
        self.file_tn = file_tn
        self.originalextension = originalextension
        self.ResrcFile = ResrcFile
        self.lobj_ResrcFile = lobj_ResrcFile
        self.lobj_ResrcFile107 = lobj_ResrcFile107
        self.lobj_ResrcFile110 = lobj_ResrcFile110
        self.lobj_ResrcFile112 = lobj_ResrcFile112
        self.resrcFile = resrcFile if resrcFile is not None else set()
        self.lobj_ResrcFile116 = lobj_ResrcFile116
        
    @property
    def resrcHref(self) -> str:
        return self.__resrcHref

    @resrcHref.setter
    def resrcHref(self, resrcHref: str):
        self.__resrcHref = resrcHref

    @property
    def originalextension(self) -> str:
        return self.__originalextension

    @originalextension.setter
    def originalextension(self, originalextension: str):
        self.__originalextension = originalextension

    @property
    def file(self) -> str:
        return self.__file

    @file.setter
    def file(self, file: str):
        self.__file = file

    @property
    def filesize(self) -> int:
        return self.__filesize

    @filesize.setter
    def filesize(self, filesize: int):
        self.__filesize = filesize

    @property
    def file_tn(self) -> str:
        return self.__file_tn

    @file_tn.setter
    def file_tn(self, file_tn: str):
        self.__file_tn = file_tn

    @property
    def resrcFile(self):
        return self.__resrcFile

    @resrcFile.setter
    def resrcFile(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lobj_ResrcFile__resrcFile", None)
        self.__resrcFile = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "HypertextContent"):
                    opp_val = getattr(item, "HypertextContent", None)
                    
                    if opp_val == self:
                        setattr(item, "HypertextContent", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "HypertextContent"):
                    opp_val = getattr(item, "HypertextContent", None)
                    
                    setattr(item, "HypertextContent", self)
                    

    @property
    def lobj_ResrcFile112(self):
        return self.__lobj_ResrcFile112

    @lobj_ResrcFile112.setter
    def lobj_ResrcFile112(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lobj_ResrcFile__lobj_ResrcFile112", None)
        self.__lobj_ResrcFile112 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lobj_Source113"):
                opp_val = getattr(old_value, "lobj_Source113", None)
                if opp_val == self:
                    setattr(old_value, "lobj_Source113", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lobj_Source113"):
                opp_val = getattr(value, "lobj_Source113", None)
                setattr(value, "lobj_Source113", self)

    @property
    def lobj_ResrcFile116(self):
        return self.__lobj_ResrcFile116

    @lobj_ResrcFile116.setter
    def lobj_ResrcFile116(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lobj_ResrcFile__lobj_ResrcFile116", None)
        self.__lobj_ResrcFile116 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lobj_ResrcMeta"):
                opp_val = getattr(old_value, "lobj_ResrcMeta", None)
                if opp_val == self:
                    setattr(old_value, "lobj_ResrcMeta", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lobj_ResrcMeta"):
                opp_val = getattr(value, "lobj_ResrcMeta", None)
                setattr(value, "lobj_ResrcMeta", self)

    @property
    def lobj_ResrcFile107(self):
        return self.__lobj_ResrcFile107

    @lobj_ResrcFile107.setter
    def lobj_ResrcFile107(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lobj_ResrcFile__lobj_ResrcFile107", None)
        self.__lobj_ResrcFile107 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lobj_AccessControl108"):
                opp_val = getattr(old_value, "lobj_AccessControl108", None)
                if opp_val == self:
                    setattr(old_value, "lobj_AccessControl108", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lobj_AccessControl108"):
                opp_val = getattr(value, "lobj_AccessControl108", None)
                setattr(value, "lobj_AccessControl108", self)

    @property
    def ResrcFile(self):
        return self.__ResrcFile

    @ResrcFile.setter
    def ResrcFile(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lobj_ResrcFile__ResrcFile", None)
        self.__ResrcFile = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "hypertextContent"):
                opp_val = getattr(old_value, "hypertextContent", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "hypertextContent"):
                opp_val = getattr(value, "hypertextContent", None)
                if opp_val is None:
                    setattr(value, "hypertextContent", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def lobj_ResrcFile110(self):
        return self.__lobj_ResrcFile110

    @lobj_ResrcFile110.setter
    def lobj_ResrcFile110(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lobj_ResrcFile__lobj_ResrcFile110", None)
        self.__lobj_ResrcFile110 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lobj_ResrcFiletype"):
                opp_val = getattr(old_value, "lobj_ResrcFiletype", None)
                if opp_val == self:
                    setattr(old_value, "lobj_ResrcFiletype", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lobj_ResrcFiletype"):
                opp_val = getattr(value, "lobj_ResrcFiletype", None)
                setattr(value, "lobj_ResrcFiletype", self)

    @property
    def lobj_ResrcFile(self):
        return self.__lobj_ResrcFile

    @lobj_ResrcFile.setter
    def lobj_ResrcFile(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lobj_ResrcFile__lobj_ResrcFile", None)
        self.__lobj_ResrcFile = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lobj_ResrcFolder94"):
                opp_val = getattr(old_value, "lobj_ResrcFolder94", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lobj_ResrcFolder94"):
                opp_val = getattr(value, "lobj_ResrcFolder94", None)
                if opp_val is None:
                    setattr(value, "lobj_ResrcFolder94", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class lobj_Module(LearningObject):

    def __init__(self, moduleFile: str, treeAsXml: str, lobj_Module: "lobj_Course" = None, lobj_Module67: set["lobj_ExternalMetadata"] = None, lobj_Module65: "lobj_ModuleMeta" = None, lobj_Module70: "lobj_Node" = None, lobj_Module72: "lobj_AccessControl" = None, lobj_Module81: "lobj_ModuleFolder" = None):
        self.moduleFile = moduleFile
        self.treeAsXml = treeAsXml
        self.lobj_Module = lobj_Module
        self.lobj_Module67 = lobj_Module67 if lobj_Module67 is not None else set()
        self.lobj_Module65 = lobj_Module65
        self.lobj_Module70 = lobj_Module70
        self.lobj_Module72 = lobj_Module72
        self.lobj_Module81 = lobj_Module81
        
    @property
    def moduleFile(self) -> str:
        return self.__moduleFile

    @moduleFile.setter
    def moduleFile(self, moduleFile: str):
        self.__moduleFile = moduleFile

    @property
    def treeAsXml(self) -> str:
        return self.__treeAsXml

    @treeAsXml.setter
    def treeAsXml(self, treeAsXml: str):
        self.__treeAsXml = treeAsXml

    @property
    def lobj_Module72(self):
        return self.__lobj_Module72

    @lobj_Module72.setter
    def lobj_Module72(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lobj_Module__lobj_Module72", None)
        self.__lobj_Module72 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lobj_AccessControl73"):
                opp_val = getattr(old_value, "lobj_AccessControl73", None)
                if opp_val == self:
                    setattr(old_value, "lobj_AccessControl73", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lobj_AccessControl73"):
                opp_val = getattr(value, "lobj_AccessControl73", None)
                setattr(value, "lobj_AccessControl73", self)

    @property
    def lobj_Module70(self):
        return self.__lobj_Module70

    @lobj_Module70.setter
    def lobj_Module70(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lobj_Module__lobj_Module70", None)
        self.__lobj_Module70 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lobj_Node"):
                opp_val = getattr(old_value, "lobj_Node", None)
                if opp_val == self:
                    setattr(old_value, "lobj_Node", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lobj_Node"):
                opp_val = getattr(value, "lobj_Node", None)
                setattr(value, "lobj_Node", self)

    @property
    def lobj_Module81(self):
        return self.__lobj_Module81

    @lobj_Module81.setter
    def lobj_Module81(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lobj_Module__lobj_Module81", None)
        self.__lobj_Module81 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lobj_ModuleFolder80"):
                opp_val = getattr(old_value, "lobj_ModuleFolder80", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lobj_ModuleFolder80"):
                opp_val = getattr(value, "lobj_ModuleFolder80", None)
                if opp_val is None:
                    setattr(value, "lobj_ModuleFolder80", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def lobj_Module(self):
        return self.__lobj_Module

    @lobj_Module.setter
    def lobj_Module(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lobj_Module__lobj_Module", None)
        self.__lobj_Module = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lobj_Course37"):
                opp_val = getattr(old_value, "lobj_Course37", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lobj_Course37"):
                opp_val = getattr(value, "lobj_Course37", None)
                if opp_val is None:
                    setattr(value, "lobj_Course37", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def lobj_Module65(self):
        return self.__lobj_Module65

    @lobj_Module65.setter
    def lobj_Module65(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lobj_Module__lobj_Module65", None)
        self.__lobj_Module65 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lobj_ModuleMeta"):
                opp_val = getattr(old_value, "lobj_ModuleMeta", None)
                if opp_val == self:
                    setattr(old_value, "lobj_ModuleMeta", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lobj_ModuleMeta"):
                opp_val = getattr(value, "lobj_ModuleMeta", None)
                setattr(value, "lobj_ModuleMeta", self)

    @property
    def lobj_Module67(self):
        return self.__lobj_Module67

    @lobj_Module67.setter
    def lobj_Module67(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lobj_Module__lobj_Module67", None)
        self.__lobj_Module67 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "lobj_ExternalMetadata68"):
                    opp_val = getattr(item, "lobj_ExternalMetadata68", None)
                    
                    if opp_val == self:
                        setattr(item, "lobj_ExternalMetadata68", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "lobj_ExternalMetadata68"):
                    opp_val = getattr(item, "lobj_ExternalMetadata68", None)
                    
                    setattr(item, "lobj_ExternalMetadata68", self)
                    

class lobj_Theme(LearningObject):

    pass
class lobj_ResrcFolder(LearningObject):

    def __init__(self, deleteScheduled: bool, lobj_ResrcFolder: "lobj_FolderMeta" = None, lobj_ResrcFolder89: "lobj_ResrcFolder" = None, lobj_ResrcFolder87: set["lobj_ResrcFolder"] = None, lobj_ResrcFolder91: "lobj_AccessControl" = None, lobj_ResrcFolder94: set["lobj_ResrcFile"] = None):
        self.deleteScheduled = deleteScheduled
        self.lobj_ResrcFolder = lobj_ResrcFolder
        self.lobj_ResrcFolder89 = lobj_ResrcFolder89
        self.lobj_ResrcFolder87 = lobj_ResrcFolder87 if lobj_ResrcFolder87 is not None else set()
        self.lobj_ResrcFolder91 = lobj_ResrcFolder91
        self.lobj_ResrcFolder94 = lobj_ResrcFolder94 if lobj_ResrcFolder94 is not None else set()
        
    @property
    def deleteScheduled(self) -> bool:
        return self.__deleteScheduled

    @deleteScheduled.setter
    def deleteScheduled(self, deleteScheduled: bool):
        self.__deleteScheduled = deleteScheduled

    @property
    def lobj_ResrcFolder87(self):
        return self.__lobj_ResrcFolder87

    @lobj_ResrcFolder87.setter
    def lobj_ResrcFolder87(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lobj_ResrcFolder__lobj_ResrcFolder87", None)
        self.__lobj_ResrcFolder87 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "lobj_ResrcFolder89"):
                    opp_val = getattr(item, "lobj_ResrcFolder89", None)
                    
                    if opp_val == self:
                        setattr(item, "lobj_ResrcFolder89", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "lobj_ResrcFolder89"):
                    opp_val = getattr(item, "lobj_ResrcFolder89", None)
                    
                    setattr(item, "lobj_ResrcFolder89", self)
                    

    @property
    def lobj_ResrcFolder(self):
        return self.__lobj_ResrcFolder

    @lobj_ResrcFolder.setter
    def lobj_ResrcFolder(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lobj_ResrcFolder__lobj_ResrcFolder", None)
        self.__lobj_ResrcFolder = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lobj_FolderMeta86"):
                opp_val = getattr(old_value, "lobj_FolderMeta86", None)
                if opp_val == self:
                    setattr(old_value, "lobj_FolderMeta86", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lobj_FolderMeta86"):
                opp_val = getattr(value, "lobj_FolderMeta86", None)
                setattr(value, "lobj_FolderMeta86", self)

    @property
    def lobj_ResrcFolder89(self):
        return self.__lobj_ResrcFolder89

    @lobj_ResrcFolder89.setter
    def lobj_ResrcFolder89(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lobj_ResrcFolder__lobj_ResrcFolder89", None)
        self.__lobj_ResrcFolder89 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lobj_ResrcFolder87"):
                opp_val = getattr(old_value, "lobj_ResrcFolder87", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lobj_ResrcFolder87"):
                opp_val = getattr(value, "lobj_ResrcFolder87", None)
                if opp_val is None:
                    setattr(value, "lobj_ResrcFolder87", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def lobj_ResrcFolder94(self):
        return self.__lobj_ResrcFolder94

    @lobj_ResrcFolder94.setter
    def lobj_ResrcFolder94(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lobj_ResrcFolder__lobj_ResrcFolder94", None)
        self.__lobj_ResrcFolder94 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "lobj_ResrcFile"):
                    opp_val = getattr(item, "lobj_ResrcFile", None)
                    
                    if opp_val == self:
                        setattr(item, "lobj_ResrcFile", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "lobj_ResrcFile"):
                    opp_val = getattr(item, "lobj_ResrcFile", None)
                    
                    setattr(item, "lobj_ResrcFile", self)
                    

    @property
    def lobj_ResrcFolder91(self):
        return self.__lobj_ResrcFolder91

    @lobj_ResrcFolder91.setter
    def lobj_ResrcFolder91(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lobj_ResrcFolder__lobj_ResrcFolder91", None)
        self.__lobj_ResrcFolder91 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lobj_AccessControl92"):
                opp_val = getattr(old_value, "lobj_AccessControl92", None)
                if opp_val == self:
                    setattr(old_value, "lobj_AccessControl92", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lobj_AccessControl92"):
                opp_val = getattr(value, "lobj_AccessControl92", None)
                setattr(value, "lobj_AccessControl92", self)

class lobj_Block(LearningObject):

    pass
class lobj_HypertextContent(AbstractContent):

    def __init__(self, content: str, lobj_HypertextContent: "lobj_HypertextBlock" = None, lobj_HypertextContent10: "lobj_BlockAudiofile" = None, hypertextContent: set["lobj_ResrcFile"] = None, HypertextContent: "lobj_ResrcFile" = None):
        self.content = content
        self.lobj_HypertextContent = lobj_HypertextContent
        self.lobj_HypertextContent10 = lobj_HypertextContent10
        self.hypertextContent = hypertextContent if hypertextContent is not None else set()
        self.HypertextContent = HypertextContent
        
    @property
    def content(self) -> str:
        return self.__content

    @content.setter
    def content(self, content: str):
        self.__content = content

    @property
    def lobj_HypertextContent(self):
        return self.__lobj_HypertextContent

    @lobj_HypertextContent.setter
    def lobj_HypertextContent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lobj_HypertextContent__lobj_HypertextContent", None)
        self.__lobj_HypertextContent = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lobj_HypertextBlock"):
                opp_val = getattr(old_value, "lobj_HypertextBlock", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lobj_HypertextBlock"):
                opp_val = getattr(value, "lobj_HypertextBlock", None)
                if opp_val is None:
                    setattr(value, "lobj_HypertextBlock", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def lobj_HypertextContent10(self):
        return self.__lobj_HypertextContent10

    @lobj_HypertextContent10.setter
    def lobj_HypertextContent10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lobj_HypertextContent__lobj_HypertextContent10", None)
        self.__lobj_HypertextContent10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lobj_BlockAudiofile"):
                opp_val = getattr(old_value, "lobj_BlockAudiofile", None)
                if opp_val == self:
                    setattr(old_value, "lobj_BlockAudiofile", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lobj_BlockAudiofile"):
                opp_val = getattr(value, "lobj_BlockAudiofile", None)
                setattr(value, "lobj_BlockAudiofile", self)

    @property
    def hypertextContent(self):
        return self.__hypertextContent

    @hypertextContent.setter
    def hypertextContent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lobj_HypertextContent__hypertextContent", None)
        self.__hypertextContent = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ResrcFile"):
                    opp_val = getattr(item, "ResrcFile", None)
                    
                    if opp_val == self:
                        setattr(item, "ResrcFile", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ResrcFile"):
                    opp_val = getattr(item, "ResrcFile", None)
                    
                    setattr(item, "ResrcFile", self)
                    

    @property
    def HypertextContent(self):
        return self.__HypertextContent

    @HypertextContent.setter
    def HypertextContent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lobj_HypertextContent__HypertextContent", None)
        self.__HypertextContent = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "resrcFile"):
                opp_val = getattr(old_value, "resrcFile", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "resrcFile"):
                opp_val = getattr(value, "resrcFile", None)
                if opp_val is None:
                    setattr(value, "resrcFile", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class lobj_LearningObject(ABC):

    def __init__(self, timestamp: date, synchronized: bool, id: str):
        self.timestamp = timestamp
        self.synchronized = synchronized
        self.id = id
        
    @property
    def synchronized(self) -> bool:
        return self.__synchronized

    @synchronized.setter
    def synchronized(self, synchronized: bool):
        self.__synchronized = synchronized

    @property
    def timestamp(self) -> date:
        return self.__timestamp

    @timestamp.setter
    def timestamp(self, timestamp: date):
        self.__timestamp = timestamp

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id
