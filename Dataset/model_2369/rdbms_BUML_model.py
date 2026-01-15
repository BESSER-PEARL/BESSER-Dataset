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

# Classes
rdbms_column = Class(name="rdbms::column")
rdbms_referencedKeys = Class(name="rdbms::referencedKeys")
rdbms_hasForeignKeys = Class(name="rdbms::hasForeignKeys")
rdbms_DocumentRoot = Class(name="rdbms::DocumentRoot")
rdbms_EStringToStringMapEntry = Class(name="rdbms::EStringToStringMapEntry")
rdbms_columns = Class(name="rdbms::columns")
rdbms_foreignKey = Class(name="rdbms::foreignKey")
rdbms_foreignKeys = Class(name="rdbms::foreignKeys")
rdbms_key = Class(name="rdbms::key")
rdbms_key2 = Class(name="rdbms::key2")
rdbms_oID = Class(name="rdbms::oID")
rdbms_RDBMS = Class(name="rdbms::RDBMS")
rdbms_schema = Class(name="rdbms::schema")
rdbms_schemas = Class(name="rdbms::schemas")
rdbms_table = Class(name="rdbms::table")
rdbms_referencedColumns = Class(name="rdbms::referencedColumns")
rdbms_tables = Class(name="rdbms::tables")

# rdbms_column class attributes and methods
rdbms_column_kind: Property = Property(name="kind", type=StringType)
rdbms_column_name: Property = Property(name="name", type=StringType)
rdbms_column_oID: Property = Property(name="oID", type=StringType)
rdbms_column_type: Property = Property(name="type", type=StringType)
rdbms_column.attributes={rdbms_column_type, rdbms_column_name, rdbms_column_kind, rdbms_column_oID}

# rdbms_referencedKeys class attributes and methods
rdbms_referencedKeys_group: Property = Property(name="group", type=StringType)
rdbms_referencedKeys.attributes={rdbms_referencedKeys_group}

# rdbms_hasForeignKeys class attributes and methods
rdbms_hasForeignKeys_group: Property = Property(name="group", type=StringType)
rdbms_hasForeignKeys.attributes={rdbms_hasForeignKeys_group}

# rdbms_DocumentRoot class attributes and methods
rdbms_DocumentRoot_mixed: Property = Property(name="mixed", type=StringType)
rdbms_DocumentRoot.attributes={rdbms_DocumentRoot_mixed}

# rdbms_EStringToStringMapEntry class attributes and methods

# rdbms_columns class attributes and methods
rdbms_columns_group: Property = Property(name="group", type=StringType)
rdbms_columns.attributes={rdbms_columns_group}

# rdbms_foreignKey class attributes and methods
rdbms_foreignKey_kind: Property = Property(name="kind", type=StringType)
rdbms_foreignKey_name: Property = Property(name="name", type=StringType)
rdbms_foreignKey_oID: Property = Property(name="oID", type=StringType)
rdbms_foreignKey_owner: Property = Property(name="owner", type=StringType)
rdbms_foreignKey_refersTo: Property = Property(name="refersTo", type=StringType)
rdbms_foreignKey.attributes={rdbms_foreignKey_owner, rdbms_foreignKey_kind, rdbms_foreignKey_name, rdbms_foreignKey_refersTo, rdbms_foreignKey_oID}

# rdbms_foreignKeys class attributes and methods
rdbms_foreignKeys_group: Property = Property(name="group", type=StringType)
rdbms_foreignKeys.attributes={rdbms_foreignKeys_group}

# rdbms_key class attributes and methods
rdbms_key_kind: Property = Property(name="kind", type=StringType)
rdbms_key_name: Property = Property(name="name", type=StringType)
rdbms_key_oID: Property = Property(name="oID", type=StringType)
rdbms_key.attributes={rdbms_key_oID, rdbms_key_name, rdbms_key_kind}

# rdbms_key2 class attributes and methods

# rdbms_oID class attributes and methods
rdbms_oID_oID: Property = Property(name="oID", type=StringType)
rdbms_oID.attributes={rdbms_oID_oID}

# rdbms_RDBMS class attributes and methods

# rdbms_schema class attributes and methods
rdbms_schema_kind: Property = Property(name="kind", type=StringType)
rdbms_schema_name: Property = Property(name="name", type=StringType)
rdbms_schema_oID: Property = Property(name="oID", type=StringType)
rdbms_schema.attributes={rdbms_schema_oID, rdbms_schema_kind, rdbms_schema_name}

# rdbms_schemas class attributes and methods
rdbms_schemas_group: Property = Property(name="group", type=StringType)
rdbms_schemas.attributes={rdbms_schemas_group}

# rdbms_table class attributes and methods
rdbms_table_kind: Property = Property(name="kind", type=StringType)
rdbms_table_name: Property = Property(name="name", type=StringType)
rdbms_table_oID: Property = Property(name="oID", type=StringType)
rdbms_table.attributes={rdbms_table_kind, rdbms_table_oID, rdbms_table_name}

# rdbms_referencedColumns class attributes and methods
rdbms_referencedColumns_group: Property = Property(name="group", type=StringType)
rdbms_referencedColumns.attributes={rdbms_referencedColumns_group}

