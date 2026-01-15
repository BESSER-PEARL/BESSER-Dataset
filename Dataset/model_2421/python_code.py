from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class ingest_Catalogue:

    pass
class ingest_SqoopImport:

    pass
class ingest_DbColumn:

    def __init__(self, name: str, jdbcType: int, jdbcScale: int, jdbcPrecision: int, ingest_DbColumn8: "ingest_SqoopHiveIncrementalImport" = None, ingest_DbColumn: "ingest_DbTable" = None):
        self.name = name
        self.jdbcType = jdbcType
        self.jdbcScale = jdbcScale
        self.jdbcPrecision = jdbcPrecision
        self.ingest_DbColumn8 = ingest_DbColumn8
        self.ingest_DbColumn = ingest_DbColumn
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def jdbcPrecision(self) -> int:
        return self.__jdbcPrecision

    @jdbcPrecision.setter
    def jdbcPrecision(self, jdbcPrecision: int):
        self.__jdbcPrecision = jdbcPrecision

    @property
    def jdbcScale(self) -> int:
        return self.__jdbcScale

    @jdbcScale.setter
    def jdbcScale(self, jdbcScale: int):
        self.__jdbcScale = jdbcScale

    @property
    def jdbcType(self) -> int:
        return self.__jdbcType

    @jdbcType.setter
    def jdbcType(self, jdbcType: int):
        self.__jdbcType = jdbcType

    @property
    def ingest_DbColumn(self):
        return self.__ingest_DbColumn

    @ingest_DbColumn.setter
    def ingest_DbColumn(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ingest_DbColumn__ingest_DbColumn", None)
        self.__ingest_DbColumn = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ingest_DbTable"):
                opp_val = getattr(old_value, "ingest_DbTable", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ingest_DbTable"):
                opp_val = getattr(value, "ingest_DbTable", None)
                if opp_val is None:
                    setattr(value, "ingest_DbTable", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ingest_DbColumn8(self):
        return self.__ingest_DbColumn8

    @ingest_DbColumn8.setter
    def ingest_DbColumn8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ingest_DbColumn__ingest_DbColumn8", None)
        self.__ingest_DbColumn8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ingest_SqoopHiveIncrementalImport"):
                opp_val = getattr(old_value, "ingest_SqoopHiveIncrementalImport", None)
                if opp_val == self:
                    setattr(old_value, "ingest_SqoopHiveIncrementalImport", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ingest_SqoopHiveIncrementalImport"):
                opp_val = getattr(value, "ingest_SqoopHiveIncrementalImport", None)
                setattr(value, "ingest_SqoopHiveIncrementalImport", self)

class SqoopHiveImport:

    pass
class ingest_SqoopHiveIncrementalImport(SqoopHiveImport):

    pass
class SqoopImport:

    pass
class ingest_SqoopHiveImport(SqoopImport):

    def __init__(self, targetHiveDatabase: str, targetHiveTable: str):
        self.targetHiveDatabase = targetHiveDatabase
        self.targetHiveTable = targetHiveTable
        
    @property
    def targetHiveDatabase(self) -> str:
        return self.__targetHiveDatabase

    @targetHiveDatabase.setter
    def targetHiveDatabase(self, targetHiveDatabase: str):
        self.__targetHiveDatabase = targetHiveDatabase

    @property
    def targetHiveTable(self) -> str:
        return self.__targetHiveTable

    @targetHiveTable.setter
    def targetHiveTable(self, targetHiveTable: str):
        self.__targetHiveTable = targetHiveTable

class ingest_DbTable:

    def __init__(self, name: str, ingest_DbTable6: "ingest_DbSchema" = None, ingest_DbTable: set["ingest_DbColumn"] = None, ingest_DbTable3: set["ingest_SqoopImport"] = None):
        self.name = name
        self.ingest_DbTable6 = ingest_DbTable6
        self.ingest_DbTable = ingest_DbTable if ingest_DbTable is not None else set()
        self.ingest_DbTable3 = ingest_DbTable3 if ingest_DbTable3 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def ingest_DbTable3(self):
        return self.__ingest_DbTable3

    @ingest_DbTable3.setter
    def ingest_DbTable3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ingest_DbTable__ingest_DbTable3", None)
        self.__ingest_DbTable3 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ingest_SqoopImport"):
                    opp_val = getattr(item, "ingest_SqoopImport", None)
                    
                    if opp_val == self:
                        setattr(item, "ingest_SqoopImport", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ingest_SqoopImport"):
                    opp_val = getattr(item, "ingest_SqoopImport", None)
                    
                    setattr(item, "ingest_SqoopImport", self)
                    

    @property
    def ingest_DbTable6(self):
        return self.__ingest_DbTable6

    @ingest_DbTable6.setter
    def ingest_DbTable6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ingest_DbTable__ingest_DbTable6", None)
        self.__ingest_DbTable6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ingest_DbSchema5"):
                opp_val = getattr(old_value, "ingest_DbSchema5", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ingest_DbSchema5"):
                opp_val = getattr(value, "ingest_DbSchema5", None)
                if opp_val is None:
                    setattr(value, "ingest_DbSchema5", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ingest_DbTable(self):
        return self.__ingest_DbTable

    @ingest_DbTable.setter
    def ingest_DbTable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ingest_DbTable__ingest_DbTable", None)
        self.__ingest_DbTable = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ingest_DbColumn"):
                    opp_val = getattr(item, "ingest_DbColumn", None)
                    
                    if opp_val == self:
                        setattr(item, "ingest_DbColumn", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ingest_DbColumn"):
                    opp_val = getattr(item, "ingest_DbColumn", None)
                    
                    setattr(item, "ingest_DbColumn", self)
                    

class ingest_DbSchema:

    def __init__(self, name: str, ingest_DbSchema: "ingest_Database" = None, ingest_DbSchema5: set["ingest_DbTable"] = None):
        self.name = name
        self.ingest_DbSchema = ingest_DbSchema
        self.ingest_DbSchema5 = ingest_DbSchema5 if ingest_DbSchema5 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def ingest_DbSchema(self):
        return self.__ingest_DbSchema

    @ingest_DbSchema.setter
    def ingest_DbSchema(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ingest_DbSchema__ingest_DbSchema", None)
        self.__ingest_DbSchema = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ingest_Database"):
                opp_val = getattr(old_value, "ingest_Database", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ingest_Database"):
                opp_val = getattr(value, "ingest_Database", None)
                if opp_val is None:
                    setattr(value, "ingest_Database", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ingest_DbSchema5(self):
        return self.__ingest_DbSchema5

    @ingest_DbSchema5.setter
    def ingest_DbSchema5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ingest_DbSchema__ingest_DbSchema5", None)
        self.__ingest_DbSchema5 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ingest_DbTable6"):
                    opp_val = getattr(item, "ingest_DbTable6", None)
                    
                    if opp_val == self:
                        setattr(item, "ingest_DbTable6", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ingest_DbTable6"):
                    opp_val = getattr(item, "ingest_DbTable6", None)
                    
                    setattr(item, "ingest_DbTable6", self)
                    

class ingest_Database:

    def __init__(self, label: str, jdbcUrl: str, jdbcUser: str, jdbcPassword: str, jdbcDriver: str, ingest_Database: set["ingest_DbSchema"] = None, ingest_Database10: "ingest_Catalogue" = None):
        self.label = label
        self.jdbcUrl = jdbcUrl
        self.jdbcUser = jdbcUser
        self.jdbcPassword = jdbcPassword
        self.jdbcDriver = jdbcDriver
        self.ingest_Database = ingest_Database if ingest_Database is not None else set()
        self.ingest_Database10 = ingest_Database10
        
    @property
    def jdbcPassword(self) -> str:
        return self.__jdbcPassword

    @jdbcPassword.setter
    def jdbcPassword(self, jdbcPassword: str):
        self.__jdbcPassword = jdbcPassword

    @property
    def label(self) -> str:
        return self.__label

    @label.setter
    def label(self, label: str):
        self.__label = label

    @property
    def jdbcUser(self) -> str:
        return self.__jdbcUser

    @jdbcUser.setter
    def jdbcUser(self, jdbcUser: str):
        self.__jdbcUser = jdbcUser

    @property
    def jdbcDriver(self) -> str:
        return self.__jdbcDriver

    @jdbcDriver.setter
    def jdbcDriver(self, jdbcDriver: str):
        self.__jdbcDriver = jdbcDriver

    @property
    def jdbcUrl(self) -> str:
        return self.__jdbcUrl

    @jdbcUrl.setter
    def jdbcUrl(self, jdbcUrl: str):
        self.__jdbcUrl = jdbcUrl

    @property
    def ingest_Database(self):
        return self.__ingest_Database

    @ingest_Database.setter
    def ingest_Database(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ingest_Database__ingest_Database", None)
        self.__ingest_Database = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ingest_DbSchema"):
                    opp_val = getattr(item, "ingest_DbSchema", None)
                    
                    if opp_val == self:
                        setattr(item, "ingest_DbSchema", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ingest_DbSchema"):
                    opp_val = getattr(item, "ingest_DbSchema", None)
                    
                    setattr(item, "ingest_DbSchema", self)
                    

    @property
    def ingest_Database10(self):
        return self.__ingest_Database10

    @ingest_Database10.setter
    def ingest_Database10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ingest_Database__ingest_Database10", None)
        self.__ingest_Database10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ingest_Catalogue"):
                opp_val = getattr(old_value, "ingest_Catalogue", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ingest_Catalogue"):
                opp_val = getattr(value, "ingest_Catalogue", None)
                if opp_val is None:
                    setattr(value, "ingest_Catalogue", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
