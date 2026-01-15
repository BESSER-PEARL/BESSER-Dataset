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

# Enumerations
EFieldState: Enumeration = Enumeration(
    name="EFieldState",
    literals={
            EnumerationLiteral(name="EDITABLE"),
			EnumerationLiteral(name="READONLY"),
			EnumerationLiteral(name="HIDDEN")
    }
)

# Classes
stateMachine_StateMachine = Class(name="stateMachine::StateMachine")
stateMachine_Event = Class(name="stateMachine::Event")
stateMachine_State = Class(name="stateMachine::State")
stateMachine_DocumentField = Class(name="stateMachine::DocumentField")
stateMachine_Role = Class(name="stateMachine::Role")
stateMachine_Trans = Class(name="stateMachine::Trans")
stateMachine_FieldState = Class(name="stateMachine::FieldState")
stateMachine_TransSet = Class(name="stateMachine::TransSet")

# stateMachine_StateMachine class attributes and methods
stateMachine_StateMachine_name: Property = Property(name="name", type=StringType)
stateMachine_StateMachine_package: Property = Property(name="package", type=StringType)
stateMachine_StateMachine.attributes={stateMachine_StateMachine_name, stateMachine_StateMachine_package}

# stateMachine_Event class attributes and methods
stateMachine_Event_name: Property = Property(name="name", type=StringType)
stateMachine_Event.attributes={stateMachine_Event_name}

# stateMachine_State class attributes and methods
stateMachine_State_name: Property = Property(name="name", type=StringType)
stateMachine_State.attributes={stateMachine_State_name}

# stateMachine_DocumentField class attributes and methods
stateMachine_DocumentField_name: Property = Property(name="name", type=StringType)
stateMachine_DocumentField.attributes={stateMachine_DocumentField_name}

# stateMachine_Role class attributes and methods
stateMachine_Role_name: Property = Property(name="name", type=StringType)
stateMachine_Role.attributes={stateMachine_Role_name}

# stateMachine_Trans class attributes and methods

# stateMachine_FieldState class attributes and methods
stateMachine_FieldState_state: Property = Property(name="state", type=StringType)
stateMachine_FieldState.attributes={stateMachine_FieldState_state}

# stateMachine_TransSet class attributes and methods

# Relationships
fieldRef22: BinaryAssociation = BinaryAssociation(
    name="fieldRef22",
    ends={
        Property(name="stateMachine_DocumentField24", type=stateMachine_FieldState, multiplicity=Multiplicity(1, 1)),
        Property(name="stateMachine_FieldState23", type=stateMachine_DocumentField, multiplicity=Multiplicity(1, 1))
    }
)
eventList0: BinaryAssociation = BinaryAssociation(
    name="eventList0",
    ends={
        Property(name="stateMachine_Event", type=stateMachine_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="stateMachine_StateMachine", type=stateMachine_Event, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
stateList1: BinaryAssociation = BinaryAssociation(
    name="stateList1",
    ends={
        Property(name="stateMachine_State", type=stateMachine_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="stateMachine_StateMachine2", type=stateMachine_State, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
initial3: BinaryAssociation = BinaryAssociation(
    name="initial3",
    ends={
        Property(name="stateMachine_State5", type=stateMachine_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="stateMachine_StateMachine4", type=stateMachine_State, multiplicity=Multiplicity(1, 1))
    }
)
fieldList6: BinaryAssociation = BinaryAssociation(
    name="fieldList6",
    ends={
        Property(name="stateMachine_DocumentField", type=stateMachine_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="stateMachine_StateMachine7", type=stateMachine_DocumentField, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
roleList8: BinaryAssociation = BinaryAssociation(
    name="roleList8",
    ends={
        Property(name="stateMachine_Role", type=stateMachine_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="stateMachine_StateMachine9", type=stateMachine_Role, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transList10: BinaryAssociation = BinaryAssociation(
    name="transList10",
    ends={
        Property(name="stateMachine_Trans", type=stateMachine_State, multiplicity=Multiplicity(1, 1)),
        Property(name="stateMachine_State11", type=stateMachine_Trans, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
fieldState12: BinaryAssociation = BinaryAssociation(
    name="fieldState12",
    ends={
        Property(name="stateMachine_FieldState", type=stateMachine_State, multiplicity=Multiplicity(1, 1)),
        Property(name="stateMachine_State13", type=stateMachine_FieldState, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transSetList14: BinaryAssociation = BinaryAssociation(
    name="transSetList14",
    ends={
        Property(name="stateMachine_TransSet", type=stateMachine_State, multiplicity=Multiplicity(1, 1)),
        Property(name="stateMachine_State15", type=stateMachine_TransSet, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
event16: BinaryAssociation = BinaryAssociation(
    name="event16",
    ends={
        Property(name="stateMachine_Event18", type=stateMachine_Trans, multiplicity=Multiplicity(1, 1)),
        Property(name="stateMachine_Trans17", type=stateMachine_Event, multiplicity=Multiplicity(1, 1))
    }
)
target19: BinaryAssociation = BinaryAssociation(
    name="target19",
    ends={
        Property(name="stateMachine_State21", type=stateMachine_Trans, multiplicity=Multiplicity(1, 1)),
        Property(name="stateMachine_Trans20", type=stateMachine_State, multiplicity=Multiplicity(1, 1))
    }
)
transList25: BinaryAssociation = BinaryAssociation(
    name="transList25",
    ends={
        Property(name="stateMachine_Trans27", type=stateMachine_TransSet, multiplicity=Multiplicity(1, 1)),
        Property(name="stateMachine_TransSet26", type=stateMachine_Trans, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
firedBy28: BinaryAssociation = BinaryAssociation(
    name="firedBy28",
    ends={
        Property(name="stateMachine_Role30", type=stateMachine_TransSet, multiplicity=Multiplicity(1, 1)),
        Property(name="stateMachine_TransSet29", type=stateMachine_Role, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="stateMachine",
    types={stateMachine_StateMachine, stateMachine_Event, stateMachine_State, stateMachine_DocumentField, stateMachine_Role, stateMachine_Trans, stateMachine_FieldState, stateMachine_TransSet, EFieldState},
    associations={fieldRef22, eventList0, stateList1, initial3, fieldList6, roleList8, transList10, fieldState12, transSetList14, event16, target19, transList25, firedBy28},
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