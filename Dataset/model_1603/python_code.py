from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class Edge:

    pass
class PetrinetDSL_PTEdge(Edge):

    pass
class PetrinetDSL_TPEdge(Edge):

    pass
class Node:

    pass
class PetrinetDSL_Place(Node):

    pass
class PetrinetDSL_Transition(Node):

    pass
class PetrinetDSL_Token(Node):

    pass
class Petrinet:

    pass
class PetrinetDSL_Edge(Petrinet):

    pass
class PetrinetDSL_Node(Petrinet):

    pass
class PetrinetDSL_Petrinet:

    def __init__(self, name: str, description: str, PetrinetDSL_Petrinet: "PetrinetDSL_Petrinet" = None, PetrinetDSL_Petrinet0: set["PetrinetDSL_Petrinet"] = None):
        self.name = name
        self.description = description
        self.PetrinetDSL_Petrinet = PetrinetDSL_Petrinet
        self.PetrinetDSL_Petrinet0 = PetrinetDSL_Petrinet0 if PetrinetDSL_Petrinet0 is not None else set()
        
    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def PetrinetDSL_Petrinet0(self):
        return self.__PetrinetDSL_Petrinet0

    @PetrinetDSL_Petrinet0.setter
    def PetrinetDSL_Petrinet0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PetrinetDSL_Petrinet__PetrinetDSL_Petrinet0", None)
        self.__PetrinetDSL_Petrinet0 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "PetrinetDSL_Petrinet"):
                    opp_val = getattr(item, "PetrinetDSL_Petrinet", None)
                    
                    if opp_val == self:
                        setattr(item, "PetrinetDSL_Petrinet", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "PetrinetDSL_Petrinet"):
                    opp_val = getattr(item, "PetrinetDSL_Petrinet", None)
                    
                    setattr(item, "PetrinetDSL_Petrinet", self)
                    

    @property
    def PetrinetDSL_Petrinet(self):
        return self.__PetrinetDSL_Petrinet

    @PetrinetDSL_Petrinet.setter
    def PetrinetDSL_Petrinet(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PetrinetDSL_Petrinet__PetrinetDSL_Petrinet", None)
        self.__PetrinetDSL_Petrinet = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PetrinetDSL_Petrinet0"):
                opp_val = getattr(old_value, "PetrinetDSL_Petrinet0", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PetrinetDSL_Petrinet0"):
                opp_val = getattr(value, "PetrinetDSL_Petrinet0", None)
                if opp_val is None:
                    setattr(value, "PetrinetDSL_Petrinet0", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
