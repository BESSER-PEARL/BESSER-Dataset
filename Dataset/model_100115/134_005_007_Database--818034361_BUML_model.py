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
DataType: Enumeration = Enumeration(
    name="DataType",
    literals={
            EnumerationLiteral(name="String"),
			EnumerationLiteral(name="Int"),
			EnumerationLiteral(name="Float"),
			EnumerationLiteral(name="Date")
    }
)

# Classes
database_Column = Class(name="database_Column")
database_Database = Class(name="database_Database")
database_ForeignKey = Class(name="database_ForeignKey")
database_Table = Class(name="database_Table")

# database_Column class attributes and methods
database_Column_Name: Property = Property(name="Name", type=StringType)
database_Column_Type: Property = Property(name="Type", type=StringType)
database_Column_IsPrimaryKey: Property = Property(name="IsPrimaryKey", type=BooleanType)
database_Column.attributes={database_Column_IsPrimaryKey, database_Column_Type, database_Column_Name}

# database_Database class attributes and methods

# database_ForeignKey class attributes and methods
database_ForeignKey_Name: Property = Property(name="Name", type=StringType)
database_ForeignKey.attributes={database_ForeignKey_Name}

# database_Table class attributes and methods
database_Table_Name: Property = Property(name="Name", type=StringType)
database_Table.attributes={database_Table_Name}

# Relationships
DbTableRoot2: BinaryAssociation = BinaryAssociation(
    name="DbTableRoot2",
    ends={
        Property(name="Database", type=database_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="DbTable", type=database_Database, multiplicity=Multiplicity(1, 1))
    }
)
TableColumn3: BinaryAssociation = BinaryAssociation(
    name="TableColumn3",
    ends={
        Property(name="Column", type=database_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="ColumnTable", type=database_Column, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
ColumnTable4: BinaryAssociation = BinaryAssociation(
    name="ColumnTable4",
    ends={
        Property(name="Table5", type=database_Column, multiplicity=Multiplicity(1, 1)),
        Property(name="TableColumn", type=database_Table, multiplicity=Multiplicity(1, 1))
    }
)
SourceTable6: BinaryAssociation = BinaryAssociation(
    name="SourceTable6",
    ends={
        Property(name="database_Table", type=database_ForeignKey, multiplicity=Multiplicity(1, 1)),
        Property(name="database_ForeignKey", type=database_Table, multiplicity=Multiplicity(1, 1))
    }
)
TargetTable7: BinaryAssociation = BinaryAssociation(
    name="TargetTable7",
    ends={
        Property(name="database_Table9", type=database_ForeignKey, multiplicity=Multiplicity(1, 1)),
        Property(name="database_ForeignKey8", type=database_Table, multiplicity=Multiplicity(1, 1))
    }
)
SourceColumn10: BinaryAssociation = BinaryAssociation(
    name="SourceColumn10",
    ends={
        Property(name="database_Column", type=database_ForeignKey, multiplicity=Multiplicity(1, 1)),
        Property(name="database_ForeignKey11", type=database_Column, multiplicity=Multiplicity(1, 9999))
    }
)
TargetColumn12: BinaryAssociation = BinaryAssociation(
    name="TargetColumn12",
    ends={
        Property(name="database_Column14", type=database_ForeignKey, multiplicity=Multiplicity(1, 1)),
        Property(name="database_ForeignKey13", type=database_Column, multiplicity=Multiplicity(1, 9999))
    }
)
DbFkRoot15: BinaryAssociation = BinaryAssociation(
    name="DbFkRoot15",
    ends={
        Property(name="Database16", type=database_ForeignKey, multiplicity=Multiplicity(1, 1)),
        Property(name="DbFK", type=database_Database, multiplicity=Multiplicity(1, 1))
    }
)
DbFK0: BinaryAssociation = BinaryAssociation(
    name="DbFK0",
    ends={
        Property(name="ForeignKey", type=database_Database, multiplicity=Multiplicity(1, 1)),
        Property(name="DbFkRoot", type=database_ForeignKey, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
DbTable1: BinaryAssociation = BinaryAssociation(
    name="DbTable1",
    ends={
        Property(name="Table", type=database_Database, multiplicity=Multiplicity(1, 1)),
        Property(name="DbTableRoot", type=database_Table, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="database",
    types={database_Column, database_Database, database_ForeignKey, database_Table, DataType},
    associations={DbTableRoot2, TableColumn3, ColumnTable4, SourceTable6, TargetTable7, SourceColumn10, TargetColumn12, DbFkRoot15, DbFK0, DbTable1},
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