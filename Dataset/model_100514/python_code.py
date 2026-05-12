from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class RequirementSourceConf_Scope:

    pass
class RequirementSourceConf_MappingElement:

    pass
class RequirementSourceConf_EStringToStringMapEntry:

    pass
class RequirementSourceConf_RequirementSource:

    def __init__(self, name: str, connectorId: str, dataModelURI: str, repositoryURI: str, destinationURI: str, RequirementSourceConf_RequirementSource: "RequirementSourceConf_RequirementSources" = None, RequirementSourceConf_RequirementSource2: "RequirementSourceConf_RequirementsContainer" = None, RequirementSourceConf_RequirementSource4: set["RequirementSourceConf_EStringToStringMapEntry"] = None, RequirementSourceConf_RequirementSource6: set["RequirementSourceConf_MappingElement"] = None, RequirementSourceConf_RequirementSource8: "RequirementSourceConf_Scope" = None):
        self.name = name
        self.connectorId = connectorId
        self.dataModelURI = dataModelURI
        self.repositoryURI = repositoryURI
        self.destinationURI = destinationURI
        self.RequirementSourceConf_RequirementSource = RequirementSourceConf_RequirementSource
        self.RequirementSourceConf_RequirementSource2 = RequirementSourceConf_RequirementSource2
        self.RequirementSourceConf_RequirementSource4 = RequirementSourceConf_RequirementSource4 if RequirementSourceConf_RequirementSource4 is not None else set()
        self.RequirementSourceConf_RequirementSource6 = RequirementSourceConf_RequirementSource6 if RequirementSourceConf_RequirementSource6 is not None else set()
        self.RequirementSourceConf_RequirementSource8 = RequirementSourceConf_RequirementSource8
        
        pass
    @property
    def connectorId(self):
        return self.__connectorId

    @connectorId.setter
    def connectorId(self, connectorId: str):
        self.__connectorId = connectorId


    @property
    def destinationURI(self):
        return self.__destinationURI

    @destinationURI.setter
    def destinationURI(self, destinationURI: str):
        self.__destinationURI = destinationURI


    @property
    def dataModelURI(self):
        return self.__dataModelURI

    @dataModelURI.setter
    def dataModelURI(self, dataModelURI: str):
        self.__dataModelURI = dataModelURI


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def repositoryURI(self):
        return self.__repositoryURI

    @repositoryURI.setter
    def repositoryURI(self, repositoryURI: str):
        self.__repositoryURI = repositoryURI


    @property
    def RequirementSourceConf_RequirementSource2(self):
        return self.__RequirementSourceConf_RequirementSource2

    @RequirementSourceConf_RequirementSource2.setter
    def RequirementSourceConf_RequirementSource2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RequirementSourceConf_RequirementSource__RequirementSourceConf_RequirementSource2", None)
        self.__RequirementSourceConf_RequirementSource2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RequirementSourceConf_RequirementsContainer"):
                opp_val = getattr(old_value, "RequirementSourceConf_RequirementsContainer", None)
                if opp_val == self:
                    setattr(old_value, "RequirementSourceConf_RequirementsContainer", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RequirementSourceConf_RequirementsContainer"):
                opp_val = getattr(value, "RequirementSourceConf_RequirementsContainer", None)
                setattr(value, "RequirementSourceConf_RequirementsContainer", self)

    @property
    def RequirementSourceConf_RequirementSource4(self):
        return self.__RequirementSourceConf_RequirementSource4

    @RequirementSourceConf_RequirementSource4.setter
    def RequirementSourceConf_RequirementSource4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RequirementSourceConf_RequirementSource__RequirementSourceConf_RequirementSource4", None)
        self.__RequirementSourceConf_RequirementSource4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "RequirementSourceConf_EStringToStringMapEntry"):
                    opp_val = getattr(item, "RequirementSourceConf_EStringToStringMapEntry", None)
                    
                    if opp_val == self:
                        setattr(item, "RequirementSourceConf_EStringToStringMapEntry", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "RequirementSourceConf_EStringToStringMapEntry"):
                    opp_val = getattr(item, "RequirementSourceConf_EStringToStringMapEntry", None)
                    
                    setattr(item, "RequirementSourceConf_EStringToStringMapEntry", self)
                    

    @property
    def RequirementSourceConf_RequirementSource8(self):
        return self.__RequirementSourceConf_RequirementSource8

    @RequirementSourceConf_RequirementSource8.setter
    def RequirementSourceConf_RequirementSource8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RequirementSourceConf_RequirementSource__RequirementSourceConf_RequirementSource8", None)
        self.__RequirementSourceConf_RequirementSource8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RequirementSourceConf_Scope"):
                opp_val = getattr(old_value, "RequirementSourceConf_Scope", None)
                if opp_val == self:
                    setattr(old_value, "RequirementSourceConf_Scope", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RequirementSourceConf_Scope"):
                opp_val = getattr(value, "RequirementSourceConf_Scope", None)
                setattr(value, "RequirementSourceConf_Scope", self)

    @property
    def RequirementSourceConf_RequirementSource(self):
        return self.__RequirementSourceConf_RequirementSource

    @RequirementSourceConf_RequirementSource.setter
    def RequirementSourceConf_RequirementSource(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RequirementSourceConf_RequirementSource__RequirementSourceConf_RequirementSource", None)
        self.__RequirementSourceConf_RequirementSource = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RequirementSourceConf_RequirementSources"):
                opp_val = getattr(old_value, "RequirementSourceConf_RequirementSources", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RequirementSourceConf_RequirementSources"):
                opp_val = getattr(value, "RequirementSourceConf_RequirementSources", None)
                if opp_val is None:
                    setattr(value, "RequirementSourceConf_RequirementSources", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def RequirementSourceConf_RequirementSource6(self):
        return self.__RequirementSourceConf_RequirementSource6

    @RequirementSourceConf_RequirementSource6.setter
    def RequirementSourceConf_RequirementSource6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RequirementSourceConf_RequirementSource__RequirementSourceConf_RequirementSource6", None)
        self.__RequirementSourceConf_RequirementSource6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "RequirementSourceConf_MappingElement"):
                    opp_val = getattr(item, "RequirementSourceConf_MappingElement", None)
                    
                    if opp_val == self:
                        setattr(item, "RequirementSourceConf_MappingElement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "RequirementSourceConf_MappingElement"):
                    opp_val = getattr(item, "RequirementSourceConf_MappingElement", None)
                    
                    setattr(item, "RequirementSourceConf_MappingElement", self)
                    

class RequirementSourceConf_RequirementSources:

    pass
class RequirementSourceConf_RequirementsContainer:

    pass