from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class petrinet_Token:

    pass
class petrinet_TransitionFireEvent:

    pass
class petrinet_NetStopEvent:

    pass
class petrinet_Transition:

    def __init__(self, name: str, petrinet_Transition: "petrinet_Net" = None, petrinet_Transition14: "petrinet_TransitionFireEvent" = None, petrinet_Transition4: set["petrinet_Place"] = None, petrinet_Transition7: set["petrinet_Place"] = None):
        self.name = name
        self.petrinet_Transition = petrinet_Transition
        self.petrinet_Transition14 = petrinet_Transition14
        self.petrinet_Transition4 = petrinet_Transition4 if petrinet_Transition4 is not None else set()
        self.petrinet_Transition7 = petrinet_Transition7 if petrinet_Transition7 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def petrinet_Transition(self):
        return self.__petrinet_Transition

    @petrinet_Transition.setter
    def petrinet_Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinet_Transition__petrinet_Transition", None)
        self.__petrinet_Transition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "petrinet_Net2"):
                opp_val = getattr(old_value, "petrinet_Net2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "petrinet_Net2"):
                opp_val = getattr(value, "petrinet_Net2", None)
                if opp_val is None:
                    setattr(value, "petrinet_Net2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def petrinet_Transition7(self):
        return self.__petrinet_Transition7

    @petrinet_Transition7.setter
    def petrinet_Transition7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinet_Transition__petrinet_Transition7", None)
        self.__petrinet_Transition7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "petrinet_Place8"):
                    opp_val = getattr(item, "petrinet_Place8", None)
                    
                    if opp_val == self:
                        setattr(item, "petrinet_Place8", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "petrinet_Place8"):
                    opp_val = getattr(item, "petrinet_Place8", None)
                    
                    setattr(item, "petrinet_Place8", self)
                    

    @property
    def petrinet_Transition4(self):
        return self.__petrinet_Transition4

    @petrinet_Transition4.setter
    def petrinet_Transition4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinet_Transition__petrinet_Transition4", None)
        self.__petrinet_Transition4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "petrinet_Place5"):
                    opp_val = getattr(item, "petrinet_Place5", None)
                    
                    if opp_val == self:
                        setattr(item, "petrinet_Place5", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "petrinet_Place5"):
                    opp_val = getattr(item, "petrinet_Place5", None)
                    
                    setattr(item, "petrinet_Place5", self)
                    

    @property
    def petrinet_Transition14(self):
        return self.__petrinet_Transition14

    @petrinet_Transition14.setter
    def petrinet_Transition14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinet_Transition__petrinet_Transition14", None)
        self.__petrinet_Transition14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "petrinet_TransitionFireEvent"):
                opp_val = getattr(old_value, "petrinet_TransitionFireEvent", None)
                if opp_val == self:
                    setattr(old_value, "petrinet_TransitionFireEvent", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "petrinet_TransitionFireEvent"):
                opp_val = getattr(value, "petrinet_TransitionFireEvent", None)
                setattr(value, "petrinet_TransitionFireEvent", self)

    def fire(self):
        # TODO: Implement fire method
        pass

    def fire_PreCondition(self):
        # TODO: Implement fire_PreCondition method
        pass

    def isEnabled(self):
        # TODO: Implement isEnabled method
        pass

