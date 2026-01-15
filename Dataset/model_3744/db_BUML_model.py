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
SQLDataType: Enumeration = Enumeration(
    name="SQLDataType",
    literals={
            EnumerationLiteral(name="Text"),
			EnumerationLiteral(name="Date"),
			EnumerationLiteral(name="DateTime"),
			EnumerationLiteral(name="Time"),
			EnumerationLiteral(name="Integer"),
			EnumerationLiteral(name="Long"),
			EnumerationLiteral(name="Double"),
			EnumerationLiteral(name="Clob"),
			EnumerationLiteral(name="Blob"),
			EnumerationLiteral(name="Array"),
			EnumerationLiteral(name="Object"),
			EnumerationLiteral(name="Boolean")
    }
)

QueryType: Enumeration = Enumeration(
    name="QueryType",
    literals={
            EnumerationLiteral(name="Select"),
			EnumerationLiteral(name="Update"),
			EnumerationLiteral(name="SPSelect"),
			EnumerationLiteral(name="SPUpdate")
    }
)

RSHoldabilityMode: Enumeration = Enumeration(
    name="RSHoldabilityMode",
    literals={
            EnumerationLiteral(name="HoldCursorsOverCommit"),
			EnumerationLiteral(name="CloseCursorsOverCommit")
    }
)

RSScrollMode: Enumeration = Enumeration(
    name="RSScrollMode",
    literals={
            EnumerationLiteral(name="ScrollInsensitive"),
			EnumerationLiteral(name="ScrollSensitive"),
			EnumerationLiteral(name="ForwardOnly")
    }
)

TransactionMode: Enumeration = Enumeration(
    name="TransactionMode",
    literals={
            EnumerationLiteral(name="None"),
			EnumerationLiteral(name="ReadCommitted"),
			EnumerationLiteral(name="ReadUncommitted"),
			EnumerationLiteral(name="RepeatableRead"),
			EnumerationLiteral(name="Serializable")
    }
)

VariableScope: Enumeration = Enumeration(
    name="VariableScope",
    literals={
            EnumerationLiteral(name="Local"),
			EnumerationLiteral(name="Global"),
			EnumerationLiteral(name="Runtime")
    }
)

VariableType: Enumeration = Enumeration(
    name="VariableType",
    literals={
            EnumerationLiteral(name="Text"),
			EnumerationLiteral(name="Integer"),
			EnumerationLiteral(name="Decimal"),
			EnumerationLiteral(name="Datetime"),
			EnumerationLiteral(name="Date"),
			EnumerationLiteral(name="Time"),
			EnumerationLiteral(name="Object"),
			EnumerationLiteral(name="Boolean"),
			EnumerationLiteral(name="Array")
    }
)

SynchMode: Enumeration = Enumeration(
    name="SynchMode",
    literals={
            EnumerationLiteral(name="ReadOnly"),
			EnumerationLiteral(name="Synch")
    }
)

# Classes
db_DBDriver = Class(name="db::DBDriver")
db_Query = Class(name="db::Query")
db_DBConnection = Class(name="db::DBConnection")
DBResource = Class(name="DBResource")
db_SafiDriverManager = Class(name="db::SafiDriverManager")
db_QueryParameter = Class(name="db::QueryParameter")
db_SafiResultSet = Class(name="db::SafiResultSet")
db_DBResource = Class(name="db::DBResource", is_abstract=True)
db_config_ServerResource = Class(name="db::config::ServerResource")
db_Variable = Class(name="db::Variable")
config_User = Class(name="config::User")
db_config_SafiServer = Class(name="db::config::SafiServer")
ServerResource = Class(name="ServerResource")
db_config_Entitlement = Class(name="db::config::Entitlement")
db_config_User = Class(name="db::config::User")
config_Role = Class(name="config::Role")
db_config_Saflet = Class(name="db::config::Saflet")
db_config_Role = Class(name="db::config::Role")
config_Entitlement = Class(name="config::Entitlement")
config_Prompt = Class(name="config::Prompt")
db_config_Prompt = Class(name="db::config::Prompt")
config_SafletProject = Class(name="config::SafletProject")
db_config_SafletProject = Class(name="db::config::SafletProject")
config_Saflet = Class(name="config::Saflet")
db_config_TelephonySubsystem = Class(name="db::config::TelephonySubsystem")
config_SafiServer = Class(name="config::SafiServer")
db_config_SFTPInfo = Class(name="db::config::SFTPInfo", is_abstract=True)

