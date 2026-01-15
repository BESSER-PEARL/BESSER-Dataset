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
db_NamedElement = Class(name="db::NamedElement", is_abstract=True)
db_DatabaseElement = Class(name="db::DatabaseElement", is_abstract=True)
NamedElement = Class(name="NamedElement")
db_Table = Class(name="db::Table")
DatabaseElement = Class(name="DatabaseElement")
db_Column = Class(name="db::Column")
db_Database = Class(name="db::Database")
db_ForeignKey = Class(name="db::ForeignKey")

# db_NamedElement class attributes and methods
db_NamedElement_name: Property = Property(name="name", type=StringType)
db_NamedElement.attributes={db_NamedElement_name}

# db_DatabaseElement class attributes and methods

# NamedElement class attributes and methods

# db_Table class attributes and methods

# DatabaseElement class attributes and methods

# db_Column class attributes and methods
db_Column_type: Property = Property(name="type", type=StringType)
db_Column.attributes={db_Column_type}

# db_Database class attributes and methods

# db_ForeignKey class attributes and methods
db_ForeignKey_isMany: Property = Property(name="isMany", type=StringType)
db_ForeignKey.attributes={db_ForeignKey_isMany}

# Relationships
contents0: BinaryAssociation = BinaryAssociation(
    name="contents0",
    ends={
        Property(name="DatabaseElement", type=db_Database, multiplicity=Multiplicity(1, 1)),
        Property(name="database", type=db_DatabaseElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
database1: BinaryAssociation = BinaryAssociation(
    name="database1",
    ends={
        Property(name="Database", type=db_DatabaseElement, multiplicity=Multiplicity(1, 1)),
        Property(name="contents", type=db_Database, multiplicity=Multiplicity(0, 1))
    }
)
primaryKeys3: BinaryAssociation = BinaryAssociation(
    name="primaryKeys3",
    ends={
        Property(name="db_Column", type=db_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="db_Table", type=db_Column, multiplicity=Multiplicity(0, 9999))
    }
)
table4: BinaryAssociation = BinaryAssociation(
    name="table4",
    ends={
        Property(name="Table", type=db_Column, multiplicity=Multiplicity(1, 1)),
        Property(name="columns", type=db_Table, multiplicity=Multiplicity(0, 1))
    }
)
parent5: BinaryAssociation = BinaryAssociation(
    name="parent5",
    ends={
        Property(name="db_Column6", type=db_ForeignKey, multiplicity=Multiplicity(1, 1)),
        Property(name="db_ForeignKey", type=db_Column, multiplicity=Multiplicity(0, 1))
    }
)
columns2: BinaryAssociation = BinaryAssociation(
    name="columns2",
    ends={
        Property(name="Column", type=db_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="table", type=db_Column, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
child7: BinaryAssociation = BinaryAssociation(
    name="child7",
    ends={
        Property(name="db_Column9", type=db_ForeignKey, multiplicity=Multiplicity(1, 1)),
        Property(name="db_ForeignKey8", type=db_Column, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_db_DatabaseElement_NamedElement = Generalization(general=NamedElement, specific=db_DatabaseElement)
gen_db_Table_DatabaseElement = Generalization(general=DatabaseElement, specific=db_Table)
gen_db_Column_DatabaseElement = Generalization(general=DatabaseElement, specific=db_Column)
gen_db_ForeignKey_DatabaseElement = Generalization(general=DatabaseElement, specific=db_ForeignKey)

# Domain Model
domain_model = DomainModel(
    name="db",
    types={db_NamedElement, db_DatabaseElement, NamedElement, db_Table, DatabaseElement, db_Column, db_Database, db_ForeignKey},
    associations={contents0, database1, primaryKeys3, table4, parent5, columns2, child7},
    generalizations={gen_db_DatabaseElement_NamedElement, gen_db_Table_DatabaseElement, gen_db_Column_DatabaseElement, gen_db_ForeignKey_DatabaseElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)