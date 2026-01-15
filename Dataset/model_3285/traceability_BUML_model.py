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
traceability_EDFDToGraph = Class(name="traceability::EDFDToGraph")
traceability_EDFDGraphTrace = Class(name="traceability::EDFDGraphTrace")
traceability_EDFD = Class(name="traceability::EDFD")
traceability_Graph = Class(name="traceability::Graph")
traceability_GraphEndToEndTrace = Class(name="traceability::GraphEndToEndTrace")
traceability_NamedEntity = Class(name="traceability::NamedEntity")
traceability_Identifiable = Class(name="traceability::Identifiable")

# traceability_EDFDToGraph class attributes and methods

# traceability_EDFDGraphTrace class attributes and methods

# traceability_EDFD class attributes and methods

# traceability_Graph class attributes and methods

# traceability_GraphEndToEndTrace class attributes and methods

# traceability_NamedEntity class attributes and methods

# traceability_Identifiable class attributes and methods

# Relationships
edfdGraphTraces0: BinaryAssociation = BinaryAssociation(
    name="edfdGraphTraces0",
    ends={
        Property(name="traceability_EDFDGraphTrace", type=traceability_EDFDToGraph, multiplicity=Multiplicity(1, 1)),
        Property(name="traceability_EDFDToGraph", type=traceability_EDFDGraphTrace, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
edfds1: BinaryAssociation = BinaryAssociation(
    name="edfds1",
    ends={
        Property(name="traceability_EDFD", type=traceability_EDFDToGraph, multiplicity=Multiplicity(1, 1)),
        Property(name="traceability_EDFDToGraph2", type=traceability_EDFD, multiplicity=Multiplicity(0, 1))
    }
)
graphs3: BinaryAssociation = BinaryAssociation(
    name="graphs3",
    ends={
        Property(name="traceability_Graph", type=traceability_EDFDToGraph, multiplicity=Multiplicity(1, 1)),
        Property(name="traceability_EDFDToGraph4", type=traceability_Graph, multiplicity=Multiplicity(0, 1))
    }
)
endtoendgraph5: BinaryAssociation = BinaryAssociation(
    name="endtoendgraph5",
    ends={
        Property(name="traceability_Graph7", type=traceability_EDFDToGraph, multiplicity=Multiplicity(1, 1)),
        Property(name="traceability_EDFDToGraph6", type=traceability_Graph, multiplicity=Multiplicity(0, 1))
    }
)
graphEndToEndTrace8: BinaryAssociation = BinaryAssociation(
    name="graphEndToEndTrace8",
    ends={
        Property(name="traceability_GraphEndToEndTrace", type=traceability_EDFDToGraph, multiplicity=Multiplicity(1, 1)),
        Property(name="traceability_EDFDToGraph9", type=traceability_GraphEndToEndTrace, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
graphElements17: BinaryAssociation = BinaryAssociation(
    name="graphElements17",
    ends={
        Property(name="traceability_Identifiable19", type=traceability_GraphEndToEndTrace, multiplicity=Multiplicity(1, 1)),
        Property(name="traceability_GraphEndToEndTrace18", type=traceability_Identifiable, multiplicity=Multiplicity(0, 9999))
    }
)
edfdElements10: BinaryAssociation = BinaryAssociation(
    name="edfdElements10",
    ends={
        Property(name="traceability_NamedEntity", type=traceability_EDFDGraphTrace, multiplicity=Multiplicity(1, 1)),
        Property(name="traceability_EDFDGraphTrace11", type=traceability_NamedEntity, multiplicity=Multiplicity(0, 9999))
    }
)
graphElements12: BinaryAssociation = BinaryAssociation(
    name="graphElements12",
    ends={
        Property(name="traceability_Identifiable", type=traceability_EDFDGraphTrace, multiplicity=Multiplicity(1, 1)),
        Property(name="traceability_EDFDGraphTrace13", type=traceability_Identifiable, multiplicity=Multiplicity(0, 9999))
    }
)
endtoendGraphElements14: BinaryAssociation = BinaryAssociation(
    name="endtoendGraphElements14",
    ends={
        Property(name="traceability_Identifiable16", type=traceability_GraphEndToEndTrace, multiplicity=Multiplicity(1, 1)),
        Property(name="traceability_GraphEndToEndTrace15", type=traceability_Identifiable, multiplicity=Multiplicity(0, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="traceability",
    types={traceability_EDFDToGraph, traceability_EDFDGraphTrace, traceability_EDFD, traceability_Graph, traceability_GraphEndToEndTrace, traceability_NamedEntity, traceability_Identifiable},
    associations={edfdGraphTraces0, edfds1, graphs3, endtoendgraph5, graphEndToEndTrace8, graphElements17, edfdElements10, graphElements12, endtoendGraphElements14},
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