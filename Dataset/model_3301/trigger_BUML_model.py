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
trigger_Trigger = Class(name="trigger::Trigger")
Decorator = Class(name="Decorator")
trigger_Predicate = Class(name="trigger::Predicate")
trigger_Decorator = Class(name="trigger::Decorator")

# trigger_Trigger class attributes and methods

# Decorator class attributes and methods

# trigger_Predicate class attributes and methods

# trigger_Decorator class attributes and methods

# Relationships
predicate0: BinaryAssociation = BinaryAssociation(
    name="predicate0",
    ends={
        Property(name="trigger_Predicate", type=trigger_Trigger, multiplicity=Multiplicity(1, 1)),
        Property(name="trigger_Trigger", type=trigger_Predicate, multiplicity=Multiplicity(0, 1))
    }
)
action1: BinaryAssociation = BinaryAssociation(
    name="action1",
    ends={
        Property(name="trigger_Decorator", type=trigger_Trigger, multiplicity=Multiplicity(1, 1)),
        Property(name="trigger_Trigger2", type=trigger_Decorator, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_trigger_Trigger_Decorator = Generalization(general=Decorator, specific=trigger_Trigger)

# Domain Model
domain_model = DomainModel(
    name="trigger",
    types={trigger_Trigger, Decorator, trigger_Predicate, trigger_Decorator},
    associations={predicate0, action1},
    generalizations={gen_trigger_Trigger_Decorator},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)