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
Relational_Named = Class(name="Relational::Named", is_abstract=True)
Relational_Table = Class(name="Relational::Table")
Named = Class(name="Named")
Relational_Column = Class(name="Relational::Column")
Relational_Type = Class(name="Relational::Type")
Relational_Database = Class(name="Relational::Database")

# Relational_Named class attributes and methods
Relational_Named_name: Property = Property(name="name", type=StringType)
Relational_Named.attributes={Relational_Named_name}

# Relational_Table class attributes and methods

# Named class attributes and methods

# Relational_Column class attributes and methods

# Relational_Type class attributes and methods

# Relational_Database class attributes and methods

# Relationships
col0: BinaryAssociation = BinaryAssociation(
    name="col0",
    ends={
        Property(name="Column", type=Relational_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="owner", type=Relational_Column, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
key1: BinaryAssociation = BinaryAssociation(
    name="key1",
    ends={
        Property(name="Column2", type=Relational_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="keyOf", type=Relational_Column, multiplicity=Multiplicity(0, 9999))
    }
)
owner3: BinaryAssociation = BinaryAssociation(
    name="owner3",
    ends={
        Property(name="Table", type=Relational_Column, multiplicity=Multiplicity(1, 1)),
        Property(name="col", type=Relational_Table, multiplicity=Multiplicity(1, 1))
    }
)
keyOf4: BinaryAssociation = BinaryAssociation(
    name="keyOf4",
    ends={
        Property(name="Table5", type=Relational_Column, multiplicity=Multiplicity(1, 1)),
        Property(name="key", type=Relational_Table, multiplicity=Multiplicity(0, 1))
    }
)
type6: BinaryAssociation = BinaryAssociation(
    name="type6",
    ends={
        Property(name="Relational_Type", type=Relational_Column, multiplicity=Multiplicity(1, 1)),
        Property(name="Relational_Column", type=Relational_Type, multiplicity=Multiplicity(1, 1))
    }
)
tables7: BinaryAssociation = BinaryAssociation(
    name="tables7",
    ends={
        Property(name="Relational_Table", type=Relational_Database, multiplicity=Multiplicity(1, 1)),
        Property(name="Relational_Database", type=Relational_Table, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
types8: BinaryAssociation = BinaryAssociation(
    name="types8",
    ends={
        Property(name="Relational_Type10", type=Relational_Database, multiplicity=Multiplicity(1, 1)),
        Property(name="Relational_Database9", type=Relational_Type, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_Relational_Table_Named = Generalization(general=Named, specific=Relational_Table)
gen_Relational_Column_Named = Generalization(general=Named, specific=Relational_Column)
gen_Relational_Type_Named = Generalization(general=Named, specific=Relational_Type)
gen_Relational_Database_Named = Generalization(general=Named, specific=Relational_Database)

# Domain Model
domain_model = DomainModel(
    name="Relational",
    types={Relational_Named, Relational_Table, Named, Relational_Column, Relational_Type, Relational_Database},
    associations={col0, key1, owner3, keyOf4, type6, tables7, types8},
    generalizations={gen_Relational_Table_Named, gen_Relational_Column_Named, gen_Relational_Type_Named, gen_Relational_Database_Named},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)