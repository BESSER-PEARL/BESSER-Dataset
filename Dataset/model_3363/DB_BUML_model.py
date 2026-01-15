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
NamedElement = Class(name="NamedElement")
DB_Table = Class(name="DB::Table")
DatabaseElement = Class(name="DatabaseElement")
DB_Column = Class(name="DB::Column")
DB_NamedElement = Class(name="DB::NamedElement", is_abstract=True)
DB_Database = Class(name="DB::Database")
DB_DatabaseElement = Class(name="DB::DatabaseElement", is_abstract=True)
DB_Type = Class(name="DB::Type")

# NamedElement class attributes and methods

# DB_Table class attributes and methods

# DatabaseElement class attributes and methods

# DB_Column class attributes and methods

# DB_NamedElement class attributes and methods
DB_NamedElement_name: Property = Property(name="name", type=StringType)
DB_NamedElement.attributes={DB_NamedElement_name}

# DB_Database class attributes and methods

# DB_DatabaseElement class attributes and methods

# DB_Type class attributes and methods

# Relationships
columns1: BinaryAssociation = BinaryAssociation(
    name="columns1",
    ends={
        Property(name="DB_Column", type=DB_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="DB_Table", type=DB_Column, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
contents0: BinaryAssociation = BinaryAssociation(
    name="contents0",
    ends={
        Property(name="DB_DatabaseElement", type=DB_Database, multiplicity=Multiplicity(1, 1)),
        Property(name="DB_Database", type=DB_DatabaseElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
primaryKeys2: BinaryAssociation = BinaryAssociation(
    name="primaryKeys2",
    ends={
        Property(name="DB_Column4", type=DB_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="DB_Table3", type=DB_Column, multiplicity=Multiplicity(0, 9999))
    }
)
type5: BinaryAssociation = BinaryAssociation(
    name="type5",
    ends={
        Property(name="DB_Type", type=DB_Column, multiplicity=Multiplicity(1, 1)),
        Property(name="DB_Column6", type=DB_Type, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_DB_DatabaseElement_NamedElement = Generalization(general=NamedElement, specific=DB_DatabaseElement)
gen_DB_Table_DatabaseElement = Generalization(general=DatabaseElement, specific=DB_Table)
gen_DB_Column_NamedElement = Generalization(general=NamedElement, specific=DB_Column)
gen_DB_Type_DatabaseElement = Generalization(general=DatabaseElement, specific=DB_Type)

# Domain Model
domain_model = DomainModel(
    name="DB",
    types={NamedElement, DB_Table, DatabaseElement, DB_Column, DB_NamedElement, DB_Database, DB_DatabaseElement, DB_Type},
    associations={columns1, contents0, primaryKeys2, type5},
    generalizations={gen_DB_DatabaseElement_NamedElement, gen_DB_Table_DatabaseElement, gen_DB_Column_NamedElement, gen_DB_Type_DatabaseElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)