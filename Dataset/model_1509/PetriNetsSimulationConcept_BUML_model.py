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
PetriNetSim_PetriNet = Class(name="PetriNetSim::PetriNet")
PetriNet = Class(name="PetriNet")
PetriNetSim_Place = Class(name="PetriNetSim::Place")
Place = Class(name="Place")
PetriNetSim_Transition = Class(name="PetriNetSim::Transition")
Transition = Class(name="Transition")

# PetriNetSim_PetriNet class attributes and methods
PetriNetSim_PetriNet_m_step: Method = Method(name="step", parameters={}, type=BooleanType)
PetriNetSim_PetriNet_m_simulate: Method = Method(name="simulate", parameters={})
PetriNetSim_PetriNet_m_pick: Method = Method(name="pick", parameters={Parameter(name='s')}, type=StringType)
PetriNetSim_PetriNet.methods={PetriNetSim_PetriNet_m_step, PetriNetSim_PetriNet_m_simulate, PetriNetSim_PetriNet_m_pick}

# PetriNet class attributes and methods

# PetriNetSim_Place class attributes and methods
PetriNetSim_Place_m_modify: Method = Method(name="modify", parameters={Parameter(name='t')}, type=BooleanType)
PetriNetSim_Place.methods={PetriNetSim_Place_m_modify}

# Place class attributes and methods

# PetriNetSim_Transition class attributes and methods
PetriNetSim_Transition_m_enabled: Method = Method(name="enabled", parameters={}, type=BooleanType)
PetriNetSim_Transition_m_fire: Method = Method(name="fire", parameters={}, type=BooleanType)
PetriNetSim_Transition.methods={PetriNetSim_Transition_m_fire, PetriNetSim_Transition_m_enabled}

# Transition class attributes and methods

# Generalizations
gen_PetriNetSim_PetriNet_PetriNet = Generalization(general=PetriNet, specific=PetriNetSim_PetriNet)
gen_PetriNetSim_Place_Place = Generalization(general=Place, specific=PetriNetSim_Place)
gen_PetriNetSim_Transition_Transition = Generalization(general=Transition, specific=PetriNetSim_Transition)

# Domain Model
domain_model = DomainModel(
    name="PetriNetSim",
    types={PetriNetSim_PetriNet, PetriNet, PetriNetSim_Place, Place, PetriNetSim_Transition, Transition},
    associations={},
    generalizations={gen_PetriNetSim_PetriNet_PetriNet, gen_PetriNetSim_Place_Place, gen_PetriNetSim_Transition_Transition},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)