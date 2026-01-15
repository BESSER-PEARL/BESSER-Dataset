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
TableM_Table = Class(name="TableM::Table")
TableM_Column = Class(name="TableM::Column")
TableM_FKey = Class(name="TableM::FKey")

# TableM_Table class attributes and methods
TableM_Table_name: Property = Property(name="name", type=StringType)
TableM_Table.attributes={TableM_Table_name}

# TableM_Column class attributes and methods
TableM_Column_name: Property = Property(name="name", type=StringType)
TableM_Column_type: Property = Property(name="type", type=StringType)
TableM_Column.attributes={TableM_Column_type, TableM_Column_name}

# TableM_FKey class attributes and methods

# Relationships
referencedBy4: BinaryAssociation = BinaryAssociation(
    name="referencedBy4",
    ends={
        Property(name="TableM_FKey", type=TableM_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="TableM_Table5", type=TableM_FKey, multiplicity=Multiplicity(0, 9999))
    }
)
owner6: BinaryAssociation = BinaryAssociation(
    name="owner6",
    ends={
        Property(name="Table", type=TableM_Column, multiplicity=Multiplicity(1, 1)),
        Property(name="cols", type=TableM_Table, multiplicity=Multiplicity(0, 1))
    }
)
cols0: BinaryAssociation = BinaryAssociation(
    name="cols0",
    ends={
        Property(name="Column", type=TableM_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="owner", type=TableM_Column, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
pkeys1: BinaryAssociation = BinaryAssociation(
    name="pkeys1",
    ends={
        Property(name="TableM_Column", type=TableM_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="TableM_Table", type=TableM_Column, multiplicity=Multiplicity(0, 9999))
    }
)
fkeys2: BinaryAssociation = BinaryAssociation(
    name="fkeys2",
    ends={
        Property(name="FKey", type=TableM_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="owner3", type=TableM_FKey, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
cols12: BinaryAssociation = BinaryAssociation(
    name="cols12",
    ends={
        Property(name="TableM_Column14", type=TableM_FKey, multiplicity=Multiplicity(1, 1)),
        Property(name="TableM_FKey13", type=TableM_Column, multiplicity=Multiplicity(0, 9999))
    }
)
references7: BinaryAssociation = BinaryAssociation(
    name="references7",
    ends={
        Property(name="TableM_Table9", type=TableM_FKey, multiplicity=Multiplicity(1, 1)),
        Property(name="TableM_FKey8", type=TableM_Table, multiplicity=Multiplicity(0, 1))
    }
)
owner10: BinaryAssociation = BinaryAssociation(
    name="owner10",
    ends={
        Property(name="Table11", type=TableM_FKey, multiplicity=Multiplicity(1, 1)),
        Property(name="fkeys", type=TableM_Table, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="TableM",
    types={TableM_Table, TableM_Column, TableM_FKey},
    associations={referencedBy4, owner6, cols0, pkeys1, fkeys2, cols12, references7, owner10},
    generalizations={},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)