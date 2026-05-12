from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class maven_Transform:

    pass
class maven_Mappings:

    pass
class maven_Scope:

    def __init__(self, name: str, exclude: bool, maven_Scope: "maven_Scopes" = None):
        self.name = name
        self.exclude = exclude
        self.maven_Scope = maven_Scope
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def exclude(self):
        return self.__exclude

    @exclude.setter
    def exclude(self, exclude: bool):
        self.__exclude = exclude


    @property
    def maven_Scope(self):
        return self.__maven_Scope

    @maven_Scope.setter
    def maven_Scope(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_maven_Scope__maven_Scope", None)
        self.__maven_Scope = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "maven_Scopes10"):
                opp_val = getattr(old_value, "maven_Scopes10", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "maven_Scopes10"):
                opp_val = getattr(value, "maven_Scopes10", None)
                if opp_val is None:
                    setattr(value, "maven_Scopes10", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class maven_Scopes:

    pass
class Provider:

    pass
class maven_MavenProvider(Provider):

    def __init__(self, transitive: bool, maven_MavenProvider: "maven_Mappings" = None, maven_MavenProvider8: "maven_Scopes" = None):
        self.transitive = transitive
        self.maven_MavenProvider = maven_MavenProvider
        self.maven_MavenProvider8 = maven_MavenProvider8
        
        pass
    @property
    def transitive(self):
        return self.__transitive

    @transitive.setter
    def transitive(self, transitive: bool):
        self.__transitive = transitive


    @property
    def maven_MavenProvider(self):
        return self.__maven_MavenProvider

    @maven_MavenProvider.setter
    def maven_MavenProvider(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_maven_MavenProvider__maven_MavenProvider", None)
        self.__maven_MavenProvider = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "maven_Mappings6"):
                opp_val = getattr(old_value, "maven_Mappings6", None)
                if opp_val == self:
                    setattr(old_value, "maven_Mappings6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "maven_Mappings6"):
                opp_val = getattr(value, "maven_Mappings6", None)
                setattr(value, "maven_Mappings6", self)

    @property
    def maven_MavenProvider8(self):
        return self.__maven_MavenProvider8

    @maven_MavenProvider8.setter
    def maven_MavenProvider8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_maven_MavenProvider__maven_MavenProvider8", None)
        self.__maven_MavenProvider8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "maven_Scopes"):
                opp_val = getattr(old_value, "maven_Scopes", None)
                if opp_val == self:
                    setattr(old_value, "maven_Scopes", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "maven_Scopes"):
                opp_val = getattr(value, "maven_Scopes", None)
                setattr(value, "maven_Scopes", self)

    def getComponentName(self, maven_groupId, maven_artifactId) :
        # TODO: Implement getComponentName method
        pass

    def getMapEntry(self, maven_name) :
        # TODO: Implement getMapEntry method
        pass

class GroupAndArtifact:

    pass
class maven_MapEntry(GroupAndArtifact):

    def __init__(self, name: str, maven_MapEntry: set["maven_GroupAndArtifact"] = None, maven_MapEntry2: "maven_Mappings" = None):
        self.name = name
        self.maven_MapEntry = maven_MapEntry if maven_MapEntry is not None else set()
        self.maven_MapEntry2 = maven_MapEntry2
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def maven_MapEntry2(self):
        return self.__maven_MapEntry2

    @maven_MapEntry2.setter
    def maven_MapEntry2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_maven_MapEntry__maven_MapEntry2", None)
        self.__maven_MapEntry2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "maven_Mappings"):
                opp_val = getattr(old_value, "maven_Mappings", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "maven_Mappings"):
                opp_val = getattr(value, "maven_Mappings", None)
                if opp_val is None:
                    setattr(value, "maven_Mappings", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def maven_MapEntry(self):
        return self.__maven_MapEntry

    @maven_MapEntry.setter
    def maven_MapEntry(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_maven_MapEntry__maven_MapEntry", None)
        self.__maven_MapEntry = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "maven_GroupAndArtifact"):
                    opp_val = getattr(item, "maven_GroupAndArtifact", None)
                    
                    if opp_val == self:
                        setattr(item, "maven_GroupAndArtifact", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "maven_GroupAndArtifact"):
                    opp_val = getattr(item, "maven_GroupAndArtifact", None)
                    
                    setattr(item, "maven_GroupAndArtifact", self)
                    

class maven_GroupAndArtifact:

    def __init__(self, artifactId: str, groupId: str, maven_GroupAndArtifact: "maven_MapEntry" = None):
        self.artifactId = artifactId
        self.groupId = groupId
        self.maven_GroupAndArtifact = maven_GroupAndArtifact
        
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
    def maven_GroupAndArtifact(self):
        return self.__maven_GroupAndArtifact

    @maven_GroupAndArtifact.setter
    def maven_GroupAndArtifact(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_maven_GroupAndArtifact__maven_GroupAndArtifact", None)
        self.__maven_GroupAndArtifact = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "maven_MapEntry"):
                opp_val = getattr(old_value, "maven_MapEntry", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "maven_MapEntry"):
                opp_val = getattr(value, "maven_MapEntry", None)
                if opp_val is None:
                    setattr(value, "maven_MapEntry", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def isMatchFor(self, maven_artifact, maven_group) :
        # TODO: Implement isMatchFor method
        pass
