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
LogicOperators: Enumeration = Enumeration(
    name="LogicOperators",
    literals={
            EnumerationLiteral(name="and_"),
			EnumerationLiteral(name="or_"),
			EnumerationLiteral(name="not_")
    }
)

MathOperators: Enumeration = Enumeration(
    name="MathOperators",
    literals={
            EnumerationLiteral(name="plus"),
			EnumerationLiteral(name="minus"),
			EnumerationLiteral(name="multiple"),
			EnumerationLiteral(name="divide")
    }
)

RelationalOperators: Enumeration = Enumeration(
    name="RelationalOperators",
    literals={
            EnumerationLiteral(name="lesser"),
			EnumerationLiteral(name="greater"),
			EnumerationLiteral(name="greater_or_equals"),
			EnumerationLiteral(name="lesser_or_equals"),
			EnumerationLiteral(name="not_equals"),
			EnumerationLiteral(name="equals")
    }
)

Classifier: Enumeration = Enumeration(
    name="Classifier",
    literals={
            EnumerationLiteral(name="Integer"),
			EnumerationLiteral(name="Double"),
			EnumerationLiteral(name="String"),
			EnumerationLiteral(name="Class")
    }
)

# Classes
Model_IPort = Class(name="Model_IPort")
Model_OPort = Class(name="Model_OPort")
Model_DEVS = Class(name="Model_DEVS", is_abstract=True)
Port = Class(name="Port")
Model_Port = Class(name="Model_Port", is_abstract=True)
Model_AtomicDEVS = Class(name="Model_AtomicDEVS")
DEVS = Class(name="DEVS")
Model_IntTransition = Class(name="Model_IntTransition")
Model_ConfTrans = Class(name="Model_ConfTrans")
Model_ExtTrans = Class(name="Model_ExtTrans")
Model_Phase = Class(name="Model_Phase")
Model_Variable = Class(name="Model_Variable")
Model_CoupledDEVS = Class(name="Model_CoupledDEVS")
Model_EIC = Class(name="Model_EIC")
Model_IC = Class(name="Model_IC")
Model_EOC = Class(name="Model_EOC")
Model_Property = Class(name="Model_Property")
PhaseTransition = Class(name="PhaseTransition")
Model_Event = Class(name="Model_Event")
Model_Predicate = Class(name="Model_Predicate", is_abstract=True)
Model_PhaseTransition = Class(name="Model_PhaseTransition", is_abstract=True)
Model_SimplePredicate = Class(name="Model_SimplePredicate")
Predicate = Class(name="Predicate")
Model_Expression = Class(name="Model_Expression")

# Model_IPort class attributes and methods

# Model_OPort class attributes and methods

# Model_DEVS class attributes and methods
Model_DEVS_name: Property = Property(name="name", type=StringType)
Model_DEVS.attributes={Model_DEVS_name}

# Port class attributes and methods

# Model_Port class attributes and methods
Model_Port_portId: Property = Property(name="portId", type=StringType)
Model_Port_portType: Property = Property(name="portType", type=StringType)
Model_Port.attributes={Model_Port_portType, Model_Port_portId}

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
Model_Variable_domain: Property = Property(name="domain", type=StringType)
Model_Variable.attributes={Model_Variable_domain, Model_Variable_name}

# Model_CoupledDEVS class attributes and methods

# Model_EIC class attributes and methods

# Model_IC class attributes and methods

# Model_EOC class attributes and methods

# Model_Property class attributes and methods

# PhaseTransition class attributes and methods

# Model_Event class attributes and methods

# Model_Predicate class attributes and methods

# Model_PhaseTransition class attributes and methods

# Model_SimplePredicate class attributes and methods
Model_SimplePredicate_operator: Property = Property(name="operator", type=StringType)
Model_SimplePredicate.attributes={Model_SimplePredicate_operator}

# Predicate class attributes and methods

# Model_Expression class attributes and methods
Model_Expression_operator: Property = Property(name="operator", type=StringType)
Model_Expression.attributes={Model_Expression_operator}