# db_DBDriver class attributes and methods
db_DBDriver_exampleUrl: Property = Property(name="exampleUrl", type=StringType)
db_DBDriver_jars: Property = Property(name="jars", type=StringType)
db_DBDriver_default: Property = Property(name="default", type=BooleanType)
db_DBDriver_guideUrl: Property = Property(name="guideUrl", type=StringType)
db_DBDriver_websiteUrl: Property = Property(name="websiteUrl", type=StringType)
db_DBDriver_defaultPort: Property = Property(name="defaultPort", type=IntegerType)
db_DBDriver_urlRegexPattern: Property = Property(name="urlRegexPattern", type=StringType)
db_DBDriver_driverClassName: Property = Property(name="driverClassName", type=StringType)
db_DBDriver_pooling: Property = Property(name="pooling", type=BooleanType)
db_DBDriver_m_getConnection: Method = Method(name="getConnection", parameters={Parameter(name='name')}, type=StringType)
db_DBDriver.attributes={db_DBDriver_guideUrl, db_DBDriver_websiteUrl, db_DBDriver_jars, db_DBDriver_urlRegexPattern, db_DBDriver_defaultPort, db_DBDriver_driverClassName, db_DBDriver_default, db_DBDriver_pooling, db_DBDriver_exampleUrl}
db_DBDriver.methods={db_DBDriver_m_getConnection}

# db_Query class attributes and methods
db_Query_querySql: Property = Property(name="querySql", type=StringType)
db_Query_catalog: Property = Property(name="catalog", type=StringType)
db_Query_queryType: Property = Property(name="queryType", type=StringType)
db_Query_m_getResultSet: Method = Method(name="getResultSet", parameters={Parameter(name='name')}, type=StringType)
db_Query_m_getParameter: Method = Method(name="getParameter", parameters={Parameter(name='name')}, type=StringType)
db_Query_m_getParameter: Method = Method(name="getParameter", parameters={Parameter(name='index')}, type=StringType)
db_Query.attributes={db_Query_queryType, db_Query_catalog, db_Query_querySql}
db_Query.methods={db_Query_m_getResultSet, db_Query_m_getParameter, db_Query_m_getParameter}

# db_DBConnection class attributes and methods
db_DBConnection_url: Property = Property(name="url", type=StringType)
db_DBConnection_user: Property = Property(name="user", type=StringType)
db_DBConnection_password: Property = Property(name="password", type=StringType)
db_DBConnection_loginTimeout: Property = Property(name="loginTimeout", type=IntegerType)
db_DBConnection_properties: Property = Property(name="properties", type=StringType)
db_DBConnection_transactionMode: Property = Property(name="transactionMode", type=StringType)
db_DBConnection_minPoolSize: Property = Property(name="minPoolSize", type=IntegerType)
db_DBConnection_maxPoolSize: Property = Property(name="maxPoolSize", type=IntegerType)
db_DBConnection_acquireIncrement: Property = Property(name="acquireIncrement", type=IntegerType)
db_DBConnection_maxIdleTime: Property = Property(name="maxIdleTime", type=IntegerType)
db_DBConnection_m_getQuery: Method = Method(name="getQuery", parameters={Parameter(name='name')}, type=StringType)
db_DBConnection.attributes={db_DBConnection_properties, db_DBConnection_maxIdleTime, db_DBConnection_transactionMode, db_DBConnection_acquireIncrement, db_DBConnection_url, db_DBConnection_password, db_DBConnection_minPoolSize, db_DBConnection_user, db_DBConnection_maxPoolSize, db_DBConnection_loginTimeout}
db_DBConnection.methods={db_DBConnection_m_getQuery}

# DBResource class attributes and methods

