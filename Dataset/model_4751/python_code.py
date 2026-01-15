from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class edd_TreeElement:

    def __init__(self, index: str, name: str, edd_TreeElement7: "edd_Block" = None, edd_TreeElement: "edd_TreeElement" = None, edd_TreeElement3: set["edd_TreeElement"] = None):
        self.index = index
        self.name = name
        self.edd_TreeElement7 = edd_TreeElement7
        self.edd_TreeElement = edd_TreeElement
        self.edd_TreeElement3 = edd_TreeElement3 if edd_TreeElement3 is not None else set()
        
    @property
    def index(self) -> str:
        return self.__index

    @index.setter
    def index(self, index: str):
        self.__index = index

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def edd_TreeElement7(self):
        return self.__edd_TreeElement7

    @edd_TreeElement7.setter
    def edd_TreeElement7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_edd_TreeElement__edd_TreeElement7", None)
        self.__edd_TreeElement7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "edd_Block6"):
                opp_val = getattr(old_value, "edd_Block6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "edd_Block6"):
                opp_val = getattr(value, "edd_Block6", None)
                if opp_val is None:
                    setattr(value, "edd_Block6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

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
            if hasattr(old_value, "edd_TreeElement3"):
                opp_val = getattr(old_value, "edd_TreeElement3", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "edd_TreeElement3"):
                opp_val = getattr(value, "edd_TreeElement3", None)
                if opp_val is None:
                    setattr(value, "edd_TreeElement3", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def edd_TreeElement3(self):
        return self.__edd_TreeElement3

    @edd_TreeElement3.setter
    def edd_TreeElement3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_edd_TreeElement__edd_TreeElement3", None)
        self.__edd_TreeElement3 = value if value is not None else set()
        
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
                    

    def validate(self) -> bool:
        # TODO: Implement validate method
        pass

class edd_Block:

    def __init__(self, name: str, edd_Block6: set["edd_TreeElement"] = None, edd_Block: "edd_Model" = None):
        self.name = name
        self.edd_Block6 = edd_Block6 if edd_Block6 is not None else set()
        self.edd_Block = edd_Block
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def edd_Block6(self):
        return self.__edd_Block6

    @edd_Block6.setter
    def edd_Block6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_edd_Block__edd_Block6", None)
        self.__edd_Block6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "edd_TreeElement7"):
                    opp_val = getattr(item, "edd_TreeElement7", None)
                    
                    if opp_val == self:
                        setattr(item, "edd_TreeElement7", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "edd_TreeElement7"):
                    opp_val = getattr(item, "edd_TreeElement7", None)
                    
                    setattr(item, "edd_TreeElement7", self)
                    

    @property
    def edd_Block(self):
        return self.__edd_Block

    @edd_Block.setter
    def edd_Block(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_edd_Block__edd_Block", None)
        self.__edd_Block = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "edd_Model2"):
                opp_val = getattr(old_value, "edd_Model2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "edd_Model2"):
                opp_val = getattr(value, "edd_Model2", None)
                if opp_val is None:
                    setattr(value, "edd_Model2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def validate(self) -> bool:
        # TODO: Implement validate method
        pass

class edd_Model:

    def __init__(self, name: str, edd_Model: "edd_Diagram" = None, edd_Model2: set["edd_Block"] = None):
        self.name = name
        self.edd_Model = edd_Model
        self.edd_Model2 = edd_Model2 if edd_Model2 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def edd_Model(self):
        return self.__edd_Model

    @edd_Model.setter
    def edd_Model(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_edd_Model__edd_Model", None)
        self.__edd_Model = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "edd_Diagram"):
                opp_val = getattr(old_value, "edd_Diagram", None)
                if opp_val == self:
                    setattr(old_value, "edd_Diagram", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "edd_Diagram"):
                opp_val = getattr(value, "edd_Diagram", None)
                setattr(value, "edd_Diagram", self)

    @property
    def edd_Model2(self):
        return self.__edd_Model2

    @edd_Model2.setter
    def edd_Model2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_edd_Model__edd_Model2", None)
        self.__edd_Model2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "edd_Block"):
                    opp_val = getattr(item, "edd_Block", None)
                    
                    if opp_val == self:
                        setattr(item, "edd_Block", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "edd_Block"):
                    opp_val = getattr(item, "edd_Block", None)
                    
                    setattr(item, "edd_Block", self)
                    

class edd_Diagram:

    pass