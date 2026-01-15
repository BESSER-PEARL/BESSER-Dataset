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
TreeDsl_Tree = Class(name="TreeDsl::Tree")

# TreeDsl_Tree class attributes and methods
TreeDsl_Tree_label: Property = Property(name="label", type=StringType)
TreeDsl_Tree.attributes={TreeDsl_Tree_label}

# Relationships
children1: BinaryAssociation = BinaryAssociation(
    name="children1",
    ends={
        Property(name="Tree", type=TreeDsl_Tree, multiplicity=Multiplicity(1, 1)),
        Property(name="parent", type=TreeDsl_Tree, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parent3: BinaryAssociation = BinaryAssociation(
    name="parent3",
    ends={
        Property(name="Tree4", type=TreeDsl_Tree, multiplicity=Multiplicity(1, 1)),
        Property(name="children", type=TreeDsl_Tree, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="TreeDsl",
    types={TreeDsl_Tree},
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