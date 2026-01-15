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
DB_Database = Class(name="DB::Database")
DB_DatabaseElement = Class(name="DB::DatabaseElement", is_abstract=True)
DB_NamedElement = Class(name="DB::NamedElement", is_abstract=True)
DB_Table = Class(name="DB::Table")
DatabaseElement = Class(name="DatabaseElement")
NamedElement = Class(name="NamedElement")
DB_Column = Class(name="DB::Column")
DB_ForeignKey = Class(name="DB::ForeignKey")

# DB_Database class attributes and methods

# DB_DatabaseElement class attributes and methods

# DB_NamedElement class attributes and methods
DB_NamedElement_name: Property = Property(name="name", type=StringType)
DB_NamedElement.attributes={DB_NamedElement_name}

# DB_Table class attributes and methods

# DatabaseElement class attributes and methods

# NamedElement class attributes and methods

# DB_Column class attributes and methods
DB_Column_type: Property = Property(name="type", type=StringType)
DB_Column.attributes={DB_Column_type}

# DB_ForeignKey class attributes and methods
DB_ForeignKey_isMany: Property = Property(name="isMany", type=StringType)
DB_ForeignKey.attributes={DB_ForeignKey_isMany}

# Relationships
contents0: BinaryAssociation = BinaryAssociation(
    name="contents0",
    ends={
        Property(name="DatabaseElement", type=DB_Database, multiplicity=Multiplicity(1, 1)),
        Property(name="database", type=DB_DatabaseElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
database1: BinaryAssociation = BinaryAssociation(
    name="database1",
    ends={
        Property(name="Database", type=DB_DatabaseElement, multiplicity=Multiplicity(1, 1)),
        Property(name="contents", type=DB_Database, multiplicity=Multiplicity(0, 1))
    }
)
table4: BinaryAssociation = BinaryAssociation(
    name="table4",
    ends={
        Property(name="Table", type=DB_Column, multiplicity=Multiplicity(1, 1)),
        Property(name="columns", type=DB_Table, multiplicity=Multiplicity(0, 1))
    }
)
columns2: BinaryAssociation = BinaryAssociation(
    name="columns2",
    ends={
        Property(name="Column", type=DB_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="table", type=DB_Column, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
primaryKeys3: BinaryAssociation = BinaryAssociation(
    name="primaryKeys3",
    ends={
        Property(name="DB_Column", type=DB_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="DB_Table", type=DB_Column, multiplicity=Multiplicity(0, 9999))
    }
)
parent5: BinaryAssociation = BinaryAssociation(
    name="parent5",
    ends={
        Property(name="DB_Column6", type=DB_ForeignKey, multiplicity=Multiplicity(1, 1)),
        Property(name="DB_ForeignKey", type=DB_Column, multiplicity=Multiplicity(0, 1))
    }
)
child7: BinaryAssociation = BinaryAssociation(
    name="child7",
    ends={
        Property(name="DB_Column9", type=DB_ForeignKey, multiplicity=Multiplicity(1, 1)),
        Property(name="DB_ForeignKey8", type=DB_Column, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_DB_Table_DatabaseElement = Generalization(general=DatabaseElement, specific=DB_Table)
gen_DB_DatabaseElement_NamedElement = Generalization(general=NamedElement, specific=DB_DatabaseElement)
gen_DB_Column_DatabaseElement = Generalization(general=DatabaseElement, specific=DB_Column)
gen_DB_ForeignKey_DatabaseElement = Generalization(general=DatabaseElement, specific=DB_ForeignKey)

# Domain Model
domain_model = DomainModel(
    name="DB",
    types={DB_Database, DB_DatabaseElement, DB_NamedElement, DB_Table, DatabaseElement, NamedElement, DB_Column, DB_ForeignKey},
    associations={contents0, database1, table4, columns2, primaryKeys3, parent5, child7},
    generalizations={gen_DB_Table_DatabaseElement, gen_DB_DatabaseElement_NamedElement, gen_DB_Column_DatabaseElement, gen_DB_ForeignKey_DatabaseElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)