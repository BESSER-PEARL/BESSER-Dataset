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
DBMS: Enumeration = Enumeration(
    name="DBMS",
    literals={
            EnumerationLiteral(name="MySQL"),
			EnumerationLiteral(name="PgSQL"),
			EnumerationLiteral(name="HSQLDB"),
			EnumerationLiteral(name="SQLite"),
			EnumerationLiteral(name="MSAccess")
    }
)

ParameterType: Enumeration = Enumeration(
    name="ParameterType",
    literals={
            EnumerationLiteral(name="AsciiStream"),
			EnumerationLiteral(name="Array"),
			EnumerationLiteral(name="BigDecimal"),
			EnumerationLiteral(name="BinaryStream"),
			EnumerationLiteral(name="Blob"),
			EnumerationLiteral(name="Boolean"),
			EnumerationLiteral(name="Byte"),
			EnumerationLiteral(name="Bytes"),
			EnumerationLiteral(name="CharacterStream"),
			EnumerationLiteral(name="Clob"),
			EnumerationLiteral(name="Date"),
			EnumerationLiteral(name="DateCalendar"),
			EnumerationLiteral(name="Double"),
			EnumerationLiteral(name="Float"),
			EnumerationLiteral(name="Int"),
			EnumerationLiteral(name="Long"),
			EnumerationLiteral(name="Object"),
			EnumerationLiteral(name="Ref"),
			EnumerationLiteral(name="Short"),
			EnumerationLiteral(name="String"),
			EnumerationLiteral(name="Token"),
			EnumerationLiteral(name="Time"),
			EnumerationLiteral(name="TimeCalendar"),
			EnumerationLiteral(name="Timestamp"),
			EnumerationLiteral(name="TimeStampCalendar"),
			EnumerationLiteral(name="UnicodeStream"),
			EnumerationLiteral(name="URL")
    }
)

# Classes
properties_DatabaseAlias = Class(name="properties_DatabaseAlias")
properties_DatabaseProperties = Class(name="properties_DatabaseProperties")
properties_SqlProperties = Class(name="properties_SqlProperties")
properties_Property = Class(name="properties_Property")
properties_DatabasePropertiesListType = Class(name="properties_DatabasePropertiesListType")
properties_DocumentRoot = Class(name="properties_DocumentRoot")
properties_EStringToStringMapEntry = Class(name="properties_EStringToStringMapEntry")
properties_SpecificDBMSProperties = Class(name="properties_SpecificDBMSProperties")
properties_SqlQuery = Class(name="properties_SqlQuery")
properties_SqlFile = Class(name="properties_SqlFile")
properties_Sql = Class(name="properties_Sql")
properties_SqlParameter = Class(name="properties_SqlParameter")
Sql = Class(name="Sql")
properties_SqlGroup = Class(name="properties_SqlGroup")

# properties_DatabaseAlias class attributes and methods
properties_DatabaseAlias_alias: Property = Property(name="alias", type=StringType)
properties_DatabaseAlias_id: Property = Property(name="id", type=StringType)
properties_DatabaseAlias.attributes={properties_DatabaseAlias_alias, properties_DatabaseAlias_id}

# properties_DatabaseProperties class attributes and methods
properties_DatabaseProperties_id: Property = Property(name="id", type=StringType)
properties_DatabaseProperties_driverClassName: Property = Property(name="driverClassName", type=StringType)
properties_DatabaseProperties_dialect: Property = Property(name="dialect", type=StringType)
properties_DatabaseProperties_serverURL: Property = Property(name="serverURL", type=StringType)
properties_DatabaseProperties_dBMS: Property = Property(name="dBMS", type=StringType)
properties_DatabaseProperties_port: Property = Property(name="port", type=StringType)
properties_DatabaseProperties_databaseName: Property = Property(name="databaseName", type=StringType)
properties_DatabaseProperties_username: Property = Property(name="username", type=StringType)
properties_DatabaseProperties_password: Property = Property(name="password", type=StringType)
properties_DatabaseProperties_namespace: Property = Property(name="namespace", type=StringType)
properties_DatabaseProperties_persistenceUnitName: Property = Property(name="persistenceUnitName", type=StringType)
properties_DatabaseProperties.attributes={properties_DatabaseProperties_databaseName, properties_DatabaseProperties_namespace, properties_DatabaseProperties_serverURL, properties_DatabaseProperties_id, properties_DatabaseProperties_driverClassName, properties_DatabaseProperties_persistenceUnitName, properties_DatabaseProperties_password, properties_DatabaseProperties_port, properties_DatabaseProperties_dBMS, properties_DatabaseProperties_dialect, properties_DatabaseProperties_username}

