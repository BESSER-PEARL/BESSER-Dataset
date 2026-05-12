####################
# STRUCTURAL MODEL #
####################

from besser.BUML.metamodel.structural import (
    Class, Property, Method, Parameter,
    BinaryAssociation, Generalization, DomainModel,
    Enumeration, EnumerationLiteral, Multiplicity,
    StringType, IntegerType, FloatType, BooleanType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    AnyType, Constraint, AssociationClass, Metadata
)

# Enumerations
key_type: Enumeration = Enumeration(
    name="key_type",
    literals={
            EnumerationLiteral(name="Primary"),
			EnumerationLiteral(name="Unique"),
			EnumerationLiteral(name="Foreign")
    }
)

ColumnType: Enumeration = Enumeration(
    name="ColumnType",
    literals={
            EnumerationLiteral(name="STD_FIELD"),
			EnumerationLiteral(name="NON_STD_FIELD")
    }
)

# Classes
database_DBModuleCommonProperty = Class(name="database_DBModuleCommonProperty")
database_DatabaseResourceData = Class(name="database_DatabaseResourceData")
JRESResourceInfo = Class(name="JRESResourceInfo")
database_TableResourceData = Class(name="database_TableResourceData")
DatabaseResourceData = Class(name="DatabaseResourceData")
database_TableColumn = Class(name="database_TableColumn")
database_ForeignKey = Class(name="database_ForeignKey")
database_TableIndexColumn = Class(name="database_TableIndexColumn")
database_TableIndex = Class(name="database_TableIndex")
database_TableKey = Class(name="database_TableKey")
ExtensibleModel = Class(name="ExtensibleModel")
database_ViewResourceData = Class(name="database_ViewResourceData")
database_DBGenContext = Class(name="database_DBGenContext")

# database_DBModuleCommonProperty class attributes and methods
database_DBModuleCommonProperty_database: Property = Property(name="database", type=StringType)
database_DBModuleCommonProperty_supportDatabases: Property = Property(name="supportDatabases", type=StringType)
database_DBModuleCommonProperty.attributes={database_DBModuleCommonProperty_supportDatabases, database_DBModuleCommonProperty_database}

# database_DatabaseResourceData class attributes and methods

# JRESResourceInfo class attributes and methods

# database_TableResourceData class attributes and methods

# DatabaseResourceData class attributes and methods

# database_TableColumn class attributes and methods
database_TableColumn_nullable: Property = Property(name="nullable", type=BooleanType)
database_TableColumn_defaultValue: Property = Property(name="defaultValue", type=StringType)
database_TableColumn_mark: Property = Property(name="mark", type=StringType)
database_TableColumn_comments: Property = Property(name="comments", type=StringType)
database_TableColumn_columnType: Property = Property(name="columnType", type=StringType)
database_TableColumn_name: Property = Property(name="name", type=StringType)
database_TableColumn_chineseName: Property = Property(name="chineseName", type=StringType)
database_TableColumn_description: Property = Property(name="description", type=StringType)
database_TableColumn_dataType: Property = Property(name="dataType", type=StringType)
database_TableColumn_columnName: Property = Property(name="columnName", type=StringType)
database_TableColumn_fieldName: Property = Property(name="fieldName", type=StringType)
database_TableColumn_primaryKey: Property = Property(name="primaryKey", type=BooleanType)
database_TableColumn_unique: Property = Property(name="unique", type=BooleanType)
database_TableColumn.attributes={database_TableColumn_mark, database_TableColumn_nullable, database_TableColumn_fieldName, database_TableColumn_dataType, database_TableColumn_defaultValue, database_TableColumn_chineseName, database_TableColumn_columnType, database_TableColumn_name, database_TableColumn_primaryKey, database_TableColumn_comments, database_TableColumn_columnName, database_TableColumn_unique, database_TableColumn_description}

# database_ForeignKey class attributes and methods
database_ForeignKey_tableName: Property = Property(name="tableName", type=StringType)
database_ForeignKey_fieldName: Property = Property(name="fieldName", type=StringType)
database_ForeignKey.attributes={database_ForeignKey_fieldName, database_ForeignKey_tableName}

# database_TableIndexColumn class attributes and methods
database_TableIndexColumn_columnName: Property = Property(name="columnName", type=StringType)
database_TableIndexColumn_ascending: Property = Property(name="ascending", type=BooleanType)
database_TableIndexColumn_columnType: Property = Property(name="columnType", type=StringType)
database_TableIndexColumn.attributes={database_TableIndexColumn_columnName, database_TableIndexColumn_ascending, database_TableIndexColumn_columnType}

# database_TableIndex class attributes and methods
database_TableIndex_name: Property = Property(name="name", type=StringType)
database_TableIndex_unique: Property = Property(name="unique", type=BooleanType)
database_TableIndex_cluster: Property = Property(name="cluster", type=BooleanType)
database_TableIndex_mark: Property = Property(name="mark", type=StringType)
database_TableIndex.attributes={database_TableIndex_name, database_TableIndex_cluster, database_TableIndex_unique, database_TableIndex_mark}

