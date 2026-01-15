from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class PetriNetModel_Token:

    pass
class Node:

    pass
class PetriNetModel_Place(Node):

    pass
class PetriNetModel_Transition(Node):

    pass
class PObject:

    pass
class PetriNetModel_Arc(PObject):

    pass
class PetriNetModel_Node(PObject):

    def __init__(self, name: str, Node7: "PetriNetModel_Arc" = None, source: set["PetriNetModel_Arc"] = None, target: set["PetriNetModel_Arc"] = None, Node: "PetriNetModel_Arc" = None):
        self.name = name
        self.Node7 = Node7
        self.source = source if source is not None else set()
        self.target = target if target is not None else set()
        self.Node = Node
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def target(self):
        return self.__target

    @target.setter
    def target(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PetriNetModel_Node__target", None)
        self.__target = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Arc3"):
                    opp_val = getattr(item, "Arc3", None)
                    
                    if opp_val == self:
                        setattr(item, "Arc3", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Arc3"):
                    opp_val = getattr(item, "Arc3", None)
                    
                    setattr(item, "Arc3", self)
                    

    @property
    def Node7(self):
        return self.__Node7

    @Node7.setter
    def Node7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PetriNetModel_Node__Node7", None)
        self.__Node7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "in"):
                opp_val = getattr(old_value, "in", None)
                if opp_val == self:
                    setattr(old_value, "in", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "in"):
                opp_val = getattr(value, "in", None)
                setattr(value, "in", self)

    @property
    def Node(self):
        return self.__Node

    @Node.setter
    def Node(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PetriNetModel_Node__Node", None)
        self.__Node = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "out"):
                opp_val = getattr(old_value, "out", None)
                if opp_val == self:
                    setattr(old_value, "out", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "out"):
                opp_val = getattr(value, "out", None)
                setattr(value, "out", self)

    @property
    def source(self):
        return self.__source

    @source.setter
    def source(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PetriNetModel_Node__source", None)
        self.__source = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Arc"):
                    opp_val = getattr(item, "Arc", None)
                    
                    if opp_val == self:
                        setattr(item, "Arc", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Arc"):
                    opp_val = getattr(item, "Arc", None)
                    
                    setattr(item, "Arc", self)
                    

class PetriNetModel_PetriNet:

    pass
class PetriNetModel_PObject:

    def __init__(self, id: int, PetriNetModel_PObject: "PetriNetModel_PetriNet" = None):
        self.id = id
        self.PetriNetModel_PObject = PetriNetModel_PObject
        
    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def PetriNetModel_PObject(self):
        return self.__PetriNetModel_PObject

    @PetriNetModel_PObject.setter
    def PetriNetModel_PObject(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PetriNetModel_PObject__PetriNetModel_PObject", None)
        self.__PetriNetModel_PObject = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PetriNetModel_PetriNet"):
                opp_val = getattr(old_value, "PetriNetModel_PetriNet", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PetriNetModel_PetriNet"):
                opp_val = getattr(value, "PetriNetModel_PetriNet", None)
                if opp_val is None:
                    setattr(value, "PetriNetModel_PetriNet", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
