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
graphgenerators_GraphGenerator = Class(name="graphgenerators_GraphGenerator", is_abstract=True)
Identifiable = Class(name="Identifiable")
graphgenerators_LatticeGraphGenerator = Class(name="graphgenerators_LatticeGraphGenerator", is_abstract=True)
GraphGenerator = Class(name="GraphGenerator")
graphgenerators_SquareLatticeGraphGenerator = Class(name="graphgenerators_SquareLatticeGraphGenerator")
LatticeGraphGenerator = Class(name="LatticeGraphGenerator")
graphgenerators_MigrationEdgeGraphGenerator = Class(name="graphgenerators_MigrationEdgeGraphGenerator")
graphgenerators_PlateCarreeGlobeGraphGenerator = Class(name="graphgenerators_PlateCarreeGlobeGraphGenerator")
graphgenerators_PajekNetGraphGenerator = Class(name="graphgenerators_PajekNetGraphGenerator")

# graphgenerators_GraphGenerator class attributes and methods
graphgenerators_GraphGenerator_m_getGraph: Method = Method(name="getGraph", parameters={}, type=StringType)
graphgenerators_GraphGenerator.methods={graphgenerators_GraphGenerator_m_getGraph}

# Identifiable class attributes and methods

# graphgenerators_LatticeGraphGenerator class attributes and methods
graphgenerators_LatticeGraphGenerator_useNearestNeighbors: Property = Property(name="useNearestNeighbors", type=BooleanType)
graphgenerators_LatticeGraphGenerator_useNextNearestNeighbors: Property = Property(name="useNextNearestNeighbors", type=BooleanType)
graphgenerators_LatticeGraphGenerator_periodicBoundaries: Property = Property(name="periodicBoundaries", type=BooleanType)
graphgenerators_LatticeGraphGenerator.attributes={graphgenerators_LatticeGraphGenerator_useNearestNeighbors, graphgenerators_LatticeGraphGenerator_periodicBoundaries, graphgenerators_LatticeGraphGenerator_useNextNearestNeighbors}

# GraphGenerator class attributes and methods

# graphgenerators_SquareLatticeGraphGenerator class attributes and methods
graphgenerators_SquareLatticeGraphGenerator_xSize: Property = Property(name="xSize", type=IntegerType)
graphgenerators_SquareLatticeGraphGenerator_ySize: Property = Property(name="ySize", type=IntegerType)
graphgenerators_SquareLatticeGraphGenerator_area: Property = Property(name="area", type=FloatType)
graphgenerators_SquareLatticeGraphGenerator.attributes={graphgenerators_SquareLatticeGraphGenerator_xSize, graphgenerators_SquareLatticeGraphGenerator_ySize, graphgenerators_SquareLatticeGraphGenerator_area}

# LatticeGraphGenerator class attributes and methods

# graphgenerators_MigrationEdgeGraphGenerator class attributes and methods
graphgenerators_MigrationEdgeGraphGenerator_location: Property = Property(name="location", type=StringType)
graphgenerators_MigrationEdgeGraphGenerator_migrationRate: Property = Property(name="migrationRate", type=FloatType)
graphgenerators_MigrationEdgeGraphGenerator_population: Property = Property(name="population", type=StringType)
graphgenerators_MigrationEdgeGraphGenerator.attributes={graphgenerators_MigrationEdgeGraphGenerator_population, graphgenerators_MigrationEdgeGraphGenerator_migrationRate, graphgenerators_MigrationEdgeGraphGenerator_location}

# graphgenerators_PlateCarreeGlobeGraphGenerator class attributes and methods
graphgenerators_PlateCarreeGlobeGraphGenerator_angularStep: Property = Property(name="angularStep", type=IntegerType)
graphgenerators_PlateCarreeGlobeGraphGenerator_radius: Property = Property(name="radius", type=FloatType)
graphgenerators_PlateCarreeGlobeGraphGenerator.attributes={graphgenerators_PlateCarreeGlobeGraphGenerator_angularStep, graphgenerators_PlateCarreeGlobeGraphGenerator_radius}

# graphgenerators_PajekNetGraphGenerator class attributes and methods
graphgenerators_PajekNetGraphGenerator_dataFile_net: Property = Property(name="dataFile_net", type=StringType)
graphgenerators_PajekNetGraphGenerator_area: Property = Property(name="area", type=FloatType)
graphgenerators_PajekNetGraphGenerator_zoomFactor: Property = Property(name="zoomFactor", type=IntegerType)
graphgenerators_PajekNetGraphGenerator_colArea: Property = Property(name="colArea", type=IntegerType)
graphgenerators_PajekNetGraphGenerator.attributes={graphgenerators_PajekNetGraphGenerator_colArea, graphgenerators_PajekNetGraphGenerator_zoomFactor, graphgenerators_PajekNetGraphGenerator_dataFile_net, graphgenerators_PajekNetGraphGenerator_area}

# Generalizations
gen_graphgenerators_GraphGenerator_Identifiable = Generalization(general=Identifiable, specific=graphgenerators_GraphGenerator)
gen_graphgenerators_LatticeGraphGenerator_GraphGenerator = Generalization(general=GraphGenerator, specific=graphgenerators_LatticeGraphGenerator)
gen_graphgenerators_SquareLatticeGraphGenerator_LatticeGraphGenerator = Generalization(general=LatticeGraphGenerator, specific=graphgenerators_SquareLatticeGraphGenerator)
gen_graphgenerators_MigrationEdgeGraphGenerator_GraphGenerator = Generalization(general=GraphGenerator, specific=graphgenerators_MigrationEdgeGraphGenerator)
gen_graphgenerators_PlateCarreeGlobeGraphGenerator_LatticeGraphGenerator = Generalization(general=LatticeGraphGenerator, specific=graphgenerators_PlateCarreeGlobeGraphGenerator)
gen_graphgenerators_PajekNetGraphGenerator_GraphGenerator = Generalization(general=GraphGenerator, specific=graphgenerators_PajekNetGraphGenerator)

# Domain Model
domain_model = DomainModel(
    name="graphgenerators",
    types={graphgenerators_GraphGenerator, Identifiable, graphgenerators_LatticeGraphGenerator, GraphGenerator, graphgenerators_SquareLatticeGraphGenerator, LatticeGraphGenerator, graphgenerators_MigrationEdgeGraphGenerator, graphgenerators_PlateCarreeGlobeGraphGenerator, graphgenerators_PajekNetGraphGenerator},
    associations={},
    generalizations={gen_graphgenerators_GraphGenerator_Identifiable, gen_graphgenerators_LatticeGraphGenerator_GraphGenerator, gen_graphgenerators_SquareLatticeGraphGenerator_LatticeGraphGenerator, gen_graphgenerators_MigrationEdgeGraphGenerator_GraphGenerator, gen_graphgenerators_PlateCarreeGlobeGraphGenerator_LatticeGraphGenerator, gen_graphgenerators_PajekNetGraphGenerator_GraphGenerator},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)