# db_SafiDriverManager class attributes and methods
db_SafiDriverManager_m_getDriver: Method = Method(name="getDriver", parameters={Parameter(name='name')}, type=StringType)
db_SafiDriverManager.methods={db_SafiDriverManager_m_getDriver}

# db_QueryParameter class attributes and methods
db_QueryParameter_dataType: Property = Property(name="dataType", type=StringType)
db_QueryParameter.attributes={db_QueryParameter_dataType}

# db_SafiResultSet class attributes and methods
db_SafiResultSet_scrollMode: Property = Property(name="scrollMode", type=StringType)
db_SafiResultSet_holdabilityMode: Property = Property(name="holdabilityMode", type=StringType)
db_SafiResultSet_useCache: Property = Property(name="useCache", type=BooleanType)
db_SafiResultSet_scrollable: Property = Property(name="scrollable", type=BooleanType)
db_SafiResultSet_readOnly: Property = Property(name="readOnly", type=BooleanType)
db_SafiResultSet.attributes={db_SafiResultSet_holdabilityMode, db_SafiResultSet_useCache, db_SafiResultSet_scrollable, db_SafiResultSet_readOnly, db_SafiResultSet_scrollMode}

# db_DBResource class attributes and methods
db_DBResource_name: Property = Property(name="name", type=StringType)
db_DBResource_lastModified: Property = Property(name="lastModified", type=DateType)
db_DBResource_lastUpdated: Property = Property(name="lastUpdated", type=DateType)
db_DBResource_id: Property = Property(name="id", type=IntegerType)
db_DBResource.attributes={db_DBResource_lastModified, db_DBResource_lastUpdated, db_DBResource_id, db_DBResource_name}

# db_config_ServerResource class attributes and methods
db_config_ServerResource_description: Property = Property(name="description", type=StringType)
db_config_ServerResource_name: Property = Property(name="name", type=StringType)
db_config_ServerResource_lastModified: Property = Property(name="lastModified", type=DateType)
db_config_ServerResource_lastUpdated: Property = Property(name="lastUpdated", type=DateType)
db_config_ServerResource_id: Property = Property(name="id", type=IntegerType)
db_config_ServerResource.attributes={db_config_ServerResource_lastUpdated, db_config_ServerResource_lastModified, db_config_ServerResource_id, db_config_ServerResource_description, db_config_ServerResource_name}

# db_Variable class attributes and methods
db_Variable_type: Property = Property(name="type", type=StringType)
db_Variable_scope: Property = Property(name="scope", type=StringType)
db_Variable_name: Property = Property(name="name", type=StringType)
db_Variable_defaultValue: Property = Property(name="defaultValue", type=StringType)
db_Variable.attributes={db_Variable_name, db_Variable_defaultValue, db_Variable_type, db_Variable_scope}

# config_User class attributes and methods

# db_config_SafiServer class attributes and methods
db_config_SafiServer_bindIP: Property = Property(name="bindIP", type=StringType)
db_config_SafiServer_managementPort: Property = Property(name="managementPort", type=IntegerType)
db_config_SafiServer_running: Property = Property(name="running", type=BooleanType)
db_config_SafiServer_debug: Property = Property(name="debug", type=BooleanType)
db_config_SafiServer_dbPort: Property = Property(name="dbPort", type=IntegerType)
db_config_SafiServer.attributes={db_config_SafiServer_bindIP, db_config_SafiServer_dbPort, db_config_SafiServer_debug, db_config_SafiServer_running, db_config_SafiServer_managementPort}

# ServerResource class attributes and methods

# db_config_Entitlement class attributes and methods

# db_config_User class attributes and methods
db_config_User_firstname: Property = Property(name="firstname", type=StringType)
db_config_User_lastname: Property = Property(name="lastname", type=StringType)
db_config_User_password: Property = Property(name="password", type=StringType)
db_config_User.attributes={db_config_User_lastname, db_config_User_firstname, db_config_User_password}

# config_Role class attributes and methods

# db_config_Saflet class attributes and methods
db_config_Saflet_code: Property = Property(name="code", type=StringType)
db_config_Saflet_subsystemId: Property = Property(name="subsystemId", type=StringType)
db_config_Saflet.attributes={db_config_Saflet_subsystemId, db_config_Saflet_code}

