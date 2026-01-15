from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class MTpre__Element:

    pass
class ramRoot_MTpre__Chair(MTpre__Element):

    def __init__(self, MTpre__order: str, ramRoot_MTpre__Chair: "ramRoot_MTpre__Table" = None):
        self.MTpre__order = MTpre__order
        self.ramRoot_MTpre__Chair = ramRoot_MTpre__Chair
        
    @property
    def MTpre__order(self) -> str:
        return self.__MTpre__order

    @MTpre__order.setter
    def MTpre__order(self, MTpre__order: str):
        self.__MTpre__order = MTpre__order

    @property
    def ramRoot_MTpre__Chair(self):
        return self.__ramRoot_MTpre__Chair

    @ramRoot_MTpre__Chair.setter
    def ramRoot_MTpre__Chair(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ramRoot_MTpre__Chair__ramRoot_MTpre__Chair", None)
        self.__ramRoot_MTpre__Chair = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ramRoot_MTpre__Table"):
                opp_val = getattr(old_value, "ramRoot_MTpre__Table", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ramRoot_MTpre__Table"):
                opp_val = getattr(value, "ramRoot_MTpre__Table", None)
                if opp_val is None:
                    setattr(value, "ramRoot_MTpre__Table", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class ramRoot_MTpre__Table(MTpre__Element):

    def __init__(self, MTpre__id: str, MTpre__isReserved: str, ramRoot_MTpre__Table6: "ramRoot_MTpre__Waitress" = None, ramRoot_MTpre__Table8: "ramRoot_MTpre__Restaurant" = None, ramRoot_MTpre__Table: set["ramRoot_MTpre__Chair"] = None):
        self.MTpre__id = MTpre__id
        self.MTpre__isReserved = MTpre__isReserved
        self.ramRoot_MTpre__Table6 = ramRoot_MTpre__Table6
        self.ramRoot_MTpre__Table8 = ramRoot_MTpre__Table8
        self.ramRoot_MTpre__Table = ramRoot_MTpre__Table if ramRoot_MTpre__Table is not None else set()
        
    @property
    def MTpre__isReserved(self) -> str:
        return self.__MTpre__isReserved

    @MTpre__isReserved.setter
    def MTpre__isReserved(self, MTpre__isReserved: str):
        self.__MTpre__isReserved = MTpre__isReserved

    @property
    def MTpre__id(self) -> str:
        return self.__MTpre__id

    @MTpre__id.setter
    def MTpre__id(self, MTpre__id: str):
        self.__MTpre__id = MTpre__id

    @property
    def ramRoot_MTpre__Table(self):
        return self.__ramRoot_MTpre__Table

    @ramRoot_MTpre__Table.setter
    def ramRoot_MTpre__Table(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ramRoot_MTpre__Table__ramRoot_MTpre__Table", None)
        self.__ramRoot_MTpre__Table = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ramRoot_MTpre__Chair"):
                    opp_val = getattr(item, "ramRoot_MTpre__Chair", None)
                    
                    if opp_val == self:
                        setattr(item, "ramRoot_MTpre__Chair", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ramRoot_MTpre__Chair"):
                    opp_val = getattr(item, "ramRoot_MTpre__Chair", None)
                    
                    setattr(item, "ramRoot_MTpre__Chair", self)
                    

    @property
    def ramRoot_MTpre__Table8(self):
        return self.__ramRoot_MTpre__Table8

    @ramRoot_MTpre__Table8.setter
    def ramRoot_MTpre__Table8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ramRoot_MTpre__Table__ramRoot_MTpre__Table8", None)
        self.__ramRoot_MTpre__Table8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ramRoot_MTpre__Restaurant"):
                opp_val = getattr(old_value, "ramRoot_MTpre__Restaurant", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ramRoot_MTpre__Restaurant"):
                opp_val = getattr(value, "ramRoot_MTpre__Restaurant", None)
                if opp_val is None:
                    setattr(value, "ramRoot_MTpre__Restaurant", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ramRoot_MTpre__Table6(self):
        return self.__ramRoot_MTpre__Table6

    @ramRoot_MTpre__Table6.setter
    def ramRoot_MTpre__Table6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ramRoot_MTpre__Table__ramRoot_MTpre__Table6", None)
        self.__ramRoot_MTpre__Table6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ramRoot_MTpre__Waitress"):
                opp_val = getattr(old_value, "ramRoot_MTpre__Waitress", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ramRoot_MTpre__Waitress"):
                opp_val = getattr(value, "ramRoot_MTpre__Waitress", None)
                if opp_val is None:
                    setattr(value, "ramRoot_MTpre__Waitress", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class ramRoot_MTpre__Restaurant(MTpre__Element):

    pass
class ramRoot_MTpre__Waitress(MTpre__Element):

    def __init__(self, MTpre__name: str, ramRoot_MTpre__Waitress: set["ramRoot_MTpre__Table"] = None, ramRoot_MTpre__Waitress11: "ramRoot_MTpre__Restaurant" = None):
        self.MTpre__name = MTpre__name
        self.ramRoot_MTpre__Waitress = ramRoot_MTpre__Waitress if ramRoot_MTpre__Waitress is not None else set()
        self.ramRoot_MTpre__Waitress11 = ramRoot_MTpre__Waitress11
        
    @property
    def MTpre__name(self) -> str:
        return self.__MTpre__name

    @MTpre__name.setter
    def MTpre__name(self, MTpre__name: str):
        self.__MTpre__name = MTpre__name

    @property
    def ramRoot_MTpre__Waitress(self):
        return self.__ramRoot_MTpre__Waitress

    @ramRoot_MTpre__Waitress.setter
    def ramRoot_MTpre__Waitress(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ramRoot_MTpre__Waitress__ramRoot_MTpre__Waitress", None)
        self.__ramRoot_MTpre__Waitress = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ramRoot_MTpre__Table6"):
                    opp_val = getattr(item, "ramRoot_MTpre__Table6", None)
                    
                    if opp_val == self:
                        setattr(item, "ramRoot_MTpre__Table6", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ramRoot_MTpre__Table6"):
                    opp_val = getattr(item, "ramRoot_MTpre__Table6", None)
                    
                    setattr(item, "ramRoot_MTpre__Table6", self)
                    

    @property
    def ramRoot_MTpre__Waitress11(self):
        return self.__ramRoot_MTpre__Waitress11

    @ramRoot_MTpre__Waitress11.setter
    def ramRoot_MTpre__Waitress11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ramRoot_MTpre__Waitress__ramRoot_MTpre__Waitress11", None)
        self.__ramRoot_MTpre__Waitress11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ramRoot_MTpre__Restaurant10"):
                opp_val = getattr(old_value, "ramRoot_MTpre__Restaurant10", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ramRoot_MTpre__Restaurant10"):
                opp_val = getattr(value, "ramRoot_MTpre__Restaurant10", None)
                if opp_val is None:
                    setattr(value, "ramRoot_MTpre__Restaurant10", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class MT__Element:

    pass
class ramRoot_MTpre__Element(MT__Element):

    def __init__(self, MT__matchSubtype: bool):
        self.MT__matchSubtype = MT__matchSubtype
        
    @property
    def MT__matchSubtype(self) -> bool:
        return self.__MT__matchSubtype

    @MT__matchSubtype.setter
    def MT__matchSubtype(self, MT__matchSubtype: bool):
        self.__MT__matchSubtype = MT__matchSubtype

class ramRoot_GenericNode(MT__Element):

    pass
class ramRoot_MTpos__Element(MT__Element):

    pass
class ramRoot_MT__Element(ABC):

    def __init__(self, MT__label: str, MT__isProcessed: bool, ramRoot_MT__Element: "ramRoot_GenericNode" = None):
        self.MT__label = MT__label
        self.MT__isProcessed = MT__isProcessed
        self.ramRoot_MT__Element = ramRoot_MT__Element
        
    @property
    def MT__label(self) -> str:
        return self.__MT__label

    @MT__label.setter
    def MT__label(self, MT__label: str):
        self.__MT__label = MT__label

    @property
    def MT__isProcessed(self) -> bool:
        return self.__MT__isProcessed

    @MT__isProcessed.setter
    def MT__isProcessed(self, MT__isProcessed: bool):
        self.__MT__isProcessed = MT__isProcessed

    @property
    def ramRoot_MT__Element(self):
        return self.__ramRoot_MT__Element

    @ramRoot_MT__Element.setter
    def ramRoot_MT__Element(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ramRoot_MT__Element__ramRoot_MT__Element", None)
        self.__ramRoot_MT__Element = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ramRoot_GenericNode"):
                opp_val = getattr(old_value, "ramRoot_GenericNode", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ramRoot_GenericNode"):
                opp_val = getattr(value, "ramRoot_GenericNode", None)
                if opp_val is None:
                    setattr(value, "ramRoot_GenericNode", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class MTpos__Element:

    pass
class ramRoot_MTpos__Chair(MTpos__Element):

    def __init__(self, MTpos__order: str, ramRoot_MTpos__Chair: "ramRoot_MTpos__Table" = None):
        self.MTpos__order = MTpos__order
        self.ramRoot_MTpos__Chair = ramRoot_MTpos__Chair
        
    @property
    def MTpos__order(self) -> str:
        return self.__MTpos__order

    @MTpos__order.setter
    def MTpos__order(self, MTpos__order: str):
        self.__MTpos__order = MTpos__order

    @property
    def ramRoot_MTpos__Chair(self):
        return self.__ramRoot_MTpos__Chair

    @ramRoot_MTpos__Chair.setter
    def ramRoot_MTpos__Chair(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ramRoot_MTpos__Chair__ramRoot_MTpos__Chair", None)
        self.__ramRoot_MTpos__Chair = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ramRoot_MTpos__Table"):
                opp_val = getattr(old_value, "ramRoot_MTpos__Table", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ramRoot_MTpos__Table"):
                opp_val = getattr(value, "ramRoot_MTpos__Table", None)
                if opp_val is None:
                    setattr(value, "ramRoot_MTpos__Table", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class ramRoot_MTpos__Waitress(MTpos__Element):

    def __init__(self, MTpos__name: str, ramRoot_MTpos__Waitress13: "ramRoot_MTpos__Restaurant" = None, ramRoot_MTpos__Waitress: set["ramRoot_MTpos__Table"] = None):
        self.MTpos__name = MTpos__name
        self.ramRoot_MTpos__Waitress13 = ramRoot_MTpos__Waitress13
        self.ramRoot_MTpos__Waitress = ramRoot_MTpos__Waitress if ramRoot_MTpos__Waitress is not None else set()
        
    @property
    def MTpos__name(self) -> str:
        return self.__MTpos__name

    @MTpos__name.setter
    def MTpos__name(self, MTpos__name: str):
        self.__MTpos__name = MTpos__name

    @property
    def ramRoot_MTpos__Waitress13(self):
        return self.__ramRoot_MTpos__Waitress13

    @ramRoot_MTpos__Waitress13.setter
    def ramRoot_MTpos__Waitress13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ramRoot_MTpos__Waitress__ramRoot_MTpos__Waitress13", None)
        self.__ramRoot_MTpos__Waitress13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ramRoot_MTpos__Restaurant"):
                opp_val = getattr(old_value, "ramRoot_MTpos__Restaurant", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ramRoot_MTpos__Restaurant"):
                opp_val = getattr(value, "ramRoot_MTpos__Restaurant", None)
                if opp_val is None:
                    setattr(value, "ramRoot_MTpos__Restaurant", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ramRoot_MTpos__Waitress(self):
        return self.__ramRoot_MTpos__Waitress

    @ramRoot_MTpos__Waitress.setter
    def ramRoot_MTpos__Waitress(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ramRoot_MTpos__Waitress__ramRoot_MTpos__Waitress", None)
        self.__ramRoot_MTpos__Waitress = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ramRoot_MTpos__Table3"):
                    opp_val = getattr(item, "ramRoot_MTpos__Table3", None)
                    
                    if opp_val == self:
                        setattr(item, "ramRoot_MTpos__Table3", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ramRoot_MTpos__Table3"):
                    opp_val = getattr(item, "ramRoot_MTpos__Table3", None)
                    
                    setattr(item, "ramRoot_MTpos__Table3", self)
                    

class ramRoot_MTpos__Restaurant(MTpos__Element):

    pass
class ramRoot_MTpos__Table(MTpos__Element):

    def __init__(self, MTpos__id: str, MTpos__isReserved: str, ramRoot_MTpos__Table: set["ramRoot_MTpos__Chair"] = None, ramRoot_MTpos__Table3: "ramRoot_MTpos__Waitress" = None, ramRoot_MTpos__Table16: "ramRoot_MTpos__Restaurant" = None):
        self.MTpos__id = MTpos__id
        self.MTpos__isReserved = MTpos__isReserved
        self.ramRoot_MTpos__Table = ramRoot_MTpos__Table if ramRoot_MTpos__Table is not None else set()
        self.ramRoot_MTpos__Table3 = ramRoot_MTpos__Table3
        self.ramRoot_MTpos__Table16 = ramRoot_MTpos__Table16
        
    @property
    def MTpos__isReserved(self) -> str:
        return self.__MTpos__isReserved

    @MTpos__isReserved.setter
    def MTpos__isReserved(self, MTpos__isReserved: str):
        self.__MTpos__isReserved = MTpos__isReserved

    @property
    def MTpos__id(self) -> str:
        return self.__MTpos__id

    @MTpos__id.setter
    def MTpos__id(self, MTpos__id: str):
        self.__MTpos__id = MTpos__id

    @property
    def ramRoot_MTpos__Table(self):
        return self.__ramRoot_MTpos__Table

    @ramRoot_MTpos__Table.setter
    def ramRoot_MTpos__Table(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ramRoot_MTpos__Table__ramRoot_MTpos__Table", None)
        self.__ramRoot_MTpos__Table = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ramRoot_MTpos__Chair"):
                    opp_val = getattr(item, "ramRoot_MTpos__Chair", None)
                    
                    if opp_val == self:
                        setattr(item, "ramRoot_MTpos__Chair", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ramRoot_MTpos__Chair"):
                    opp_val = getattr(item, "ramRoot_MTpos__Chair", None)
                    
                    setattr(item, "ramRoot_MTpos__Chair", self)
                    

    @property
    def ramRoot_MTpos__Table3(self):
        return self.__ramRoot_MTpos__Table3

    @ramRoot_MTpos__Table3.setter
    def ramRoot_MTpos__Table3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ramRoot_MTpos__Table__ramRoot_MTpos__Table3", None)
        self.__ramRoot_MTpos__Table3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ramRoot_MTpos__Waitress"):
                opp_val = getattr(old_value, "ramRoot_MTpos__Waitress", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ramRoot_MTpos__Waitress"):
                opp_val = getattr(value, "ramRoot_MTpos__Waitress", None)
                if opp_val is None:
                    setattr(value, "ramRoot_MTpos__Waitress", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ramRoot_MTpos__Table16(self):
        return self.__ramRoot_MTpos__Table16

    @ramRoot_MTpos__Table16.setter
    def ramRoot_MTpos__Table16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ramRoot_MTpos__Table__ramRoot_MTpos__Table16", None)
        self.__ramRoot_MTpos__Table16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ramRoot_MTpos__Restaurant15"):
                opp_val = getattr(old_value, "ramRoot_MTpos__Restaurant15", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ramRoot_MTpos__Restaurant15"):
                opp_val = getattr(value, "ramRoot_MTpos__Restaurant15", None)
                if opp_val is None:
                    setattr(value, "ramRoot_MTpos__Restaurant15", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
