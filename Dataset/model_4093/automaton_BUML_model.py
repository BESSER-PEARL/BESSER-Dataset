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
automaton_State = Class(name="automaton::State")
NamedElement = Class(name="NamedElement")
automaton_Input = Class(name="automaton::Input")
automaton_Output = Class(name="automaton::Output")
automaton_Transition = Class(name="automaton::Transition")
automaton_NamedElement = Class(name="automaton::NamedElement", is_abstract=True)
automaton_Automaton = Class(name="automaton::Automaton")

# automaton_State class attributes and methods

# NamedElement class attributes and methods

# automaton_Input class attributes and methods

# automaton_Output class attributes and methods

# automaton_Transition class attributes and methods

# automaton_NamedElement class attributes and methods
automaton_NamedElement_name: Property = Property(name="name", type=StringType)
automaton_NamedElement.attributes={automaton_NamedElement_name}

# automaton_Automaton class attributes and methods

# Relationships
outputs16: BinaryAssociation = BinaryAssociation(
    name="outputs16",
    ends={
        Property(name="automaton_Output18", type=automaton_Automaton, multiplicity=Multiplicity(1, 1)),
        Property(name="automaton_Automaton17", type=automaton_Output, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
event0: BinaryAssociation = BinaryAssociation(
    name="event0",
    ends={
        Property(name="automaton_Input", type=automaton_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="automaton_Transition", type=automaton_Input, multiplicity=Multiplicity(0, 1))
    }
)
actions1: BinaryAssociation = BinaryAssociation(
    name="actions1",
    ends={
        Property(name="automaton_Output", type=automaton_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="automaton_Transition2", type=automaton_Output, multiplicity=Multiplicity(0, 9999))
    }
)
origin3: BinaryAssociation = BinaryAssociation(
    name="origin3",
    ends={
        Property(name="automaton_State", type=automaton_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="automaton_Transition4", type=automaton_State, multiplicity=Multiplicity(0, 1))
    }
)
destination5: BinaryAssociation = BinaryAssociation(
    name="destination5",
    ends={
        Property(name="automaton_State7", type=automaton_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="automaton_Transition6", type=automaton_State, multiplicity=Multiplicity(0, 1))
    }
)
states8: BinaryAssociation = BinaryAssociation(
    name="states8",
    ends={
        Property(name="automaton_State9", type=automaton_Automaton, multiplicity=Multiplicity(1, 1)),
        Property(name="automaton_Automaton", type=automaton_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transitions10: BinaryAssociation = BinaryAssociation(
    name="transitions10",
    ends={
        Property(name="automaton_Transition12", type=automaton_Automaton, multiplicity=Multiplicity(1, 1)),
        Property(name="automaton_Automaton11", type=automaton_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
inputs13: BinaryAssociation = BinaryAssociation(
    name="inputs13",
    ends={
        Property(name="automaton_Input15", type=automaton_Automaton, multiplicity=Multiplicity(1, 1)),
        Property(name="automaton_Automaton14", type=automaton_Input, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_automaton_State_NamedElement = Generalization(general=NamedElement, specific=automaton_State)
gen_automaton_Input_NamedElement = Generalization(general=NamedElement, specific=automaton_Input)
gen_automaton_Output_NamedElement = Generalization(general=NamedElement, specific=automaton_Output)
gen_automaton_Transition_NamedElement = Generalization(general=NamedElement, specific=automaton_Transition)
gen_automaton_Automaton_NamedElement = Generalization(general=NamedElement, specific=automaton_Automaton)

# Domain Model
domain_model = DomainModel(
    name="automaton",
    types={automaton_State, NamedElement, automaton_Input, automaton_Output, automaton_Transition, automaton_NamedElement, automaton_Automaton},
    associations={outputs16, event0, actions1, origin3, destination5, states8, transitions10, inputs13},
    generalizations={gen_automaton_State_NamedElement, gen_automaton_Input_NamedElement, gen_automaton_Output_NamedElement, gen_automaton_Transition_NamedElement, gen_automaton_Automaton_NamedElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)