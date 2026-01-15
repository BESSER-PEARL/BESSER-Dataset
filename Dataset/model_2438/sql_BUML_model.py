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
Sql_NamedElement = Class(name="Sql::NamedElement", is_abstract=True)
Sql_Column = Class(name="Sql::Column")
Sql_Database = Class(name="Sql::Database")
NamedElement = Class(name="NamedElement")
Sql_Table = Class(name="Sql::Table")

# Sql_NamedElement class attributes and methods
Sql_NamedElement_name: Property = Property(name="name", type=StringType)
Sql_NamedElement.attributes={Sql_NamedElement_name}

# Sql_Column class attributes and methods
Sql_Column_type: Property = Property(name="type", type=StringType)
Sql_Column.attributes={Sql_Column_type}

# Sql_Database class attributes and methods

# NamedElement class attributes and methods

# Sql_Table class attributes and methods

# Relationships
column1: BinaryAssociation = BinaryAssociation(
    name="column1",
    ends={
        Property(name="Sql_Column", type=Sql_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="Sql_Table2", type=Sql_Column, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
table0: BinaryAssociation = BinaryAssociation(
    name="table0",
    ends={
        Property(name="Sql_Table", type=Sql_Database, multiplicity=Multiplicity(1, 1)),
        Property(name="Sql_Database", type=Sql_Table, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_Sql_Column_NamedElement = Generalization(general=NamedElement, specific=Sql_Column)
gen_Sql_Database_NamedElement = Generalization(general=NamedElement, specific=Sql_Database)
gen_Sql_Table_NamedElement = Generalization(general=NamedElement, specific=Sql_Table)

# Domain Model
domain_model = DomainModel(
    name="Sql",
    types={Sql_NamedElement, Sql_Column, Sql_Database, NamedElement, Sql_Table},
    associations={column1, table0},
    generalizations={gen_Sql_Column_NamedElement, gen_Sql_Database_NamedElement, gen_Sql_Table_NamedElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)