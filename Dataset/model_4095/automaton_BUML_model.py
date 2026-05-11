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
automaton_Automaton = Class(name="automaton_Automaton")
automaton_NamedElement = Class(name="automaton_NamedElement", is_abstract=True)
automaton_State = Class(name="automaton_State")
NamedElement = Class(name="NamedElement")
automaton_Input = Class(name="automaton_Input")
automaton_Output = Class(name="automaton_Output")
automaton_Transition = Class(name="automaton_Transition")

# automaton_Automaton class attributes and methods

# automaton_NamedElement class attributes and methods
automaton_NamedElement_name: Property = Property(name="name", type=StringType)
automaton_NamedElement.attributes={automaton_NamedElement_name}

# automaton_State class attributes and methods

# NamedElement class attributes and methods

# automaton_Input class attributes and methods

# automaton_Output class attributes and methods

# automaton_Transition class attributes and methods

# Relationships
action1: BinaryAssociation = BinaryAssociation(
    name="action1",
    ends={
        Property(name="automaton_Transition2", type=automaton_Output, multiplicity=Multiplicity(0, 9999)),
        Property(name="automaton_Output", type=automaton_Transition, multiplicity=Multiplicity(1, 1))
    }
)
origine3: BinaryAssociation = BinaryAssociation(
    name="origine3",
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
state8: BinaryAssociation = BinaryAssociation(
    name="state8",
    ends={
        Property(name="automaton_State9", type=automaton_Automaton, multiplicity=Multiplicity(1, 1)),
        Property(name="automaton_Automaton", type=automaton_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transition10: BinaryAssociation = BinaryAssociation(
    name="transition10",
    ends={
        Property(name="automaton_Transition12", type=automaton_Automaton, multiplicity=Multiplicity(1, 1)),
        Property(name="automaton_Automaton11", type=automaton_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
output13: BinaryAssociation = BinaryAssociation(
    name="output13",
    ends={
        Property(name="automaton_Output15", type=automaton_Automaton, multiplicity=Multiplicity(1, 1)),
        Property(name="automaton_Automaton14", type=automaton_Output, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
input16: BinaryAssociation = BinaryAssociation(
    name="input16",
    ends={
        Property(name="automaton_Input18", type=automaton_Automaton, multiplicity=Multiplicity(1, 1)),
        Property(name="automaton_Automaton17", type=automaton_Input, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
event0: BinaryAssociation = BinaryAssociation(
    name="event0",
    ends={
        Property(name="automaton_Input", type=automaton_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="automaton_Transition", type=automaton_Input, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_automaton_Automaton_NamedElement = Generalization(general=NamedElement, specific=automaton_Automaton)
gen_automaton_State_NamedElement = Generalization(general=NamedElement, specific=automaton_State)
gen_automaton_Input_NamedElement = Generalization(general=NamedElement, specific=automaton_Input)
gen_automaton_Output_NamedElement = Generalization(general=NamedElement, specific=automaton_Output)
gen_automaton_Transition_NamedElement = Generalization(general=NamedElement, specific=automaton_Transition)

# Domain Model
domain_model = DomainModel(
    name="automaton",
    types={automaton_Automaton, automaton_NamedElement, automaton_State, NamedElement, automaton_Input, automaton_Output, automaton_Transition},
    associations={action1, origine3, destination5, state8, transition10, output13, input16, event0},
    generalizations={gen_automaton_Automaton_NamedElement, gen_automaton_State_NamedElement, gen_automaton_Input_NamedElement, gen_automaton_Output_NamedElement, gen_automaton_Transition_NamedElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)