from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class rdbms_RdbmsOperationMeta:

    pass
class rdbms_RdbmsViewRecordValue:

    def __init__(self, value: str, rdbms_RdbmsViewRecordValue96: "rdbms_RdbmsViewIdentifierField" = None, rdbms_RdbmsViewRecordValue99: "rdbms_RdbmsViewValueField" = None, rdbms_RdbmsViewRecordValue: "rdbms_RdbmsViewRecord" = None):
        self.value = value
        self.rdbms_RdbmsViewRecordValue96 = rdbms_RdbmsViewRecordValue96
        self.rdbms_RdbmsViewRecordValue99 = rdbms_RdbmsViewRecordValue99
        self.rdbms_RdbmsViewRecordValue = rdbms_RdbmsViewRecordValue
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def rdbms_RdbmsViewRecordValue96(self):
        return self.__rdbms_RdbmsViewRecordValue96

    @rdbms_RdbmsViewRecordValue96.setter
    def rdbms_RdbmsViewRecordValue96(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdbms_RdbmsViewRecordValue__rdbms_RdbmsViewRecordValue96", None)
        self.__rdbms_RdbmsViewRecordValue96 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rdbms_RdbmsViewIdentifierField97"):
                opp_val = getattr(old_value, "rdbms_RdbmsViewIdentifierField97", None)
                if opp_val == self:
                    setattr(old_value, "rdbms_RdbmsViewIdentifierField97", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rdbms_RdbmsViewIdentifierField97"):
                opp_val = getattr(value, "rdbms_RdbmsViewIdentifierField97", None)
                setattr(value, "rdbms_RdbmsViewIdentifierField97", self)

    @property
    def rdbms_RdbmsViewRecordValue(self):
        return self.__rdbms_RdbmsViewRecordValue

    @rdbms_RdbmsViewRecordValue.setter
    def rdbms_RdbmsViewRecordValue(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdbms_RdbmsViewRecordValue__rdbms_RdbmsViewRecordValue", None)
        self.__rdbms_RdbmsViewRecordValue = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rdbms_RdbmsViewRecord91"):
                opp_val = getattr(old_value, "rdbms_RdbmsViewRecord91", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rdbms_RdbmsViewRecord91"):
                opp_val = getattr(value, "rdbms_RdbmsViewRecord91", None)
                if opp_val is None:
                    setattr(value, "rdbms_RdbmsViewRecord91", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def rdbms_RdbmsViewRecordValue99(self):
        return self.__rdbms_RdbmsViewRecordValue99

    @rdbms_RdbmsViewRecordValue99.setter
    def rdbms_RdbmsViewRecordValue99(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdbms_RdbmsViewRecordValue__rdbms_RdbmsViewRecordValue99", None)
        self.__rdbms_RdbmsViewRecordValue99 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rdbms_RdbmsViewValueField"):
                opp_val = getattr(old_value, "rdbms_RdbmsViewValueField", None)
                if opp_val == self:
                    setattr(old_value, "rdbms_RdbmsViewValueField", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rdbms_RdbmsViewValueField"):
                opp_val = getattr(value, "rdbms_RdbmsViewValueField", None)
                setattr(value, "rdbms_RdbmsViewValueField", self)

class RdbmsFieldOperation:

    pass
class RdbmsViewTableField:

    pass
class rdbms_RdbmsViewForeignIdentifierField(RdbmsViewTableField):

    pass
class rdbms_RdbmsViewAliasField(RdbmsViewTableField):

    pass
class RdbmsExpression:

    pass
class rdbms_RdbmsRelationExpression(RdbmsExpression):

    pass
class rdbms_RdbmsLabelExpression(RdbmsExpression):

    def __init__(self, text: str):
        self.text = text
        
    @property
    def text(self) -> str:
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text

class rdbms_RdbmsDeleteFieldOperation(RdbmsFieldOperation):

    pass
class rdbms_RdbmsModifyFieldOperation(RdbmsFieldOperation):

    def __init__(self, sizeChanged: str, nameChanged: str, changedValueFieldToForeignKey: str, changedForeignKeyToValueField: str, typeChanged: bool, mandatoryChanged: bool, rdbms_RdbmsModifyFieldOperation: "rdbms_RdbmsModifyTableOperation" = None, rdbms_RdbmsModifyFieldOperation68: "rdbms_RdbmsField" = None):
        self.sizeChanged = sizeChanged
        self.nameChanged = nameChanged
        self.changedValueFieldToForeignKey = changedValueFieldToForeignKey
        self.changedForeignKeyToValueField = changedForeignKeyToValueField
        self.typeChanged = typeChanged
        self.mandatoryChanged = mandatoryChanged
        self.rdbms_RdbmsModifyFieldOperation = rdbms_RdbmsModifyFieldOperation
        self.rdbms_RdbmsModifyFieldOperation68 = rdbms_RdbmsModifyFieldOperation68
        
    @property
    def changedForeignKeyToValueField(self) -> str:
        return self.__changedForeignKeyToValueField

    @changedForeignKeyToValueField.setter
    def changedForeignKeyToValueField(self, changedForeignKeyToValueField: str):
        self.__changedForeignKeyToValueField = changedForeignKeyToValueField

    @property
    def mandatoryChanged(self) -> bool:
        return self.__mandatoryChanged

    @mandatoryChanged.setter
    def mandatoryChanged(self, mandatoryChanged: bool):
        self.__mandatoryChanged = mandatoryChanged

    @property
    def changedValueFieldToForeignKey(self) -> str:
        return self.__changedValueFieldToForeignKey

    @changedValueFieldToForeignKey.setter
    def changedValueFieldToForeignKey(self, changedValueFieldToForeignKey: str):
        self.__changedValueFieldToForeignKey = changedValueFieldToForeignKey

    @property
    def nameChanged(self) -> str:
        return self.__nameChanged

    @nameChanged.setter
    def nameChanged(self, nameChanged: str):
        self.__nameChanged = nameChanged

    @property
    def sizeChanged(self) -> str:
        return self.__sizeChanged

    @sizeChanged.setter
    def sizeChanged(self, sizeChanged: str):
        self.__sizeChanged = sizeChanged

    @property
    def typeChanged(self) -> bool:
        return self.__typeChanged

    @typeChanged.setter
    def typeChanged(self, typeChanged: bool):
        self.__typeChanged = typeChanged

    @property
    def rdbms_RdbmsModifyFieldOperation68(self):
        return self.__rdbms_RdbmsModifyFieldOperation68

    @rdbms_RdbmsModifyFieldOperation68.setter
    def rdbms_RdbmsModifyFieldOperation68(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdbms_RdbmsModifyFieldOperation__rdbms_RdbmsModifyFieldOperation68", None)
        self.__rdbms_RdbmsModifyFieldOperation68 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rdbms_RdbmsField69"):
                opp_val = getattr(old_value, "rdbms_RdbmsField69", None)
                if opp_val == self:
                    setattr(old_value, "rdbms_RdbmsField69", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rdbms_RdbmsField69"):
                opp_val = getattr(value, "rdbms_RdbmsField69", None)
                setattr(value, "rdbms_RdbmsField69", self)

    @property
    def rdbms_RdbmsModifyFieldOperation(self):
        return self.__rdbms_RdbmsModifyFieldOperation

    @rdbms_RdbmsModifyFieldOperation.setter
    def rdbms_RdbmsModifyFieldOperation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdbms_RdbmsModifyFieldOperation__rdbms_RdbmsModifyFieldOperation", None)
        self.__rdbms_RdbmsModifyFieldOperation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rdbms_RdbmsModifyTableOperation59"):
                opp_val = getattr(old_value, "rdbms_RdbmsModifyTableOperation59", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rdbms_RdbmsModifyTableOperation59"):
                opp_val = getattr(value, "rdbms_RdbmsModifyTableOperation59", None)
                if opp_val is None:
                    setattr(value, "rdbms_RdbmsModifyTableOperation59", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class rdbms_RdbmsCreateFieldOperation(RdbmsFieldOperation):

    pass
class RdbmsTableOperation:

    pass
class rdbms_RdbmsDeleteTableOperation(RdbmsTableOperation):

    pass
class rdbms_RdbmsCreateTableOperation(RdbmsTableOperation):

    pass
class rdbms_RdbmsModifyTableOperation(RdbmsTableOperation):

    def __init__(self, nameChanged: str, rdbms_RdbmsModifyTableOperation: set["rdbms_RdbmsCreateFieldOperation"] = None, rdbms_RdbmsModifyTableOperation59: set["rdbms_RdbmsModifyFieldOperation"] = None, rdbms_RdbmsModifyTableOperation61: set["rdbms_RdbmsDeleteFieldOperation"] = None, rdbms_RdbmsModifyTableOperation63: "rdbms_RdbmsTable" = None):
        self.nameChanged = nameChanged
        self.rdbms_RdbmsModifyTableOperation = rdbms_RdbmsModifyTableOperation if rdbms_RdbmsModifyTableOperation is not None else set()
        self.rdbms_RdbmsModifyTableOperation59 = rdbms_RdbmsModifyTableOperation59 if rdbms_RdbmsModifyTableOperation59 is not None else set()
        self.rdbms_RdbmsModifyTableOperation61 = rdbms_RdbmsModifyTableOperation61 if rdbms_RdbmsModifyTableOperation61 is not None else set()
        self.rdbms_RdbmsModifyTableOperation63 = rdbms_RdbmsModifyTableOperation63
        
    @property
    def nameChanged(self) -> str:
        return self.__nameChanged

    @nameChanged.setter
    def nameChanged(self, nameChanged: str):
        self.__nameChanged = nameChanged

    @property
    def rdbms_RdbmsModifyTableOperation(self):
        return self.__rdbms_RdbmsModifyTableOperation

    @rdbms_RdbmsModifyTableOperation.setter
    def rdbms_RdbmsModifyTableOperation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdbms_RdbmsModifyTableOperation__rdbms_RdbmsModifyTableOperation", None)
        self.__rdbms_RdbmsModifyTableOperation = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "rdbms_RdbmsCreateFieldOperation"):
                    opp_val = getattr(item, "rdbms_RdbmsCreateFieldOperation", None)
                    
                    if opp_val == self:
                        setattr(item, "rdbms_RdbmsCreateFieldOperation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "rdbms_RdbmsCreateFieldOperation"):
                    opp_val = getattr(item, "rdbms_RdbmsCreateFieldOperation", None)
                    
                    setattr(item, "rdbms_RdbmsCreateFieldOperation", self)
                    

    @property
    def rdbms_RdbmsModifyTableOperation63(self):
        return self.__rdbms_RdbmsModifyTableOperation63

    @rdbms_RdbmsModifyTableOperation63.setter
    def rdbms_RdbmsModifyTableOperation63(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdbms_RdbmsModifyTableOperation__rdbms_RdbmsModifyTableOperation63", None)
        self.__rdbms_RdbmsModifyTableOperation63 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rdbms_RdbmsTable64"):
                opp_val = getattr(old_value, "rdbms_RdbmsTable64", None)
                if opp_val == self:
                    setattr(old_value, "rdbms_RdbmsTable64", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rdbms_RdbmsTable64"):
                opp_val = getattr(value, "rdbms_RdbmsTable64", None)
                setattr(value, "rdbms_RdbmsTable64", self)

    @property
    def rdbms_RdbmsModifyTableOperation61(self):
        return self.__rdbms_RdbmsModifyTableOperation61

    @rdbms_RdbmsModifyTableOperation61.setter
    def rdbms_RdbmsModifyTableOperation61(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdbms_RdbmsModifyTableOperation__rdbms_RdbmsModifyTableOperation61", None)
        self.__rdbms_RdbmsModifyTableOperation61 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "rdbms_RdbmsDeleteFieldOperation"):
                    opp_val = getattr(item, "rdbms_RdbmsDeleteFieldOperation", None)
                    
                    if opp_val == self:
                        setattr(item, "rdbms_RdbmsDeleteFieldOperation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "rdbms_RdbmsDeleteFieldOperation"):
                    opp_val = getattr(item, "rdbms_RdbmsDeleteFieldOperation", None)
                    
                    setattr(item, "rdbms_RdbmsDeleteFieldOperation", self)
                    

    @property
    def rdbms_RdbmsModifyTableOperation59(self):
        return self.__rdbms_RdbmsModifyTableOperation59

    @rdbms_RdbmsModifyTableOperation59.setter
    def rdbms_RdbmsModifyTableOperation59(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdbms_RdbmsModifyTableOperation__rdbms_RdbmsModifyTableOperation59", None)
        self.__rdbms_RdbmsModifyTableOperation59 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "rdbms_RdbmsModifyFieldOperation"):
                    opp_val = getattr(item, "rdbms_RdbmsModifyFieldOperation", None)
                    
                    if opp_val == self:
                        setattr(item, "rdbms_RdbmsModifyFieldOperation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "rdbms_RdbmsModifyFieldOperation"):
                    opp_val = getattr(item, "rdbms_RdbmsModifyFieldOperation", None)
                    
                    setattr(item, "rdbms_RdbmsModifyFieldOperation", self)
                    

class rdbms_RdbmsViewRecord:

    pass
class rdbms_RdbmsFeature:

    def __init__(self, name: str, rdbms_RdbmsFeature: "rdbms_RdbmsConfiguration" = None):
        self.name = name
        self.rdbms_RdbmsFeature = rdbms_RdbmsFeature
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def rdbms_RdbmsFeature(self):
        return self.__rdbms_RdbmsFeature

    @rdbms_RdbmsFeature.setter
    def rdbms_RdbmsFeature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdbms_RdbmsFeature__rdbms_RdbmsFeature", None)
        self.__rdbms_RdbmsFeature = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rdbms_RdbmsConfiguration47"):
                opp_val = getattr(old_value, "rdbms_RdbmsConfiguration47", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rdbms_RdbmsConfiguration47"):
                opp_val = getattr(value, "rdbms_RdbmsConfiguration47", None)
                if opp_val is None:
                    setattr(value, "rdbms_RdbmsConfiguration47", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class rdbms_RdbmsConfiguration:

    def __init__(self, dialect: str, rdbms_RdbmsConfiguration: "rdbms_RdbmsModel" = None, rdbms_RdbmsConfiguration47: set["rdbms_RdbmsFeature"] = None):
        self.dialect = dialect
        self.rdbms_RdbmsConfiguration = rdbms_RdbmsConfiguration
        self.rdbms_RdbmsConfiguration47 = rdbms_RdbmsConfiguration47 if rdbms_RdbmsConfiguration47 is not None else set()
        
    @property
    def dialect(self) -> str:
        return self.__dialect

    @dialect.setter
    def dialect(self, dialect: str):
        self.__dialect = dialect

    @property
    def rdbms_RdbmsConfiguration(self):
        return self.__rdbms_RdbmsConfiguration

    @rdbms_RdbmsConfiguration.setter
    def rdbms_RdbmsConfiguration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdbms_RdbmsConfiguration__rdbms_RdbmsConfiguration", None)
        self.__rdbms_RdbmsConfiguration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rdbms_RdbmsModel41"):
                opp_val = getattr(old_value, "rdbms_RdbmsModel41", None)
                if opp_val == self:
                    setattr(old_value, "rdbms_RdbmsModel41", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rdbms_RdbmsModel41"):
                opp_val = getattr(value, "rdbms_RdbmsModel41", None)
                setattr(value, "rdbms_RdbmsModel41", self)

    @property
    def rdbms_RdbmsConfiguration47(self):
        return self.__rdbms_RdbmsConfiguration47

    @rdbms_RdbmsConfiguration47.setter
    def rdbms_RdbmsConfiguration47(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdbms_RdbmsConfiguration__rdbms_RdbmsConfiguration47", None)
        self.__rdbms_RdbmsConfiguration47 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "rdbms_RdbmsFeature"):
                    opp_val = getattr(item, "rdbms_RdbmsFeature", None)
                    
                    if opp_val == self:
                        setattr(item, "rdbms_RdbmsFeature", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "rdbms_RdbmsFeature"):
                    opp_val = getattr(item, "rdbms_RdbmsFeature", None)
                    
                    setattr(item, "rdbms_RdbmsFeature", self)
                    

class rdbms_RdbmsModel:

    def __init__(self, version: str, rdbms_RdbmsModel: set["rdbms_RdbmsFieldType"] = None, rdbms_RdbmsModel35: set["rdbms_RdbmsTable"] = None, rdbms_RdbmsModel38: set["rdbms_RdbmsView"] = None, rdbms_RdbmsModel41: "rdbms_RdbmsConfiguration" = None, rdbms_RdbmsModel43: set["rdbms_RdbmsTableOperation"] = None, rdbms_RdbmsModel45: set["rdbms_RdbmsViewRecord"] = None, rdbms_RdbmsModel104: "rdbms_RdbmsOperationMeta" = None, rdbms_RdbmsModel107: "rdbms_RdbmsOperationMeta" = None, rdbms_RdbmsModel110: "rdbms_RdbmsOperationMeta" = None):
        self.version = version
        self.rdbms_RdbmsModel = rdbms_RdbmsModel if rdbms_RdbmsModel is not None else set()
        self.rdbms_RdbmsModel35 = rdbms_RdbmsModel35 if rdbms_RdbmsModel35 is not None else set()
        self.rdbms_RdbmsModel38 = rdbms_RdbmsModel38 if rdbms_RdbmsModel38 is not None else set()
        self.rdbms_RdbmsModel41 = rdbms_RdbmsModel41
        self.rdbms_RdbmsModel43 = rdbms_RdbmsModel43 if rdbms_RdbmsModel43 is not None else set()
        self.rdbms_RdbmsModel45 = rdbms_RdbmsModel45 if rdbms_RdbmsModel45 is not None else set()
        self.rdbms_RdbmsModel104 = rdbms_RdbmsModel104
        self.rdbms_RdbmsModel107 = rdbms_RdbmsModel107
        self.rdbms_RdbmsModel110 = rdbms_RdbmsModel110
        
    @property
    def version(self) -> str:
        return self.__version

    @version.setter
    def version(self, version: str):
        self.__version = version

    @property
    def rdbms_RdbmsModel104(self):
        return self.__rdbms_RdbmsModel104

    @rdbms_RdbmsModel104.setter
    def rdbms_RdbmsModel104(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdbms_RdbmsModel__rdbms_RdbmsModel104", None)
        self.__rdbms_RdbmsModel104 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rdbms_RdbmsOperationMeta"):
                opp_val = getattr(old_value, "rdbms_RdbmsOperationMeta", None)
                if opp_val == self:
                    setattr(old_value, "rdbms_RdbmsOperationMeta", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rdbms_RdbmsOperationMeta"):
                opp_val = getattr(value, "rdbms_RdbmsOperationMeta", None)
                setattr(value, "rdbms_RdbmsOperationMeta", self)

    @property
    def rdbms_RdbmsModel43(self):
        return self.__rdbms_RdbmsModel43

    @rdbms_RdbmsModel43.setter
    def rdbms_RdbmsModel43(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdbms_RdbmsModel__rdbms_RdbmsModel43", None)
        self.__rdbms_RdbmsModel43 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "rdbms_RdbmsTableOperation"):
                    opp_val = getattr(item, "rdbms_RdbmsTableOperation", None)
                    
                    if opp_val == self:
                        setattr(item, "rdbms_RdbmsTableOperation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "rdbms_RdbmsTableOperation"):
                    opp_val = getattr(item, "rdbms_RdbmsTableOperation", None)
                    
                    setattr(item, "rdbms_RdbmsTableOperation", self)
                    

    @property
    def rdbms_RdbmsModel41(self):
        return self.__rdbms_RdbmsModel41

    @rdbms_RdbmsModel41.setter
    def rdbms_RdbmsModel41(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdbms_RdbmsModel__rdbms_RdbmsModel41", None)
        self.__rdbms_RdbmsModel41 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rdbms_RdbmsConfiguration"):
                opp_val = getattr(old_value, "rdbms_RdbmsConfiguration", None)
                if opp_val == self:
                    setattr(old_value, "rdbms_RdbmsConfiguration", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rdbms_RdbmsConfiguration"):
                opp_val = getattr(value, "rdbms_RdbmsConfiguration", None)
                setattr(value, "rdbms_RdbmsConfiguration", self)

    @property
    def rdbms_RdbmsModel35(self):
        return self.__rdbms_RdbmsModel35

    @rdbms_RdbmsModel35.setter
    def rdbms_RdbmsModel35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdbms_RdbmsModel__rdbms_RdbmsModel35", None)
        self.__rdbms_RdbmsModel35 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "rdbms_RdbmsTable36"):
                    opp_val = getattr(item, "rdbms_RdbmsTable36", None)
                    
                    if opp_val == self:
                        setattr(item, "rdbms_RdbmsTable36", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "rdbms_RdbmsTable36"):
                    opp_val = getattr(item, "rdbms_RdbmsTable36", None)
                    
                    setattr(item, "rdbms_RdbmsTable36", self)
                    

    @property
    def rdbms_RdbmsModel107(self):
        return self.__rdbms_RdbmsModel107

    @rdbms_RdbmsModel107.setter
    def rdbms_RdbmsModel107(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdbms_RdbmsModel__rdbms_RdbmsModel107", None)
        self.__rdbms_RdbmsModel107 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rdbms_RdbmsOperationMeta106"):
                opp_val = getattr(old_value, "rdbms_RdbmsOperationMeta106", None)
                if opp_val == self:
                    setattr(old_value, "rdbms_RdbmsOperationMeta106", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rdbms_RdbmsOperationMeta106"):
                opp_val = getattr(value, "rdbms_RdbmsOperationMeta106", None)
                setattr(value, "rdbms_RdbmsOperationMeta106", self)

    @property
    def rdbms_RdbmsModel45(self):
        return self.__rdbms_RdbmsModel45

    @rdbms_RdbmsModel45.setter
    def rdbms_RdbmsModel45(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdbms_RdbmsModel__rdbms_RdbmsModel45", None)
        self.__rdbms_RdbmsModel45 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "rdbms_RdbmsViewRecord"):
                    opp_val = getattr(item, "rdbms_RdbmsViewRecord", None)
                    
                    if opp_val == self:
                        setattr(item, "rdbms_RdbmsViewRecord", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "rdbms_RdbmsViewRecord"):
                    opp_val = getattr(item, "rdbms_RdbmsViewRecord", None)
                    
                    setattr(item, "rdbms_RdbmsViewRecord", self)
                    

    @property
    def rdbms_RdbmsModel(self):
        return self.__rdbms_RdbmsModel

    @rdbms_RdbmsModel.setter
    def rdbms_RdbmsModel(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdbms_RdbmsModel__rdbms_RdbmsModel", None)
        self.__rdbms_RdbmsModel = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "rdbms_RdbmsFieldType33"):
                    opp_val = getattr(item, "rdbms_RdbmsFieldType33", None)
                    
                    if opp_val == self:
                        setattr(item, "rdbms_RdbmsFieldType33", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "rdbms_RdbmsFieldType33"):
                    opp_val = getattr(item, "rdbms_RdbmsFieldType33", None)
                    
                    setattr(item, "rdbms_RdbmsFieldType33", self)
                    

    @property
    def rdbms_RdbmsModel110(self):
        return self.__rdbms_RdbmsModel110

    @rdbms_RdbmsModel110.setter
    def rdbms_RdbmsModel110(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdbms_RdbmsModel__rdbms_RdbmsModel110", None)
        self.__rdbms_RdbmsModel110 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rdbms_RdbmsOperationMeta109"):
                opp_val = getattr(old_value, "rdbms_RdbmsOperationMeta109", None)
                if opp_val == self:
                    setattr(old_value, "rdbms_RdbmsOperationMeta109", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rdbms_RdbmsOperationMeta109"):
                opp_val = getattr(value, "rdbms_RdbmsOperationMeta109", None)
                setattr(value, "rdbms_RdbmsOperationMeta109", self)

    @property
    def rdbms_RdbmsModel38(self):
        return self.__rdbms_RdbmsModel38

    @rdbms_RdbmsModel38.setter
    def rdbms_RdbmsModel38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdbms_RdbmsModel__rdbms_RdbmsModel38", None)
        self.__rdbms_RdbmsModel38 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "rdbms_RdbmsView39"):
                    opp_val = getattr(item, "rdbms_RdbmsView39", None)
                    
                    if opp_val == self:
                        setattr(item, "rdbms_RdbmsView39", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "rdbms_RdbmsView39"):
                    opp_val = getattr(item, "rdbms_RdbmsView39", None)
                    
                    setattr(item, "rdbms_RdbmsView39", self)
                    

class rdbms_RdbmsViewRelation:

    def __init__(self, name: str, rdbms_RdbmsViewRelation: "rdbms_RdbmsView" = None, rdbms_RdbmsViewRelation77: "rdbms_RdbmsIdentifierField" = None, rdbms_RdbmsViewRelation80: "rdbms_RdbmsIdentifierField" = None, rdbms_RdbmsViewRelation71: "rdbms_RdbmsTableAlias" = None, rdbms_RdbmsViewRelation74: "rdbms_RdbmsTableAlias" = None):
        self.name = name
        self.rdbms_RdbmsViewRelation = rdbms_RdbmsViewRelation
        self.rdbms_RdbmsViewRelation77 = rdbms_RdbmsViewRelation77
        self.rdbms_RdbmsViewRelation80 = rdbms_RdbmsViewRelation80
        self.rdbms_RdbmsViewRelation71 = rdbms_RdbmsViewRelation71
        self.rdbms_RdbmsViewRelation74 = rdbms_RdbmsViewRelation74
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def rdbms_RdbmsViewRelation(self):
        return self.__rdbms_RdbmsViewRelation

    @rdbms_RdbmsViewRelation.setter
    def rdbms_RdbmsViewRelation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdbms_RdbmsViewRelation__rdbms_RdbmsViewRelation", None)
        self.__rdbms_RdbmsViewRelation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rdbms_RdbmsView24"):
                opp_val = getattr(old_value, "rdbms_RdbmsView24", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rdbms_RdbmsView24"):
                opp_val = getattr(value, "rdbms_RdbmsView24", None)
                if opp_val is None:
                    setattr(value, "rdbms_RdbmsView24", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def rdbms_RdbmsViewRelation74(self):
        return self.__rdbms_RdbmsViewRelation74

    @rdbms_RdbmsViewRelation74.setter
    def rdbms_RdbmsViewRelation74(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdbms_RdbmsViewRelation__rdbms_RdbmsViewRelation74", None)
        self.__rdbms_RdbmsViewRelation74 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rdbms_RdbmsTableAlias75"):
                opp_val = getattr(old_value, "rdbms_RdbmsTableAlias75", None)
                if opp_val == self:
                    setattr(old_value, "rdbms_RdbmsTableAlias75", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rdbms_RdbmsTableAlias75"):
                opp_val = getattr(value, "rdbms_RdbmsTableAlias75", None)
                setattr(value, "rdbms_RdbmsTableAlias75", self)

    @property
    def rdbms_RdbmsViewRelation80(self):
        return self.__rdbms_RdbmsViewRelation80

    @rdbms_RdbmsViewRelation80.setter
    def rdbms_RdbmsViewRelation80(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdbms_RdbmsViewRelation__rdbms_RdbmsViewRelation80", None)
        self.__rdbms_RdbmsViewRelation80 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rdbms_RdbmsIdentifierField81"):
                opp_val = getattr(old_value, "rdbms_RdbmsIdentifierField81", None)
                if opp_val == self:
                    setattr(old_value, "rdbms_RdbmsIdentifierField81", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rdbms_RdbmsIdentifierField81"):
                opp_val = getattr(value, "rdbms_RdbmsIdentifierField81", None)
                setattr(value, "rdbms_RdbmsIdentifierField81", self)

    @property
    def rdbms_RdbmsViewRelation71(self):
        return self.__rdbms_RdbmsViewRelation71

    @rdbms_RdbmsViewRelation71.setter
    def rdbms_RdbmsViewRelation71(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdbms_RdbmsViewRelation__rdbms_RdbmsViewRelation71", None)
        self.__rdbms_RdbmsViewRelation71 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rdbms_RdbmsTableAlias72"):
                opp_val = getattr(old_value, "rdbms_RdbmsTableAlias72", None)
                if opp_val == self:
                    setattr(old_value, "rdbms_RdbmsTableAlias72", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rdbms_RdbmsTableAlias72"):
                opp_val = getattr(value, "rdbms_RdbmsTableAlias72", None)
                setattr(value, "rdbms_RdbmsTableAlias72", self)

    @property
    def rdbms_RdbmsViewRelation77(self):
        return self.__rdbms_RdbmsViewRelation77

    @rdbms_RdbmsViewRelation77.setter
    def rdbms_RdbmsViewRelation77(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdbms_RdbmsViewRelation__rdbms_RdbmsViewRelation77", None)
        self.__rdbms_RdbmsViewRelation77 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rdbms_RdbmsIdentifierField78"):
                opp_val = getattr(old_value, "rdbms_RdbmsIdentifierField78", None)
                if opp_val == self:
                    setattr(old_value, "rdbms_RdbmsIdentifierField78", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rdbms_RdbmsIdentifierField78"):
                opp_val = getattr(value, "rdbms_RdbmsIdentifierField78", None)
                setattr(value, "rdbms_RdbmsIdentifierField78", self)

class RdbmsViewField:

    pass
class rdbms_RdbmsViewTableField(RdbmsViewField):

    def __init__(self, foreign: bool, rdbms_RdbmsViewTableField: "rdbms_RdbmsField" = None):
        self.foreign = foreign
        self.rdbms_RdbmsViewTableField = rdbms_RdbmsViewTableField
        
    @property
    def foreign(self) -> bool:
        return self.__foreign

    @foreign.setter
    def foreign(self, foreign: bool):
        self.__foreign = foreign

    @property
    def rdbms_RdbmsViewTableField(self):
        return self.__rdbms_RdbmsViewTableField

    @rdbms_RdbmsViewTableField.setter
    def rdbms_RdbmsViewTableField(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdbms_RdbmsViewTableField__rdbms_RdbmsViewTableField", None)
        self.__rdbms_RdbmsViewTableField = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rdbms_RdbmsField83"):
                opp_val = getattr(old_value, "rdbms_RdbmsField83", None)
                if opp_val == self:
                    setattr(old_value, "rdbms_RdbmsField83", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rdbms_RdbmsField83"):
                opp_val = getattr(value, "rdbms_RdbmsField83", None)
                setattr(value, "rdbms_RdbmsField83", self)

class rdbms_RdbmsViewExpressionField(RdbmsViewField):

    def __init__(self, expression: str, rdbms_RdbmsViewExpressionField: set["rdbms_RdbmsExpression"] = None):
        self.expression = expression
        self.rdbms_RdbmsViewExpressionField = rdbms_RdbmsViewExpressionField if rdbms_RdbmsViewExpressionField is not None else set()
        
    @property
    def expression(self) -> str:
        return self.__expression

    @expression.setter
    def expression(self, expression: str):
        self.__expression = expression

    @property
    def rdbms_RdbmsViewExpressionField(self):
        return self.__rdbms_RdbmsViewExpressionField

    @rdbms_RdbmsViewExpressionField.setter
    def rdbms_RdbmsViewExpressionField(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdbms_RdbmsViewExpressionField__rdbms_RdbmsViewExpressionField", None)
        self.__rdbms_RdbmsViewExpressionField = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "rdbms_RdbmsExpression"):
                    opp_val = getattr(item, "rdbms_RdbmsExpression", None)
                    
                    if opp_val == self:
                        setattr(item, "rdbms_RdbmsExpression", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "rdbms_RdbmsExpression"):
                    opp_val = getattr(item, "rdbms_RdbmsExpression", None)
                    
                    setattr(item, "rdbms_RdbmsExpression", self)
                    

class RdbmsViewAliasField:

    pass
class rdbms_RdbmsViewIdentifierField(RdbmsViewAliasField):

    pass
class rdbms_RdbmsViewValueField(RdbmsViewAliasField):

    pass
class RdbmsIdentifierField:

    pass
class rdbms_RdbmsForeignKey(RdbmsIdentifierField):

    def __init__(self, inheritenceBased: bool, foreignKeySqlName: str, deleteOnCascade: bool, deferred: bool, readOnly: bool, rdbms_RdbmsForeignKey: "rdbms_RdbmsJunctionTable" = None, rdbms_RdbmsForeignKey19: "rdbms_RdbmsJunctionTable" = None, RdbmsForeignKey: "rdbms_RdbmsIdentifierField" = None, foreignKeys: "rdbms_RdbmsIdentifierField" = None):
        self.inheritenceBased = inheritenceBased
        self.foreignKeySqlName = foreignKeySqlName
        self.deleteOnCascade = deleteOnCascade
        self.deferred = deferred
        self.readOnly = readOnly
        self.rdbms_RdbmsForeignKey = rdbms_RdbmsForeignKey
        self.rdbms_RdbmsForeignKey19 = rdbms_RdbmsForeignKey19
        self.RdbmsForeignKey = RdbmsForeignKey
        self.foreignKeys = foreignKeys
        
    @property
    def readOnly(self) -> bool:
        return self.__readOnly

    @readOnly.setter
    def readOnly(self, readOnly: bool):
        self.__readOnly = readOnly

    @property
    def foreignKeySqlName(self) -> str:
        return self.__foreignKeySqlName

    @foreignKeySqlName.setter
    def foreignKeySqlName(self, foreignKeySqlName: str):
        self.__foreignKeySqlName = foreignKeySqlName

    @property
    def inheritenceBased(self) -> bool:
        return self.__inheritenceBased

    @inheritenceBased.setter
    def inheritenceBased(self, inheritenceBased: bool):
        self.__inheritenceBased = inheritenceBased

    @property
    def deferred(self) -> bool:
        return self.__deferred

    @deferred.setter
    def deferred(self, deferred: bool):
        self.__deferred = deferred

    @property
    def deleteOnCascade(self) -> bool:
        return self.__deleteOnCascade

    @deleteOnCascade.setter
    def deleteOnCascade(self, deleteOnCascade: bool):
        self.__deleteOnCascade = deleteOnCascade

    @property
    def foreignKeys(self):
        return self.__foreignKeys

    @foreignKeys.setter
    def foreignKeys(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdbms_RdbmsForeignKey__foreignKeys", None)
        self.__foreignKeys = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RdbmsIdentifierField"):
                opp_val = getattr(old_value, "RdbmsIdentifierField", None)
                if opp_val == self:
                    setattr(old_value, "RdbmsIdentifierField", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RdbmsIdentifierField"):
                opp_val = getattr(value, "RdbmsIdentifierField", None)
                setattr(value, "RdbmsIdentifierField", self)

    @property
    def RdbmsForeignKey(self):
        return self.__RdbmsForeignKey

    @RdbmsForeignKey.setter
    def RdbmsForeignKey(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdbms_RdbmsForeignKey__RdbmsForeignKey", None)
        self.__RdbmsForeignKey = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "referenceKey"):
                opp_val = getattr(old_value, "referenceKey", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "referenceKey"):
                opp_val = getattr(value, "referenceKey", None)
                if opp_val is None:
                    setattr(value, "referenceKey", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def rdbms_RdbmsForeignKey(self):
        return self.__rdbms_RdbmsForeignKey

    @rdbms_RdbmsForeignKey.setter
    def rdbms_RdbmsForeignKey(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdbms_RdbmsForeignKey__rdbms_RdbmsForeignKey", None)
        self.__rdbms_RdbmsForeignKey = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rdbms_RdbmsJunctionTable"):
                opp_val = getattr(old_value, "rdbms_RdbmsJunctionTable", None)
                if opp_val == self:
                    setattr(old_value, "rdbms_RdbmsJunctionTable", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rdbms_RdbmsJunctionTable"):
                opp_val = getattr(value, "rdbms_RdbmsJunctionTable", None)
                setattr(value, "rdbms_RdbmsJunctionTable", self)

    @property
    def rdbms_RdbmsForeignKey19(self):
        return self.__rdbms_RdbmsForeignKey19

    @rdbms_RdbmsForeignKey19.setter
    def rdbms_RdbmsForeignKey19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdbms_RdbmsForeignKey__rdbms_RdbmsForeignKey19", None)
        self.__rdbms_RdbmsForeignKey19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rdbms_RdbmsJunctionTable18"):
                opp_val = getattr(old_value, "rdbms_RdbmsJunctionTable18", None)
                if opp_val == self:
                    setattr(old_value, "rdbms_RdbmsJunctionTable18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rdbms_RdbmsJunctionTable18"):
                opp_val = getattr(value, "rdbms_RdbmsJunctionTable18", None)
                setattr(value, "rdbms_RdbmsJunctionTable18", self)

class RdbmsField:

    pass
class rdbms_RdbmsValueField(RdbmsField):

    def __init__(self, technical: bool):
        self.technical = technical
        
    @property
    def technical(self) -> bool:
        return self.__technical

    @technical.setter
    def technical(self, technical: bool):
        self.__technical = technical

class RdbmsTable:

    pass
class rdbms_RdbmsJunctionTable(RdbmsTable):

    pass
class rdbms_RdbmsIdentifierField(RdbmsField):

    pass
class rdbms_RdbmsFieldType:

    def __init__(self, scale: int, storageByte: int, name: str, rdbmsTypeName: str, uuid: str, description: str, size: int, precision: int, rdbms_RdbmsFieldType: "rdbms_RdbmsField" = None, rdbms_RdbmsFieldType33: "rdbms_RdbmsModel" = None):
        self.scale = scale
        self.storageByte = storageByte
        self.name = name
        self.rdbmsTypeName = rdbmsTypeName
        self.uuid = uuid
        self.description = description
        self.size = size
        self.precision = precision
        self.rdbms_RdbmsFieldType = rdbms_RdbmsFieldType
        self.rdbms_RdbmsFieldType33 = rdbms_RdbmsFieldType33
        
    @property
    def scale(self) -> int:
        return self.__scale

    @scale.setter
    def scale(self, scale: int):
        self.__scale = scale

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def precision(self) -> int:
        return self.__precision

    @precision.setter
    def precision(self, precision: int):
        self.__precision = precision

    @property
    def size(self) -> int:
        return self.__size

    @size.setter
    def size(self, size: int):
        self.__size = size

    @property
    def rdbmsTypeName(self) -> str:
        return self.__rdbmsTypeName

    @rdbmsTypeName.setter
    def rdbmsTypeName(self, rdbmsTypeName: str):
        self.__rdbmsTypeName = rdbmsTypeName

    @property
    def uuid(self) -> str:
        return self.__uuid

    @uuid.setter
    def uuid(self, uuid: str):
        self.__uuid = uuid

    @property
    def storageByte(self) -> int:
        return self.__storageByte

    @storageByte.setter
    def storageByte(self, storageByte: int):
        self.__storageByte = storageByte

    @property
    def rdbms_RdbmsFieldType(self):
        return self.__rdbms_RdbmsFieldType

    @rdbms_RdbmsFieldType.setter
    def rdbms_RdbmsFieldType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdbms_RdbmsFieldType__rdbms_RdbmsFieldType", None)
        self.__rdbms_RdbmsFieldType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rdbms_RdbmsField"):
                opp_val = getattr(old_value, "rdbms_RdbmsField", None)
                if opp_val == self:
                    setattr(old_value, "rdbms_RdbmsField", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rdbms_RdbmsField"):
                opp_val = getattr(value, "rdbms_RdbmsField", None)
                setattr(value, "rdbms_RdbmsField", self)

    @property
    def rdbms_RdbmsFieldType33(self):
        return self.__rdbms_RdbmsFieldType33

    @rdbms_RdbmsFieldType33.setter
    def rdbms_RdbmsFieldType33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdbms_RdbmsFieldType__rdbms_RdbmsFieldType33", None)
        self.__rdbms_RdbmsFieldType33 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rdbms_RdbmsModel"):
                opp_val = getattr(old_value, "rdbms_RdbmsModel", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rdbms_RdbmsModel"):
                opp_val = getattr(value, "rdbms_RdbmsModel", None)
                if opp_val is None:
                    setattr(value, "rdbms_RdbmsModel", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class RdbmsElement:

    pass
class rdbms_RdbmsUniqueConstraint(RdbmsElement):

    pass
class rdbms_RdbmsViewField(RdbmsElement):

    def __init__(self, inherited: bool, fields30: "rdbms_RdbmsView" = None, RdbmsViewField: "rdbms_RdbmsView" = None):
        self.inherited = inherited
        self.fields30 = fields30
        self.RdbmsViewField = RdbmsViewField
        
    @property
    def inherited(self) -> bool:
        return self.__inherited

    @inherited.setter
    def inherited(self, inherited: bool):
        self.__inherited = inherited

    @property
    def fields30(self):
        return self.__fields30

    @fields30.setter
    def fields30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdbms_RdbmsViewField__fields30", None)
        self.__fields30 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RdbmsView"):
                opp_val = getattr(old_value, "RdbmsView", None)
                if opp_val == self:
                    setattr(old_value, "RdbmsView", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RdbmsView"):
                opp_val = getattr(value, "RdbmsView", None)
                setattr(value, "RdbmsView", self)

    @property
    def RdbmsViewField(self):
        return self.__RdbmsViewField

    @RdbmsViewField.setter
    def RdbmsViewField(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdbms_RdbmsViewField__RdbmsViewField", None)
        self.__RdbmsViewField = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "view"):
                opp_val = getattr(old_value, "view", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "view"):
                opp_val = getattr(value, "view", None)
                if opp_val is None:
                    setattr(value, "view", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class rdbms_RdbmsTableOperation(RdbmsElement):

    pass
class rdbms_RdbmsView(RdbmsElement):

    def __init__(self, originUuid: str, rdbms_RdbmsView26: "rdbms_RdbmsViewIdentifierField" = None, view28: set["rdbms_RdbmsTableAlias"] = None, RdbmsView: "rdbms_RdbmsViewField" = None, view: set["rdbms_RdbmsViewField"] = None, rdbms_RdbmsView: "rdbms_RdbmsTableAlias" = None, rdbms_RdbmsView24: set["rdbms_RdbmsViewRelation"] = None, rdbms_RdbmsView39: "rdbms_RdbmsModel" = None, RdbmsView52: "rdbms_RdbmsTableAlias" = None, rdbms_RdbmsView94: "rdbms_RdbmsViewRecord" = None):
        self.originUuid = originUuid
        self.rdbms_RdbmsView26 = rdbms_RdbmsView26
        self.view28 = view28 if view28 is not None else set()
        self.RdbmsView = RdbmsView
        self.view = view if view is not None else set()
        self.rdbms_RdbmsView = rdbms_RdbmsView
        self.rdbms_RdbmsView24 = rdbms_RdbmsView24 if rdbms_RdbmsView24 is not None else set()
        self.rdbms_RdbmsView39 = rdbms_RdbmsView39
        self.RdbmsView52 = RdbmsView52
        self.rdbms_RdbmsView94 = rdbms_RdbmsView94
        
    @property
    def originUuid(self) -> str:
        return self.__originUuid

    @originUuid.setter
    def originUuid(self, originUuid: str):
        self.__originUuid = originUuid

    @property
    def RdbmsView52(self):
        return self.__RdbmsView52

    @RdbmsView52.setter
    def RdbmsView52(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdbms_RdbmsView__RdbmsView52", None)
        self.__RdbmsView52 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tables"):
                opp_val = getattr(old_value, "tables", None)
                if opp_val == self:
                    setattr(old_value, "tables", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tables"):
                opp_val = getattr(value, "tables", None)
                setattr(value, "tables", self)

    @property
    def view28(self):
        return self.__view28

    @view28.setter
    def view28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdbms_RdbmsView__view28", None)
        self.__view28 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "RdbmsTableAlias"):
                    opp_val = getattr(item, "RdbmsTableAlias", None)
                    
                    if opp_val == self:
                        setattr(item, "RdbmsTableAlias", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "RdbmsTableAlias"):
                    opp_val = getattr(item, "RdbmsTableAlias", None)
                    
                    setattr(item, "RdbmsTableAlias", self)
                    

    @property
    def rdbms_RdbmsView24(self):
        return self.__rdbms_RdbmsView24

    @rdbms_RdbmsView24.setter
    def rdbms_RdbmsView24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdbms_RdbmsView__rdbms_RdbmsView24", None)
        self.__rdbms_RdbmsView24 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "rdbms_RdbmsViewRelation"):
                    opp_val = getattr(item, "rdbms_RdbmsViewRelation", None)
                    
                    if opp_val == self:
                        setattr(item, "rdbms_RdbmsViewRelation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "rdbms_RdbmsViewRelation"):
                    opp_val = getattr(item, "rdbms_RdbmsViewRelation", None)
                    
                    setattr(item, "rdbms_RdbmsViewRelation", self)
                    

    @property
    def rdbms_RdbmsView94(self):
        return self.__rdbms_RdbmsView94

    @rdbms_RdbmsView94.setter
    def rdbms_RdbmsView94(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdbms_RdbmsView__rdbms_RdbmsView94", None)
        self.__rdbms_RdbmsView94 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rdbms_RdbmsViewRecord93"):
                opp_val = getattr(old_value, "rdbms_RdbmsViewRecord93", None)
                if opp_val == self:
                    setattr(old_value, "rdbms_RdbmsViewRecord93", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rdbms_RdbmsViewRecord93"):
                opp_val = getattr(value, "rdbms_RdbmsViewRecord93", None)
                setattr(value, "rdbms_RdbmsViewRecord93", self)

    @property
    def rdbms_RdbmsView26(self):
        return self.__rdbms_RdbmsView26

    @rdbms_RdbmsView26.setter
    def rdbms_RdbmsView26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdbms_RdbmsView__rdbms_RdbmsView26", None)
        self.__rdbms_RdbmsView26 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rdbms_RdbmsViewIdentifierField"):
                opp_val = getattr(old_value, "rdbms_RdbmsViewIdentifierField", None)
                if opp_val == self:
                    setattr(old_value, "rdbms_RdbmsViewIdentifierField", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rdbms_RdbmsViewIdentifierField"):
                opp_val = getattr(value, "rdbms_RdbmsViewIdentifierField", None)
                setattr(value, "rdbms_RdbmsViewIdentifierField", self)

    @property
    def view(self):
        return self.__view

    @view.setter
    def view(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdbms_RdbmsView__view", None)
        self.__view = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "RdbmsViewField"):
                    opp_val = getattr(item, "RdbmsViewField", None)
                    
                    if opp_val == self:
                        setattr(item, "RdbmsViewField", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "RdbmsViewField"):
                    opp_val = getattr(item, "RdbmsViewField", None)
                    
                    setattr(item, "RdbmsViewField", self)
                    

    @property
    def rdbms_RdbmsView(self):
        return self.__rdbms_RdbmsView

    @rdbms_RdbmsView.setter
    def rdbms_RdbmsView(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdbms_RdbmsView__rdbms_RdbmsView", None)
        self.__rdbms_RdbmsView = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rdbms_RdbmsTableAlias"):
                opp_val = getattr(old_value, "rdbms_RdbmsTableAlias", None)
                if opp_val == self:
                    setattr(old_value, "rdbms_RdbmsTableAlias", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rdbms_RdbmsTableAlias"):
                opp_val = getattr(value, "rdbms_RdbmsTableAlias", None)
                setattr(value, "rdbms_RdbmsTableAlias", self)

    @property
    def rdbms_RdbmsView39(self):
        return self.__rdbms_RdbmsView39

    @rdbms_RdbmsView39.setter
    def rdbms_RdbmsView39(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdbms_RdbmsView__rdbms_RdbmsView39", None)
        self.__rdbms_RdbmsView39 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rdbms_RdbmsModel38"):
                opp_val = getattr(old_value, "rdbms_RdbmsModel38", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rdbms_RdbmsModel38"):
                opp_val = getattr(value, "rdbms_RdbmsModel38", None)
                if opp_val is None:
                    setattr(value, "rdbms_RdbmsModel38", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def RdbmsView(self):
        return self.__RdbmsView

    @RdbmsView.setter
    def RdbmsView(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdbms_RdbmsView__RdbmsView", None)
        self.__RdbmsView = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fields30"):
                opp_val = getattr(old_value, "fields30", None)
                if opp_val == self:
                    setattr(old_value, "fields30", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fields30"):
                opp_val = getattr(value, "fields30", None)
                setattr(value, "fields30", self)

class rdbms_RdbmsTableAlias(RdbmsElement):

    pass
class rdbms_RdbmsFieldOperation(RdbmsElement):

    def __init__(self, reviewRequired: bool, rdbms_RdbmsFieldOperation: "rdbms_RdbmsField" = None):
        self.reviewRequired = reviewRequired
        self.rdbms_RdbmsFieldOperation = rdbms_RdbmsFieldOperation
        
    @property
    def reviewRequired(self) -> bool:
        return self.__reviewRequired

    @reviewRequired.setter
    def reviewRequired(self, reviewRequired: bool):
        self.__reviewRequired = reviewRequired

    @property
    def rdbms_RdbmsFieldOperation(self):
        return self.__rdbms_RdbmsFieldOperation

    @rdbms_RdbmsFieldOperation.setter
    def rdbms_RdbmsFieldOperation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdbms_RdbmsFieldOperation__rdbms_RdbmsFieldOperation", None)
        self.__rdbms_RdbmsFieldOperation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rdbms_RdbmsField66"):
                opp_val = getattr(old_value, "rdbms_RdbmsField66", None)
                if opp_val == self:
                    setattr(old_value, "rdbms_RdbmsField66", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rdbms_RdbmsField66"):
                opp_val = getattr(value, "rdbms_RdbmsField66", None)
                setattr(value, "rdbms_RdbmsField66", self)

class rdbms_RdbmsExpression(RdbmsElement):

    def __init__(self, expression: str, rdbms_RdbmsExpression: "rdbms_RdbmsViewExpressionField" = None):
        self.expression = expression
        self.rdbms_RdbmsExpression = rdbms_RdbmsExpression
        
    @property
    def expression(self) -> str:
        return self.__expression

    @expression.setter
    def expression(self, expression: str):
        self.__expression = expression

    @property
    def rdbms_RdbmsExpression(self):
        return self.__rdbms_RdbmsExpression

    @rdbms_RdbmsExpression.setter
    def rdbms_RdbmsExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdbms_RdbmsExpression__rdbms_RdbmsExpression", None)
        self.__rdbms_RdbmsExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rdbms_RdbmsViewExpressionField"):
                opp_val = getattr(old_value, "rdbms_RdbmsViewExpressionField", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rdbms_RdbmsViewExpressionField"):
                opp_val = getattr(value, "rdbms_RdbmsViewExpressionField", None)
                if opp_val is None:
                    setattr(value, "rdbms_RdbmsViewExpressionField", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class rdbms_RdbmsField(RdbmsElement):

    def __init__(self, mandatory: bool, rdbmsTypeName: str, size: int, precision: int, scale: int, storageByte: int, fields: "rdbms_RdbmsTable" = None, rdbms_RdbmsField: "rdbms_RdbmsFieldType" = None, RdbmsField: "rdbms_RdbmsTable" = None, rdbms_RdbmsField15: "rdbms_RdbmsUniqueConstraint" = None, rdbms_RdbmsField66: "rdbms_RdbmsFieldOperation" = None, rdbms_RdbmsField69: "rdbms_RdbmsModifyFieldOperation" = None, rdbms_RdbmsField83: "rdbms_RdbmsViewTableField" = None, rdbms_RdbmsField89: "rdbms_RdbmsIndex" = None):
        self.mandatory = mandatory
        self.rdbmsTypeName = rdbmsTypeName
        self.size = size
        self.precision = precision
        self.scale = scale
        self.storageByte = storageByte
        self.fields = fields
        self.rdbms_RdbmsField = rdbms_RdbmsField
        self.RdbmsField = RdbmsField
        self.rdbms_RdbmsField15 = rdbms_RdbmsField15
        self.rdbms_RdbmsField66 = rdbms_RdbmsField66
        self.rdbms_RdbmsField69 = rdbms_RdbmsField69
        self.rdbms_RdbmsField83 = rdbms_RdbmsField83
        self.rdbms_RdbmsField89 = rdbms_RdbmsField89
        
    @property
    def rdbmsTypeName(self) -> str:
        return self.__rdbmsTypeName

    @rdbmsTypeName.setter
    def rdbmsTypeName(self, rdbmsTypeName: str):
        self.__rdbmsTypeName = rdbmsTypeName

    @property
    def scale(self) -> int:
        return self.__scale

    @scale.setter
    def scale(self, scale: int):
        self.__scale = scale

    @property
    def storageByte(self) -> int:
        return self.__storageByte

    @storageByte.setter
    def storageByte(self, storageByte: int):
        self.__storageByte = storageByte

    @property
    def precision(self) -> int:
        return self.__precision

    @precision.setter
    def precision(self, precision: int):
        self.__precision = precision

    @property
    def mandatory(self) -> bool:
        return self.__mandatory

    @mandatory.setter
    def mandatory(self, mandatory: bool):
        self.__mandatory = mandatory

    @property
    def size(self) -> int:
        return self.__size

    @size.setter
    def size(self, size: int):
        self.__size = size

    @property
    def rdbms_RdbmsField83(self):
        return self.__rdbms_RdbmsField83

    @rdbms_RdbmsField83.setter
    def rdbms_RdbmsField83(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdbms_RdbmsField__rdbms_RdbmsField83", None)
        self.__rdbms_RdbmsField83 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rdbms_RdbmsViewTableField"):
                opp_val = getattr(old_value, "rdbms_RdbmsViewTableField", None)
                if opp_val == self:
                    setattr(old_value, "rdbms_RdbmsViewTableField", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rdbms_RdbmsViewTableField"):
                opp_val = getattr(value, "rdbms_RdbmsViewTableField", None)
                setattr(value, "rdbms_RdbmsViewTableField", self)

    @property
    def rdbms_RdbmsField89(self):
        return self.__rdbms_RdbmsField89

    @rdbms_RdbmsField89.setter
    def rdbms_RdbmsField89(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdbms_RdbmsField__rdbms_RdbmsField89", None)
        self.__rdbms_RdbmsField89 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rdbms_RdbmsIndex"):
                opp_val = getattr(old_value, "rdbms_RdbmsIndex", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rdbms_RdbmsIndex"):
                opp_val = getattr(value, "rdbms_RdbmsIndex", None)
                if opp_val is None:
                    setattr(value, "rdbms_RdbmsIndex", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def fields(self):
        return self.__fields

    @fields.setter
    def fields(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdbms_RdbmsField__fields", None)
        self.__fields = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RdbmsTable"):
                opp_val = getattr(old_value, "RdbmsTable", None)
                if opp_val == self:
                    setattr(old_value, "RdbmsTable", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RdbmsTable"):
                opp_val = getattr(value, "RdbmsTable", None)
                setattr(value, "RdbmsTable", self)

    @property
    def RdbmsField(self):
        return self.__RdbmsField

    @RdbmsField.setter
    def RdbmsField(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdbms_RdbmsField__RdbmsField", None)
        self.__RdbmsField = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "table"):
                opp_val = getattr(old_value, "table", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "table"):
                opp_val = getattr(value, "table", None)
                if opp_val is None:
                    setattr(value, "table", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def rdbms_RdbmsField66(self):
        return self.__rdbms_RdbmsField66

    @rdbms_RdbmsField66.setter
    def rdbms_RdbmsField66(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdbms_RdbmsField__rdbms_RdbmsField66", None)
        self.__rdbms_RdbmsField66 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rdbms_RdbmsFieldOperation"):
                opp_val = getattr(old_value, "rdbms_RdbmsFieldOperation", None)
                if opp_val == self:
                    setattr(old_value, "rdbms_RdbmsFieldOperation", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rdbms_RdbmsFieldOperation"):
                opp_val = getattr(value, "rdbms_RdbmsFieldOperation", None)
                setattr(value, "rdbms_RdbmsFieldOperation", self)

    @property
    def rdbms_RdbmsField69(self):
        return self.__rdbms_RdbmsField69

    @rdbms_RdbmsField69.setter
    def rdbms_RdbmsField69(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdbms_RdbmsField__rdbms_RdbmsField69", None)
        self.__rdbms_RdbmsField69 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rdbms_RdbmsModifyFieldOperation68"):
                opp_val = getattr(old_value, "rdbms_RdbmsModifyFieldOperation68", None)
                if opp_val == self:
                    setattr(old_value, "rdbms_RdbmsModifyFieldOperation68", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rdbms_RdbmsModifyFieldOperation68"):
                opp_val = getattr(value, "rdbms_RdbmsModifyFieldOperation68", None)
                setattr(value, "rdbms_RdbmsModifyFieldOperation68", self)

    @property
    def rdbms_RdbmsField15(self):
        return self.__rdbms_RdbmsField15

    @rdbms_RdbmsField15.setter
    def rdbms_RdbmsField15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdbms_RdbmsField__rdbms_RdbmsField15", None)
        self.__rdbms_RdbmsField15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rdbms_RdbmsUniqueConstraint"):
                opp_val = getattr(old_value, "rdbms_RdbmsUniqueConstraint", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rdbms_RdbmsUniqueConstraint"):
                opp_val = getattr(value, "rdbms_RdbmsUniqueConstraint", None)
                if opp_val is None:
                    setattr(value, "rdbms_RdbmsUniqueConstraint", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def rdbms_RdbmsField(self):
        return self.__rdbms_RdbmsField

    @rdbms_RdbmsField.setter
    def rdbms_RdbmsField(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdbms_RdbmsField__rdbms_RdbmsField", None)
        self.__rdbms_RdbmsField = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rdbms_RdbmsFieldType"):
                opp_val = getattr(old_value, "rdbms_RdbmsFieldType", None)
                if opp_val == self:
                    setattr(old_value, "rdbms_RdbmsFieldType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rdbms_RdbmsFieldType"):
                opp_val = getattr(value, "rdbms_RdbmsFieldType", None)
                setattr(value, "rdbms_RdbmsFieldType", self)

class rdbms_RdbmsIndex(RdbmsElement):

    def __init__(self, unique: bool, RdbmsIndex: "rdbms_RdbmsTable" = None, indexes: "rdbms_RdbmsTable" = None, rdbms_RdbmsIndex: set["rdbms_RdbmsField"] = None):
        self.unique = unique
        self.RdbmsIndex = RdbmsIndex
        self.indexes = indexes
        self.rdbms_RdbmsIndex = rdbms_RdbmsIndex if rdbms_RdbmsIndex is not None else set()
        
    @property
    def unique(self) -> bool:
        return self.__unique

    @unique.setter
    def unique(self, unique: bool):
        self.__unique = unique

    @property
    def rdbms_RdbmsIndex(self):
        return self.__rdbms_RdbmsIndex

    @rdbms_RdbmsIndex.setter
    def rdbms_RdbmsIndex(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdbms_RdbmsIndex__rdbms_RdbmsIndex", None)
        self.__rdbms_RdbmsIndex = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "rdbms_RdbmsField89"):
                    opp_val = getattr(item, "rdbms_RdbmsField89", None)
                    
                    if opp_val == self:
                        setattr(item, "rdbms_RdbmsField89", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "rdbms_RdbmsField89"):
                    opp_val = getattr(item, "rdbms_RdbmsField89", None)
                    
                    setattr(item, "rdbms_RdbmsField89", self)
                    

    @property
    def indexes(self):
        return self.__indexes

    @indexes.setter
    def indexes(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdbms_RdbmsIndex__indexes", None)
        self.__indexes = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RdbmsTable87"):
                opp_val = getattr(old_value, "RdbmsTable87", None)
                if opp_val == self:
                    setattr(old_value, "RdbmsTable87", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RdbmsTable87"):
                opp_val = getattr(value, "RdbmsTable87", None)
                setattr(value, "RdbmsTable87", self)

    @property
    def RdbmsIndex(self):
        return self.__RdbmsIndex

    @RdbmsIndex.setter
    def RdbmsIndex(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdbms_RdbmsIndex__RdbmsIndex", None)
        self.__RdbmsIndex = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "table5"):
                opp_val = getattr(old_value, "table5", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "table5"):
                opp_val = getattr(value, "table5", None)
                if opp_val is None:
                    setattr(value, "table5", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class rdbms_RdbmsTable(RdbmsElement):

    pass
class rdbms_RdbmsElement(ABC):

    def __init__(self, name: str, uuid: str, shortName: str, fullName: str, description: str, sqlName: str, originalName: str, originalPackage: str):
        self.name = name
        self.uuid = uuid
        self.shortName = shortName
        self.fullName = fullName
        self.description = description
        self.sqlName = sqlName
        self.originalName = originalName
        self.originalPackage = originalPackage
        
    @property
    def sqlName(self) -> str:
        return self.__sqlName

    @sqlName.setter
    def sqlName(self, sqlName: str):
        self.__sqlName = sqlName

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def originalName(self) -> str:
        return self.__originalName

    @originalName.setter
    def originalName(self, originalName: str):
        self.__originalName = originalName

    @property
    def fullName(self) -> str:
        return self.__fullName

    @fullName.setter
    def fullName(self, fullName: str):
        self.__fullName = fullName

    @property
    def uuid(self) -> str:
        return self.__uuid

    @uuid.setter
    def uuid(self, uuid: str):
        self.__uuid = uuid

    @property
    def originalPackage(self) -> str:
        return self.__originalPackage

    @originalPackage.setter
    def originalPackage(self, originalPackage: str):
        self.__originalPackage = originalPackage

    @property
    def shortName(self) -> str:
        return self.__shortName

    @shortName.setter
    def shortName(self, shortName: str):
        self.__shortName = shortName
