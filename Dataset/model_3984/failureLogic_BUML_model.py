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
FailureOriginType: Enumeration = Enumeration(
    name="FailureOriginType",
    literals={
            EnumerationLiteral(name="Input"),
			EnumerationLiteral(name="Output"),
			EnumerationLiteral(name="Internal")
    }
)

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

CauseType: Enumeration = Enumeration(
    name="CauseType",
    literals={
            EnumerationLiteral(name="InputEvent"),
			EnumerationLiteral(name="OutputEvent"),
			EnumerationLiteral(name="BasicEvent"),
			EnumerationLiteral(name="Gate")
    }
)

FMEAType: Enumeration = Enumeration(
    name="FMEAType",
    literals={
            EnumerationLiteral(name="FMEA"),
			EnumerationLiteral(name="FMEDA")
    }
)

# Classes
failureLogic_FailureLogicPackage = Class(name="failureLogic::FailureLogicPackage")
ODEProductPackage = Class(name="ODEProductPackage")
failureLogic_MinimalCutSets = Class(name="failureLogic::MinimalCutSets")
failureLogic_MinimalCutset = Class(name="failureLogic::MinimalCutset")
failureLogic_ProbDistParam = Class(name="failureLogic::ProbDistParam")
failureLogic_FailureModel = Class(name="failureLogic::FailureModel")
failureLogic_Failure = Class(name="failureLogic::Failure")
BaseElement = Class(name="BaseElement")
failureLogic_ProbDist = Class(name="failureLogic::ProbDist")
failureLogic_SecurityViolation = Class(name="failureLogic::SecurityViolation")
Failure = Class(name="Failure")
failureLogic_FaultTree = Class(name="failureLogic::FaultTree")
FailureModel = Class(name="FailureModel")
failureLogic_Cause = Class(name="failureLogic::Cause")
failureLogic_Gate = Class(name="failureLogic::Gate")
Cause = Class(name="Cause")
failureLogic_MarkovChain = Class(name="failureLogic::MarkovChain")
failureLogic_Transition = Class(name="failureLogic::Transition")
failureLogic_State = Class(name="failureLogic::State")
failureLogic_FMEDAEntry = Class(name="failureLogic::FMEDAEntry")
FMEAEntry = Class(name="FMEAEntry")
failureLogic_FMEA = Class(name="failureLogic::FMEA")
failureLogic_FMEAEntry = Class(name="failureLogic::FMEAEntry")

# failureLogic_FailureLogicPackage class attributes and methods

# ODEProductPackage class attributes and methods

# failureLogic_MinimalCutSets class attributes and methods

# failureLogic_MinimalCutset class attributes and methods

# failureLogic_ProbDistParam class attributes and methods
failureLogic_ProbDistParam_value: Property = Property(name="value", type=StringType)
failureLogic_ProbDistParam.attributes={failureLogic_ProbDistParam_value}

# failureLogic_FailureModel class attributes and methods

# failureLogic_Failure class attributes and methods
failureLogic_Failure_originType: Property = Property(name="originType", type=StringType)
failureLogic_Failure_failureClass: Property = Property(name="failureClass", type=StringType)
failureLogic_Failure_failureRate: Property = Property(name="failureRate", type=FloatType)
failureLogic_Failure_isCcf: Property = Property(name="isCcf", type=BooleanType)
failureLogic_Failure.attributes={failureLogic_Failure_failureClass, failureLogic_Failure_isCcf, failureLogic_Failure_originType, failureLogic_Failure_failureRate}

# BaseElement class attributes and methods

# failureLogic_ProbDist class attributes and methods
failureLogic_ProbDist_type: Property = Property(name="type", type=StringType)
failureLogic_ProbDist.attributes={failureLogic_ProbDist_type}

# failureLogic_SecurityViolation class attributes and methods

# Failure class attributes and methods

# failureLogic_FaultTree class attributes and methods

# FailureModel class attributes and methods

# failureLogic_Cause class attributes and methods
failureLogic_Cause_causeType: Property = Property(name="causeType", type=StringType)
failureLogic_Cause.attributes={failureLogic_Cause_causeType}

# failureLogic_Gate class attributes and methods
failureLogic_Gate_gateType: Property = Property(name="gateType", type=StringType)
failureLogic_Gate.attributes={failureLogic_Gate_gateType}

# Cause class attributes and methods

# failureLogic_MarkovChain class attributes and methods

# failureLogic_Transition class attributes and methods
failureLogic_Transition_transition: Property = Property(name="transition", type=FloatType)
failureLogic_Transition.attributes={failureLogic_Transition_transition}

# failureLogic_State class attributes and methods
failureLogic_State_isInitialState: Property = Property(name="isInitialState", type=BooleanType)
failureLogic_State_isFailState: Property = Property(name="isFailState", type=BooleanType)
failureLogic_State.attributes={failureLogic_State_isFailState, failureLogic_State_isInitialState}

