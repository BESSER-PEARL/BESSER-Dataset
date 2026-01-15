from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class model_analytical_AnalyticalModel:

    pass
class model_behavioural_BehaviouralModel:

    pass
class VirtualCubeMeasure:

    pass
class VirtualCubeDimension:

    pass
class Dimension:

    pass
class VirtualCube:

    pass
class Cube:

    pass
class olap_model_Model:

    pass
class Level:

    pass
class Hierarchy:

    pass
class NamedSet:

    pass
class CalculatedMember:

    pass
class Measure:

    pass
class BusinessColumn:

    pass
class model_business_SimpleBusinessColumn(BusinessColumn):

    pass
class model_business_CalculatedBusinessColumn(BusinessColumn):

    pass
class BusinessViewInnerJoinRelationship:

    pass
class BusinessDomain:

    pass
class BusinessIdentifier:

    pass
class BusinessRelationship:

    pass
class BusinessColumnSet:

    pass
class model_business_BusinessView(BusinessColumnSet):

    pass
class model_business_BusinessTable(BusinessColumnSet):

    pass
class business_model_Model:

    pass
class OlapModel:

    pass
class BusinessModel:

    pass
class PhysicalModel:

    pass
class ModelObject:

    pass
class model_olap_Level(ModelObject):

    pass
class model_business_BusinessColumn(ModelObject):

    pass
class model_olap_VirtualCubeDimension(ModelObject):

    pass
class model_olap_Dimension(ModelObject):

    pass
class model_olap_Measure(ModelObject):

    pass
class model_olap_NamedSet(ModelObject):

    pass
class model_olap_CalculatedMember(ModelObject):

    pass
class model_olap_Hierarchy(ModelObject):

    pass
class model_olap_VirtualCube(ModelObject):

    pass
class model_olap_VirtualCubeMeasure(ModelObject):

    pass
class model_business_BusinessColumnSet(ModelObject):

    pass
class model_business_BusinessRelationship(ModelObject):

    pass
