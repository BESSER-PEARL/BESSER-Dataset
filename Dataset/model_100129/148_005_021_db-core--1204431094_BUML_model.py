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
DatabaseDataType: Enumeration = Enumeration(
    name="DatabaseDataType",
    literals={
            EnumerationLiteral(name="Identity"),
			EnumerationLiteral(name="Character"),
			EnumerationLiteral(name="Varchar"),
			EnumerationLiteral(name="Decimal"),
			EnumerationLiteral(name="Boolean"),
			EnumerationLiteral(name="Date"),
			EnumerationLiteral(name="Time"),
			EnumerationLiteral(name="TimeStamp"),
			EnumerationLiteral(name="Integer"),
			EnumerationLiteral(name="Float"),
			EnumerationLiteral(name="Graphical"),
			EnumerationLiteral(name="Text"),
			EnumerationLiteral(name="Blob")
    }
)

OrderingType: Enumeration = Enumeration(
    name="OrderingType",
    literals={
            EnumerationLiteral(name="Ascend"),
			EnumerationLiteral(name="Descend")
    }
)

# Classes
core_ConnectionConfig = Class(name="core_ConnectionConfig")
core_CatalogContainer = Class(name="core_CatalogContainer")
core_Connection = Class(name="core_Connection", is_abstract=True)
ContextID = Class(name="ContextID")
ContextProvider = Class(name="ContextProvider")
core_CatalogGenerationStrategy = Class(name="core_CatalogGenerationStrategy")
core_CatalogMetaData = Class(name="core_CatalogMetaData", is_abstract=True)
core_ConnectionDescription = Class(name="core_ConnectionDescription", is_abstract=True)
core_ConnectionManager = Class(name="core_ConnectionManager", is_abstract=True)
Service = Class(name="Service")
core_DatabaseContainer = Class(name="core_DatabaseContainer")
ServiceConfig = Class(name="ServiceConfig")
core_ConnectionCredentials = Class(name="core_ConnectionCredentials")
Credentials = Class(name="Credentials")
core_DatabaseObjectDef = Class(name="core_DatabaseObjectDef", is_abstract=True)
core_DatabaseManager = Class(name="core_DatabaseManager", is_abstract=True)
core_PreparedStatement = Class(name="core_PreparedStatement", is_abstract=True)
Statement = Class(name="Statement")
core_QualifiedName = Class(name="core_QualifiedName")
core_DataSourceFactory = Class(name="core_DataSourceFactory", is_abstract=True)
core_IndexDef = Class(name="core_IndexDef")
DatabaseObjectDef = Class(name="DatabaseObjectDef")
core_IndexColumnDef = Class(name="core_IndexColumnDef")
core_ViewDef = Class(name="core_ViewDef")
TableDef = Class(name="TableDef")
core_SchemaDef = Class(name="core_SchemaDef")
core_Statement = Class(name="core_Statement", is_abstract=True)
core_TableDef = Class(name="core_TableDef")
core_TableColumnDef = Class(name="core_TableColumnDef")

# core_ConnectionConfig class attributes and methods
core_ConnectionConfig_vendor: Property = Property(name="vendor", type=StringType)
core_ConnectionConfig_version: Property = Property(name="version", type=StringType)
core_ConnectionConfig_url: Property = Property(name="url", type=StringType)
core_ConnectionConfig_catalog: Property = Property(name="catalog", type=StringType)
core_ConnectionConfig_persistent: Property = Property(name="persistent", type=BooleanType)
core_ConnectionConfig.attributes={core_ConnectionConfig_url, core_ConnectionConfig_catalog, core_ConnectionConfig_persistent, core_ConnectionConfig_version, core_ConnectionConfig_vendor}

