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
petrinetv3_TracedPlace = Class(name="petrinetv3_TracedPlace")
petrinetv3Trace_Trace = Class(name="petrinetv3Trace_Trace")
Petrinetv3_Net_Initialize = Class(name="Petrinetv3_Net_Initialize")
Petrinetv3_Net_Run = Class(name="Petrinetv3_Net_Run")
Petrinetv3_Net_TickEnabledTransitions = Class(name="Petrinetv3_Net_TickEnabledTransitions")
Petrinetv3_Transition_Fire = Class(name="Petrinetv3_Transition_Fire")
Petrinetv3_Net_Run_AbstractSubStep = Class(name="Petrinetv3_Net_Run_AbstractSubStep")
petrinetv3Trace_Steps_Petrinetv3_Net_Run_AbstractSubStep = Class(name="petrinetv3Trace_Steps_Petrinetv3_Net_Run_AbstractSubStep", is_abstract=True)
petrinetv3Trace_Steps_Petrinetv3_Net_Run_ImplicitStep = Class(name="petrinetv3Trace_Steps_Petrinetv3_Net_Run_ImplicitStep")
petrinetv3Trace_Steps_Petrinetv3_Net_TickEnabledTransitions = Class(name="petrinetv3Trace_Steps_Petrinetv3_Net_TickEnabledTransitions")
petrinetv3Trace_Steps_Petrinetv3_Transition_Fire = Class(name="petrinetv3Trace_Steps_Petrinetv3_Transition_Fire")
petrinetv3_TracedToken = Class(name="petrinetv3_TracedToken")
petrinetv3_TracedTransition = Class(name="petrinetv3_TracedTransition")
Step = Class(name="Step")
State = Class(name="State")
petrinetv3Trace_Steps_BigStep = Class(name="petrinetv3Trace_Steps_BigStep", is_abstract=True)
petrinetv3Trace_Steps_Petrinetv3_Net_Initialize = Class(name="petrinetv3Trace_Steps_Petrinetv3_Net_Initialize")
Steps_Petrinetv3_Net_Run_AbstractSubStep = Class(name="Steps_Petrinetv3_Net_Run_AbstractSubStep")
Steps_SmallStep = Class(name="Steps_SmallStep")
petrinetv3Trace_Steps_Petrinetv3_Net_Run = Class(name="petrinetv3Trace_Steps_Petrinetv3_Net_Run")
BigStep = Class(name="BigStep")
petrinetv3Trace_States_State = Class(name="petrinetv3Trace_States_State")
Place_tokens_Value = Class(name="Place_tokens_Value")
Transition_clock_Value = Class(name="Transition_clock_Value")
petrinetv3Trace_Steps_RootImplicitStep = Class(name="petrinetv3Trace_Steps_RootImplicitStep")
SmallStep = Class(name="SmallStep")
petrinetv3Trace_Steps_SmallStep = Class(name="petrinetv3Trace_Steps_SmallStep", is_abstract=True)
petrinetv3Trace_Steps_Step = Class(name="petrinetv3Trace_Steps_Step", is_abstract=True)
MSEOccurrence = Class(name="MSEOccurrence")
petrinetv3Trace_States_Place_tokens_Value = Class(name="petrinetv3Trace_States_Place_tokens_Value")
petrinetv3_petrinetv3Trace_Transition = Class(name="petrinetv3_petrinetv3Trace_Transition")
petrinetv3_petrinetv3Trace_Net = Class(name="petrinetv3_petrinetv3Trace_Net")
petrinetv3Trace_States_Transition_clock_Value = Class(name="petrinetv3Trace_States_Transition_clock_Value")
petrinetv3Trace_petrinetv3_TracedPlace = Class(name="petrinetv3Trace_petrinetv3_TracedPlace")
petrinetv3_petrinetv3Trace_Place = Class(name="petrinetv3_petrinetv3Trace_Place")
petrinetv3_petrinetv3Trace_Token = Class(name="petrinetv3_petrinetv3Trace_Token")
petrinetv3Trace_petrinetv3_TracedToken = Class(name="petrinetv3Trace_petrinetv3_TracedToken")
petrinetv3Trace_petrinetv3_TracedTransition = Class(name="petrinetv3Trace_petrinetv3_TracedTransition")

# petrinetv3_TracedPlace class attributes and methods

# petrinetv3Trace_Trace class attributes and methods

# Petrinetv3_Net_Initialize class attributes and methods

