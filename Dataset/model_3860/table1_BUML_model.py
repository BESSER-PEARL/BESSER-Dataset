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
table_NamedElement = Class(name="table::NamedElement")
table_Table = Class(name="table::Table")
NamedElement = Class(name="NamedElement")
table_Column = Class(name="table::Column")

# table_NamedElement class attributes and methods
table_NamedElement_name: Property = Property(name="name", type=StringType)
table_NamedElement.attributes={table_NamedElement_name}

# table_Table class attributes and methods

# NamedElement class attributes and methods

# table_Column class attributes and methods
table_Column_type: Property = Property(name="type", type=StringType)
table_Column.attributes={table_Column_type}

# Relationships
columns0: BinaryAssociation = BinaryAssociation(
    name="columns0",
    ends={
        Property(name="table_Column", type=table_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="table_Table", type=table_Column, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
pkeys1: BinaryAssociation = BinaryAssociation(
    name="pkeys1",
    ends={
        Property(name="table_Column3", type=table_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="table_Table2", type=table_Column, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_table_Table_NamedElement = Generalization(general=NamedElement, specific=table_Table)
gen_table_Column_NamedElement = Generalization(general=NamedElement, specific=table_Column)

# Domain Model
domain_model = DomainModel(
    name="table",
    types={table_NamedElement, table_Table, NamedElement, table_Column},
    associations={columns0, pkeys1},
    generalizations={gen_table_Table_NamedElement, gen_table_Column_NamedElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)