# core_CatalogContainer class attributes and methods
core_CatalogContainer_name: Property = Property(name="name", type=StringType)
core_CatalogContainer_active: Property = Property(name="active", type=BooleanType)
core_CatalogContainer_supportsGuestAccess: Property = Property(name="supportsGuestAccess", type=BooleanType)
core_CatalogContainer_m_loadSchema: Method = Method(name="loadSchema", parameters={Parameter(name='core_name', type=StringType)}, type=StringType)
core_CatalogContainer_m_loadTable: Method = Method(name="loadTable", parameters={Parameter(name='core_name', type=StringType), Parameter(name='core_schema', type=StringType)}, type=StringType)
core_CatalogContainer_m_loadView: Method = Method(name="loadView", parameters={Parameter(name='core_name', type=StringType), Parameter(name='core_schema', type=StringType)}, type=StringType)
core_CatalogContainer_m_removeIndex: Method = Method(name="removeIndex", parameters={Parameter(name='core_index', type=StringType)})
core_CatalogContainer_m_removeSchema: Method = Method(name="removeSchema", parameters={Parameter(name='core_schema', type=StringType)})
core_CatalogContainer_m_removeTable: Method = Method(name="removeTable", parameters={Parameter(name='core_table', type=StringType)})
core_CatalogContainer_m_removeView: Method = Method(name="removeView", parameters={Parameter(name='core_view', type=StringType)})
core_CatalogContainer_m_createConnection: Method = Method(name="createConnection", parameters={Parameter(name='core_factory', type=StringType)})
core_CatalogContainer_m_createConnection: Method = Method(name="createConnection", parameters={Parameter(name='core_user', type=StringType), Parameter(name='core_factory', type=StringType), Parameter(name='core_password', type=StringType)})
core_CatalogContainer_m_getMetaData: Method = Method(name="getMetaData", parameters={}, type=StringType)
core_CatalogContainer_m_getCatalogContext: Method = Method(name="getCatalogContext", parameters={}, type=StringType)
core_CatalogContainer_m_loadIndex: Method = Method(name="loadIndex", parameters={Parameter(name='core_name', type=StringType), Parameter(name='core_table', type=StringType)}, type=StringType)
core_CatalogContainer.attributes={core_CatalogContainer_active, core_CatalogContainer_name, core_CatalogContainer_supportsGuestAccess}
core_CatalogContainer.methods={core_CatalogContainer_m_getCatalogContext, core_CatalogContainer_m_getMetaData, core_CatalogContainer_m_removeSchema, core_CatalogContainer_m_loadTable, core_CatalogContainer_m_loadSchema, core_CatalogContainer_m_loadView, core_CatalogContainer_m_loadIndex, core_CatalogContainer_m_removeIndex, core_CatalogContainer_m_createConnection, core_CatalogContainer_m_removeTable, core_CatalogContainer_m_removeView, core_CatalogContainer_m_createConnection}

# core_Connection class attributes and methods
core_Connection_m_close: Method = Method(name="close", parameters={})
core_Connection_m_createStatement: Method = Method(name="createStatement", parameters={}, type=StringType)
core_Connection_m_createStatement: Method = Method(name="createStatement", parameters={Parameter(name='core_native', type=StringType)}, type=StringType)
core_Connection_m_createStatement: Method = Method(name="createStatement", parameters={Parameter(name='core_native', type=StringType), Parameter(name='core_updatable', type=StringType)}, type=StringType)
core_Connection_m_getCatalog: Method = Method(name="getCatalog", parameters={}, type=StringType)
core_Connection_m_getCatalogGenerationStrategy: Method = Method(name="getCatalogGenerationStrategy", parameters={}, type=StringType)
core_Connection_m_getCatalogMetaData: Method = Method(name="getCatalogMetaData", parameters={}, type=StringType)
core_Connection_m_getConnectionDescription: Method = Method(name="getConnectionDescription", parameters={}, type=StringType)
core_Connection_m_prepareStatement: Method = Method(name="prepareStatement", parameters={Parameter(name='core_sql', type=StringType)}, type=StringType)
core_Connection_m_prepareStatement: Method = Method(name="prepareStatement", parameters={Parameter(name='core_sql', type=StringType), Parameter(name='core_native', type=StringType)}, type=StringType)
core_Connection_m_prepareStatement: Method = Method(name="prepareStatement", parameters={Parameter(name='core_updatable', type=StringType), Parameter(name='core_native', type=StringType), Parameter(name='core_sql', type=StringType)}, type=StringType)
core_Connection_m_setCatalog: Method = Method(name="setCatalog", parameters={Parameter(name='core_catalog', type=StringType)})
core_Connection_m_translate: Method = Method(name="translate", parameters={Parameter(name='core_sql', type=StringType)}, type=StringType)
core_Connection.methods={core_Connection_m_createStatement, core_Connection_m_getCatalog, core_Connection_m_getCatalogMetaData, core_Connection_m_createStatement, core_Connection_m_prepareStatement, core_Connection_m_close, core_Connection_m_setCatalog, core_Connection_m_getCatalogGenerationStrategy, core_Connection_m_translate, core_Connection_m_createStatement, core_Connection_m_getConnectionDescription, core_Connection_m_prepareStatement, core_Connection_m_prepareStatement}

