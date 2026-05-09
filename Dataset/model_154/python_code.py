from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class petrinetmodel_Edge:

    def __init__(self, weight: int):
        self.weight = weight
        
        pass
    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, weight: int):
        self.__weight = weight


class Edge:

    pass
class petrinetmodel_EdgeToTransaction(Edge):

    pass
class petrinetmodel_EdgeToPlace(Edge):

    pass
class petrinetmodel_Place:

    def __init__(self, token: int, id: int, petrinetmodel_Place: "petrinetmodel_Petrinet" = None, petrinetmodel_Place7: "petrinetmodel_Transition" = None, petrinetmodel_Place9: set["petrinetmodel_EdgeToTransaction"] = None, petrinetmodel_Place12: "petrinetmodel_EdgeToPlace" = None):
        self.token = token
        self.id = id
        self.petrinetmodel_Place = petrinetmodel_Place
        self.petrinetmodel_Place7 = petrinetmodel_Place7
        self.petrinetmodel_Place9 = petrinetmodel_Place9 if petrinetmodel_Place9 is not None else set()
        self.petrinetmodel_Place12 = petrinetmodel_Place12
        
        pass
    @property
    def token(self):
        return self.__token

    @token.setter
    def token(self, token: int):
        self.__token = token


    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id: int):
        self.__id = id


    @property
    def petrinetmodel_Place12(self):
        return self.__petrinetmodel_Place12

    @petrinetmodel_Place12.setter
    def petrinetmodel_Place12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinetmodel_Place__petrinetmodel_Place12", None)
        self.__petrinetmodel_Place12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "petrinetmodel_EdgeToPlace11"):
                opp_val = getattr(old_value, "petrinetmodel_EdgeToPlace11", None)
                if opp_val == self:
                    setattr(old_value, "petrinetmodel_EdgeToPlace11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "petrinetmodel_EdgeToPlace11"):
                opp_val = getattr(value, "petrinetmodel_EdgeToPlace11", None)
                setattr(value, "petrinetmodel_EdgeToPlace11", self)

    @property
    def petrinetmodel_Place9(self):
        return self.__petrinetmodel_Place9

    @petrinetmodel_Place9.setter
    def petrinetmodel_Place9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinetmodel_Place__petrinetmodel_Place9", None)
        self.__petrinetmodel_Place9 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "petrinetmodel_EdgeToTransaction"):
                    opp_val = getattr(item, "petrinetmodel_EdgeToTransaction", None)
                    
                    if opp_val == self:
                        setattr(item, "petrinetmodel_EdgeToTransaction", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "petrinetmodel_EdgeToTransaction"):
                    opp_val = getattr(item, "petrinetmodel_EdgeToTransaction", None)
                    
                    setattr(item, "petrinetmodel_EdgeToTransaction", self)
                    

    @property
    def petrinetmodel_Place(self):
        return self.__petrinetmodel_Place

    @petrinetmodel_Place.setter
    def petrinetmodel_Place(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinetmodel_Place__petrinetmodel_Place", None)
        self.__petrinetmodel_Place = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "petrinetmodel_Petrinet2"):
                opp_val = getattr(old_value, "petrinetmodel_Petrinet2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "petrinetmodel_Petrinet2"):
                opp_val = getattr(value, "petrinetmodel_Petrinet2", None)
                if opp_val is None:
                    setattr(value, "petrinetmodel_Petrinet2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def petrinetmodel_Place7(self):
        return self.__petrinetmodel_Place7

    @petrinetmodel_Place7.setter
    def petrinetmodel_Place7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinetmodel_Place__petrinetmodel_Place7", None)
        self.__petrinetmodel_Place7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "petrinetmodel_Transition6"):
                opp_val = getattr(old_value, "petrinetmodel_Transition6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "petrinetmodel_Transition6"):
                opp_val = getattr(value, "petrinetmodel_Transition6", None)
                if opp_val is None:
                    setattr(value, "petrinetmodel_Transition6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def hasToken(self) :
        # TODO: Implement hasToken method
        pass

    def addToken(self):
        # TODO: Implement addToken method
        pass

    def removeToken(self):
        # TODO: Implement removeToken method
        pass

    def init(self):
        # TODO: Implement init method
        pass

class petrinetmodel_Transition:

    def __init__(self, token: int, id: int, priority: int, petrinetmodel_Transition: "petrinetmodel_Petrinet" = None, petrinetmodel_Transition4: set["petrinetmodel_EdgeToPlace"] = None, petrinetmodel_Transition6: set["petrinetmodel_Place"] = None, petrinetmodel_Transition15: "petrinetmodel_EdgeToTransaction" = None):
        self.token = token
        self.id = id
        self.priority = priority
        self.petrinetmodel_Transition = petrinetmodel_Transition
        self.petrinetmodel_Transition4 = petrinetmodel_Transition4 if petrinetmodel_Transition4 is not None else set()
        self.petrinetmodel_Transition6 = petrinetmodel_Transition6 if petrinetmodel_Transition6 is not None else set()
        self.petrinetmodel_Transition15 = petrinetmodel_Transition15
        
        pass
    @property
    def priority(self):
        return self.__priority

    @priority.setter
    def priority(self, priority: int):
        self.__priority = priority


    @property
    def token(self):
        return self.__token

    @token.setter
    def token(self, token: int):
        self.__token = token


    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id: int):
        self.__id = id


    @property
    def petrinetmodel_Transition4(self):
        return self.__petrinetmodel_Transition4

    @petrinetmodel_Transition4.setter
    def petrinetmodel_Transition4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinetmodel_Transition__petrinetmodel_Transition4", None)
        self.__petrinetmodel_Transition4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "petrinetmodel_EdgeToPlace"):
                    opp_val = getattr(item, "petrinetmodel_EdgeToPlace", None)
                    
                    if opp_val == self:
                        setattr(item, "petrinetmodel_EdgeToPlace", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "petrinetmodel_EdgeToPlace"):
                    opp_val = getattr(item, "petrinetmodel_EdgeToPlace", None)
                    
                    setattr(item, "petrinetmodel_EdgeToPlace", self)
                    

    @property
    def petrinetmodel_Transition(self):
        return self.__petrinetmodel_Transition

    @petrinetmodel_Transition.setter
    def petrinetmodel_Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinetmodel_Transition__petrinetmodel_Transition", None)
        self.__petrinetmodel_Transition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "petrinetmodel_Petrinet"):
                opp_val = getattr(old_value, "petrinetmodel_Petrinet", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "petrinetmodel_Petrinet"):
                opp_val = getattr(value, "petrinetmodel_Petrinet", None)
                if opp_val is None:
                    setattr(value, "petrinetmodel_Petrinet", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def petrinetmodel_Transition6(self):
        return self.__petrinetmodel_Transition6

    @petrinetmodel_Transition6.setter
    def petrinetmodel_Transition6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinetmodel_Transition__petrinetmodel_Transition6", None)
        self.__petrinetmodel_Transition6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "petrinetmodel_Place7"):
                    opp_val = getattr(item, "petrinetmodel_Place7", None)
                    
                    if opp_val == self:
                        setattr(item, "petrinetmodel_Place7", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "petrinetmodel_Place7"):
                    opp_val = getattr(item, "petrinetmodel_Place7", None)
                    
                    setattr(item, "petrinetmodel_Place7", self)
                    

    @property
    def petrinetmodel_Transition15(self):
        return self.__petrinetmodel_Transition15

    @petrinetmodel_Transition15.setter
    def petrinetmodel_Transition15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinetmodel_Transition__petrinetmodel_Transition15", None)
        self.__petrinetmodel_Transition15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "petrinetmodel_EdgeToTransaction14"):
                opp_val = getattr(old_value, "petrinetmodel_EdgeToTransaction14", None)
                if opp_val == self:
                    setattr(old_value, "petrinetmodel_EdgeToTransaction14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "petrinetmodel_EdgeToTransaction14"):
                opp_val = getattr(value, "petrinetmodel_EdgeToTransaction14", None)
                setattr(value, "petrinetmodel_EdgeToTransaction14", self)

    def addInputPlace(self, petrinetmodel_p):
        # TODO: Implement addInputPlace method
        pass

    def fire(self):
        # TODO: Implement fire method
        pass

    def prepare(self) :
        # TODO: Implement prepare method
        pass

class petrinetmodel_Petrinet:

    def __init__(self, petrinetmodel_Petrinet: set["petrinetmodel_Transition"] = None, petrinetmodel_Petrinet2: set["petrinetmodel_Place"] = None):
        self.petrinetmodel_Petrinet = petrinetmodel_Petrinet if petrinetmodel_Petrinet is not None else set()
        self.petrinetmodel_Petrinet2 = petrinetmodel_Petrinet2 if petrinetmodel_Petrinet2 is not None else set()
        
        pass
    @property
    def petrinetmodel_Petrinet2(self):
        return self.__petrinetmodel_Petrinet2

    @petrinetmodel_Petrinet2.setter
    def petrinetmodel_Petrinet2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinetmodel_Petrinet__petrinetmodel_Petrinet2", None)
        self.__petrinetmodel_Petrinet2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "petrinetmodel_Place"):
                    opp_val = getattr(item, "petrinetmodel_Place", None)
                    
                    if opp_val == self:
                        setattr(item, "petrinetmodel_Place", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "petrinetmodel_Place"):
                    opp_val = getattr(item, "petrinetmodel_Place", None)
                    
                    setattr(item, "petrinetmodel_Place", self)
                    

    @property
    def petrinetmodel_Petrinet(self):
        return self.__petrinetmodel_Petrinet

    @petrinetmodel_Petrinet.setter
    def petrinetmodel_Petrinet(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinetmodel_Petrinet__petrinetmodel_Petrinet", None)
        self.__petrinetmodel_Petrinet = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "petrinetmodel_Transition"):
                    opp_val = getattr(item, "petrinetmodel_Transition", None)
                    
                    if opp_val == self:
                        setattr(item, "petrinetmodel_Transition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "petrinetmodel_Transition"):
                    opp_val = getattr(item, "petrinetmodel_Transition", None)
                    
                    setattr(item, "petrinetmodel_Transition", self)
                    

    def fireTransactionsByPriority(self):
        # TODO: Implement fireTransactionsByPriority method
        pass

    def init(self):
        # TODO: Implement init method
        pass
