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
fiacre_Variable = Class(name="fiacre::Variable")
fiacre_State = Class(name="fiacre::State")
EModelElement = Class(name="EModelElement")
fiacre_Transition = Class(name="fiacre::Transition")
fiacre_Process = Class(name="fiacre::Process")
fiacre_DataType = Class(name="fiacre::DataType")
fiacre_Component = Class(name="fiacre::Component")
fiacre_Init = Class(name="fiacre::Init")
State = Class(name="State")
fiacre_Program = Class(name="fiacre::Program")

# fiacre_Variable class attributes and methods
fiacre_Variable_ID: Property = Property(name="ID", type=StringType)
fiacre_Variable.attributes={fiacre_Variable_ID}

# fiacre_State class attributes and methods
fiacre_State_ID: Property = Property(name="ID", type=StringType)
fiacre_State_m_StateInvariant: Method = Method(name="StateInvariant", parameters={})
fiacre_State.attributes={fiacre_State_ID}
fiacre_State.methods={fiacre_State_m_StateInvariant}

# EModelElement class attributes and methods

# fiacre_Transition class attributes and methods
fiacre_Transition_m_Guard: Method = Method(name="Guard", parameters={})
fiacre_Transition_m_Trigger: Method = Method(name="Trigger", parameters={})
fiacre_Transition_m_Action: Method = Method(name="Action", parameters={})
fiacre_Transition.methods={fiacre_Transition_m_Action, fiacre_Transition_m_Trigger, fiacre_Transition_m_Guard}

# fiacre_Process class attributes and methods
fiacre_Process_ID: Property = Property(name="ID", type=StringType)
fiacre_Process.attributes={fiacre_Process_ID}

# fiacre_DataType class attributes and methods

# fiacre_Component class attributes and methods
fiacre_Component_ID: Property = Property(name="ID", type=StringType)
fiacre_Component.attributes={fiacre_Component_ID}

# fiacre_Init class attributes and methods
fiacre_Init_m_Assignment: Method = Method(name="Assignment", parameters={})
fiacre_Init.methods={fiacre_Init_m_Assignment}

# State class attributes and methods

# fiacre_Program class attributes and methods

# Relationships
state1: BinaryAssociation = BinaryAssociation(
    name="state1",
    ends={
        Property(name="fiacre_State", type=fiacre_Process, multiplicity=Multiplicity(1, 1)),
        Property(name="fiacre_Process", type=fiacre_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transition2: BinaryAssociation = BinaryAssociation(
    name="transition2",
    ends={
        Property(name="fiacre_Transition", type=fiacre_Process, multiplicity=Multiplicity(1, 1)),
        Property(name="fiacre_Process3", type=fiacre_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
variable4: BinaryAssociation = BinaryAssociation(
    name="variable4",
    ends={
        Property(name="Variable", type=fiacre_Process, multiplicity=Multiplicity(1, 1)),
        Property(name="process", type=fiacre_Variable, multiplicity=Multiplicity(0, 9999))
    }
)
transition0: BinaryAssociation = BinaryAssociation(
    name="transition0",
    ends={
        Property(name="Transition", type=fiacre_State, multiplicity=Multiplicity(1, 1)),
        Property(name="state", type=fiacre_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
process10: BinaryAssociation = BinaryAssociation(
    name="process10",
    ends={
        Property(name="fiacre_Process11", type=fiacre_Component, multiplicity=Multiplicity(1, 1)),
        Property(name="fiacre_Component", type=fiacre_Process, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
variable12: BinaryAssociation = BinaryAssociation(
    name="variable12",
    ends={
        Property(name="Variable13", type=fiacre_Component, multiplicity=Multiplicity(1, 1)),
        Property(name="component", type=fiacre_Variable, multiplicity=Multiplicity(0, 9999))
    }
)
state5: BinaryAssociation = BinaryAssociation(
    name="state5",
    ends={
        Property(name="State", type=fiacre_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="transition", type=fiacre_State, multiplicity=Multiplicity(0, 9999))
    }
)
datatype6: BinaryAssociation = BinaryAssociation(
    name="datatype6",
    ends={
        Property(name="fiacre_DataType", type=fiacre_Variable, multiplicity=Multiplicity(1, 1)),
        Property(name="fiacre_Variable", type=fiacre_DataType, multiplicity=Multiplicity(0, 1))
    }
)
process7: BinaryAssociation = BinaryAssociation(
    name="process7",
    ends={
        Property(name="Process", type=fiacre_Variable, multiplicity=Multiplicity(1, 1)),
        Property(name="variable", type=fiacre_Process, multiplicity=Multiplicity(0, 9999))
    }
)
component8: BinaryAssociation = BinaryAssociation(
    name="component8",
    ends={
        Property(name="Component", type=fiacre_Variable, multiplicity=Multiplicity(1, 1)),
        Property(name="variable9", type=fiacre_Component, multiplicity=Multiplicity(0, 9999))
    }
)
component14: BinaryAssociation = BinaryAssociation(
    name="component14",
    ends={
        Property(name="fiacre_Component15", type=fiacre_Program, multiplicity=Multiplicity(1, 1)),
        Property(name="fiacre_Program", type=fiacre_Component, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
variable16: BinaryAssociation = BinaryAssociation(
    name="variable16",
    ends={
        Property(name="fiacre_Variable18", type=fiacre_Program, multiplicity=Multiplicity(1, 1)),
        Property(name="fiacre_Program17", type=fiacre_Variable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
process19: BinaryAssociation = BinaryAssociation(
    name="process19",
    ends={
        Property(name="fiacre_Process21", type=fiacre_Program, multiplicity=Multiplicity(1, 1)),
        Property(name="fiacre_Program20", type=fiacre_Process, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_fiacre_State_EModelElement = Generalization(general=EModelElement, specific=fiacre_State)
gen_fiacre_Process_EModelElement = Generalization(general=EModelElement, specific=fiacre_Process)
gen_fiacre_Component_EModelElement = Generalization(general=EModelElement, specific=fiacre_Component)
gen_fiacre_Transition_EModelElement = Generalization(general=EModelElement, specific=fiacre_Transition)
gen_fiacre_DataType_EModelElement = Generalization(general=EModelElement, specific=fiacre_DataType)
gen_fiacre_Variable_EModelElement = Generalization(general=EModelElement, specific=fiacre_Variable)
gen_fiacre_Init_State = Generalization(general=State, specific=fiacre_Init)
gen_fiacre_Program_EModelElement = Generalization(general=EModelElement, specific=fiacre_Program)

# Domain Model
domain_model = DomainModel(
    name="fiacre",
    types={fiacre_Variable, fiacre_State, EModelElement, fiacre_Transition, fiacre_Process, fiacre_DataType, fiacre_Component, fiacre_Init, State, fiacre_Program},
    associations={state1, transition2, variable4, transition0, process10, variable12, state5, datatype6, process7, component8, component14, variable16, process19},
    generalizations={gen_fiacre_State_EModelElement, gen_fiacre_Process_EModelElement, gen_fiacre_Component_EModelElement, gen_fiacre_Transition_EModelElement, gen_fiacre_DataType_EModelElement, gen_fiacre_Variable_EModelElement, gen_fiacre_Init_State, gen_fiacre_Program_EModelElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)