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
statediagram_StateDiagram = Class(name="statediagram::StateDiagram")
statediagram_State = Class(name="statediagram::State")
statediagram_Transition = Class(name="statediagram::Transition")

# statediagram_StateDiagram class attributes and methods
statediagram_StateDiagram_name: Property = Property(name="name", type=StringType)
statediagram_StateDiagram.attributes={statediagram_StateDiagram_name}

# statediagram_State class attributes and methods
statediagram_State_name: Property = Property(name="name", type=StringType)
statediagram_State_isInitial: Property = Property(name="isInitial", type=BooleanType)
statediagram_State.attributes={statediagram_State_name, statediagram_State_isInitial}

# statediagram_Transition class attributes and methods

# Relationships
states0: BinaryAssociation = BinaryAssociation(
    name="states0",
    ends={
        Property(name="statediagram_State", type=statediagram_StateDiagram, multiplicity=Multiplicity(1, 1)),
        Property(name="statediagram_StateDiagram", type=statediagram_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transitions1: BinaryAssociation = BinaryAssociation(
    name="transitions1",
    ends={
        Property(name="statediagram_Transition", type=statediagram_State, multiplicity=Multiplicity(1, 1)),
        Property(name="statediagram_State2", type=statediagram_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
next3: BinaryAssociation = BinaryAssociation(
    name="next3",
    ends={
        Property(name="statediagram_State5", type=statediagram_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="statediagram_Transition4", type=statediagram_State, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="statediagram",
    types={statediagram_StateDiagram, statediagram_State, statediagram_Transition},
    associations={states0, transitions1, next3},
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