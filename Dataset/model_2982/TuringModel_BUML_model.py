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
Direction: Enumeration = Enumeration(
    name="Direction",
    literals={
            EnumerationLiteral(name="HOLD"),
			EnumerationLiteral(name="LEFT"),
			EnumerationLiteral(name="RIGHT")
    }
)

# Classes
turingmodel_TuringMachine = Class(name="turingmodel::TuringMachine")
turingmodel_State = Class(name="turingmodel::State")
turingmodel_Transition = Class(name="turingmodel::Transition")

# turingmodel_TuringMachine class attributes and methods

# turingmodel_State class attributes and methods
turingmodel_State_name: Property = Property(name="name", type=StringType)
turingmodel_State_isEndState: Property = Property(name="isEndState", type=BooleanType)
turingmodel_State.attributes={turingmodel_State_name, turingmodel_State_isEndState}

# turingmodel_Transition class attributes and methods
turingmodel_Transition_condition: Property = Property(name="condition", type=StringType)
turingmodel_Transition_write: Property = Property(name="write", type=StringType)
turingmodel_Transition_dir: Property = Property(name="dir", type=StringType)
turingmodel_Transition.attributes={turingmodel_Transition_condition, turingmodel_Transition_write, turingmodel_Transition_dir}

# Relationships
startState3: BinaryAssociation = BinaryAssociation(
    name="startState3",
    ends={
        Property(name="turingmodel_State5", type=turingmodel_TuringMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="turingmodel_TuringMachine4", type=turingmodel_State, multiplicity=Multiplicity(1, 1))
    }
)
next6: BinaryAssociation = BinaryAssociation(
    name="next6",
    ends={
        Property(name="Transition", type=turingmodel_State, multiplicity=Multiplicity(1, 1)),
        Property(name="source", type=turingmodel_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
substates8: BinaryAssociation = BinaryAssociation(
    name="substates8",
    ends={
        Property(name="turingmodel_State9", type=turingmodel_State, multiplicity=Multiplicity(1, 1)),
        Property(name="turingmodel_State7", type=turingmodel_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
startSubstate11: BinaryAssociation = BinaryAssociation(
    name="startSubstate11",
    ends={
        Property(name="turingmodel_State12", type=turingmodel_State, multiplicity=Multiplicity(1, 1)),
        Property(name="turingmodel_State10", type=turingmodel_State, multiplicity=Multiplicity(0, 1))
    }
)
subtransitions13: BinaryAssociation = BinaryAssociation(
    name="subtransitions13",
    ends={
        Property(name="turingmodel_Transition15", type=turingmodel_State, multiplicity=Multiplicity(1, 1)),
        Property(name="turingmodel_State14", type=turingmodel_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
states0: BinaryAssociation = BinaryAssociation(
    name="states0",
    ends={
        Property(name="turingmodel_State", type=turingmodel_TuringMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="turingmodel_TuringMachine", type=turingmodel_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transitions1: BinaryAssociation = BinaryAssociation(
    name="transitions1",
    ends={
        Property(name="turingmodel_Transition", type=turingmodel_TuringMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="turingmodel_TuringMachine2", type=turingmodel_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
source16: BinaryAssociation = BinaryAssociation(
    name="source16",
    ends={
        Property(name="State", type=turingmodel_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="next", type=turingmodel_State, multiplicity=Multiplicity(1, 1))
    }
)
target17: BinaryAssociation = BinaryAssociation(
    name="target17",
    ends={
        Property(name="turingmodel_State19", type=turingmodel_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="turingmodel_Transition18", type=turingmodel_State, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="turingmodel",
    types={turingmodel_TuringMachine, turingmodel_State, turingmodel_Transition, Direction},
    associations={startState3, next6, substates8, startSubstate11, subtransitions13, states0, transitions1, source16, target17},
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