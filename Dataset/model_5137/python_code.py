from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class a_Root:

    def __init__(self, visible: bool, a_Root: "a_A" = None, a_Root2: set["a_A"] = None, a_Root5: set["a_B"] = None):
        self.visible = visible
        self.a_Root = a_Root
        self.a_Root2 = a_Root2 if a_Root2 is not None else set()
        self.a_Root5 = a_Root5 if a_Root5 is not None else set()
        
    @property
    def visible(self) -> bool:
        return self.__visible

    @visible.setter
    def visible(self, visible: bool):
        self.__visible = visible

    @property
    def a_Root5(self):
        return self.__a_Root5

    @a_Root5.setter
    def a_Root5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_a_Root__a_Root5", None)
        self.__a_Root5 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "a_B"):
                    opp_val = getattr(item, "a_B", None)
                    
                    if opp_val == self:
                        setattr(item, "a_B", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "a_B"):
                    opp_val = getattr(item, "a_B", None)
                    
                    setattr(item, "a_B", self)
                    

    @property
    def a_Root2(self):
        return self.__a_Root2

    @a_Root2.setter
    def a_Root2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_a_Root__a_Root2", None)
        self.__a_Root2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "a_A3"):
                    opp_val = getattr(item, "a_A3", None)
                    
                    if opp_val == self:
                        setattr(item, "a_A3", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "a_A3"):
                    opp_val = getattr(item, "a_A3", None)
                    
                    setattr(item, "a_A3", self)
                    

    @property
    def a_Root(self):
        return self.__a_Root

    @a_Root.setter
    def a_Root(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_a_Root__a_Root", None)
        self.__a_Root = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "a_A"):
                opp_val = getattr(old_value, "a_A", None)
                if opp_val == self:
                    setattr(old_value, "a_A", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "a_A"):
                opp_val = getattr(value, "a_A", None)
                setattr(value, "a_A", self)

class SuperStuff2:

    pass
class SuperStuff:

    pass
class a_A(SuperStuff, SuperStuff2):

    pass
class a_B:

    def __init__(self, name: str, nameID: str, a_B: "a_Root" = None, a_B8: "a_A" = None):
        self.name = name
        self.nameID = nameID
        self.a_B = a_B
        self.a_B8 = a_B8
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def nameID(self) -> str:
        return self.__nameID

    @nameID.setter
    def nameID(self, nameID: str):
        self.__nameID = nameID

    @property
    def a_B(self):
        return self.__a_B

    @a_B.setter
    def a_B(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_a_B__a_B", None)
        self.__a_B = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "a_Root5"):
                opp_val = getattr(old_value, "a_Root5", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "a_Root5"):
                opp_val = getattr(value, "a_Root5", None)
                if opp_val is None:
                    setattr(value, "a_Root5", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def a_B8(self):
        return self.__a_B8

    @a_B8.setter
    def a_B8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_a_B__a_B8", None)
        self.__a_B8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "a_A7"):
                opp_val = getattr(old_value, "a_A7", None)
                if opp_val == self:
                    setattr(old_value, "a_A7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "a_A7"):
                opp_val = getattr(value, "a_A7", None)
                setattr(value, "a_A7", self)
