from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class CodeTagType(Enum):
    CLASSPUBLICMETHODSSECTIONDECLARE = "CLASSPUBLICMETHODSSECTIONDECLARE"
    CLASSPUBLICMETHODSSECTIONIMPL = "CLASSPUBLICMETHODSSECTIONIMPL"
    CLASSPRIVATEMETHODSSECTIONDECLARE = "CLASSPRIVATEMETHODSSECTIONDECLARE"
    CLASSPRIVATEMETHODSSECTIONIMPL = "CLASSPRIVATEMETHODSSECTIONIMPL"
    FILEHEADERH = "FILEHEADERH"
    FILEHEADERCPP = "FILEHEADERCPP"
    FILEFOOTERH = "FILEFOOTERH"
    FILEFOOTERCPP = "FILEFOOTERCPP"
    FILEINCLUDESH = "FILEINCLUDESH"
    FILEINCLUDESCPP = "FILEINCLUDESCPP"
    CONSTRUCTORINITLIST = "CONSTRUCTORINITLIST"
    CLASSGENERATEDOPERATIONIMPL = "CLASSGENERATEDOPERATIONIMPL"
    CLASSGENERATEDATTRIBUTEGET = "CLASSGENERATEDATTRIBUTEGET"
    CLASSGENERATEDATTRIBUTESET = "CLASSGENERATEDATTRIBUTESET"
    CLASSPRIVATEMEMBERSSECTIONDECLARE = "CLASSPRIVATEMEMBERSSECTIONDECLARE"


############################################
# Definition of Classes
############################################

class codetaginfo_EStringToStringMapEntry:

    pass
class codetaginfo_DocumentRoot:

    def __init__(self, mixed: str, codetaginfo_DocumentRoot: set["codetaginfo_EStringToStringMapEntry"] = None, codetaginfo_DocumentRoot5: set["codetaginfo_EStringToStringMapEntry"] = None, codetaginfo_DocumentRoot8: set["codetaginfo_CodeTagInfo"] = None):
        self.mixed = mixed
        self.codetaginfo_DocumentRoot = codetaginfo_DocumentRoot if codetaginfo_DocumentRoot is not None else set()
        self.codetaginfo_DocumentRoot5 = codetaginfo_DocumentRoot5 if codetaginfo_DocumentRoot5 is not None else set()
        self.codetaginfo_DocumentRoot8 = codetaginfo_DocumentRoot8 if codetaginfo_DocumentRoot8 is not None else set()
        
    @property
    def mixed(self) -> str:
        return self.__mixed

    @mixed.setter
    def mixed(self, mixed: str):
        self.__mixed = mixed

    @property
    def codetaginfo_DocumentRoot5(self):
        return self.__codetaginfo_DocumentRoot5

    @codetaginfo_DocumentRoot5.setter
    def codetaginfo_DocumentRoot5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_codetaginfo_DocumentRoot__codetaginfo_DocumentRoot5", None)
        self.__codetaginfo_DocumentRoot5 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "codetaginfo_EStringToStringMapEntry6"):
                    opp_val = getattr(item, "codetaginfo_EStringToStringMapEntry6", None)
                    
                    if opp_val == self:
                        setattr(item, "codetaginfo_EStringToStringMapEntry6", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "codetaginfo_EStringToStringMapEntry6"):
                    opp_val = getattr(item, "codetaginfo_EStringToStringMapEntry6", None)
                    
                    setattr(item, "codetaginfo_EStringToStringMapEntry6", self)
                    

    @property
    def codetaginfo_DocumentRoot8(self):
        return self.__codetaginfo_DocumentRoot8

    @codetaginfo_DocumentRoot8.setter
    def codetaginfo_DocumentRoot8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_codetaginfo_DocumentRoot__codetaginfo_DocumentRoot8", None)
        self.__codetaginfo_DocumentRoot8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "codetaginfo_CodeTagInfo9"):
                    opp_val = getattr(item, "codetaginfo_CodeTagInfo9", None)
                    
                    if opp_val == self:
                        setattr(item, "codetaginfo_CodeTagInfo9", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "codetaginfo_CodeTagInfo9"):
                    opp_val = getattr(item, "codetaginfo_CodeTagInfo9", None)
                    
                    setattr(item, "codetaginfo_CodeTagInfo9", self)
                    

    @property
    def codetaginfo_DocumentRoot(self):
        return self.__codetaginfo_DocumentRoot

    @codetaginfo_DocumentRoot.setter
    def codetaginfo_DocumentRoot(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_codetaginfo_DocumentRoot__codetaginfo_DocumentRoot", None)
        self.__codetaginfo_DocumentRoot = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "codetaginfo_EStringToStringMapEntry"):
                    opp_val = getattr(item, "codetaginfo_EStringToStringMapEntry", None)
                    
                    if opp_val == self:
                        setattr(item, "codetaginfo_EStringToStringMapEntry", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "codetaginfo_EStringToStringMapEntry"):
                    opp_val = getattr(item, "codetaginfo_EStringToStringMapEntry", None)
                    
                    setattr(item, "codetaginfo_EStringToStringMapEntry", self)
                    

