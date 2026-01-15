from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class TreeElement:

    pass
class edd_Leaf(TreeElement):

    pass
class edd_Node(TreeElement):

    pass
class edd_TreeElement:

    def __init__(self, index: str, name: str, edd_TreeElement: "edd_EDD" = None, edd_TreeElement2: "edd_Node" = None):
        self.index = index
        self.name = name
        self.edd_TreeElement = edd_TreeElement
        self.edd_TreeElement2 = edd_TreeElement2
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def index(self) -> str:
        return self.__index

    @index.setter
    def index(self, index: str):
        self.__index = index

    @property
    def edd_TreeElement(self):
        return self.__edd_TreeElement

    @edd_TreeElement.setter
    def edd_TreeElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_edd_TreeElement__edd_TreeElement", None)
        self.__edd_TreeElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "edd_EDD"):
                opp_val = getattr(old_value, "edd_EDD", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "edd_EDD"):
                opp_val = getattr(value, "edd_EDD", None)
                if opp_val is None:
                    setattr(value, "edd_EDD", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def edd_TreeElement2(self):
        return self.__edd_TreeElement2

    @edd_TreeElement2.setter
    def edd_TreeElement2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_edd_TreeElement__edd_TreeElement2", None)
        self.__edd_TreeElement2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "edd_Node"):
                opp_val = getattr(old_value, "edd_Node", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "edd_Node"):
                opp_val = getattr(value, "edd_Node", None)
                if opp_val is None:
                    setattr(value, "edd_Node", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class edd_EDD:

    def __init__(self, name: str, edd_EDD: set["edd_TreeElement"] = None):
        self.name = name
        self.edd_EDD = edd_EDD if edd_EDD is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def edd_EDD(self):
        return self.__edd_EDD

    @edd_EDD.setter
    def edd_EDD(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_edd_EDD__edd_EDD", None)
        self.__edd_EDD = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "edd_TreeElement"):
                    opp_val = getattr(item, "edd_TreeElement", None)
                    
                    if opp_val == self:
                        setattr(item, "edd_TreeElement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "edd_TreeElement"):
                    opp_val = getattr(item, "edd_TreeElement", None)
                    
                    setattr(item, "edd_TreeElement", self)
                    
