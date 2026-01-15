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
declarationorder_Child = Class(name="declarationorder::Child")
S = Class(name="S")
declarationorder_S = Class(name="declarationorder::S")

# declarationorder_Child class attributes and methods

# S class attributes and methods

# declarationorder_S class attributes and methods

# Generalizations
gen_declarationorder_Child_S = Generalization(general=S, specific=declarationorder_Child)

# Domain Model
domain_model = DomainModel(
    name="declarationorder",
    types={declarationorder_Child, S, declarationorder_S},
    associations={},
    generalizations={gen_declarationorder_Child_S},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)