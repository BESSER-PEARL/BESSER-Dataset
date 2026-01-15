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
mdc_TransactionalState = Class(name="mdc::TransactionalState", is_abstract=True)
State = Class(name="State")
mdc_Chatbot = Class(name="mdc::Chatbot")
mdc_State = Class(name="mdc::State", is_abstract=True)
mdc_StationaryState = Class(name="mdc::StationaryState", is_abstract=True)
mdc_TransactionalStateImpl = Class(name="mdc::TransactionalStateImpl")
TransactionalState = Class(name="TransactionalState")
mdc_StationaryStateImpl = Class(name="mdc::StationaryStateImpl")
StationaryState = Class(name="StationaryState")

# mdc_TransactionalState class attributes and methods

# State class attributes and methods

# mdc_Chatbot class attributes and methods
mdc_Chatbot_name: Property = Property(name="name", type=StringType)
mdc_Chatbot_token: Property = Property(name="token", type=StringType)
mdc_Chatbot.attributes={mdc_Chatbot_token, mdc_Chatbot_name}

# mdc_State class attributes and methods
mdc_State_name: Property = Property(name="name", type=StringType)
mdc_State_messages: Property = Property(name="messages", type=StringType)
mdc_State_input: Property = Property(name="input", type=StringType)
mdc_State_m_entryPoint: Method = Method(name="entryPoint", parameters={}, type=StringType)
mdc_State.attributes={mdc_State_input, mdc_State_name, mdc_State_messages}
mdc_State.methods={mdc_State_m_entryPoint}

# mdc_StationaryState class attributes and methods
mdc_StationaryState_m_handler: Method = Method(name="handler", parameters={}, type=State)
mdc_StationaryState_m_sincTransitions: Method = Method(name="sincTransitions", parameters={})
mdc_StationaryState.methods={mdc_StationaryState_m_sincTransitions, mdc_StationaryState_m_handler}

# mdc_TransactionalStateImpl class attributes and methods

# TransactionalState class attributes and methods

# mdc_StationaryStateImpl class attributes and methods

# StationaryState class attributes and methods

# Relationships
initState1: BinaryAssociation = BinaryAssociation(
    name="initState1",
    ends={
        Property(name="mdc_StationaryState", type=mdc_Chatbot, multiplicity=Multiplicity(1, 1)),
        Property(name="mdc_Chatbot2", type=mdc_StationaryState, multiplicity=Multiplicity(1, 1))
    }
)
states0: BinaryAssociation = BinaryAssociation(
    name="states0",
    ends={
        Property(name="mdc_State", type=mdc_Chatbot, multiplicity=Multiplicity(1, 1)),
        Property(name="mdc_Chatbot", type=mdc_State, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
transitions3: BinaryAssociation = BinaryAssociation(
    name="transitions3",
    ends={
        Property(name="mdc_State5", type=mdc_StationaryState, multiplicity=Multiplicity(1, 1)),
        Property(name="mdc_StationaryState4", type=mdc_State, multiplicity=Multiplicity(0, 9999))
    }
)
errorState6: BinaryAssociation = BinaryAssociation(
    name="errorState6",
    ends={
        Property(name="mdc_TransactionalState", type=mdc_StationaryState, multiplicity=Multiplicity(1, 1)),
        Property(name="mdc_StationaryState7", type=mdc_TransactionalState, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_mdc_TransactionalState_State = Generalization(general=State, specific=mdc_TransactionalState)
gen_mdc_StationaryState_State = Generalization(general=State, specific=mdc_StationaryState)
gen_mdc_TransactionalStateImpl_TransactionalState = Generalization(general=TransactionalState, specific=mdc_TransactionalStateImpl)
gen_mdc_StationaryStateImpl_StationaryState = Generalization(general=StationaryState, specific=mdc_StationaryStateImpl)

# Domain Model
domain_model = DomainModel(
    name="mdc",
    types={mdc_TransactionalState, State, mdc_Chatbot, mdc_State, mdc_StationaryState, mdc_TransactionalStateImpl, TransactionalState, mdc_StationaryStateImpl, StationaryState},
    associations={initState1, states0, transitions3, errorState6},
    generalizations={gen_mdc_TransactionalState_State, gen_mdc_StationaryState_State, gen_mdc_TransactionalStateImpl_TransactionalState, gen_mdc_StationaryStateImpl_StationaryState},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)