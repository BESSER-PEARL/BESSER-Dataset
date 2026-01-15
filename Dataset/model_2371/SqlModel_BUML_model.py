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
            EnumerationLiteral(name="int"),
			EnumerationLiteral(name="varchar"),
			EnumerationLiteral(name="text"),
			EnumerationLiteral(name="unknown"),
			EnumerationLiteral(name="bool"),
			EnumerationLiteral(name="decimal")
    }
)

# Classes
DB_Database = Class(name="DB::Database")
DB_Table = Class(name="DB::Table")
DB_ForeignKey = Class(name="DB::ForeignKey")
DB_Key = Class(name="DB::Key")
DB_Column = Class(name="DB::Column")

# DB_Database class attributes and methods
DB_Database_name: Property = Property(name="name", type=StringType)
DB_Database.attributes={DB_Database_name}

# DB_Table class attributes and methods
DB_Table_name: Property = Property(name="name", type=StringType)
DB_Table.attributes={DB_Table_name}

# DB_ForeignKey class attributes and methods
DB_ForeignKey_isMany: Property = Property(name="isMany", type=StringType)
DB_ForeignKey.attributes={DB_ForeignKey_isMany}

# DB_Key class attributes and methods
DB_Key_name: Property = Property(name="name", type=StringType)
DB_Key.attributes={DB_Key_name}

# DB_Column class attributes and methods
DB_Column_name: Property = Property(name="name", type=StringType)
DB_Column_type: Property = Property(name="type", type=StringType)
DB_Column_notNull: Property = Property(name="notNull", type=BooleanType)
DB_Column.attributes={DB_Column_notNull, DB_Column_type, DB_Column_name}

# Relationships
tables0: BinaryAssociation = BinaryAssociation(
    name="tables0",
    ends={
        Property(name="DB_Table", type=DB_Database, multiplicity=Multiplicity(1, 1)),
        Property(name="DB_Database", type=DB_Table, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
foreignkeys1: BinaryAssociation = BinaryAssociation(
    name="foreignkeys1",
    ends={
        Property(name="DB_ForeignKey", type=DB_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="DB_Table2", type=DB_ForeignKey, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
primary_key3: BinaryAssociation = BinaryAssociation(
    name="primary_key3",
    ends={
        Property(name="DB_Key", type=DB_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="DB_Table4", type=DB_Key, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
key13: BinaryAssociation = BinaryAssociation(
    name="key13",
    ends={
        Property(name="DB_Key15", type=DB_Column, multiplicity=Multiplicity(1, 1)),
        Property(name="DB_Column14", type=DB_Key, multiplicity=Multiplicity(0, 1))
    }
)
foreign16: BinaryAssociation = BinaryAssociation(
    name="foreign16",
    ends={
        Property(name="DB_ForeignKey18", type=DB_Column, multiplicity=Multiplicity(1, 1)),
        Property(name="DB_Column17", type=DB_ForeignKey, multiplicity=Multiplicity(0, 9999))
    }
)
referencedKey19: BinaryAssociation = BinaryAssociation(
    name="referencedKey19",
    ends={
        Property(name="DB_Key21", type=DB_ForeignKey, multiplicity=Multiplicity(1, 1)),
        Property(name="DB_ForeignKey20", type=DB_Key, multiplicity=Multiplicity(0, 1))
    }
)
foreign_column22: BinaryAssociation = BinaryAssociation(
    name="foreign_column22",
    ends={
        Property(name="DB_Column24", type=DB_ForeignKey, multiplicity=Multiplicity(1, 1)),
        Property(name="DB_ForeignKey23", type=DB_Column, multiplicity=Multiplicity(0, 1))
    }
)
columns5: BinaryAssociation = BinaryAssociation(
    name="columns5",
    ends={
        Property(name="DB_Column", type=DB_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="DB_Table6", type=DB_Column, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
database7: BinaryAssociation = BinaryAssociation(
    name="database7",
    ends={
        Property(name="DB_Database9", type=DB_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="DB_Table8", type=DB_Database, multiplicity=Multiplicity(1, 1))
    }
)
table10: BinaryAssociation = BinaryAssociation(
    name="table10",
    ends={
        Property(name="DB_Table12", type=DB_Column, multiplicity=Multiplicity(1, 1)),
        Property(name="DB_Column11", type=DB_Table, multiplicity=Multiplicity(0, 1))
    }
)
key_column25: BinaryAssociation = BinaryAssociation(
    name="key_column25",
    ends={
        Property(name="DB_Column27", type=DB_Key, multiplicity=Multiplicity(1, 1)),
        Property(name="DB_Key26", type=DB_Column, multiplicity=Multiplicity(1, 9999))
    }
)
referenced28: BinaryAssociation = BinaryAssociation(
    name="referenced28",
    ends={
        Property(name="DB_ForeignKey30", type=DB_Key, multiplicity=Multiplicity(1, 1)),
        Property(name="DB_Key29", type=DB_ForeignKey, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="DB",
    types={DB_Database, DB_Table, DB_ForeignKey, DB_Key, DB_Column, DataType},
    associations={tables0, foreignkeys1, primary_key3, key13, foreign16, referencedKey19, foreign_column22, columns5, database7, table10, key_column25, referenced28},
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