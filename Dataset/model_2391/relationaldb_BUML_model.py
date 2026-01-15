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
DatabaseKind: Enumeration = Enumeration(
    name="DatabaseKind",
    literals={
            EnumerationLiteral(name="POSTGRES")
    }
)

# Classes
relationaldb_Named = Class(name="relationaldb::Named", is_abstract=True)
relationaldb_Database = Class(name="relationaldb::Database")
Named = Class(name="Named")
relationaldb_Table = Class(name="relationaldb::Table")
relationaldb_Column = Class(name="relationaldb::Column")
relationaldb_Type = Class(name="relationaldb::Type", is_abstract=True)
relationaldb_ForeignKey = Class(name="relationaldb::ForeignKey")
Column = Class(name="Column")
relationaldb_PrimitiveType = Class(name="relationaldb::PrimitiveType", is_abstract=True)
Type = Class(name="Type")
PrimitiveType = Class(name="PrimitiveType")
relationaldb_Integer = Class(name="relationaldb::Integer")
relationaldb_UmlToNoSQLID = Class(name="relationaldb::UmlToNoSQLID")
relationaldb_Varchar = Class(name="relationaldb::Varchar")

# relationaldb_Named class attributes and methods
relationaldb_Named_name: Property = Property(name="name", type=StringType)
relationaldb_Named.attributes={relationaldb_Named_name}

# relationaldb_Database class attributes and methods
relationaldb_Database_rawDatabase: Property = Property(name="rawDatabase", type=StringType)
relationaldb_Database.attributes={relationaldb_Database_rawDatabase}

# Named class attributes and methods

# relationaldb_Table class attributes and methods

# relationaldb_Column class attributes and methods

# relationaldb_Type class attributes and methods

# relationaldb_ForeignKey class attributes and methods

# Column class attributes and methods

# relationaldb_PrimitiveType class attributes and methods

# Type class attributes and methods

# PrimitiveType class attributes and methods

# relationaldb_Integer class attributes and methods

# relationaldb_UmlToNoSQLID class attributes and methods

# relationaldb_Varchar class attributes and methods
relationaldb_Varchar_length: Property = Property(name="length", type=IntegerType)
relationaldb_Varchar.attributes={relationaldb_Varchar_length}

# Relationships
tables0: BinaryAssociation = BinaryAssociation(
    name="tables0",
    ends={
        Property(name="relationaldb_Table", type=relationaldb_Database, multiplicity=Multiplicity(1, 1)),
        Property(name="relationaldb_Database", type=relationaldb_Table, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
col1: BinaryAssociation = BinaryAssociation(
    name="col1",
    ends={
        Property(name="Column", type=relationaldb_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="owner", type=relationaldb_Column, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
primaryKeys2: BinaryAssociation = BinaryAssociation(
    name="primaryKeys2",
    ends={
        Property(name="relationaldb_Column", type=relationaldb_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="relationaldb_Table3", type=relationaldb_Column, multiplicity=Multiplicity(0, 9999))
    }
)
owner4: BinaryAssociation = BinaryAssociation(
    name="owner4",
    ends={
        Property(name="Table", type=relationaldb_Column, multiplicity=Multiplicity(1, 1)),
        Property(name="col", type=relationaldb_Table, multiplicity=Multiplicity(1, 1))
    }
)
type5: BinaryAssociation = BinaryAssociation(
    name="type5",
    ends={
        Property(name="relationaldb_Type", type=relationaldb_Column, multiplicity=Multiplicity(1, 1)),
        Property(name="relationaldb_Column6", type=relationaldb_Type, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
referencedColumn7: BinaryAssociation = BinaryAssociation(
    name="referencedColumn7",
    ends={
        Property(name="relationaldb_Column8", type=relationaldb_ForeignKey, multiplicity=Multiplicity(1, 1)),
        Property(name="relationaldb_ForeignKey", type=relationaldb_Column, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_relationaldb_Database_Named = Generalization(general=Named, specific=relationaldb_Database)
gen_relationaldb_Table_Named = Generalization(general=Named, specific=relationaldb_Table)
gen_relationaldb_Column_Named = Generalization(general=Named, specific=relationaldb_Column)
gen_relationaldb_ForeignKey_Column = Generalization(general=Column, specific=relationaldb_ForeignKey)
gen_relationaldb_PrimitiveType_Type = Generalization(general=Type, specific=relationaldb_PrimitiveType)
gen_relationaldb_Varchar_PrimitiveType = Generalization(general=PrimitiveType, specific=relationaldb_Varchar)
gen_relationaldb_Integer_PrimitiveType = Generalization(general=PrimitiveType, specific=relationaldb_Integer)
gen_relationaldb_UmlToNoSQLID_PrimitiveType = Generalization(general=PrimitiveType, specific=relationaldb_UmlToNoSQLID)

# Domain Model
domain_model = DomainModel(
    name="relationaldb",
    types={relationaldb_Named, relationaldb_Database, Named, relationaldb_Table, relationaldb_Column, relationaldb_Type, relationaldb_ForeignKey, Column, relationaldb_PrimitiveType, Type, PrimitiveType, relationaldb_Integer, relationaldb_UmlToNoSQLID, relationaldb_Varchar, DatabaseKind},
    associations={tables0, col1, primaryKeys2, owner4, type5, referencedColumn7},
    generalizations={gen_relationaldb_Database_Named, gen_relationaldb_Table_Named, gen_relationaldb_Column_Named, gen_relationaldb_ForeignKey_Column, gen_relationaldb_PrimitiveType_Type, gen_relationaldb_Varchar_PrimitiveType, gen_relationaldb_Integer_PrimitiveType, gen_relationaldb_UmlToNoSQLID_PrimitiveType},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)