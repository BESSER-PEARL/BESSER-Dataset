from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class uml2rdbms_Column:

    pass
class uml2rdbms_ToColumn(ABC):

    pass
class uml2rdbms_PrimitiveDataType:

    pass
class uml2rdbms_Schema:

    pass
class uml2rdbms_Package:

    pass
class uml2rdbms_Attribute:

    pass
class uml2rdbms_FromAttributeOwner(ABC):

    pass
class uml2rdbms_FromAttribute(ABC):

    def __init__(self, name: str, kind: str, fromAttributes: "uml2rdbms_FromAttributeOwner" = None, uml2rdbms_FromAttribute: set["uml2rdbms_AttributeToColumn"] = None, uml2rdbms_FromAttribute19: "uml2rdbms_Attribute" = None, FromAttribute: "uml2rdbms_FromAttributeOwner" = None):
        self.name = name
        self.kind = kind
        self.fromAttributes = fromAttributes
        self.uml2rdbms_FromAttribute = uml2rdbms_FromAttribute if uml2rdbms_FromAttribute is not None else set()
        self.uml2rdbms_FromAttribute19 = uml2rdbms_FromAttribute19
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
    def uml2rdbms_FromAttribute(self):
        return self.__uml2rdbms_FromAttribute

    @uml2rdbms_FromAttribute.setter
    def uml2rdbms_FromAttribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml2rdbms_FromAttribute__uml2rdbms_FromAttribute", None)
        self.__uml2rdbms_FromAttribute = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uml2rdbms_AttributeToColumn17"):
                    opp_val = getattr(item, "uml2rdbms_AttributeToColumn17", None)
                    
                    if opp_val == self:
                        setattr(item, "uml2rdbms_AttributeToColumn17", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uml2rdbms_AttributeToColumn17"):
                    opp_val = getattr(item, "uml2rdbms_AttributeToColumn17", None)
                    
                    setattr(item, "uml2rdbms_AttributeToColumn17", self)
                    

    @property
    def fromAttributes(self):
        return self.__fromAttributes

    @fromAttributes.setter
    def fromAttributes(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml2rdbms_FromAttribute__fromAttributes", None)
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
    def FromAttribute(self):
        return self.__FromAttribute

    @FromAttribute.setter
    def FromAttribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml2rdbms_FromAttribute__FromAttribute", None)
        self.__FromAttribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "owner21"):
                opp_val = getattr(old_value, "owner21", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "owner21"):
                opp_val = getattr(value, "owner21", None)
                if opp_val is None:
                    setattr(value, "owner21", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def uml2rdbms_FromAttribute19(self):
        return self.__uml2rdbms_FromAttribute19

    @uml2rdbms_FromAttribute19.setter
    def uml2rdbms_FromAttribute19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml2rdbms_FromAttribute__uml2rdbms_FromAttribute19", None)
        self.__uml2rdbms_FromAttribute19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml2rdbms_Attribute"):
                opp_val = getattr(old_value, "uml2rdbms_Attribute", None)
                if opp_val == self:
                    setattr(old_value, "uml2rdbms_Attribute", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml2rdbms_Attribute"):
                opp_val = getattr(value, "uml2rdbms_Attribute", None)
                setattr(value, "uml2rdbms_Attribute", self)

class uml2rdbms_Key:

    pass
class uml2rdbms_Table:

    pass
class uml2rdbms_Class:

    pass
class uml2rdbms_PackageToSchema:

    def __init__(self, name: str, PackageToSchema: "uml2rdbms_ClassToTable" = None, owner23: set["uml2rdbms_ClassToTable"] = None, owner26: set["uml2rdbms_PrimitiveToName"] = None, uml2rdbms_PackageToSchema: "uml2rdbms_Package" = None, uml2rdbms_PackageToSchema29: "uml2rdbms_Schema" = None, PackageToSchema31: "uml2rdbms_PrimitiveToName" = None):
        self.name = name
        self.PackageToSchema = PackageToSchema
        self.owner23 = owner23 if owner23 is not None else set()
        self.owner26 = owner26 if owner26 is not None else set()
        self.uml2rdbms_PackageToSchema = uml2rdbms_PackageToSchema
        self.uml2rdbms_PackageToSchema29 = uml2rdbms_PackageToSchema29
        self.PackageToSchema31 = PackageToSchema31
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def uml2rdbms_PackageToSchema(self):
        return self.__uml2rdbms_PackageToSchema

    @uml2rdbms_PackageToSchema.setter
    def uml2rdbms_PackageToSchema(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml2rdbms_PackageToSchema__uml2rdbms_PackageToSchema", None)
        self.__uml2rdbms_PackageToSchema = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml2rdbms_Package"):
                opp_val = getattr(old_value, "uml2rdbms_Package", None)
                if opp_val == self:
                    setattr(old_value, "uml2rdbms_Package", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml2rdbms_Package"):
                opp_val = getattr(value, "uml2rdbms_Package", None)
                setattr(value, "uml2rdbms_Package", self)

    @property
    def owner23(self):
        return self.__owner23

    @owner23.setter
    def owner23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml2rdbms_PackageToSchema__owner23", None)
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
                    

    @property
    def PackageToSchema31(self):
        return self.__PackageToSchema31

    @PackageToSchema31.setter
    def PackageToSchema31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml2rdbms_PackageToSchema__PackageToSchema31", None)
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
    def owner26(self):
        return self.__owner26

    @owner26.setter
    def owner26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml2rdbms_PackageToSchema__owner26", None)
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
    def PackageToSchema(self):
        return self.__PackageToSchema

    @PackageToSchema.setter
    def PackageToSchema(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml2rdbms_PackageToSchema__PackageToSchema", None)
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
    def uml2rdbms_PackageToSchema29(self):
        return self.__uml2rdbms_PackageToSchema29

    @uml2rdbms_PackageToSchema29.setter
    def uml2rdbms_PackageToSchema29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml2rdbms_PackageToSchema__uml2rdbms_PackageToSchema29", None)
        self.__uml2rdbms_PackageToSchema29 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml2rdbms_Schema"):
                opp_val = getattr(old_value, "uml2rdbms_Schema", None)
                if opp_val == self:
                    setattr(old_value, "uml2rdbms_Schema", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml2rdbms_Schema"):
                opp_val = getattr(value, "uml2rdbms_Schema", None)
                setattr(value, "uml2rdbms_Schema", self)

class FromAttributeOwner:

    pass
class uml2rdbms_PrimitiveToName:

    def __init__(self, name: str, typeName: str, uml2rdbms_PrimitiveToName: "uml2rdbms_AttributeToColumn" = None, PrimitiveToName: "uml2rdbms_PackageToSchema" = None, primitivesToNames: "uml2rdbms_PackageToSchema" = None, uml2rdbms_PrimitiveToName33: "uml2rdbms_PrimitiveDataType" = None, uml2rdbms_PrimitiveToName36: "uml2rdbms_NonLeafAttribute" = None):
        self.name = name
        self.typeName = typeName
        self.uml2rdbms_PrimitiveToName = uml2rdbms_PrimitiveToName
        self.PrimitiveToName = PrimitiveToName
        self.primitivesToNames = primitivesToNames
        self.uml2rdbms_PrimitiveToName33 = uml2rdbms_PrimitiveToName33
        self.uml2rdbms_PrimitiveToName36 = uml2rdbms_PrimitiveToName36
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def typeName(self) -> str:
        return self.__typeName

    @typeName.setter
    def typeName(self, typeName: str):
        self.__typeName = typeName

    @property
    def uml2rdbms_PrimitiveToName(self):
        return self.__uml2rdbms_PrimitiveToName

    @uml2rdbms_PrimitiveToName.setter
    def uml2rdbms_PrimitiveToName(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml2rdbms_PrimitiveToName__uml2rdbms_PrimitiveToName", None)
        self.__uml2rdbms_PrimitiveToName = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml2rdbms_AttributeToColumn"):
                opp_val = getattr(old_value, "uml2rdbms_AttributeToColumn", None)
                if opp_val == self:
                    setattr(old_value, "uml2rdbms_AttributeToColumn", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml2rdbms_AttributeToColumn"):
                opp_val = getattr(value, "uml2rdbms_AttributeToColumn", None)
                setattr(value, "uml2rdbms_AttributeToColumn", self)

    @property
    def PrimitiveToName(self):
        return self.__PrimitiveToName

    @PrimitiveToName.setter
    def PrimitiveToName(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml2rdbms_PrimitiveToName__PrimitiveToName", None)
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

    @property
    def uml2rdbms_PrimitiveToName36(self):
        return self.__uml2rdbms_PrimitiveToName36

    @uml2rdbms_PrimitiveToName36.setter
    def uml2rdbms_PrimitiveToName36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml2rdbms_PrimitiveToName__uml2rdbms_PrimitiveToName36", None)
        self.__uml2rdbms_PrimitiveToName36 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml2rdbms_NonLeafAttribute"):
                opp_val = getattr(old_value, "uml2rdbms_NonLeafAttribute", None)
                if opp_val == self:
                    setattr(old_value, "uml2rdbms_NonLeafAttribute", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml2rdbms_NonLeafAttribute"):
                opp_val = getattr(value, "uml2rdbms_NonLeafAttribute", None)
                setattr(value, "uml2rdbms_NonLeafAttribute", self)

    @property
    def uml2rdbms_PrimitiveToName33(self):
        return self.__uml2rdbms_PrimitiveToName33

    @uml2rdbms_PrimitiveToName33.setter
    def uml2rdbms_PrimitiveToName33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml2rdbms_PrimitiveToName__uml2rdbms_PrimitiveToName33", None)
        self.__uml2rdbms_PrimitiveToName33 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml2rdbms_PrimitiveDataType"):
                opp_val = getattr(old_value, "uml2rdbms_PrimitiveDataType", None)
                if opp_val == self:
                    setattr(old_value, "uml2rdbms_PrimitiveDataType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml2rdbms_PrimitiveDataType"):
                opp_val = getattr(value, "uml2rdbms_PrimitiveDataType", None)
                setattr(value, "uml2rdbms_PrimitiveDataType", self)

    @property
    def primitivesToNames(self):
        return self.__primitivesToNames

    @primitivesToNames.setter
    def primitivesToNames(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml2rdbms_PrimitiveToName__primitivesToNames", None)
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

class FromAttribute:

    pass
class uml2rdbms_NonLeafAttribute(FromAttribute, FromAttributeOwner):

    pass
class uml2rdbms_ForeignKey:

    pass
class uml2rdbms_Association:

    pass
class ToColumn:

    pass
class uml2rdbms_AttributeToColumn(FromAttribute, ToColumn):

    pass
class uml2rdbms_ClassToTable(ToColumn, FromAttributeOwner):

    def __init__(self, name: str, uml2rdbms_ClassToTable: "uml2rdbms_AssociationToForeignKey" = None, ClassToTable: "uml2rdbms_AssociationToForeignKey" = None, classesToTables: "uml2rdbms_PackageToSchema" = None, owner: set["uml2rdbms_AssociationToForeignKey"] = None, ClassToTable24: "uml2rdbms_PackageToSchema" = None, uml2rdbms_ClassToTable10: "uml2rdbms_Class" = None, uml2rdbms_ClassToTable12: "uml2rdbms_Table" = None, uml2rdbms_ClassToTable14: "uml2rdbms_Key" = None):
        self.name = name
        self.uml2rdbms_ClassToTable = uml2rdbms_ClassToTable
        self.ClassToTable = ClassToTable
        self.classesToTables = classesToTables
        self.owner = owner if owner is not None else set()
        self.ClassToTable24 = ClassToTable24
        self.uml2rdbms_ClassToTable10 = uml2rdbms_ClassToTable10
        self.uml2rdbms_ClassToTable12 = uml2rdbms_ClassToTable12
        self.uml2rdbms_ClassToTable14 = uml2rdbms_ClassToTable14
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def classesToTables(self):
        return self.__classesToTables

    @classesToTables.setter
    def classesToTables(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml2rdbms_ClassToTable__classesToTables", None)
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
    def uml2rdbms_ClassToTable10(self):
        return self.__uml2rdbms_ClassToTable10

    @uml2rdbms_ClassToTable10.setter
    def uml2rdbms_ClassToTable10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml2rdbms_ClassToTable__uml2rdbms_ClassToTable10", None)
        self.__uml2rdbms_ClassToTable10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml2rdbms_Class"):
                opp_val = getattr(old_value, "uml2rdbms_Class", None)
                if opp_val == self:
                    setattr(old_value, "uml2rdbms_Class", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml2rdbms_Class"):
                opp_val = getattr(value, "uml2rdbms_Class", None)
                setattr(value, "uml2rdbms_Class", self)

    @property
    def uml2rdbms_ClassToTable12(self):
        return self.__uml2rdbms_ClassToTable12

    @uml2rdbms_ClassToTable12.setter
    def uml2rdbms_ClassToTable12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml2rdbms_ClassToTable__uml2rdbms_ClassToTable12", None)
        self.__uml2rdbms_ClassToTable12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml2rdbms_Table"):
                opp_val = getattr(old_value, "uml2rdbms_Table", None)
                if opp_val == self:
                    setattr(old_value, "uml2rdbms_Table", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml2rdbms_Table"):
                opp_val = getattr(value, "uml2rdbms_Table", None)
                setattr(value, "uml2rdbms_Table", self)

    @property
    def owner(self):
        return self.__owner

    @owner.setter
    def owner(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml2rdbms_ClassToTable__owner", None)
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
    def ClassToTable24(self):
        return self.__ClassToTable24

    @ClassToTable24.setter
    def ClassToTable24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml2rdbms_ClassToTable__ClassToTable24", None)
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

    @property
    def uml2rdbms_ClassToTable(self):
        return self.__uml2rdbms_ClassToTable

    @uml2rdbms_ClassToTable.setter
    def uml2rdbms_ClassToTable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml2rdbms_ClassToTable__uml2rdbms_ClassToTable", None)
        self.__uml2rdbms_ClassToTable = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml2rdbms_AssociationToForeignKey"):
                opp_val = getattr(old_value, "uml2rdbms_AssociationToForeignKey", None)
                if opp_val == self:
                    setattr(old_value, "uml2rdbms_AssociationToForeignKey", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml2rdbms_AssociationToForeignKey"):
                opp_val = getattr(value, "uml2rdbms_AssociationToForeignKey", None)
                setattr(value, "uml2rdbms_AssociationToForeignKey", self)

    @property
    def ClassToTable(self):
        return self.__ClassToTable

    @ClassToTable.setter
    def ClassToTable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml2rdbms_ClassToTable__ClassToTable", None)
        self.__ClassToTable = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "associationToForeignKeys"):
                opp_val = getattr(old_value, "associationToForeignKeys", None)
                if opp_val == self:
                    setattr(old_value, "associationToForeignKeys", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "associationToForeignKeys"):
                opp_val = getattr(value, "associationToForeignKeys", None)
                setattr(value, "associationToForeignKeys", self)

    @property
    def uml2rdbms_ClassToTable14(self):
        return self.__uml2rdbms_ClassToTable14

    @uml2rdbms_ClassToTable14.setter
    def uml2rdbms_ClassToTable14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml2rdbms_ClassToTable__uml2rdbms_ClassToTable14", None)
        self.__uml2rdbms_ClassToTable14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml2rdbms_Key"):
                opp_val = getattr(old_value, "uml2rdbms_Key", None)
                if opp_val == self:
                    setattr(old_value, "uml2rdbms_Key", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml2rdbms_Key"):
                opp_val = getattr(value, "uml2rdbms_Key", None)
                setattr(value, "uml2rdbms_Key", self)

class uml2rdbms_AssociationToForeignKey(ToColumn):

    def __init__(self, name: str, associationToForeignKeys: "uml2rdbms_ClassToTable" = None, uml2rdbms_AssociationToForeignKey: "uml2rdbms_ClassToTable" = None, uml2rdbms_AssociationToForeignKey3: "uml2rdbms_Association" = None, uml2rdbms_AssociationToForeignKey5: "uml2rdbms_ForeignKey" = None, AssociationToForeignKey: "uml2rdbms_ClassToTable" = None):
        self.name = name
        self.associationToForeignKeys = associationToForeignKeys
        self.uml2rdbms_AssociationToForeignKey = uml2rdbms_AssociationToForeignKey
        self.uml2rdbms_AssociationToForeignKey3 = uml2rdbms_AssociationToForeignKey3
        self.uml2rdbms_AssociationToForeignKey5 = uml2rdbms_AssociationToForeignKey5
        self.AssociationToForeignKey = AssociationToForeignKey
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def uml2rdbms_AssociationToForeignKey(self):
        return self.__uml2rdbms_AssociationToForeignKey

    @uml2rdbms_AssociationToForeignKey.setter
    def uml2rdbms_AssociationToForeignKey(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml2rdbms_AssociationToForeignKey__uml2rdbms_AssociationToForeignKey", None)
        self.__uml2rdbms_AssociationToForeignKey = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml2rdbms_ClassToTable"):
                opp_val = getattr(old_value, "uml2rdbms_ClassToTable", None)
                if opp_val == self:
                    setattr(old_value, "uml2rdbms_ClassToTable", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml2rdbms_ClassToTable"):
                opp_val = getattr(value, "uml2rdbms_ClassToTable", None)
                setattr(value, "uml2rdbms_ClassToTable", self)

    @property
    def AssociationToForeignKey(self):
        return self.__AssociationToForeignKey

    @AssociationToForeignKey.setter
    def AssociationToForeignKey(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml2rdbms_AssociationToForeignKey__AssociationToForeignKey", None)
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

    @property
    def uml2rdbms_AssociationToForeignKey3(self):
        return self.__uml2rdbms_AssociationToForeignKey3

    @uml2rdbms_AssociationToForeignKey3.setter
    def uml2rdbms_AssociationToForeignKey3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml2rdbms_AssociationToForeignKey__uml2rdbms_AssociationToForeignKey3", None)
        self.__uml2rdbms_AssociationToForeignKey3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml2rdbms_Association"):
                opp_val = getattr(old_value, "uml2rdbms_Association", None)
                if opp_val == self:
                    setattr(old_value, "uml2rdbms_Association", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml2rdbms_Association"):
                opp_val = getattr(value, "uml2rdbms_Association", None)
                setattr(value, "uml2rdbms_Association", self)

    @property
    def uml2rdbms_AssociationToForeignKey5(self):
        return self.__uml2rdbms_AssociationToForeignKey5

    @uml2rdbms_AssociationToForeignKey5.setter
    def uml2rdbms_AssociationToForeignKey5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml2rdbms_AssociationToForeignKey__uml2rdbms_AssociationToForeignKey5", None)
        self.__uml2rdbms_AssociationToForeignKey5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml2rdbms_ForeignKey"):
                opp_val = getattr(old_value, "uml2rdbms_ForeignKey", None)
                if opp_val == self:
                    setattr(old_value, "uml2rdbms_ForeignKey", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml2rdbms_ForeignKey"):
                opp_val = getattr(value, "uml2rdbms_ForeignKey", None)
                setattr(value, "uml2rdbms_ForeignKey", self)

    @property
    def associationToForeignKeys(self):
        return self.__associationToForeignKeys

    @associationToForeignKeys.setter
    def associationToForeignKeys(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml2rdbms_AssociationToForeignKey__associationToForeignKeys", None)
        self.__associationToForeignKeys = value
        
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
