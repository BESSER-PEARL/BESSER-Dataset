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
kiamacs_TopCS = Class(name="kiamacs::TopCS")
BaseCS = Class(name="BaseCS")
kiamacs_NodeCS = Class(name="kiamacs::NodeCS", is_abstract=True)
kiamacs_PlusCS = Class(name="kiamacs::PlusCS")
NodeCS = Class(name="NodeCS")
kiamacs_NumCS = Class(name="kiamacs::NumCS")
kiamacs_BaseCS = Class(name="kiamacs::BaseCS", is_abstract=True)
kiamacs_EObject = Class(name="kiamacs::EObject")

# kiamacs_TopCS class attributes and methods

# BaseCS class attributes and methods

# kiamacs_NodeCS class attributes and methods

# kiamacs_PlusCS class attributes and methods

# NodeCS class attributes and methods

# kiamacs_NumCS class attributes and methods
kiamacs_NumCS_value: Property = Property(name="value", type=IntegerType)
kiamacs_NumCS.attributes={kiamacs_NumCS_value}

# kiamacs_BaseCS class attributes and methods

# kiamacs_EObject class attributes and methods

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
        Property(name="kiamacs_PlusCS", type=kiamacs_NodeCS, multiplicity=Multiplicity(0, 1), is_composite=True),
        Property(name="kiamacs_NodeCS2", type=kiamacs_PlusCS, multiplicity=Multiplicity(1, 1))
    }
)
right3: BinaryAssociation = BinaryAssociation(
    name="right3",
    ends={
        Property(name="kiamacs_NodeCS5", type=kiamacs_PlusCS, multiplicity=Multiplicity(1, 1)),
        Property(name="kiamacs_PlusCS4", type=kiamacs_NodeCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ast6: BinaryAssociation = BinaryAssociation(
    name="ast6",
    ends={
        Property(name="kiamacs_EObject", type=kiamacs_BaseCS, multiplicity=Multiplicity(1, 1)),
        Property(name="kiamacs_BaseCS", type=kiamacs_EObject, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_kiamacs_TopCS_BaseCS = Generalization(general=BaseCS, specific=kiamacs_TopCS)
gen_kiamacs_NodeCS_BaseCS = Generalization(general=BaseCS, specific=kiamacs_NodeCS)
gen_kiamacs_NumCS_NodeCS = Generalization(general=NodeCS, specific=kiamacs_NumCS)
gen_kiamacs_PlusCS_NodeCS = Generalization(general=NodeCS, specific=kiamacs_PlusCS)

# Domain Model
domain_model = DomainModel(
    name="kiamacs",
    types={kiamacs_TopCS, BaseCS, kiamacs_NodeCS, kiamacs_PlusCS, NodeCS, kiamacs_NumCS, kiamacs_BaseCS, kiamacs_EObject},
    associations={node0, left1, right3, ast6},
    generalizations={gen_kiamacs_TopCS_BaseCS, gen_kiamacs_NodeCS_BaseCS, gen_kiamacs_NumCS_NodeCS, gen_kiamacs_PlusCS_NodeCS},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)