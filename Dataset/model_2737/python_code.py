from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class TypeB_CDescription:

    def __init__(self, description: str, TypeB_CDescription: "TypeB_C" = None):
        self.description = description
        self.TypeB_CDescription = TypeB_CDescription
        
    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def TypeB_CDescription(self):
        return self.__TypeB_CDescription

    @TypeB_CDescription.setter
    def TypeB_CDescription(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_TypeB_CDescription__TypeB_CDescription", None)
        self.__TypeB_CDescription = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "TypeB_C10"):
                opp_val = getattr(old_value, "TypeB_C10", None)
                if opp_val == self:
                    setattr(old_value, "TypeB_C10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "TypeB_C10"):
                opp_val = getattr(value, "TypeB_C10", None)
                setattr(value, "TypeB_C10", self)

class TypeB_BDescription1:

    def __init__(self, description: str, TypeB_BDescription1: "TypeB_B" = None):
        self.description = description
        self.TypeB_BDescription1 = TypeB_BDescription1
        
    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def TypeB_BDescription1(self):
        return self.__TypeB_BDescription1

    @TypeB_BDescription1.setter
    def TypeB_BDescription1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_TypeB_BDescription1__TypeB_BDescription1", None)
        self.__TypeB_BDescription1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "TypeB_B4"):
                opp_val = getattr(old_value, "TypeB_B4", None)
                if opp_val == self:
                    setattr(old_value, "TypeB_B4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "TypeB_B4"):
                opp_val = getattr(value, "TypeB_B4", None)
                setattr(value, "TypeB_B4", self)

class TypeB_C:

    def __init__(self, name: str, TypeB_C: "TypeB_A" = None, TypeB_C10: "TypeB_CDescription" = None):
        self.name = name
        self.TypeB_C = TypeB_C
        self.TypeB_C10 = TypeB_C10
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def TypeB_C10(self):
        return self.__TypeB_C10

    @TypeB_C10.setter
    def TypeB_C10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_TypeB_C__TypeB_C10", None)
        self.__TypeB_C10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "TypeB_CDescription"):
                opp_val = getattr(old_value, "TypeB_CDescription", None)
                if opp_val == self:
                    setattr(old_value, "TypeB_CDescription", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "TypeB_CDescription"):
                opp_val = getattr(value, "TypeB_CDescription", None)
                setattr(value, "TypeB_CDescription", self)

    @property
    def TypeB_C(self):
        return self.__TypeB_C

    @TypeB_C.setter
    def TypeB_C(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_TypeB_C__TypeB_C", None)
        self.__TypeB_C = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "TypeB_A2"):
                opp_val = getattr(old_value, "TypeB_A2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "TypeB_A2"):
                opp_val = getattr(value, "TypeB_A2", None)
                if opp_val is None:
                    setattr(value, "TypeB_A2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class TypeB_B:

    def __init__(self, name: str, TypeB_B4: "TypeB_BDescription1" = None, TypeB_B6: "TypeB_BDescription2" = None, TypeB_B8: "TypeB_BDescription3" = None, TypeB_B: "TypeB_A" = None):
        self.name = name
        self.TypeB_B4 = TypeB_B4
        self.TypeB_B6 = TypeB_B6
        self.TypeB_B8 = TypeB_B8
        self.TypeB_B = TypeB_B
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def TypeB_B4(self):
        return self.__TypeB_B4

    @TypeB_B4.setter
    def TypeB_B4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_TypeB_B__TypeB_B4", None)
        self.__TypeB_B4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "TypeB_BDescription1"):
                opp_val = getattr(old_value, "TypeB_BDescription1", None)
                if opp_val == self:
                    setattr(old_value, "TypeB_BDescription1", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "TypeB_BDescription1"):
                opp_val = getattr(value, "TypeB_BDescription1", None)
                setattr(value, "TypeB_BDescription1", self)

    @property
    def TypeB_B(self):
        return self.__TypeB_B

    @TypeB_B.setter
    def TypeB_B(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_TypeB_B__TypeB_B", None)
        self.__TypeB_B = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "TypeB_A"):
                opp_val = getattr(old_value, "TypeB_A", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "TypeB_A"):
                opp_val = getattr(value, "TypeB_A", None)
                if opp_val is None:
                    setattr(value, "TypeB_A", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def TypeB_B6(self):
        return self.__TypeB_B6

    @TypeB_B6.setter
    def TypeB_B6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_TypeB_B__TypeB_B6", None)
        self.__TypeB_B6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "TypeB_BDescription2"):
                opp_val = getattr(old_value, "TypeB_BDescription2", None)
                if opp_val == self:
                    setattr(old_value, "TypeB_BDescription2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "TypeB_BDescription2"):
                opp_val = getattr(value, "TypeB_BDescription2", None)
                setattr(value, "TypeB_BDescription2", self)

    @property
    def TypeB_B8(self):
        return self.__TypeB_B8

    @TypeB_B8.setter
    def TypeB_B8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_TypeB_B__TypeB_B8", None)
        self.__TypeB_B8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "TypeB_BDescription3"):
                opp_val = getattr(old_value, "TypeB_BDescription3", None)
                if opp_val == self:
                    setattr(old_value, "TypeB_BDescription3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "TypeB_BDescription3"):
                opp_val = getattr(value, "TypeB_BDescription3", None)
                setattr(value, "TypeB_BDescription3", self)

class TypeB_A:

    def __init__(self, name: str, TypeB_A: set["TypeB_B"] = None, TypeB_A2: set["TypeB_C"] = None):
        self.name = name
        self.TypeB_A = TypeB_A if TypeB_A is not None else set()
        self.TypeB_A2 = TypeB_A2 if TypeB_A2 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def TypeB_A2(self):
        return self.__TypeB_A2

    @TypeB_A2.setter
    def TypeB_A2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_TypeB_A__TypeB_A2", None)
        self.__TypeB_A2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "TypeB_C"):
                    opp_val = getattr(item, "TypeB_C", None)
                    
                    if opp_val == self:
                        setattr(item, "TypeB_C", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "TypeB_C"):
                    opp_val = getattr(item, "TypeB_C", None)
                    
                    setattr(item, "TypeB_C", self)
                    

    @property
    def TypeB_A(self):
        return self.__TypeB_A

    @TypeB_A.setter
    def TypeB_A(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_TypeB_A__TypeB_A", None)
        self.__TypeB_A = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "TypeB_B"):
                    opp_val = getattr(item, "TypeB_B", None)
                    
                    if opp_val == self:
                        setattr(item, "TypeB_B", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "TypeB_B"):
                    opp_val = getattr(item, "TypeB_B", None)
                    
                    setattr(item, "TypeB_B", self)
                    

class TypeB_BDescription3:

    def __init__(self, description: str, TypeB_BDescription3: "TypeB_B" = None):
        self.description = description
        self.TypeB_BDescription3 = TypeB_BDescription3
        
    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def TypeB_BDescription3(self):
        return self.__TypeB_BDescription3

    @TypeB_BDescription3.setter
    def TypeB_BDescription3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_TypeB_BDescription3__TypeB_BDescription3", None)
        self.__TypeB_BDescription3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "TypeB_B8"):
                opp_val = getattr(old_value, "TypeB_B8", None)
                if opp_val == self:
                    setattr(old_value, "TypeB_B8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "TypeB_B8"):
                opp_val = getattr(value, "TypeB_B8", None)
                setattr(value, "TypeB_B8", self)

class TypeB_BDescription2:

    def __init__(self, description: str, TypeB_BDescription2: "TypeB_B" = None):
        self.description = description
        self.TypeB_BDescription2 = TypeB_BDescription2
        
    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def TypeB_BDescription2(self):
        return self.__TypeB_BDescription2

    @TypeB_BDescription2.setter
    def TypeB_BDescription2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_TypeB_BDescription2__TypeB_BDescription2", None)
        self.__TypeB_BDescription2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "TypeB_B6"):
                opp_val = getattr(old_value, "TypeB_B6", None)
                if opp_val == self:
                    setattr(old_value, "TypeB_B6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "TypeB_B6"):
                opp_val = getattr(value, "TypeB_B6", None)
                setattr(value, "TypeB_B6", self)
