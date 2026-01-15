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
GateType: Enumeration = Enumeration(
    name="GateType",
    literals={
            EnumerationLiteral(name="OR"),
			EnumerationLiteral(name="AND"),
			EnumerationLiteral(name="NOT"),
			EnumerationLiteral(name="XOR"),
			EnumerationLiteral(name="VOTE"),
			EnumerationLiteral(name="PAND"),
			EnumerationLiteral(name="POR"),
			EnumerationLiteral(name="SAND"),
			EnumerationLiteral(name="InputEvent"),
			EnumerationLiteral(name="OutputEvent")
    }
)

FailureOriginType: Enumeration = Enumeration(
    name="FailureOriginType",
    literals={
            EnumerationLiteral(name="Input"),
			EnumerationLiteral(name="Output"),
			EnumerationLiteral(name="Internal")
    }
)

FMEAType: Enumeration = Enumeration(
    name="FMEAType",
    literals={
            EnumerationLiteral(name="FMEA"),
			EnumerationLiteral(name="FMEDA")
    }
)

CauseType: Enumeration = Enumeration(
    name="CauseType",
    literals={
            EnumerationLiteral(name="InputEvent"),
			EnumerationLiteral(name="OutputEvent"),
			EnumerationLiteral(name="BasicEvent"),
			EnumerationLiteral(name="Gate")
    }
)

# Classes
failureLogic_FailureLogicPackage = Class(name="failureLogic::FailureLogicPackage")
failureLogic_FailureModel = Class(name="failureLogic::FailureModel")
failureLogic_MinimalCutset = Class(name="failureLogic::MinimalCutset")
failureLogic_ProbDistParam = Class(name="failureLogic::ProbDistParam")
failureLogic_Failure = Class(name="failureLogic::Failure")
BaseElement = Class(name="BaseElement")
failureLogic_ProbDist = Class(name="failureLogic::ProbDist")
failureLogic_SecurityViolation = Class(name="failureLogic::SecurityViolation")
Failure = Class(name="Failure")
failureLogic_MinimalCutSets = Class(name="failureLogic::MinimalCutSets")
failureLogic_Markov_MarkovChain = Class(name="failureLogic::Markov::MarkovChain")
Transition = Class(name="Transition")
State = Class(name="State")
failureLogic_Markov_State = Class(name="failureLogic::Markov::State")
Markov_failureLogic_Failure = Class(name="Markov::failureLogic::Failure")
failureLogic_Markov_Transition = Class(name="failureLogic::Markov::Transition")
Markov_failureLogic_ProbDist = Class(name="Markov::failureLogic::ProbDist")
failureLogic_FMEA_FMEA = Class(name="failureLogic::FMEA::FMEA")
FMEAEntry = Class(name="FMEAEntry")
failureLogic_FTA_FaultTree = Class(name="failureLogic::FTA::FaultTree")
FailureModel = Class(name="FailureModel")
Cause = Class(name="Cause")
failureLogic_FTA_Cause = Class(name="failureLogic::FTA::Cause")
FTA_failureLogic_Failure = Class(name="FTA::failureLogic::Failure")
failureLogic_FTA_Gate = Class(name="failureLogic::FTA::Gate")
failureLogic_FMEA_FMEAEntry = Class(name="failureLogic::FMEA::FMEAEntry")
FMEA_failureLogic_Failure = Class(name="FMEA::failureLogic::Failure")
failureLogic_FMEA_FMEDAEntry = Class(name="failureLogic::FMEA::FMEDAEntry")
FMEA_failureLogic_ProbDist = Class(name="FMEA::failureLogic::ProbDist")

# failureLogic_FailureLogicPackage class attributes and methods

# failureLogic_FailureModel class attributes and methods

# failureLogic_MinimalCutset class attributes and methods

# failureLogic_ProbDistParam class attributes and methods
failureLogic_ProbDistParam_value: Property = Property(name="value", type=StringType)
failureLogic_ProbDistParam.attributes={failureLogic_ProbDistParam_value}

