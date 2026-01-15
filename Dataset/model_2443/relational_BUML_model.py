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
relationalmm_Named = Class(name="relationalmm::Named")
relationalmm_Table = Class(name="relationalmm::Table")
Named = Class(name="Named")
relationalmm_Column = Class(name="relationalmm::Column")
relationalmm_Type = Class(name="relationalmm::Type")

# relationalmm_Named class attributes and methods
relationalmm_Named_name: Property = Property(name="name", type=StringType)
relationalmm_Named.attributes={relationalmm_Named_name}

# relationalmm_Table class attributes and methods

# Named class attributes and methods

# relationalmm_Column class attributes and methods

# relationalmm_Type class attributes and methods

# Relationships
type2: BinaryAssociation = BinaryAssociation(
    name="type2",
    ends={
        Property(name="relationalmm_Type", type=relationalmm_Column, multiplicity=Multiplicity(1, 1)),
        Property(name="relationalmm_Column3", type=relationalmm_Type, multiplicity=Multiplicity(1, 1))
    }
)
owner4: BinaryAssociation = BinaryAssociation(
    name="owner4",
    ends={
        Property(name="Table", type=relationalmm_Column, multiplicity=Multiplicity(1, 1)),
        Property(name="col", type=relationalmm_Table, multiplicity=Multiplicity(1, 1))
    }
)
col0: BinaryAssociation = BinaryAssociation(
    name="col0",
    ends={
        Property(name="Column", type=relationalmm_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="owner", type=relationalmm_Column, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
key1: BinaryAssociation = BinaryAssociation(
    name="key1",
    ends={
        Property(name="relationalmm_Column", type=relationalmm_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="relationalmm_Table", type=relationalmm_Column, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_relationalmm_Table_Named = Generalization(general=Named, specific=relationalmm_Table)
gen_relationalmm_Column_Named = Generalization(general=Named, specific=relationalmm_Column)
gen_relationalmm_Type_Named = Generalization(general=Named, specific=relationalmm_Type)

# Domain Model
domain_model = DomainModel(
    name="relationalmm",
    types={relationalmm_Named, relationalmm_Table, Named, relationalmm_Column, relationalmm_Type},
    associations={type2, owner4, col0, key1},
    generalizations={gen_relationalmm_Table_Named, gen_relationalmm_Column_Named, gen_relationalmm_Type_Named},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)