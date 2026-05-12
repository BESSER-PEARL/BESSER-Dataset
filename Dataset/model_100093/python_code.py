from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class JreType(Enum):
    J2SE14 = "J2SE14"
    J2SE15 = "J2SE15"


############################################
# Definition of Classes
############################################

class pushbuttonbuild_EStringToStringMapEntry:

    pass
class pushbuttonbuild_DocumentRoot:

    def __init__(self, mixed: str, pushbuttonbuild_DocumentRoot: set["pushbuttonbuild_EStringToStringMapEntry"] = None, pushbuttonbuild_DocumentRoot3: set["pushbuttonbuild_EStringToStringMapEntry"] = None, pushbuttonbuild_DocumentRoot6: set["pushbuttonbuild_BuildType"] = None, pushbuttonbuild_DocumentRoot9: set["pushbuttonbuild_ExtraZIPType"] = None):
        self.mixed = mixed
        self.pushbuttonbuild_DocumentRoot = pushbuttonbuild_DocumentRoot if pushbuttonbuild_DocumentRoot is not None else set()
        self.pushbuttonbuild_DocumentRoot3 = pushbuttonbuild_DocumentRoot3 if pushbuttonbuild_DocumentRoot3 is not None else set()
        self.pushbuttonbuild_DocumentRoot6 = pushbuttonbuild_DocumentRoot6 if pushbuttonbuild_DocumentRoot6 is not None else set()
        self.pushbuttonbuild_DocumentRoot9 = pushbuttonbuild_DocumentRoot9 if pushbuttonbuild_DocumentRoot9 is not None else set()
        
        pass
    @property
    def mixed(self):
        return self.__mixed

    @mixed.setter
    def mixed(self, mixed: str):
        self.__mixed = mixed


    @property
    def pushbuttonbuild_DocumentRoot(self):
        return self.__pushbuttonbuild_DocumentRoot

    @pushbuttonbuild_DocumentRoot.setter
    def pushbuttonbuild_DocumentRoot(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pushbuttonbuild_DocumentRoot__pushbuttonbuild_DocumentRoot", None)
        self.__pushbuttonbuild_DocumentRoot = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "pushbuttonbuild_EStringToStringMapEntry"):
                    opp_val = getattr(item, "pushbuttonbuild_EStringToStringMapEntry", None)
                    
                    if opp_val == self:
                        setattr(item, "pushbuttonbuild_EStringToStringMapEntry", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "pushbuttonbuild_EStringToStringMapEntry"):
                    opp_val = getattr(item, "pushbuttonbuild_EStringToStringMapEntry", None)
                    
                    setattr(item, "pushbuttonbuild_EStringToStringMapEntry", self)
                    

    @property
    def pushbuttonbuild_DocumentRoot9(self):
        return self.__pushbuttonbuild_DocumentRoot9

    @pushbuttonbuild_DocumentRoot9.setter
    def pushbuttonbuild_DocumentRoot9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pushbuttonbuild_DocumentRoot__pushbuttonbuild_DocumentRoot9", None)
        self.__pushbuttonbuild_DocumentRoot9 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "pushbuttonbuild_ExtraZIPType10"):
                    opp_val = getattr(item, "pushbuttonbuild_ExtraZIPType10", None)
                    
                    if opp_val == self:
                        setattr(item, "pushbuttonbuild_ExtraZIPType10", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "pushbuttonbuild_ExtraZIPType10"):
                    opp_val = getattr(item, "pushbuttonbuild_ExtraZIPType10", None)
                    
                    setattr(item, "pushbuttonbuild_ExtraZIPType10", self)
                    

    @property
    def pushbuttonbuild_DocumentRoot6(self):
        return self.__pushbuttonbuild_DocumentRoot6

    @pushbuttonbuild_DocumentRoot6.setter
    def pushbuttonbuild_DocumentRoot6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pushbuttonbuild_DocumentRoot__pushbuttonbuild_DocumentRoot6", None)
        self.__pushbuttonbuild_DocumentRoot6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "pushbuttonbuild_BuildType7"):
                    opp_val = getattr(item, "pushbuttonbuild_BuildType7", None)
                    
                    if opp_val == self:
                        setattr(item, "pushbuttonbuild_BuildType7", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "pushbuttonbuild_BuildType7"):
                    opp_val = getattr(item, "pushbuttonbuild_BuildType7", None)
                    
                    setattr(item, "pushbuttonbuild_BuildType7", self)
                    

    @property
    def pushbuttonbuild_DocumentRoot3(self):
        return self.__pushbuttonbuild_DocumentRoot3

    @pushbuttonbuild_DocumentRoot3.setter
    def pushbuttonbuild_DocumentRoot3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pushbuttonbuild_DocumentRoot__pushbuttonbuild_DocumentRoot3", None)
        self.__pushbuttonbuild_DocumentRoot3 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "pushbuttonbuild_EStringToStringMapEntry4"):
                    opp_val = getattr(item, "pushbuttonbuild_EStringToStringMapEntry4", None)
                    
                    if opp_val == self:
                        setattr(item, "pushbuttonbuild_EStringToStringMapEntry4", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "pushbuttonbuild_EStringToStringMapEntry4"):
                    opp_val = getattr(item, "pushbuttonbuild_EStringToStringMapEntry4", None)
                    
                    setattr(item, "pushbuttonbuild_EStringToStringMapEntry4", self)
                    

