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
table_type: Enumeration = Enumeration(
    name="table_type",
    literals={
            EnumerationLiteral(name="COMMON"),
			EnumerationLiteral(name="TEMP_NO_VALUE"),
			EnumerationLiteral(name="TEMP_WITH_VALUE")
    }
)

# Classes
oracle_OracleTableProperty = Class(name="oracle_OracleTableProperty")
oracle_OracleIndexProperty = Class(name="oracle_OracleIndexProperty")
oracle_OracleViewProperty = Class(name="oracle_OracleViewProperty")
oracle_OracleModuleProperty = Class(name="oracle_OracleModuleProperty")
oracle_OracleSpaceResourceData = Class(name="oracle_OracleSpaceResourceData")
DatabaseResourceData = Class(name="DatabaseResourceData")
oracle_TableSpace = Class(name="oracle_TableSpace")
oracle_TableSpaceRelation = Class(name="oracle_TableSpaceRelation")
ExtensibleModel = Class(name="ExtensibleModel")
oracle_OracleUserResourceData = Class(name="oracle_OracleUserResourceData")
oracle_OracleUser = Class(name="oracle_OracleUser")
oracle_OraclePrivilege = Class(name="oracle_OraclePrivilege")
oracle_TriggerResourceData = Class(name="oracle_TriggerResourceData")
oracle_SequenceResourceData = Class(name="oracle_SequenceResourceData")
oracle_OracleSequenceProperty = Class(name="oracle_OracleSequenceProperty")
oracle_DatabaseModuleExtensibleProperty = Class(name="oracle_DatabaseModuleExtensibleProperty")

# oracle_OracleTableProperty class attributes and methods
oracle_OracleTableProperty_space: Property = Property(name="space", type=StringType)
oracle_OracleTableProperty_tabletype: Property = Property(name="tabletype", type=StringType)
oracle_OracleTableProperty.attributes={oracle_OracleTableProperty_tabletype, oracle_OracleTableProperty_space}

# oracle_OracleIndexProperty class attributes and methods
oracle_OracleIndexProperty_reverse: Property = Property(name="reverse", type=BooleanType)
oracle_OracleIndexProperty.attributes={oracle_OracleIndexProperty_reverse}

# oracle_OracleViewProperty class attributes and methods
oracle_OracleViewProperty_space: Property = Property(name="space", type=StringType)
oracle_OracleViewProperty.attributes={oracle_OracleViewProperty_space}

# oracle_OracleModuleProperty class attributes and methods
oracle_OracleModuleProperty_space: Property = Property(name="space", type=StringType)
oracle_OracleModuleProperty.attributes={oracle_OracleModuleProperty_space}

# oracle_OracleSpaceResourceData class attributes and methods

# DatabaseResourceData class attributes and methods

# oracle_TableSpace class attributes and methods
oracle_TableSpace_name: Property = Property(name="name", type=StringType)
oracle_TableSpace_chineseName: Property = Property(name="chineseName", type=StringType)
oracle_TableSpace_user: Property = Property(name="user", type=StringType)
oracle_TableSpace_file: Property = Property(name="file", type=StringType)
oracle_TableSpace_size: Property = Property(name="size", type=StringType)
oracle_TableSpace_description: Property = Property(name="description", type=StringType)
oracle_TableSpace_logicName: Property = Property(name="logicName", type=StringType)
oracle_TableSpace.attributes={oracle_TableSpace_file, oracle_TableSpace_logicName, oracle_TableSpace_size, oracle_TableSpace_name, oracle_TableSpace_chineseName, oracle_TableSpace_user, oracle_TableSpace_description}

# oracle_TableSpaceRelation class attributes and methods
oracle_TableSpaceRelation_mainSpace: Property = Property(name="mainSpace", type=StringType)
oracle_TableSpaceRelation_indexSpace: Property = Property(name="indexSpace", type=StringType)
oracle_TableSpaceRelation.attributes={oracle_TableSpaceRelation_mainSpace, oracle_TableSpaceRelation_indexSpace}

# ExtensibleModel class attributes and methods

# oracle_OracleUserResourceData class attributes and methods