# db_config_Role class attributes and methods

# config_Entitlement class attributes and methods

# config_Prompt class attributes and methods

# db_config_Prompt class attributes and methods
db_config_Prompt_system: Property = Property(name="system", type=BooleanType)
db_config_Prompt_extension: Property = Property(name="extension", type=StringType)
db_config_Prompt.attributes={db_config_Prompt_extension, db_config_Prompt_system}

# config_SafletProject class attributes and methods

# db_config_SafletProject class attributes and methods
db_config_SafletProject_enabled: Property = Property(name="enabled", type=BooleanType)
db_config_SafletProject.attributes={db_config_SafletProject_enabled}

# config_Saflet class attributes and methods

# db_config_TelephonySubsystem class attributes and methods
db_config_TelephonySubsystem_hostname: Property = Property(name="hostname", type=StringType)
db_config_TelephonySubsystem_running: Property = Property(name="running", type=BooleanType)
db_config_TelephonySubsystem_private: Property = Property(name="private", type=BooleanType)
db_config_TelephonySubsystem_visibleSafiServerIP: Property = Property(name="visibleSafiServerIP", type=StringType)
db_config_TelephonySubsystem_enabled: Property = Property(name="enabled", type=BooleanType)
db_config_TelephonySubsystem_managerName: Property = Property(name="managerName", type=StringType)
db_config_TelephonySubsystem_managerPassword: Property = Property(name="managerPassword", type=StringType)
db_config_TelephonySubsystem_managerPort: Property = Property(name="managerPort", type=IntegerType)
db_config_TelephonySubsystem_versionId: Property = Property(name="versionId", type=StringType)
db_config_TelephonySubsystem_promptDirectory: Property = Property(name="promptDirectory", type=StringType)
db_config_TelephonySubsystem_platformId: Property = Property(name="platformId", type=StringType)
db_config_TelephonySubsystem.attributes={db_config_TelephonySubsystem_visibleSafiServerIP, db_config_TelephonySubsystem_managerName, db_config_TelephonySubsystem_hostname, db_config_TelephonySubsystem_private, db_config_TelephonySubsystem_platformId, db_config_TelephonySubsystem_versionId, db_config_TelephonySubsystem_promptDirectory, db_config_TelephonySubsystem_managerPassword, db_config_TelephonySubsystem_running, db_config_TelephonySubsystem_enabled, db_config_TelephonySubsystem_managerPort}

# config_SafiServer class attributes and methods

# db_config_SFTPInfo class attributes and methods
db_config_SFTPInfo_sftpUser: Property = Property(name="sftpUser", type=StringType)
db_config_SFTPInfo_sftpPassword: Property = Property(name="sftpPassword", type=StringType)
db_config_SFTPInfo_sftpPort: Property = Property(name="sftpPort", type=IntegerType)
db_config_SFTPInfo.attributes={db_config_SFTPInfo_sftpPassword, db_config_SFTPInfo_sftpUser, db_config_SFTPInfo_sftpPort}

