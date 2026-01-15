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
p_append = Class(name="p::append")
p_ThisClassWasFirst = Class(name="p::ThisClassWasFirst")
p_ThisClassWasMiddle = Class(name="p::ThisClassWasMiddle")
p_ThisClassWasLast = Class(name="p::ThisClassWasLast")

# p_append class attributes and methods

# p_ThisClassWasFirst class attributes and methods

# p_ThisClassWasMiddle class attributes and methods

# p_ThisClassWasLast class attributes and methods

# Domain Model
domain_model = DomainModel(
    name="p",
    types={p_append, p_ThisClassWasFirst, p_ThisClassWasMiddle, p_ThisClassWasLast},
    associations={},
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