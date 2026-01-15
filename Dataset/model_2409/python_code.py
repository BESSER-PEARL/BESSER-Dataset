from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class relationalMetaModel_RelationalForeignKey:

    def __init__(self, Name: str, RelationalForeignKey: "relationalMetaModel_RelationalTable" = None, RelationalForeignKey4: "relationalMetaModel_RelationalTable" = None, ForeignKeys: "relationalMetaModel_RelationalTable" = None, ReferencedBy: "relationalMetaModel_RelationalTable" = None):
        self.Name = Name
        self.RelationalForeignKey = RelationalForeignKey
        self.RelationalForeignKey4 = RelationalForeignKey4
        self.ForeignKeys = ForeignKeys
        self.ReferencedBy = ReferencedBy
        
    @property
    def Name(self) -> str:
        return self.__Name

    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def RelationalForeignKey4(self):
        return self.__RelationalForeignKey4

    @RelationalForeignKey4.setter
    def RelationalForeignKey4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_relationalMetaModel_RelationalForeignKey__RelationalForeignKey4", None)
        self.__RelationalForeignKey4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ReferencedTable"):
                opp_val = getattr(old_value, "ReferencedTable", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ReferencedTable"):
                opp_val = getattr(value, "ReferencedTable", None)
                if opp_val is None:
                    setattr(value, "ReferencedTable", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ForeignKeys(self):
        return self.__ForeignKeys

    @ForeignKeys.setter
    def ForeignKeys(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_relationalMetaModel_RelationalForeignKey__ForeignKeys", None)
        self.__ForeignKeys = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RelationalTable6"):
                opp_val = getattr(old_value, "RelationalTable6", None)
                if opp_val == self:
                    setattr(old_value, "RelationalTable6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RelationalTable6"):
                opp_val = getattr(value, "RelationalTable6", None)
                setattr(value, "RelationalTable6", self)

    @property
    def RelationalForeignKey(self):
        return self.__RelationalForeignKey

    @RelationalForeignKey.setter
    def RelationalForeignKey(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_relationalMetaModel_RelationalForeignKey__RelationalForeignKey", None)
        self.__RelationalForeignKey = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OwnedByTable"):
                opp_val = getattr(old_value, "OwnedByTable", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OwnedByTable"):
                opp_val = getattr(value, "OwnedByTable", None)
                if opp_val is None:
                    setattr(value, "OwnedByTable", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ReferencedBy(self):
        return self.__ReferencedBy

    @ReferencedBy.setter
    def ReferencedBy(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_relationalMetaModel_RelationalForeignKey__ReferencedBy", None)
        self.__ReferencedBy = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RelationalTable8"):
                opp_val = getattr(old_value, "RelationalTable8", None)
                if opp_val == self:
                    setattr(old_value, "RelationalTable8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RelationalTable8"):
                opp_val = getattr(value, "RelationalTable8", None)
                setattr(value, "RelationalTable8", self)

class relationalMetaModel_RelationalTable:

    def __init__(self, Name: str, RelationalTable: "relationalMetaModel_RelationalSchema" = None, Tables: "relationalMetaModel_RelationalSchema" = None, OwnedByTable: set["relationalMetaModel_RelationalForeignKey"] = None, ReferencedTable: set["relationalMetaModel_RelationalForeignKey"] = None, RelationalTable6: "relationalMetaModel_RelationalForeignKey" = None, RelationalTable8: "relationalMetaModel_RelationalForeignKey" = None):
        self.Name = Name
        self.RelationalTable = RelationalTable
        self.Tables = Tables
        self.OwnedByTable = OwnedByTable if OwnedByTable is not None else set()
        self.ReferencedTable = ReferencedTable if ReferencedTable is not None else set()
        self.RelationalTable6 = RelationalTable6
        self.RelationalTable8 = RelationalTable8
        
    @property
    def Name(self) -> str:
        return self.__Name

    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def RelationalTable(self):
        return self.__RelationalTable

    @RelationalTable.setter
    def RelationalTable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_relationalMetaModel_RelationalTable__RelationalTable", None)
        self.__RelationalTable = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Schema"):
                opp_val = getattr(old_value, "Schema", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Schema"):
                opp_val = getattr(value, "Schema", None)
                if opp_val is None:
                    setattr(value, "Schema", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def RelationalTable6(self):
        return self.__RelationalTable6

    @RelationalTable6.setter
    def RelationalTable6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_relationalMetaModel_RelationalTable__RelationalTable6", None)
        self.__RelationalTable6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ForeignKeys"):
                opp_val = getattr(old_value, "ForeignKeys", None)
                if opp_val == self:
                    setattr(old_value, "ForeignKeys", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ForeignKeys"):
                opp_val = getattr(value, "ForeignKeys", None)
                setattr(value, "ForeignKeys", self)

    @property
    def RelationalTable8(self):
        return self.__RelationalTable8

    @RelationalTable8.setter
    def RelationalTable8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_relationalMetaModel_RelationalTable__RelationalTable8", None)
        self.__RelationalTable8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ReferencedBy"):
                opp_val = getattr(old_value, "ReferencedBy", None)
                if opp_val == self:
                    setattr(old_value, "ReferencedBy", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ReferencedBy"):
                opp_val = getattr(value, "ReferencedBy", None)
                setattr(value, "ReferencedBy", self)

    @property
    def ReferencedTable(self):
        return self.__ReferencedTable

    @ReferencedTable.setter
    def ReferencedTable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_relationalMetaModel_RelationalTable__ReferencedTable", None)
        self.__ReferencedTable = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "RelationalForeignKey4"):
                    opp_val = getattr(item, "RelationalForeignKey4", None)
                    
                    if opp_val == self:
                        setattr(item, "RelationalForeignKey4", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "RelationalForeignKey4"):
                    opp_val = getattr(item, "RelationalForeignKey4", None)
                    
                    setattr(item, "RelationalForeignKey4", self)
                    

    @property
    def OwnedByTable(self):
        return self.__OwnedByTable

    @OwnedByTable.setter
    def OwnedByTable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_relationalMetaModel_RelationalTable__OwnedByTable", None)
        self.__OwnedByTable = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "RelationalForeignKey"):
                    opp_val = getattr(item, "RelationalForeignKey", None)
                    
                    if opp_val == self:
                        setattr(item, "RelationalForeignKey", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "RelationalForeignKey"):
                    opp_val = getattr(item, "RelationalForeignKey", None)
                    
                    setattr(item, "RelationalForeignKey", self)
                    

    @property
    def Tables(self):
        return self.__Tables

    @Tables.setter
    def Tables(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_relationalMetaModel_RelationalTable__Tables", None)
        self.__Tables = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RelationalSchema"):
                opp_val = getattr(old_value, "RelationalSchema", None)
                if opp_val == self:
                    setattr(old_value, "RelationalSchema", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RelationalSchema"):
                opp_val = getattr(value, "RelationalSchema", None)
                setattr(value, "RelationalSchema", self)

class relationalMetaModel_RelationalSchema:

    def __init__(self, Name: str, Schema: set["relationalMetaModel_RelationalTable"] = None, RelationalSchema: "relationalMetaModel_RelationalTable" = None):
        self.Name = Name
        self.Schema = Schema if Schema is not None else set()
        self.RelationalSchema = RelationalSchema
        
    @property
    def Name(self) -> str:
        return self.__Name

    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def Schema(self):
        return self.__Schema

    @Schema.setter
    def Schema(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_relationalMetaModel_RelationalSchema__Schema", None)
        self.__Schema = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "RelationalTable"):
                    opp_val = getattr(item, "RelationalTable", None)
                    
                    if opp_val == self:
                        setattr(item, "RelationalTable", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "RelationalTable"):
                    opp_val = getattr(item, "RelationalTable", None)
                    
                    setattr(item, "RelationalTable", self)
                    

    @property
    def RelationalSchema(self):
        return self.__RelationalSchema

    @RelationalSchema.setter
    def RelationalSchema(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_relationalMetaModel_RelationalSchema__RelationalSchema", None)
        self.__RelationalSchema = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Tables"):
                opp_val = getattr(old_value, "Tables", None)
                if opp_val == self:
                    setattr(old_value, "Tables", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Tables"):
                opp_val = getattr(value, "Tables", None)
                setattr(value, "Tables", self)