# Relationships
driver0: BinaryAssociation = BinaryAssociation(
    name="driver0",
    ends={
        Property(name="DBDriver", type=db_DBConnection, multiplicity=Multiplicity(1, 1)),
        Property(name="connections", type=db_DBDriver, multiplicity=Multiplicity(0, 1))
    }
)
queries1: BinaryAssociation = BinaryAssociation(
    name="queries1",
    ends={
        Property(name="Query", type=db_DBConnection, multiplicity=Multiplicity(1, 1)),
        Property(name="connection", type=db_Query, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
connections2: BinaryAssociation = BinaryAssociation(
    name="connections2",
    ends={
        Property(name="DBConnection", type=db_DBDriver, multiplicity=Multiplicity(1, 1)),
        Property(name="driver", type=db_DBConnection, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
driverManager3: BinaryAssociation = BinaryAssociation(
    name="driverManager3",
    ends={
        Property(name="SafiDriverManager", type=db_DBDriver, multiplicity=Multiplicity(1, 1)),
        Property(name="drivers", type=db_SafiDriverManager, multiplicity=Multiplicity(0, 1))
    }
)
parameters4: BinaryAssociation = BinaryAssociation(
    name="parameters4",
    ends={
        Property(name="QueryParameter", type=db_Query, multiplicity=Multiplicity(1, 1)),
        Property(name="query", type=db_QueryParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
connection5: BinaryAssociation = BinaryAssociation(
    name="connection5",
    ends={
        Property(name="DBConnection6", type=db_Query, multiplicity=Multiplicity(1, 1)),
        Property(name="queries", type=db_DBConnection, multiplicity=Multiplicity(0, 1))
    }
)
resultSets7: BinaryAssociation = BinaryAssociation(
    name="resultSets7",
    ends={
        Property(name="SafiResultSet", type=db_Query, multiplicity=Multiplicity(1, 1)),
        Property(name="query8", type=db_SafiResultSet, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
query9: BinaryAssociation = BinaryAssociation(
    name="query9",
    ends={
        Property(name="Query10", type=db_QueryParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="parameters", type=db_Query, multiplicity=Multiplicity(0, 1))
    }
)
query13: BinaryAssociation = BinaryAssociation(
    name="query13",
    ends={
        Property(name="Query14", type=db_SafiResultSet, multiplicity=Multiplicity(1, 1)),
        Property(name="resultSets", type=db_Query, multiplicity=Multiplicity(0, 1))
    }
)
drivers11: BinaryAssociation = BinaryAssociation(
    name="drivers11",
    ends={
        Property(name="DBDriver12", type=db_SafiDriverManager, multiplicity=Multiplicity(1, 1)),
        Property(name="driverManager", type=db_DBDriver, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
createdBy15: BinaryAssociation = BinaryAssociation(
    name="createdBy15",
    ends={
        Property(name="config_User", type=db_config_ServerResource, multiplicity=Multiplicity(1, 1)),
        Property(name="db_config_ServerResource", type=config_User, multiplicity=Multiplicity(0, 1))
    }
)
modifiedBy16: BinaryAssociation = BinaryAssociation(
    name="modifiedBy16",
    ends={
        Property(name="config_User18", type=db_config_ServerResource, multiplicity=Multiplicity(1, 1)),
        Property(name="db_config_ServerResource17", type=config_User, multiplicity=Multiplicity(0, 1))
    }
)
user19: BinaryAssociation = BinaryAssociation(
    name="user19",
    ends={
        Property(name="config_User20", type=db_config_SafiServer, multiplicity=Multiplicity(1, 1)),
        Property(name="db_config_SafiServer", type=config_User, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
users21: BinaryAssociation = BinaryAssociation(
    name="users21",
    ends={
        Property(name="config_User23", type=db_config_SafiServer, multiplicity=Multiplicity(1, 1)),
        Property(name="db_config_SafiServer22", type=config_User, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
entitlements24: BinaryAssociation = BinaryAssociation(
    name="entitlements24",
    ends={
        Property(name="config_Entitlement", type=db_config_Role, multiplicity=Multiplicity(1, 1)),
        Property(name="db_config_Role", type=config_Entitlement, multiplicity=Multiplicity(0, 9999))
    }
)
roles25: BinaryAssociation = BinaryAssociation(
    name="roles25",
    ends={
        Property(name="config_Role", type=db_config_User, multiplicity=Multiplicity(1, 1)),
        Property(name="db_config_User", type=config_Role, multiplicity=Multiplicity(0, 9999))
    }
)
saflets27: BinaryAssociation = BinaryAssociation(
    name="saflets27",
    ends={
        Property(name="config28", type=config_Saflet, multiplicity=Multiplicity(0, 9999), is_composite=True),
        Property(name="server29", type=db_config_SafletProject, multiplicity=Multiplicity(1, 1))
    }
)
prompts30: BinaryAssociation = BinaryAssociation(
    name="prompts30",
    ends={
        Property(name="server32", type=db_config_SafletProject, multiplicity=Multiplicity(1, 1)),
        Property(name="config31", type=config_Prompt, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
project33: BinaryAssociation = BinaryAssociation(
    name="project33",
    ends={
        Property(name="server35", type=db_config_Prompt, multiplicity=Multiplicity(1, 1)),
        Property(name="config34", type=config_SafletProject, multiplicity=Multiplicity(0, 1))
    }
)
project26: BinaryAssociation = BinaryAssociation(
    name="project26",
    ends={
        Property(name="server", type=db_config_Saflet, multiplicity=Multiplicity(1, 1)),
        Property(name="config", type=config_SafletProject, multiplicity=Multiplicity(0, 1))
    }
)
safiServer36: BinaryAssociation = BinaryAssociation(
    name="safiServer36",
    ends={
        Property(name="config_SafiServer", type=db_config_TelephonySubsystem, multiplicity=Multiplicity(1, 1)),
        Property(name="db_config_TelephonySubsystem", type=config_SafiServer, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_db_DBConnection_DBResource = Generalization(general=DBResource, specific=db_DBConnection)
gen_db_DBDriver_DBResource = Generalization(general=DBResource, specific=db_DBDriver)
gen_db_QueryParameter_DBResource = Generalization(general=DBResource, specific=db_QueryParameter)
gen_db_Query_DBResource = Generalization(general=DBResource, specific=db_Query)
gen_db_SafiDriverManager_DBResource = Generalization(general=DBResource, specific=db_SafiDriverManager)
gen_db_SafiResultSet_DBResource = Generalization(general=DBResource, specific=db_SafiResultSet)
gen_db_config_SafiServer_ServerResource = Generalization(general=ServerResource, specific=db_config_SafiServer)
gen_db_config_Entitlement_ServerResource = Generalization(general=ServerResource, specific=db_config_Entitlement)
gen_db_config_User_ServerResource = Generalization(general=ServerResource, specific=db_config_User)
gen_db_config_Saflet_ServerResource = Generalization(general=ServerResource, specific=db_config_Saflet)
gen_db_config_Role_ServerResource = Generalization(general=ServerResource, specific=db_config_Role)
gen_db_config_Prompt_ServerResource = Generalization(general=ServerResource, specific=db_config_Prompt)
gen_db_config_SafletProject_ServerResource = Generalization(general=ServerResource, specific=db_config_SafletProject)
gen_db_config_TelephonySubsystem_ServerResource = Generalization(general=ServerResource, specific=db_config_TelephonySubsystem)

# Domain Model
domain_model = DomainModel(
    name="db",
    types={db_DBDriver, db_Query, db_DBConnection, DBResource, db_SafiDriverManager, db_QueryParameter, db_SafiResultSet, db_DBResource, db_config_ServerResource, db_Variable, config_User, db_config_SafiServer, ServerResource, db_config_Entitlement, db_config_User, config_Role, db_config_Saflet, db_config_Role, config_Entitlement, config_Prompt, db_config_Prompt, config_SafletProject, db_config_SafletProject, config_Saflet, db_config_TelephonySubsystem, config_SafiServer, db_config_SFTPInfo, SQLDataType, QueryType, RSHoldabilityMode, RSScrollMode, TransactionMode, VariableScope, VariableType, SynchMode},
    associations={driver0, queries1, connections2, driverManager3, parameters4, connection5, resultSets7, query9, query13, drivers11, createdBy15, modifiedBy16, user19, users21, entitlements24, roles25, saflets27, prompts30, project33, project26, safiServer36},
    generalizations={gen_db_DBConnection_DBResource, gen_db_DBDriver_DBResource, gen_db_QueryParameter_DBResource, gen_db_Query_DBResource, gen_db_SafiDriverManager_DBResource, gen_db_SafiResultSet_DBResource, gen_db_config_SafiServer_ServerResource, gen_db_config_Entitlement_ServerResource, gen_db_config_User_ServerResource, gen_db_config_Saflet_ServerResource, gen_db_config_Role_ServerResource, gen_db_config_Prompt_ServerResource, gen_db_config_SafletProject_ServerResource, gen_db_config_TelephonySubsystem_ServerResource},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)