# Petrinetv3_Net_Run class attributes and methods

# Petrinetv3_Net_TickEnabledTransitions class attributes and methods

# Petrinetv3_Transition_Fire class attributes and methods

# Petrinetv3_Net_Run_AbstractSubStep class attributes and methods

# petrinetv3Trace_Steps_Petrinetv3_Net_Run_AbstractSubStep class attributes and methods

# petrinetv3Trace_Steps_Petrinetv3_Net_Run_ImplicitStep class attributes and methods

# petrinetv3Trace_Steps_Petrinetv3_Net_TickEnabledTransitions class attributes and methods
petrinetv3Trace_Steps_Petrinetv3_Net_TickEnabledTransitions_m_getCaller: Method = Method(name="getCaller", parameters={}, type=StringType)
petrinetv3Trace_Steps_Petrinetv3_Net_TickEnabledTransitions.methods={petrinetv3Trace_Steps_Petrinetv3_Net_TickEnabledTransitions_m_getCaller}

# petrinetv3Trace_Steps_Petrinetv3_Transition_Fire class attributes and methods
petrinetv3Trace_Steps_Petrinetv3_Transition_Fire_m_getCaller: Method = Method(name="getCaller", parameters={}, type=StringType)
petrinetv3Trace_Steps_Petrinetv3_Transition_Fire.methods={petrinetv3Trace_Steps_Petrinetv3_Transition_Fire_m_getCaller}

# petrinetv3_TracedToken class attributes and methods

# petrinetv3_TracedTransition class attributes and methods

# Step class attributes and methods

# State class attributes and methods

# petrinetv3Trace_Steps_BigStep class attributes and methods

# petrinetv3Trace_Steps_Petrinetv3_Net_Initialize class attributes and methods
petrinetv3Trace_Steps_Petrinetv3_Net_Initialize_m_getCaller: Method = Method(name="getCaller", parameters={}, type=StringType)
petrinetv3Trace_Steps_Petrinetv3_Net_Initialize.methods={petrinetv3Trace_Steps_Petrinetv3_Net_Initialize_m_getCaller}

# Steps_Petrinetv3_Net_Run_AbstractSubStep class attributes and methods

# Steps_SmallStep class attributes and methods

# petrinetv3Trace_Steps_Petrinetv3_Net_Run class attributes and methods
petrinetv3Trace_Steps_Petrinetv3_Net_Run_m_getCaller: Method = Method(name="getCaller", parameters={}, type=StringType)
petrinetv3Trace_Steps_Petrinetv3_Net_Run.methods={petrinetv3Trace_Steps_Petrinetv3_Net_Run_m_getCaller}

# BigStep class attributes and methods

# petrinetv3Trace_States_State class attributes and methods

# Place_tokens_Value class attributes and methods

# Transition_clock_Value class attributes and methods

# petrinetv3Trace_Steps_RootImplicitStep class attributes and methods

# SmallStep class attributes and methods

# petrinetv3Trace_Steps_SmallStep class attributes and methods

# petrinetv3Trace_Steps_Step class attributes and methods

# MSEOccurrence class attributes and methods

# petrinetv3Trace_States_Place_tokens_Value class attributes and methods

# petrinetv3_petrinetv3Trace_Transition class attributes and methods

# petrinetv3_petrinetv3Trace_Net class attributes and methods

# petrinetv3Trace_States_Transition_clock_Value class attributes and methods
petrinetv3Trace_States_Transition_clock_Value_clock: Property = Property(name="clock", type=IntegerType)
petrinetv3Trace_States_Transition_clock_Value.attributes={petrinetv3Trace_States_Transition_clock_Value_clock}

# petrinetv3Trace_petrinetv3_TracedPlace class attributes and methods

# petrinetv3_petrinetv3Trace_Place class attributes and methods

# petrinetv3_petrinetv3Trace_Token class attributes and methods

# petrinetv3Trace_petrinetv3_TracedToken class attributes and methods

# petrinetv3Trace_petrinetv3_TracedTransition class attributes and methods

