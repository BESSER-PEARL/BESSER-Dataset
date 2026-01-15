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
trees_Node = Class(name="trees::Node")

# trees_Node class attributes and methods
trees_Node_m_next: Method = Method(name="next", parameters={}, type=StringType)
trees_Node_m_hasNext: Method = Method(name="hasNext", parameters={}, type=BooleanType)
trees_Node.methods={trees_Node_m_hasNext, trees_Node_m_next}

# Relationships
children1: BinaryAssociation = BinaryAssociation(
    name="children1",
    ends={
        Property(name="trees_Node", type=trees_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="trees_Node0", type=trees_Node, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="trees",
    types={trees_Node},
    associations={children1},
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