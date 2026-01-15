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
sql_Model = Class(name="sql::Model")
sql_SelectQuery = Class(name="sql::SelectQuery")
sql_Table = Class(name="sql::Table")
NamedElement = Class(name="NamedElement")
sql_Column = Class(name="sql::Column")
sql_NamedElement = Class(name="sql::NamedElement", is_abstract=True)

# sql_Model class attributes and methods

# sql_SelectQuery class attributes and methods

# sql_Table class attributes and methods

# NamedElement class attributes and methods

# sql_Column class attributes and methods

# sql_NamedElement class attributes and methods
sql_NamedElement_name: Property = Property(name="name", type=StringType)
sql_NamedElement.attributes={sql_NamedElement_name}

# Relationships
queries0: BinaryAssociation = BinaryAssociation(
    name="queries0",
    ends={
        Property(name="sql_Model", type=sql_SelectQuery, multiplicity=Multiplicity(0, 9999), is_composite=True),
        Property(name="sql_SelectQuery", type=sql_Model, multiplicity=Multiplicity(1, 1))
    }
)
columns3: BinaryAssociation = BinaryAssociation(
    name="columns3",
    ends={
        Property(name="sql_Table4", type=sql_Column, multiplicity=Multiplicity(0, 9999), is_composite=True),
        Property(name="sql_Column", type=sql_Table, multiplicity=Multiplicity(1, 1))
    }
)
tables1: BinaryAssociation = BinaryAssociation(
    name="tables1",
    ends={
        Property(name="sql_Table", type=sql_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_Model2", type=sql_Table, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
from5: BinaryAssociation = BinaryAssociation(
    name="from5",
    ends={
        Property(name="sql_Table7", type=sql_SelectQuery, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_SelectQuery6", type=sql_Table, multiplicity=Multiplicity(1, 9999))
    }
)
what8: BinaryAssociation = BinaryAssociation(
    name="what8",
    ends={
        Property(name="sql_Column10", type=sql_SelectQuery, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_SelectQuery9", type=sql_Column, multiplicity=Multiplicity(1, 9999))
    }
)

# Generalizations
gen_sql_Table_NamedElement = Generalization(general=NamedElement, specific=sql_Table)
gen_sql_Column_NamedElement = Generalization(general=NamedElement, specific=sql_Column)

# Domain Model
domain_model = DomainModel(
    name="sql",
    types={sql_Model, sql_SelectQuery, sql_Table, NamedElement, sql_Column, sql_NamedElement},
    associations={queries0, columns3, tables1, from5, what8},
    generalizations={gen_sql_Table_NamedElement, gen_sql_Column_NamedElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)