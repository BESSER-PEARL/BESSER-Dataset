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
Model_DEVS = Class(name="Model::DEVS", is_abstract=True)
Model_EClassifier = Class(name="Model::EClassifier")
Model_IPort = Class(name="Model::IPort")
Model_OPort = Class(name="Model::OPort")
Model_AtomicDEVS = Class(name="Model::AtomicDEVS")
DEVS = Class(name="DEVS")
Model_IntTransition = Class(name="Model::IntTransition")
Model_ConfTrans = Class(name="Model::ConfTrans")
Model_ExtTrans = Class(name="Model::ExtTrans")
Model_Phase = Class(name="Model::Phase")
Model_Variable = Class(name="Model::Variable")
Model_CoupledDEVS = Class(name="Model::CoupledDEVS")
Model_EIC = Class(name="Model::EIC")
Model_IC = Class(name="Model::IC")
Model_EOC = Class(name="Model::EOC")
Port = Class(name="Port")
Model_Port = Class(name="Model::Port", is_abstract=True)
PhaseTransition = Class(name="PhaseTransition")
Model_Event = Class(name="Model::Event")
Model_PhaseTransition = Class(name="Model::PhaseTransition", is_abstract=True)

# Model_DEVS class attributes and methods
Model_DEVS_name: Property = Property(name="name", type=StringType)
Model_DEVS.attributes={Model_DEVS_name}

# Model_EClassifier class attributes and methods

# Model_IPort class attributes and methods

# Model_OPort class attributes and methods

# Model_AtomicDEVS class attributes and methods

# DEVS class attributes and methods

# Model_IntTransition class attributes and methods

# Model_ConfTrans class attributes and methods

# Model_ExtTrans class attributes and methods

# Model_Phase class attributes and methods
Model_Phase_phaseID: Property = Property(name="phaseID", type=StringType)
Model_Phase_timeAdvance: Property = Property(name="timeAdvance", type=FloatType)
Model_Phase.attributes={Model_Phase_timeAdvance, Model_Phase_phaseID}

# Model_Variable class attributes and methods
Model_Variable_name: Property = Property(name="name", type=StringType)
Model_Variable.attributes={Model_Variable_name}

# Model_CoupledDEVS class attributes and methods

# Model_EIC class attributes and methods

# Model_IC class attributes and methods

# Model_EOC class attributes and methods

# Port class attributes and methods

# Model_Port class attributes and methods
Model_Port_portId: Property = Property(name="portId", type=StringType)
Model_Port.attributes={Model_Port_portId}

# PhaseTransition class attributes and methods

# Model_Event class attributes and methods

# Model_PhaseTransition class attributes and methods

