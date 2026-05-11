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
dgf_DVertex = Class(name="dgf_DVertex", is_abstract=True)
DGraphElement = Class(name="DGraphElement")
dgf_DNode = Class(name="dgf_DNode")
dgf_DGraphElement = Class(name="dgf_DGraphElement", is_abstract=True)
DTypedElement = Class(name="DTypedElement")
DContainedElement = Class(name="DContainedElement")
dgf_DLink = Class(name="dgf_DLink")
dgf_DContainment = Class(name="dgf_DContainment")
dgf_Graph = Class(name="dgf_Graph")
dgf_DTypedElement = Class(name="dgf_DTypedElement", is_abstract=True)
dgf_DContainedElement = Class(name="dgf_DContainedElement", is_abstract=True)
dgf_DContainedVertex = Class(name="dgf_DContainedVertex", is_abstract=True)
DContainedVertex = Class(name="DContainedVertex")
dgf_DReference = Class(name="dgf_DReference")
DVertex = Class(name="DVertex")

# dgf_DVertex class attributes and methods

# DGraphElement class attributes and methods

# dgf_DNode class attributes and methods
dgf_DNode_pointOfView: Property = Property(name="pointOfView", type=StringType)
dgf_DNode.attributes={dgf_DNode_pointOfView}

# dgf_DGraphElement class attributes and methods
dgf_DGraphElement_name: Property = Property(name="name", type=StringType)
dgf_DGraphElement.attributes={dgf_DGraphElement_name}

# DTypedElement class attributes and methods

# DContainedElement class attributes and methods

# dgf_DLink class attributes and methods

# dgf_DContainment class attributes and methods
dgf_DContainment_compartment: Property = Property(name="compartment", type=StringType)
dgf_DContainment.attributes={dgf_DContainment_compartment}

# dgf_Graph class attributes and methods

# dgf_DTypedElement class attributes and methods

# dgf_DContainedElement class attributes and methods

# dgf_DContainedVertex class attributes and methods

# DContainedVertex class attributes and methods

# dgf_DReference class attributes and methods
dgf_DReference__property: Property = Property(name="_property", type=BooleanType)
dgf_DReference.attributes={dgf_DReference__property}

# DVertex class attributes and methods

# Relationships
target0: BinaryAssociation = BinaryAssociation(
    name="target0",
    ends={
        Property(name="dgf_DNode", type=dgf_DVertex, multiplicity=Multiplicity(1, 1)),
        Property(name="dgf_DVertex", type=dgf_DNode, multiplicity=Multiplicity(0, 1))
    }
)
source1: BinaryAssociation = BinaryAssociation(
    name="source1",
    ends={
        Property(name="dgf_DNode3", type=dgf_DVertex, multiplicity=Multiplicity(1, 1)),
        Property(name="dgf_DVertex2", type=dgf_DNode, multiplicity=Multiplicity(0, 1))
    }
)
vertices4: BinaryAssociation = BinaryAssociation(
    name="vertices4",
    ends={
        Property(name="dgf_DVertex6", type=dgf_DNode, multiplicity=Multiplicity(1, 1)),
        Property(name="dgf_DNode5", type=dgf_DVertex, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elements7: BinaryAssociation = BinaryAssociation(
    name="elements7",
    ends={
        Property(name="dgf_DGraphElement", type=dgf_Graph, multiplicity=Multiplicity(1, 1)),
        Property(name="dgf_Graph", type=dgf_DGraphElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
containment8: BinaryAssociation = BinaryAssociation(
    name="containment8",
    ends={
        Property(name="dgf_DNode9", type=dgf_DContainedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="dgf_DContainedElement", type=dgf_DNode, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_dgf_DVertex_DGraphElement = Generalization(general=DGraphElement, specific=dgf_DVertex)
gen_dgf_DNode_DGraphElement = Generalization(general=DGraphElement, specific=dgf_DNode)
gen_dgf_DNode_DTypedElement = Generalization(general=DTypedElement, specific=dgf_DNode)
gen_dgf_DNode_DContainedElement = Generalization(general=DContainedElement, specific=dgf_DNode)
gen_dgf_DContainment_DContainedVertex = Generalization(general=DContainedVertex, specific=dgf_DContainment)
gen_dgf_DContainedElement_DGraphElement = Generalization(general=DGraphElement, specific=dgf_DContainedElement)
gen_dgf_DContainedVertex_DContainedElement = Generalization(general=DContainedElement, specific=dgf_DContainedVertex)
gen_dgf_DContainedVertex_DVertex = Generalization(general=DVertex, specific=dgf_DContainedVertex)
gen_dgf_DLink_DContainedVertex = Generalization(general=DContainedVertex, specific=dgf_DLink)
gen_dgf_DLink_DTypedElement = Generalization(general=DTypedElement, specific=dgf_DLink)
gen_dgf_DReference_DVertex = Generalization(general=DVertex, specific=dgf_DReference)

# Domain Model
domain_model = DomainModel(
    name="dgf",
    types={dgf_DVertex, DGraphElement, dgf_DNode, dgf_DGraphElement, DTypedElement, DContainedElement, dgf_DLink, dgf_DContainment, dgf_Graph, dgf_DTypedElement, dgf_DContainedElement, dgf_DContainedVertex, DContainedVertex, dgf_DReference, DVertex},
    associations={target0, source1, vertices4, elements7, containment8},
    generalizations={gen_dgf_DVertex_DGraphElement, gen_dgf_DNode_DGraphElement, gen_dgf_DNode_DTypedElement, gen_dgf_DNode_DContainedElement, gen_dgf_DContainment_DContainedVertex, gen_dgf_DContainedElement_DGraphElement, gen_dgf_DContainedVertex_DContainedElement, gen_dgf_DContainedVertex_DVertex, gen_dgf_DLink_DContainedVertex, gen_dgf_DLink_DTypedElement, gen_dgf_DReference_DVertex},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)