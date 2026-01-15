from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class graph_EnvironmentGraph:

    pass
class graph_EStringToStringMapEntry:

    pass
class graph_DocumentRoot:

    def __init__(self, mixed: str, graph_DocumentRoot: set["graph_EStringToStringMapEntry"] = None, graph_DocumentRoot11: set["graph_Cause"] = None, graph_DocumentRoot14: set["graph_Dependency"] = None, graph_DocumentRoot17: set["graph_EnvironmentGraph"] = None, graph_DocumentRoot8: set["graph_EStringToStringMapEntry"] = None, graph_DocumentRoot19: set["graph_Node"] = None):
        self.mixed = mixed
        self.graph_DocumentRoot = graph_DocumentRoot if graph_DocumentRoot is not None else set()
        self.graph_DocumentRoot11 = graph_DocumentRoot11 if graph_DocumentRoot11 is not None else set()
        self.graph_DocumentRoot14 = graph_DocumentRoot14 if graph_DocumentRoot14 is not None else set()
        self.graph_DocumentRoot17 = graph_DocumentRoot17 if graph_DocumentRoot17 is not None else set()
        self.graph_DocumentRoot8 = graph_DocumentRoot8 if graph_DocumentRoot8 is not None else set()
        self.graph_DocumentRoot19 = graph_DocumentRoot19 if graph_DocumentRoot19 is not None else set()
        
    @property
    def mixed(self) -> str:
        return self.__mixed

    @mixed.setter
    def mixed(self, mixed: str):
        self.__mixed = mixed

    @property
    def graph_DocumentRoot8(self):
        return self.__graph_DocumentRoot8

    @graph_DocumentRoot8.setter
    def graph_DocumentRoot8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph_DocumentRoot__graph_DocumentRoot8", None)
        self.__graph_DocumentRoot8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "graph_EStringToStringMapEntry9"):
                    opp_val = getattr(item, "graph_EStringToStringMapEntry9", None)
                    
                    if opp_val == self:
                        setattr(item, "graph_EStringToStringMapEntry9", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "graph_EStringToStringMapEntry9"):
                    opp_val = getattr(item, "graph_EStringToStringMapEntry9", None)
                    
                    setattr(item, "graph_EStringToStringMapEntry9", self)
                    

    @property
    def graph_DocumentRoot19(self):
        return self.__graph_DocumentRoot19

    @graph_DocumentRoot19.setter
    def graph_DocumentRoot19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph_DocumentRoot__graph_DocumentRoot19", None)
        self.__graph_DocumentRoot19 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "graph_Node20"):
                    opp_val = getattr(item, "graph_Node20", None)
                    
                    if opp_val == self:
                        setattr(item, "graph_Node20", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "graph_Node20"):
                    opp_val = getattr(item, "graph_Node20", None)
                    
                    setattr(item, "graph_Node20", self)
                    

    @property
    def graph_DocumentRoot14(self):
        return self.__graph_DocumentRoot14

    @graph_DocumentRoot14.setter
    def graph_DocumentRoot14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph_DocumentRoot__graph_DocumentRoot14", None)
        self.__graph_DocumentRoot14 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "graph_Dependency15"):
                    opp_val = getattr(item, "graph_Dependency15", None)
                    
                    if opp_val == self:
                        setattr(item, "graph_Dependency15", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "graph_Dependency15"):
                    opp_val = getattr(item, "graph_Dependency15", None)
                    
                    setattr(item, "graph_Dependency15", self)
                    

    @property
    def graph_DocumentRoot11(self):
        return self.__graph_DocumentRoot11

    @graph_DocumentRoot11.setter
    def graph_DocumentRoot11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph_DocumentRoot__graph_DocumentRoot11", None)
        self.__graph_DocumentRoot11 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "graph_Cause12"):
                    opp_val = getattr(item, "graph_Cause12", None)
                    
                    if opp_val == self:
                        setattr(item, "graph_Cause12", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "graph_Cause12"):
                    opp_val = getattr(item, "graph_Cause12", None)
                    
                    setattr(item, "graph_Cause12", self)
                    

    @property
    def graph_DocumentRoot17(self):
        return self.__graph_DocumentRoot17

    @graph_DocumentRoot17.setter
    def graph_DocumentRoot17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph_DocumentRoot__graph_DocumentRoot17", None)
        self.__graph_DocumentRoot17 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "graph_EnvironmentGraph"):
                    opp_val = getattr(item, "graph_EnvironmentGraph", None)
                    
                    if opp_val == self:
                        setattr(item, "graph_EnvironmentGraph", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "graph_EnvironmentGraph"):
                    opp_val = getattr(item, "graph_EnvironmentGraph", None)
                    
                    setattr(item, "graph_EnvironmentGraph", self)
                    

    @property
    def graph_DocumentRoot(self):
        return self.__graph_DocumentRoot

    @graph_DocumentRoot.setter
    def graph_DocumentRoot(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph_DocumentRoot__graph_DocumentRoot", None)
        self.__graph_DocumentRoot = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "graph_EStringToStringMapEntry"):
                    opp_val = getattr(item, "graph_EStringToStringMapEntry", None)
                    
                    if opp_val == self:
                        setattr(item, "graph_EStringToStringMapEntry", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "graph_EStringToStringMapEntry"):
                    opp_val = getattr(item, "graph_EStringToStringMapEntry", None)
                    
                    setattr(item, "graph_EStringToStringMapEntry", self)
                    

