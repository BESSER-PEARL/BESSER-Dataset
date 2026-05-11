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
traceability_NamedEntity = Class(name="traceability_NamedEntity")
traceability_EDFDToGraph = Class(name="traceability_EDFDToGraph")
traceability_EDFDGraphTrace = Class(name="traceability_EDFDGraphTrace")
traceability_EDFD = Class(name="traceability_EDFD")
traceability_Graph = Class(name="traceability_Graph")
traceability_GraphEndToEndTrace = Class(name="traceability_GraphEndToEndTrace")
traceability_Identifiable = Class(name="traceability_Identifiable")

# traceability_NamedEntity class attributes and methods

# traceability_EDFDToGraph class attributes and methods

# traceability_EDFDGraphTrace class attributes and methods

# traceability_EDFD class attributes and methods

# traceability_Graph class attributes and methods

# traceability_GraphEndToEndTrace class attributes and methods

# traceability_Identifiable class attributes and methods

# Relationships
edfdElements10: BinaryAssociation = BinaryAssociation(
    name="edfdElements10",
    ends={
        Property(name="traceability_NamedEntity", type=traceability_EDFDGraphTrace, multiplicity=Multiplicity(1, 1)),
        Property(name="traceability_EDFDGraphTrace11", type=traceability_NamedEntity, multiplicity=Multiplicity(0, 9999))
    }
)
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
graphElements17: BinaryAssociation = BinaryAssociation(
    name="graphElements17",
    ends={
        Property(name="traceability_Identifiable19", type=traceability_GraphEndToEndTrace, multiplicity=Multiplicity(1, 1)),
        Property(name="traceability_GraphEndToEndTrace18", type=traceability_Identifiable, multiplicity=Multiplicity(0, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="traceability",
    types={traceability_NamedEntity, traceability_EDFDToGraph, traceability_EDFDGraphTrace, traceability_EDFD, traceability_Graph, traceability_GraphEndToEndTrace, traceability_Identifiable},
    associations={edfdElements10, edfdGraphTraces0, edfds1, graphs3, endtoendgraph5, graphEndToEndTrace8, graphElements12, endtoendGraphElements14, graphElements17},
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