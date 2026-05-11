from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class model_analytical_AnalyticalModel:

    pass
class model_behavioural_BehaviouralModel:

    pass
class VirtualCubeDimension:

    pass
class VirtualCubeMeasure:

    pass
class Level:

    pass
class olap_model_Model:

    pass
class Hierarchy:

    pass
class NamedSet:

    pass
class CalculatedMember:

    pass
class Measure:

    pass
class Dimension:

    pass
class VirtualCube:

    pass
class Cube:

    pass
class BusinessColumnSet:

    pass
class business_model_Model:

    pass
class model_business_BusinessView(BusinessColumnSet):

    pass
class model_business_BusinessTable(BusinessColumnSet):

    pass
class BusinessColumn:

    pass
class model_business_CalculatedBusinessColumn(BusinessColumn):

    pass
class model_business_SimpleBusinessColumn(BusinessColumn):

    pass
class BusinessViewInnerJoinRelationship:

    pass
class BusinessDomain:

    pass
class BusinessIdentifier:

    pass
class BusinessRelationship:

    pass
class PhysicalColumn:

    pass
class model_ModelObject(ABC):

    def __init__(self, uniqueName: str, description: str, id: str, name: str, model_ModelObject: set["model_ModelPropertyMapEntry"] = None):
        self.uniqueName = uniqueName
        self.description = description
        self.id = id
        self.name = name
        self.model_ModelObject = model_ModelObject if model_ModelObject is not None else set()
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description


    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id


    @property
    def uniqueName(self):
        return self.__uniqueName

    @uniqueName.setter
    def uniqueName(self, uniqueName: str):
        self.__uniqueName = uniqueName


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

    def __init__(self, key: str, model_ModelPropertyMapEntry11: "model_ModelObject" = None, model_ModelPropertyMapEntry: "model_ModelProperty" = None):
        self.key = key
        self.model_ModelPropertyMapEntry11 = model_ModelPropertyMapEntry11
        self.model_ModelPropertyMapEntry = model_ModelPropertyMapEntry
        
        pass
    @property
    def key(self):
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

class PhysicalForeignKey:

    pass
class PhysicalPrimaryKey:

    pass
class PhysicalTable:

    pass
class physical_model_Model:

    pass
class OlapModel:

    pass
class BusinessModel:

    pass
class PhysicalModel:

    pass
class ModelObject:

    pass
class model_olap_VirtualCubeDimension(ModelObject):

    pass
class model_business_BusinessColumnSet(ModelObject):

    pass
class model_olap_OlapModel(ModelObject):

    pass