# Relationships
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
owner23: BinaryAssociation = BinaryAssociation(
    name="owner23",
    ends={
        Property(name="Model_DEVS24", type=Model_Port, multiplicity=Multiplicity(1, 1)),
        Property(name="Model_Port", type=Model_DEVS, multiplicity=Multiplicity(1, 1))
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
inputs51: BinaryAssociation = BinaryAssociation(
    name="inputs51",
    ends={
        Property(name="Model_Event53", type=Model_ExtTrans, multiplicity=Multiplicity(1, 1)),
        Property(name="Model_ExtTrans52", type=Model_Event, multiplicity=Multiplicity(0, 9999))
    }
)
targetPort54: BinaryAssociation = BinaryAssociation(
    name="targetPort54",
    ends={
        Property(name="Model_Port56", type=Model_Event, multiplicity=Multiplicity(1, 1)),
        Property(name="Model_Event55", type=Model_Port, multiplicity=Multiplicity(1, 1))
    }
)
proprty57: BinaryAssociation = BinaryAssociation(
    name="proprty57",
    ends={
        Property(name="Model_Property", type=Model_Phase, multiplicity=Multiplicity(1, 1)),
        Property(name="Model_Phase58", type=Model_Property, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
influencer25: BinaryAssociation = BinaryAssociation(
    name="influencer25",
    ends={
        Property(name="Model_IPort27", type=Model_EIC, multiplicity=Multiplicity(1, 1)),
        Property(name="Model_EIC26", type=Model_IPort, multiplicity=Multiplicity(1, 1))
    }
)
influencee28: BinaryAssociation = BinaryAssociation(
    name="influencee28",
    ends={
        Property(name="Model_IPort30", type=Model_EIC, multiplicity=Multiplicity(1, 1)),
        Property(name="Model_EIC29", type=Model_IPort, multiplicity=Multiplicity(1, 1))
    }
)
influencer31: BinaryAssociation = BinaryAssociation(
    name="influencer31",
    ends={
        Property(name="Model_OPort33", type=Model_IC, multiplicity=Multiplicity(1, 1)),
        Property(name="Model_IC32", type=Model_OPort, multiplicity=Multiplicity(0, 1))
    }
)
influencee34: BinaryAssociation = BinaryAssociation(
    name="influencee34",
    ends={
        Property(name="Model_IPort36", type=Model_IC, multiplicity=Multiplicity(1, 1)),
        Property(name="Model_IC35", type=Model_IPort, multiplicity=Multiplicity(0, 1))
    }
)
influencer37: BinaryAssociation = BinaryAssociation(
    name="influencer37",
    ends={
        Property(name="Model_OPort39", type=Model_EOC, multiplicity=Multiplicity(1, 1)),
        Property(name="Model_EOC38", type=Model_OPort, multiplicity=Multiplicity(0, 1))
    }
)
influencee40: BinaryAssociation = BinaryAssociation(
    name="influencee40",
    ends={
        Property(name="Model_OPort42", type=Model_EOC, multiplicity=Multiplicity(1, 1)),
        Property(name="Model_EOC41", type=Model_OPort, multiplicity=Multiplicity(0, 1))
    }
)
outputs43: BinaryAssociation = BinaryAssociation(
    name="outputs43",
    ends={
        Property(name="Model_Event", type=Model_IntTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="Model_IntTransition44", type=Model_Event, multiplicity=Multiplicity(0, 9999))
    }
)
outputs45: BinaryAssociation = BinaryAssociation(
    name="outputs45",
    ends={
        Property(name="Model_Event47", type=Model_ConfTrans, multiplicity=Multiplicity(1, 1)),
        Property(name="Model_ConfTrans46", type=Model_Event, multiplicity=Multiplicity(0, 9999))
    }
)
inputs48: BinaryAssociation = BinaryAssociation(
    name="inputs48",
    ends={
        Property(name="Model_Event50", type=Model_ConfTrans, multiplicity=Multiplicity(1, 1)),
        Property(name="Model_ConfTrans49", type=Model_Event, multiplicity=Multiplicity(0, 9999))
    }
)
predicates59: BinaryAssociation = BinaryAssociation(
    name="predicates59",
    ends={
        Property(name="Model_Predicate", type=Model_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="Model_Property60", type=Model_Predicate, multiplicity=Multiplicity(1, 9999))
    }
)
sourcePhase61: BinaryAssociation = BinaryAssociation(
    name="sourcePhase61",
    ends={
        Property(name="Model_Phase62", type=Model_PhaseTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="Model_PhaseTransition", type=Model_Phase, multiplicity=Multiplicity(1, 1))
    }
)
targetPhase63: BinaryAssociation = BinaryAssociation(
    name="targetPhase63",
    ends={
        Property(name="Model_Phase65", type=Model_PhaseTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="Model_PhaseTransition64", type=Model_Phase, multiplicity=Multiplicity(1, 1))
    }
)
variable66: BinaryAssociation = BinaryAssociation(
    name="variable66",
    ends={
        Property(name="Model_Variable67", type=Model_SimplePredicate, multiplicity=Multiplicity(1, 1)),
        Property(name="Model_SimplePredicate", type=Model_Variable, multiplicity=Multiplicity(1, 1))
    }
)
lhs68: BinaryAssociation = BinaryAssociation(
    name="lhs68",
    ends={
        Property(name="Model_Predicate69", type=Model_Expression, multiplicity=Multiplicity(1, 1)),
        Property(name="Model_Expression", type=Model_Predicate, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
rhs70: BinaryAssociation = BinaryAssociation(
    name="rhs70",
    ends={
        Property(name="Model_Predicate72", type=Model_Expression, multiplicity=Multiplicity(1, 1)),
        Property(name="Model_Expression71", type=Model_Predicate, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)

# Generalizations
gen_Model_IPort_Port = Generalization(general=Port, specific=Model_IPort)
gen_Model_OPort_Port = Generalization(general=Port, specific=Model_OPort)
gen_Model_AtomicDEVS_DEVS = Generalization(general=DEVS, specific=Model_AtomicDEVS)
gen_Model_CoupledDEVS_DEVS = Generalization(general=DEVS, specific=Model_CoupledDEVS)
gen_Model_IntTransition_PhaseTransition = Generalization(general=PhaseTransition, specific=Model_IntTransition)
gen_Model_ConfTrans_PhaseTransition = Generalization(general=PhaseTransition, specific=Model_ConfTrans)
gen_Model_ExtTrans_PhaseTransition = Generalization(general=PhaseTransition, specific=Model_ExtTrans)
gen_Model_SimplePredicate_Predicate = Generalization(general=Predicate, specific=Model_SimplePredicate)
gen_Model_Expression_Predicate = Generalization(general=Predicate, specific=Model_Expression)

# Domain Model
domain_model = DomainModel(
    name="Model",
    types={Model_IPort, Model_OPort, Model_DEVS, Port, Model_Port, Model_AtomicDEVS, DEVS, Model_IntTransition, Model_ConfTrans, Model_ExtTrans, Model_Phase, Model_Variable, Model_CoupledDEVS, Model_EIC, Model_IC, Model_EOC, Model_Property, PhaseTransition, Model_Event, Model_Predicate, Model_PhaseTransition, Model_SimplePredicate, Predicate, Model_Expression, LogicOperators, MathOperators, RelationalOperators, Classifier},
    associations={container1, iports2, oports4, owner23, deltaInt6, deltaConf7, deltaExt9, phases11, stateVars13, subModels15, eics17, ics19, eocs21, inputs51, targetPort54, proprty57, influencer25, influencee28, influencer31, influencee34, influencer37, influencee40, outputs43, outputs45, inputs48, predicates59, sourcePhase61, targetPhase63, variable66, lhs68, rhs70},
    generalizations={gen_Model_IPort_Port, gen_Model_OPort_Port, gen_Model_AtomicDEVS_DEVS, gen_Model_CoupledDEVS_DEVS, gen_Model_IntTransition_PhaseTransition, gen_Model_ConfTrans_PhaseTransition, gen_Model_ExtTrans_PhaseTransition, gen_Model_SimplePredicate_Predicate, gen_Model_Expression_Predicate},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)