class pushbuttonbuild_ExtraZIPType:

    def __init__(self, name: str, pushbuttonbuild_ExtraZIPType: "pushbuttonbuild_BuildType" = None, pushbuttonbuild_ExtraZIPType10: "pushbuttonbuild_DocumentRoot" = None):
        self.name = name
        self.pushbuttonbuild_ExtraZIPType = pushbuttonbuild_ExtraZIPType
        self.pushbuttonbuild_ExtraZIPType10 = pushbuttonbuild_ExtraZIPType10
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def pushbuttonbuild_ExtraZIPType(self):
        return self.__pushbuttonbuild_ExtraZIPType

    @pushbuttonbuild_ExtraZIPType.setter
    def pushbuttonbuild_ExtraZIPType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pushbuttonbuild_ExtraZIPType__pushbuttonbuild_ExtraZIPType", None)
        self.__pushbuttonbuild_ExtraZIPType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pushbuttonbuild_BuildType"):
                opp_val = getattr(old_value, "pushbuttonbuild_BuildType", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pushbuttonbuild_BuildType"):
                opp_val = getattr(value, "pushbuttonbuild_BuildType", None)
                if opp_val is None:
                    setattr(value, "pushbuttonbuild_BuildType", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def pushbuttonbuild_ExtraZIPType10(self):
        return self.__pushbuttonbuild_ExtraZIPType10

    @pushbuttonbuild_ExtraZIPType10.setter
    def pushbuttonbuild_ExtraZIPType10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pushbuttonbuild_ExtraZIPType__pushbuttonbuild_ExtraZIPType10", None)
        self.__pushbuttonbuild_ExtraZIPType10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pushbuttonbuild_DocumentRoot9"):
                opp_val = getattr(old_value, "pushbuttonbuild_DocumentRoot9", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pushbuttonbuild_DocumentRoot9"):
                opp_val = getattr(value, "pushbuttonbuild_DocumentRoot9", None)
                if opp_val is None:
                    setattr(value, "pushbuttonbuild_DocumentRoot9", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class pushbuttonbuild_BuildType:

    def __init__(self, isIncubation: str, jre: str, newsgroupPublisherName: str, newsgroupPublisherEmail: str, parentProjectName: str, projectNamespace: str, shortName: str, testsAreJarred: str, pushbuttonbuild_BuildType: set["pushbuttonbuild_ExtraZIPType"] = None, pushbuttonbuild_BuildType7: "pushbuttonbuild_DocumentRoot" = None):
        self.isIncubation = isIncubation
        self.jre = jre
        self.newsgroupPublisherName = newsgroupPublisherName
        self.newsgroupPublisherEmail = newsgroupPublisherEmail
        self.parentProjectName = parentProjectName
        self.projectNamespace = projectNamespace
        self.shortName = shortName
        self.testsAreJarred = testsAreJarred
        self.pushbuttonbuild_BuildType = pushbuttonbuild_BuildType if pushbuttonbuild_BuildType is not None else set()
        self.pushbuttonbuild_BuildType7 = pushbuttonbuild_BuildType7
        
        pass
    @property
    def testsAreJarred(self):
        return self.__testsAreJarred

    @testsAreJarred.setter
    def testsAreJarred(self, testsAreJarred: str):
        self.__testsAreJarred = testsAreJarred


    @property
    def jre(self):
        return self.__jre

    @jre.setter
    def jre(self, jre: str):
        self.__jre = jre


    @property
    def newsgroupPublisherName(self):
        return self.__newsgroupPublisherName

    @newsgroupPublisherName.setter
    def newsgroupPublisherName(self, newsgroupPublisherName: str):
        self.__newsgroupPublisherName = newsgroupPublisherName


    @property
    def isIncubation(self):
        return self.__isIncubation

    @isIncubation.setter
    def isIncubation(self, isIncubation: str):
        self.__isIncubation = isIncubation


    @property
    def parentProjectName(self):
        return self.__parentProjectName

    @parentProjectName.setter
    def parentProjectName(self, parentProjectName: str):
        self.__parentProjectName = parentProjectName


    @property
    def newsgroupPublisherEmail(self):
        return self.__newsgroupPublisherEmail

    @newsgroupPublisherEmail.setter
    def newsgroupPublisherEmail(self, newsgroupPublisherEmail: str):
        self.__newsgroupPublisherEmail = newsgroupPublisherEmail


    @property
    def shortName(self):
        return self.__shortName

    @shortName.setter
    def shortName(self, shortName: str):
        self.__shortName = shortName


    @property
    def projectNamespace(self):
        return self.__projectNamespace

    @projectNamespace.setter
    def projectNamespace(self, projectNamespace: str):
        self.__projectNamespace = projectNamespace


    @property
    def pushbuttonbuild_BuildType7(self):
        return self.__pushbuttonbuild_BuildType7

    @pushbuttonbuild_BuildType7.setter
    def pushbuttonbuild_BuildType7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pushbuttonbuild_BuildType__pushbuttonbuild_BuildType7", None)
        self.__pushbuttonbuild_BuildType7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pushbuttonbuild_DocumentRoot6"):
                opp_val = getattr(old_value, "pushbuttonbuild_DocumentRoot6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pushbuttonbuild_DocumentRoot6"):
                opp_val = getattr(value, "pushbuttonbuild_DocumentRoot6", None)
                if opp_val is None:
                    setattr(value, "pushbuttonbuild_DocumentRoot6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def pushbuttonbuild_BuildType(self):
        return self.__pushbuttonbuild_BuildType

    @pushbuttonbuild_BuildType.setter
    def pushbuttonbuild_BuildType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pushbuttonbuild_BuildType__pushbuttonbuild_BuildType", None)
        self.__pushbuttonbuild_BuildType = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "pushbuttonbuild_ExtraZIPType"):
                    opp_val = getattr(item, "pushbuttonbuild_ExtraZIPType", None)
                    
                    if opp_val == self:
                        setattr(item, "pushbuttonbuild_ExtraZIPType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "pushbuttonbuild_ExtraZIPType"):
                    opp_val = getattr(item, "pushbuttonbuild_ExtraZIPType", None)
                    
                    setattr(item, "pushbuttonbuild_ExtraZIPType", self)
                    
