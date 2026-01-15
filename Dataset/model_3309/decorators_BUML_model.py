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
decorators_TestGraphDecorator1 = Class(name="decorators::TestGraphDecorator1")
GraphDecorator = Class(name="GraphDecorator")
decorators_TestNodeDecorator1 = Class(name="decorators::TestNodeDecorator1")
NodeDecorator = Class(name="NodeDecorator")
decorators_TestScenarioGraphDecorator1 = Class(name="decorators::TestScenarioGraphDecorator1")
decorators_STEMTime = Class(name="decorators::STEMTime")
decorators_EdgeDecorator = Class(name="decorators::EdgeDecorator", is_abstract=True)
decorators_GraphDecorator = Class(name="decorators::GraphDecorator", is_abstract=True)
decorators_NodeDecorator = Class(name="decorators::NodeDecorator", is_abstract=True)
decorators_TestEdgeDecorator1 = Class(name="decorators::TestEdgeDecorator1")
EdgeDecorator = Class(name="EdgeDecorator")

# decorators_TestGraphDecorator1 class attributes and methods

# GraphDecorator class attributes and methods

# decorators_TestNodeDecorator1 class attributes and methods

# NodeDecorator class attributes and methods

# decorators_TestScenarioGraphDecorator1 class attributes and methods
decorators_TestScenarioGraphDecorator1_doubleValue: Property = Property(name="doubleValue", type=FloatType)
decorators_TestScenarioGraphDecorator1_intValue: Property = Property(name="intValue", type=IntegerType)
decorators_TestScenarioGraphDecorator1_stringValue: Property = Property(name="stringValue", type=StringType)
decorators_TestScenarioGraphDecorator1_booleanValue: Property = Property(name="booleanValue", type=BooleanType)
decorators_TestScenarioGraphDecorator1.attributes={decorators_TestScenarioGraphDecorator1_stringValue, decorators_TestScenarioGraphDecorator1_doubleValue, decorators_TestScenarioGraphDecorator1_intValue, decorators_TestScenarioGraphDecorator1_booleanValue}

# decorators_STEMTime class attributes and methods

# decorators_EdgeDecorator class attributes and methods

# decorators_GraphDecorator class attributes and methods

# decorators_NodeDecorator class attributes and methods

# decorators_TestEdgeDecorator1 class attributes and methods
decorators_TestEdgeDecorator1_nodeAURI: Property = Property(name="nodeAURI", type=StringType)
decorators_TestEdgeDecorator1_nodeBURI: Property = Property(name="nodeBURI", type=StringType)
decorators_TestEdgeDecorator1_edgeURI: Property = Property(name="edgeURI", type=StringType)
decorators_TestEdgeDecorator1.attributes={decorators_TestEdgeDecorator1_nodeAURI, decorators_TestEdgeDecorator1_nodeBURI, decorators_TestEdgeDecorator1_edgeURI}

# EdgeDecorator class attributes and methods

# Relationships
sTEMTimeValue0: BinaryAssociation = BinaryAssociation(
    name="sTEMTimeValue0",
    ends={
        Property(name="decorators_STEMTime", type=decorators_TestScenarioGraphDecorator1, multiplicity=Multiplicity(1, 1)),
        Property(name="decorators_TestScenarioGraphDecorator1", type=decorators_STEMTime, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_decorators_TestGraphDecorator1_GraphDecorator = Generalization(general=GraphDecorator, specific=decorators_TestGraphDecorator1)
gen_decorators_TestNodeDecorator1_NodeDecorator = Generalization(general=NodeDecorator, specific=decorators_TestNodeDecorator1)
gen_decorators_TestScenarioGraphDecorator1_GraphDecorator = Generalization(general=GraphDecorator, specific=decorators_TestScenarioGraphDecorator1)
gen_decorators_TestEdgeDecorator1_EdgeDecorator = Generalization(general=EdgeDecorator, specific=decorators_TestEdgeDecorator1)

# Domain Model
domain_model = DomainModel(
    name="decorators",
    types={decorators_TestGraphDecorator1, GraphDecorator, decorators_TestNodeDecorator1, NodeDecorator, decorators_TestScenarioGraphDecorator1, decorators_STEMTime, decorators_EdgeDecorator, decorators_GraphDecorator, decorators_NodeDecorator, decorators_TestEdgeDecorator1, EdgeDecorator},
    associations={sTEMTimeValue0},
    generalizations={gen_decorators_TestGraphDecorator1_GraphDecorator, gen_decorators_TestNodeDecorator1_NodeDecorator, gen_decorators_TestScenarioGraphDecorator1_GraphDecorator, gen_decorators_TestEdgeDecorator1_EdgeDecorator},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)