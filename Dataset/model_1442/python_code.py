from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class simpleGraph_Parameter:

    def __init__(self, key: str, value: str, simpleGraph_Parameter: "simpleGraph_GraphElement" = None):
        self.key = key
        self.value = value
        self.simpleGraph_Parameter = simpleGraph_Parameter
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def key(self) -> str:
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key

    @property
    def simpleGraph_Parameter(self):
        return self.__simpleGraph_Parameter

    @simpleGraph_Parameter.setter
    def simpleGraph_Parameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleGraph_Parameter__simpleGraph_Parameter", None)
        self.__simpleGraph_Parameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simpleGraph_GraphElement"):
                opp_val = getattr(old_value, "simpleGraph_GraphElement", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simpleGraph_GraphElement"):
                opp_val = getattr(value, "simpleGraph_GraphElement", None)
                if opp_val is None:
                    setattr(value, "simpleGraph_GraphElement", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class simpleGraph_GraphElement(ABC):

    def __init__(self, id: int, generated: bool, simpleGraph_GraphElement: set["simpleGraph_Parameter"] = None):
        self.id = id
        self.generated = generated
        self.simpleGraph_GraphElement = simpleGraph_GraphElement if simpleGraph_GraphElement is not None else set()
        
    @property
    def generated(self) -> bool:
        return self.__generated

    @generated.setter
    def generated(self, generated: bool):
        self.__generated = generated

    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def simpleGraph_GraphElement(self):
        return self.__simpleGraph_GraphElement

    @simpleGraph_GraphElement.setter
    def simpleGraph_GraphElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleGraph_GraphElement__simpleGraph_GraphElement", None)
        self.__simpleGraph_GraphElement = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "simpleGraph_Parameter"):
                    opp_val = getattr(item, "simpleGraph_Parameter", None)
                    
                    if opp_val == self:
                        setattr(item, "simpleGraph_Parameter", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "simpleGraph_Parameter"):
                    opp_val = getattr(item, "simpleGraph_Parameter", None)
                    
                    setattr(item, "simpleGraph_Parameter", self)
                    

class Position:

    pass
class simpleGraph_Nail(Position):

    pass
class simpleGraph_Label(Position):

    def __init__(self, value: str, simpleGraph_Label: "simpleGraph_Edge" = None, simpleGraph_Label16: "simpleGraph_Node" = None):
        self.value = value
        self.simpleGraph_Label = simpleGraph_Label
        self.simpleGraph_Label16 = simpleGraph_Label16
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def simpleGraph_Label(self):
        return self.__simpleGraph_Label

    @simpleGraph_Label.setter
    def simpleGraph_Label(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleGraph_Label__simpleGraph_Label", None)
        self.__simpleGraph_Label = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simpleGraph_Edge11"):
                opp_val = getattr(old_value, "simpleGraph_Edge11", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simpleGraph_Edge11"):
                opp_val = getattr(value, "simpleGraph_Edge11", None)
                if opp_val is None:
                    setattr(value, "simpleGraph_Edge11", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def simpleGraph_Label16(self):
        return self.__simpleGraph_Label16

    @simpleGraph_Label16.setter
    def simpleGraph_Label16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleGraph_Label__simpleGraph_Label16", None)
        self.__simpleGraph_Label16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simpleGraph_Node15"):
                opp_val = getattr(old_value, "simpleGraph_Node15", None)
                if opp_val == self:
                    setattr(old_value, "simpleGraph_Node15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simpleGraph_Node15"):
                opp_val = getattr(value, "simpleGraph_Node15", None)
                setattr(value, "simpleGraph_Node15", self)

class simpleGraph_Node(Position):

    pass
class GraphElement:

    pass
class simpleGraph_Edge(GraphElement):

    pass
class simpleGraph_Position(GraphElement):

    def __init__(self, X: int, Y: int):
        self.X = X
        self.Y = Y
        
    @property
    def X(self) -> int:
        return self.__X

    @X.setter
    def X(self, X: int):
        self.__X = X

    @property
    def Y(self) -> int:
        return self.__Y

    @Y.setter
    def Y(self, Y: int):
        self.__Y = Y

class simpleGraph_Graph(GraphElement):

    pass