# ContextID class attributes and methods

# ContextProvider class attributes and methods

# core_CatalogGenerationStrategy class attributes and methods
core_CatalogGenerationStrategy_createIndexOnView: Property = Property(name="createIndexOnView", type=BooleanType)
core_CatalogGenerationStrategy_createRelativeRecordNumber: Property = Property(name="createRelativeRecordNumber", type=BooleanType)
core_CatalogGenerationStrategy.attributes={core_CatalogGenerationStrategy_createRelativeRecordNumber, core_CatalogGenerationStrategy_createIndexOnView}

# core_CatalogMetaData class attributes and methods
core_CatalogMetaData_m_getView: Method = Method(name="getView", parameters={Parameter(name='core_table', type=StringType), Parameter(name='core_schema', type=StringType)}, type=StringType)
core_CatalogMetaData_m_getIndex: Method = Method(name="getIndex", parameters={Parameter(name='core_schema', type=StringType), Parameter(name='core_index', type=StringType), Parameter(name='core_table', type=StringType)}, type=StringType)
core_CatalogMetaData_m_getSchema: Method = Method(name="getSchema", parameters={Parameter(name='core_schema', type=StringType)}, type=StringType)
core_CatalogMetaData_m_getSchemas: Method = Method(name="getSchemas", parameters={}, type=StringType)
core_CatalogMetaData_m_getTable: Method = Method(name="getTable", parameters={Parameter(name='core_schema', type=StringType), Parameter(name='core_table', type=StringType)}, type=StringType)
core_CatalogMetaData_m_getTable: Method = Method(name="getTable", parameters={Parameter(name='core_table', type=StringType), Parameter(name='core_connectionDescription', type=StringType)}, type=StringType)
core_CatalogMetaData.methods={core_CatalogMetaData_m_getView, core_CatalogMetaData_m_getIndex, core_CatalogMetaData_m_getSchemas, core_CatalogMetaData_m_getTable, core_CatalogMetaData_m_getSchema, core_CatalogMetaData_m_getTable}

# core_ConnectionDescription class attributes and methods
core_ConnectionDescription_schemas: Property = Property(name="schemas", type=StringType)
core_ConnectionDescription.attributes={core_ConnectionDescription_schemas}

# core_ConnectionManager class attributes and methods
core_ConnectionManager_m_createConnection: Method = Method(name="createConnection", parameters={}, type=StringType)
core_ConnectionManager_m_createConnection: Method = Method(name="createConnection", parameters={Parameter(name='core_catalog', type=StringType)}, type=StringType)
core_ConnectionManager_m_createConnection: Method = Method(name="createConnection", parameters={Parameter(name='core_password', type=StringType), Parameter(name='core_user', type=StringType)}, type=StringType)
core_ConnectionManager_m_createConnection: Method = Method(name="createConnection", parameters={Parameter(name='core_password', type=StringType), Parameter(name='core_catalog', type=StringType), Parameter(name='core_user', type=StringType)}, type=StringType)
core_ConnectionManager.methods={core_ConnectionManager_m_createConnection, core_ConnectionManager_m_createConnection, core_ConnectionManager_m_createConnection, core_ConnectionManager_m_createConnection}

# Service class attributes and methods

# core_DatabaseContainer class attributes and methods
core_DatabaseContainer_vendor: Property = Property(name="vendor", type=StringType)
core_DatabaseContainer_version: Property = Property(name="version", type=StringType)
core_DatabaseContainer.attributes={core_DatabaseContainer_version, core_DatabaseContainer_vendor}

# ServiceConfig class attributes and methods

# core_ConnectionCredentials class attributes and methods

# Credentials class attributes and methods

# core_DatabaseObjectDef class attributes and methods