class model_physical_PhysicalForeignKey(ModelObject):

    def __init__(self, sourceName: str, destinationName: str, model_physical_PhysicalForeignKey52: set["PhysicalColumn"] = None, PhysicalModel55: "PhysicalModel" = None, model_physical_PhysicalForeignKey: "PhysicalTable" = None, model_physical_PhysicalForeignKey46: set["PhysicalColumn"] = None, model_physical_PhysicalForeignKey49: "PhysicalTable" = None):
        self.sourceName = sourceName
        self.destinationName = destinationName
        self.model_physical_PhysicalForeignKey52 = model_physical_PhysicalForeignKey52 if model_physical_PhysicalForeignKey52 is not None else set()
        self.PhysicalModel55 = PhysicalModel55
        self.model_physical_PhysicalForeignKey = model_physical_PhysicalForeignKey
        self.model_physical_PhysicalForeignKey46 = model_physical_PhysicalForeignKey46 if model_physical_PhysicalForeignKey46 is not None else set()
        self.model_physical_PhysicalForeignKey49 = model_physical_PhysicalForeignKey49
        
    @property
    def destinationName(self) -> str:
        return self.__destinationName

    @destinationName.setter
    def destinationName(self, destinationName: str):
        self.__destinationName = destinationName

    @property
    def sourceName(self) -> str:
        return self.__sourceName

    @sourceName.setter
    def sourceName(self, sourceName: str):
        self.__sourceName = sourceName

    @property
    def PhysicalModel55(self):
        return self.__PhysicalModel55

    @PhysicalModel55.setter
    def PhysicalModel55(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_physical_PhysicalForeignKey__PhysicalModel55", None)
        self.__PhysicalModel55 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "physical56"):
                opp_val = getattr(old_value, "physical56", None)
                if opp_val == self:
                    setattr(old_value, "physical56", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "physical56"):
                opp_val = getattr(value, "physical56", None)
                setattr(value, "physical56", self)

    @property
    def model_physical_PhysicalForeignKey49(self):
        return self.__model_physical_PhysicalForeignKey49

    @model_physical_PhysicalForeignKey49.setter
    def model_physical_PhysicalForeignKey49(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_physical_PhysicalForeignKey__model_physical_PhysicalForeignKey49", None)
        self.__model_physical_PhysicalForeignKey49 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PhysicalTable50"):
                opp_val = getattr(old_value, "PhysicalTable50", None)
                if opp_val == self:
                    setattr(old_value, "PhysicalTable50", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PhysicalTable50"):
                opp_val = getattr(value, "PhysicalTable50", None)
                setattr(value, "PhysicalTable50", self)

    @property
    def model_physical_PhysicalForeignKey(self):
        return self.__model_physical_PhysicalForeignKey

    @model_physical_PhysicalForeignKey.setter
    def model_physical_PhysicalForeignKey(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_physical_PhysicalForeignKey__model_physical_PhysicalForeignKey", None)
        self.__model_physical_PhysicalForeignKey = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PhysicalTable44"):
                opp_val = getattr(old_value, "PhysicalTable44", None)
                if opp_val == self:
                    setattr(old_value, "PhysicalTable44", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PhysicalTable44"):
                opp_val = getattr(value, "PhysicalTable44", None)
                setattr(value, "PhysicalTable44", self)

    @property
    def model_physical_PhysicalForeignKey52(self):
        return self.__model_physical_PhysicalForeignKey52

    @model_physical_PhysicalForeignKey52.setter
    def model_physical_PhysicalForeignKey52(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_physical_PhysicalForeignKey__model_physical_PhysicalForeignKey52", None)
        self.__model_physical_PhysicalForeignKey52 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "PhysicalColumn53"):
                    opp_val = getattr(item, "PhysicalColumn53", None)
                    
                    if opp_val == self:
                        setattr(item, "PhysicalColumn53", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "PhysicalColumn53"):
                    opp_val = getattr(item, "PhysicalColumn53", None)
                    
                    setattr(item, "PhysicalColumn53", self)
                    

    @property
    def model_physical_PhysicalForeignKey46(self):
        return self.__model_physical_PhysicalForeignKey46

    @model_physical_PhysicalForeignKey46.setter
    def model_physical_PhysicalForeignKey46(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_physical_PhysicalForeignKey__model_physical_PhysicalForeignKey46", None)
        self.__model_physical_PhysicalForeignKey46 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "PhysicalColumn47"):
                    opp_val = getattr(item, "PhysicalColumn47", None)
                    
                    if opp_val == self:
                        setattr(item, "PhysicalColumn47", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "PhysicalColumn47"):
                    opp_val = getattr(item, "PhysicalColumn47", None)
                    
                    setattr(item, "PhysicalColumn47", self)
                    

class model_business_BusinessModel(ModelObject):

    pass
class model_business_BusinessViewInnerJoinRelationship(ModelObject):

    pass
class model_physical_PhysicalModel(ModelObject):

    def __init__(self, databaseName: str, databaseVersion: str, catalog: str, schema: str, physicalModels: "physical_model_Model" = None, PhysicalTable: set["PhysicalTable"] = None, PhysicalPrimaryKey: set["PhysicalPrimaryKey"] = None, PhysicalForeignKey: set["PhysicalForeignKey"] = None):
        self.databaseName = databaseName
        self.databaseVersion = databaseVersion
        self.catalog = catalog
        self.schema = schema
        self.physicalModels = physicalModels
        self.PhysicalTable = PhysicalTable if PhysicalTable is not None else set()
        self.PhysicalPrimaryKey = PhysicalPrimaryKey if PhysicalPrimaryKey is not None else set()
        self.PhysicalForeignKey = PhysicalForeignKey if PhysicalForeignKey is not None else set()
        
    @property
    def databaseName(self) -> str:
        return self.__databaseName

    @databaseName.setter
    def databaseName(self, databaseName: str):
        self.__databaseName = databaseName

    @property
    def databaseVersion(self) -> str:
        return self.__databaseVersion

    @databaseVersion.setter
    def databaseVersion(self, databaseVersion: str):
        self.__databaseVersion = databaseVersion

    @property
    def catalog(self) -> str:
        return self.__catalog

    @catalog.setter
    def catalog(self, catalog: str):
        self.__catalog = catalog

    @property
    def schema(self) -> str:
        return self.__schema

    @schema.setter
    def schema(self, schema: str):
        self.__schema = schema

    @property
    def PhysicalTable(self):
        return self.__PhysicalTable

    @PhysicalTable.setter
    def PhysicalTable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_physical_PhysicalModel__PhysicalTable", None)
        self.__PhysicalTable = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "physical22"):
                    opp_val = getattr(item, "physical22", None)
                    
                    if opp_val == self:
                        setattr(item, "physical22", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "physical22"):
                    opp_val = getattr(item, "physical22", None)
                    
                    setattr(item, "physical22", self)
                    

    @property
    def PhysicalForeignKey(self):
        return self.__PhysicalForeignKey

    @PhysicalForeignKey.setter
    def PhysicalForeignKey(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_physical_PhysicalModel__PhysicalForeignKey", None)
        self.__PhysicalForeignKey = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "physical26"):
                    opp_val = getattr(item, "physical26", None)
                    
                    if opp_val == self:
                        setattr(item, "physical26", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "physical26"):
                    opp_val = getattr(item, "physical26", None)
                    
                    setattr(item, "physical26", self)
                    

    @property
    def PhysicalPrimaryKey(self):
        return self.__PhysicalPrimaryKey

    @PhysicalPrimaryKey.setter
    def PhysicalPrimaryKey(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_physical_PhysicalModel__PhysicalPrimaryKey", None)
        self.__PhysicalPrimaryKey = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "physical24"):
                    opp_val = getattr(item, "physical24", None)
                    
                    if opp_val == self:
                        setattr(item, "physical24", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "physical24"):
                    opp_val = getattr(item, "physical24", None)
                    
                    setattr(item, "physical24", self)
                    

    @property
    def physicalModels(self):
        return self.__physicalModels

    @physicalModels.setter
    def physicalModels(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_physical_PhysicalModel__physicalModels", None)
        self.__physicalModels = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Model"):
                opp_val = getattr(old_value, "Model", None)
                if opp_val == self:
                    setattr(old_value, "Model", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Model"):
                opp_val = getattr(value, "Model", None)
                setattr(value, "Model", self)

class model_business_BusinessIdentifier(ModelObject):

    pass
class model_olap_Cube(ModelObject):

    pass
class model_olap_OlapModel(ModelObject):

    pass
class model_business_BusinessDomain(ModelObject):

    pass
class model_Model(ModelObject):

    pass
class model_physical_PhysicalPrimaryKey(ModelObject):

    pass
class model_physical_PhysicalColumn(ModelObject):

    def __init__(self, comment: str, dataType: str, typeName: str, size: int, octectLength: int, decimalDigits: int, radix: int, defaultValue: str, nullable: bool, position: int, PhysicalTable33: "PhysicalTable" = None):
        self.comment = comment
        self.dataType = dataType
        self.typeName = typeName
        self.size = size
        self.octectLength = octectLength
        self.decimalDigits = decimalDigits
        self.radix = radix
        self.defaultValue = defaultValue
        self.nullable = nullable
        self.position = position
        self.PhysicalTable33 = PhysicalTable33
        
    @property
    def comment(self) -> str:
        return self.__comment

    @comment.setter
    def comment(self, comment: str):
        self.__comment = comment

    @property
    def defaultValue(self) -> str:
        return self.__defaultValue

    @defaultValue.setter
    def defaultValue(self, defaultValue: str):
        self.__defaultValue = defaultValue

    @property
    def position(self) -> int:
        return self.__position

    @position.setter
    def position(self, position: int):
        self.__position = position

    @property
    def decimalDigits(self) -> int:
        return self.__decimalDigits

    @decimalDigits.setter
    def decimalDigits(self, decimalDigits: int):
        self.__decimalDigits = decimalDigits

    @property
    def radix(self) -> int:
        return self.__radix

    @radix.setter
    def radix(self, radix: int):
        self.__radix = radix

    @property
    def size(self) -> int:
        return self.__size

    @size.setter
    def size(self, size: int):
        self.__size = size

    @property
    def typeName(self) -> str:
        return self.__typeName

    @typeName.setter
    def typeName(self, typeName: str):
        self.__typeName = typeName

    @property
    def octectLength(self) -> int:
        return self.__octectLength

    @octectLength.setter
    def octectLength(self, octectLength: int):
        self.__octectLength = octectLength

    @property
    def nullable(self) -> bool:
        return self.__nullable

    @nullable.setter
    def nullable(self, nullable: bool):
        self.__nullable = nullable

    @property
    def dataType(self) -> str:
        return self.__dataType

    @dataType.setter
    def dataType(self, dataType: str):
        self.__dataType = dataType

    @property
    def PhysicalTable33(self):
        return self.__PhysicalTable33

    @PhysicalTable33.setter
    def PhysicalTable33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_physical_PhysicalColumn__PhysicalTable33", None)
        self.__PhysicalTable33 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "physical34"):
                opp_val = getattr(old_value, "physical34", None)
                if opp_val == self:
                    setattr(old_value, "physical34", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "physical34"):
                opp_val = getattr(value, "physical34", None)
                setattr(value, "physical34", self)

class PhysicalColumn:

    pass
class model_physical_PhysicalTable(ModelObject):

    def __init__(self, comment: str, type: str, PhysicalModel28: "PhysicalModel" = None, PhysicalColumn: set["PhysicalColumn"] = None):
        self.comment = comment
        self.type = type
        self.PhysicalModel28 = PhysicalModel28
        self.PhysicalColumn = PhysicalColumn if PhysicalColumn is not None else set()
        
    @property
    def comment(self) -> str:
        return self.__comment

    @comment.setter
    def comment(self, comment: str):
        self.__comment = comment

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def PhysicalColumn(self):
        return self.__PhysicalColumn

    @PhysicalColumn.setter
    def PhysicalColumn(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_physical_PhysicalTable__PhysicalColumn", None)
        self.__PhysicalColumn = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "physical31"):
                    opp_val = getattr(item, "physical31", None)
                    
                    if opp_val == self:
                        setattr(item, "physical31", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "physical31"):
                    opp_val = getattr(item, "physical31", None)
                    
                    setattr(item, "physical31", self)
                    

    @property
    def PhysicalModel28(self):
        return self.__PhysicalModel28

    @PhysicalModel28.setter
    def PhysicalModel28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_physical_PhysicalTable__PhysicalModel28", None)
        self.__PhysicalModel28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "physical29"):
                opp_val = getattr(old_value, "physical29", None)
                if opp_val == self:
                    setattr(old_value, "physical29", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "physical29"):
                opp_val = getattr(value, "physical29", None)
                setattr(value, "physical29", self)

class PhysicalForeignKey:

    pass
class PhysicalPrimaryKey:

    pass
class PhysicalTable:

    pass
class physical_model_Model:

    pass
class model_ModelPropertyCategory:

    def __init__(self, description: str, name: str, model_ModelPropertyCategory: "model_ModelPropertyCategory" = None, model_ModelPropertyCategory0: "model_ModelPropertyCategory" = None, model_ModelPropertyCategory4: "model_ModelPropertyCategory" = None, model_ModelPropertyCategory2: set["model_ModelPropertyCategory"] = None, category: set["model_ModelPropertyType"] = None, ModelPropertyCategory: "model_ModelPropertyType" = None, model_ModelPropertyCategory19: "model_Model" = None):
        self.description = description
        self.name = name
        self.model_ModelPropertyCategory = model_ModelPropertyCategory
        self.model_ModelPropertyCategory0 = model_ModelPropertyCategory0
        self.model_ModelPropertyCategory4 = model_ModelPropertyCategory4
        self.model_ModelPropertyCategory2 = model_ModelPropertyCategory2 if model_ModelPropertyCategory2 is not None else set()
        self.category = category if category is not None else set()
        self.ModelPropertyCategory = ModelPropertyCategory
        self.model_ModelPropertyCategory19 = model_ModelPropertyCategory19
        
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
    def model_ModelPropertyCategory(self):
        return self.__model_ModelPropertyCategory

    @model_ModelPropertyCategory.setter
    def model_ModelPropertyCategory(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_ModelPropertyCategory__model_ModelPropertyCategory", None)
        self.__model_ModelPropertyCategory = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_ModelPropertyCategory0"):
                opp_val = getattr(old_value, "model_ModelPropertyCategory0", None)
                if opp_val == self:
                    setattr(old_value, "model_ModelPropertyCategory0", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_ModelPropertyCategory0"):
                opp_val = getattr(value, "model_ModelPropertyCategory0", None)
                setattr(value, "model_ModelPropertyCategory0", self)

    @property
    def model_ModelPropertyCategory0(self):
        return self.__model_ModelPropertyCategory0

    @model_ModelPropertyCategory0.setter
    def model_ModelPropertyCategory0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_ModelPropertyCategory__model_ModelPropertyCategory0", None)
        self.__model_ModelPropertyCategory0 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_ModelPropertyCategory"):
                opp_val = getattr(old_value, "model_ModelPropertyCategory", None)
                if opp_val == self:
                    setattr(old_value, "model_ModelPropertyCategory", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_ModelPropertyCategory"):
                opp_val = getattr(value, "model_ModelPropertyCategory", None)
                setattr(value, "model_ModelPropertyCategory", self)

    @property
    def model_ModelPropertyCategory19(self):
        return self.__model_ModelPropertyCategory19

    @model_ModelPropertyCategory19.setter
    def model_ModelPropertyCategory19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_ModelPropertyCategory__model_ModelPropertyCategory19", None)
        self.__model_ModelPropertyCategory19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_Model18"):
                opp_val = getattr(old_value, "model_Model18", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_Model18"):
                opp_val = getattr(value, "model_Model18", None)
                if opp_val is None:
                    setattr(value, "model_Model18", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def category(self):
        return self.__category

    @category.setter
    def category(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_ModelPropertyCategory__category", None)
        self.__category = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ModelPropertyType"):
                    opp_val = getattr(item, "ModelPropertyType", None)
                    
                    if opp_val == self:
                        setattr(item, "ModelPropertyType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ModelPropertyType"):
                    opp_val = getattr(item, "ModelPropertyType", None)
                    
                    setattr(item, "ModelPropertyType", self)
                    

    @property
    def ModelPropertyCategory(self):
        return self.__ModelPropertyCategory

    @ModelPropertyCategory.setter
    def ModelPropertyCategory(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_ModelPropertyCategory__ModelPropertyCategory", None)
        self.__ModelPropertyCategory = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "propertyTypes"):
                opp_val = getattr(old_value, "propertyTypes", None)
                if opp_val == self:
                    setattr(old_value, "propertyTypes", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "propertyTypes"):
                opp_val = getattr(value, "propertyTypes", None)
                setattr(value, "propertyTypes", self)

    @property
    def model_ModelPropertyCategory2(self):
        return self.__model_ModelPropertyCategory2

    @model_ModelPropertyCategory2.setter
    def model_ModelPropertyCategory2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_ModelPropertyCategory__model_ModelPropertyCategory2", None)
        self.__model_ModelPropertyCategory2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "model_ModelPropertyCategory4"):
                    opp_val = getattr(item, "model_ModelPropertyCategory4", None)
                    
                    if opp_val == self:
                        setattr(item, "model_ModelPropertyCategory4", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "model_ModelPropertyCategory4"):
                    opp_val = getattr(item, "model_ModelPropertyCategory4", None)
                    
                    setattr(item, "model_ModelPropertyCategory4", self)
                    

    @property
    def model_ModelPropertyCategory4(self):
        return self.__model_ModelPropertyCategory4

    @model_ModelPropertyCategory4.setter
    def model_ModelPropertyCategory4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_ModelPropertyCategory__model_ModelPropertyCategory4", None)
        self.__model_ModelPropertyCategory4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_ModelPropertyCategory2"):
                opp_val = getattr(old_value, "model_ModelPropertyCategory2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_ModelPropertyCategory2"):
                opp_val = getattr(value, "model_ModelPropertyCategory2", None)
                if opp_val is None:
                    setattr(value, "model_ModelPropertyCategory2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class model_ModelObject(ABC):

    def __init__(self, id: str, name: str, uniqueName: str, description: str, model_ModelObject: set["model_ModelPropertyMapEntry"] = None):
        self.id = id
        self.name = name
        self.uniqueName = uniqueName
        self.description = description
        self.model_ModelObject = model_ModelObject if model_ModelObject is not None else set()
        
    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def uniqueName(self) -> str:
        return self.__uniqueName

    @uniqueName.setter
    def uniqueName(self, uniqueName: str):
        self.__uniqueName = uniqueName

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def model_ModelObject(self):
        return self.__model_ModelObject

    @model_ModelObject.setter
    def model_ModelObject(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_ModelObject__model_ModelObject", None)
        self.__model_ModelObject = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "model_ModelPropertyMapEntry11"):
                    opp_val = getattr(item, "model_ModelPropertyMapEntry11", None)
                    
                    if opp_val == self:
                        setattr(item, "model_ModelPropertyMapEntry11", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "model_ModelPropertyMapEntry11"):
                    opp_val = getattr(item, "model_ModelPropertyMapEntry11", None)
                    
                    setattr(item, "model_ModelPropertyMapEntry11", self)
                    

class model_ModelPropertyMapEntry:

    def __init__(self, key: str, model_ModelPropertyMapEntry: "model_ModelProperty" = None, model_ModelPropertyMapEntry11: "model_ModelObject" = None):
        self.key = key
        self.model_ModelPropertyMapEntry = model_ModelPropertyMapEntry
        self.model_ModelPropertyMapEntry11 = model_ModelPropertyMapEntry11
        
    @property
    def key(self) -> str:
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key

    @property
    def model_ModelPropertyMapEntry11(self):
        return self.__model_ModelPropertyMapEntry11

    @model_ModelPropertyMapEntry11.setter
    def model_ModelPropertyMapEntry11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_ModelPropertyMapEntry__model_ModelPropertyMapEntry11", None)
        self.__model_ModelPropertyMapEntry11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_ModelObject"):
                opp_val = getattr(old_value, "model_ModelObject", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_ModelObject"):
                opp_val = getattr(value, "model_ModelObject", None)
                if opp_val is None:
                    setattr(value, "model_ModelObject", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def model_ModelPropertyMapEntry(self):
        return self.__model_ModelPropertyMapEntry

    @model_ModelPropertyMapEntry.setter
    def model_ModelPropertyMapEntry(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_ModelPropertyMapEntry__model_ModelPropertyMapEntry", None)
        self.__model_ModelPropertyMapEntry = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_ModelProperty9"):
                opp_val = getattr(old_value, "model_ModelProperty9", None)
                if opp_val == self:
                    setattr(old_value, "model_ModelProperty9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_ModelProperty9"):
                opp_val = getattr(value, "model_ModelProperty9", None)
                setattr(value, "model_ModelProperty9", self)

class model_ModelProperty:

    def __init__(self, value: str, model_ModelProperty: "model_ModelPropertyType" = None, model_ModelProperty9: "model_ModelPropertyMapEntry" = None):
        self.value = value
        self.model_ModelProperty = model_ModelProperty
        self.model_ModelProperty9 = model_ModelProperty9
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def model_ModelProperty(self):
        return self.__model_ModelProperty

    @model_ModelProperty.setter
    def model_ModelProperty(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_ModelProperty__model_ModelProperty", None)
        self.__model_ModelProperty = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_ModelPropertyType"):
                opp_val = getattr(old_value, "model_ModelPropertyType", None)
                if opp_val == self:
                    setattr(old_value, "model_ModelPropertyType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_ModelPropertyType"):
                opp_val = getattr(value, "model_ModelPropertyType", None)
                setattr(value, "model_ModelPropertyType", self)

    @property
    def model_ModelProperty9(self):
        return self.__model_ModelProperty9

    @model_ModelProperty9.setter
    def model_ModelProperty9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_ModelProperty__model_ModelProperty9", None)
        self.__model_ModelProperty9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_ModelPropertyMapEntry"):
                opp_val = getattr(old_value, "model_ModelPropertyMapEntry", None)
                if opp_val == self:
                    setattr(old_value, "model_ModelPropertyMapEntry", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_ModelPropertyMapEntry"):
                opp_val = getattr(value, "model_ModelPropertyMapEntry", None)
                setattr(value, "model_ModelPropertyMapEntry", self)

class model_ModelPropertyType:

    def __init__(self, id: str, name: str, description: str, admissibleValues: str, defaultValue: str, ModelPropertyType: "model_ModelPropertyCategory" = None, propertyTypes: "model_ModelPropertyCategory" = None, model_ModelPropertyType: "model_ModelProperty" = None, model_ModelPropertyType16: "model_Model" = None):
        self.id = id
        self.name = name
        self.description = description
        self.admissibleValues = admissibleValues
        self.defaultValue = defaultValue
        self.ModelPropertyType = ModelPropertyType
        self.propertyTypes = propertyTypes
        self.model_ModelPropertyType = model_ModelPropertyType
        self.model_ModelPropertyType16 = model_ModelPropertyType16
        
    @property
    def admissibleValues(self) -> str:
        return self.__admissibleValues

    @admissibleValues.setter
    def admissibleValues(self, admissibleValues: str):
        self.__admissibleValues = admissibleValues

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def defaultValue(self) -> str:
        return self.__defaultValue

    @defaultValue.setter
    def defaultValue(self, defaultValue: str):
        self.__defaultValue = defaultValue

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def ModelPropertyType(self):
        return self.__ModelPropertyType

    @ModelPropertyType.setter
    def ModelPropertyType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_ModelPropertyType__ModelPropertyType", None)
        self.__ModelPropertyType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "category"):
                opp_val = getattr(old_value, "category", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "category"):
                opp_val = getattr(value, "category", None)
                if opp_val is None:
                    setattr(value, "category", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def propertyTypes(self):
        return self.__propertyTypes

    @propertyTypes.setter
    def propertyTypes(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_ModelPropertyType__propertyTypes", None)
        self.__propertyTypes = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ModelPropertyCategory"):
                opp_val = getattr(old_value, "ModelPropertyCategory", None)
                if opp_val == self:
                    setattr(old_value, "ModelPropertyCategory", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ModelPropertyCategory"):
                opp_val = getattr(value, "ModelPropertyCategory", None)
                setattr(value, "ModelPropertyCategory", self)

    @property
    def model_ModelPropertyType16(self):
        return self.__model_ModelPropertyType16

    @model_ModelPropertyType16.setter
    def model_ModelPropertyType16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_ModelPropertyType__model_ModelPropertyType16", None)
        self.__model_ModelPropertyType16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_Model"):
                opp_val = getattr(old_value, "model_Model", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_Model"):
                opp_val = getattr(value, "model_Model", None)
                if opp_val is None:
                    setattr(value, "model_Model", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def model_ModelPropertyType(self):
        return self.__model_ModelPropertyType

    @model_ModelPropertyType.setter
    def model_ModelPropertyType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_ModelPropertyType__model_ModelPropertyType", None)
        self.__model_ModelPropertyType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_ModelProperty"):
                opp_val = getattr(old_value, "model_ModelProperty", None)
                if opp_val == self:
                    setattr(old_value, "model_ModelProperty", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_ModelProperty"):
                opp_val = getattr(value, "model_ModelProperty", None)
                setattr(value, "model_ModelProperty", self)