class graph_Cause:

    def __init__(self, type: str, version: str, name: str, graph_Cause: "graph_Dependency" = None, graph_Cause12: "graph_DocumentRoot" = None):
        self.type = type
        self.version = version
        self.name = name
        self.graph_Cause = graph_Cause
        self.graph_Cause12 = graph_Cause12
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def version(self) -> str:
        return self.__version

    @version.setter
    def version(self, version: str):
        self.__version = version

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def graph_Cause(self):
        return self.__graph_Cause

    @graph_Cause.setter
    def graph_Cause(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph_Cause__graph_Cause", None)
        self.__graph_Cause = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graph_Dependency"):
                opp_val = getattr(old_value, "graph_Dependency", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graph_Dependency"):
                opp_val = getattr(value, "graph_Dependency", None)
                if opp_val is None:
                    setattr(value, "graph_Dependency", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def graph_Cause12(self):
        return self.__graph_Cause12

    @graph_Cause12.setter
    def graph_Cause12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph_Cause__graph_Cause12", None)
        self.__graph_Cause12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graph_DocumentRoot11"):
                opp_val = getattr(old_value, "graph_DocumentRoot11", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graph_DocumentRoot11"):
                opp_val = getattr(value, "graph_DocumentRoot11", None)
                if opp_val is None:
                    setattr(value, "graph_DocumentRoot11", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class graph_Node:

    def __init__(self, containerName: str, id: str, nodeName: str, unitName: str, unitVersion: str, graph_Node: "graph_Dependency" = None, graph_Node5: "graph_Dependency" = None, graph_Node23: "graph_EnvironmentGraph" = None, graph_Node29: "graph_EnvironmentGraph" = None, graph_Node20: "graph_DocumentRoot" = None, graph_Node34: set["graph_Dependency"] = None, graph_Node31: set["graph_Dependency"] = None):
        self.containerName = containerName
        self.id = id
        self.nodeName = nodeName
        self.unitName = unitName
        self.unitVersion = unitVersion
        self.graph_Node = graph_Node
        self.graph_Node5 = graph_Node5
        self.graph_Node23 = graph_Node23
        self.graph_Node29 = graph_Node29
        self.graph_Node20 = graph_Node20
        self.graph_Node34 = graph_Node34 if graph_Node34 is not None else set()
        self.graph_Node31 = graph_Node31 if graph_Node31 is not None else set()
        
    @property
    def containerName(self) -> str:
        return self.__containerName

    @containerName.setter
    def containerName(self, containerName: str):
        self.__containerName = containerName

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def unitVersion(self) -> str:
        return self.__unitVersion

    @unitVersion.setter
    def unitVersion(self, unitVersion: str):
        self.__unitVersion = unitVersion

    @property
    def nodeName(self) -> str:
        return self.__nodeName

    @nodeName.setter
    def nodeName(self, nodeName: str):
        self.__nodeName = nodeName

    @property
    def unitName(self) -> str:
        return self.__unitName

    @unitName.setter
    def unitName(self, unitName: str):
        self.__unitName = unitName

    @property
    def graph_Node(self):
        return self.__graph_Node

    @graph_Node.setter
    def graph_Node(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph_Node__graph_Node", None)
        self.__graph_Node = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graph_Dependency2"):
                opp_val = getattr(old_value, "graph_Dependency2", None)
                if opp_val == self:
                    setattr(old_value, "graph_Dependency2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graph_Dependency2"):
                opp_val = getattr(value, "graph_Dependency2", None)
                setattr(value, "graph_Dependency2", self)

    @property
    def graph_Node29(self):
        return self.__graph_Node29

    @graph_Node29.setter
    def graph_Node29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph_Node__graph_Node29", None)
        self.__graph_Node29 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graph_EnvironmentGraph28"):
                opp_val = getattr(old_value, "graph_EnvironmentGraph28", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graph_EnvironmentGraph28"):
                opp_val = getattr(value, "graph_EnvironmentGraph28", None)
                if opp_val is None:
                    setattr(value, "graph_EnvironmentGraph28", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def graph_Node31(self):
        return self.__graph_Node31

    @graph_Node31.setter
    def graph_Node31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph_Node__graph_Node31", None)
        self.__graph_Node31 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "graph_Dependency32"):
                    opp_val = getattr(item, "graph_Dependency32", None)
                    
                    if opp_val == self:
                        setattr(item, "graph_Dependency32", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "graph_Dependency32"):
                    opp_val = getattr(item, "graph_Dependency32", None)
                    
                    setattr(item, "graph_Dependency32", self)
                    

    @property
    def graph_Node23(self):
        return self.__graph_Node23

    @graph_Node23.setter
    def graph_Node23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph_Node__graph_Node23", None)
        self.__graph_Node23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graph_EnvironmentGraph22"):
                opp_val = getattr(old_value, "graph_EnvironmentGraph22", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graph_EnvironmentGraph22"):
                opp_val = getattr(value, "graph_EnvironmentGraph22", None)
                if opp_val is None:
                    setattr(value, "graph_EnvironmentGraph22", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def graph_Node34(self):
        return self.__graph_Node34

    @graph_Node34.setter
    def graph_Node34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph_Node__graph_Node34", None)
        self.__graph_Node34 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "graph_Dependency35"):
                    opp_val = getattr(item, "graph_Dependency35", None)
                    
                    if opp_val == self:
                        setattr(item, "graph_Dependency35", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "graph_Dependency35"):
                    opp_val = getattr(item, "graph_Dependency35", None)
                    
                    setattr(item, "graph_Dependency35", self)
                    

    @property
    def graph_Node20(self):
        return self.__graph_Node20

    @graph_Node20.setter
    def graph_Node20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph_Node__graph_Node20", None)
        self.__graph_Node20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graph_DocumentRoot19"):
                opp_val = getattr(old_value, "graph_DocumentRoot19", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graph_DocumentRoot19"):
                opp_val = getattr(value, "graph_DocumentRoot19", None)
                if opp_val is None:
                    setattr(value, "graph_DocumentRoot19", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def graph_Node5(self):
        return self.__graph_Node5

    @graph_Node5.setter
    def graph_Node5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph_Node__graph_Node5", None)
        self.__graph_Node5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graph_Dependency4"):
                opp_val = getattr(old_value, "graph_Dependency4", None)
                if opp_val == self:
                    setattr(old_value, "graph_Dependency4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graph_Dependency4"):
                opp_val = getattr(value, "graph_Dependency4", None)
                setattr(value, "graph_Dependency4", self)

class graph_Dependency:

    def __init__(self, locality: str, id: str, graph_Dependency: set["graph_Cause"] = None, graph_Dependency2: "graph_Node" = None, graph_Dependency4: "graph_Node" = None, graph_Dependency15: "graph_DocumentRoot" = None, graph_Dependency26: "graph_EnvironmentGraph" = None, graph_Dependency35: "graph_Node" = None, graph_Dependency32: "graph_Node" = None):
        self.locality = locality
        self.id = id
        self.graph_Dependency = graph_Dependency if graph_Dependency is not None else set()
        self.graph_Dependency2 = graph_Dependency2
        self.graph_Dependency4 = graph_Dependency4
        self.graph_Dependency15 = graph_Dependency15
        self.graph_Dependency26 = graph_Dependency26
        self.graph_Dependency35 = graph_Dependency35
        self.graph_Dependency32 = graph_Dependency32
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def locality(self) -> str:
        return self.__locality

    @locality.setter
    def locality(self, locality: str):
        self.__locality = locality

    @property
    def graph_Dependency4(self):
        return self.__graph_Dependency4

    @graph_Dependency4.setter
    def graph_Dependency4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph_Dependency__graph_Dependency4", None)
        self.__graph_Dependency4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graph_Node5"):
                opp_val = getattr(old_value, "graph_Node5", None)
                if opp_val == self:
                    setattr(old_value, "graph_Node5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graph_Node5"):
                opp_val = getattr(value, "graph_Node5", None)
                setattr(value, "graph_Node5", self)

    @property
    def graph_Dependency2(self):
        return self.__graph_Dependency2

    @graph_Dependency2.setter
    def graph_Dependency2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph_Dependency__graph_Dependency2", None)
        self.__graph_Dependency2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graph_Node"):
                opp_val = getattr(old_value, "graph_Node", None)
                if opp_val == self:
                    setattr(old_value, "graph_Node", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graph_Node"):
                opp_val = getattr(value, "graph_Node", None)
                setattr(value, "graph_Node", self)

    @property
    def graph_Dependency26(self):
        return self.__graph_Dependency26

    @graph_Dependency26.setter
    def graph_Dependency26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph_Dependency__graph_Dependency26", None)
        self.__graph_Dependency26 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graph_EnvironmentGraph25"):
                opp_val = getattr(old_value, "graph_EnvironmentGraph25", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graph_EnvironmentGraph25"):
                opp_val = getattr(value, "graph_EnvironmentGraph25", None)
                if opp_val is None:
                    setattr(value, "graph_EnvironmentGraph25", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def graph_Dependency32(self):
        return self.__graph_Dependency32

    @graph_Dependency32.setter
    def graph_Dependency32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph_Dependency__graph_Dependency32", None)
        self.__graph_Dependency32 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graph_Node31"):
                opp_val = getattr(old_value, "graph_Node31", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graph_Node31"):
                opp_val = getattr(value, "graph_Node31", None)
                if opp_val is None:
                    setattr(value, "graph_Node31", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def graph_Dependency15(self):
        return self.__graph_Dependency15

    @graph_Dependency15.setter
    def graph_Dependency15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph_Dependency__graph_Dependency15", None)
        self.__graph_Dependency15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graph_DocumentRoot14"):
                opp_val = getattr(old_value, "graph_DocumentRoot14", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graph_DocumentRoot14"):
                opp_val = getattr(value, "graph_DocumentRoot14", None)
                if opp_val is None:
                    setattr(value, "graph_DocumentRoot14", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def graph_Dependency35(self):
        return self.__graph_Dependency35

    @graph_Dependency35.setter
    def graph_Dependency35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph_Dependency__graph_Dependency35", None)
        self.__graph_Dependency35 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graph_Node34"):
                opp_val = getattr(old_value, "graph_Node34", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graph_Node34"):
                opp_val = getattr(value, "graph_Node34", None)
                if opp_val is None:
                    setattr(value, "graph_Node34", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def graph_Dependency(self):
        return self.__graph_Dependency

    @graph_Dependency.setter
    def graph_Dependency(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph_Dependency__graph_Dependency", None)
        self.__graph_Dependency = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "graph_Cause"):
                    opp_val = getattr(item, "graph_Cause", None)
                    
                    if opp_val == self:
                        setattr(item, "graph_Cause", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "graph_Cause"):
                    opp_val = getattr(item, "graph_Cause", None)
                    
                    setattr(item, "graph_Cause", self)
                    
