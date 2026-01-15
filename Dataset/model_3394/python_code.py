from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class tables_Restaurant:

    pass
class tables_Waitress:

    def __init__(self, name: str, tables_Waitress: set["tables_Table"] = None, tables_Waitress4: "tables_Restaurant" = None):
        self.name = name
        self.tables_Waitress = tables_Waitress if tables_Waitress is not None else set()
        self.tables_Waitress4 = tables_Waitress4
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def tables_Waitress4(self):
        return self.__tables_Waitress4

    @tables_Waitress4.setter
    def tables_Waitress4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tables_Waitress__tables_Waitress4", None)
        self.__tables_Waitress4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tables_Restaurant"):
                opp_val = getattr(old_value, "tables_Restaurant", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tables_Restaurant"):
                opp_val = getattr(value, "tables_Restaurant", None)
                if opp_val is None:
                    setattr(value, "tables_Restaurant", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def tables_Waitress(self):
        return self.__tables_Waitress

    @tables_Waitress.setter
    def tables_Waitress(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tables_Waitress__tables_Waitress", None)
        self.__tables_Waitress = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "tables_Table2"):
                    opp_val = getattr(item, "tables_Table2", None)
                    
                    if opp_val == self:
                        setattr(item, "tables_Table2", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "tables_Table2"):
                    opp_val = getattr(item, "tables_Table2", None)
                    
                    setattr(item, "tables_Table2", self)
                    

class tables_Chair:

    def __init__(self, order: int, tables_Chair: "tables_Table" = None):
        self.order = order
        self.tables_Chair = tables_Chair
        
    @property
    def order(self) -> int:
        return self.__order

    @order.setter
    def order(self, order: int):
        self.__order = order

    @property
    def tables_Chair(self):
        return self.__tables_Chair

    @tables_Chair.setter
    def tables_Chair(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tables_Chair__tables_Chair", None)
        self.__tables_Chair = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tables_Table"):
                opp_val = getattr(old_value, "tables_Table", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tables_Table"):
                opp_val = getattr(value, "tables_Table", None)
                if opp_val is None:
                    setattr(value, "tables_Table", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class tables_Table:

    def __init__(self, id: int, isReserved: bool, tables_Table: set["tables_Chair"] = None, tables_Table2: "tables_Waitress" = None, tables_Table7: "tables_Restaurant" = None):
        self.id = id
        self.isReserved = isReserved
        self.tables_Table = tables_Table if tables_Table is not None else set()
        self.tables_Table2 = tables_Table2
        self.tables_Table7 = tables_Table7
        
    @property
    def isReserved(self) -> bool:
        return self.__isReserved

    @isReserved.setter
    def isReserved(self, isReserved: bool):
        self.__isReserved = isReserved

    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def tables_Table(self):
        return self.__tables_Table

    @tables_Table.setter
    def tables_Table(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tables_Table__tables_Table", None)
        self.__tables_Table = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "tables_Chair"):
                    opp_val = getattr(item, "tables_Chair", None)
                    
                    if opp_val == self:
                        setattr(item, "tables_Chair", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "tables_Chair"):
                    opp_val = getattr(item, "tables_Chair", None)
                    
                    setattr(item, "tables_Chair", self)
                    

    @property
    def tables_Table7(self):
        return self.__tables_Table7

    @tables_Table7.setter
    def tables_Table7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tables_Table__tables_Table7", None)
        self.__tables_Table7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tables_Restaurant6"):
                opp_val = getattr(old_value, "tables_Restaurant6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tables_Restaurant6"):
                opp_val = getattr(value, "tables_Restaurant6", None)
                if opp_val is None:
                    setattr(value, "tables_Restaurant6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def tables_Table2(self):
        return self.__tables_Table2

    @tables_Table2.setter
    def tables_Table2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tables_Table__tables_Table2", None)
        self.__tables_Table2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tables_Waitress"):
                opp_val = getattr(old_value, "tables_Waitress", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tables_Waitress"):
                opp_val = getattr(value, "tables_Waitress", None)
                if opp_val is None:
                    setattr(value, "tables_Waitress", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