# properties_SqlProperties class attributes and methods

# properties_Property class attributes and methods
properties_Property_key: Property = Property(name="key", type=StringType)
properties_Property_value: Property = Property(name="value", type=StringType)
properties_Property.attributes={properties_Property_value, properties_Property_key}

# properties_DatabasePropertiesListType class attributes and methods

# properties_DocumentRoot class attributes and methods
properties_DocumentRoot_mixed: Property = Property(name="mixed", type=StringType)
properties_DocumentRoot.attributes={properties_DocumentRoot_mixed}

# properties_EStringToStringMapEntry class attributes and methods

# properties_SpecificDBMSProperties class attributes and methods
properties_SpecificDBMSProperties_dBMS: Property = Property(name="dBMS", type=StringType)
properties_SpecificDBMSProperties.attributes={properties_SpecificDBMSProperties_dBMS}

# properties_SqlQuery class attributes and methods
properties_SqlQuery_queryString: Property = Property(name="queryString", type=StringType)
properties_SqlQuery.attributes={properties_SqlQuery_queryString}

# properties_SqlFile class attributes and methods
properties_SqlFile_filePath: Property = Property(name="filePath", type=StringType)
properties_SqlFile.attributes={properties_SqlFile_filePath}

# properties_Sql class attributes and methods
properties_Sql_id: Property = Property(name="id", type=StringType)
properties_Sql_hqlQuery: Property = Property(name="hqlQuery", type=StringType)
properties_Sql.attributes={properties_Sql_id, properties_Sql_hqlQuery}

# properties_SqlParameter class attributes and methods
properties_SqlParameter_index: Property = Property(name="index", type=StringType)
properties_SqlParameter_name: Property = Property(name="name", type=StringType)
properties_SqlParameter_type: Property = Property(name="type", type=StringType)
properties_SqlParameter.attributes={properties_SqlParameter_type, properties_SqlParameter_name, properties_SqlParameter_index}

# Sql class attributes and methods

# properties_SqlGroup class attributes and methods
properties_SqlGroup_id: Property = Property(name="id", type=StringType)
properties_SqlGroup_description: Property = Property(name="description", type=StringType)
properties_SqlGroup.attributes={properties_SqlGroup_description, properties_SqlGroup_id}

