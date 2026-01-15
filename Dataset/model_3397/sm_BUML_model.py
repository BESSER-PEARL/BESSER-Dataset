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
StateMachine_Arc = Class(name="StateMachine::Arc")
StateMachine_PNTransition = Class(name="StateMachine::PNTransition")
StateMachine_Place = Class(name="StateMachine::Place")

# StateMachine_Arc class attributes and methods
StateMachine_Arc_weight: Property = Property(name="weight", type=IntegerType)
StateMachine_Arc_toPlace: Property = Property(name="toPlace", type=BooleanType)
StateMachine_Arc.attributes={StateMachine_Arc_toPlace, StateMachine_Arc_weight}

# StateMachine_PNTransition class attributes and methods

# StateMachine_Place class attributes and methods
StateMachine_Place_tokens: Property = Property(name="tokens", type=IntegerType)
StateMachine_Place_name: Property = Property(name="name", type=StringType)
StateMachine_Place.attributes={StateMachine_Place_name, StateMachine_Place_tokens}

# Relationships
arcTransition0: BinaryAssociation = BinaryAssociation(
    name="arcTransition0",
    ends={
        Property(name="StateMachine_PNTransition", type=StateMachine_Arc, multiplicity=Multiplicity(1, 1)),
        Property(name="StateMachine_Arc", type=StateMachine_PNTransition, multiplicity=Multiplicity(1, 1))
    }
)
arcPlace1: BinaryAssociation = BinaryAssociation(
    name="arcPlace1",
    ends={
        Property(name="StateMachine_Arc2", type=StateMachine_Place, multiplicity=Multiplicity(1, 1)),
        Property(name="StateMachine_Place", type=StateMachine_Arc, multiplicity=Multiplicity(0, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="StateMachine",
    types={StateMachine_Arc, StateMachine_PNTransition, StateMachine_Place},
    associations={arcTransition0, arcPlace1},
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