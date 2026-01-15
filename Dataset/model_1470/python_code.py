from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class graph_DeploymentUnitType:

    pass
class graph_EStringToStringMapEntry:

    pass
class graph_DocumentRoot:

    def __init__(self, mixed: str, graph_DocumentRoot: set["graph_EStringToStringMapEntry"] = None, graph_DocumentRoot16: set["graph_EStringToStringMapEntry"] = None, graph_DocumentRoot19: set["graph_DependencyGraph"] = None):
        self.mixed = mixed
        self.graph_DocumentRoot = graph_DocumentRoot if graph_DocumentRoot is not None else set()
        self.graph_DocumentRoot16 = graph_DocumentRoot16 if graph_DocumentRoot16 is not None else set()
        self.graph_DocumentRoot19 = graph_DocumentRoot19 if graph_DocumentRoot19 is not None else set()
        
    @property
    def mixed(self) -> str:
        return self.__mixed

    @mixed.setter
    def mixed(self, mixed: str):
        self.__mixed = mixed

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
                if hasattr(item, "graph_DependencyGraph20"):
                    opp_val = getattr(item, "graph_DependencyGraph20", None)
                    
                    if opp_val == self:
                        setattr(item, "graph_DependencyGraph20", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "graph_DependencyGraph20"):
                    opp_val = getattr(item, "graph_DependencyGraph20", None)
                    
                    setattr(item, "graph_DependencyGraph20", self)
                    

    @property
    def graph_DocumentRoot16(self):
        return self.__graph_DocumentRoot16

    @graph_DocumentRoot16.setter
    def graph_DocumentRoot16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph_DocumentRoot__graph_DocumentRoot16", None)
        self.__graph_DocumentRoot16 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "graph_EStringToStringMapEntry17"):
                    opp_val = getattr(item, "graph_EStringToStringMapEntry17", None)
                    
                    if opp_val == self:
                        setattr(item, "graph_EStringToStringMapEntry17", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "graph_EStringToStringMapEntry17"):
                    opp_val = getattr(item, "graph_EStringToStringMapEntry17", None)
                    
                    setattr(item, "graph_EStringToStringMapEntry17", self)
                    

class graph_DependencyGraph:

    pass
class graph_Node:

    def __init__(self, id: str, graph_Node: "graph_Dependency" = None, graph_Node5: "graph_Dependency" = None, graph_Node7: "graph_DependencyGraph" = None, graph_Node13: "graph_DependencyGraph" = None, graph_Node22: "graph_DeploymentUnitType" = None, graph_Node24: set["graph_Dependency"] = None):
        self.id = id
        self.graph_Node = graph_Node
        self.graph_Node5 = graph_Node5
        self.graph_Node7 = graph_Node7
        self.graph_Node13 = graph_Node13
        self.graph_Node22 = graph_Node22
        self.graph_Node24 = graph_Node24 if graph_Node24 is not None else set()
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

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
    def graph_Node13(self):
        return self.__graph_Node13

    @graph_Node13.setter
    def graph_Node13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph_Node__graph_Node13", None)
        self.__graph_Node13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graph_DependencyGraph12"):
                opp_val = getattr(old_value, "graph_DependencyGraph12", None)
                if opp_val == self:
                    setattr(old_value, "graph_DependencyGraph12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graph_DependencyGraph12"):
                opp_val = getattr(value, "graph_DependencyGraph12", None)
                setattr(value, "graph_DependencyGraph12", self)

    @property
    def graph_Node7(self):
        return self.__graph_Node7

    @graph_Node7.setter
    def graph_Node7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph_Node__graph_Node7", None)
        self.__graph_Node7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graph_DependencyGraph"):
                opp_val = getattr(old_value, "graph_DependencyGraph", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graph_DependencyGraph"):
                opp_val = getattr(value, "graph_DependencyGraph", None)
                if opp_val is None:
                    setattr(value, "graph_DependencyGraph", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def graph_Node22(self):
        return self.__graph_Node22

    @graph_Node22.setter
    def graph_Node22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph_Node__graph_Node22", None)
        self.__graph_Node22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graph_DeploymentUnitType"):
                opp_val = getattr(old_value, "graph_DeploymentUnitType", None)
                if opp_val == self:
                    setattr(old_value, "graph_DeploymentUnitType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graph_DeploymentUnitType"):
                opp_val = getattr(value, "graph_DeploymentUnitType", None)
                setattr(value, "graph_DeploymentUnitType", self)

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

    @property
    def graph_Node24(self):
        return self.__graph_Node24

    @graph_Node24.setter
    def graph_Node24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph_Node__graph_Node24", None)
        self.__graph_Node24 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "graph_Dependency25"):
                    opp_val = getattr(item, "graph_Dependency25", None)
                    
                    if opp_val == self:
                        setattr(item, "graph_Dependency25", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "graph_Dependency25"):
                    opp_val = getattr(item, "graph_Dependency25", None)
                    
                    setattr(item, "graph_Dependency25", self)
                    

class graph_Dependency:

    def __init__(self, id: str, locality: str, graph_Dependency: set["graph_Cause"] = None, graph_Dependency10: "graph_DependencyGraph" = None, graph_Dependency2: "graph_Node" = None, graph_Dependency4: "graph_Node" = None, graph_Dependency25: "graph_Node" = None):
        self.id = id
        self.locality = locality
        self.graph_Dependency = graph_Dependency if graph_Dependency is not None else set()
        self.graph_Dependency10 = graph_Dependency10
        self.graph_Dependency2 = graph_Dependency2
        self.graph_Dependency4 = graph_Dependency4
        self.graph_Dependency25 = graph_Dependency25
        
    @property
    def locality(self) -> str:
        return self.__locality

    @locality.setter
    def locality(self, locality: str):
        self.__locality = locality

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def graph_Dependency10(self):
        return self.__graph_Dependency10

    @graph_Dependency10.setter
    def graph_Dependency10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph_Dependency__graph_Dependency10", None)
        self.__graph_Dependency10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graph_DependencyGraph9"):
                opp_val = getattr(old_value, "graph_DependencyGraph9", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graph_DependencyGraph9"):
                opp_val = getattr(value, "graph_DependencyGraph9", None)
                if opp_val is None:
                    setattr(value, "graph_DependencyGraph9", set([self]))
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
    def graph_Dependency25(self):
        return self.__graph_Dependency25

    @graph_Dependency25.setter
    def graph_Dependency25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph_Dependency__graph_Dependency25", None)
        self.__graph_Dependency25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graph_Node24"):
                opp_val = getattr(old_value, "graph_Node24", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graph_Node24"):
                opp_val = getattr(value, "graph_Node24", None)
                if opp_val is None:
                    setattr(value, "graph_Node24", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class graph_Cause:

    def __init__(self, name: str, type: str, graph_Cause: "graph_Dependency" = None):
        self.name = name
        self.type = type
        self.graph_Cause = graph_Cause
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

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