class petrinet_Place:

    def __init__(self, name: str, initialTokens: int, petrinet_Place: "petrinet_Net" = None, petrinet_Place5: "petrinet_Transition" = None, petrinet_Place8: "petrinet_Transition" = None, petrinet_Place10: set["petrinet_Token"] = None):
        self.name = name
        self.initialTokens = initialTokens
        self.petrinet_Place = petrinet_Place
        self.petrinet_Place5 = petrinet_Place5
        self.petrinet_Place8 = petrinet_Place8
        self.petrinet_Place10 = petrinet_Place10 if petrinet_Place10 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def initialTokens(self) -> int:
        return self.__initialTokens

    @initialTokens.setter
    def initialTokens(self, initialTokens: int):
        self.__initialTokens = initialTokens

    @property
    def petrinet_Place10(self):
        return self.__petrinet_Place10

    @petrinet_Place10.setter
    def petrinet_Place10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinet_Place__petrinet_Place10", None)
        self.__petrinet_Place10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "petrinet_Token"):
                    opp_val = getattr(item, "petrinet_Token", None)
                    
                    if opp_val == self:
                        setattr(item, "petrinet_Token", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "petrinet_Token"):
                    opp_val = getattr(item, "petrinet_Token", None)
                    
                    setattr(item, "petrinet_Token", self)
                    

    @property
    def petrinet_Place(self):
        return self.__petrinet_Place

    @petrinet_Place.setter
    def petrinet_Place(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinet_Place__petrinet_Place", None)
        self.__petrinet_Place = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "petrinet_Net"):
                opp_val = getattr(old_value, "petrinet_Net", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "petrinet_Net"):
                opp_val = getattr(value, "petrinet_Net", None)
                if opp_val is None:
                    setattr(value, "petrinet_Net", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def petrinet_Place5(self):
        return self.__petrinet_Place5

    @petrinet_Place5.setter
    def petrinet_Place5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinet_Place__petrinet_Place5", None)
        self.__petrinet_Place5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "petrinet_Transition4"):
                opp_val = getattr(old_value, "petrinet_Transition4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "petrinet_Transition4"):
                opp_val = getattr(value, "petrinet_Transition4", None)
                if opp_val is None:
                    setattr(value, "petrinet_Transition4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def petrinet_Place8(self):
        return self.__petrinet_Place8

    @petrinet_Place8.setter
    def petrinet_Place8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinet_Place__petrinet_Place8", None)
        self.__petrinet_Place8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "petrinet_Transition7"):
                opp_val = getattr(old_value, "petrinet_Transition7", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "petrinet_Transition7"):
                opp_val = getattr(value, "petrinet_Transition7", None)
                if opp_val is None:
                    setattr(value, "petrinet_Transition7", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class petrinet_Net:

    def __init__(self, petrinet_Net2: set["petrinet_Transition"] = None, petrinet_Net: set["petrinet_Place"] = None, petrinet_Net12: "petrinet_NetStopEvent" = None):
        self.petrinet_Net2 = petrinet_Net2 if petrinet_Net2 is not None else set()
        self.petrinet_Net = petrinet_Net if petrinet_Net is not None else set()
        self.petrinet_Net12 = petrinet_Net12
        
    @property
    def petrinet_Net(self):
        return self.__petrinet_Net

    @petrinet_Net.setter
    def petrinet_Net(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinet_Net__petrinet_Net", None)
        self.__petrinet_Net = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "petrinet_Place"):
                    opp_val = getattr(item, "petrinet_Place", None)
                    
                    if opp_val == self:
                        setattr(item, "petrinet_Place", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "petrinet_Place"):
                    opp_val = getattr(item, "petrinet_Place", None)
                    
                    setattr(item, "petrinet_Place", self)
                    

    @property
    def petrinet_Net12(self):
        return self.__petrinet_Net12

    @petrinet_Net12.setter
    def petrinet_Net12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinet_Net__petrinet_Net12", None)
        self.__petrinet_Net12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "petrinet_NetStopEvent"):
                opp_val = getattr(old_value, "petrinet_NetStopEvent", None)
                if opp_val == self:
                    setattr(old_value, "petrinet_NetStopEvent", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "petrinet_NetStopEvent"):
                opp_val = getattr(value, "petrinet_NetStopEvent", None)
                setattr(value, "petrinet_NetStopEvent", self)

    @property
    def petrinet_Net2(self):
        return self.__petrinet_Net2

    @petrinet_Net2.setter
    def petrinet_Net2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinet_Net__petrinet_Net2", None)
        self.__petrinet_Net2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "petrinet_Transition"):
                    opp_val = getattr(item, "petrinet_Transition", None)
                    
                    if opp_val == self:
                        setattr(item, "petrinet_Transition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "petrinet_Transition"):
                    opp_val = getattr(item, "petrinet_Transition", None)
                    
                    setattr(item, "petrinet_Transition", self)
                    

    def stop(self):
        # TODO: Implement stop method
        pass

    def initializeModel(self, args: str):
        # TODO: Implement initializeModel method
        pass

    def fireEnabledTransition(self):
        # TODO: Implement fireEnabledTransition method
        pass

    def run(self):
        # TODO: Implement run method
        pass
