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
automation_State = Class(name="automation::State")
NamedElement = Class(name="NamedElement")
automation_Input = Class(name="automation::Input")
automation_Output = Class(name="automation::Output")
automation_Transition = Class(name="automation::Transition")
automation_NamedElement = Class(name="automation::NamedElement", is_abstract=True)
automation_Automation = Class(name="automation::Automation")

# automation_State class attributes and methods

# NamedElement class attributes and methods

# automation_Input class attributes and methods

# automation_Output class attributes and methods

# automation_Transition class attributes and methods

# automation_NamedElement class attributes and methods
automation_NamedElement_name: Property = Property(name="name", type=StringType)
automation_NamedElement.attributes={automation_NamedElement_name}

# automation_Automation class attributes and methods

# Relationships
inputs13: BinaryAssociation = BinaryAssociation(
    name="inputs13",
    ends={
        Property(name="automation_Input15", type=automation_Automation, multiplicity=Multiplicity(1, 1)),
        Property(name="automation_Automation14", type=automation_Input, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
outputs16: BinaryAssociation = BinaryAssociation(
    name="outputs16",
    ends={
        Property(name="automation_Output18", type=automation_Automation, multiplicity=Multiplicity(1, 1)),
        Property(name="automation_Automation17", type=automation_Output, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
event0: BinaryAssociation = BinaryAssociation(
    name="event0",
    ends={
        Property(name="automation_Input", type=automation_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="automation_Transition", type=automation_Input, multiplicity=Multiplicity(0, 1))
    }
)
actions1: BinaryAssociation = BinaryAssociation(
    name="actions1",
    ends={
        Property(name="automation_Output", type=automation_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="automation_Transition2", type=automation_Output, multiplicity=Multiplicity(0, 9999))
    }
)
origin3: BinaryAssociation = BinaryAssociation(
    name="origin3",
    ends={
        Property(name="automation_State", type=automation_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="automation_Transition4", type=automation_State, multiplicity=Multiplicity(0, 1))
    }
)
disnation5: BinaryAssociation = BinaryAssociation(
    name="disnation5",
    ends={
        Property(name="automation_State7", type=automation_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="automation_Transition6", type=automation_State, multiplicity=Multiplicity(0, 1))
    }
)
transitions8: BinaryAssociation = BinaryAssociation(
    name="transitions8",
    ends={
        Property(name="automation_Transition9", type=automation_Automation, multiplicity=Multiplicity(1, 1)),
        Property(name="automation_Automation", type=automation_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
states10: BinaryAssociation = BinaryAssociation(
    name="states10",
    ends={
        Property(name="automation_State12", type=automation_Automation, multiplicity=Multiplicity(1, 1)),
        Property(name="automation_Automation11", type=automation_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_automation_State_NamedElement = Generalization(general=NamedElement, specific=automation_State)
gen_automation_Input_NamedElement = Generalization(general=NamedElement, specific=automation_Input)
gen_automation_Output_NamedElement = Generalization(general=NamedElement, specific=automation_Output)
gen_automation_Transition_NamedElement = Generalization(general=NamedElement, specific=automation_Transition)
gen_automation_Automation_NamedElement = Generalization(general=NamedElement, specific=automation_Automation)

# Domain Model
domain_model = DomainModel(
    name="automation",
    types={automation_State, NamedElement, automation_Input, automation_Output, automation_Transition, automation_NamedElement, automation_Automation},
    associations={inputs13, outputs16, event0, actions1, origin3, disnation5, transitions8, states10},
    generalizations={gen_automation_State_NamedElement, gen_automation_Input_NamedElement, gen_automation_Output_NamedElement, gen_automation_Transition_NamedElement, gen_automation_Automation_NamedElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)