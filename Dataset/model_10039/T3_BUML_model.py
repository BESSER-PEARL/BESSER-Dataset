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
t3_Tree = Class(name="t3_Tree")

# t3_Tree class attributes and methods
t3_Tree_balanced: Property = Property(name="balanced", type=BooleanType)
t3_Tree.attributes={t3_Tree_balanced}


# OCL Constraints
Unnamed: Constraint = Constraint(
    name="Unnamed",
    context=t3_Tree,
    expression="context Tree inv: Tree.allInstances()->exists(t|t.balanced)endpackage T3",
    language="OCL"
)

# Domain Model
domain_model = DomainModel(
    name="t3",
    types={t3_Tree},
    associations={},
    constraints={Unnamed},
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