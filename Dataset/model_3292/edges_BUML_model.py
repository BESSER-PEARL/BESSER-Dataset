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
edges_MigrationEdge = Class(name="edges::MigrationEdge")
PopulationEdge = Class(name="PopulationEdge")
edges_MigrationEdgeLabel = Class(name="edges::MigrationEdgeLabel")
EdgeLabel = Class(name="EdgeLabel")
edges_MigrationEdgeLabelValue = Class(name="edges::MigrationEdgeLabelValue")
LabelValue = Class(name="LabelValue")
edges_MixingEdge = Class(name="edges::MixingEdge")
edges_MixingEdgeLabel = Class(name="edges::MixingEdgeLabel")
edges_MixingEdgeLabelValue = Class(name="edges::MixingEdgeLabelValue")
edges_PopulationEdge = Class(name="edges::PopulationEdge")
Edge = Class(name="Edge")

# edges_MigrationEdge class attributes and methods

# PopulationEdge class attributes and methods

# edges_MigrationEdgeLabel class attributes and methods

# EdgeLabel class attributes and methods

# edges_MigrationEdgeLabelValue class attributes and methods
edges_MigrationEdgeLabelValue_migrationRate: Property = Property(name="migrationRate", type=FloatType)
edges_MigrationEdgeLabelValue.attributes={edges_MigrationEdgeLabelValue_migrationRate}

# LabelValue class attributes and methods

# edges_MixingEdge class attributes and methods

# edges_MixingEdgeLabel class attributes and methods

# edges_MixingEdgeLabelValue class attributes and methods
edges_MixingEdgeLabelValue_mixingRate: Property = Property(name="mixingRate", type=FloatType)
edges_MixingEdgeLabelValue.attributes={edges_MixingEdgeLabelValue_mixingRate}

# edges_PopulationEdge class attributes and methods
edges_PopulationEdge_populationIdentifier: Property = Property(name="populationIdentifier", type=StringType)
edges_PopulationEdge.attributes={edges_PopulationEdge_populationIdentifier}

# Edge class attributes and methods

# Generalizations
gen_edges_MigrationEdge_PopulationEdge = Generalization(general=PopulationEdge, specific=edges_MigrationEdge)
gen_edges_MigrationEdgeLabel_EdgeLabel = Generalization(general=EdgeLabel, specific=edges_MigrationEdgeLabel)
gen_edges_MigrationEdgeLabelValue_LabelValue = Generalization(general=LabelValue, specific=edges_MigrationEdgeLabelValue)
gen_edges_MixingEdge_PopulationEdge = Generalization(general=PopulationEdge, specific=edges_MixingEdge)
gen_edges_MixingEdgeLabel_EdgeLabel = Generalization(general=EdgeLabel, specific=edges_MixingEdgeLabel)
gen_edges_MixingEdgeLabelValue_LabelValue = Generalization(general=LabelValue, specific=edges_MixingEdgeLabelValue)
gen_edges_PopulationEdge_Edge = Generalization(general=Edge, specific=edges_PopulationEdge)

# Domain Model
domain_model = DomainModel(
    name="edges",
    types={edges_MigrationEdge, PopulationEdge, edges_MigrationEdgeLabel, EdgeLabel, edges_MigrationEdgeLabelValue, LabelValue, edges_MixingEdge, edges_MixingEdgeLabel, edges_MixingEdgeLabelValue, edges_PopulationEdge, Edge},
    associations={},
    generalizations={gen_edges_MigrationEdge_PopulationEdge, gen_edges_MigrationEdgeLabel_EdgeLabel, gen_edges_MigrationEdgeLabelValue_LabelValue, gen_edges_MixingEdge_PopulationEdge, gen_edges_MixingEdgeLabel_EdgeLabel, gen_edges_MixingEdgeLabelValue_LabelValue, gen_edges_PopulationEdge_Edge},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)