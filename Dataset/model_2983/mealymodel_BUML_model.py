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
mealymodel_MealyMachine = Class(name="mealymodel::MealyMachine")
mealymodel_State = Class(name="mealymodel::State")
mealymodel_Alphabet = Class(name="mealymodel::Alphabet")
mealymodel_Transition = Class(name="mealymodel::Transition")

# mealymodel_MealyMachine class attributes and methods

# mealymodel_State class attributes and methods
mealymodel_State_name: Property = Property(name="name", type=StringType)
mealymodel_State.attributes={mealymodel_State_name}

# mealymodel_Alphabet class attributes and methods
mealymodel_Alphabet_characters: Property = Property(name="characters", type=StringType)
mealymodel_Alphabet.attributes={mealymodel_Alphabet_characters}

# mealymodel_Transition class attributes and methods
mealymodel_Transition_input: Property = Property(name="input", type=StringType)
mealymodel_Transition_output: Property = Property(name="output", type=StringType)
mealymodel_Transition.attributes={mealymodel_Transition_output, mealymodel_Transition_input}

# Relationships
initialState0: BinaryAssociation = BinaryAssociation(
    name="initialState0",
    ends={
        Property(name="mealymodel_State", type=mealymodel_MealyMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="mealymodel_MealyMachine", type=mealymodel_State, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
states1: BinaryAssociation = BinaryAssociation(
    name="states1",
    ends={
        Property(name="mealymodel_State3", type=mealymodel_MealyMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="mealymodel_MealyMachine2", type=mealymodel_State, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
inputAlphabet4: BinaryAssociation = BinaryAssociation(
    name="inputAlphabet4",
    ends={
        Property(name="mealymodel_Alphabet", type=mealymodel_MealyMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="mealymodel_MealyMachine5", type=mealymodel_Alphabet, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
transitions9: BinaryAssociation = BinaryAssociation(
    name="transitions9",
    ends={
        Property(name="mealymodel_Transition", type=mealymodel_MealyMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="mealymodel_MealyMachine10", type=mealymodel_Transition, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
sourceState11: BinaryAssociation = BinaryAssociation(
    name="sourceState11",
    ends={
        Property(name="mealymodel_State13", type=mealymodel_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="mealymodel_Transition12", type=mealymodel_State, multiplicity=Multiplicity(1, 1))
    }
)
targetState14: BinaryAssociation = BinaryAssociation(
    name="targetState14",
    ends={
        Property(name="mealymodel_State16", type=mealymodel_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="mealymodel_Transition15", type=mealymodel_State, multiplicity=Multiplicity(1, 1))
    }
)
outputAlphabet6: BinaryAssociation = BinaryAssociation(
    name="outputAlphabet6",
    ends={
        Property(name="mealymodel_Alphabet8", type=mealymodel_MealyMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="mealymodel_MealyMachine7", type=mealymodel_Alphabet, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="mealymodel",
    types={mealymodel_MealyMachine, mealymodel_State, mealymodel_Alphabet, mealymodel_Transition},
    associations={initialState0, states1, inputAlphabet4, transitions9, sourceState11, targetState14, outputAlphabet6},
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