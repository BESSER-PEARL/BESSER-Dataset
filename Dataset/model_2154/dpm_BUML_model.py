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
dfg_DfgGraph = Class(name="dfg::DfgGraph")
dfg_DfgVertex = Class(name="dfg::DfgVertex")
dfg_DfgEdge = Class(name="dfg::DfgEdge")

# dfg_DfgGraph class attributes and methods

# dfg_DfgVertex class attributes and methods
dfg_DfgVertex_mappings: Property = Property(name="mappings", type=StringType)
dfg_DfgVertex.attributes={dfg_DfgVertex_mappings}

# dfg_DfgEdge class attributes and methods
dfg_DfgEdge_label: Property = Property(name="label", type=StringType)
dfg_DfgEdge.attributes={dfg_DfgEdge_label}

# Relationships
neighbors4: BinaryAssociation = BinaryAssociation(
    name="neighbors4",
    ends={
        Property(name="dfg_DfgVertex5", type=dfg_DfgVertex, multiplicity=Multiplicity(1, 1)),
        Property(name="dfg_DfgVertex3", type=dfg_DfgVertex, multiplicity=Multiplicity(0, 9999))
    }
)
connecting6: BinaryAssociation = BinaryAssociation(
    name="connecting6",
    ends={
        Property(name="dfg_DfgEdge8", type=dfg_DfgVertex, multiplicity=Multiplicity(1, 1)),
        Property(name="dfg_DfgVertex7", type=dfg_DfgEdge, multiplicity=Multiplicity(0, 9999))
    }
)
vertices0: BinaryAssociation = BinaryAssociation(
    name="vertices0",
    ends={
        Property(name="dfg_DfgVertex", type=dfg_DfgGraph, multiplicity=Multiplicity(1, 1)),
        Property(name="dfg_DfgGraph", type=dfg_DfgVertex, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
edges1: BinaryAssociation = BinaryAssociation(
    name="edges1",
    ends={
        Property(name="dfg_DfgEdge", type=dfg_DfgGraph, multiplicity=Multiplicity(1, 1)),
        Property(name="dfg_DfgGraph2", type=dfg_DfgEdge, multiplicity=Multiplicity(0, 9999))
    }
)
vertex19: BinaryAssociation = BinaryAssociation(
    name="vertex19",
    ends={
        Property(name="dfg_DfgVertex11", type=dfg_DfgEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="dfg_DfgEdge10", type=dfg_DfgVertex, multiplicity=Multiplicity(0, 1))
    }
)
vertex212: BinaryAssociation = BinaryAssociation(
    name="vertex212",
    ends={
        Property(name="dfg_DfgVertex14", type=dfg_DfgEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="dfg_DfgEdge13", type=dfg_DfgVertex, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="dfg",
    types={dfg_DfgGraph, dfg_DfgVertex, dfg_DfgEdge},
    associations={neighbors4, connecting6, vertices0, edges1, vertex19, vertex212},
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