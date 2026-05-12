from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class ProductionSystem_Piece(ABC):

    def __init__(self, id: str, Piece: "ProductionSystem_Conveyor" = None, piece: "ProductionSystem_Conveyor" = None):
        self.id = id
        self.Piece = Piece
        self.piece = piece
        
        pass
    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id


    @property
    def Piece(self):
        return self.__Piece

    @Piece.setter
    def Piece(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ProductionSystem_Piece__Piece", None)
        self.__Piece = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "conveyor"):
                opp_val = getattr(old_value, "conveyor", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "conveyor"):
                opp_val = getattr(value, "conveyor", None)
                if opp_val is None:
                    setattr(value, "conveyor", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def piece(self):
        return self.__piece

    @piece.setter
    def piece(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ProductionSystem_Piece__piece", None)
        self.__piece = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Conveyor14"):
                opp_val = getattr(old_value, "Conveyor14", None)
                if opp_val == self:
                    setattr(old_value, "Conveyor14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Conveyor14"):
                opp_val = getattr(value, "Conveyor14", None)
                setattr(value, "Conveyor14", self)

class ProductionSystem_Conveyor:

    def __init__(self, capacity: int, id: str, Conveyor: "ProductionSystem_Machine" = None, Conveyor2: "ProductionSystem_Machine" = None, conveyor: set["ProductionSystem_Piece"] = None, Conveyor6: "ProductionSystem_Conveyor" = None, prev: set["ProductionSystem_Conveyor"] = None, Conveyor9: "ProductionSystem_Conveyor" = None, next: "ProductionSystem_Conveyor" = None, oc: "ProductionSystem_Machine" = None, ic: "ProductionSystem_Machine" = None, Conveyor14: "ProductionSystem_Piece" = None):
        self.capacity = capacity
        self.id = id
        self.Conveyor = Conveyor
        self.Conveyor2 = Conveyor2
        self.conveyor = conveyor if conveyor is not None else set()
        self.Conveyor6 = Conveyor6
        self.prev = prev if prev is not None else set()
        self.Conveyor9 = Conveyor9
        self.next = next
        self.oc = oc
        self.ic = ic
        self.Conveyor14 = Conveyor14
        
        pass
    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id


    @property
    def capacity(self):
        return self.__capacity

    @capacity.setter
    def capacity(self, capacity: int):
        self.__capacity = capacity


    @property
    def Conveyor(self):
        return self.__Conveyor

    @Conveyor.setter
    def Conveyor(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ProductionSystem_Conveyor__Conveyor", None)
        self.__Conveyor = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "om"):
                opp_val = getattr(old_value, "om", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "om"):
                opp_val = getattr(value, "om", None)
                if opp_val is None:
                    setattr(value, "om", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def oc(self):
        return self.__oc

    @oc.setter
    def oc(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ProductionSystem_Conveyor__oc", None)
        self.__oc = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Machine"):
                opp_val = getattr(old_value, "Machine", None)
                if opp_val == self:
                    setattr(old_value, "Machine", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Machine"):
                opp_val = getattr(value, "Machine", None)
                setattr(value, "Machine", self)

    @property
    def Conveyor14(self):
        return self.__Conveyor14

    @Conveyor14.setter
    def Conveyor14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ProductionSystem_Conveyor__Conveyor14", None)
        self.__Conveyor14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "piece"):
                opp_val = getattr(old_value, "piece", None)
                if opp_val == self:
                    setattr(old_value, "piece", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "piece"):
                opp_val = getattr(value, "piece", None)
                setattr(value, "piece", self)

    @property
    def Conveyor6(self):
        return self.__Conveyor6

    @Conveyor6.setter
    def Conveyor6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ProductionSystem_Conveyor__Conveyor6", None)
        self.__Conveyor6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "prev"):
                opp_val = getattr(old_value, "prev", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "prev"):
                opp_val = getattr(value, "prev", None)
                if opp_val is None:
                    setattr(value, "prev", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Conveyor2(self):
        return self.__Conveyor2

    @Conveyor2.setter
    def Conveyor2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ProductionSystem_Conveyor__Conveyor2", None)
        self.__Conveyor2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "im"):
                opp_val = getattr(old_value, "im", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "im"):
                opp_val = getattr(value, "im", None)
                if opp_val is None:
                    setattr(value, "im", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ProductionSystem_Conveyor__next", None)
        self.__next = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Conveyor9"):
                opp_val = getattr(old_value, "Conveyor9", None)
                if opp_val == self:
                    setattr(old_value, "Conveyor9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Conveyor9"):
                opp_val = getattr(value, "Conveyor9", None)
                setattr(value, "Conveyor9", self)

    @property
    def ic(self):
        return self.__ic

    @ic.setter
    def ic(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ProductionSystem_Conveyor__ic", None)
        self.__ic = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Machine12"):
                opp_val = getattr(old_value, "Machine12", None)
                if opp_val == self:
                    setattr(old_value, "Machine12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Machine12"):
                opp_val = getattr(value, "Machine12", None)
                setattr(value, "Machine12", self)

    @property
    def conveyor(self):
        return self.__conveyor

    @conveyor.setter
    def conveyor(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ProductionSystem_Conveyor__conveyor", None)
        self.__conveyor = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Piece"):
                    opp_val = getattr(item, "Piece", None)
                    
                    if opp_val == self:
                        setattr(item, "Piece", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Piece"):
                    opp_val = getattr(item, "Piece", None)
                    
                    setattr(item, "Piece", self)
                    

    @property
    def Conveyor9(self):
        return self.__Conveyor9

    @Conveyor9.setter
    def Conveyor9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ProductionSystem_Conveyor__Conveyor9", None)
        self.__Conveyor9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "next"):
                opp_val = getattr(old_value, "next", None)
                if opp_val == self:
                    setattr(old_value, "next", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "next"):
                opp_val = getattr(value, "next", None)
                setattr(value, "next", self)

    @property
    def prev(self):
        return self.__prev

    @prev.setter
    def prev(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ProductionSystem_Conveyor__prev", None)
        self.__prev = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Conveyor6"):
                    opp_val = getattr(item, "Conveyor6", None)
                    
                    if opp_val == self:
                        setattr(item, "Conveyor6", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Conveyor6"):
                    opp_val = getattr(item, "Conveyor6", None)
                    
                    setattr(item, "Conveyor6", self)
                    

class ProductionSystem_Machine:

    def __init__(self, id: str, om: set["ProductionSystem_Conveyor"] = None, im: set["ProductionSystem_Conveyor"] = None, Machine: "ProductionSystem_Conveyor" = None, Machine12: "ProductionSystem_Conveyor" = None):
        self.id = id
        self.om = om if om is not None else set()
        self.im = im if im is not None else set()
        self.Machine = Machine
        self.Machine12 = Machine12
        
        pass
    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id


    @property
    def Machine(self):
        return self.__Machine

    @Machine.setter
    def Machine(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ProductionSystem_Machine__Machine", None)
        self.__Machine = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "oc"):
                opp_val = getattr(old_value, "oc", None)
                if opp_val == self:
                    setattr(old_value, "oc", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "oc"):
                opp_val = getattr(value, "oc", None)
                setattr(value, "oc", self)

    @property
    def im(self):
        return self.__im

    @im.setter
    def im(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ProductionSystem_Machine__im", None)
        self.__im = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Conveyor2"):
                    opp_val = getattr(item, "Conveyor2", None)
                    
                    if opp_val == self:
                        setattr(item, "Conveyor2", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Conveyor2"):
                    opp_val = getattr(item, "Conveyor2", None)
                    
                    setattr(item, "Conveyor2", self)
                    

    @property
    def Machine12(self):
        return self.__Machine12

    @Machine12.setter
    def Machine12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ProductionSystem_Machine__Machine12", None)
        self.__Machine12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ic"):
                opp_val = getattr(old_value, "ic", None)
                if opp_val == self:
                    setattr(old_value, "ic", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ic"):
                opp_val = getattr(value, "ic", None)
                setattr(value, "ic", self)

    @property
    def om(self):
        return self.__om

    @om.setter
    def om(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ProductionSystem_Machine__om", None)
        self.__om = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Conveyor"):
                    opp_val = getattr(item, "Conveyor", None)
                    
                    if opp_val == self:
                        setattr(item, "Conveyor", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Conveyor"):
                    opp_val = getattr(item, "Conveyor", None)
                    
                    setattr(item, "Conveyor", self)
                    

class Piece:

    pass
class ProductionSystem_Processed(Piece):

    pass
class ProductionSystem_Raw(Piece):

    pass