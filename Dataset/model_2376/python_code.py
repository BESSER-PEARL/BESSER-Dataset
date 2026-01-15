from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class umltordbms_Column:

    pass
class umltordbms_ToColumn:

    pass
class umltordbms_PrimitiveDataType:

    pass
class umltordbms_Schema:

    pass
class umltordbms_Package:

    pass
class umltordbms_PrimitiveToName:

    def __init__(self, name: str, typeName: str, umltordbms_PrimitiveToName: "umltordbms_AttributeToColumn" = None, primitivesToNames: "umltordbms_PackageToSchema" = None, umltordbms_PrimitiveToName33: "umltordbms_PrimitiveDataType" = None, PrimitiveToName: "umltordbms_PackageToSchema" = None):
        self.name = name
        self.typeName = typeName
        self.umltordbms_PrimitiveToName = umltordbms_PrimitiveToName
        self.primitivesToNames = primitivesToNames
        self.umltordbms_PrimitiveToName33 = umltordbms_PrimitiveToName33
        self.PrimitiveToName = PrimitiveToName
        
    @property
    def typeName(self) -> str:
        return self.__typeName

    @typeName.setter
    def typeName(self, typeName: str):
        self.__typeName = typeName

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def primitivesToNames(self):
        return self.__primitivesToNames

    @primitivesToNames.setter
    def primitivesToNames(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umltordbms_PrimitiveToName__primitivesToNames", None)
        self.__primitivesToNames = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PackageToSchema31"):
                opp_val = getattr(old_value, "PackageToSchema31", None)
                if opp_val == self:
                    setattr(old_value, "PackageToSchema31", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PackageToSchema31"):
                opp_val = getattr(value, "PackageToSchema31", None)
                setattr(value, "PackageToSchema31", self)

    @property
    def umltordbms_PrimitiveToName(self):
        return self.__umltordbms_PrimitiveToName

    @umltordbms_PrimitiveToName.setter
    def umltordbms_PrimitiveToName(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umltordbms_PrimitiveToName__umltordbms_PrimitiveToName", None)
        self.__umltordbms_PrimitiveToName = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "umltordbms_AttributeToColumn"):
                opp_val = getattr(old_value, "umltordbms_AttributeToColumn", None)
                if opp_val == self:
                    setattr(old_value, "umltordbms_AttributeToColumn", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "umltordbms_AttributeToColumn"):
                opp_val = getattr(value, "umltordbms_AttributeToColumn", None)
                setattr(value, "umltordbms_AttributeToColumn", self)

    @property
    def umltordbms_PrimitiveToName33(self):
        return self.__umltordbms_PrimitiveToName33

    @umltordbms_PrimitiveToName33.setter
    def umltordbms_PrimitiveToName33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umltordbms_PrimitiveToName__umltordbms_PrimitiveToName33", None)
        self.__umltordbms_PrimitiveToName33 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "umltordbms_PrimitiveDataType"):
                opp_val = getattr(old_value, "umltordbms_PrimitiveDataType", None)
                if opp_val == self:
                    setattr(old_value, "umltordbms_PrimitiveDataType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "umltordbms_PrimitiveDataType"):
                opp_val = getattr(value, "umltordbms_PrimitiveDataType", None)
                setattr(value, "umltordbms_PrimitiveDataType", self)

    @property
    def PrimitiveToName(self):
        return self.__PrimitiveToName

    @PrimitiveToName.setter
    def PrimitiveToName(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umltordbms_PrimitiveToName__PrimitiveToName", None)
        self.__PrimitiveToName = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "owner26"):
                opp_val = getattr(old_value, "owner26", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "owner26"):
                opp_val = getattr(value, "owner26", None)
                if opp_val is None:
                    setattr(value, "owner26", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class ToColumn:

    pass
class umltordbms_AssociationToForeignKey(ToColumn):

    def __init__(self, name: str, umltordbms_AssociationToForeignKey: "umltordbms_ClassToTable" = None, associationsToForeignKeys: "umltordbms_ClassToTable" = None, umltordbms_AssociationToForeignKey4: "umltordbms_Association" = None, umltordbms_AssociationToForeignKey6: "umltordbms_ForeignKey" = None, AssociationToForeignKey: "umltordbms_ClassToTable" = None):
        self.name = name
        self.umltordbms_AssociationToForeignKey = umltordbms_AssociationToForeignKey
        self.associationsToForeignKeys = associationsToForeignKeys
        self.umltordbms_AssociationToForeignKey4 = umltordbms_AssociationToForeignKey4
        self.umltordbms_AssociationToForeignKey6 = umltordbms_AssociationToForeignKey6
        self.AssociationToForeignKey = AssociationToForeignKey
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def umltordbms_AssociationToForeignKey(self):
        return self.__umltordbms_AssociationToForeignKey

    @umltordbms_AssociationToForeignKey.setter
    def umltordbms_AssociationToForeignKey(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umltordbms_AssociationToForeignKey__umltordbms_AssociationToForeignKey", None)
        self.__umltordbms_AssociationToForeignKey = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "umltordbms_ClassToTable"):
                opp_val = getattr(old_value, "umltordbms_ClassToTable", None)
                if opp_val == self:
                    setattr(old_value, "umltordbms_ClassToTable", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "umltordbms_ClassToTable"):
                opp_val = getattr(value, "umltordbms_ClassToTable", None)
                setattr(value, "umltordbms_ClassToTable", self)

    @property
    def umltordbms_AssociationToForeignKey4(self):
        return self.__umltordbms_AssociationToForeignKey4

    @umltordbms_AssociationToForeignKey4.setter
    def umltordbms_AssociationToForeignKey4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umltordbms_AssociationToForeignKey__umltordbms_AssociationToForeignKey4", None)
        self.__umltordbms_AssociationToForeignKey4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "umltordbms_Association"):
                opp_val = getattr(old_value, "umltordbms_Association", None)
                if opp_val == self:
                    setattr(old_value, "umltordbms_Association", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "umltordbms_Association"):
                opp_val = getattr(value, "umltordbms_Association", None)
                setattr(value, "umltordbms_Association", self)

    @property
    def umltordbms_AssociationToForeignKey6(self):
        return self.__umltordbms_AssociationToForeignKey6

    @umltordbms_AssociationToForeignKey6.setter
    def umltordbms_AssociationToForeignKey6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umltordbms_AssociationToForeignKey__umltordbms_AssociationToForeignKey6", None)
        self.__umltordbms_AssociationToForeignKey6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "umltordbms_ForeignKey"):
                opp_val = getattr(old_value, "umltordbms_ForeignKey", None)
                if opp_val == self:
                    setattr(old_value, "umltordbms_ForeignKey", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "umltordbms_ForeignKey"):
                opp_val = getattr(value, "umltordbms_ForeignKey", None)
                setattr(value, "umltordbms_ForeignKey", self)

    @property
    def associationsToForeignKeys(self):
        return self.__associationsToForeignKeys

    @associationsToForeignKeys.setter
    def associationsToForeignKeys(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umltordbms_AssociationToForeignKey__associationsToForeignKeys", None)
        self.__associationsToForeignKeys = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ClassToTable"):
                opp_val = getattr(old_value, "ClassToTable", None)
                if opp_val == self:
                    setattr(old_value, "ClassToTable", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ClassToTable"):
                opp_val = getattr(value, "ClassToTable", None)
                setattr(value, "ClassToTable", self)

    @property
    def AssociationToForeignKey(self):
        return self.__AssociationToForeignKey

    @AssociationToForeignKey.setter
    def AssociationToForeignKey(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umltordbms_AssociationToForeignKey__AssociationToForeignKey", None)
        self.__AssociationToForeignKey = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "owner"):
                opp_val = getattr(old_value, "owner", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "owner"):
                opp_val = getattr(value, "owner", None)
                if opp_val is None:
                    setattr(value, "owner", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class FromAttribute:

    pass
class umltordbms_AttributeToColumn(ToColumn, FromAttribute):

    pass
class umltordbms_Attribute:

    pass
class umltordbms_FromAttributeOwner(ABC):

    pass
class umltordbms_FromAttribute(ABC):

    def __init__(self, name: str, kind: str, fromAttributes: "umltordbms_FromAttributeOwner" = None, umltordbms_FromAttribute: set["umltordbms_AttributeToColumn"] = None, umltordbms_FromAttribute19: "umltordbms_Attribute" = None, FromAttribute: "umltordbms_FromAttributeOwner" = None):
        self.name = name
        self.kind = kind
        self.fromAttributes = fromAttributes
        self.umltordbms_FromAttribute = umltordbms_FromAttribute if umltordbms_FromAttribute is not None else set()
        self.umltordbms_FromAttribute19 = umltordbms_FromAttribute19
        self.FromAttribute = FromAttribute
        
    @property
    def kind(self) -> str:
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def FromAttribute(self):
        return self.__FromAttribute

    @FromAttribute.setter
    def FromAttribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umltordbms_FromAttribute__FromAttribute", None)
        self.__FromAttribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "owner21"):
                opp_val = getattr(old_value, "owner21", None)
                if opp_val == self:
                    setattr(old_value, "owner21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "owner21"):
                opp_val = getattr(value, "owner21", None)
                setattr(value, "owner21", self)

    @property
    def fromAttributes(self):
        return self.__fromAttributes

    @fromAttributes.setter
    def fromAttributes(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umltordbms_FromAttribute__fromAttributes", None)
        self.__fromAttributes = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "FromAttributeOwner"):
                opp_val = getattr(old_value, "FromAttributeOwner", None)
                if opp_val == self:
                    setattr(old_value, "FromAttributeOwner", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FromAttributeOwner"):
                opp_val = getattr(value, "FromAttributeOwner", None)
                setattr(value, "FromAttributeOwner", self)

    @property
    def umltordbms_FromAttribute(self):
        return self.__umltordbms_FromAttribute

    @umltordbms_FromAttribute.setter
    def umltordbms_FromAttribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umltordbms_FromAttribute__umltordbms_FromAttribute", None)
        self.__umltordbms_FromAttribute = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "umltordbms_AttributeToColumn17"):
                    opp_val = getattr(item, "umltordbms_AttributeToColumn17", None)
                    
                    if opp_val == self:
                        setattr(item, "umltordbms_AttributeToColumn17", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "umltordbms_AttributeToColumn17"):
                    opp_val = getattr(item, "umltordbms_AttributeToColumn17", None)
                    
                    setattr(item, "umltordbms_AttributeToColumn17", self)
                    

    @property
    def umltordbms_FromAttribute19(self):
        return self.__umltordbms_FromAttribute19

    @umltordbms_FromAttribute19.setter
    def umltordbms_FromAttribute19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umltordbms_FromAttribute__umltordbms_FromAttribute19", None)
        self.__umltordbms_FromAttribute19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "umltordbms_Attribute"):
                opp_val = getattr(old_value, "umltordbms_Attribute", None)
                if opp_val == self:
                    setattr(old_value, "umltordbms_Attribute", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "umltordbms_Attribute"):
                opp_val = getattr(value, "umltordbms_Attribute", None)
                setattr(value, "umltordbms_Attribute", self)

class umltordbms_Key:

    pass
class umltordbms_Table:

    pass
class umltordbms_Class:

    pass
class umltordbms_PackageToSchema:

    def __init__(self, name: str, PackageToSchema: "umltordbms_ClassToTable" = None, umltordbms_PackageToSchema: "umltordbms_Package" = None, umltordbms_PackageToSchema29: "umltordbms_Schema" = None, PackageToSchema31: "umltordbms_PrimitiveToName" = None, owner23: set["umltordbms_ClassToTable"] = None, owner26: set["umltordbms_PrimitiveToName"] = None):
        self.name = name
        self.PackageToSchema = PackageToSchema
        self.umltordbms_PackageToSchema = umltordbms_PackageToSchema
        self.umltordbms_PackageToSchema29 = umltordbms_PackageToSchema29
        self.PackageToSchema31 = PackageToSchema31
        self.owner23 = owner23 if owner23 is not None else set()
        self.owner26 = owner26 if owner26 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def PackageToSchema31(self):
        return self.__PackageToSchema31

    @PackageToSchema31.setter
    def PackageToSchema31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umltordbms_PackageToSchema__PackageToSchema31", None)
        self.__PackageToSchema31 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "primitivesToNames"):
                opp_val = getattr(old_value, "primitivesToNames", None)
                if opp_val == self:
                    setattr(old_value, "primitivesToNames", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "primitivesToNames"):
                opp_val = getattr(value, "primitivesToNames", None)
                setattr(value, "primitivesToNames", self)

    @property
    def umltordbms_PackageToSchema(self):
        return self.__umltordbms_PackageToSchema

    @umltordbms_PackageToSchema.setter
    def umltordbms_PackageToSchema(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umltordbms_PackageToSchema__umltordbms_PackageToSchema", None)
        self.__umltordbms_PackageToSchema = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "umltordbms_Package"):
                opp_val = getattr(old_value, "umltordbms_Package", None)
                if opp_val == self:
                    setattr(old_value, "umltordbms_Package", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "umltordbms_Package"):
                opp_val = getattr(value, "umltordbms_Package", None)
                setattr(value, "umltordbms_Package", self)

    @property
    def owner26(self):
        return self.__owner26

    @owner26.setter
    def owner26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umltordbms_PackageToSchema__owner26", None)
        self.__owner26 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "PrimitiveToName"):
                    opp_val = getattr(item, "PrimitiveToName", None)
                    
                    if opp_val == self:
                        setattr(item, "PrimitiveToName", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "PrimitiveToName"):
                    opp_val = getattr(item, "PrimitiveToName", None)
                    
                    setattr(item, "PrimitiveToName", self)
                    

    @property
    def umltordbms_PackageToSchema29(self):
        return self.__umltordbms_PackageToSchema29

    @umltordbms_PackageToSchema29.setter
    def umltordbms_PackageToSchema29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umltordbms_PackageToSchema__umltordbms_PackageToSchema29", None)
        self.__umltordbms_PackageToSchema29 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "umltordbms_Schema"):
                opp_val = getattr(old_value, "umltordbms_Schema", None)
                if opp_val == self:
                    setattr(old_value, "umltordbms_Schema", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "umltordbms_Schema"):
                opp_val = getattr(value, "umltordbms_Schema", None)
                setattr(value, "umltordbms_Schema", self)

    @property
    def PackageToSchema(self):
        return self.__PackageToSchema

    @PackageToSchema.setter
    def PackageToSchema(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umltordbms_PackageToSchema__PackageToSchema", None)
        self.__PackageToSchema = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "classesToTables"):
                opp_val = getattr(old_value, "classesToTables", None)
                if opp_val == self:
                    setattr(old_value, "classesToTables", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "classesToTables"):
                opp_val = getattr(value, "classesToTables", None)
                setattr(value, "classesToTables", self)

    @property
    def owner23(self):
        return self.__owner23

    @owner23.setter
    def owner23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umltordbms_PackageToSchema__owner23", None)
        self.__owner23 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ClassToTable24"):
                    opp_val = getattr(item, "ClassToTable24", None)
                    
                    if opp_val == self:
                        setattr(item, "ClassToTable24", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ClassToTable24"):
                    opp_val = getattr(item, "ClassToTable24", None)
                    
                    setattr(item, "ClassToTable24", self)
                    

class FromAttributeOwner:

    pass
class umltordbms_NonLeafAttribute(FromAttributeOwner, FromAttribute):

    pass
class umltordbms_ClassToTable(ToColumn, FromAttributeOwner):

    def __init__(self, name: str, umltordbms_ClassToTable: "umltordbms_AssociationToForeignKey" = None, ClassToTable: "umltordbms_AssociationToForeignKey" = None, classesToTables: "umltordbms_PackageToSchema" = None, owner: set["umltordbms_AssociationToForeignKey"] = None, umltordbms_ClassToTable10: "umltordbms_Class" = None, umltordbms_ClassToTable12: "umltordbms_Table" = None, umltordbms_ClassToTable14: "umltordbms_Key" = None, ClassToTable24: "umltordbms_PackageToSchema" = None):
        self.name = name
        self.umltordbms_ClassToTable = umltordbms_ClassToTable
        self.ClassToTable = ClassToTable
        self.classesToTables = classesToTables
        self.owner = owner if owner is not None else set()
        self.umltordbms_ClassToTable10 = umltordbms_ClassToTable10
        self.umltordbms_ClassToTable12 = umltordbms_ClassToTable12
        self.umltordbms_ClassToTable14 = umltordbms_ClassToTable14
        self.ClassToTable24 = ClassToTable24
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def umltordbms_ClassToTable14(self):
        return self.__umltordbms_ClassToTable14

    @umltordbms_ClassToTable14.setter
    def umltordbms_ClassToTable14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umltordbms_ClassToTable__umltordbms_ClassToTable14", None)
        self.__umltordbms_ClassToTable14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "umltordbms_Key"):
                opp_val = getattr(old_value, "umltordbms_Key", None)
                if opp_val == self:
                    setattr(old_value, "umltordbms_Key", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "umltordbms_Key"):
                opp_val = getattr(value, "umltordbms_Key", None)
                setattr(value, "umltordbms_Key", self)

    @property
    def umltordbms_ClassToTable10(self):
        return self.__umltordbms_ClassToTable10

    @umltordbms_ClassToTable10.setter
    def umltordbms_ClassToTable10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umltordbms_ClassToTable__umltordbms_ClassToTable10", None)
        self.__umltordbms_ClassToTable10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "umltordbms_Class"):
                opp_val = getattr(old_value, "umltordbms_Class", None)
                if opp_val == self:
                    setattr(old_value, "umltordbms_Class", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "umltordbms_Class"):
                opp_val = getattr(value, "umltordbms_Class", None)
                setattr(value, "umltordbms_Class", self)

    @property
    def ClassToTable(self):
        return self.__ClassToTable

    @ClassToTable.setter
    def ClassToTable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umltordbms_ClassToTable__ClassToTable", None)
        self.__ClassToTable = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "associationsToForeignKeys"):
                opp_val = getattr(old_value, "associationsToForeignKeys", None)
                if opp_val == self:
                    setattr(old_value, "associationsToForeignKeys", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "associationsToForeignKeys"):
                opp_val = getattr(value, "associationsToForeignKeys", None)
                setattr(value, "associationsToForeignKeys", self)

    @property
    def owner(self):
        return self.__owner

    @owner.setter
    def owner(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umltordbms_ClassToTable__owner", None)
        self.__owner = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "AssociationToForeignKey"):
                    opp_val = getattr(item, "AssociationToForeignKey", None)
                    
                    if opp_val == self:
                        setattr(item, "AssociationToForeignKey", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "AssociationToForeignKey"):
                    opp_val = getattr(item, "AssociationToForeignKey", None)
                    
                    setattr(item, "AssociationToForeignKey", self)
                    

    @property
    def umltordbms_ClassToTable12(self):
        return self.__umltordbms_ClassToTable12

    @umltordbms_ClassToTable12.setter
    def umltordbms_ClassToTable12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umltordbms_ClassToTable__umltordbms_ClassToTable12", None)
        self.__umltordbms_ClassToTable12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "umltordbms_Table"):
                opp_val = getattr(old_value, "umltordbms_Table", None)
                if opp_val == self:
                    setattr(old_value, "umltordbms_Table", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "umltordbms_Table"):
                opp_val = getattr(value, "umltordbms_Table", None)
                setattr(value, "umltordbms_Table", self)

    @property
    def classesToTables(self):
        return self.__classesToTables

    @classesToTables.setter
    def classesToTables(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umltordbms_ClassToTable__classesToTables", None)
        self.__classesToTables = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PackageToSchema"):
                opp_val = getattr(old_value, "PackageToSchema", None)
                if opp_val == self:
                    setattr(old_value, "PackageToSchema", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PackageToSchema"):
                opp_val = getattr(value, "PackageToSchema", None)
                setattr(value, "PackageToSchema", self)

    @property
    def umltordbms_ClassToTable(self):
        return self.__umltordbms_ClassToTable

    @umltordbms_ClassToTable.setter
    def umltordbms_ClassToTable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umltordbms_ClassToTable__umltordbms_ClassToTable", None)
        self.__umltordbms_ClassToTable = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "umltordbms_AssociationToForeignKey"):
                opp_val = getattr(old_value, "umltordbms_AssociationToForeignKey", None)
                if opp_val == self:
                    setattr(old_value, "umltordbms_AssociationToForeignKey", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "umltordbms_AssociationToForeignKey"):
                opp_val = getattr(value, "umltordbms_AssociationToForeignKey", None)
                setattr(value, "umltordbms_AssociationToForeignKey", self)

    @property
    def ClassToTable24(self):
        return self.__ClassToTable24

    @ClassToTable24.setter
    def ClassToTable24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umltordbms_ClassToTable__ClassToTable24", None)
        self.__ClassToTable24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "owner23"):
                opp_val = getattr(old_value, "owner23", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "owner23"):
                opp_val = getattr(value, "owner23", None)
                if opp_val is None:
                    setattr(value, "owner23", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class umltordbms_ForeignKey:

    pass
class umltordbms_Association:

    pass