# core_DatabaseManager class attributes and methods
core_DatabaseManager_m_dropIndex: Method = Method(name="dropIndex", parameters={Parameter(name='core_connection', type=StringType), Parameter(name='core_index', type=StringType)})
core_DatabaseManager_m_dropSchema: Method = Method(name="dropSchema", parameters={Parameter(name='core_connection', type=StringType), Parameter(name='core_schema', type=StringType), Parameter(name='core_ignoreFailOnNonEmpty', type=StringType)})
core_DatabaseManager_m_dropTable: Method = Method(name="dropTable", parameters={Parameter(name='core_table', type=StringType), Parameter(name='core_connection', type=StringType)})
core_DatabaseManager_m_dropView: Method = Method(name="dropView", parameters={Parameter(name='core_connection', type=StringType), Parameter(name='core_view', type=StringType)})
core_DatabaseManager_m_isStarted: Method = Method(name="isStarted", parameters={}, type=BooleanType)
core_DatabaseManager_m_start: Method = Method(name="start", parameters={Parameter(name='core_databaseContainer', type=StringType)})
core_DatabaseManager_m_createIndex: Method = Method(name="createIndex", parameters={Parameter(name='core_name', type=StringType), Parameter(name='core_connection', type=StringType), Parameter(name='core_table', type=StringType), Parameter(name='core_index', type=StringType)}, type=StringType)
core_DatabaseManager_m_createSchema: Method = Method(name="createSchema", parameters={Parameter(name='core_schema', type=StringType), Parameter(name='core_connection', type=StringType), Parameter(name='core_name', type=StringType)}, type=StringType)
core_DatabaseManager_m_createTable: Method = Method(name="createTable", parameters={Parameter(name='core_table', type=StringType), Parameter(name='core_schema', type=StringType), Parameter(name='core_connection', type=StringType), Parameter(name='core_name', type=StringType)}, type=StringType)
core_DatabaseManager_m_createView: Method = Method(name="createView", parameters={Parameter(name='core_connection', type=StringType), Parameter(name='core_name', type=StringType), Parameter(name='core_schema', type=StringType), Parameter(name='core_view', type=StringType)}, type=StringType)
core_DatabaseManager.methods={core_DatabaseManager_m_dropSchema, core_DatabaseManager_m_createView, core_DatabaseManager_m_isStarted, core_DatabaseManager_m_dropView, core_DatabaseManager_m_createSchema, core_DatabaseManager_m_dropTable, core_DatabaseManager_m_createTable, core_DatabaseManager_m_start, core_DatabaseManager_m_dropIndex, core_DatabaseManager_m_createIndex}

# core_PreparedStatement class attributes and methods
core_PreparedStatement_m_addBatch: Method = Method(name="addBatch", parameters={})
core_PreparedStatement_m_clearParameters: Method = Method(name="clearParameters", parameters={})
core_PreparedStatement_m_execute: Method = Method(name="execute", parameters={}, type=BooleanType)
core_PreparedStatement_m_executeQuery: Method = Method(name="executeQuery", parameters={}, type=StringType)
core_PreparedStatement_m_executeUpdate: Method = Method(name="executeUpdate", parameters={}, type=IntegerType)
core_PreparedStatement_m_setInt: Method = Method(name="setInt", parameters={Parameter(name='core_position', type=StringType), Parameter(name='core_value', type=StringType)})
core_PreparedStatement_m_setString: Method = Method(name="setString", parameters={Parameter(name='core_value', type=StringType), Parameter(name='core_position', type=StringType)})
core_PreparedStatement.methods={core_PreparedStatement_m_executeUpdate, core_PreparedStatement_m_addBatch, core_PreparedStatement_m_setString, core_PreparedStatement_m_executeQuery, core_PreparedStatement_m_clearParameters, core_PreparedStatement_m_execute, core_PreparedStatement_m_setInt}

# Statement class attributes and methods

# core_QualifiedName class attributes and methods
core_QualifiedName_qualifiers: Property = Property(name="qualifiers", type=StringType)
core_QualifiedName_m_getFirstQualifier: Method = Method(name="getFirstQualifier", parameters={}, type=StringType)
core_QualifiedName_m_getLastQualifier: Method = Method(name="getLastQualifier", parameters={}, type=StringType)
core_QualifiedName.attributes={core_QualifiedName_qualifiers}
core_QualifiedName.methods={core_QualifiedName_m_getLastQualifier, core_QualifiedName_m_getFirstQualifier}

