from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class SpaceType(Enum):
    default = "default"
    preserve = "preserve"


############################################
# Definition of Classes
############################################

class namespace_EStringToStringMapEntry:

    pass
class namespace_XMLNamespaceDocumentRoot:

    def __init__(self, base: str, id: str, lang: str, space: str, mixed: str, namespace_XMLNamespaceDocumentRoot: set["namespace_EStringToStringMapEntry"] = None, namespace_XMLNamespaceDocumentRoot2: set["namespace_EStringToStringMapEntry"] = None):
        self.base = base
        self.id = id
        self.lang = lang
        self.space = space
        self.mixed = mixed
        self.namespace_XMLNamespaceDocumentRoot = namespace_XMLNamespaceDocumentRoot if namespace_XMLNamespaceDocumentRoot is not None else set()
        self.namespace_XMLNamespaceDocumentRoot2 = namespace_XMLNamespaceDocumentRoot2 if namespace_XMLNamespaceDocumentRoot2 is not None else set()
        
        pass
    @property
    def space(self):
        return self.__space

    @space.setter
    def space(self, space: str):
        self.__space = space


    @property
    def lang(self):
        return self.__lang

    @lang.setter
    def lang(self, lang: str):
        self.__lang = lang


    @property
    def base(self):
        return self.__base

    @base.setter
    def base(self, base: str):
        self.__base = base


    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id


    @property
    def mixed(self):
        return self.__mixed

    @mixed.setter
    def mixed(self, mixed: str):
        self.__mixed = mixed


    @property
    def namespace_XMLNamespaceDocumentRoot(self):
        return self.__namespace_XMLNamespaceDocumentRoot

    @namespace_XMLNamespaceDocumentRoot.setter
    def namespace_XMLNamespaceDocumentRoot(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_namespace_XMLNamespaceDocumentRoot__namespace_XMLNamespaceDocumentRoot", None)
        self.__namespace_XMLNamespaceDocumentRoot = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "namespace_EStringToStringMapEntry"):
                    opp_val = getattr(item, "namespace_EStringToStringMapEntry", None)
                    
                    if opp_val == self:
                        setattr(item, "namespace_EStringToStringMapEntry", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "namespace_EStringToStringMapEntry"):
                    opp_val = getattr(item, "namespace_EStringToStringMapEntry", None)
                    
                    setattr(item, "namespace_EStringToStringMapEntry", self)
                    

    @property
    def namespace_XMLNamespaceDocumentRoot2(self):
        return self.__namespace_XMLNamespaceDocumentRoot2

    @namespace_XMLNamespaceDocumentRoot2.setter
    def namespace_XMLNamespaceDocumentRoot2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_namespace_XMLNamespaceDocumentRoot__namespace_XMLNamespaceDocumentRoot2", None)
        self.__namespace_XMLNamespaceDocumentRoot2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "namespace_EStringToStringMapEntry3"):
                    opp_val = getattr(item, "namespace_EStringToStringMapEntry3", None)
                    
                    if opp_val == self:
                        setattr(item, "namespace_EStringToStringMapEntry3", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "namespace_EStringToStringMapEntry3"):
                    opp_val = getattr(item, "namespace_EStringToStringMapEntry3", None)
                    
                    setattr(item, "namespace_EStringToStringMapEntry3", self)
                    