class model_physical_PhysicalTable(ModelObject):

    def __init__(self, comment: str, type: str, tables: "PhysicalModel" = None, table: set["PhysicalColumn"] = None):
        self.comment = comment
        self.type = type
        self.tables = tables
        self.table = table if table is not None else set()
        
        pass
    @property
    def comment(self):
        return self.__comment

    @comment.setter
    def comment(self, comment: str):
        self.__comment = comment


    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type


    @property
    def table(self):
        return self.__table

    @table.setter
    def table(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_physical_PhysicalTable__table", None)
        self.__table = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "PhysicalColumn"):
                    opp_val = getattr(item, "PhysicalColumn", None)
                    
                    if opp_val == self:
                        setattr(item, "PhysicalColumn", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "PhysicalColumn"):
                    opp_val = getattr(item, "PhysicalColumn", None)
                    
                    setattr(item, "PhysicalColumn", self)
                    

    @property
    def tables(self):
        return self.__tables

    @tables.setter
    def tables(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_physical_PhysicalTable__tables", None)
        self.__tables = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PhysicalModel29"):
                opp_val = getattr(old_value, "PhysicalModel29", None)
                if opp_val == self:
                    setattr(old_value, "PhysicalModel29", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PhysicalModel29"):
                opp_val = getattr(value, "PhysicalModel29", None)
                setattr(value, "PhysicalModel29", self)

class model_olap_CalculatedMember(ModelObject):

    pass
class model_olap_Cube(ModelObject):

    pass
class model_business_BusinessDomain(ModelObject):

    pass
class model_olap_VirtualCube(ModelObject):

    pass
class model_physical_PhysicalColumn(ModelObject):

    def __init__(self, dataType: str, typeName: str, size: int, octectLength: int, decimalDigits: int, radix: int, defaultValue: str, nullable: bool, position: int, comment: str, columns: "PhysicalTable" = None):
        self.dataType = dataType
        self.typeName = typeName
        self.size = size
        self.octectLength = octectLength
        self.decimalDigits = decimalDigits
        self.radix = radix
        self.defaultValue = defaultValue
        self.nullable = nullable
        self.position = position
        self.comment = comment
        self.columns = columns
        
        pass
    @property
    def typeName(self):
        return self.__typeName

    @typeName.setter
    def typeName(self, typeName: str):
        self.__typeName = typeName


    @property
    def radix(self):
        return self.__radix

    @radix.setter
    def radix(self, radix: int):
        self.__radix = radix


    @property
    def comment(self):
        return self.__comment

    @comment.setter
    def comment(self, comment: str):
        self.__comment = comment


    @property
    def dataType(self):
        return self.__dataType

    @dataType.setter
    def dataType(self, dataType: str):
        self.__dataType = dataType


    @property
    def defaultValue(self):
        return self.__defaultValue

    @defaultValue.setter
    def defaultValue(self, defaultValue: str):
        self.__defaultValue = defaultValue


    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size: int):
        self.__size = size


    @property
    def nullable(self):
        return self.__nullable

    @nullable.setter
    def nullable(self, nullable: bool):
        self.__nullable = nullable


    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, position: int):
        self.__position = position


    @property
    def decimalDigits(self):
        return self.__decimalDigits

    @decimalDigits.setter
    def decimalDigits(self, decimalDigits: int):
        self.__decimalDigits = decimalDigits


    @property
    def octectLength(self):
        return self.__octectLength

    @octectLength.setter
    def octectLength(self, octectLength: int):
        self.__octectLength = octectLength


    @property
    def columns(self):
        return self.__columns

    @columns.setter
    def columns(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_physical_PhysicalColumn__columns", None)
        self.__columns = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PhysicalTable32"):
                opp_val = getattr(old_value, "PhysicalTable32", None)
                if opp_val == self:
                    setattr(old_value, "PhysicalTable32", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PhysicalTable32"):
                opp_val = getattr(value, "PhysicalTable32", None)
                setattr(value, "PhysicalTable32", self)

class model_olap_Dimension(ModelObject):

    pass
class model_physical_PhysicalForeignKey(ModelObject):

    def __init__(self, sourceName: str, destinationName: str, model_physical_PhysicalForeignKey: "PhysicalTable" = None, model_physical_PhysicalForeignKey43: set["PhysicalColumn"] = None, model_physical_PhysicalForeignKey46: "PhysicalTable" = None, model_physical_PhysicalForeignKey49: set["PhysicalColumn"] = None, foreignKeys: "PhysicalModel" = None):
        self.sourceName = sourceName
        self.destinationName = destinationName
        self.model_physical_PhysicalForeignKey = model_physical_PhysicalForeignKey
        self.model_physical_PhysicalForeignKey43 = model_physical_PhysicalForeignKey43 if model_physical_PhysicalForeignKey43 is not None else set()
        self.model_physical_PhysicalForeignKey46 = model_physical_PhysicalForeignKey46
        self.model_physical_PhysicalForeignKey49 = model_physical_PhysicalForeignKey49 if model_physical_PhysicalForeignKey49 is not None else set()
        self.foreignKeys = foreignKeys
        
        pass
    @property
    def destinationName(self):
        return self.__destinationName

    @destinationName.setter
    def destinationName(self, destinationName: str):
        self.__destinationName = destinationName


    @property
    def sourceName(self):
        return self.__sourceName

    @sourceName.setter
    def sourceName(self, sourceName: str):
        self.__sourceName = sourceName


    @property
    def foreignKeys(self):
        return self.__foreignKeys

    @foreignKeys.setter
    def foreignKeys(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_physical_PhysicalForeignKey__foreignKeys", None)
        self.__foreignKeys = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PhysicalModel52"):
                opp_val = getattr(old_value, "PhysicalModel52", None)
                if opp_val == self:
                    setattr(old_value, "PhysicalModel52", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PhysicalModel52"):
                opp_val = getattr(value, "PhysicalModel52", None)
                setattr(value, "PhysicalModel52", self)

    @property
    def model_physical_PhysicalForeignKey46(self):
        return self.__model_physical_PhysicalForeignKey46

    @model_physical_PhysicalForeignKey46.setter
    def model_physical_PhysicalForeignKey46(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_physical_PhysicalForeignKey__model_physical_PhysicalForeignKey46", None)
        self.__model_physical_PhysicalForeignKey46 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PhysicalTable47"):
                opp_val = getattr(old_value, "PhysicalTable47", None)
                if opp_val == self:
                    setattr(old_value, "PhysicalTable47", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PhysicalTable47"):
                opp_val = getattr(value, "PhysicalTable47", None)
                setattr(value, "PhysicalTable47", self)

    @property
    def model_physical_PhysicalForeignKey49(self):
        return self.__model_physical_PhysicalForeignKey49

    @model_physical_PhysicalForeignKey49.setter
    def model_physical_PhysicalForeignKey49(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_physical_PhysicalForeignKey__model_physical_PhysicalForeignKey49", None)
        self.__model_physical_PhysicalForeignKey49 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "PhysicalColumn50"):
                    opp_val = getattr(item, "PhysicalColumn50", None)
                    
                    if opp_val == self:
                        setattr(item, "PhysicalColumn50", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "PhysicalColumn50"):
                    opp_val = getattr(item, "PhysicalColumn50", None)
                    
                    setattr(item, "PhysicalColumn50", self)
                    

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
            if hasattr(old_value, "PhysicalTable41"):
                opp_val = getattr(old_value, "PhysicalTable41", None)
                if opp_val == self:
                    setattr(old_value, "PhysicalTable41", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PhysicalTable41"):
                opp_val = getattr(value, "PhysicalTable41", None)
                setattr(value, "PhysicalTable41", self)

    @property
    def model_physical_PhysicalForeignKey43(self):
        return self.__model_physical_PhysicalForeignKey43

    @model_physical_PhysicalForeignKey43.setter
    def model_physical_PhysicalForeignKey43(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_physical_PhysicalForeignKey__model_physical_PhysicalForeignKey43", None)
        self.__model_physical_PhysicalForeignKey43 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "PhysicalColumn44"):
                    opp_val = getattr(item, "PhysicalColumn44", None)
                    
                    if opp_val == self:
                        setattr(item, "PhysicalColumn44", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "PhysicalColumn44"):
                    opp_val = getattr(item, "PhysicalColumn44", None)
                    
                    setattr(item, "PhysicalColumn44", self)
                    

class model_olap_Hierarchy(ModelObject):

    pass
class model_business_BusinessIdentifier(ModelObject):

    pass
class model_olap_Level(ModelObject):

    pass
class model_olap_NamedSet(ModelObject):

    pass
class model_business_BusinessViewInnerJoinRelationship(ModelObject):

    pass
class model_physical_PhysicalPrimaryKey(ModelObject):

    pass
class model_business_BusinessRelationship(ModelObject):

    pass
class model_business_BusinessColumn(ModelObject):

    pass
class model_olap_VirtualCubeMeasure(ModelObject):

    pass
class model_olap_Measure(ModelObject):

    pass
class model_physical_PhysicalModel(ModelObject):

    def __init__(self, databaseName: str, databaseVersion: str, catalog: str, schema: str, physicalModels: "physical_model_Model" = None, model: set["PhysicalTable"] = None, model25: set["PhysicalPrimaryKey"] = None, model27: set["PhysicalForeignKey"] = None):
        self.databaseName = databaseName
        self.databaseVersion = databaseVersion
        self.catalog = catalog
        self.schema = schema
        self.physicalModels = physicalModels
        self.model = model if model is not None else set()
        self.model25 = model25 if model25 is not None else set()
        self.model27 = model27 if model27 is not None else set()
        
        pass
    @property
    def databaseVersion(self):
        return self.__databaseVersion

    @databaseVersion.setter
    def databaseVersion(self, databaseVersion: str):
        self.__databaseVersion = databaseVersion


    @property
    def catalog(self):
        return self.__catalog

    @catalog.setter
    def catalog(self, catalog: str):
        self.__catalog = catalog


    @property
    def schema(self):
        return self.__schema

    @schema.setter
    def schema(self, schema: str):
        self.__schema = schema


    @property
    def databaseName(self):
        return self.__databaseName

    @databaseName.setter
    def databaseName(self, databaseName: str):
        self.__databaseName = databaseName


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

    @property
    def model27(self):
        return self.__model27

    @model27.setter
    def model27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_physical_PhysicalModel__model27", None)
        self.__model27 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "PhysicalForeignKey"):
                    opp_val = getattr(item, "PhysicalForeignKey", None)
                    
                    if opp_val == self:
                        setattr(item, "PhysicalForeignKey", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "PhysicalForeignKey"):
                    opp_val = getattr(item, "PhysicalForeignKey", None)
                    
                    setattr(item, "PhysicalForeignKey", self)
                    

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_physical_PhysicalModel__model", None)
        self.__model = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "PhysicalTable"):
                    opp_val = getattr(item, "PhysicalTable", None)
                    
                    if opp_val == self:
                        setattr(item, "PhysicalTable", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "PhysicalTable"):
                    opp_val = getattr(item, "PhysicalTable", None)
                    
                    setattr(item, "PhysicalTable", self)
                    

    @property
    def model25(self):
        return self.__model25

    @model25.setter
    def model25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_physical_PhysicalModel__model25", None)
        self.__model25 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "PhysicalPrimaryKey"):
                    opp_val = getattr(item, "PhysicalPrimaryKey", None)
                    
                    if opp_val == self:
                        setattr(item, "PhysicalPrimaryKey", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "PhysicalPrimaryKey"):
                    opp_val = getattr(item, "PhysicalPrimaryKey", None)
                    
                    setattr(item, "PhysicalPrimaryKey", self)
                    

class model_business_BusinessModel(ModelObject):

    pass
class model_Model(ModelObject):

    pass
class model_ModelProperty:

    def __init__(self, value: str, model_ModelProperty: "model_ModelPropertyType" = None, model_ModelProperty9: "model_ModelPropertyMapEntry" = None):
        self.value = value
        self.model_ModelProperty = model_ModelProperty
        self.model_ModelProperty9 = model_ModelProperty9
        
        pass
    @property
    def value(self):
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

    def __init__(self, id: str, name: str, description: str, admissibleValues: str, defaultValue: str, ModelPropertyType: "model_ModelPropertyCategory" = None, propertyTypes: "model_ModelPropertyCategory" = None, model_ModelPropertyType18: "model_Model" = None, model_ModelPropertyType: "model_ModelProperty" = None):
        self.id = id
        self.name = name
        self.description = description
        self.admissibleValues = admissibleValues
        self.defaultValue = defaultValue
        self.ModelPropertyType = ModelPropertyType
        self.propertyTypes = propertyTypes
        self.model_ModelPropertyType18 = model_ModelPropertyType18
        self.model_ModelPropertyType = model_ModelPropertyType
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id


    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description


    @property
    def admissibleValues(self):
        return self.__admissibleValues

    @admissibleValues.setter
    def admissibleValues(self, admissibleValues: str):
        self.__admissibleValues = admissibleValues


    @property
    def defaultValue(self):
        return self.__defaultValue

    @defaultValue.setter
    def defaultValue(self, defaultValue: str):
        self.__defaultValue = defaultValue


    @property
    def model_ModelPropertyType18(self):
        return self.__model_ModelPropertyType18

    @model_ModelPropertyType18.setter
    def model_ModelPropertyType18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_ModelPropertyType__model_ModelPropertyType18", None)
        self.__model_ModelPropertyType18 = value
        
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

class model_ModelPropertyCategory:

    def __init__(self, name: str, description: str, model_ModelPropertyCategory: "model_ModelPropertyCategory" = None, model_ModelPropertyCategory0: "model_ModelPropertyCategory" = None, model_ModelPropertyCategory4: "model_ModelPropertyCategory" = None, model_ModelPropertyCategory2: set["model_ModelPropertyCategory"] = None, category: set["model_ModelPropertyType"] = None, ModelPropertyCategory: "model_ModelPropertyType" = None, model_ModelPropertyCategory21: "model_Model" = None):
        self.name = name
        self.description = description
        self.model_ModelPropertyCategory = model_ModelPropertyCategory
        self.model_ModelPropertyCategory0 = model_ModelPropertyCategory0
        self.model_ModelPropertyCategory4 = model_ModelPropertyCategory4
        self.model_ModelPropertyCategory2 = model_ModelPropertyCategory2 if model_ModelPropertyCategory2 is not None else set()
        self.category = category if category is not None else set()
        self.ModelPropertyCategory = ModelPropertyCategory
        self.model_ModelPropertyCategory21 = model_ModelPropertyCategory21
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description


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
    def model_ModelPropertyCategory21(self):
        return self.__model_ModelPropertyCategory21

    @model_ModelPropertyCategory21.setter
    def model_ModelPropertyCategory21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_ModelPropertyCategory__model_ModelPropertyCategory21", None)
        self.__model_ModelPropertyCategory21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_Model20"):
                opp_val = getattr(old_value, "model_Model20", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_Model20"):
                opp_val = getattr(value, "model_Model20", None)
                if opp_val is None:
                    setattr(value, "model_Model20", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

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
