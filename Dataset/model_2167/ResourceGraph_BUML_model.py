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

# Enumerations
FitPolicy: Enumeration = Enumeration(
    name="FitPolicy",
    literals={
            EnumerationLiteral(name="AUTO"),
			EnumerationLiteral(name="CUSTOM")
    }
)

# Classes
graph_ResourceGraph = Class(name="graph::ResourceGraph")
graph_ResourcePlot = Class(name="graph::ResourcePlot")
graph_ResourceGraphs = Class(name="graph::ResourceGraphs")

# graph_ResourceGraph class attributes and methods
graph_ResourceGraph_name: Property = Property(name="name", type=StringType)
graph_ResourceGraph.attributes={graph_ResourceGraph_name}

# graph_ResourcePlot class attributes and methods
graph_ResourcePlot_name: Property = Property(name="name", type=StringType)
graph_ResourcePlot_rgb: Property = Property(name="rgb", type=StringType)
graph_ResourcePlot_fit: Property = Property(name="fit", type=StringType)
graph_ResourcePlot_min: Property = Property(name="min", type=FloatType)
graph_ResourcePlot_max: Property = Property(name="max", type=FloatType)
graph_ResourcePlot.attributes={graph_ResourcePlot_max, graph_ResourcePlot_rgb, graph_ResourcePlot_min, graph_ResourcePlot_fit, graph_ResourcePlot_name}

# graph_ResourceGraphs class attributes and methods

# Relationships
graphs0: BinaryAssociation = BinaryAssociation(
    name="graphs0",
    ends={
        Property(name="graph_ResourceGraph", type=graph_ResourceGraphs, multiplicity=Multiplicity(1, 1)),
        Property(name="graph_ResourceGraphs", type=graph_ResourceGraph, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
plots1: BinaryAssociation = BinaryAssociation(
    name="plots1",
    ends={
        Property(name="graph_ResourcePlot", type=graph_ResourceGraph, multiplicity=Multiplicity(1, 1)),
        Property(name="graph_ResourceGraph2", type=graph_ResourcePlot, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="graph",
    types={graph_ResourceGraph, graph_ResourcePlot, graph_ResourceGraphs, FitPolicy},
    associations={graphs0, plots1},
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