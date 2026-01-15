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
Color: Enumeration = Enumeration(
    name="Color",
    literals={
            EnumerationLiteral(name="red"),
			EnumerationLiteral(name="green"),
			EnumerationLiteral(name="blue")
    }
)

# Classes
coloredTree_HueTree = Class(name="coloredTree::HueTree")

# coloredTree_HueTree class attributes and methods
coloredTree_HueTree_label: Property = Property(name="label", type=StringType)
coloredTree_HueTree_color: Property = Property(name="color", type=StringType)
coloredTree_HueTree.attributes={coloredTree_HueTree_label, coloredTree_HueTree_color}

# Relationships
children1: BinaryAssociation = BinaryAssociation(
    name="children1",
    ends={
        Property(name="HueTree", type=coloredTree_HueTree, multiplicity=Multiplicity(1, 1)),
        Property(name="parent", type=coloredTree_HueTree, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parent3: BinaryAssociation = BinaryAssociation(
    name="parent3",
    ends={
        Property(name="HueTree4", type=coloredTree_HueTree, multiplicity=Multiplicity(1, 1)),
        Property(name="children", type=coloredTree_HueTree, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="coloredTree",
    types={coloredTree_HueTree, Color},
    associations={children1, parent3},
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