# rdbms_tables class attributes and methods
rdbms_tables_group: Property = Property(name="group", type=StringType)
rdbms_tables.attributes={rdbms_tables_group}

# Relationships
hasForeignKeys1: BinaryAssociation = BinaryAssociation(
    name="hasForeignKeys1",
    ends={
        Property(name="rdbms_hasForeignKeys", type=rdbms_column, multiplicity=Multiplicity(1, 1)),
        Property(name="rdbms_column2", type=rdbms_hasForeignKeys, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
referencedKeys0: BinaryAssociation = BinaryAssociation(
    name="referencedKeys0",
    ends={
        Property(name="rdbms_referencedKeys", type=rdbms_column, multiplicity=Multiplicity(1, 1)),
        Property(name="rdbms_column", type=rdbms_referencedKeys, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
column3: BinaryAssociation = BinaryAssociation(
    name="column3",
    ends={
        Property(name="rdbms_column4", type=rdbms_columns, multiplicity=Multiplicity(1, 1)),
        Property(name="rdbms_columns", type=rdbms_column, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
xMLNSPrefixMap5: BinaryAssociation = BinaryAssociation(
    name="xMLNSPrefixMap5",
    ends={
        Property(name="rdbms_EStringToStringMapEntry", type=rdbms_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="rdbms_DocumentRoot", type=rdbms_EStringToStringMapEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
column9: BinaryAssociation = BinaryAssociation(
    name="column9",
    ends={
        Property(name="rdbms_column11", type=rdbms_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="rdbms_DocumentRoot10", type=rdbms_column, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
columns12: BinaryAssociation = BinaryAssociation(
    name="columns12",
    ends={
        Property(name="rdbms_columns14", type=rdbms_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="rdbms_DocumentRoot13", type=rdbms_columns, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
foreignKey15: BinaryAssociation = BinaryAssociation(
    name="foreignKey15",
    ends={
        Property(name="rdbms_foreignKey", type=rdbms_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="rdbms_DocumentRoot16", type=rdbms_foreignKey, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
foreignKeys17: BinaryAssociation = BinaryAssociation(
    name="foreignKeys17",
    ends={
        Property(name="rdbms_foreignKeys", type=rdbms_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="rdbms_DocumentRoot18", type=rdbms_foreignKeys, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
xSISchemaLocation6: BinaryAssociation = BinaryAssociation(
    name="xSISchemaLocation6",
    ends={
        Property(name="rdbms_EStringToStringMapEntry8", type=rdbms_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="rdbms_DocumentRoot7", type=rdbms_EStringToStringMapEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
key22: BinaryAssociation = BinaryAssociation(
    name="key22",
    ends={
        Property(name="rdbms_key", type=rdbms_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="rdbms_DocumentRoot23", type=rdbms_key, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
key224: BinaryAssociation = BinaryAssociation(
    name="key224",
    ends={
        Property(name="rdbms_key2", type=rdbms_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="rdbms_DocumentRoot25", type=rdbms_key2, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
oID26: BinaryAssociation = BinaryAssociation(
    name="oID26",
    ends={
        Property(name="rdbms_oID", type=rdbms_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="rdbms_DocumentRoot27", type=rdbms_oID, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
rDBMS28: BinaryAssociation = BinaryAssociation(
    name="rDBMS28",
    ends={
        Property(name="rdbms_RDBMS", type=rdbms_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="rdbms_DocumentRoot29", type=rdbms_RDBMS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
hasForeignKeys19: BinaryAssociation = BinaryAssociation(
    name="hasForeignKeys19",
    ends={
        Property(name="rdbms_hasForeignKeys21", type=rdbms_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="rdbms_DocumentRoot20", type=rdbms_hasForeignKeys, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
referencedKeys32: BinaryAssociation = BinaryAssociation(
    name="referencedKeys32",
    ends={
        Property(name="rdbms_referencedKeys34", type=rdbms_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="rdbms_DocumentRoot33", type=rdbms_referencedKeys, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
schema35: BinaryAssociation = BinaryAssociation(
    name="schema35",
    ends={
        Property(name="rdbms_schema", type=rdbms_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="rdbms_DocumentRoot36", type=rdbms_schema, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
schemas37: BinaryAssociation = BinaryAssociation(
    name="schemas37",
    ends={
        Property(name="rdbms_schemas", type=rdbms_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="rdbms_DocumentRoot38", type=rdbms_schemas, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
table39: BinaryAssociation = BinaryAssociation(
    name="table39",
    ends={
        Property(name="rdbms_table", type=rdbms_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="rdbms_DocumentRoot40", type=rdbms_table, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
referencedColumns30: BinaryAssociation = BinaryAssociation(
    name="referencedColumns30",
    ends={
        Property(name="rdbms_referencedColumns", type=rdbms_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="rdbms_DocumentRoot31", type=rdbms_referencedColumns, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
referencedColumns43: BinaryAssociation = BinaryAssociation(
    name="referencedColumns43",
    ends={
        Property(name="rdbms_referencedColumns45", type=rdbms_foreignKey, multiplicity=Multiplicity(1, 1)),
        Property(name="rdbms_foreignKey44", type=rdbms_referencedColumns, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
tables41: BinaryAssociation = BinaryAssociation(
    name="tables41",
    ends={
        Property(name="rdbms_tables", type=rdbms_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="rdbms_DocumentRoot42", type=rdbms_tables, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
foreignKey46: BinaryAssociation = BinaryAssociation(
    name="foreignKey46",
    ends={
        Property(name="rdbms_foreignKey48", type=rdbms_foreignKeys, multiplicity=Multiplicity(1, 1)),
        Property(name="rdbms_foreignKeys47", type=rdbms_foreignKey, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
oID49: BinaryAssociation = BinaryAssociation(
    name="oID49",
    ends={
        Property(name="rdbms_oID51", type=rdbms_hasForeignKeys, multiplicity=Multiplicity(1, 1)),
        Property(name="rdbms_hasForeignKeys50", type=rdbms_oID, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
key55: BinaryAssociation = BinaryAssociation(
    name="key55",
    ends={
        Property(name="rdbms_key57", type=rdbms_key2, multiplicity=Multiplicity(1, 1)),
        Property(name="rdbms_key256", type=rdbms_key, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
referencedColumns52: BinaryAssociation = BinaryAssociation(
    name="referencedColumns52",
    ends={
        Property(name="rdbms_referencedColumns54", type=rdbms_key, multiplicity=Multiplicity(1, 1)),
        Property(name="rdbms_key53", type=rdbms_referencedColumns, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
oID61: BinaryAssociation = BinaryAssociation(
    name="oID61",
    ends={
        Property(name="rdbms_oID63", type=rdbms_referencedColumns, multiplicity=Multiplicity(1, 1)),
        Property(name="rdbms_referencedColumns62", type=rdbms_oID, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
oID64: BinaryAssociation = BinaryAssociation(
    name="oID64",
    ends={
        Property(name="rdbms_oID66", type=rdbms_referencedKeys, multiplicity=Multiplicity(1, 1)),
        Property(name="rdbms_referencedKeys65", type=rdbms_oID, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
schemas58: BinaryAssociation = BinaryAssociation(
    name="schemas58",
    ends={
        Property(name="rdbms_schemas60", type=rdbms_RDBMS, multiplicity=Multiplicity(1, 1)),
        Property(name="rdbms_RDBMS59", type=rdbms_schemas, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
foreignKeys70: BinaryAssociation = BinaryAssociation(
    name="foreignKeys70",
    ends={
        Property(name="rdbms_foreignKeys72", type=rdbms_schema, multiplicity=Multiplicity(1, 1)),
        Property(name="rdbms_schema71", type=rdbms_foreignKeys, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
tables67: BinaryAssociation = BinaryAssociation(
    name="tables67",
    ends={
        Property(name="rdbms_tables69", type=rdbms_schema, multiplicity=Multiplicity(1, 1)),
        Property(name="rdbms_schema68", type=rdbms_tables, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
columns76: BinaryAssociation = BinaryAssociation(
    name="columns76",
    ends={
        Property(name="rdbms_columns78", type=rdbms_table, multiplicity=Multiplicity(1, 1)),
        Property(name="rdbms_table77", type=rdbms_columns, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
key279: BinaryAssociation = BinaryAssociation(
    name="key279",
    ends={
        Property(name="rdbms_key281", type=rdbms_table, multiplicity=Multiplicity(1, 1)),
        Property(name="rdbms_table80", type=rdbms_key2, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
schema73: BinaryAssociation = BinaryAssociation(
    name="schema73",
    ends={
        Property(name="rdbms_schema75", type=rdbms_schemas, multiplicity=Multiplicity(1, 1)),
        Property(name="rdbms_schemas74", type=rdbms_schema, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
table82: BinaryAssociation = BinaryAssociation(
    name="table82",
    ends={
        Property(name="rdbms_table84", type=rdbms_tables, multiplicity=Multiplicity(1, 1)),
        Property(name="rdbms_tables83", type=rdbms_table, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="rdbms",
    types={rdbms_column, rdbms_referencedKeys, rdbms_hasForeignKeys, rdbms_DocumentRoot, rdbms_EStringToStringMapEntry, rdbms_columns, rdbms_foreignKey, rdbms_foreignKeys, rdbms_key, rdbms_key2, rdbms_oID, rdbms_RDBMS, rdbms_schema, rdbms_schemas, rdbms_table, rdbms_referencedColumns, rdbms_tables},
    associations={hasForeignKeys1, referencedKeys0, column3, xMLNSPrefixMap5, column9, columns12, foreignKey15, foreignKeys17, xSISchemaLocation6, key22, key224, oID26, rDBMS28, hasForeignKeys19, referencedKeys32, schema35, schemas37, table39, referencedColumns30, referencedColumns43, tables41, foreignKey46, oID49, key55, referencedColumns52, oID61, oID64, schemas58, foreignKeys70, tables67, columns76, key279, schema73, table82},
    generalizations={},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)