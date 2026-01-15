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
Type: Enumeration = Enumeration(
    name="Type",
    literals={
            EnumerationLiteral(name="integer"),
			EnumerationLiteral(name="float"),
			EnumerationLiteral(name="string"),
			EnumerationLiteral(name="datetime"),
			EnumerationLiteral(name="bool")
    }
)

# Classes
tables_Database = Class(name="tables::Database")
tables_Table = Class(name="tables::Table")
tables_Column = Class(name="tables::Column")
tables_ForeignKey = Class(name="tables::ForeignKey")

# tables_Database class attributes and methods
tables_Database_name: Property = Property(name="name", type=StringType)
tables_Database.attributes={tables_Database_name}

# tables_Table class attributes and methods
tables_Table_name: Property = Property(name="name", type=StringType)
tables_Table.attributes={tables_Table_name}

# tables_Column class attributes and methods
tables_Column_name: Property = Property(name="name", type=StringType)
tables_Column_type: Property = Property(name="type", type=StringType)
tables_Column.attributes={tables_Column_name, tables_Column_type}

# tables_ForeignKey class attributes and methods
tables_ForeignKey_name: Property = Property(name="name", type=StringType)
tables_ForeignKey.attributes={tables_ForeignKey_name}

# Relationships
tables0: BinaryAssociation = BinaryAssociation(
    name="tables0",
    ends={
        Property(name="Table", type=tables_Database, multiplicity=Multiplicity(1, 1)),
        Property(name="database", type=tables_Table, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
columns1: BinaryAssociation = BinaryAssociation(
    name="columns1",
    ends={
        Property(name="Column", type=tables_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="table", type=tables_Column, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
database2: BinaryAssociation = BinaryAssociation(
    name="database2",
    ends={
        Property(name="Database", type=tables_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="tables", type=tables_Database, multiplicity=Multiplicity(1, 1))
    }
)
primary_key3: BinaryAssociation = BinaryAssociation(
    name="primary_key3",
    ends={
        Property(name="tables_Column", type=tables_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="tables_Table", type=tables_Column, multiplicity=Multiplicity(0, 1))
    }
)
foreign_key6: BinaryAssociation = BinaryAssociation(
    name="foreign_key6",
    ends={
        Property(name="ForeignKey", type=tables_Column, multiplicity=Multiplicity(1, 1)),
        Property(name="column", type=tables_ForeignKey, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
target7: BinaryAssociation = BinaryAssociation(
    name="target7",
    ends={
        Property(name="tables_Table8", type=tables_ForeignKey, multiplicity=Multiplicity(1, 1)),
        Property(name="tables_ForeignKey", type=tables_Table, multiplicity=Multiplicity(1, 1))
    }
)
column9: BinaryAssociation = BinaryAssociation(
    name="column9",
    ends={
        Property(name="Column10", type=tables_ForeignKey, multiplicity=Multiplicity(1, 1)),
        Property(name="foreign_key", type=tables_Column, multiplicity=Multiplicity(1, 1))
    }
)
table4: BinaryAssociation = BinaryAssociation(
    name="table4",
    ends={
        Property(name="Table5", type=tables_Column, multiplicity=Multiplicity(1, 1)),
        Property(name="columns", type=tables_Table, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="tables",
    types={tables_Database, tables_Table, tables_Column, tables_ForeignKey, Type},
    associations={tables0, columns1, database2, primary_key3, foreign_key6, target7, column9, table4},
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