# failureLogic_Failure class attributes and methods
failureLogic_Failure_originType: Property = Property(name="originType", type=StringType)
failureLogic_Failure_failureClass: Property = Property(name="failureClass", type=StringType)
failureLogic_Failure_failureRate: Property = Property(name="failureRate", type=FloatType)
failureLogic_Failure_isCcf: Property = Property(name="isCcf", type=BooleanType)
failureLogic_Failure.attributes={failureLogic_Failure_originType, failureLogic_Failure_failureRate, failureLogic_Failure_failureClass, failureLogic_Failure_isCcf}

# BaseElement class attributes and methods

# failureLogic_ProbDist class attributes and methods
failureLogic_ProbDist_type: Property = Property(name="type", type=StringType)
failureLogic_ProbDist.attributes={failureLogic_ProbDist_type}

# failureLogic_SecurityViolation class attributes and methods

# Failure class attributes and methods

# failureLogic_MinimalCutSets class attributes and methods

# failureLogic_Markov_MarkovChain class attributes and methods

# Transition class attributes and methods

# State class attributes and methods

# failureLogic_Markov_State class attributes and methods
failureLogic_Markov_State_isInitialState: Property = Property(name="isInitialState", type=BooleanType)
failureLogic_Markov_State_isFailState: Property = Property(name="isFailState", type=BooleanType)
failureLogic_Markov_State.attributes={failureLogic_Markov_State_isFailState, failureLogic_Markov_State_isInitialState}

# Markov_failureLogic_Failure class attributes and methods

# failureLogic_Markov_Transition class attributes and methods
failureLogic_Markov_Transition_transition: Property = Property(name="transition", type=FloatType)
failureLogic_Markov_Transition.attributes={failureLogic_Markov_Transition_transition}

# Markov_failureLogic_ProbDist class attributes and methods

# failureLogic_FMEA_FMEA class attributes and methods
failureLogic_FMEA_FMEA_type: Property = Property(name="type", type=StringType)
failureLogic_FMEA_FMEA.attributes={failureLogic_FMEA_FMEA_type}

# FMEAEntry class attributes and methods

# failureLogic_FTA_FaultTree class attributes and methods

# FailureModel class attributes and methods

# Cause class attributes and methods

# failureLogic_FTA_Cause class attributes and methods
failureLogic_FTA_Cause_type: Property = Property(name="type", type=StringType)
failureLogic_FTA_Cause.attributes={failureLogic_FTA_Cause_type}

# FTA_failureLogic_Failure class attributes and methods

# failureLogic_FTA_Gate class attributes and methods
failureLogic_FTA_Gate_gateType: Property = Property(name="gateType", type=StringType)
failureLogic_FTA_Gate.attributes={failureLogic_FTA_Gate_gateType}

# failureLogic_FMEA_FMEAEntry class attributes and methods

# FMEA_failureLogic_Failure class attributes and methods

# failureLogic_FMEA_FMEDAEntry class attributes and methods
failureLogic_FMEA_FMEDAEntry_diagnosisRate: Property = Property(name="diagnosisRate", type=FloatType)
failureLogic_FMEA_FMEDAEntry.attributes={failureLogic_FMEA_FMEDAEntry_diagnosisRate}

# FMEA_failureLogic_ProbDist class attributes and methods