# failureLogic_FMEDAEntry class attributes and methods
failureLogic_FMEDAEntry_diagnosisRate: Property = Property(name="diagnosisRate", type=FloatType)
failureLogic_FMEDAEntry.attributes={failureLogic_FMEDAEntry_diagnosisRate}

# FMEAEntry class attributes and methods

# failureLogic_FMEA class attributes and methods
failureLogic_FMEA_type: Property = Property(name="type", type=StringType)
failureLogic_FMEA.attributes={failureLogic_FMEA_type}

# failureLogic_FMEAEntry class attributes and methods

# Relationships
minimalCutsets5: BinaryAssociation = BinaryAssociation(
    name="minimalCutsets5",
    ends={
        Property(name="failureLogic_MinimalCutSets", type=failureLogic_FailureModel, multiplicity=Multiplicity(1, 1)),
        Property(name="failureLogic_FailureModel6", type=failureLogic_MinimalCutSets, multiplicity=Multiplicity(0, 9999), is_composite=True)
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
failureModels0: BinaryAssociation = BinaryAssociation(
    name="failureModels0",
    ends={
        Property(name="failureLogic_FailureModel", type=failureLogic_FailureLogicPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="failureLogic_FailureLogicPackage", type=failureLogic_FailureModel, multiplicity=Multiplicity(0, 9999), is_composite=True)
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
causes23: BinaryAssociation = BinaryAssociation(
    name="causes23",
    ends={
        Property(name="failureLogic_Cause", type=failureLogic_FaultTree, multiplicity=Multiplicity(1, 1)),
        Property(name="failureLogic_FaultTree", type=failureLogic_Cause, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
failure24: BinaryAssociation = BinaryAssociation(
    name="failure24",
    ends={
        Property(name="failureLogic_Failure26", type=failureLogic_Cause, multiplicity=Multiplicity(1, 1)),
        Property(name="failureLogic_Cause25", type=failureLogic_Failure, multiplicity=Multiplicity(0, 1))
    }
)
causes27: BinaryAssociation = BinaryAssociation(
    name="causes27",
    ends={
        Property(name="failureLogic_Cause28", type=failureLogic_Gate, multiplicity=Multiplicity(1, 1)),
        Property(name="failureLogic_Gate", type=failureLogic_Cause, multiplicity=Multiplicity(0, 9999))
    }
)
transitions29: BinaryAssociation = BinaryAssociation(
    name="transitions29",
    ends={
        Property(name="failureLogic_Transition", type=failureLogic_MarkovChain, multiplicity=Multiplicity(1, 1)),
        Property(name="failureLogic_MarkovChain", type=failureLogic_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
states30: BinaryAssociation = BinaryAssociation(
    name="states30",
    ends={
        Property(name="failureLogic_State", type=failureLogic_MarkovChain, multiplicity=Multiplicity(1, 1)),
        Property(name="failureLogic_MarkovChain31", type=failureLogic_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
failState32: BinaryAssociation = BinaryAssociation(
    name="failState32",
    ends={
        Property(name="failureLogic_Failure34", type=failureLogic_State, multiplicity=Multiplicity(1, 1)),
        Property(name="failureLogic_State33", type=failureLogic_Failure, multiplicity=Multiplicity(0, 1))
    }
)
effect45: BinaryAssociation = BinaryAssociation(
    name="effect45",
    ends={
        Property(name="failureLogic_Failure47", type=failureLogic_FMEAEntry, multiplicity=Multiplicity(1, 1)),
        Property(name="failureLogic_FMEAEntry46", type=failureLogic_Failure, multiplicity=Multiplicity(0, 1))
    }
)
mode48: BinaryAssociation = BinaryAssociation(
    name="mode48",
    ends={
        Property(name="failureLogic_Failure50", type=failureLogic_FMEAEntry, multiplicity=Multiplicity(1, 1)),
        Property(name="failureLogic_FMEAEntry49", type=failureLogic_Failure, multiplicity=Multiplicity(0, 1))
    }
)
diagnosisProbDistribution51: BinaryAssociation = BinaryAssociation(
    name="diagnosisProbDistribution51",
    ends={
        Property(name="failureLogic_ProbDist52", type=failureLogic_FMEDAEntry, multiplicity=Multiplicity(1, 1)),
        Property(name="failureLogic_FMEDAEntry", type=failureLogic_ProbDist, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
transitionProbDistribution35: BinaryAssociation = BinaryAssociation(
    name="transitionProbDistribution35",
    ends={
        Property(name="failureLogic_ProbDist37", type=failureLogic_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="failureLogic_Transition36", type=failureLogic_ProbDist, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
fromStates38: BinaryAssociation = BinaryAssociation(
    name="fromStates38",
    ends={
        Property(name="failureLogic_State40", type=failureLogic_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="failureLogic_Transition39", type=failureLogic_State, multiplicity=Multiplicity(0, 9999))
    }
)
toStates41: BinaryAssociation = BinaryAssociation(
    name="toStates41",
    ends={
        Property(name="failureLogic_State43", type=failureLogic_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="failureLogic_Transition42", type=failureLogic_State, multiplicity=Multiplicity(0, 9999))
    }
)
entries44: BinaryAssociation = BinaryAssociation(
    name="entries44",
    ends={
        Property(name="failureLogic_FMEAEntry", type=failureLogic_FMEA, multiplicity=Multiplicity(1, 1)),
        Property(name="failureLogic_FMEA", type=failureLogic_FMEAEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_failureLogic_FailureLogicPackage_ODEProductPackage = Generalization(general=ODEProductPackage, specific=failureLogic_FailureLogicPackage)
gen_failureLogic_SecurityViolation_Failure = Generalization(general=Failure, specific=failureLogic_SecurityViolation)
gen_failureLogic_FailureModel_BaseElement = Generalization(general=BaseElement, specific=failureLogic_FailureModel)
gen_failureLogic_MinimalCutSets_BaseElement = Generalization(general=BaseElement, specific=failureLogic_MinimalCutSets)
gen_failureLogic_MinimalCutset_BaseElement = Generalization(general=BaseElement, specific=failureLogic_MinimalCutset)
gen_failureLogic_ProbDist_BaseElement = Generalization(general=BaseElement, specific=failureLogic_ProbDist)
gen_failureLogic_Failure_BaseElement = Generalization(general=BaseElement, specific=failureLogic_Failure)
gen_failureLogic_FaultTree_FailureModel = Generalization(general=FailureModel, specific=failureLogic_FaultTree)
gen_failureLogic_Cause_BaseElement = Generalization(general=BaseElement, specific=failureLogic_Cause)
gen_failureLogic_Gate_Cause = Generalization(general=Cause, specific=failureLogic_Gate)
gen_failureLogic_MarkovChain_FailureModel = Generalization(general=FailureModel, specific=failureLogic_MarkovChain)
gen_failureLogic_State_BaseElement = Generalization(general=BaseElement, specific=failureLogic_State)
gen_failureLogic_Transition_BaseElement = Generalization(general=BaseElement, specific=failureLogic_Transition)
gen_failureLogic_ProbDistParam_BaseElement = Generalization(general=BaseElement, specific=failureLogic_ProbDistParam)
gen_failureLogic_FMEDAEntry_FMEAEntry = Generalization(general=FMEAEntry, specific=failureLogic_FMEDAEntry)
gen_failureLogic_FMEA_FailureModel = Generalization(general=FailureModel, specific=failureLogic_FMEA)
gen_failureLogic_FMEAEntry_BaseElement = Generalization(general=BaseElement, specific=failureLogic_FMEAEntry)

# Domain Model
domain_model = DomainModel(
    name="failureLogic",
    types={failureLogic_FailureLogicPackage, ODEProductPackage, failureLogic_MinimalCutSets, failureLogic_MinimalCutset, failureLogic_ProbDistParam, failureLogic_FailureModel, failureLogic_Failure, BaseElement, failureLogic_ProbDist, failureLogic_SecurityViolation, Failure, failureLogic_FaultTree, FailureModel, failureLogic_Cause, failureLogic_Gate, Cause, failureLogic_MarkovChain, failureLogic_Transition, failureLogic_State, failureLogic_FMEDAEntry, FMEAEntry, failureLogic_FMEA, failureLogic_FMEAEntry, FailureOriginType, GateType, CauseType, FMEAType},
    associations={minimalCutsets5, failures7, subModels11, cutsets13, failures15, failures18, parameters21, failureModels0, failureProbDistribution1, ccfFailures3, causes23, failure24, causes27, transitions29, states30, failState32, effect45, mode48, diagnosisProbDistribution51, transitionProbDistribution35, fromStates38, toStates41, entries44},
    generalizations={gen_failureLogic_FailureLogicPackage_ODEProductPackage, gen_failureLogic_SecurityViolation_Failure, gen_failureLogic_FailureModel_BaseElement, gen_failureLogic_MinimalCutSets_BaseElement, gen_failureLogic_MinimalCutset_BaseElement, gen_failureLogic_ProbDist_BaseElement, gen_failureLogic_Failure_BaseElement, gen_failureLogic_FaultTree_FailureModel, gen_failureLogic_Cause_BaseElement, gen_failureLogic_Gate_Cause, gen_failureLogic_MarkovChain_FailureModel, gen_failureLogic_State_BaseElement, gen_failureLogic_Transition_BaseElement, gen_failureLogic_ProbDistParam_BaseElement, gen_failureLogic_FMEDAEntry_FMEAEntry, gen_failureLogic_FMEA_FailureModel, gen_failureLogic_FMEAEntry_BaseElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)