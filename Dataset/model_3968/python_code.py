from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class Element:

    pass
class subsetUnion_Element_Level10(Element):

    pass
class subsetUnion_Element_Level9(Element):

    pass
class subsetUnion_Element_Level8(Element):

    pass
class subsetUnion_Element_Level7(Element):

    pass
class subsetUnion_Element_Level6(Element):

    pass
class subsetUnion_Element_Level5(Element):

    pass
class subsetUnion_Element_Level4(Element):

    pass
class subsetUnion_Element_Level3(Element):

    pass
class subsetUnion_Element_Level2(Element):

    pass
class subsetUnion_Element_Level1(Element):

    pass
class subsetUnion_Element:

    def __init__(self, name: str, subsetUnion_Element: "subsetUnion_Container" = None):
        self.name = name
        self.subsetUnion_Element = subsetUnion_Element
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def subsetUnion_Element(self):
        return self.__subsetUnion_Element

    @subsetUnion_Element.setter
    def subsetUnion_Element(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_subsetUnion_Element__subsetUnion_Element", None)
        self.__subsetUnion_Element = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "subsetUnion_Container"):
                opp_val = getattr(old_value, "subsetUnion_Container", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "subsetUnion_Container"):
                opp_val = getattr(value, "subsetUnion_Container", None)
                if opp_val is None:
                    setattr(value, "subsetUnion_Container", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class subsetUnion_Container:

    def __init__(self, name: str, subsetUnion_Container: set["subsetUnion_Element"] = None, subsetUnion_Container2: set["subsetUnion_Element_Level1"] = None, subsetUnion_Container4: set["subsetUnion_Element_Level2"] = None, subsetUnion_Container6: set["subsetUnion_Element_Level3"] = None, subsetUnion_Container8: set["subsetUnion_Element_Level4"] = None, subsetUnion_Container10: set["subsetUnion_Element_Level5"] = None, subsetUnion_Container12: set["subsetUnion_Element_Level6"] = None, subsetUnion_Container14: set["subsetUnion_Element_Level7"] = None, subsetUnion_Container16: set["subsetUnion_Element_Level8"] = None, subsetUnion_Container18: set["subsetUnion_Element_Level9"] = None, subsetUnion_Container20: set["subsetUnion_Element_Level10"] = None):
        self.name = name
        self.subsetUnion_Container = subsetUnion_Container if subsetUnion_Container is not None else set()
        self.subsetUnion_Container2 = subsetUnion_Container2 if subsetUnion_Container2 is not None else set()
        self.subsetUnion_Container4 = subsetUnion_Container4 if subsetUnion_Container4 is not None else set()
        self.subsetUnion_Container6 = subsetUnion_Container6 if subsetUnion_Container6 is not None else set()
        self.subsetUnion_Container8 = subsetUnion_Container8 if subsetUnion_Container8 is not None else set()
        self.subsetUnion_Container10 = subsetUnion_Container10 if subsetUnion_Container10 is not None else set()
        self.subsetUnion_Container12 = subsetUnion_Container12 if subsetUnion_Container12 is not None else set()
        self.subsetUnion_Container14 = subsetUnion_Container14 if subsetUnion_Container14 is not None else set()
        self.subsetUnion_Container16 = subsetUnion_Container16 if subsetUnion_Container16 is not None else set()
        self.subsetUnion_Container18 = subsetUnion_Container18 if subsetUnion_Container18 is not None else set()
        self.subsetUnion_Container20 = subsetUnion_Container20 if subsetUnion_Container20 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def subsetUnion_Container6(self):
        return self.__subsetUnion_Container6

    @subsetUnion_Container6.setter
    def subsetUnion_Container6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_subsetUnion_Container__subsetUnion_Container6", None)
        self.__subsetUnion_Container6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "subsetUnion_Element_Level3"):
                    opp_val = getattr(item, "subsetUnion_Element_Level3", None)
                    
                    if opp_val == self:
                        setattr(item, "subsetUnion_Element_Level3", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "subsetUnion_Element_Level3"):
                    opp_val = getattr(item, "subsetUnion_Element_Level3", None)
                    
                    setattr(item, "subsetUnion_Element_Level3", self)
                    

    @property
    def subsetUnion_Container4(self):
        return self.__subsetUnion_Container4

    @subsetUnion_Container4.setter
    def subsetUnion_Container4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_subsetUnion_Container__subsetUnion_Container4", None)
        self.__subsetUnion_Container4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "subsetUnion_Element_Level2"):
                    opp_val = getattr(item, "subsetUnion_Element_Level2", None)
                    
                    if opp_val == self:
                        setattr(item, "subsetUnion_Element_Level2", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "subsetUnion_Element_Level2"):
                    opp_val = getattr(item, "subsetUnion_Element_Level2", None)
                    
                    setattr(item, "subsetUnion_Element_Level2", self)
                    

    @property
    def subsetUnion_Container12(self):
        return self.__subsetUnion_Container12

    @subsetUnion_Container12.setter
    def subsetUnion_Container12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_subsetUnion_Container__subsetUnion_Container12", None)
        self.__subsetUnion_Container12 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "subsetUnion_Element_Level6"):
                    opp_val = getattr(item, "subsetUnion_Element_Level6", None)
                    
                    if opp_val == self:
                        setattr(item, "subsetUnion_Element_Level6", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "subsetUnion_Element_Level6"):
                    opp_val = getattr(item, "subsetUnion_Element_Level6", None)
                    
                    setattr(item, "subsetUnion_Element_Level6", self)
                    

    @property
    def subsetUnion_Container10(self):
        return self.__subsetUnion_Container10

    @subsetUnion_Container10.setter
    def subsetUnion_Container10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_subsetUnion_Container__subsetUnion_Container10", None)
        self.__subsetUnion_Container10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "subsetUnion_Element_Level5"):
                    opp_val = getattr(item, "subsetUnion_Element_Level5", None)
                    
                    if opp_val == self:
                        setattr(item, "subsetUnion_Element_Level5", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "subsetUnion_Element_Level5"):
                    opp_val = getattr(item, "subsetUnion_Element_Level5", None)
                    
                    setattr(item, "subsetUnion_Element_Level5", self)
                    

    @property
    def subsetUnion_Container20(self):
        return self.__subsetUnion_Container20

    @subsetUnion_Container20.setter
    def subsetUnion_Container20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_subsetUnion_Container__subsetUnion_Container20", None)
        self.__subsetUnion_Container20 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "subsetUnion_Element_Level10"):
                    opp_val = getattr(item, "subsetUnion_Element_Level10", None)
                    
                    if opp_val == self:
                        setattr(item, "subsetUnion_Element_Level10", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "subsetUnion_Element_Level10"):
                    opp_val = getattr(item, "subsetUnion_Element_Level10", None)
                    
                    setattr(item, "subsetUnion_Element_Level10", self)
                    

    @property
    def subsetUnion_Container8(self):
        return self.__subsetUnion_Container8

    @subsetUnion_Container8.setter
    def subsetUnion_Container8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_subsetUnion_Container__subsetUnion_Container8", None)
        self.__subsetUnion_Container8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "subsetUnion_Element_Level4"):
                    opp_val = getattr(item, "subsetUnion_Element_Level4", None)
                    
                    if opp_val == self:
                        setattr(item, "subsetUnion_Element_Level4", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "subsetUnion_Element_Level4"):
                    opp_val = getattr(item, "subsetUnion_Element_Level4", None)
                    
                    setattr(item, "subsetUnion_Element_Level4", self)
                    

    @property
    def subsetUnion_Container16(self):
        return self.__subsetUnion_Container16

    @subsetUnion_Container16.setter
    def subsetUnion_Container16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_subsetUnion_Container__subsetUnion_Container16", None)
        self.__subsetUnion_Container16 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "subsetUnion_Element_Level8"):
                    opp_val = getattr(item, "subsetUnion_Element_Level8", None)
                    
                    if opp_val == self:
                        setattr(item, "subsetUnion_Element_Level8", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "subsetUnion_Element_Level8"):
                    opp_val = getattr(item, "subsetUnion_Element_Level8", None)
                    
                    setattr(item, "subsetUnion_Element_Level8", self)
                    

    @property
    def subsetUnion_Container18(self):
        return self.__subsetUnion_Container18

    @subsetUnion_Container18.setter
    def subsetUnion_Container18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_subsetUnion_Container__subsetUnion_Container18", None)
        self.__subsetUnion_Container18 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "subsetUnion_Element_Level9"):
                    opp_val = getattr(item, "subsetUnion_Element_Level9", None)
                    
                    if opp_val == self:
                        setattr(item, "subsetUnion_Element_Level9", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "subsetUnion_Element_Level9"):
                    opp_val = getattr(item, "subsetUnion_Element_Level9", None)
                    
                    setattr(item, "subsetUnion_Element_Level9", self)
                    

    @property
    def subsetUnion_Container(self):
        return self.__subsetUnion_Container

    @subsetUnion_Container.setter
    def subsetUnion_Container(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_subsetUnion_Container__subsetUnion_Container", None)
        self.__subsetUnion_Container = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "subsetUnion_Element"):
                    opp_val = getattr(item, "subsetUnion_Element", None)
                    
                    if opp_val == self:
                        setattr(item, "subsetUnion_Element", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "subsetUnion_Element"):
                    opp_val = getattr(item, "subsetUnion_Element", None)
                    
                    setattr(item, "subsetUnion_Element", self)
                    

    @property
    def subsetUnion_Container14(self):
        return self.__subsetUnion_Container14

    @subsetUnion_Container14.setter
    def subsetUnion_Container14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_subsetUnion_Container__subsetUnion_Container14", None)
        self.__subsetUnion_Container14 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "subsetUnion_Element_Level7"):
                    opp_val = getattr(item, "subsetUnion_Element_Level7", None)
                    
                    if opp_val == self:
                        setattr(item, "subsetUnion_Element_Level7", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "subsetUnion_Element_Level7"):
                    opp_val = getattr(item, "subsetUnion_Element_Level7", None)
                    
                    setattr(item, "subsetUnion_Element_Level7", self)
                    

    @property
    def subsetUnion_Container2(self):
        return self.__subsetUnion_Container2

    @subsetUnion_Container2.setter
    def subsetUnion_Container2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_subsetUnion_Container__subsetUnion_Container2", None)
        self.__subsetUnion_Container2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "subsetUnion_Element_Level1"):
                    opp_val = getattr(item, "subsetUnion_Element_Level1", None)
                    
                    if opp_val == self:
                        setattr(item, "subsetUnion_Element_Level1", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "subsetUnion_Element_Level1"):
                    opp_val = getattr(item, "subsetUnion_Element_Level1", None)
                    
                    setattr(item, "subsetUnion_Element_Level1", self)
                    
