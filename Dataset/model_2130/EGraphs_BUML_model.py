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
egraphs_EGraph = Class(name="egraphs::EGraph")
egraphs_ENode = Class(name="egraphs::ENode")
egraphs_EHyperEdge = Class(name="egraphs::EHyperEdge")

# egraphs_EGraph class attributes and methods

# egraphs_ENode class attributes and methods
egraphs_ENode_element: Property = Property(name="element", type=StringType)
egraphs_ENode.attributes={egraphs_ENode_element}

# egraphs_EHyperEdge class attributes and methods
egraphs_EHyperEdge_label: Property = Property(name="label", type=StringType)
egraphs_EHyperEdge.attributes={egraphs_EHyperEdge_label}

# Relationships
contents0: BinaryAssociation = BinaryAssociation(
    name="contents0",
    ends={
        Property(name="egraphs_ENode", type=egraphs_EGraph, multiplicity=Multiplicity(1, 1)),
        Property(name="egraphs_EGraph", type=egraphs_ENode, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
outgoing1: BinaryAssociation = BinaryAssociation(
    name="outgoing1",
    ends={
        Property(name="EHyperEdge", type=egraphs_ENode, multiplicity=Multiplicity(1, 1)),
        Property(name="source", type=egraphs_EHyperEdge, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
incoming2: BinaryAssociation = BinaryAssociation(
    name="incoming2",
    ends={
        Property(name="EHyperEdge3", type=egraphs_ENode, multiplicity=Multiplicity(1, 1)),
        Property(name="targets", type=egraphs_EHyperEdge, multiplicity=Multiplicity(0, 9999))
    }
)
source4: BinaryAssociation = BinaryAssociation(
    name="source4",
    ends={
        Property(name="ENode", type=egraphs_EHyperEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoing", type=egraphs_ENode, multiplicity=Multiplicity(1, 1))
    }
)
targets5: BinaryAssociation = BinaryAssociation(
    name="targets5",
    ends={
        Property(name="ENode6", type=egraphs_EHyperEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="incoming", type=egraphs_ENode, multiplicity=Multiplicity(0, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="egraphs",
    types={egraphs_EGraph, egraphs_ENode, egraphs_EHyperEdge},
    associations={contents0, outgoing1, incoming2, source4, targets5},
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