class codetaginfo_CodeTagInfo:

    def __init__(self, group: str, filename: str, codetaginfo_CodeTagInfo: set["codetaginfo_CodeTag"] = None, codetaginfo_CodeTagInfo9: "codetaginfo_DocumentRoot" = None):
        self.group = group
        self.filename = filename
        self.codetaginfo_CodeTagInfo = codetaginfo_CodeTagInfo if codetaginfo_CodeTagInfo is not None else set()
        self.codetaginfo_CodeTagInfo9 = codetaginfo_CodeTagInfo9
        
    @property
    def group(self) -> str:
        return self.__group

    @group.setter
    def group(self, group: str):
        self.__group = group

    @property
    def filename(self) -> str:
        return self.__filename

    @filename.setter
    def filename(self, filename: str):
        self.__filename = filename

    @property
    def codetaginfo_CodeTagInfo(self):
        return self.__codetaginfo_CodeTagInfo

    @codetaginfo_CodeTagInfo.setter
    def codetaginfo_CodeTagInfo(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_codetaginfo_CodeTagInfo__codetaginfo_CodeTagInfo", None)
        self.__codetaginfo_CodeTagInfo = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "codetaginfo_CodeTag2"):
                    opp_val = getattr(item, "codetaginfo_CodeTag2", None)
                    
                    if opp_val == self:
                        setattr(item, "codetaginfo_CodeTag2", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "codetaginfo_CodeTag2"):
                    opp_val = getattr(item, "codetaginfo_CodeTag2", None)
                    
                    setattr(item, "codetaginfo_CodeTag2", self)
                    

    @property
    def codetaginfo_CodeTagInfo9(self):
        return self.__codetaginfo_CodeTagInfo9

    @codetaginfo_CodeTagInfo9.setter
    def codetaginfo_CodeTagInfo9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_codetaginfo_CodeTagInfo__codetaginfo_CodeTagInfo9", None)
        self.__codetaginfo_CodeTagInfo9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "codetaginfo_DocumentRoot8"):
                opp_val = getattr(old_value, "codetaginfo_DocumentRoot8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "codetaginfo_DocumentRoot8"):
                opp_val = getattr(value, "codetaginfo_DocumentRoot8", None)
                if opp_val is None:
                    setattr(value, "codetaginfo_DocumentRoot8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class codetaginfo_CodeTagContext:

    def __init__(self, group: str, component_name: str, class_name: str, operation_name: str, codetaginfo_CodeTagContext: "codetaginfo_CodeTag" = None):
        self.group = group
        self.component_name = component_name
        self.class_name = class_name
        self.operation_name = operation_name
        self.codetaginfo_CodeTagContext = codetaginfo_CodeTagContext
        
    @property
    def component_name(self) -> str:
        return self.__component_name

    @component_name.setter
    def component_name(self, component_name: str):
        self.__component_name = component_name

    @property
    def group(self) -> str:
        return self.__group

    @group.setter
    def group(self, group: str):
        self.__group = group

    @property
    def operation_name(self) -> str:
        return self.__operation_name

    @operation_name.setter
    def operation_name(self, operation_name: str):
        self.__operation_name = operation_name

    @property
    def class_name(self) -> str:
        return self.__class_name

    @class_name.setter
    def class_name(self, class_name: str):
        self.__class_name = class_name

    @property
    def codetaginfo_CodeTagContext(self):
        return self.__codetaginfo_CodeTagContext

    @codetaginfo_CodeTagContext.setter
    def codetaginfo_CodeTagContext(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_codetaginfo_CodeTagContext__codetaginfo_CodeTagContext", None)
        self.__codetaginfo_CodeTagContext = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "codetaginfo_CodeTag"):
                opp_val = getattr(old_value, "codetaginfo_CodeTag", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "codetaginfo_CodeTag"):
                opp_val = getattr(value, "codetaginfo_CodeTag", None)
                if opp_val is None:
                    setattr(value, "codetaginfo_CodeTag", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class codetaginfo_CodeTag:

    def __init__(self, name: str, uuid: str, type: str, tag_begin: str, group: str, contents: str, tag_end: str, codetaginfo_CodeTag: set["codetaginfo_CodeTagContext"] = None, codetaginfo_CodeTag2: "codetaginfo_CodeTagInfo" = None):
        self.name = name
        self.uuid = uuid
        self.type = type
        self.tag_begin = tag_begin
        self.group = group
        self.contents = contents
        self.tag_end = tag_end
        self.codetaginfo_CodeTag = codetaginfo_CodeTag if codetaginfo_CodeTag is not None else set()
        self.codetaginfo_CodeTag2 = codetaginfo_CodeTag2
        
    @property
    def tag_end(self) -> str:
        return self.__tag_end

    @tag_end.setter
    def tag_end(self, tag_end: str):
        self.__tag_end = tag_end

    @property
    def contents(self) -> str:
        return self.__contents

    @contents.setter
    def contents(self, contents: str):
        self.__contents = contents

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def uuid(self) -> str:
        return self.__uuid

    @uuid.setter
    def uuid(self, uuid: str):
        self.__uuid = uuid

    @property
    def group(self) -> str:
        return self.__group

    @group.setter
    def group(self, group: str):
        self.__group = group

    @property
    def tag_begin(self) -> str:
        return self.__tag_begin

    @tag_begin.setter
    def tag_begin(self, tag_begin: str):
        self.__tag_begin = tag_begin

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def codetaginfo_CodeTag(self):
        return self.__codetaginfo_CodeTag

    @codetaginfo_CodeTag.setter
    def codetaginfo_CodeTag(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_codetaginfo_CodeTag__codetaginfo_CodeTag", None)
        self.__codetaginfo_CodeTag = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "codetaginfo_CodeTagContext"):
                    opp_val = getattr(item, "codetaginfo_CodeTagContext", None)
                    
                    if opp_val == self:
                        setattr(item, "codetaginfo_CodeTagContext", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "codetaginfo_CodeTagContext"):
                    opp_val = getattr(item, "codetaginfo_CodeTagContext", None)
                    
                    setattr(item, "codetaginfo_CodeTagContext", self)
                    

    @property
    def codetaginfo_CodeTag2(self):
        return self.__codetaginfo_CodeTag2

    @codetaginfo_CodeTag2.setter
    def codetaginfo_CodeTag2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_codetaginfo_CodeTag__codetaginfo_CodeTag2", None)
        self.__codetaginfo_CodeTag2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "codetaginfo_CodeTagInfo"):
                opp_val = getattr(old_value, "codetaginfo_CodeTagInfo", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "codetaginfo_CodeTagInfo"):
                opp_val = getattr(value, "codetaginfo_CodeTagInfo", None)
                if opp_val is None:
                    setattr(value, "codetaginfo_CodeTagInfo", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
