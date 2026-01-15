from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class model_Constraint:

    pass
class model_Diagram:

    pass
class model_Column:

    def __init__(self, name: str, model_Column: "model_Table" = None):
        self.name = name
        self.model_Column = model_Column
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def model_Column(self):
        return self.__model_Column

    @model_Column.setter
    def model_Column(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Column__model_Column", None)
        self.__model_Column = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_Table"):
                opp_val = getattr(old_value, "model_Table", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_Table"):
                opp_val = getattr(value, "model_Table", None)
                if opp_val is None:
                    setattr(value, "model_Table", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class model_Table:

    def __init__(self, name: str, model_Table: set["model_Column"] = None, model_Table7: "model_Diagram" = None, model_Table10: "model_Constraint" = None, model_Table13: "model_Constraint" = None, model_Table2: set["model_Constraint"] = None, model_Table4: set["model_Constraint"] = None):
        self.name = name
        self.model_Table = model_Table if model_Table is not None else set()
        self.model_Table7 = model_Table7
        self.model_Table10 = model_Table10
        self.model_Table13 = model_Table13
        self.model_Table2 = model_Table2 if model_Table2 is not None else set()
        self.model_Table4 = model_Table4 if model_Table4 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def model_Table4(self):
        return self.__model_Table4

    @model_Table4.setter
    def model_Table4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Table__model_Table4", None)
        self.__model_Table4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "model_Constraint5"):
                    opp_val = getattr(item, "model_Constraint5", None)
                    
                    if opp_val == self:
                        setattr(item, "model_Constraint5", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "model_Constraint5"):
                    opp_val = getattr(item, "model_Constraint5", None)
                    
                    setattr(item, "model_Constraint5", self)
                    

    @property
    def model_Table2(self):
        return self.__model_Table2

    @model_Table2.setter
    def model_Table2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Table__model_Table2", None)
        self.__model_Table2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "model_Constraint"):
                    opp_val = getattr(item, "model_Constraint", None)
                    
                    if opp_val == self:
                        setattr(item, "model_Constraint", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "model_Constraint"):
                    opp_val = getattr(item, "model_Constraint", None)
                    
                    setattr(item, "model_Constraint", self)
                    

    @property
    def model_Table13(self):
        return self.__model_Table13

    @model_Table13.setter
    def model_Table13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Table__model_Table13", None)
        self.__model_Table13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_Constraint12"):
                opp_val = getattr(old_value, "model_Constraint12", None)
                if opp_val == self:
                    setattr(old_value, "model_Constraint12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_Constraint12"):
                opp_val = getattr(value, "model_Constraint12", None)
                setattr(value, "model_Constraint12", self)

    @property
    def model_Table(self):
        return self.__model_Table

    @model_Table.setter
    def model_Table(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Table__model_Table", None)
        self.__model_Table = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "model_Column"):
                    opp_val = getattr(item, "model_Column", None)
                    
                    if opp_val == self:
                        setattr(item, "model_Column", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "model_Column"):
                    opp_val = getattr(item, "model_Column", None)
                    
                    setattr(item, "model_Column", self)
                    

    @property
    def model_Table7(self):
        return self.__model_Table7

    @model_Table7.setter
    def model_Table7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Table__model_Table7", None)
        self.__model_Table7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_Diagram"):
                opp_val = getattr(old_value, "model_Diagram", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_Diagram"):
                opp_val = getattr(value, "model_Diagram", None)
                if opp_val is None:
                    setattr(value, "model_Diagram", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def model_Table10(self):
        return self.__model_Table10

    @model_Table10.setter
    def model_Table10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Table__model_Table10", None)
        self.__model_Table10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_Constraint9"):
                opp_val = getattr(old_value, "model_Constraint9", None)
                if opp_val == self:
                    setattr(old_value, "model_Constraint9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_Constraint9"):
                opp_val = getattr(value, "model_Constraint9", None)
                setattr(value, "model_Constraint9", self)
