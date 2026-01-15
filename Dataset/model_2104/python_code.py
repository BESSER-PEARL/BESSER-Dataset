from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class TreeNodeType(Enum):
    FOLDER = "FOLDER"
    FILE = "FILE"
    PROJECT = "PROJECT"
    UNKNOWN = "UNKNOWN"


############################################
# Definition of Classes
############################################

class ResourceTreeNode:

    pass
class SemanticResourceDB_TreeRoot(ResourceTreeNode):

    def __init__(self, rootURI: str, TreeRoot: "SemanticResourceDB_SemanticDB" = None, roots: "SemanticResourceDB_SemanticDB" = None):
        self.rootURI = rootURI
        self.TreeRoot = TreeRoot
        self.roots = roots
        
    @property
    def rootURI(self) -> str:
        return self.__rootURI

    @rootURI.setter
    def rootURI(self, rootURI: str):
        self.__rootURI = rootURI

    @property
    def TreeRoot(self):
        return self.__TreeRoot

    @TreeRoot.setter
    def TreeRoot(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SemanticResourceDB_TreeRoot__TreeRoot", None)
        self.__TreeRoot = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "parentDB"):
                opp_val = getattr(old_value, "parentDB", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "parentDB"):
                opp_val = getattr(value, "parentDB", None)
                if opp_val is None:
                    setattr(value, "parentDB", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def roots(self):
        return self.__roots

    @roots.setter
    def roots(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SemanticResourceDB_TreeRoot__roots", None)
        self.__roots = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SemanticDB"):
                opp_val = getattr(old_value, "SemanticDB", None)
                if opp_val == self:
                    setattr(old_value, "SemanticDB", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SemanticDB"):
                opp_val = getattr(value, "SemanticDB", None)
                setattr(value, "SemanticDB", self)

class SemanticResourceDB_SemanticDB:

    pass
class SemanticResourceDB_ResourceTreeNode:

    def __init__(self, name: str, exists: bool, templateID: str, persistentProperties: str, dynamicContentProviderID: str, localOnly: bool, type: str, sessionProperties: str, path: str, queryPart: str, remoteURI: str, ResourceTreeNode: "SemanticResourceDB_ResourceTreeNode" = None, parent: set["SemanticResourceDB_ResourceTreeNode"] = None, ResourceTreeNode4: "SemanticResourceDB_ResourceTreeNode" = None, children: "SemanticResourceDB_ResourceTreeNode" = None):
        self.name = name
        self.exists = exists
        self.templateID = templateID
        self.persistentProperties = persistentProperties
        self.dynamicContentProviderID = dynamicContentProviderID
        self.localOnly = localOnly
        self.type = type
        self.sessionProperties = sessionProperties
        self.path = path
        self.queryPart = queryPart
        self.remoteURI = remoteURI
        self.ResourceTreeNode = ResourceTreeNode
        self.parent = parent if parent is not None else set()
        self.ResourceTreeNode4 = ResourceTreeNode4
        self.children = children
        
    @property
    def sessionProperties(self) -> str:
        return self.__sessionProperties

    @sessionProperties.setter
    def sessionProperties(self, sessionProperties: str):
        self.__sessionProperties = sessionProperties

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def templateID(self) -> str:
        return self.__templateID

    @templateID.setter
    def templateID(self, templateID: str):
        self.__templateID = templateID

    @property
    def queryPart(self) -> str:
        return self.__queryPart

    @queryPart.setter
    def queryPart(self, queryPart: str):
        self.__queryPart = queryPart

    @property
    def dynamicContentProviderID(self) -> str:
        return self.__dynamicContentProviderID

    @dynamicContentProviderID.setter
    def dynamicContentProviderID(self, dynamicContentProviderID: str):
        self.__dynamicContentProviderID = dynamicContentProviderID

    @property
    def remoteURI(self) -> str:
        return self.__remoteURI

    @remoteURI.setter
    def remoteURI(self, remoteURI: str):
        self.__remoteURI = remoteURI

    @property
    def localOnly(self) -> bool:
        return self.__localOnly

    @localOnly.setter
    def localOnly(self, localOnly: bool):
        self.__localOnly = localOnly

    @property
    def exists(self) -> bool:
        return self.__exists

    @exists.setter
    def exists(self, exists: bool):
        self.__exists = exists

    @property
    def persistentProperties(self) -> str:
        return self.__persistentProperties

    @persistentProperties.setter
    def persistentProperties(self, persistentProperties: str):
        self.__persistentProperties = persistentProperties

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def path(self) -> str:
        return self.__path

    @path.setter
    def path(self, path: str):
        self.__path = path

    @property
    def ResourceTreeNode(self):
        return self.__ResourceTreeNode

    @ResourceTreeNode.setter
    def ResourceTreeNode(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SemanticResourceDB_ResourceTreeNode__ResourceTreeNode", None)
        self.__ResourceTreeNode = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "parent"):
                opp_val = getattr(old_value, "parent", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "parent"):
                opp_val = getattr(value, "parent", None)
                if opp_val is None:
                    setattr(value, "parent", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ResourceTreeNode4(self):
        return self.__ResourceTreeNode4

    @ResourceTreeNode4.setter
    def ResourceTreeNode4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SemanticResourceDB_ResourceTreeNode__ResourceTreeNode4", None)
        self.__ResourceTreeNode4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "children"):
                opp_val = getattr(old_value, "children", None)
                if opp_val == self:
                    setattr(old_value, "children", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "children"):
                opp_val = getattr(value, "children", None)
                setattr(value, "children", self)

    @property
    def parent(self):
        return self.__parent

    @parent.setter
    def parent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SemanticResourceDB_ResourceTreeNode__parent", None)
        self.__parent = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ResourceTreeNode"):
                    opp_val = getattr(item, "ResourceTreeNode", None)
                    
                    if opp_val == self:
                        setattr(item, "ResourceTreeNode", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ResourceTreeNode"):
                    opp_val = getattr(item, "ResourceTreeNode", None)
                    
                    setattr(item, "ResourceTreeNode", self)
                    

    @property
    def children(self):
        return self.__children

    @children.setter
    def children(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SemanticResourceDB_ResourceTreeNode__children", None)
        self.__children = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ResourceTreeNode4"):
                opp_val = getattr(old_value, "ResourceTreeNode4", None)
                if opp_val == self:
                    setattr(old_value, "ResourceTreeNode4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ResourceTreeNode4"):
                opp_val = getattr(value, "ResourceTreeNode4", None)
                setattr(value, "ResourceTreeNode4", self)
