from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class PetriEdge:

    pass
class PetriNet_Arc(PetriEdge):

    pass
class PetriNet_PetriModel:

    def __init__(self, name: str, description: str, PetriNet_PetriModel: "PetriNet_PetriModel" = None, PetriNet_PetriModel7: set["PetriNet_PetriModel"] = None):
        self.name = name
        self.description = description
        self.PetriNet_PetriModel = PetriNet_PetriModel
        self.PetriNet_PetriModel7 = PetriNet_PetriModel7 if PetriNet_PetriModel7 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def PetriNet_PetriModel7(self):
        return self.__PetriNet_PetriModel7

    @PetriNet_PetriModel7.setter
    def PetriNet_PetriModel7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PetriNet_PetriModel__PetriNet_PetriModel7", None)
        self.__PetriNet_PetriModel7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "PetriNet_PetriModel"):
                    opp_val = getattr(item, "PetriNet_PetriModel", None)
                    
                    if opp_val == self:
                        setattr(item, "PetriNet_PetriModel", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "PetriNet_PetriModel"):
                    opp_val = getattr(item, "PetriNet_PetriModel", None)
                    
                    setattr(item, "PetriNet_PetriModel", self)
                    

    @property
    def PetriNet_PetriModel(self):
        return self.__PetriNet_PetriModel

    @PetriNet_PetriModel.setter
    def PetriNet_PetriModel(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PetriNet_PetriModel__PetriNet_PetriModel", None)
        self.__PetriNet_PetriModel = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PetriNet_PetriModel7"):
                opp_val = getattr(old_value, "PetriNet_PetriModel7", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PetriNet_PetriModel7"):
                opp_val = getattr(value, "PetriNet_PetriModel7", None)
                if opp_val is None:
                    setattr(value, "PetriNet_PetriModel7", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class PetriNode:

    pass
class PetriNet_Transition(PetriNode):

    pass
class PetriNet_Token(PetriNode):

    pass
class PetriNet_Place(PetriNode):

    pass
class PetriModel:

    pass
class PetriNet_PetriEdge(PetriModel):

    pass
class PetriNet_PetriNode(PetriModel):

    pass