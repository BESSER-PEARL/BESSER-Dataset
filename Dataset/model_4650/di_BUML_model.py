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
ContainerShape = Class(name="ContainerShape")
di_Link = Class(name="di_Link")
di_ContainerShape = Class(name="di_ContainerShape", is_abstract=True)
DiNode = Class(name="DiNode")
di_Shape = Class(name="di_Shape")
di_DiNode = Class(name="di_DiNode", is_abstract=True)
di_EStringToStringMapEntry = Class(name="di_EStringToStringMapEntry")
di_Diagram = Class(name="di_Diagram")

# ContainerShape class attributes and methods

# di_Link class attributes and methods

# di_ContainerShape class attributes and methods

# DiNode class attributes and methods

# di_Shape class attributes and methods
di_Shape_x: Property = Property(name="x", type=IntegerType)
di_Shape_y: Property = Property(name="y", type=IntegerType)
di_Shape_width: Property = Property(name="width", type=IntegerType)
di_Shape_height: Property = Property(name="height", type=IntegerType)
di_Shape.attributes={di_Shape_x, di_Shape_width, di_Shape_y, di_Shape_height}

# di_DiNode class attributes and methods
di_DiNode_modelElement: Property = Property(name="modelElement", type=StringType)
di_DiNode.attributes={di_DiNode_modelElement}

# di_EStringToStringMapEntry class attributes and methods

# di_Diagram class attributes and methods

# Relationships
sourceLinks1: BinaryAssociation = BinaryAssociation(
    name="sourceLinks1",
    ends={
        Property(name="Link", type=di_Shape, multiplicity=Multiplicity(1, 1)),
        Property(name="target", type=di_Link, multiplicity=Multiplicity(0, 9999))
    }
)
targetLinks2: BinaryAssociation = BinaryAssociation(
    name="targetLinks2",
    ends={
        Property(name="Link3", type=di_Shape, multiplicity=Multiplicity(1, 1)),
        Property(name="source", type=di_Link, multiplicity=Multiplicity(0, 9999))
    }
)
shapes0: BinaryAssociation = BinaryAssociation(
    name="shapes0",
    ends={
        Property(name="di_Shape", type=di_ContainerShape, multiplicity=Multiplicity(1, 1)),
        Property(name="di_ContainerShape", type=di_Shape, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
properties8: BinaryAssociation = BinaryAssociation(
    name="properties8",
    ends={
        Property(name="di_EStringToStringMapEntry", type=di_DiNode, multiplicity=Multiplicity(1, 1)),
        Property(name="di_DiNode", type=di_EStringToStringMapEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
source4: BinaryAssociation = BinaryAssociation(
    name="source4",
    ends={
        Property(name="Shape", type=di_Link, multiplicity=Multiplicity(1, 1)),
        Property(name="targetLinks", type=di_Shape, multiplicity=Multiplicity(0, 1))
    }
)
target5: BinaryAssociation = BinaryAssociation(
    name="target5",
    ends={
        Property(name="Shape6", type=di_Link, multiplicity=Multiplicity(1, 1)),
        Property(name="sourceLinks", type=di_Shape, multiplicity=Multiplicity(0, 1))
    }
)
links7: BinaryAssociation = BinaryAssociation(
    name="links7",
    ends={
        Property(name="di_Link", type=di_Diagram, multiplicity=Multiplicity(1, 1)),
        Property(name="di_Diagram", type=di_Link, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_di_Shape_ContainerShape = Generalization(general=ContainerShape, specific=di_Shape)
gen_di_Link_DiNode = Generalization(general=DiNode, specific=di_Link)
gen_di_ContainerShape_DiNode = Generalization(general=DiNode, specific=di_ContainerShape)
gen_di_Diagram_ContainerShape = Generalization(general=ContainerShape, specific=di_Diagram)

# Domain Model
domain_model = DomainModel(
    name="di",
    types={ContainerShape, di_Link, di_ContainerShape, DiNode, di_Shape, di_DiNode, di_EStringToStringMapEntry, di_Diagram},
    associations={sourceLinks1, targetLinks2, shapes0, properties8, source4, target5, links7},
    generalizations={gen_di_Shape_ContainerShape, gen_di_Link_DiNode, gen_di_ContainerShape_DiNode, gen_di_Diagram_ContainerShape},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)