# core_DataSourceFactory class attributes and methods

# core_IndexDef class attributes and methods
core_IndexDef_clustered: Property = Property(name="clustered", type=BooleanType)
core_IndexDef_unique: Property = Property(name="unique", type=BooleanType)
core_IndexDef.attributes={core_IndexDef_clustered, core_IndexDef_unique}

# DatabaseObjectDef class attributes and methods

# core_IndexColumnDef class attributes and methods
core_IndexColumnDef_ordering: Property = Property(name="ordering", type=StringType)
core_IndexColumnDef_sequence: Property = Property(name="sequence", type=IntegerType)
core_IndexColumnDef_name: Property = Property(name="name", type=StringType)
core_IndexColumnDef.attributes={core_IndexColumnDef_ordering, core_IndexColumnDef_sequence, core_IndexColumnDef_name}

# core_ViewDef class attributes and methods
core_ViewDef_querySelect: Property = Property(name="querySelect", type=StringType)
core_ViewDef.attributes={core_ViewDef_querySelect}

# TableDef class attributes and methods

# core_SchemaDef class attributes and methods

# core_Statement class attributes and methods
core_Statement_m_close: Method = Method(name="close", parameters={})
core_Statement_m_execute: Method = Method(name="execute", parameters={Parameter(name='core_sql', type=StringType)}, type=BooleanType)
core_Statement_m_executeQuery: Method = Method(name="executeQuery", parameters={Parameter(name='core_sql', type=StringType)}, type=StringType)
core_Statement_m_executeUpdate: Method = Method(name="executeUpdate", parameters={Parameter(name='core_sql', type=StringType)}, type=IntegerType)
core_Statement_m_addBatch: Method = Method(name="addBatch", parameters={Parameter(name='core_sql', type=StringType)})
core_Statement_m_clearBatch: Method = Method(name="clearBatch", parameters={})
core_Statement_m_executeBatch: Method = Method(name="executeBatch", parameters={}, type=StringType)
core_Statement.methods={core_Statement_m_executeUpdate, core_Statement_m_close, core_Statement_m_executeBatch, core_Statement_m_execute, core_Statement_m_executeQuery, core_Statement_m_clearBatch, core_Statement_m_addBatch}

# core_TableDef class attributes and methods

# core_TableColumnDef class attributes and methods
core_TableColumnDef_dataType: Property = Property(name="dataType", type=StringType)
core_TableColumnDef_default: Property = Property(name="default", type=BooleanType)
core_TableColumnDef_length: Property = Property(name="length", type=IntegerType)
core_TableColumnDef_name: Property = Property(name="name", type=StringType)
core_TableColumnDef_nullable: Property = Property(name="nullable", type=BooleanType)
core_TableColumnDef_scale: Property = Property(name="scale", type=IntegerType)
core_TableColumnDef.attributes={core_TableColumnDef_dataType, core_TableColumnDef_length, core_TableColumnDef_nullable, core_TableColumnDef_default, core_TableColumnDef_scale, core_TableColumnDef_name}

