from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class datasetload_TableRow(ABC):

    def __init__(self, Key: str, NewRow: bool, RowNumber: int, datasetload_TableRow: "datasetload_Table" = None, datasetload_TableRow9: "datasetload_Table" = None):
        self.Key = Key
        self.NewRow = NewRow
        self.RowNumber = RowNumber
        self.datasetload_TableRow = datasetload_TableRow
        self.datasetload_TableRow9 = datasetload_TableRow9
        
        pass
    @property
    def RowNumber(self):
        return self.__RowNumber

    @RowNumber.setter
    def RowNumber(self, RowNumber: int):
        self.__RowNumber = RowNumber


    @property
    def Key(self):
        return self.__Key

    @Key.setter
    def Key(self, Key: str):
        self.__Key = Key


    @property
    def NewRow(self):
        return self.__NewRow

    @NewRow.setter
    def NewRow(self, NewRow: bool):
        self.__NewRow = NewRow


    @property
    def datasetload_TableRow(self):
        return self.__datasetload_TableRow

    @datasetload_TableRow.setter
    def datasetload_TableRow(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_datasetload_TableRow__datasetload_TableRow", None)
        self.__datasetload_TableRow = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "datasetload_Table7"):
                opp_val = getattr(old_value, "datasetload_Table7", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "datasetload_Table7"):
                opp_val = getattr(value, "datasetload_Table7", None)
                if opp_val is None:
                    setattr(value, "datasetload_Table7", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def datasetload_TableRow9(self):
        return self.__datasetload_TableRow9

    @datasetload_TableRow9.setter
    def datasetload_TableRow9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_datasetload_TableRow__datasetload_TableRow9", None)
        self.__datasetload_TableRow9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "datasetload_Table10"):
                opp_val = getattr(old_value, "datasetload_Table10", None)
                if opp_val == self:
                    setattr(old_value, "datasetload_Table10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "datasetload_Table10"):
                opp_val = getattr(value, "datasetload_Table10", None)
                setattr(value, "datasetload_Table10", self)

    def refresh(self):
        # TODO: Implement refresh method
        pass

class DataSource:

    pass
class datasetload_DataSourceJdbc(DataSource):

    def __init__(self, DataBaseUser: str, DataBaseUserPwd: str, DefaultSchema: str):
        self.DataBaseUser = DataBaseUser
        self.DataBaseUserPwd = DataBaseUserPwd
        self.DefaultSchema = DefaultSchema
        
        pass
    @property
    def DefaultSchema(self):
        return self.__DefaultSchema

    @DefaultSchema.setter
    def DefaultSchema(self, DefaultSchema: str):
        self.__DefaultSchema = DefaultSchema


    @property
    def DataBaseUserPwd(self):
        return self.__DataBaseUserPwd

    @DataBaseUserPwd.setter
    def DataBaseUserPwd(self, DataBaseUserPwd: str):
        self.__DataBaseUserPwd = DataBaseUserPwd


    @property
    def DataBaseUser(self):
        return self.__DataBaseUser

    @DataBaseUser.setter
    def DataBaseUser(self, DataBaseUser: str):
        self.__DataBaseUser = DataBaseUser


class datasetload_DataSource(ABC):

    def __init__(self, Name: str, Connected: bool, datasetload_DataSource: "datasetload_TableGroup" = None):
        self.Name = Name
        self.Connected = Connected
        self.datasetload_DataSource = datasetload_DataSource
        
        pass
    @property
    def Name(self):
        return self.__Name

    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name


    @property
    def Connected(self):
        return self.__Connected

    @Connected.setter
    def Connected(self, Connected: bool):
        self.__Connected = Connected


    @property
    def datasetload_DataSource(self):
        return self.__datasetload_DataSource

    @datasetload_DataSource.setter
    def datasetload_DataSource(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_datasetload_DataSource__datasetload_DataSource", None)
        self.__datasetload_DataSource = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "datasetload_TableGroup2"):
                opp_val = getattr(old_value, "datasetload_TableGroup2", None)
                if opp_val == self:
                    setattr(old_value, "datasetload_TableGroup2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "datasetload_TableGroup2"):
                opp_val = getattr(value, "datasetload_TableGroup2", None)
                setattr(value, "datasetload_TableGroup2", self)

    def loadTableImpl(self, datasetload_table):
        # TODO: Implement loadTableImpl method
        pass

    def disconnect(self):
        # TODO: Implement disconnect method
        pass

    def connect(self):
        # TODO: Implement connect method
        pass

class datasetload_Table(ABC):

    def __init__(self, Name: str, ParamTableGroupAttributes: str, SQLStatement: str, ColumnTableRowAttributes: str, KeyColumns: int, LastLoad: date, NumberOfRows: int, datasetload_Table: "datasetload_TableGroup" = None, datasetload_Table4: "datasetload_TableGroup" = None, datasetload_Table7: set["datasetload_TableRow"] = None, datasetload_Table10: "datasetload_TableRow" = None):
        self.Name = Name
        self.ParamTableGroupAttributes = ParamTableGroupAttributes
        self.SQLStatement = SQLStatement
        self.ColumnTableRowAttributes = ColumnTableRowAttributes
        self.KeyColumns = KeyColumns
        self.LastLoad = LastLoad
        self.NumberOfRows = NumberOfRows
        self.datasetload_Table = datasetload_Table
        self.datasetload_Table4 = datasetload_Table4
        self.datasetload_Table7 = datasetload_Table7 if datasetload_Table7 is not None else set()
        self.datasetload_Table10 = datasetload_Table10
        
        pass
    @property
    def SQLStatement(self):
        return self.__SQLStatement

    @SQLStatement.setter
    def SQLStatement(self, SQLStatement: str):
        self.__SQLStatement = SQLStatement


    @property
    def ParamTableGroupAttributes(self):
        return self.__ParamTableGroupAttributes

    @ParamTableGroupAttributes.setter
    def ParamTableGroupAttributes(self, ParamTableGroupAttributes: str):
        self.__ParamTableGroupAttributes = ParamTableGroupAttributes


    @property
    def ColumnTableRowAttributes(self):
        return self.__ColumnTableRowAttributes

    @ColumnTableRowAttributes.setter
    def ColumnTableRowAttributes(self, ColumnTableRowAttributes: str):
        self.__ColumnTableRowAttributes = ColumnTableRowAttributes


    @property
    def LastLoad(self):
        return self.__LastLoad

    @LastLoad.setter
    def LastLoad(self, LastLoad: date):
        self.__LastLoad = LastLoad


    @property
    def NumberOfRows(self):
        return self.__NumberOfRows

    @NumberOfRows.setter
    def NumberOfRows(self, NumberOfRows: int):
        self.__NumberOfRows = NumberOfRows


    @property
    def Name(self):
        return self.__Name

    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name


    @property
    def KeyColumns(self):
        return self.__KeyColumns

    @KeyColumns.setter
    def KeyColumns(self, KeyColumns: int):
        self.__KeyColumns = KeyColumns


    @property
    def datasetload_Table4(self):
        return self.__datasetload_Table4

    @datasetload_Table4.setter
    def datasetload_Table4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_datasetload_Table__datasetload_Table4", None)
        self.__datasetload_Table4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "datasetload_TableGroup5"):
                opp_val = getattr(old_value, "datasetload_TableGroup5", None)
                if opp_val == self:
                    setattr(old_value, "datasetload_TableGroup5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "datasetload_TableGroup5"):
                opp_val = getattr(value, "datasetload_TableGroup5", None)
                setattr(value, "datasetload_TableGroup5", self)

    @property
    def datasetload_Table10(self):
        return self.__datasetload_Table10

    @datasetload_Table10.setter
    def datasetload_Table10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_datasetload_Table__datasetload_Table10", None)
        self.__datasetload_Table10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "datasetload_TableRow9"):
                opp_val = getattr(old_value, "datasetload_TableRow9", None)
                if opp_val == self:
                    setattr(old_value, "datasetload_TableRow9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "datasetload_TableRow9"):
                opp_val = getattr(value, "datasetload_TableRow9", None)
                setattr(value, "datasetload_TableRow9", self)

    @property
    def datasetload_Table(self):
        return self.__datasetload_Table

    @datasetload_Table.setter
    def datasetload_Table(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_datasetload_Table__datasetload_Table", None)
        self.__datasetload_Table = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "datasetload_TableGroup"):
                opp_val = getattr(old_value, "datasetload_TableGroup", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "datasetload_TableGroup"):
                opp_val = getattr(value, "datasetload_TableGroup", None)
                if opp_val is None:
                    setattr(value, "datasetload_TableGroup", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def datasetload_Table7(self):
        return self.__datasetload_Table7

    @datasetload_Table7.setter
    def datasetload_Table7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_datasetload_Table__datasetload_Table7", None)
        self.__datasetload_Table7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "datasetload_TableRow"):
                    opp_val = getattr(item, "datasetload_TableRow", None)
                    
                    if opp_val == self:
                        setattr(item, "datasetload_TableRow", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "datasetload_TableRow"):
                    opp_val = getattr(item, "datasetload_TableRow", None)
                    
                    setattr(item, "datasetload_TableRow", self)
                    

    def newRow(self) :
        # TODO: Implement newRow method
        pass

    def load(self):
        # TODO: Implement load method
        pass

    def removeRow(self, datasetload_row):
        # TODO: Implement removeRow method
        pass

    def getRow(self, datasetload_key) :
        # TODO: Implement getRow method
        pass

    def refresh(self):
        # TODO: Implement refresh method
        pass

    def addRow(self, datasetload_row):
        # TODO: Implement addRow method
        pass

class datasetload_TableGroup(ABC):

    def __init__(self, Name: str, datasetload_TableGroup: set["datasetload_Table"] = None, datasetload_TableGroup2: "datasetload_DataSource" = None, datasetload_TableGroup5: "datasetload_Table" = None):
        self.Name = Name
        self.datasetload_TableGroup = datasetload_TableGroup if datasetload_TableGroup is not None else set()
        self.datasetload_TableGroup2 = datasetload_TableGroup2
        self.datasetload_TableGroup5 = datasetload_TableGroup5
        
        pass
    @property
    def Name(self):
        return self.__Name

    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name


    @property
    def datasetload_TableGroup5(self):
        return self.__datasetload_TableGroup5

    @datasetload_TableGroup5.setter
    def datasetload_TableGroup5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_datasetload_TableGroup__datasetload_TableGroup5", None)
        self.__datasetload_TableGroup5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "datasetload_Table4"):
                opp_val = getattr(old_value, "datasetload_Table4", None)
                if opp_val == self:
                    setattr(old_value, "datasetload_Table4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "datasetload_Table4"):
                opp_val = getattr(value, "datasetload_Table4", None)
                setattr(value, "datasetload_Table4", self)

    @property
    def datasetload_TableGroup(self):
        return self.__datasetload_TableGroup

    @datasetload_TableGroup.setter
    def datasetload_TableGroup(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_datasetload_TableGroup__datasetload_TableGroup", None)
        self.__datasetload_TableGroup = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "datasetload_Table"):
                    opp_val = getattr(item, "datasetload_Table", None)
                    
                    if opp_val == self:
                        setattr(item, "datasetload_Table", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "datasetload_Table"):
                    opp_val = getattr(item, "datasetload_Table", None)
                    
                    setattr(item, "datasetload_Table", self)
                    

    @property
    def datasetload_TableGroup2(self):
        return self.__datasetload_TableGroup2

    @datasetload_TableGroup2.setter
    def datasetload_TableGroup2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_datasetload_TableGroup__datasetload_TableGroup2", None)
        self.__datasetload_TableGroup2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "datasetload_DataSource"):
                opp_val = getattr(old_value, "datasetload_DataSource", None)
                if opp_val == self:
                    setattr(old_value, "datasetload_DataSource", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "datasetload_DataSource"):
                opp_val = getattr(value, "datasetload_DataSource", None)
                setattr(value, "datasetload_DataSource", self)

    def load(self):
        # TODO: Implement load method
        pass

    def refresh(self):
        # TODO: Implement refresh method
        pass
