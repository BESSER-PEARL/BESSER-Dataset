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
kiamacs_NodeCS = Class(name="kiamacs::NodeCS", is_abstract=True)
kiamacs_TopCS = Class(name="kiamacs::TopCS")
kiamacs_NumCS = Class(name="kiamacs::NumCS")
kiamacs_PlusCS = Class(name="kiamacs::PlusCS")
NodeCS = Class(name="NodeCS")

# kiamacs_NodeCS class attributes and methods

# kiamacs_TopCS class attributes and methods

# kiamacs_NumCS class attributes and methods
kiamacs_NumCS_value: Property = Property(name="value", type=IntegerType)
kiamacs_NumCS.attributes={kiamacs_NumCS_value}

# kiamacs_PlusCS class attributes and methods

# NodeCS class attributes and methods

# Relationships
node0: BinaryAssociation = BinaryAssociation(
    name="node0",
    ends={
        Property(name="kiamacs_NodeCS", type=kiamacs_TopCS, multiplicity=Multiplicity(1, 1)),
        Property(name="kiamacs_TopCS", type=kiamacs_NodeCS, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
left1: BinaryAssociation = BinaryAssociation(
    name="left1",
    ends={
        Property(name="kiamacs_NodeCS2", type=kiamacs_PlusCS, multiplicity=Multiplicity(1, 1)),
        Property(name="kiamacs_PlusCS", type=kiamacs_NodeCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right3: BinaryAssociation = BinaryAssociation(
    name="right3",
    ends={
        Property(name="kiamacs_NodeCS5", type=kiamacs_PlusCS, multiplicity=Multiplicity(1, 1)),
        Property(name="kiamacs_PlusCS4", type=kiamacs_NodeCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_kiamacs_NumCS_NodeCS = Generalization(general=NodeCS, specific=kiamacs_NumCS)
gen_kiamacs_PlusCS_NodeCS = Generalization(general=NodeCS, specific=kiamacs_PlusCS)

# Domain Model
domain_model = DomainModel(
    name="kiamacs",
    types={kiamacs_NodeCS, kiamacs_TopCS, kiamacs_NumCS, kiamacs_PlusCS, NodeCS},
    associations={node0, left1, right3},
    generalizations={gen_kiamacs_NumCS_NodeCS, gen_kiamacs_PlusCS_NodeCS},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)