# Relationships
connectionConfig0: BinaryAssociation = BinaryAssociation(
    name="connectionConfig0",
    ends={
        Property(name="core_ConnectionConfig", type=core_CatalogContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="core_CatalogContainer", type=core_ConnectionConfig, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
generationStrategy1: BinaryAssociation = BinaryAssociation(
    name="generationStrategy1",
    ends={
        Property(name="core_CatalogGenerationStrategy", type=core_CatalogContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="core_CatalogContainer2", type=core_CatalogGenerationStrategy, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
catalogContainers5: BinaryAssociation = BinaryAssociation(
    name="catalogContainers5",
    ends={
        Property(name="core_CatalogContainer6", type=core_DatabaseContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="core_DatabaseContainer", type=core_CatalogContainer, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
defaultCatalogContainer7: BinaryAssociation = BinaryAssociation(
    name="defaultCatalogContainer7",
    ends={
        Property(name="core_CatalogContainer9", type=core_DatabaseContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="core_DatabaseContainer8", type=core_CatalogContainer, multiplicity=Multiplicity(1, 1))
    }
)
credentials3: BinaryAssociation = BinaryAssociation(
    name="credentials3",
    ends={
        Property(name="core_ConnectionCredentials", type=core_ConnectionConfig, multiplicity=Multiplicity(1, 1)),
        Property(name="core_ConnectionConfig4", type=core_ConnectionCredentials, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
columns10: BinaryAssociation = BinaryAssociation(
    name="columns10",
    ends={
        Property(name="core_IndexColumnDef", type=core_IndexDef, multiplicity=Multiplicity(1, 1)),
        Property(name="core_IndexDef", type=core_IndexColumnDef, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
columns11: BinaryAssociation = BinaryAssociation(
    name="columns11",
    ends={
        Property(name="core_TableColumnDef", type=core_TableDef, multiplicity=Multiplicity(1, 1)),
        Property(name="core_TableDef", type=core_TableColumnDef, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_core_Connection_ContextID = Generalization(general=ContextID, specific=core_Connection)
gen_core_Connection_ContextProvider = Generalization(general=ContextProvider, specific=core_Connection)
gen_core_ConnectionManager_Service = Generalization(general=Service, specific=core_ConnectionManager)
gen_core_DatabaseContainer_ServiceConfig = Generalization(general=ServiceConfig, specific=core_DatabaseContainer)
gen_core_ConnectionConfig_ServiceConfig = Generalization(general=ServiceConfig, specific=core_ConnectionConfig)
gen_core_ConnectionCredentials_Credentials = Generalization(general=Credentials, specific=core_ConnectionCredentials)
gen_core_DatabaseManager_Service = Generalization(general=Service, specific=core_DatabaseManager)
gen_core_PreparedStatement_Statement = Generalization(general=Statement, specific=core_PreparedStatement)
gen_core_IndexDef_DatabaseObjectDef = Generalization(general=DatabaseObjectDef, specific=core_IndexDef)
gen_core_IndexColumnDef_DatabaseObjectDef = Generalization(general=DatabaseObjectDef, specific=core_IndexColumnDef)
gen_core_TableColumnDef_DatabaseObjectDef = Generalization(general=DatabaseObjectDef, specific=core_TableColumnDef)
gen_core_ViewDef_TableDef = Generalization(general=TableDef, specific=core_ViewDef)
gen_core_SchemaDef_DatabaseObjectDef = Generalization(general=DatabaseObjectDef, specific=core_SchemaDef)
gen_core_TableDef_DatabaseObjectDef = Generalization(general=DatabaseObjectDef, specific=core_TableDef)

# Domain Model
domain_model = DomainModel(
    name="core",
    types={core_ConnectionConfig, core_CatalogContainer, core_Connection, ContextID, ContextProvider, core_CatalogGenerationStrategy, core_CatalogMetaData, core_ConnectionDescription, core_ConnectionManager, Service, core_DatabaseContainer, ServiceConfig, core_ConnectionCredentials, Credentials, core_DatabaseObjectDef, core_DatabaseManager, core_PreparedStatement, Statement, core_QualifiedName, core_DataSourceFactory, core_IndexDef, DatabaseObjectDef, core_IndexColumnDef, core_ViewDef, TableDef, core_SchemaDef, core_Statement, core_TableDef, core_TableColumnDef, DatabaseDataType, OrderingType},
    associations={connectionConfig0, generationStrategy1, catalogContainers5, defaultCatalogContainer7, credentials3, columns10, columns11},
    generalizations={gen_core_Connection_ContextID, gen_core_Connection_ContextProvider, gen_core_ConnectionManager_Service, gen_core_DatabaseContainer_ServiceConfig, gen_core_ConnectionConfig_ServiceConfig, gen_core_ConnectionCredentials_Credentials, gen_core_DatabaseManager_Service, gen_core_PreparedStatement_Statement, gen_core_IndexDef_DatabaseObjectDef, gen_core_IndexColumnDef_DatabaseObjectDef, gen_core_TableColumnDef_DatabaseObjectDef, gen_core_ViewDef_TableDef, gen_core_SchemaDef_DatabaseObjectDef, gen_core_TableDef_DatabaseObjectDef},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)