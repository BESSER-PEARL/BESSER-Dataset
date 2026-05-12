from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class metadata_Versions:

    def __init__(self, version: str, metadata_Versions: "metadata_Versioning" = None):
        self.version = version
        self.metadata_Versions = metadata_Versions
        
        pass
    @property
    def version(self):
        return self.__version

    @version.setter
    def version(self, version: str):
        self.__version = version


    @property
    def metadata_Versions(self):
        return self.__metadata_Versions

    @metadata_Versions.setter
    def metadata_Versions(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metadata_Versions__metadata_Versions", None)
        self.__metadata_Versions = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "metadata_Versioning9"):
                opp_val = getattr(old_value, "metadata_Versioning9", None)
                if opp_val == self:
                    setattr(old_value, "metadata_Versioning9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "metadata_Versioning9"):
                opp_val = getattr(value, "metadata_Versioning9", None)
                setattr(value, "metadata_Versioning9", self)

class metadata_Versioning:

    def __init__(self, release: str, latest: str, lastUpdated: str, metadata_Versioning: "metadata_MetaData" = None, metadata_Versioning9: "metadata_Versions" = None):
        self.release = release
        self.latest = latest
        self.lastUpdated = lastUpdated
        self.metadata_Versioning = metadata_Versioning
        self.metadata_Versioning9 = metadata_Versioning9
        
        pass
    @property
    def lastUpdated(self):
        return self.__lastUpdated

    @lastUpdated.setter
    def lastUpdated(self, lastUpdated: str):
        self.__lastUpdated = lastUpdated


    @property
    def release(self):
        return self.__release

    @release.setter
    def release(self, release: str):
        self.__release = release


    @property
    def latest(self):
        return self.__latest

    @latest.setter
    def latest(self, latest: str):
        self.__latest = latest


    @property
    def metadata_Versioning9(self):
        return self.__metadata_Versioning9

    @metadata_Versioning9.setter
    def metadata_Versioning9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metadata_Versioning__metadata_Versioning9", None)
        self.__metadata_Versioning9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "metadata_Versions"):
                opp_val = getattr(old_value, "metadata_Versions", None)
                if opp_val == self:
                    setattr(old_value, "metadata_Versions", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "metadata_Versions"):
                opp_val = getattr(value, "metadata_Versions", None)
                setattr(value, "metadata_Versions", self)

    @property
    def metadata_Versioning(self):
        return self.__metadata_Versioning

    @metadata_Versioning.setter
    def metadata_Versioning(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metadata_Versioning__metadata_Versioning", None)
        self.__metadata_Versioning = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "metadata_MetaData7"):
                opp_val = getattr(old_value, "metadata_MetaData7", None)
                if opp_val == self:
                    setattr(old_value, "metadata_MetaData7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "metadata_MetaData7"):
                opp_val = getattr(value, "metadata_MetaData7", None)
                setattr(value, "metadata_MetaData7", self)

class metadata_MetaData:

    def __init__(self, groupId: str, artifactId: str, version: str, metadata_MetaData: "metadata_DocumentRoot" = None, metadata_MetaData7: "metadata_Versioning" = None):
        self.groupId = groupId
        self.artifactId = artifactId
        self.version = version
        self.metadata_MetaData = metadata_MetaData
        self.metadata_MetaData7 = metadata_MetaData7
        
        pass
    @property
    def groupId(self):
        return self.__groupId

    @groupId.setter
    def groupId(self, groupId: str):
        self.__groupId = groupId


    @property
    def artifactId(self):
        return self.__artifactId

    @artifactId.setter
    def artifactId(self, artifactId: str):
        self.__artifactId = artifactId


    @property
    def version(self):
        return self.__version

    @version.setter
    def version(self, version: str):
        self.__version = version


    @property
    def metadata_MetaData(self):
        return self.__metadata_MetaData

    @metadata_MetaData.setter
    def metadata_MetaData(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metadata_MetaData__metadata_MetaData", None)
        self.__metadata_MetaData = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "metadata_DocumentRoot5"):
                opp_val = getattr(old_value, "metadata_DocumentRoot5", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "metadata_DocumentRoot5"):
                opp_val = getattr(value, "metadata_DocumentRoot5", None)
                if opp_val is None:
                    setattr(value, "metadata_DocumentRoot5", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def metadata_MetaData7(self):
        return self.__metadata_MetaData7

    @metadata_MetaData7.setter
    def metadata_MetaData7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metadata_MetaData__metadata_MetaData7", None)
        self.__metadata_MetaData7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "metadata_Versioning"):
                opp_val = getattr(old_value, "metadata_Versioning", None)
                if opp_val == self:
                    setattr(old_value, "metadata_Versioning", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "metadata_Versioning"):
                opp_val = getattr(value, "metadata_Versioning", None)
                setattr(value, "metadata_Versioning", self)

class metadata_EStringToStringMapEntry:

    pass
class metadata_DocumentRoot:

    def __init__(self, mixed: str, metadata_DocumentRoot: set["metadata_EStringToStringMapEntry"] = None, metadata_DocumentRoot2: set["metadata_EStringToStringMapEntry"] = None, metadata_DocumentRoot5: set["metadata_MetaData"] = None):
        self.mixed = mixed
        self.metadata_DocumentRoot = metadata_DocumentRoot if metadata_DocumentRoot is not None else set()
        self.metadata_DocumentRoot2 = metadata_DocumentRoot2 if metadata_DocumentRoot2 is not None else set()
        self.metadata_DocumentRoot5 = metadata_DocumentRoot5 if metadata_DocumentRoot5 is not None else set()
        
        pass
    @property
    def mixed(self):
        return self.__mixed

    @mixed.setter
    def mixed(self, mixed: str):
        self.__mixed = mixed


    @property
    def metadata_DocumentRoot5(self):
        return self.__metadata_DocumentRoot5

    @metadata_DocumentRoot5.setter
    def metadata_DocumentRoot5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metadata_DocumentRoot__metadata_DocumentRoot5", None)
        self.__metadata_DocumentRoot5 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "metadata_MetaData"):
                    opp_val = getattr(item, "metadata_MetaData", None)
                    
                    if opp_val == self:
                        setattr(item, "metadata_MetaData", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "metadata_MetaData"):
                    opp_val = getattr(item, "metadata_MetaData", None)
                    
                    setattr(item, "metadata_MetaData", self)
                    

    @property
    def metadata_DocumentRoot(self):
        return self.__metadata_DocumentRoot

    @metadata_DocumentRoot.setter
    def metadata_DocumentRoot(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metadata_DocumentRoot__metadata_DocumentRoot", None)
        self.__metadata_DocumentRoot = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "metadata_EStringToStringMapEntry"):
                    opp_val = getattr(item, "metadata_EStringToStringMapEntry", None)
                    
                    if opp_val == self:
                        setattr(item, "metadata_EStringToStringMapEntry", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "metadata_EStringToStringMapEntry"):
                    opp_val = getattr(item, "metadata_EStringToStringMapEntry", None)
                    
                    setattr(item, "metadata_EStringToStringMapEntry", self)
                    

    @property
    def metadata_DocumentRoot2(self):
        return self.__metadata_DocumentRoot2

    @metadata_DocumentRoot2.setter
    def metadata_DocumentRoot2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metadata_DocumentRoot__metadata_DocumentRoot2", None)
        self.__metadata_DocumentRoot2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "metadata_EStringToStringMapEntry3"):
                    opp_val = getattr(item, "metadata_EStringToStringMapEntry3", None)
                    
                    if opp_val == self:
                        setattr(item, "metadata_EStringToStringMapEntry3", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "metadata_EStringToStringMapEntry3"):
                    opp_val = getattr(item, "metadata_EStringToStringMapEntry3", None)
                    
                    setattr(item, "metadata_EStringToStringMapEntry3", self)
                    