# oracle_OracleUser class attributes and methods
oracle_OracleUser_name: Property = Property(name="name", type=StringType)
oracle_OracleUser_decription: Property = Property(name="decription", type=StringType)
oracle_OracleUser_attributes: Property = Property(name="attributes", type=StringType)
oracle_OracleUser_enable: Property = Property(name="enable", type=BooleanType)
oracle_OracleUser_password: Property = Property(name="password", type=StringType)
oracle_OracleUser_defaultTableSpace: Property = Property(name="defaultTableSpace", type=StringType)
oracle_OracleUser.attributes={oracle_OracleUser_defaultTableSpace, oracle_OracleUser_password, oracle_OracleUser_decription, oracle_OracleUser_attributes, oracle_OracleUser_enable, oracle_OracleUser_name}

# oracle_OraclePrivilege class attributes and methods
oracle_OraclePrivilege_name: Property = Property(name="name", type=StringType)
oracle_OraclePrivilege_type: Property = Property(name="type", type=StringType)
oracle_OraclePrivilege_decription: Property = Property(name="decription", type=StringType)
oracle_OraclePrivilege.attributes={oracle_OraclePrivilege_name, oracle_OraclePrivilege_type, oracle_OraclePrivilege_decription}

# oracle_TriggerResourceData class attributes and methods
oracle_TriggerResourceData_sql: Property = Property(name="sql", type=StringType)
oracle_TriggerResourceData.attributes={oracle_TriggerResourceData_sql}

# oracle_SequenceResourceData class attributes and methods
oracle_SequenceResourceData_tableName: Property = Property(name="tableName", type=StringType)
oracle_SequenceResourceData_start: Property = Property(name="start", type=StringType)
oracle_SequenceResourceData_increment: Property = Property(name="increment", type=StringType)
oracle_SequenceResourceData_minValue: Property = Property(name="minValue", type=StringType)
oracle_SequenceResourceData_maxValue: Property = Property(name="maxValue", type=StringType)
oracle_SequenceResourceData_cycle: Property = Property(name="cycle", type=BooleanType)
oracle_SequenceResourceData_cache: Property = Property(name="cache", type=StringType)
oracle_SequenceResourceData_useCache: Property = Property(name="useCache", type=BooleanType)
oracle_SequenceResourceData_isHistory: Property = Property(name="isHistory", type=BooleanType)
oracle_SequenceResourceData.attributes={oracle_SequenceResourceData_maxValue, oracle_SequenceResourceData_useCache, oracle_SequenceResourceData_isHistory, oracle_SequenceResourceData_minValue, oracle_SequenceResourceData_increment, oracle_SequenceResourceData_cycle, oracle_SequenceResourceData_cache, oracle_SequenceResourceData_tableName, oracle_SequenceResourceData_start}

# oracle_OracleSequenceProperty class attributes and methods
oracle_OracleSequenceProperty_space: Property = Property(name="space", type=StringType)
oracle_OracleSequenceProperty.attributes={oracle_OracleSequenceProperty_space}

# oracle_DatabaseModuleExtensibleProperty class attributes and methods
oracle_DatabaseModuleExtensibleProperty_tableType: Property = Property(name="tableType", type=StringType)
oracle_DatabaseModuleExtensibleProperty_space: Property = Property(name="space", type=StringType)
oracle_DatabaseModuleExtensibleProperty_splitField: Property = Property(name="splitField", type=StringType)
oracle_DatabaseModuleExtensibleProperty_splitNum: Property = Property(name="splitNum", type=StringType)
oracle_DatabaseModuleExtensibleProperty_startDate: Property = Property(name="startDate", type=StringType)
oracle_DatabaseModuleExtensibleProperty_bizPkg: Property = Property(name="bizPkg", type=StringType)
oracle_DatabaseModuleExtensibleProperty.attributes={oracle_DatabaseModuleExtensibleProperty_startDate, oracle_DatabaseModuleExtensibleProperty_splitNum, oracle_DatabaseModuleExtensibleProperty_tableType, oracle_DatabaseModuleExtensibleProperty_bizPkg, oracle_DatabaseModuleExtensibleProperty_space, oracle_DatabaseModuleExtensibleProperty_splitField}

