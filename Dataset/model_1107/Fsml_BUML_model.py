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
fsml_FSM = Class(name="fsml_FSM")
fsml_FSMState = Class(name="fsml_FSMState")
fsml_FSMTransition = Class(name="fsml_FSMTransition")

# fsml_FSM class attributes and methods
fsml_FSM_m_hasExactOneInitialState: Method = Method(name="hasExactOneInitialState", parameters={Parameter(name='fsml_diagnostics', type=StringType), Parameter(name='fsml_context', type=StringType)}, type=BooleanType)
fsml_FSM.methods={fsml_FSM_m_hasExactOneInitialState}

# fsml_FSMState class attributes and methods
fsml_FSMState_initial: Property = Property(name="initial", type=BooleanType)
fsml_FSMState_name: Property = Property(name="name", type=StringType)
fsml_FSMState_m_hasDistinctEvents: Method = Method(name="hasDistinctEvents", parameters={Parameter(name='fsml_context', type=StringType), Parameter(name='fsml_diagnostics', type=StringType)}, type=BooleanType)
fsml_FSMState_m_isReachable: Method = Method(name="isReachable", parameters={Parameter(name='fsml_context', type=StringType), Parameter(name='fsml_diagnostics', type=StringType)}, type=BooleanType)
fsml_FSMState.attributes={fsml_FSMState_name, fsml_FSMState_initial}
fsml_FSMState.methods={fsml_FSMState_m_isReachable, fsml_FSMState_m_hasDistinctEvents}

# fsml_FSMTransition class attributes and methods
fsml_FSMTransition_input: Property = Property(name="input", type=StringType)
fsml_FSMTransition_action: Property = Property(name="action", type=StringType)
fsml_FSMTransition.attributes={fsml_FSMTransition_input, fsml_FSMTransition_action}

# Relationships
states0: BinaryAssociation = BinaryAssociation(
    name="states0",
    ends={
        Property(name="fsml_FSMState", type=fsml_FSM, multiplicity=Multiplicity(1, 1)),
        Property(name="fsml_FSM", type=fsml_FSMState, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
target3: BinaryAssociation = BinaryAssociation(
    name="target3",
    ends={
        Property(name="fsml_FSMState5", type=fsml_FSMTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="fsml_FSMTransition4", type=fsml_FSMState, multiplicity=Multiplicity(0, 1))
    }
)
transitions1: BinaryAssociation = BinaryAssociation(
    name="transitions1",
    ends={
        Property(name="fsml_FSMTransition", type=fsml_FSMState, multiplicity=Multiplicity(1, 1)),
        Property(name="fsml_FSMState2", type=fsml_FSMTransition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="fsml",
    types={fsml_FSM, fsml_FSMState, fsml_FSMTransition},
    associations={states0, target3, transitions1},
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