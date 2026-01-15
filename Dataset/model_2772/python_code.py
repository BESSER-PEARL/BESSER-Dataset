from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class nestedgroup_Element:

    def __init__(self, mixed: str, name: str, true: str, nestedgroup_Element: set["nestedgroup_CType"] = None, nestedgroup_Element5: "nestedgroup_Element" = None, nestedgroup_Element3: "nestedgroup_Element" = None):
        self.mixed = mixed
        self.name = name
        self.true = true
        self.nestedgroup_Element = nestedgroup_Element if nestedgroup_Element is not None else set()
        self.nestedgroup_Element5 = nestedgroup_Element5
        self.nestedgroup_Element3 = nestedgroup_Element3
        
    @property
    def true(self) -> str:
        return self.__true

    @true.setter
    def true(self, true: str):
        self.__true = true

    @property
    def mixed(self) -> str:
        return self.__mixed

    @mixed.setter
    def mixed(self, mixed: str):
        self.__mixed = mixed

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def nestedgroup_Element5(self):
        return self.__nestedgroup_Element5

    @nestedgroup_Element5.setter
    def nestedgroup_Element5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_nestedgroup_Element__nestedgroup_Element5", None)
        self.__nestedgroup_Element5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "nestedgroup_Element3"):
                opp_val = getattr(old_value, "nestedgroup_Element3", None)
                if opp_val == self:
                    setattr(old_value, "nestedgroup_Element3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "nestedgroup_Element3"):
                opp_val = getattr(value, "nestedgroup_Element3", None)
                setattr(value, "nestedgroup_Element3", self)

    @property
    def nestedgroup_Element(self):
        return self.__nestedgroup_Element

    @nestedgroup_Element.setter
    def nestedgroup_Element(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_nestedgroup_Element__nestedgroup_Element", None)
        self.__nestedgroup_Element = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "nestedgroup_CType2"):
                    opp_val = getattr(item, "nestedgroup_CType2", None)
                    
                    if opp_val == self:
                        setattr(item, "nestedgroup_CType2", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "nestedgroup_CType2"):
                    opp_val = getattr(item, "nestedgroup_CType2", None)
                    
                    setattr(item, "nestedgroup_CType2", self)
                    

    @property
    def nestedgroup_Element3(self):
        return self.__nestedgroup_Element3

    @nestedgroup_Element3.setter
    def nestedgroup_Element3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_nestedgroup_Element__nestedgroup_Element3", None)
        self.__nestedgroup_Element3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "nestedgroup_Element5"):
                opp_val = getattr(old_value, "nestedgroup_Element5", None)
                if opp_val == self:
                    setattr(old_value, "nestedgroup_Element5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "nestedgroup_Element5"):
                opp_val = getattr(value, "nestedgroup_Element5", None)
                setattr(value, "nestedgroup_Element5", self)

class nestedgroup_CType:

    def __init__(self, cname: str, cvalue: str, nestedgroup_CType: "nestedgroup_A" = None, nestedgroup_CType2: "nestedgroup_Element" = None):
        self.cname = cname
        self.cvalue = cvalue
        self.nestedgroup_CType = nestedgroup_CType
        self.nestedgroup_CType2 = nestedgroup_CType2
        
    @property
    def cvalue(self) -> str:
        return self.__cvalue

    @cvalue.setter
    def cvalue(self, cvalue: str):
        self.__cvalue = cvalue

    @property
    def cname(self) -> str:
        return self.__cname

    @cname.setter
    def cname(self, cname: str):
        self.__cname = cname

    @property
    def nestedgroup_CType2(self):
        return self.__nestedgroup_CType2

    @nestedgroup_CType2.setter
    def nestedgroup_CType2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_nestedgroup_CType__nestedgroup_CType2", None)
        self.__nestedgroup_CType2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "nestedgroup_Element"):
                opp_val = getattr(old_value, "nestedgroup_Element", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "nestedgroup_Element"):
                opp_val = getattr(value, "nestedgroup_Element", None)
                if opp_val is None:
                    setattr(value, "nestedgroup_Element", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def nestedgroup_CType(self):
        return self.__nestedgroup_CType

    @nestedgroup_CType.setter
    def nestedgroup_CType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_nestedgroup_CType__nestedgroup_CType", None)
        self.__nestedgroup_CType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "nestedgroup_A"):
                opp_val = getattr(old_value, "nestedgroup_A", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "nestedgroup_A"):
                opp_val = getattr(value, "nestedgroup_A", None)
                if opp_val is None:
                    setattr(value, "nestedgroup_A", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class nestedgroup_A:

    def __init__(self, group: str, b: str, name: str, nestedgroup_A: set["nestedgroup_CType"] = None):
        self.group = group
        self.b = b
        self.name = name
        self.nestedgroup_A = nestedgroup_A if nestedgroup_A is not None else set()
        
    @property
    def group(self) -> str:
        return self.__group

    @group.setter
    def group(self, group: str):
        self.__group = group

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def b(self) -> str:
        return self.__b

    @b.setter
    def b(self, b: str):
        self.__b = b

    @property
    def nestedgroup_A(self):
        return self.__nestedgroup_A

    @nestedgroup_A.setter
    def nestedgroup_A(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_nestedgroup_A__nestedgroup_A", None)
        self.__nestedgroup_A = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "nestedgroup_CType"):
                    opp_val = getattr(item, "nestedgroup_CType", None)
                    
                    if opp_val == self:
                        setattr(item, "nestedgroup_CType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "nestedgroup_CType"):
                    opp_val = getattr(item, "nestedgroup_CType", None)
                    
                    setattr(item, "nestedgroup_CType", self)
                    
