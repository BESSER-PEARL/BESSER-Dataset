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
kiamacs_EObject = Class(name="kiamacs::EObject")
kiamacs_CompositeCS = Class(name="kiamacs::CompositeCS")
NodeCS = Class(name="NodeCS")
kiamacs_LeafCS = Class(name="kiamacs::LeafCS")
kiamacs_BaseCS = Class(name="kiamacs::BaseCS", is_abstract=True)

# kiamacs_TopCS class attributes and methods

# BaseCS class attributes and methods

# kiamacs_NodeCS class attributes and methods

# kiamacs_EObject class attributes and methods

# kiamacs_CompositeCS class attributes and methods

# NodeCS class attributes and methods

# kiamacs_LeafCS class attributes and methods

# kiamacs_BaseCS class attributes and methods

# Relationships
ast3: BinaryAssociation = BinaryAssociation(
    name="ast3",
    ends={
        Property(name="kiamacs_EObject", type=kiamacs_BaseCS, multiplicity=Multiplicity(1, 1)),
        Property(name="kiamacs_BaseCS", type=kiamacs_EObject, multiplicity=Multiplicity(0, 1))
    }
)
node0: BinaryAssociation = BinaryAssociation(
    name="node0",
    ends={
        Property(name="kiamacs_NodeCS", type=kiamacs_TopCS, multiplicity=Multiplicity(1, 1)),
        Property(name="kiamacs_TopCS", type=kiamacs_NodeCS, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
child1: BinaryAssociation = BinaryAssociation(
    name="child1",
    ends={
        Property(name="kiamacs_NodeCS2", type=kiamacs_CompositeCS, multiplicity=Multiplicity(1, 1)),
        Property(name="kiamacs_CompositeCS", type=kiamacs_NodeCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_kiamacs_TopCS_BaseCS = Generalization(general=BaseCS, specific=kiamacs_TopCS)
gen_kiamacs_NodeCS_BaseCS = Generalization(general=BaseCS, specific=kiamacs_NodeCS)
gen_kiamacs_CompositeCS_NodeCS = Generalization(general=NodeCS, specific=kiamacs_CompositeCS)
gen_kiamacs_LeafCS_NodeCS = Generalization(general=NodeCS, specific=kiamacs_LeafCS)

# Domain Model
domain_model = DomainModel(
    name="kiamacs",
    types={kiamacs_TopCS, BaseCS, kiamacs_NodeCS, kiamacs_EObject, kiamacs_CompositeCS, NodeCS, kiamacs_LeafCS, kiamacs_BaseCS},
    associations={ast3, node0, child1},
    generalizations={gen_kiamacs_TopCS_BaseCS, gen_kiamacs_NodeCS_BaseCS, gen_kiamacs_CompositeCS_NodeCS, gen_kiamacs_LeafCS_NodeCS},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)