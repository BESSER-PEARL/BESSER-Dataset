from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class Node:

    pass
class pETRI_Transition(Node):

    pass
class pETRI_Place(Node):

    def __init__(self, marking: int):
        self.marking = marking
        
        pass
    @property
    def marking(self):
        return self.__marking

    @marking.setter
    def marking(self, marking: int):
        self.__marking = marking


class pETRI_PetriNet:

    def __init__(self, name: str, pETRI_PetriNet: set["pETRI_PetriNetElement"] = None):
        self.name = name
        self.pETRI_PetriNet = pETRI_PetriNet if pETRI_PetriNet is not None else set()
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def pETRI_PetriNet(self):
        return self.__pETRI_PetriNet

    @pETRI_PetriNet.setter
    def pETRI_PetriNet(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pETRI_PetriNet__pETRI_PetriNet", None)
        self.__pETRI_PetriNet = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "pETRI_PetriNetElement"):
                    opp_val = getattr(item, "pETRI_PetriNetElement", None)
                    
                    if opp_val == self:
                        setattr(item, "pETRI_PetriNetElement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "pETRI_PetriNetElement"):
                    opp_val = getattr(item, "pETRI_PetriNetElement", None)
                    
                    setattr(item, "pETRI_PetriNetElement", self)
                    

class PetriNetElement:

    pass
class pETRI_Arc(PetriNetElement):

    def __init__(self, multiplicity: int, readOnly: bool, pETRI_Arc: "pETRI_Node" = None, pETRI_Arc3: "pETRI_Node" = None):
        self.multiplicity = multiplicity
        self.readOnly = readOnly
        self.pETRI_Arc = pETRI_Arc
        self.pETRI_Arc3 = pETRI_Arc3
        
        pass
    @property
    def readOnly(self):
        return self.__readOnly

    @readOnly.setter
    def readOnly(self, readOnly: bool):
        self.__readOnly = readOnly


    @property
    def multiplicity(self):
        return self.__multiplicity

    @multiplicity.setter
    def multiplicity(self, multiplicity: int):
        self.__multiplicity = multiplicity


    @property
    def pETRI_Arc(self):
        return self.__pETRI_Arc

    @pETRI_Arc.setter
    def pETRI_Arc(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pETRI_Arc__pETRI_Arc", None)
        self.__pETRI_Arc = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pETRI_Node"):
                opp_val = getattr(old_value, "pETRI_Node", None)
                if opp_val == self:
                    setattr(old_value, "pETRI_Node", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pETRI_Node"):
                opp_val = getattr(value, "pETRI_Node", None)
                setattr(value, "pETRI_Node", self)

    @property
    def pETRI_Arc3(self):
        return self.__pETRI_Arc3

    @pETRI_Arc3.setter
    def pETRI_Arc3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pETRI_Arc__pETRI_Arc3", None)
        self.__pETRI_Arc3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pETRI_Node4"):
                opp_val = getattr(old_value, "pETRI_Node4", None)
                if opp_val == self:
                    setattr(old_value, "pETRI_Node4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pETRI_Node4"):
                opp_val = getattr(value, "pETRI_Node4", None)
                setattr(value, "pETRI_Node4", self)

class pETRI_Node(PetriNetElement):

    def __init__(self, name: str, pETRI_Node: "pETRI_Arc" = None, pETRI_Node4: "pETRI_Arc" = None):
        self.name = name
        self.pETRI_Node = pETRI_Node
        self.pETRI_Node4 = pETRI_Node4
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def pETRI_Node4(self):
        return self.__pETRI_Node4

    @pETRI_Node4.setter
    def pETRI_Node4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pETRI_Node__pETRI_Node4", None)
        self.__pETRI_Node4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pETRI_Arc3"):
                opp_val = getattr(old_value, "pETRI_Arc3", None)
                if opp_val == self:
                    setattr(old_value, "pETRI_Arc3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pETRI_Arc3"):
                opp_val = getattr(value, "pETRI_Arc3", None)
                setattr(value, "pETRI_Arc3", self)

    @property
    def pETRI_Node(self):
        return self.__pETRI_Node

    @pETRI_Node.setter
    def pETRI_Node(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pETRI_Node__pETRI_Node", None)
        self.__pETRI_Node = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pETRI_Arc"):
                opp_val = getattr(old_value, "pETRI_Arc", None)
                if opp_val == self:
                    setattr(old_value, "pETRI_Arc", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pETRI_Arc"):
                opp_val = getattr(value, "pETRI_Arc", None)
                setattr(value, "pETRI_Arc", self)

class pETRI_PetriNetElement:

    pass