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
base_BaseType = Class(name="base::BaseType")
base_nested_SubA = Class(name="base::nested::SubA")
BaseType = Class(name="BaseType")

# base_BaseType class attributes and methods
base_BaseType_stuff: Property = Property(name="stuff", type=StringType)
base_BaseType.attributes={base_BaseType_stuff}

# base_nested_SubA class attributes and methods

# BaseType class attributes and methods

# Generalizations
gen_base_nested_SubA_BaseType = Generalization(general=BaseType, specific=base_nested_SubA)

# Domain Model
domain_model = DomainModel(
    name="base",
    types={base_BaseType, base_nested_SubA, BaseType},
    associations={},
    generalizations={gen_base_nested_SubA_BaseType},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)