# database_TableKey class attributes and methods
database_TableKey_name: Property = Property(name="name", type=StringType)
database_TableKey_type: Property = Property(name="type", type=StringType)
database_TableKey_mark: Property = Property(name="mark", type=StringType)
database_TableKey.attributes={database_TableKey_mark, database_TableKey_type, database_TableKey_name}

# ExtensibleModel class attributes and methods

# database_ViewResourceData class attributes and methods
database_ViewResourceData_sql: Property = Property(name="sql", type=StringType)
database_ViewResourceData_isHistory: Property = Property(name="isHistory", type=BooleanType)
database_ViewResourceData.attributes={database_ViewResourceData_sql, database_ViewResourceData_isHistory}

# database_DBGenContext class attributes and methods

# Relationships
foreignkey5: BinaryAssociation = BinaryAssociation(
    name="foreignkey5",
    ends={
        Property(name="database_ForeignKey", type=database_TableColumn, multiplicity=Multiplicity(1, 1)),
        Property(name="database_TableColumn6", type=database_ForeignKey, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
columns0: BinaryAssociation = BinaryAssociation(
    name="columns0",
    ends={
        Property(name="database_TableColumn", type=database_TableResourceData, multiplicity=Multiplicity(1, 1)),
        Property(name="database_TableResourceData", type=database_TableColumn, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
indexes1: BinaryAssociation = BinaryAssociation(
    name="indexes1",
    ends={
        Property(name="database_TableIndex", type=database_TableResourceData, multiplicity=Multiplicity(1, 1)),
        Property(name="database_TableResourceData2", type=database_TableIndex, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
keys3: BinaryAssociation = BinaryAssociation(
    name="keys3",
    ends={
        Property(name="database_TableKey", type=database_TableResourceData, multiplicity=Multiplicity(1, 1)),
        Property(name="database_TableResourceData4", type=database_TableKey, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
columns7: BinaryAssociation = BinaryAssociation(
    name="columns7",
    ends={
        Property(name="database_TableIndexColumn", type=database_TableIndex, multiplicity=Multiplicity(1, 1)),
        Property(name="database_TableIndex8", type=database_TableIndexColumn, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
foreignKey9: BinaryAssociation = BinaryAssociation(
    name="foreignKey9",
    ends={
        Property(name="database_ForeignKey11", type=database_TableKey, multiplicity=Multiplicity(1, 1)),
        Property(name="database_TableKey10", type=database_ForeignKey, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
columns12: BinaryAssociation = BinaryAssociation(
    name="columns12",
    ends={
        Property(name="database_TableColumn14", type=database_TableKey, multiplicity=Multiplicity(1, 1)),
        Property(name="database_TableKey13", type=database_TableColumn, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_database_DatabaseResourceData_JRESResourceInfo = Generalization(general=JRESResourceInfo, specific=database_DatabaseResourceData)
gen_database_TableResourceData_DatabaseResourceData = Generalization(general=DatabaseResourceData, specific=database_TableResourceData)
gen_database_TableIndexColumn_ExtensibleModel = Generalization(general=ExtensibleModel, specific=database_TableIndexColumn)
gen_database_TableIndex_ExtensibleModel = Generalization(general=ExtensibleModel, specific=database_TableIndex)
gen_database_TableColumn_ExtensibleModel = Generalization(general=ExtensibleModel, specific=database_TableColumn)
gen_database_ViewResourceData_DatabaseResourceData = Generalization(general=DatabaseResourceData, specific=database_ViewResourceData)
gen_database_DBGenContext_ExtensibleModel = Generalization(general=ExtensibleModel, specific=database_DBGenContext)
gen_database_TableKey_ExtensibleModel = Generalization(general=ExtensibleModel, specific=database_TableKey)

# Domain Model
domain_model = DomainModel(
    name="database",
    types={database_DBModuleCommonProperty, database_DatabaseResourceData, JRESResourceInfo, database_TableResourceData, DatabaseResourceData, database_TableColumn, database_ForeignKey, database_TableIndexColumn, database_TableIndex, database_TableKey, ExtensibleModel, database_ViewResourceData, database_DBGenContext, key_type, ColumnType},
    associations={foreignkey5, columns0, indexes1, keys3, columns7, foreignKey9, columns12},
    generalizations={gen_database_DatabaseResourceData_JRESResourceInfo, gen_database_TableResourceData_DatabaseResourceData, gen_database_TableIndexColumn_ExtensibleModel, gen_database_TableIndex_ExtensibleModel, gen_database_TableColumn_ExtensibleModel, gen_database_ViewResourceData_DatabaseResourceData, gen_database_DBGenContext_ExtensibleModel, gen_database_TableKey_ExtensibleModel},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)