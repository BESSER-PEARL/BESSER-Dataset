from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class genSql_ForeignKey:

    pass
class genSql_PrimaryKey:

    pass
class genSql_Column:

    def __init__(self, name: str, SQLType: str, Longitud: str, genSql_Column9: "genSql_PrimaryKey" = None, genSql_Column12: "genSql_ForeignKey" = None, genSql_Column: "genSql_Table" = None, genSql_Column18: "genSql_ForeignKey" = None):
        self.name = name
        self.SQLType = SQLType
        self.Longitud = Longitud
        self.genSql_Column9 = genSql_Column9
        self.genSql_Column12 = genSql_Column12
        self.genSql_Column = genSql_Column
        self.genSql_Column18 = genSql_Column18
        
    @property
    def SQLType(self) -> str:
        return self.__SQLType

    @SQLType.setter
    def SQLType(self, SQLType: str):
        self.__SQLType = SQLType

    @property
    def Longitud(self) -> str:
        return self.__Longitud

    @Longitud.setter
    def Longitud(self, Longitud: str):
        self.__Longitud = Longitud

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def genSql_Column9(self):
        return self.__genSql_Column9

    @genSql_Column9.setter
    def genSql_Column9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_genSql_Column__genSql_Column9", None)
        self.__genSql_Column9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "genSql_PrimaryKey8"):
                opp_val = getattr(old_value, "genSql_PrimaryKey8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "genSql_PrimaryKey8"):
                opp_val = getattr(value, "genSql_PrimaryKey8", None)
                if opp_val is None:
                    setattr(value, "genSql_PrimaryKey8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def genSql_Column12(self):
        return self.__genSql_Column12

    @genSql_Column12.setter
    def genSql_Column12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_genSql_Column__genSql_Column12", None)
        self.__genSql_Column12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "genSql_ForeignKey11"):
                opp_val = getattr(old_value, "genSql_ForeignKey11", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "genSql_ForeignKey11"):
                opp_val = getattr(value, "genSql_ForeignKey11", None)
                if opp_val is None:
                    setattr(value, "genSql_ForeignKey11", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def genSql_Column18(self):
        return self.__genSql_Column18

    @genSql_Column18.setter
    def genSql_Column18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_genSql_Column__genSql_Column18", None)
        self.__genSql_Column18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "genSql_ForeignKey17"):
                opp_val = getattr(old_value, "genSql_ForeignKey17", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "genSql_ForeignKey17"):
                opp_val = getattr(value, "genSql_ForeignKey17", None)
                if opp_val is None:
                    setattr(value, "genSql_ForeignKey17", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def genSql_Column(self):
        return self.__genSql_Column

    @genSql_Column.setter
    def genSql_Column(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_genSql_Column__genSql_Column", None)
        self.__genSql_Column = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "genSql_Table2"):
                opp_val = getattr(old_value, "genSql_Table2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "genSql_Table2"):
                opp_val = getattr(value, "genSql_Table2", None)
                if opp_val is None:
                    setattr(value, "genSql_Table2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class genSql_Table:

    def __init__(self, name: str, genSql_Table: "genSql_DataBase" = None, genSql_Table2: set["genSql_Column"] = None, genSql_Table4: "genSql_PrimaryKey" = None, genSql_Table6: set["genSql_ForeignKey"] = None, genSql_Table15: "genSql_ForeignKey" = None):
        self.name = name
        self.genSql_Table = genSql_Table
        self.genSql_Table2 = genSql_Table2 if genSql_Table2 is not None else set()
        self.genSql_Table4 = genSql_Table4
        self.genSql_Table6 = genSql_Table6 if genSql_Table6 is not None else set()
        self.genSql_Table15 = genSql_Table15
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def genSql_Table2(self):
        return self.__genSql_Table2

    @genSql_Table2.setter
    def genSql_Table2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_genSql_Table__genSql_Table2", None)
        self.__genSql_Table2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "genSql_Column"):
                    opp_val = getattr(item, "genSql_Column", None)
                    
                    if opp_val == self:
                        setattr(item, "genSql_Column", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "genSql_Column"):
                    opp_val = getattr(item, "genSql_Column", None)
                    
                    setattr(item, "genSql_Column", self)
                    

    @property
    def genSql_Table(self):
        return self.__genSql_Table

    @genSql_Table.setter
    def genSql_Table(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_genSql_Table__genSql_Table", None)
        self.__genSql_Table = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "genSql_DataBase"):
                opp_val = getattr(old_value, "genSql_DataBase", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "genSql_DataBase"):
                opp_val = getattr(value, "genSql_DataBase", None)
                if opp_val is None:
                    setattr(value, "genSql_DataBase", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def genSql_Table4(self):
        return self.__genSql_Table4

    @genSql_Table4.setter
    def genSql_Table4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_genSql_Table__genSql_Table4", None)
        self.__genSql_Table4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "genSql_PrimaryKey"):
                opp_val = getattr(old_value, "genSql_PrimaryKey", None)
                if opp_val == self:
                    setattr(old_value, "genSql_PrimaryKey", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "genSql_PrimaryKey"):
                opp_val = getattr(value, "genSql_PrimaryKey", None)
                setattr(value, "genSql_PrimaryKey", self)

    @property
    def genSql_Table15(self):
        return self.__genSql_Table15

    @genSql_Table15.setter
    def genSql_Table15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_genSql_Table__genSql_Table15", None)
        self.__genSql_Table15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "genSql_ForeignKey14"):
                opp_val = getattr(old_value, "genSql_ForeignKey14", None)
                if opp_val == self:
                    setattr(old_value, "genSql_ForeignKey14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "genSql_ForeignKey14"):
                opp_val = getattr(value, "genSql_ForeignKey14", None)
                setattr(value, "genSql_ForeignKey14", self)

    @property
    def genSql_Table6(self):
        return self.__genSql_Table6

    @genSql_Table6.setter
    def genSql_Table6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_genSql_Table__genSql_Table6", None)
        self.__genSql_Table6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "genSql_ForeignKey"):
                    opp_val = getattr(item, "genSql_ForeignKey", None)
                    
                    if opp_val == self:
                        setattr(item, "genSql_ForeignKey", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "genSql_ForeignKey"):
                    opp_val = getattr(item, "genSql_ForeignKey", None)
                    
                    setattr(item, "genSql_ForeignKey", self)
                    

class genSql_DataBase:

    pass