# Relationships
portType25: BinaryAssociation = BinaryAssociation(
    name="portType25",
    ends={
        Property(name="Model_EClassifier", type=Model_Port, multiplicity=Multiplicity(1, 1)),
        Property(name="Model_Port26", type=Model_EClassifier, multiplicity=Multiplicity(1, 1))
    }
)
container1: BinaryAssociation = BinaryAssociation(
    name="container1",
    ends={
        Property(name="Model_DEVS", type=Model_DEVS, multiplicity=Multiplicity(1, 1)),
        Property(name="Model_DEVS0", type=Model_DEVS, multiplicity=Multiplicity(0, 1))
    }
)
iports2: BinaryAssociation = BinaryAssociation(
    name="iports2",
    ends={
        Property(name="Model_IPort", type=Model_DEVS, multiplicity=Multiplicity(1, 1)),
        Property(name="Model_DEVS3", type=Model_IPort, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
oports4: BinaryAssociation = BinaryAssociation(
    name="oports4",
    ends={
        Property(name="Model_OPort", type=Model_DEVS, multiplicity=Multiplicity(1, 1)),
        Property(name="Model_DEVS5", type=Model_OPort, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
deltaInt6: BinaryAssociation = BinaryAssociation(
    name="deltaInt6",
    ends={
        Property(name="Model_IntTransition", type=Model_AtomicDEVS, multiplicity=Multiplicity(1, 1)),
        Property(name="Model_AtomicDEVS", type=Model_IntTransition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
deltaConf7: BinaryAssociation = BinaryAssociation(
    name="deltaConf7",
    ends={
        Property(name="Model_ConfTrans", type=Model_AtomicDEVS, multiplicity=Multiplicity(1, 1)),
        Property(name="Model_AtomicDEVS8", type=Model_ConfTrans, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
deltaExt9: BinaryAssociation = BinaryAssociation(
    name="deltaExt9",
    ends={
        Property(name="Model_ExtTrans", type=Model_AtomicDEVS, multiplicity=Multiplicity(1, 1)),
        Property(name="Model_AtomicDEVS10", type=Model_ExtTrans, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
phases11: BinaryAssociation = BinaryAssociation(
    name="phases11",
    ends={
        Property(name="Model_Phase", type=Model_AtomicDEVS, multiplicity=Multiplicity(1, 1)),
        Property(name="Model_AtomicDEVS12", type=Model_Phase, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
stateVars13: BinaryAssociation = BinaryAssociation(
    name="stateVars13",
    ends={
        Property(name="Model_Variable", type=Model_AtomicDEVS, multiplicity=Multiplicity(1, 1)),
        Property(name="Model_AtomicDEVS14", type=Model_Variable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
subModels15: BinaryAssociation = BinaryAssociation(
    name="subModels15",
    ends={
        Property(name="Model_DEVS16", type=Model_CoupledDEVS, multiplicity=Multiplicity(1, 1)),
        Property(name="Model_CoupledDEVS", type=Model_DEVS, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
eics17: BinaryAssociation = BinaryAssociation(
    name="eics17",
    ends={
        Property(name="Model_EIC", type=Model_CoupledDEVS, multiplicity=Multiplicity(1, 1)),
        Property(name="Model_CoupledDEVS18", type=Model_EIC, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ics19: BinaryAssociation = BinaryAssociation(
    name="ics19",
    ends={
        Property(name="Model_IC", type=Model_CoupledDEVS, multiplicity=Multiplicity(1, 1)),
        Property(name="Model_CoupledDEVS20", type=Model_IC, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eocs21: BinaryAssociation = BinaryAssociation(
    name="eocs21",
    ends={
        Property(name="Model_EOC", type=Model_CoupledDEVS, multiplicity=Multiplicity(1, 1)),
        Property(name="Model_CoupledDEVS22", type=Model_EOC, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
owner23: BinaryAssociation = BinaryAssociation(
    name="owner23",
    ends={
        Property(name="Model_DEVS24", type=Model_Port, multiplicity=Multiplicity(1, 1)),
        Property(name="Model_Port", type=Model_DEVS, multiplicity=Multiplicity(1, 1))
    }
)
influencer27: BinaryAssociation = BinaryAssociation(
    name="influencer27",
    ends={
        Property(name="Model_IPort29", type=Model_EIC, multiplicity=Multiplicity(1, 1)),
        Property(name="Model_EIC28", type=Model_IPort, multiplicity=Multiplicity(1, 1))
    }
)
influencee30: BinaryAssociation = BinaryAssociation(
    name="influencee30",
    ends={
        Property(name="Model_IPort32", type=Model_EIC, multiplicity=Multiplicity(1, 1)),
        Property(name="Model_EIC31", type=Model_IPort, multiplicity=Multiplicity(1, 1))
    }
)
influencer33: BinaryAssociation = BinaryAssociation(
    name="influencer33",
    ends={
        Property(name="Model_OPort35", type=Model_IC, multiplicity=Multiplicity(1, 1)),
        Property(name="Model_IC34", type=Model_OPort, multiplicity=Multiplicity(0, 1))
    }
)
influencee36: BinaryAssociation = BinaryAssociation(
    name="influencee36",
    ends={
        Property(name="Model_IPort38", type=Model_IC, multiplicity=Multiplicity(1, 1)),
        Property(name="Model_IC37", type=Model_IPort, multiplicity=Multiplicity(0, 1))
    }
)
influencer39: BinaryAssociation = BinaryAssociation(
    name="influencer39",
    ends={
        Property(name="Model_OPort41", type=Model_EOC, multiplicity=Multiplicity(1, 1)),
        Property(name="Model_EOC40", type=Model_OPort, multiplicity=Multiplicity(0, 1))
    }
)
influencee42: BinaryAssociation = BinaryAssociation(
    name="influencee42",
    ends={
        Property(name="Model_OPort44", type=Model_EOC, multiplicity=Multiplicity(1, 1)),
        Property(name="Model_EOC43", type=Model_OPort, multiplicity=Multiplicity(0, 1))
    }
)
outputs45: BinaryAssociation = BinaryAssociation(
    name="outputs45",
    ends={
        Property(name="Model_Event", type=Model_IntTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="Model_IntTransition46", type=Model_Event, multiplicity=Multiplicity(0, 9999))
    }
)
outputs47: BinaryAssociation = BinaryAssociation(
    name="outputs47",
    ends={
        Property(name="Model_Event49", type=Model_ConfTrans, multiplicity=Multiplicity(1, 1)),
        Property(name="Model_ConfTrans48", type=Model_Event, multiplicity=Multiplicity(0, 9999))
    }
)
inputs50: BinaryAssociation = BinaryAssociation(
    name="inputs50",
    ends={
        Property(name="Model_Event52", type=Model_ConfTrans, multiplicity=Multiplicity(1, 1)),
        Property(name="Model_ConfTrans51", type=Model_Event, multiplicity=Multiplicity(0, 9999))
    }
)
inputs53: BinaryAssociation = BinaryAssociation(
    name="inputs53",
    ends={
        Property(name="Model_Event55", type=Model_ExtTrans, multiplicity=Multiplicity(1, 1)),
        Property(name="Model_ExtTrans54", type=Model_Event, multiplicity=Multiplicity(0, 9999))
    }
)
targetPort56: BinaryAssociation = BinaryAssociation(
    name="targetPort56",
    ends={
        Property(name="Model_Port58", type=Model_Event, multiplicity=Multiplicity(1, 1)),
        Property(name="Model_Event57", type=Model_Port, multiplicity=Multiplicity(1, 1))
    }
)
value59: BinaryAssociation = BinaryAssociation(
    name="value59",
    ends={
        Property(name="Model_EClassifier61", type=Model_Event, multiplicity=Multiplicity(1, 1)),
        Property(name="Model_Event60", type=Model_EClassifier, multiplicity=Multiplicity(1, 1))
    }
)
predicates62: BinaryAssociation = BinaryAssociation(
    name="predicates62",
    ends={
        Property(name="Model_Variable64", type=Model_Phase, multiplicity=Multiplicity(1, 1)),
        Property(name="Model_Phase63", type=Model_Variable, multiplicity=Multiplicity(1, 9999))
    }
)
sourcePhase65: BinaryAssociation = BinaryAssociation(
    name="sourcePhase65",
    ends={
        Property(name="Model_Phase66", type=Model_PhaseTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="Model_PhaseTransition", type=Model_Phase, multiplicity=Multiplicity(1, 1))
    }
)
targetPhase67: BinaryAssociation = BinaryAssociation(
    name="targetPhase67",
    ends={
        Property(name="Model_Phase69", type=Model_PhaseTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="Model_PhaseTransition68", type=Model_Phase, multiplicity=Multiplicity(1, 1))
    }
)
domain70: BinaryAssociation = BinaryAssociation(
    name="domain70",
    ends={
        Property(name="Model_EClassifier72", type=Model_Variable, multiplicity=Multiplicity(1, 1)),
        Property(name="Model_Variable71", type=Model_EClassifier, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_Model_AtomicDEVS_DEVS = Generalization(general=DEVS, specific=Model_AtomicDEVS)
gen_Model_CoupledDEVS_DEVS = Generalization(general=DEVS, specific=Model_CoupledDEVS)
gen_Model_IPort_Port = Generalization(general=Port, specific=Model_IPort)
gen_Model_OPort_Port = Generalization(general=Port, specific=Model_OPort)
gen_Model_IntTransition_PhaseTransition = Generalization(general=PhaseTransition, specific=Model_IntTransition)
gen_Model_ConfTrans_PhaseTransition = Generalization(general=PhaseTransition, specific=Model_ConfTrans)
gen_Model_ExtTrans_PhaseTransition = Generalization(general=PhaseTransition, specific=Model_ExtTrans)

# Domain Model
domain_model = DomainModel(
    name="Model",
    types={Model_DEVS, Model_EClassifier, Model_IPort, Model_OPort, Model_AtomicDEVS, DEVS, Model_IntTransition, Model_ConfTrans, Model_ExtTrans, Model_Phase, Model_Variable, Model_CoupledDEVS, Model_EIC, Model_IC, Model_EOC, Port, Model_Port, PhaseTransition, Model_Event, Model_PhaseTransition},
    associations={portType25, container1, iports2, oports4, deltaInt6, deltaConf7, deltaExt9, phases11, stateVars13, subModels15, eics17, ics19, eocs21, owner23, influencer27, influencee30, influencer33, influencee36, influencer39, influencee42, outputs45, outputs47, inputs50, inputs53, targetPort56, value59, predicates62, sourcePhase65, targetPhase67, domain70},
    generalizations={gen_Model_AtomicDEVS_DEVS, gen_Model_CoupledDEVS_DEVS, gen_Model_IPort_Port, gen_Model_OPort_Port, gen_Model_IntTransition_PhaseTransition, gen_Model_ConfTrans_PhaseTransition, gen_Model_ExtTrans_PhaseTransition},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)