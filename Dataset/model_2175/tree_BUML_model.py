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
Tree_Tree = Class(name="Tree::Tree")

# Tree_Tree class attributes and methods
Tree_Tree_label: Property = Property(name="label", type=StringType)
Tree_Tree.attributes={Tree_Tree_label}

# Relationships
parent3: BinaryAssociation = BinaryAssociation(
    name="parent3",
    ends={
        Property(name="Tree4", type=Tree_Tree, multiplicity=Multiplicity(1, 1)),
        Property(name="children", type=Tree_Tree, multiplicity=Multiplicity(0, 1))
    }
)
children1: BinaryAssociation = BinaryAssociation(
    name="children1",
    ends={
        Property(name="Tree", type=Tree_Tree, multiplicity=Multiplicity(1, 1)),
        Property(name="parent", type=Tree_Tree, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="Tree",
    types={Tree_Tree},
    associations={parent3, children1},
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