# Relationships
spaces0: BinaryAssociation = BinaryAssociation(
    name="spaces0",
    ends={
        Property(name="oracle_TableSpace", type=oracle_OracleSpaceResourceData, multiplicity=Multiplicity(1, 1)),
        Property(name="oracle_OracleSpaceResourceData", type=oracle_TableSpace, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
relations1: BinaryAssociation = BinaryAssociation(
    name="relations1",
    ends={
        Property(name="oracle_TableSpaceRelation", type=oracle_OracleSpaceResourceData, multiplicity=Multiplicity(1, 1)),
        Property(name="oracle_OracleSpaceResourceData2", type=oracle_TableSpaceRelation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
users3: BinaryAssociation = BinaryAssociation(
    name="users3",
    ends={
        Property(name="oracle_OracleUser", type=oracle_OracleUserResourceData, multiplicity=Multiplicity(1, 1)),
        Property(name="oracle_OracleUserResourceData", type=oracle_OracleUser, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
privileges6: BinaryAssociation = BinaryAssociation(
    name="privileges6",
    ends={
        Property(name="oracle_OraclePrivilege8", type=oracle_OracleUser, multiplicity=Multiplicity(1, 1)),
        Property(name="oracle_OracleUser7", type=oracle_OraclePrivilege, multiplicity=Multiplicity(0, 9999))
    }
)
privileges4: BinaryAssociation = BinaryAssociation(
    name="privileges4",
    ends={
        Property(name="oracle_OraclePrivilege", type=oracle_OracleUserResourceData, multiplicity=Multiplicity(1, 1)),
        Property(name="oracle_OracleUserResourceData5", type=oracle_OraclePrivilege, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_oracle_OracleSpaceResourceData_DatabaseResourceData = Generalization(general=DatabaseResourceData, specific=oracle_OracleSpaceResourceData)
gen_oracle_TableSpaceRelation_ExtensibleModel = Generalization(general=ExtensibleModel, specific=oracle_TableSpaceRelation)
gen_oracle_TableSpace_ExtensibleModel = Generalization(general=ExtensibleModel, specific=oracle_TableSpace)
gen_oracle_OracleUserResourceData_DatabaseResourceData = Generalization(general=DatabaseResourceData, specific=oracle_OracleUserResourceData)
gen_oracle_OracleUser_ExtensibleModel = Generalization(general=ExtensibleModel, specific=oracle_OracleUser)
gen_oracle_OraclePrivilege_ExtensibleModel = Generalization(general=ExtensibleModel, specific=oracle_OraclePrivilege)
gen_oracle_TriggerResourceData_DatabaseResourceData = Generalization(general=DatabaseResourceData, specific=oracle_TriggerResourceData)
gen_oracle_SequenceResourceData_DatabaseResourceData = Generalization(general=DatabaseResourceData, specific=oracle_SequenceResourceData)
gen_oracle_DatabaseModuleExtensibleProperty_ExtensibleModel = Generalization(general=ExtensibleModel, specific=oracle_DatabaseModuleExtensibleProperty)

# Domain Model
domain_model = DomainModel(
    name="oracle",
    types={oracle_OracleTableProperty, oracle_OracleIndexProperty, oracle_OracleViewProperty, oracle_OracleModuleProperty, oracle_OracleSpaceResourceData, DatabaseResourceData, oracle_TableSpace, oracle_TableSpaceRelation, ExtensibleModel, oracle_OracleUserResourceData, oracle_OracleUser, oracle_OraclePrivilege, oracle_TriggerResourceData, oracle_SequenceResourceData, oracle_OracleSequenceProperty, oracle_DatabaseModuleExtensibleProperty, table_type},
    associations={spaces0, relations1, users3, privileges6, privileges4},
    generalizations={gen_oracle_OracleSpaceResourceData_DatabaseResourceData, gen_oracle_TableSpaceRelation_ExtensibleModel, gen_oracle_TableSpace_ExtensibleModel, gen_oracle_OracleUserResourceData_DatabaseResourceData, gen_oracle_OracleUser_ExtensibleModel, gen_oracle_OraclePrivilege_ExtensibleModel, gen_oracle_TriggerResourceData_DatabaseResourceData, gen_oracle_SequenceResourceData_DatabaseResourceData, gen_oracle_DatabaseModuleExtensibleProperty_ExtensibleModel},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)