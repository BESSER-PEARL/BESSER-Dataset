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
transform_Transformation = Class(name="transform::Transformation")
Named = Class(name="Named")
transform_Graph = Class(name="transform::Graph")
transform_Grammar = Class(name="transform::Grammar")

# transform_Transformation class attributes and methods

# Named class attributes and methods

# transform_Graph class attributes and methods

# transform_Grammar class attributes and methods

# Relationships
hote0: BinaryAssociation = BinaryAssociation(
    name="hote0",
    ends={
        Property(name="transform_Graph", type=transform_Transformation, multiplicity=Multiplicity(1, 1)),
        Property(name="transform_Transformation", type=transform_Graph, multiplicity=Multiplicity(0, 1))
    }
)
grammar1: BinaryAssociation = BinaryAssociation(
    name="grammar1",
    ends={
        Property(name="transform_Grammar", type=transform_Transformation, multiplicity=Multiplicity(1, 1)),
        Property(name="transform_Transformation2", type=transform_Grammar, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_transform_Transformation_Named = Generalization(general=Named, specific=transform_Transformation)

# Domain Model
domain_model = DomainModel(
    name="transform",
    types={transform_Transformation, Named, transform_Graph, transform_Grammar},
    associations={hote0, grammar1},
    generalizations={gen_transform_Transformation_Named},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)