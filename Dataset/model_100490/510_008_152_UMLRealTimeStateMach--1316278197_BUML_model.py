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
UMLRealTimeStateMach_RTStateMachine = Class(name="UMLRealTimeStateMach_RTStateMachine")
UMLRealTimeStateMach_StateMachine = Class(name="UMLRealTimeStateMach_StateMachine")
UMLRealTimeStateMach_RTRegion = Class(name="UMLRealTimeStateMach_RTRegion")
UMLRealTimeStateMach_Region = Class(name="UMLRealTimeStateMach_Region")
UMLRealTimeStateMach_RTState = Class(name="UMLRealTimeStateMach_RTState")
UMLRealTimeStateMach_State = Class(name="UMLRealTimeStateMach_State")
UMLRealTimeStateMach_RTPseudostate = Class(name="UMLRealTimeStateMach_RTPseudostate")
UMLRealTimeStateMach_Operation = Class(name="UMLRealTimeStateMach_Operation")
UMLRealTimeStateMach_Pseudostate = Class(name="UMLRealTimeStateMach_Pseudostate")
UMLRealTimeStateMach_RTTrigger = Class(name="UMLRealTimeStateMach_RTTrigger")

# UMLRealTimeStateMach_RTStateMachine class attributes and methods
UMLRealTimeStateMach_RTStateMachine_isPassive: Property = Property(name="isPassive", type=StringType)
UMLRealTimeStateMach_RTStateMachine_m_AnRTstatemachinehasexactlyoneregion: Method = Method(name="AnRTstatemachinehasexactlyoneregion", parameters={Parameter(name='UMLRealTimeStateMach_diagnostics', type=StringType), Parameter(name='UMLRealTimeStateMach_context', type=StringType)}, type=BooleanType)
UMLRealTimeStateMach_RTStateMachine_m_RTstatemachinesdonothaveparametersorparametersets: Method = Method(name="RTstatemachinesdonothaveparametersorparametersets", parameters={Parameter(name='UMLRealTimeStateMach_diagnostics', type=StringType), Parameter(name='UMLRealTimeStateMach_context', type=StringType)}, type=BooleanType)
UMLRealTimeStateMach_RTStateMachine_m_RTstatemachinesmusthaveacontextanditmustbeaClass: Method = Method(name="RTstatemachinesmusthaveacontextanditmustbeaClass", parameters={Parameter(name='UMLRealTimeStateMach_context', type=StringType), Parameter(name='UMLRealTimeStateMach_diagnostics', type=StringType)}, type=BooleanType)
UMLRealTimeStateMach_RTStateMachine_m_AnRTstatemachineisneverreentrant: Method = Method(name="AnRTstatemachineisneverreentrant", parameters={Parameter(name='UMLRealTimeStateMach_diagnostics', type=StringType), Parameter(name='UMLRealTimeStateMach_context', type=StringType)}, type=BooleanType)
UMLRealTimeStateMach_RTStateMachine_m_Passivestatemachineareonlyallowedonpassivedataclasses: Method = Method(name="Passivestatemachineareonlyallowedonpassivedataclasses", parameters={Parameter(name='UMLRealTimeStateMach_context', type=StringType), Parameter(name='UMLRealTimeStateMach_diagnostics', type=StringType)}, type=BooleanType)
UMLRealTimeStateMach_RTStateMachine.attributes={UMLRealTimeStateMach_RTStateMachine_isPassive}
UMLRealTimeStateMach_RTStateMachine.methods={UMLRealTimeStateMach_RTStateMachine_m_AnRTstatemachineisneverreentrant, UMLRealTimeStateMach_RTStateMachine_m_AnRTstatemachinehasexactlyoneregion, UMLRealTimeStateMach_RTStateMachine_m_RTstatemachinesmusthaveacontextanditmustbeaClass, UMLRealTimeStateMach_RTStateMachine_m_Passivestatemachineareonlyallowedonpassivedataclasses, UMLRealTimeStateMach_RTStateMachine_m_RTstatemachinesdonothaveparametersorparametersets}

# UMLRealTimeStateMach_StateMachine class attributes and methods

# UMLRealTimeStateMach_RTRegion class attributes and methods
UMLRealTimeStateMach_RTRegion_m_RegionsinRTstatemachinescannothaveafinalstate: Method = Method(name="RegionsinRTstatemachinescannothaveafinalstate", parameters={Parameter(name='UMLRealTimeStateMach_diagnostics', type=StringType), Parameter(name='UMLRealTimeStateMach_context', type=StringType)}, type=BooleanType)
UMLRealTimeStateMach_RTRegion.methods={UMLRealTimeStateMach_RTRegion_m_RegionsinRTstatemachinescannothaveafinalstate}

# UMLRealTimeStateMach_Region class attributes and methods