# Relationships
Petrinetv3_Transition_Fire_Sequence5: BinaryAssociation = BinaryAssociation(
    name="Petrinetv3_Transition_Fire_Sequence5",
    ends={
        Property(name="petrinetv3Trace_Trace6", type=Petrinetv3_Transition_Fire, multiplicity=Multiplicity(0, 9999)),
        Property(name="Petrinetv3_Transition_Fire", type=petrinetv3Trace_Trace, multiplicity=Multiplicity(1, 1))
    }
)
petrinetv3_tracedPlaces7: BinaryAssociation = BinaryAssociation(
    name="petrinetv3_tracedPlaces7",
    ends={
        Property(name="petrinetv3_TracedPlace", type=petrinetv3Trace_Trace, multiplicity=Multiplicity(1, 1)),
        Property(name="petrinetv3Trace_Trace8", type=petrinetv3_TracedPlace, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Petrinetv3_Net_Initialize_Sequence0: BinaryAssociation = BinaryAssociation(
    name="Petrinetv3_Net_Initialize_Sequence0",
    ends={
        Property(name="Petrinetv3_Net_Initialize", type=petrinetv3Trace_Trace, multiplicity=Multiplicity(1, 1)),
        Property(name="petrinetv3Trace_Trace", type=Petrinetv3_Net_Initialize, multiplicity=Multiplicity(0, 9999))
    }
)
Petrinetv3_Net_Run_Sequence1: BinaryAssociation = BinaryAssociation(
    name="Petrinetv3_Net_Run_Sequence1",
    ends={
        Property(name="Petrinetv3_Net_Run", type=petrinetv3Trace_Trace, multiplicity=Multiplicity(1, 1)),
        Property(name="petrinetv3Trace_Trace2", type=Petrinetv3_Net_Run, multiplicity=Multiplicity(0, 9999))
    }
)
Petrinetv3_Net_TickEnabledTransitions_Sequence3: BinaryAssociation = BinaryAssociation(
    name="Petrinetv3_Net_TickEnabledTransitions_Sequence3",
    ends={
        Property(name="Petrinetv3_Net_TickEnabledTransitions", type=petrinetv3Trace_Trace, multiplicity=Multiplicity(1, 1)),
        Property(name="petrinetv3Trace_Trace4", type=Petrinetv3_Net_TickEnabledTransitions, multiplicity=Multiplicity(0, 9999))
    }
)
subSteps17: BinaryAssociation = BinaryAssociation(
    name="subSteps17",
    ends={
        Property(name="Petrinetv3_Net_Run_AbstractSubStep", type=petrinetv3Trace_Steps_Petrinetv3_Net_Run, multiplicity=Multiplicity(1, 1)),
        Property(name="petrinetv3Trace_Steps_Petrinetv3_Net_Run", type=Petrinetv3_Net_Run_AbstractSubStep, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
petrinetv3_tracedTokens9: BinaryAssociation = BinaryAssociation(
    name="petrinetv3_tracedTokens9",
    ends={
        Property(name="petrinetv3_TracedToken", type=petrinetv3Trace_Trace, multiplicity=Multiplicity(1, 1)),
        Property(name="petrinetv3Trace_Trace10", type=petrinetv3_TracedToken, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
petrinetv3_tracedTransitions11: BinaryAssociation = BinaryAssociation(
    name="petrinetv3_tracedTransitions11",
    ends={
        Property(name="petrinetv3_TracedTransition", type=petrinetv3Trace_Trace, multiplicity=Multiplicity(1, 1)),
        Property(name="petrinetv3Trace_Trace12", type=petrinetv3_TracedTransition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
rootSteps13: BinaryAssociation = BinaryAssociation(
    name="rootSteps13",
    ends={
        Property(name="Step", type=petrinetv3Trace_Trace, multiplicity=Multiplicity(1, 1)),
        Property(name="petrinetv3Trace_Trace14", type=Step, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
statesTrace15: BinaryAssociation = BinaryAssociation(
    name="statesTrace15",
    ends={
        Property(name="State", type=petrinetv3Trace_Trace, multiplicity=Multiplicity(1, 1)),
        Property(name="petrinetv3Trace_Trace16", type=State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
endedSteps27: BinaryAssociation = BinaryAssociation(
    name="endedSteps27",
    ends={
        Property(name="Step28", type=petrinetv3Trace_States_State, multiplicity=Multiplicity(1, 1)),
        Property(name="endingState", type=Step, multiplicity=Multiplicity(0, 9999))
    }
)
place_tokens_Values29: BinaryAssociation = BinaryAssociation(
    name="place_tokens_Values29",
    ends={
        Property(name="Place_tokens_Value", type=petrinetv3Trace_States_State, multiplicity=Multiplicity(1, 1)),
        Property(name="states", type=Place_tokens_Value, multiplicity=Multiplicity(0, 9999))
    }
)
startedSteps30: BinaryAssociation = BinaryAssociation(
    name="startedSteps30",
    ends={
        Property(name="Step31", type=petrinetv3Trace_States_State, multiplicity=Multiplicity(1, 1)),
        Property(name="startingState", type=Step, multiplicity=Multiplicity(0, 9999))
    }
)
transition_clock_Values32: BinaryAssociation = BinaryAssociation(
    name="transition_clock_Values32",
    ends={
        Property(name="Transition_clock_Value", type=petrinetv3Trace_States_State, multiplicity=Multiplicity(1, 1)),
        Property(name="states33", type=Transition_clock_Value, multiplicity=Multiplicity(0, 9999))
    }
)
endingState18: BinaryAssociation = BinaryAssociation(
    name="endingState18",
    ends={
        Property(name="State19", type=petrinetv3Trace_Steps_Step, multiplicity=Multiplicity(1, 1)),
        Property(name="endedSteps", type=State, multiplicity=Multiplicity(0, 1))
    }
)
startingState20: BinaryAssociation = BinaryAssociation(
    name="startingState20",
    ends={
        Property(name="State21", type=petrinetv3Trace_Steps_Step, multiplicity=Multiplicity(1, 1)),
        Property(name="startedSteps", type=State, multiplicity=Multiplicity(1, 1))
    }
)
parent22: BinaryAssociation = BinaryAssociation(
    name="parent22",
    ends={
        Property(name="TracedPlace", type=petrinetv3Trace_States_Place_tokens_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="tokensSequence", type=petrinetv3_TracedPlace, multiplicity=Multiplicity(1, 1))
    }
)
states23: BinaryAssociation = BinaryAssociation(
    name="states23",
    ends={
        Property(name="State24", type=petrinetv3Trace_States_Place_tokens_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="place_tokens_Values", type=State, multiplicity=Multiplicity(1, 9999))
    }
)
tokens25: BinaryAssociation = BinaryAssociation(
    name="tokens25",
    ends={
        Property(name="petrinetv3_TracedToken26", type=petrinetv3Trace_States_Place_tokens_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="petrinetv3Trace_States_Place_tokens_Value", type=petrinetv3_TracedToken, multiplicity=Multiplicity(0, 9999))
    }
)
input45: BinaryAssociation = BinaryAssociation(
    name="input45",
    ends={
        Property(name="petrinetv3_TracedPlace46", type=petrinetv3Trace_petrinetv3_TracedTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="petrinetv3Trace_petrinetv3_TracedTransition", type=petrinetv3_TracedPlace, multiplicity=Multiplicity(1, 9999))
    }
)
originalObject47: BinaryAssociation = BinaryAssociation(
    name="originalObject47",
    ends={
        Property(name="petrinetv3_petrinetv3Trace_Transition", type=petrinetv3Trace_petrinetv3_TracedTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="petrinetv3Trace_petrinetv3_TracedTransition48", type=petrinetv3_petrinetv3Trace_Transition, multiplicity=Multiplicity(0, 1))
    }
)
output49: BinaryAssociation = BinaryAssociation(
    name="output49",
    ends={
        Property(name="petrinetv3_TracedPlace51", type=petrinetv3Trace_petrinetv3_TracedTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="petrinetv3Trace_petrinetv3_TracedTransition50", type=petrinetv3_TracedPlace, multiplicity=Multiplicity(1, 9999))
    }
)
parentNet52: BinaryAssociation = BinaryAssociation(
    name="parentNet52",
    ends={
        Property(name="petrinetv3_petrinetv3Trace_Net", type=petrinetv3Trace_petrinetv3_TracedTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="petrinetv3Trace_petrinetv3_TracedTransition53", type=petrinetv3_petrinetv3Trace_Net, multiplicity=Multiplicity(1, 1))
    }
)
parent34: BinaryAssociation = BinaryAssociation(
    name="parent34",
    ends={
        Property(name="TracedTransition", type=petrinetv3Trace_States_Transition_clock_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="clockSequence", type=petrinetv3_TracedTransition, multiplicity=Multiplicity(1, 1))
    }
)
states35: BinaryAssociation = BinaryAssociation(
    name="states35",
    ends={
        Property(name="State36", type=petrinetv3Trace_States_Transition_clock_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="transition_clock_Values", type=State, multiplicity=Multiplicity(1, 9999))
    }
)
originalObject37: BinaryAssociation = BinaryAssociation(
    name="originalObject37",
    ends={
        Property(name="petrinetv3_petrinetv3Trace_Place", type=petrinetv3Trace_petrinetv3_TracedPlace, multiplicity=Multiplicity(1, 1)),
        Property(name="petrinetv3Trace_petrinetv3_TracedPlace", type=petrinetv3_petrinetv3Trace_Place, multiplicity=Multiplicity(0, 1))
    }
)
tokens38: BinaryAssociation = BinaryAssociation(
    name="tokens38",
    ends={
        Property(name="petrinetv3_petrinetv3Trace_Token", type=petrinetv3Trace_petrinetv3_TracedPlace, multiplicity=Multiplicity(1, 1)),
        Property(name="petrinetv3Trace_petrinetv3_TracedPlace39", type=petrinetv3_petrinetv3Trace_Token, multiplicity=Multiplicity(0, 9999))
    }
)
tokensSequence40: BinaryAssociation = BinaryAssociation(
    name="tokensSequence40",
    ends={
        Property(name="Place_tokens_Value41", type=petrinetv3Trace_petrinetv3_TracedPlace, multiplicity=Multiplicity(1, 1)),
        Property(name="parent", type=Place_tokens_Value, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
clockSequence42: BinaryAssociation = BinaryAssociation(
    name="clockSequence42",
    ends={
        Property(name="Transition_clock_Value44", type=petrinetv3Trace_petrinetv3_TracedTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="parent43", type=Transition_clock_Value, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_petrinetv3Trace_Steps_Petrinetv3_Net_Run_ImplicitStep_Steps_Petrinetv3_Net_Run_AbstractSubStep = Generalization(general=Steps_Petrinetv3_Net_Run_AbstractSubStep, specific=petrinetv3Trace_Steps_Petrinetv3_Net_Run_ImplicitStep)
gen_petrinetv3Trace_Steps_Petrinetv3_Net_Run_ImplicitStep_Steps_SmallStep = Generalization(general=Steps_SmallStep, specific=petrinetv3Trace_Steps_Petrinetv3_Net_Run_ImplicitStep)
gen_petrinetv3Trace_Steps_Petrinetv3_Net_TickEnabledTransitions_Steps_Petrinetv3_Net_Run_AbstractSubStep = Generalization(general=Steps_Petrinetv3_Net_Run_AbstractSubStep, specific=petrinetv3Trace_Steps_Petrinetv3_Net_TickEnabledTransitions)
gen_petrinetv3Trace_Steps_Petrinetv3_Net_TickEnabledTransitions_Steps_SmallStep = Generalization(general=Steps_SmallStep, specific=petrinetv3Trace_Steps_Petrinetv3_Net_TickEnabledTransitions)
gen_petrinetv3Trace_Steps_Petrinetv3_Transition_Fire_Steps_Petrinetv3_Net_Run_AbstractSubStep = Generalization(general=Steps_Petrinetv3_Net_Run_AbstractSubStep, specific=petrinetv3Trace_Steps_Petrinetv3_Transition_Fire)
gen_petrinetv3Trace_Steps_Petrinetv3_Transition_Fire_Steps_SmallStep = Generalization(general=Steps_SmallStep, specific=petrinetv3Trace_Steps_Petrinetv3_Transition_Fire)
gen_petrinetv3Trace_Steps_BigStep_Step = Generalization(general=Step, specific=petrinetv3Trace_Steps_BigStep)
gen_petrinetv3Trace_Steps_Petrinetv3_Net_Initialize_Steps_Petrinetv3_Net_Run_AbstractSubStep = Generalization(general=Steps_Petrinetv3_Net_Run_AbstractSubStep, specific=petrinetv3Trace_Steps_Petrinetv3_Net_Initialize)
gen_petrinetv3Trace_Steps_Petrinetv3_Net_Initialize_Steps_SmallStep = Generalization(general=Steps_SmallStep, specific=petrinetv3Trace_Steps_Petrinetv3_Net_Initialize)
gen_petrinetv3Trace_Steps_Petrinetv3_Net_Run_BigStep = Generalization(general=BigStep, specific=petrinetv3Trace_Steps_Petrinetv3_Net_Run)
gen_petrinetv3Trace_Steps_RootImplicitStep_SmallStep = Generalization(general=SmallStep, specific=petrinetv3Trace_Steps_RootImplicitStep)
gen_petrinetv3Trace_Steps_SmallStep_Step = Generalization(general=Step, specific=petrinetv3Trace_Steps_SmallStep)
gen_petrinetv3Trace_Steps_Step_MSEOccurrence = Generalization(general=MSEOccurrence, specific=petrinetv3Trace_Steps_Step)

# Domain Model
domain_model = DomainModel(
    name="petrinetv3Trace",
    types={petrinetv3_TracedPlace, petrinetv3Trace_Trace, Petrinetv3_Net_Initialize, Petrinetv3_Net_Run, Petrinetv3_Net_TickEnabledTransitions, Petrinetv3_Transition_Fire, Petrinetv3_Net_Run_AbstractSubStep, petrinetv3Trace_Steps_Petrinetv3_Net_Run_AbstractSubStep, petrinetv3Trace_Steps_Petrinetv3_Net_Run_ImplicitStep, petrinetv3Trace_Steps_Petrinetv3_Net_TickEnabledTransitions, petrinetv3Trace_Steps_Petrinetv3_Transition_Fire, petrinetv3_TracedToken, petrinetv3_TracedTransition, Step, State, petrinetv3Trace_Steps_BigStep, petrinetv3Trace_Steps_Petrinetv3_Net_Initialize, Steps_Petrinetv3_Net_Run_AbstractSubStep, Steps_SmallStep, petrinetv3Trace_Steps_Petrinetv3_Net_Run, BigStep, petrinetv3Trace_States_State, Place_tokens_Value, Transition_clock_Value, petrinetv3Trace_Steps_RootImplicitStep, SmallStep, petrinetv3Trace_Steps_SmallStep, petrinetv3Trace_Steps_Step, MSEOccurrence, petrinetv3Trace_States_Place_tokens_Value, petrinetv3_petrinetv3Trace_Transition, petrinetv3_petrinetv3Trace_Net, petrinetv3Trace_States_Transition_clock_Value, petrinetv3Trace_petrinetv3_TracedPlace, petrinetv3_petrinetv3Trace_Place, petrinetv3_petrinetv3Trace_Token, petrinetv3Trace_petrinetv3_TracedToken, petrinetv3Trace_petrinetv3_TracedTransition},
    associations={Petrinetv3_Transition_Fire_Sequence5, petrinetv3_tracedPlaces7, Petrinetv3_Net_Initialize_Sequence0, Petrinetv3_Net_Run_Sequence1, Petrinetv3_Net_TickEnabledTransitions_Sequence3, subSteps17, petrinetv3_tracedTokens9, petrinetv3_tracedTransitions11, rootSteps13, statesTrace15, endedSteps27, place_tokens_Values29, startedSteps30, transition_clock_Values32, endingState18, startingState20, parent22, states23, tokens25, input45, originalObject47, output49, parentNet52, parent34, states35, originalObject37, tokens38, tokensSequence40, clockSequence42},
    generalizations={gen_petrinetv3Trace_Steps_Petrinetv3_Net_Run_ImplicitStep_Steps_Petrinetv3_Net_Run_AbstractSubStep, gen_petrinetv3Trace_Steps_Petrinetv3_Net_Run_ImplicitStep_Steps_SmallStep, gen_petrinetv3Trace_Steps_Petrinetv3_Net_TickEnabledTransitions_Steps_Petrinetv3_Net_Run_AbstractSubStep, gen_petrinetv3Trace_Steps_Petrinetv3_Net_TickEnabledTransitions_Steps_SmallStep, gen_petrinetv3Trace_Steps_Petrinetv3_Transition_Fire_Steps_Petrinetv3_Net_Run_AbstractSubStep, gen_petrinetv3Trace_Steps_Petrinetv3_Transition_Fire_Steps_SmallStep, gen_petrinetv3Trace_Steps_BigStep_Step, gen_petrinetv3Trace_Steps_Petrinetv3_Net_Initialize_Steps_Petrinetv3_Net_Run_AbstractSubStep, gen_petrinetv3Trace_Steps_Petrinetv3_Net_Initialize_Steps_SmallStep, gen_petrinetv3Trace_Steps_Petrinetv3_Net_Run_BigStep, gen_petrinetv3Trace_Steps_RootImplicitStep_SmallStep, gen_petrinetv3Trace_Steps_SmallStep_Step, gen_petrinetv3Trace_Steps_Step_MSEOccurrence},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)