from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class TPArc:

    pass
class PTArc:

    pass
class PetriNet:

    pass
class GenericPT:

    pass
class PetriNetMM2_Transition(GenericPT):

    def __init__(self, name: str, relevance: int, transitions: "PetriNet" = None, dst12: set["PTArc"] = None, src15: set["TPArc"] = None):
        self.name = name
        self.relevance = relevance
        self.transitions = transitions
        self.dst12 = dst12 if dst12 is not None else set()
        self.src15 = src15 if src15 is not None else set()
        
        pass
    @property
    def relevance(self):
        return self.__relevance

    @relevance.setter
    def relevance(self, relevance: int):
        self.__relevance = relevance


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def transitions(self):
        return self.__transitions

    @transitions.setter
    def transitions(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PetriNetMM2_Transition__transitions", None)
        self.__transitions = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PetriNet10"):
                opp_val = getattr(old_value, "PetriNet10", None)
                if opp_val == self:
                    setattr(old_value, "PetriNet10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PetriNet10"):
                opp_val = getattr(value, "PetriNet10", None)
                setattr(value, "PetriNet10", self)

    @property
    def dst12(self):
        return self.__dst12

    @dst12.setter
    def dst12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PetriNetMM2_Transition__dst12", None)
        self.__dst12 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "PTArc13"):
                    opp_val = getattr(item, "PTArc13", None)
                    
                    if opp_val == self:
                        setattr(item, "PTArc13", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "PTArc13"):
                    opp_val = getattr(item, "PTArc13", None)
                    
                    setattr(item, "PTArc13", self)
                    

    @property
    def src15(self):
        return self.__src15

    @src15.setter
    def src15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PetriNetMM2_Transition__src15", None)
        self.__src15 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "TPArc16"):
                    opp_val = getattr(item, "TPArc16", None)
                    
                    if opp_val == self:
                        setattr(item, "TPArc16", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "TPArc16"):
                    opp_val = getattr(item, "TPArc16", None)
                    
                    setattr(item, "TPArc16", self)
                    

class PetriNetMM2_Place(GenericPT):

    def __init__(self, name: str, relevance: int, places: "PetriNet" = None, src: set["PTArc"] = None, dst: set["TPArc"] = None):
        self.name = name
        self.relevance = relevance
        self.places = places
        self.src = src if src is not None else set()
        self.dst = dst if dst is not None else set()
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def relevance(self):
        return self.__relevance

    @relevance.setter
    def relevance(self, relevance: int):
        self.__relevance = relevance


    @property
    def dst(self):
        return self.__dst

    @dst.setter
    def dst(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PetriNetMM2_Place__dst", None)
        self.__dst = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "TPArc"):
                    opp_val = getattr(item, "TPArc", None)
                    
                    if opp_val == self:
                        setattr(item, "TPArc", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "TPArc"):
                    opp_val = getattr(item, "TPArc", None)
                    
                    setattr(item, "TPArc", self)
                    

    @property
    def src(self):
        return self.__src

    @src.setter
    def src(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PetriNetMM2_Place__src", None)
        self.__src = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "PTArc"):
                    opp_val = getattr(item, "PTArc", None)
                    
                    if opp_val == self:
                        setattr(item, "PTArc", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "PTArc"):
                    opp_val = getattr(item, "PTArc", None)
                    
                    setattr(item, "PTArc", self)
                    

    @property
    def places(self):
        return self.__places

    @places.setter
    def places(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PetriNetMM2_Place__places", None)
        self.__places = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PetriNet"):
                opp_val = getattr(old_value, "PetriNet", None)
                if opp_val == self:
                    setattr(old_value, "PetriNet", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PetriNet"):
                opp_val = getattr(value, "PetriNet", None)
                setattr(value, "PetriNet", self)

class PetriNetModel:

    pass
class PetriNetMM2_PetriNetModelElement:

    pass
class PetriNetModelElement:

    pass
class PetriNetMM2_GenericPT(PetriNetModelElement):

    def __init__(self, label: str, PetriNetModelElement: "PetriNetMM2_PetriNetModel" = None):
        self.label = label
        
        pass
    @property
    def label(self):
        return self.__label

    @label.setter
    def label(self, label: str):
        self.__label = label


class PetriNetMM2_Arc(PetriNetModelElement):

    def __init__(self, weight: int, PetriNetModelElement: "PetriNetMM2_PetriNetModel" = None):
        self.weight = weight
        
        pass
    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, weight: int):
        self.__weight = weight


class PetriNetMM2_PetriNetModel:

    pass
class Arc:

    pass
class PetriNetMM2_PTArc(Arc):

    pass
class PetriNetMM2_TPArc(Arc):

    pass
class Transition:

    pass
class Place:

    pass
class PetriNetMM2_PetriNet(PetriNetModelElement):

    def __init__(self, name: str, net: set["Place"] = None, net4: set["Transition"] = None, PetriNetMM2_PetriNet: set["Arc"] = None, PetriNetModelElement: "PetriNetMM2_PetriNetModel" = None):
        self.name = name
        self.net = net if net is not None else set()
        self.net4 = net4 if net4 is not None else set()
        self.PetriNetMM2_PetriNet = PetriNetMM2_PetriNet if PetriNetMM2_PetriNet is not None else set()
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def PetriNetMM2_PetriNet(self):
        return self.__PetriNetMM2_PetriNet

    @PetriNetMM2_PetriNet.setter
    def PetriNetMM2_PetriNet(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PetriNetMM2_PetriNet__PetriNetMM2_PetriNet", None)
        self.__PetriNetMM2_PetriNet = value if value is not None else set()
        
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
                    

    @property
    def net4(self):
        return self.__net4

    @net4.setter
    def net4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PetriNetMM2_PetriNet__net4", None)
        self.__net4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Transition"):
                    opp_val = getattr(item, "Transition", None)
                    
                    if opp_val == self:
                        setattr(item, "Transition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Transition"):
                    opp_val = getattr(item, "Transition", None)
                    
                    setattr(item, "Transition", self)
                    

    @property
    def net(self):
        return self.__net

    @net.setter
    def net(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PetriNetMM2_PetriNet__net", None)
        self.__net = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Place"):
                    opp_val = getattr(item, "Place", None)
                    
                    if opp_val == self:
                        setattr(item, "Place", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Place"):
                    opp_val = getattr(item, "Place", None)
                    
                    setattr(item, "Place", self)
                    
