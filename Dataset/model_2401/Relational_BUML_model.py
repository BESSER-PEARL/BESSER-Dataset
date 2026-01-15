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
relational_Named = Class(name="relational::Named", is_abstract=True)
relational_Table = Class(name="relational::Table")
Named = Class(name="Named")
relational_Schema = Class(name="relational::Schema")
relational_Column = Class(name="relational::Column")
relational_Type = Class(name="relational::Type")

# relational_Named class attributes and methods
relational_Named_name: Property = Property(name="name", type=StringType)
relational_Named.attributes={relational_Named_name}

# relational_Table class attributes and methods

# Named class attributes and methods

# relational_Schema class attributes and methods

# relational_Column class attributes and methods

# relational_Type class attributes and methods

# Relationships
key1: BinaryAssociation = BinaryAssociation(
    name="key1",
    ends={
        Property(name="Column2", type=relational_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="keyOf", type=relational_Column, multiplicity=Multiplicity(0, 9999))
    }
)
owner3: BinaryAssociation = BinaryAssociation(
    name="owner3",
    ends={
        Property(name="Schema", type=relational_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="tables", type=relational_Schema, multiplicity=Multiplicity(0, 1))
    }
)
owner4: BinaryAssociation = BinaryAssociation(
    name="owner4",
    ends={
        Property(name="Table", type=relational_Column, multiplicity=Multiplicity(1, 1)),
        Property(name="col", type=relational_Table, multiplicity=Multiplicity(1, 1))
    }
)
col0: BinaryAssociation = BinaryAssociation(
    name="col0",
    ends={
        Property(name="Column", type=relational_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="owner", type=relational_Column, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type7: BinaryAssociation = BinaryAssociation(
    name="type7",
    ends={
        Property(name="relational_Type", type=relational_Column, multiplicity=Multiplicity(1, 1)),
        Property(name="relational_Column", type=relational_Type, multiplicity=Multiplicity(1, 1))
    }
)
tables8: BinaryAssociation = BinaryAssociation(
    name="tables8",
    ends={
        Property(name="Table10", type=relational_Schema, multiplicity=Multiplicity(1, 1)),
        Property(name="owner9", type=relational_Table, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
types11: BinaryAssociation = BinaryAssociation(
    name="types11",
    ends={
        Property(name="relational_Type12", type=relational_Schema, multiplicity=Multiplicity(1, 1)),
        Property(name="relational_Schema", type=relational_Type, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
keyOf5: BinaryAssociation = BinaryAssociation(
    name="keyOf5",
    ends={
        Property(name="Table6", type=relational_Column, multiplicity=Multiplicity(1, 1)),
        Property(name="key", type=relational_Table, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_relational_Table_Named = Generalization(general=Named, specific=relational_Table)
gen_relational_Column_Named = Generalization(general=Named, specific=relational_Column)
gen_relational_Type_Named = Generalization(general=Named, specific=relational_Type)
gen_relational_Schema_Named = Generalization(general=Named, specific=relational_Schema)

# Domain Model
domain_model = DomainModel(
    name="relational",
    types={relational_Named, relational_Table, Named, relational_Schema, relational_Column, relational_Type},
    associations={key1, owner3, owner4, col0, type7, tables8, types11, keyOf5},
    generalizations={gen_relational_Table_Named, gen_relational_Column_Named, gen_relational_Type_Named, gen_relational_Schema_Named},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)