# Relationships
sqlProperties0: BinaryAssociation = BinaryAssociation(
    name="sqlProperties0",
    ends={
        Property(name="properties_SqlProperties", type=properties_DatabaseProperties, multiplicity=Multiplicity(1, 1)),
        Property(name="properties_DatabaseProperties", type=properties_SqlProperties, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
additionalProperties1: BinaryAssociation = BinaryAssociation(
    name="additionalProperties1",
    ends={
        Property(name="properties_Property", type=properties_DatabaseProperties, multiplicity=Multiplicity(1, 1)),
        Property(name="properties_DatabaseProperties2", type=properties_Property, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
databaseProperties3: BinaryAssociation = BinaryAssociation(
    name="databaseProperties3",
    ends={
        Property(name="properties_DatabaseProperties4", type=properties_DatabasePropertiesListType, multiplicity=Multiplicity(1, 1)),
        Property(name="properties_DatabasePropertiesListType", type=properties_DatabaseProperties, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
databaseAlias5: BinaryAssociation = BinaryAssociation(
    name="databaseAlias5",
    ends={
        Property(name="properties_DatabaseAlias", type=properties_DatabasePropertiesListType, multiplicity=Multiplicity(1, 1)),
        Property(name="properties_DatabasePropertiesListType6", type=properties_DatabaseAlias, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
xMLNSPrefixMap7: BinaryAssociation = BinaryAssociation(
    name="xMLNSPrefixMap7",
    ends={
        Property(name="properties_EStringToStringMapEntry", type=properties_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="properties_DocumentRoot", type=properties_EStringToStringMapEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
xSISchemaLocation8: BinaryAssociation = BinaryAssociation(
    name="xSISchemaLocation8",
    ends={
        Property(name="properties_EStringToStringMapEntry10", type=properties_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="properties_DocumentRoot9", type=properties_EStringToStringMapEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
databasePropertiesList11: BinaryAssociation = BinaryAssociation(
    name="databasePropertiesList11",
    ends={
        Property(name="properties_DatabasePropertiesListType13", type=properties_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="properties_DocumentRoot12", type=properties_DatabasePropertiesListType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
sqlProperties14: BinaryAssociation = BinaryAssociation(
    name="sqlProperties14",
    ends={
        Property(name="properties_SqlProperties16", type=properties_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="properties_DocumentRoot15", type=properties_SqlProperties, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
sqlQuery17: BinaryAssociation = BinaryAssociation(
    name="sqlQuery17",
    ends={
        Property(name="properties_SqlQuery", type=properties_SpecificDBMSProperties, multiplicity=Multiplicity(1, 1)),
        Property(name="properties_SpecificDBMSProperties", type=properties_SqlQuery, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
sqlFile18: BinaryAssociation = BinaryAssociation(
    name="sqlFile18",
    ends={
        Property(name="properties_SqlFile", type=properties_SpecificDBMSProperties, multiplicity=Multiplicity(1, 1)),
        Property(name="properties_SpecificDBMSProperties19", type=properties_SqlFile, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parameters20: BinaryAssociation = BinaryAssociation(
    name="parameters20",
    ends={
        Property(name="properties_SqlParameter", type=properties_Sql, multiplicity=Multiplicity(1, 1)),
        Property(name="properties_Sql", type=properties_SqlParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
sqlQuery21: BinaryAssociation = BinaryAssociation(
    name="sqlQuery21",
    ends={
        Property(name="properties_SqlQuery22", type=properties_SqlGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="properties_SqlGroup", type=properties_SqlQuery, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
sqlFile23: BinaryAssociation = BinaryAssociation(
    name="sqlFile23",
    ends={
        Property(name="properties_SqlFile25", type=properties_SqlGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="properties_SqlGroup24", type=properties_SqlFile, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
specificDBMSProperties26: BinaryAssociation = BinaryAssociation(
    name="specificDBMSProperties26",
    ends={
        Property(name="properties_SpecificDBMSProperties28", type=properties_SqlGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="properties_SqlGroup27", type=properties_SpecificDBMSProperties, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
sqlGroup29: BinaryAssociation = BinaryAssociation(
    name="sqlGroup29",
    ends={
        Property(name="properties_SqlGroup31", type=properties_SqlProperties, multiplicity=Multiplicity(1, 1)),
        Property(name="properties_SqlProperties30", type=properties_SqlGroup, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)

# Generalizations
gen_properties_SqlFile_Sql = Generalization(general=Sql, specific=properties_SqlFile)
gen_properties_SqlQuery_Sql = Generalization(general=Sql, specific=properties_SqlQuery)

# Domain Model
domain_model = DomainModel(
    name="properties",
    types={properties_DatabaseAlias, properties_DatabaseProperties, properties_SqlProperties, properties_Property, properties_DatabasePropertiesListType, properties_DocumentRoot, properties_EStringToStringMapEntry, properties_SpecificDBMSProperties, properties_SqlQuery, properties_SqlFile, properties_Sql, properties_SqlParameter, Sql, properties_SqlGroup, DBMS, ParameterType},
    associations={sqlProperties0, additionalProperties1, databaseProperties3, databaseAlias5, xMLNSPrefixMap7, xSISchemaLocation8, databasePropertiesList11, sqlProperties14, sqlQuery17, sqlFile18, parameters20, sqlQuery21, sqlFile23, specificDBMSProperties26, sqlGroup29},
    generalizations={gen_properties_SqlFile_Sql, gen_properties_SqlQuery_Sql},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)