# Relationships
failureModels0: BinaryAssociation = BinaryAssociation(
    name="failureModels0",
    ends={
        Property(name="failureLogic_FailureModel", type=failureLogic_FailureLogicPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="failureLogic_FailureLogicPackage", type=failureLogic_FailureModel, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
failures7: BinaryAssociation = BinaryAssociation(
    name="failures7",
    ends={
        Property(name="failureLogic_Failure9", type=failureLogic_FailureModel, multiplicity=Multiplicity(1, 1)),
        Property(name="failureLogic_FailureModel8", type=failureLogic_Failure, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
subModels11: BinaryAssociation = BinaryAssociation(
    name="subModels11",
    ends={
        Property(name="failureLogic_FailureModel12", type=failureLogic_FailureModel, multiplicity=Multiplicity(1, 1)),
        Property(name="failureLogic_FailureModel10", type=failureLogic_FailureModel, multiplicity=Multiplicity(0, 9999))
    }
)
cutsets13: BinaryAssociation = BinaryAssociation(
    name="cutsets13",
    ends={
        Property(name="failureLogic_MinimalCutset", type=failureLogic_MinimalCutSets, multiplicity=Multiplicity(1, 1)),
        Property(name="failureLogic_MinimalCutSets14", type=failureLogic_MinimalCutset, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
failures15: BinaryAssociation = BinaryAssociation(
    name="failures15",
    ends={
        Property(name="failureLogic_Failure17", type=failureLogic_MinimalCutSets, multiplicity=Multiplicity(1, 1)),
        Property(name="failureLogic_MinimalCutSets16", type=failureLogic_Failure, multiplicity=Multiplicity(0, 9999))
    }
)
failures18: BinaryAssociation = BinaryAssociation(
    name="failures18",
    ends={
        Property(name="failureLogic_Failure20", type=failureLogic_MinimalCutset, multiplicity=Multiplicity(1, 1)),
        Property(name="failureLogic_MinimalCutset19", type=failureLogic_Failure, multiplicity=Multiplicity(0, 9999))
    }
)
parameters21: BinaryAssociation = BinaryAssociation(
    name="parameters21",
    ends={
        Property(name="failureLogic_ProbDistParam", type=failureLogic_ProbDist, multiplicity=Multiplicity(1, 1)),
        Property(name="failureLogic_ProbDist22", type=failureLogic_ProbDistParam, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
failureProbDistribution1: BinaryAssociation = BinaryAssociation(
    name="failureProbDistribution1",
    ends={
        Property(name="failureLogic_ProbDist", type=failureLogic_Failure, multiplicity=Multiplicity(1, 1)),
        Property(name="failureLogic_Failure", type=failureLogic_ProbDist, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ccfFailures3: BinaryAssociation = BinaryAssociation(
    name="ccfFailures3",
    ends={
        Property(name="failureLogic_Failure4", type=failureLogic_Failure, multiplicity=Multiplicity(1, 1)),
        Property(name="failureLogic_Failure2", type=failureLogic_Failure, multiplicity=Multiplicity(0, 9999))
    }
)
minimalCutsets5: BinaryAssociation = BinaryAssociation(
    name="minimalCutsets5",
    ends={
        Property(name="failureLogic_MinimalCutSets", type=failureLogic_FailureModel, multiplicity=Multiplicity(1, 1)),
        Property(name="failureLogic_FailureModel6", type=failureLogic_MinimalCutSets, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transitions27: BinaryAssociation = BinaryAssociation(
    name="transitions27",
    ends={
        Property(name="Transition", type=failureLogic_Markov_MarkovChain, multiplicity=Multiplicity(1, 1)),
        Property(name="failureLogic_Markov_MarkovChain", type=Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
states28: BinaryAssociation = BinaryAssociation(
    name="states28",
    ends={
        Property(name="State", type=failureLogic_Markov_MarkovChain, multiplicity=Multiplicity(1, 1)),
        Property(name="failureLogic_Markov_MarkovChain29", type=State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
failState30: BinaryAssociation = BinaryAssociation(
    name="failState30",
    ends={
        Property(name="Markov_failureLogic_Failure", type=failureLogic_Markov_State, multiplicity=Multiplicity(1, 1)),
        Property(name="failureLogic_Markov_State", type=Markov_failureLogic_Failure, multiplicity=Multiplicity(0, 1))
    }
)
transitionProbDistribution31: BinaryAssociation = BinaryAssociation(
    name="transitionProbDistribution31",
    ends={
        Property(name="Markov_failureLogic_ProbDist", type=failureLogic_Markov_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="failureLogic_Markov_Transition", type=Markov_failureLogic_ProbDist, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
fromStates32: BinaryAssociation = BinaryAssociation(
    name="fromStates32",
    ends={
        Property(name="State34", type=failureLogic_Markov_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="failureLogic_Markov_Transition33", type=State, multiplicity=Multiplicity(0, 9999))
    }
)
toStates35: BinaryAssociation = BinaryAssociation(
    name="toStates35",
    ends={
        Property(name="State37", type=failureLogic_Markov_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="failureLogic_Markov_Transition36", type=State, multiplicity=Multiplicity(0, 9999))
    }
)
causes23: BinaryAssociation = BinaryAssociation(
    name="causes23",
    ends={
        Property(name="Cause", type=failureLogic_FTA_FaultTree, multiplicity=Multiplicity(1, 1)),
        Property(name="failureLogic_FTA_FaultTree", type=Cause, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
failure24: BinaryAssociation = BinaryAssociation(
    name="failure24",
    ends={
        Property(name="FTA_failureLogic_Failure", type=failureLogic_FTA_Cause, multiplicity=Multiplicity(1, 1)),
        Property(name="failureLogic_FTA_Cause", type=FTA_failureLogic_Failure, multiplicity=Multiplicity(0, 1))
    }
)
causes25: BinaryAssociation = BinaryAssociation(
    name="causes25",
    ends={
        Property(name="Cause26", type=failureLogic_FTA_Gate, multiplicity=Multiplicity(1, 1)),
        Property(name="failureLogic_FTA_Gate", type=Cause, multiplicity=Multiplicity(0, 9999))
    }
)
entries38: BinaryAssociation = BinaryAssociation(
    name="entries38",
    ends={
        Property(name="FMEAEntry", type=failureLogic_FMEA_FMEA, multiplicity=Multiplicity(1, 1)),
        Property(name="failureLogic_FMEA_FMEA", type=FMEAEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
effect39: BinaryAssociation = BinaryAssociation(
    name="effect39",
    ends={
        Property(name="FMEA_failureLogic_Failure", type=failureLogic_FMEA_FMEAEntry, multiplicity=Multiplicity(1, 1)),
        Property(name="failureLogic_FMEA_FMEAEntry", type=FMEA_failureLogic_Failure, multiplicity=Multiplicity(0, 1))
    }
)
mode40: BinaryAssociation = BinaryAssociation(
    name="mode40",
    ends={
        Property(name="FMEA_failureLogic_Failure42", type=failureLogic_FMEA_FMEAEntry, multiplicity=Multiplicity(1, 1)),
        Property(name="failureLogic_FMEA_FMEAEntry41", type=FMEA_failureLogic_Failure, multiplicity=Multiplicity(0, 1))
    }
)
diagnosisProbDistribution43: BinaryAssociation = BinaryAssociation(
    name="diagnosisProbDistribution43",
    ends={
        Property(name="FMEA_failureLogic_ProbDist", type=failureLogic_FMEA_FMEDAEntry, multiplicity=Multiplicity(1, 1)),
        Property(name="failureLogic_FMEA_FMEDAEntry", type=FMEA_failureLogic_ProbDist, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_failureLogic_MinimalCutSets_BaseElement = Generalization(general=BaseElement, specific=failureLogic_MinimalCutSets)
gen_failureLogic_MinimalCutset_BaseElement = Generalization(general=BaseElement, specific=failureLogic_MinimalCutset)
gen_failureLogic_ProbDist_BaseElement = Generalization(general=BaseElement, specific=failureLogic_ProbDist)
gen_failureLogic_ProbDistParam_BaseElement = Generalization(general=BaseElement, specific=failureLogic_ProbDistParam)
gen_failureLogic_Failure_BaseElement = Generalization(general=BaseElement, specific=failureLogic_Failure)
gen_failureLogic_SecurityViolation_Failure = Generalization(general=Failure, specific=failureLogic_SecurityViolation)
gen_failureLogic_FailureModel_BaseElement = Generalization(general=BaseElement, specific=failureLogic_FailureModel)
gen_failureLogic_Markov_MarkovChain_FailureModel = Generalization(general=FailureModel, specific=failureLogic_Markov_MarkovChain)
gen_failureLogic_Markov_State_BaseElement = Generalization(general=BaseElement, specific=failureLogic_Markov_State)
gen_failureLogic_Markov_Transition_BaseElement = Generalization(general=BaseElement, specific=failureLogic_Markov_Transition)
gen_failureLogic_FMEA_FMEA_FailureModel = Generalization(general=FailureModel, specific=failureLogic_FMEA_FMEA)
gen_failureLogic_FTA_FaultTree_FailureModel = Generalization(general=FailureModel, specific=failureLogic_FTA_FaultTree)
gen_failureLogic_FTA_Cause_BaseElement = Generalization(general=BaseElement, specific=failureLogic_FTA_Cause)
gen_failureLogic_FTA_Gate_Cause = Generalization(general=Cause, specific=failureLogic_FTA_Gate)
gen_failureLogic_FMEA_FMEAEntry_BaseElement = Generalization(general=BaseElement, specific=failureLogic_FMEA_FMEAEntry)
gen_failureLogic_FMEA_FMEDAEntry_FMEAEntry = Generalization(general=FMEAEntry, specific=failureLogic_FMEA_FMEDAEntry)

# Domain Model
domain_model = DomainModel(
    name="failureLogic",
    types={failureLogic_FailureLogicPackage, failureLogic_FailureModel, failureLogic_MinimalCutset, failureLogic_ProbDistParam, failureLogic_Failure, BaseElement, failureLogic_ProbDist, failureLogic_SecurityViolation, Failure, failureLogic_MinimalCutSets, failureLogic_Markov_MarkovChain, Transition, State, failureLogic_Markov_State, Markov_failureLogic_Failure, failureLogic_Markov_Transition, Markov_failureLogic_ProbDist, failureLogic_FMEA_FMEA, FMEAEntry, failureLogic_FTA_FaultTree, FailureModel, Cause, failureLogic_FTA_Cause, FTA_failureLogic_Failure, failureLogic_FTA_Gate, failureLogic_FMEA_FMEAEntry, FMEA_failureLogic_Failure, failureLogic_FMEA_FMEDAEntry, FMEA_failureLogic_ProbDist, GateType, FailureOriginType, FMEAType, CauseType},
    associations={failureModels0, failures7, subModels11, cutsets13, failures15, failures18, parameters21, failureProbDistribution1, ccfFailures3, minimalCutsets5, transitions27, states28, failState30, transitionProbDistribution31, fromStates32, toStates35, causes23, failure24, causes25, entries38, effect39, mode40, diagnosisProbDistribution43},
    generalizations={gen_failureLogic_MinimalCutSets_BaseElement, gen_failureLogic_MinimalCutset_BaseElement, gen_failureLogic_ProbDist_BaseElement, gen_failureLogic_ProbDistParam_BaseElement, gen_failureLogic_Failure_BaseElement, gen_failureLogic_SecurityViolation_Failure, gen_failureLogic_FailureModel_BaseElement, gen_failureLogic_Markov_MarkovChain_FailureModel, gen_failureLogic_Markov_State_BaseElement, gen_failureLogic_Markov_Transition_BaseElement, gen_failureLogic_FMEA_FMEA_FailureModel, gen_failureLogic_FTA_FaultTree_FailureModel, gen_failureLogic_FTA_Cause_BaseElement, gen_failureLogic_FTA_Gate_Cause, gen_failureLogic_FMEA_FMEAEntry_BaseElement, gen_failureLogic_FMEA_FMEDAEntry_FMEAEntry},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)