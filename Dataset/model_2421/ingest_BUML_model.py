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
ingest_Database = Class(name="ingest::Database")
ingest_DbSchema = Class(name="ingest::DbSchema")
ingest_DbTable = Class(name="ingest::DbTable")
ingest_SqoopHiveImport = Class(name="ingest::SqoopHiveImport")
SqoopImport = Class(name="SqoopImport")
ingest_SqoopHiveIncrementalImport = Class(name="ingest::SqoopHiveIncrementalImport")
SqoopHiveImport = Class(name="SqoopHiveImport")
ingest_DbColumn = Class(name="ingest::DbColumn")
ingest_SqoopImport = Class(name="ingest::SqoopImport")
ingest_Catalogue = Class(name="ingest::Catalogue")

# ingest_Database class attributes and methods
ingest_Database_label: Property = Property(name="label", type=StringType)
ingest_Database_jdbcUrl: Property = Property(name="jdbcUrl", type=StringType)
ingest_Database_jdbcUser: Property = Property(name="jdbcUser", type=StringType)
ingest_Database_jdbcPassword: Property = Property(name="jdbcPassword", type=StringType)
ingest_Database_jdbcDriver: Property = Property(name="jdbcDriver", type=StringType)
ingest_Database.attributes={ingest_Database_jdbcPassword, ingest_Database_label, ingest_Database_jdbcUser, ingest_Database_jdbcDriver, ingest_Database_jdbcUrl}

# ingest_DbSchema class attributes and methods
ingest_DbSchema_name: Property = Property(name="name", type=StringType)
ingest_DbSchema.attributes={ingest_DbSchema_name}

# ingest_DbTable class attributes and methods
ingest_DbTable_name: Property = Property(name="name", type=StringType)
ingest_DbTable.attributes={ingest_DbTable_name}

# ingest_SqoopHiveImport class attributes and methods
ingest_SqoopHiveImport_targetHiveDatabase: Property = Property(name="targetHiveDatabase", type=StringType)
ingest_SqoopHiveImport_targetHiveTable: Property = Property(name="targetHiveTable", type=StringType)
ingest_SqoopHiveImport.attributes={ingest_SqoopHiveImport_targetHiveDatabase, ingest_SqoopHiveImport_targetHiveTable}

# SqoopImport class attributes and methods

# ingest_SqoopHiveIncrementalImport class attributes and methods

# SqoopHiveImport class attributes and methods

# ingest_DbColumn class attributes and methods
ingest_DbColumn_name: Property = Property(name="name", type=StringType)
ingest_DbColumn_jdbcType: Property = Property(name="jdbcType", type=IntegerType)
ingest_DbColumn_jdbcScale: Property = Property(name="jdbcScale", type=IntegerType)
ingest_DbColumn_jdbcPrecision: Property = Property(name="jdbcPrecision", type=IntegerType)
ingest_DbColumn.attributes={ingest_DbColumn_name, ingest_DbColumn_jdbcPrecision, ingest_DbColumn_jdbcScale, ingest_DbColumn_jdbcType}

# ingest_SqoopImport class attributes and methods

# ingest_Catalogue class attributes and methods

# Relationships
schemas0: BinaryAssociation = BinaryAssociation(
    name="schemas0",
    ends={
        Property(name="ingest_DbSchema", type=ingest_Database, multiplicity=Multiplicity(1, 1)),
        Property(name="ingest_Database", type=ingest_DbSchema, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
tables4: BinaryAssociation = BinaryAssociation(
    name="tables4",
    ends={
        Property(name="ingest_DbTable6", type=ingest_DbSchema, multiplicity=Multiplicity(1, 1)),
        Property(name="ingest_DbSchema5", type=ingest_DbTable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
checkColumn7: BinaryAssociation = BinaryAssociation(
    name="checkColumn7",
    ends={
        Property(name="ingest_DbColumn8", type=ingest_SqoopHiveIncrementalImport, multiplicity=Multiplicity(1, 1)),
        Property(name="ingest_SqoopHiveIncrementalImport", type=ingest_DbColumn, multiplicity=Multiplicity(1, 1))
    }
)
columns1: BinaryAssociation = BinaryAssociation(
    name="columns1",
    ends={
        Property(name="ingest_DbColumn", type=ingest_DbTable, multiplicity=Multiplicity(1, 1)),
        Property(name="ingest_DbTable", type=ingest_DbColumn, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
sqoopImports2: BinaryAssociation = BinaryAssociation(
    name="sqoopImports2",
    ends={
        Property(name="ingest_SqoopImport", type=ingest_DbTable, multiplicity=Multiplicity(1, 1)),
        Property(name="ingest_DbTable3", type=ingest_SqoopImport, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
databases9: BinaryAssociation = BinaryAssociation(
    name="databases9",
    ends={
        Property(name="ingest_Database10", type=ingest_Catalogue, multiplicity=Multiplicity(1, 1)),
        Property(name="ingest_Catalogue", type=ingest_Database, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_ingest_SqoopHiveImport_SqoopImport = Generalization(general=SqoopImport, specific=ingest_SqoopHiveImport)
gen_ingest_SqoopHiveIncrementalImport_SqoopHiveImport = Generalization(general=SqoopHiveImport, specific=ingest_SqoopHiveIncrementalImport)

# Domain Model
domain_model = DomainModel(
    name="ingest",
    types={ingest_Database, ingest_DbSchema, ingest_DbTable, ingest_SqoopHiveImport, SqoopImport, ingest_SqoopHiveIncrementalImport, SqoopHiveImport, ingest_DbColumn, ingest_SqoopImport, ingest_Catalogue},
    associations={schemas0, tables4, checkColumn7, columns1, sqoopImports2, databases9},
    generalizations={gen_ingest_SqoopHiveImport_SqoopImport, gen_ingest_SqoopHiveIncrementalImport_SqoopHiveImport},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)