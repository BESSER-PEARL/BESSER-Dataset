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
Player = Class(name="Player")

# Player class attributes and methods
Player_name: Property = Property(name="name", type=StringType)
Player_token: Property = Property(name="token", type=StringType)
Player_position: Property = Property(name="position", type=IntegerType)
Player_balance: Property = Property(name="balance", type=IntegerType)
Player.attributes={Player_balance, Player_position, Player_name, Player_token}

# Domain Model
domain_model = DomainModel(
    name="_b6nJsDrEEemJ8_ntaCiHBw",
    types={Player},
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