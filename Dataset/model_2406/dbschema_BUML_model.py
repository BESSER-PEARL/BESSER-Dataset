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
ColumnType: Enumeration = Enumeration(
    name="ColumnType",
    literals={
            EnumerationLiteral(name="TINYINT"),
			EnumerationLiteral(name="SMALLINT"),
			EnumerationLiteral(name="INTEGER"),
			EnumerationLiteral(name="BIGINT"),
			EnumerationLiteral(name="FLOAT"),
			EnumerationLiteral(name="REAL"),
			EnumerationLiteral(name="BIT"),
			EnumerationLiteral(name="VARCHAR"),
			EnumerationLiteral(name="LONGVARCHAR"),
			EnumerationLiteral(name="DATE"),
			EnumerationLiteral(name="TIME"),
			EnumerationLiteral(name="TIMESTAMP"),
			EnumerationLiteral(name="BINARY"),
			EnumerationLiteral(name="DOUBLE"),
			EnumerationLiteral(name="NUMERIC"),
			EnumerationLiteral(name="DECIMAL"),
			EnumerationLiteral(name="CHAR"),
			EnumerationLiteral(name="JAVAOBJECT"),
			EnumerationLiteral(name="DISTINCT"),
			EnumerationLiteral(name="STRUCT"),
			EnumerationLiteral(name="ARRAY"),
			EnumerationLiteral(name="BLOB"),
			EnumerationLiteral(name="CLOB"),
			EnumerationLiteral(name="VARBINARY"),
			EnumerationLiteral(name="LONGVARBINARY"),
			EnumerationLiteral(name="NULL"),
			EnumerationLiteral(name="OTHER"),
			EnumerationLiteral(name="NCHAR"),
			EnumerationLiteral(name="NVARCHAR"),
			EnumerationLiteral(name="LONGNVARCHAR"),
			EnumerationLiteral(name="NCLOB"),
			EnumerationLiteral(name="SQLXML"),
			EnumerationLiteral(name="REF"),
			EnumerationLiteral(name="DATALINK"),
			EnumerationLiteral(name="BOOLEAN"),
			EnumerationLiteral(name="ROWID")
    }
)

# Classes
dbschema_NamedElement = Class(name="dbschema::NamedElement", is_abstract=True)
dbschema_DBSchema = Class(name="dbschema::DBSchema")
NamedElement = Class(name="NamedElement")
dbschema_Table = Class(name="dbschema::Table")
dbschema_AttributeColumn = Class(name="dbschema::AttributeColumn")
Column = Class(name="Column")
dbschema_ForeignKeyColumn = Class(name="dbschema::ForeignKeyColumn")
dbschema_Column = Class(name="dbschema::Column", is_abstract=True)

# dbschema_NamedElement class attributes and methods
dbschema_NamedElement_name: Property = Property(name="name", type=StringType)
dbschema_NamedElement.attributes={dbschema_NamedElement_name}

# dbschema_DBSchema class attributes and methods

# NamedElement class attributes and methods

# dbschema_Table class attributes and methods

# dbschema_AttributeColumn class attributes and methods

# Column class attributes and methods

# dbschema_ForeignKeyColumn class attributes and methods

# dbschema_Column class attributes and methods
dbschema_Column_type: Property = Property(name="type", type=StringType)
dbschema_Column_size: Property = Property(name="size", type=IntegerType)
dbschema_Column_primary: Property = Property(name="primary", type=BooleanType)
dbschema_Column.attributes={dbschema_Column_primary, dbschema_Column_size, dbschema_Column_type}

# Relationships
tables0: BinaryAssociation = BinaryAssociation(
    name="tables0",
    ends={
        Property(name="dbschema_Table", type=dbschema_DBSchema, multiplicity=Multiplicity(1, 1)),
        Property(name="dbschema_DBSchema", type=dbschema_Table, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
columns1: BinaryAssociation = BinaryAssociation(
    name="columns1",
    ends={
        Property(name="dbschema_Column", type=dbschema_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="dbschema_Table2", type=dbschema_Column, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
referencedColumn3: BinaryAssociation = BinaryAssociation(
    name="referencedColumn3",
    ends={
        Property(name="dbschema_AttributeColumn", type=dbschema_ForeignKeyColumn, multiplicity=Multiplicity(1, 1)),
        Property(name="dbschema_ForeignKeyColumn", type=dbschema_AttributeColumn, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_dbschema_DBSchema_NamedElement = Generalization(general=NamedElement, specific=dbschema_DBSchema)
gen_dbschema_Table_NamedElement = Generalization(general=NamedElement, specific=dbschema_Table)
gen_dbschema_AttributeColumn_Column = Generalization(general=Column, specific=dbschema_AttributeColumn)
gen_dbschema_ForeignKeyColumn_Column = Generalization(general=Column, specific=dbschema_ForeignKeyColumn)
gen_dbschema_Column_NamedElement = Generalization(general=NamedElement, specific=dbschema_Column)

# Domain Model
domain_model = DomainModel(
    name="dbschema",
    types={dbschema_NamedElement, dbschema_DBSchema, NamedElement, dbschema_Table, dbschema_AttributeColumn, Column, dbschema_ForeignKeyColumn, dbschema_Column, ColumnType},
    associations={tables0, columns1, referencedColumn3},
    generalizations={gen_dbschema_DBSchema_NamedElement, gen_dbschema_Table_NamedElement, gen_dbschema_AttributeColumn_Column, gen_dbschema_ForeignKeyColumn_Column, gen_dbschema_Column_NamedElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)