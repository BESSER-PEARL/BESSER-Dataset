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
sql_Element = Class(name="sql::Element")
sql_Table = Class(name="sql::Table")
Element = Class(name="Element")
sql_Column = Class(name="sql::Column")

# sql_Element class attributes and methods
sql_Element_name: Property = Property(name="name", type=StringType)
sql_Element.attributes={sql_Element_name}

# sql_Table class attributes and methods

# Element class attributes and methods

# sql_Column class attributes and methods
sql_Column_type: Property = Property(name="type", type=StringType)
sql_Column.attributes={sql_Column_type}

# Relationships
column0: BinaryAssociation = BinaryAssociation(
    name="column0",
    ends={
        Property(name="Column", type=sql_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="owner", type=sql_Column, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
owner5: BinaryAssociation = BinaryAssociation(
    name="owner5",
    ends={
        Property(name="Table", type=sql_Column, multiplicity=Multiplicity(1, 1)),
        Property(name="column", type=sql_Table, multiplicity=Multiplicity(1, 1))
    }
)
key1: BinaryAssociation = BinaryAssociation(
    name="key1",
    ends={
        Property(name="sql_Column", type=sql_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_Table", type=sql_Column, multiplicity=Multiplicity(1, 9999))
    }
)
fkey2: BinaryAssociation = BinaryAssociation(
    name="fkey2",
    ends={
        Property(name="sql_Column4", type=sql_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_Table3", type=sql_Column, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_sql_Table_Element = Generalization(general=Element, specific=sql_Table)
gen_sql_Column_Element = Generalization(general=Element, specific=sql_Column)

# Domain Model
domain_model = DomainModel(
    name="sql",
    types={sql_Element, sql_Table, Element, sql_Column},
    associations={column0, owner5, key1, fkey2},
    generalizations={gen_sql_Table_Element, gen_sql_Column_Element},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)