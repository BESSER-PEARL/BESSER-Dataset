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
Relational_FKey = Class(name="Relational::FKey")
Relational_Type = Class(name="Relational::Type")
Relational_ERModel = Class(name="Relational::ERModel")

# Relational_Named class attributes and methods
Relational_Named_name: Property = Property(name="name", type=StringType)
Relational_Named.attributes={Relational_Named_name}

# Relational_Table class attributes and methods

# Named class attributes and methods

# Relational_Column class attributes and methods

# Relational_FKey class attributes and methods

# Relational_Type class attributes and methods

# Relational_ERModel class attributes and methods

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
fkeys3: BinaryAssociation = BinaryAssociation(
    name="fkeys3",
    ends={
        Property(name="Relational_FKey", type=Relational_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="Relational_Table", type=Relational_FKey, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
owner4: BinaryAssociation = BinaryAssociation(
    name="owner4",
    ends={
        Property(name="Table", type=Relational_Column, multiplicity=Multiplicity(1, 1)),
        Property(name="col", type=Relational_Table, multiplicity=Multiplicity(1, 1))
    }
)
keyOf5: BinaryAssociation = BinaryAssociation(
    name="keyOf5",
    ends={
        Property(name="Table6", type=Relational_Column, multiplicity=Multiplicity(1, 1)),
        Property(name="key", type=Relational_Table, multiplicity=Multiplicity(0, 1))
    }
)
type7: BinaryAssociation = BinaryAssociation(
    name="type7",
    ends={
        Property(name="Relational_Type", type=Relational_Column, multiplicity=Multiplicity(1, 1)),
        Property(name="Relational_Column", type=Relational_Type, multiplicity=Multiplicity(1, 1))
    }
)
ref8: BinaryAssociation = BinaryAssociation(
    name="ref8",
    ends={
        Property(name="Relational_Table10", type=Relational_FKey, multiplicity=Multiplicity(1, 1)),
        Property(name="Relational_FKey9", type=Relational_Table, multiplicity=Multiplicity(1, 1))
    }
)
cols11: BinaryAssociation = BinaryAssociation(
    name="cols11",
    ends={
        Property(name="Relational_Column13", type=Relational_FKey, multiplicity=Multiplicity(1, 1)),
        Property(name="Relational_FKey12", type=Relational_Column, multiplicity=Multiplicity(1, 1))
    }
)
table14: BinaryAssociation = BinaryAssociation(
    name="table14",
    ends={
        Property(name="Relational_Table15", type=Relational_ERModel, multiplicity=Multiplicity(1, 1)),
        Property(name="Relational_ERModel", type=Relational_Table, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
type16: BinaryAssociation = BinaryAssociation(
    name="type16",
    ends={
        Property(name="Relational_Type18", type=Relational_ERModel, multiplicity=Multiplicity(1, 1)),
        Property(name="Relational_ERModel17", type=Relational_Type, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_Relational_Table_Named = Generalization(general=Named, specific=Relational_Table)
gen_Relational_Column_Named = Generalization(general=Named, specific=Relational_Column)
gen_Relational_Type_Named = Generalization(general=Named, specific=Relational_Type)

# Domain Model
domain_model = DomainModel(
    name="Relational",
    types={Relational_Named, Relational_Table, Named, Relational_Column, Relational_FKey, Relational_Type, Relational_ERModel},
    associations={col0, key1, fkeys3, owner4, keyOf5, type7, ref8, cols11, table14, type16},
    generalizations={gen_Relational_Table_Named, gen_Relational_Column_Named, gen_Relational_Type_Named},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)