# UMLRealTimeStateMach_RTState class attributes and methods
UMLRealTimeStateMach_RTState_m_RTdoesnotsupportsubmachinestates: Method = Method(name="RTdoesnotsupportsubmachinestates", parameters={Parameter(name='UMLRealTimeStateMach_context', type=StringType), Parameter(name='UMLRealTimeStateMach_diagnostics', type=StringType)}, type=BooleanType)
UMLRealTimeStateMach_RTState_m_RTstatemachinesdonotsupportdoactivities: Method = Method(name="RTstatemachinesdonotsupportdoactivities", parameters={Parameter(name='UMLRealTimeStateMach_diagnostics', type=StringType), Parameter(name='UMLRealTimeStateMach_context', type=StringType)}, type=BooleanType)
UMLRealTimeStateMach_RTState_m_AcomposteRTstatehasexactlyoneregion: Method = Method(name="AcomposteRTstatehasexactlyoneregion", parameters={Parameter(name='UMLRealTimeStateMach_diagnostics', type=StringType), Parameter(name='UMLRealTimeStateMach_context', type=StringType)}, type=BooleanType)
UMLRealTimeStateMach_RTState_m_Constraint5: Method = Method(name="Constraint5", parameters={Parameter(name='UMLRealTimeStateMach_context', type=StringType), Parameter(name='UMLRealTimeStateMach_diagnostics', type=StringType)}, type=BooleanType)
UMLRealTimeStateMach_RTState_m_RTstatemachinescannothaveanydeferredtriggers: Method = Method(name="RTstatemachinescannothaveanydeferredtriggers", parameters={Parameter(name='UMLRealTimeStateMach_diagnostics', type=StringType), Parameter(name='UMLRealTimeStateMach_context', type=StringType)}, type=BooleanType)
UMLRealTimeStateMach_RTState.methods={UMLRealTimeStateMach_RTState_m_RTdoesnotsupportsubmachinestates, UMLRealTimeStateMach_RTState_m_RTstatemachinescannothaveanydeferredtriggers, UMLRealTimeStateMach_RTState_m_Constraint5, UMLRealTimeStateMach_RTState_m_AcomposteRTstatehasexactlyoneregion, UMLRealTimeStateMach_RTState_m_RTstatemachinesdonotsupportdoactivities}

# UMLRealTimeStateMach_State class attributes and methods

# UMLRealTimeStateMach_RTPseudostate class attributes and methods
UMLRealTimeStateMach_RTPseudostate_m_RTstatemachinesdonotsupportconcurrencyorshallowhistory: Method = Method(name="RTstatemachinesdonotsupportconcurrencyorshallowhistory", parameters={Parameter(name='UMLRealTimeStateMach_diagnostics', type=StringType), Parameter(name='UMLRealTimeStateMach_context', type=StringType)}, type=BooleanType)
UMLRealTimeStateMach_RTPseudostate.methods={UMLRealTimeStateMach_RTPseudostate_m_RTstatemachinesdonotsupportconcurrencyorshallowhistory}

# UMLRealTimeStateMach_Operation class attributes and methods

# UMLRealTimeStateMach_Pseudostate class attributes and methods

# UMLRealTimeStateMach_RTTrigger class attributes and methods

# Relationships
base_StateMachine0: BinaryAssociation = BinaryAssociation(
    name="base_StateMachine0",
    ends={
        Property(name="UMLRealTimeStateMach_StateMachine", type=UMLRealTimeStateMach_RTStateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="UMLRealTimeStateMach_RTStateMachine", type=UMLRealTimeStateMach_StateMachine, multiplicity=Multiplicity(1, 1))
    }
)
base_Region1: BinaryAssociation = BinaryAssociation(
    name="base_Region1",
    ends={
        Property(name="UMLRealTimeStateMach_Region", type=UMLRealTimeStateMach_RTRegion, multiplicity=Multiplicity(1, 1)),
        Property(name="UMLRealTimeStateMach_RTRegion", type=UMLRealTimeStateMach_Region, multiplicity=Multiplicity(1, 1))
    }
)
base_State2: BinaryAssociation = BinaryAssociation(
    name="base_State2",
    ends={
        Property(name="UMLRealTimeStateMach_State", type=UMLRealTimeStateMach_RTState, multiplicity=Multiplicity(1, 1)),
        Property(name="UMLRealTimeStateMach_RTState", type=UMLRealTimeStateMach_State, multiplicity=Multiplicity(1, 1))
    }
)
base_Operation4: BinaryAssociation = BinaryAssociation(
    name="base_Operation4",
    ends={
        Property(name="UMLRealTimeStateMach_Operation", type=UMLRealTimeStateMach_RTTrigger, multiplicity=Multiplicity(1, 1)),
        Property(name="UMLRealTimeStateMach_RTTrigger", type=UMLRealTimeStateMach_Operation, multiplicity=Multiplicity(1, 1))
    }
)
base_Pseudostate3: BinaryAssociation = BinaryAssociation(
    name="base_Pseudostate3",
    ends={
        Property(name="UMLRealTimeStateMach_Pseudostate", type=UMLRealTimeStateMach_RTPseudostate, multiplicity=Multiplicity(1, 1)),
        Property(name="UMLRealTimeStateMach_RTPseudostate", type=UMLRealTimeStateMach_Pseudostate, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="UMLRealTimeStateMach",
    types={UMLRealTimeStateMach_RTStateMachine, UMLRealTimeStateMach_StateMachine, UMLRealTimeStateMach_RTRegion, UMLRealTimeStateMach_Region, UMLRealTimeStateMach_RTState, UMLRealTimeStateMach_State, UMLRealTimeStateMach_RTPseudostate, UMLRealTimeStateMach_Operation, UMLRealTimeStateMach_Pseudostate, UMLRealTimeStateMach_RTTrigger},
    associations={base_StateMachine0, base_Region1, base_State2, base_Operation4, base_Pseudostate3},
    generalizations={},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)