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
automata_Current = Class(name="automata::Current")
automata_Initial = Class(name="automata::Initial")
automata_State = Class(name="automata::State")
automata_Transition = Class(name="automata::Transition")
automata_Final = Class(name="automata::Final")
automata_Automata = Class(name="automata::Automata")

# automata_Current class attributes and methods
automata_Current_name: Property = Property(name="name", type=StringType)
automata_Current.attributes={automata_Current_name}

# automata_Initial class attributes and methods
automata_Initial_name: Property = Property(name="name", type=StringType)
automata_Initial.attributes={automata_Initial_name}

# automata_State class attributes and methods
automata_State_name: Property = Property(name="name", type=StringType)
automata_State.attributes={automata_State_name}

# automata_Transition class attributes and methods
automata_Transition_token: Property = Property(name="token", type=StringType)
automata_Transition_name: Property = Property(name="name", type=StringType)
automata_Transition.attributes={automata_Transition_token, automata_Transition_name}

# automata_Final class attributes and methods
automata_Final_name: Property = Property(name="name", type=StringType)
automata_Final.attributes={automata_Final_name}

# automata_Automata class attributes and methods

# Relationships
current0: BinaryAssociation = BinaryAssociation(
    name="current0",
    ends={
        Property(name="automata_Current", type=automata_Automata, multiplicity=Multiplicity(1, 1)),
        Property(name="automata_Automata", type=automata_Current, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
initial1: BinaryAssociation = BinaryAssociation(
    name="initial1",
    ends={
        Property(name="automata_Initial", type=automata_Automata, multiplicity=Multiplicity(1, 1)),
        Property(name="automata_Automata2", type=automata_Initial, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
states3: BinaryAssociation = BinaryAssociation(
    name="states3",
    ends={
        Property(name="automata_State", type=automata_Automata, multiplicity=Multiplicity(1, 1)),
        Property(name="automata_Automata4", type=automata_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transitions5: BinaryAssociation = BinaryAssociation(
    name="transitions5",
    ends={
        Property(name="automata_Transition", type=automata_Automata, multiplicity=Multiplicity(1, 1)),
        Property(name="automata_Automata6", type=automata_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
finals7: BinaryAssociation = BinaryAssociation(
    name="finals7",
    ends={
        Property(name="automata_Final", type=automata_Automata, multiplicity=Multiplicity(1, 1)),
        Property(name="automata_Automata8", type=automata_Final, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
state21: BinaryAssociation = BinaryAssociation(
    name="state21",
    ends={
        Property(name="automata_State23", type=automata_Current, multiplicity=Multiplicity(1, 1)),
        Property(name="automata_Current22", type=automata_State, multiplicity=Multiplicity(0, 1))
    }
)
source9: BinaryAssociation = BinaryAssociation(
    name="source9",
    ends={
        Property(name="automata_State11", type=automata_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="automata_Transition10", type=automata_State, multiplicity=Multiplicity(0, 1))
    }
)
target12: BinaryAssociation = BinaryAssociation(
    name="target12",
    ends={
        Property(name="automata_State14", type=automata_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="automata_Transition13", type=automata_State, multiplicity=Multiplicity(0, 1))
    }
)
state15: BinaryAssociation = BinaryAssociation(
    name="state15",
    ends={
        Property(name="automata_State17", type=automata_Initial, multiplicity=Multiplicity(1, 1)),
        Property(name="automata_Initial16", type=automata_State, multiplicity=Multiplicity(0, 1))
    }
)
state18: BinaryAssociation = BinaryAssociation(
    name="state18",
    ends={
        Property(name="automata_State20", type=automata_Final, multiplicity=Multiplicity(1, 1)),
        Property(name="automata_Final19", type=automata_State, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="automata",
    types={automata_Current, automata_Initial, automata_State, automata_Transition, automata_Final, automata_Automata},
    associations={current0, initial1, states3, transitions5, finals7, state21, source9, target12, state15, state18},
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