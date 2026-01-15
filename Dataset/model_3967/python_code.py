from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class Container_Level9:

    pass
class subsetUnionDepth_Container_Level10(Container_Level9):

    pass
class Element_Level9:

    pass
class subsetUnionDepth_Element_Level10(Element_Level9):

    pass
class Container_Level8:

    pass
class subsetUnionDepth_Container_Level9(Container_Level8):

    pass
class Element_Level8:

    pass
class subsetUnionDepth_Element_Level9(Element_Level8):

    pass
class Element_Level7:

    pass
class subsetUnionDepth_Element_Level8(Element_Level7):

    pass
class Container_Level7:

    pass
class subsetUnionDepth_Container_Level8(Container_Level7):

    pass
class Container_Level6:

    pass
class subsetUnionDepth_Container_Level7(Container_Level6):

    pass
class Element_Level6:

    pass
class subsetUnionDepth_Element_Level7(Element_Level6):

    pass
class Container_Level5:

    pass
class subsetUnionDepth_Container_Level6(Container_Level5):

    pass
class Element_Level5:

    pass
class subsetUnionDepth_Element_Level6(Element_Level5):

    pass
class Element_Level4:

    pass
class subsetUnionDepth_Element_Level5(Element_Level4):

    pass
class Container_Level4:

    pass
class subsetUnionDepth_Container_Level5(Container_Level4):

    pass
class Container_Level3:

    pass
class subsetUnionDepth_Container_Level4(Container_Level3):

    pass
class Element_Level3:

    pass
class subsetUnionDepth_Element_Level4(Element_Level3):

    pass
class Container_Level2:

    pass
class subsetUnionDepth_Container_Level3(Container_Level2):

    pass
class Element_Level2:

    pass
class subsetUnionDepth_Element_Level3(Element_Level2):

    pass
class Container_Level1:

    pass
class subsetUnionDepth_Container_Level2(Container_Level1):

    pass
class Element_Level1:

    pass
class subsetUnionDepth_Element_Level2(Element_Level1):

    pass
class Container:

    pass
class subsetUnionDepth_Container_Level1(Container):

    pass
class Element:

    pass
class subsetUnionDepth_Element_Level1(Element):

    pass
class subsetUnionDepth_Element:

    def __init__(self, name: str, subsetUnionDepth_Element: "subsetUnionDepth_Container" = None):
        self.name = name
        self.subsetUnionDepth_Element = subsetUnionDepth_Element
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def subsetUnionDepth_Element(self):
        return self.__subsetUnionDepth_Element

    @subsetUnionDepth_Element.setter
    def subsetUnionDepth_Element(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_subsetUnionDepth_Element__subsetUnionDepth_Element", None)
        self.__subsetUnionDepth_Element = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "subsetUnionDepth_Container"):
                opp_val = getattr(old_value, "subsetUnionDepth_Container", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "subsetUnionDepth_Container"):
                opp_val = getattr(value, "subsetUnionDepth_Container", None)
                if opp_val is None:
                    setattr(value, "subsetUnionDepth_Container", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class subsetUnionDepth_Container:

    def __init__(self, name: str, subsetUnionDepth_Container: set["subsetUnionDepth_Element"] = None):
        self.name = name
        self.subsetUnionDepth_Container = subsetUnionDepth_Container if subsetUnionDepth_Container is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def subsetUnionDepth_Container(self):
        return self.__subsetUnionDepth_Container

    @subsetUnionDepth_Container.setter
    def subsetUnionDepth_Container(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_subsetUnionDepth_Container__subsetUnionDepth_Container", None)
        self.__subsetUnionDepth_Container = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "subsetUnionDepth_Element"):
                    opp_val = getattr(item, "subsetUnionDepth_Element", None)
                    
                    if opp_val == self:
                        setattr(item, "subsetUnionDepth_Element", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "subsetUnionDepth_Element"):
                    opp_val = getattr(item, "subsetUnionDepth_Element", None)
                    
                    setattr(item, "subsetUnionDepth_Element", self)
                    
