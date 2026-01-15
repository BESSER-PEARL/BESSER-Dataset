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
FlowDesigner_Flow = Class(name="FlowDesigner::Flow")
FlowDesigner_InitialState = Class(name="FlowDesigner::InitialState")
Source = Class(name="Source")
FlowDesigner_FinalState = Class(name="FlowDesigner::FinalState")
Target = Class(name="Target")
FlowDesigner_ActionState = Class(name="FlowDesigner::ActionState")
NamedState = Class(name="NamedState")
FlowDesigner_ViewState = Class(name="FlowDesigner::ViewState")
FlowDesigner_Event = Class(name="FlowDesigner::Event")
FlowDesigner_Target = Class(name="FlowDesigner::Target", is_abstract=True)
FlowDesigner_Source = Class(name="FlowDesigner::Source", is_abstract=True)
FlowDesigner_NamedState = Class(name="FlowDesigner::NamedState", is_abstract=True)

# FlowDesigner_Flow class attributes and methods
FlowDesigner_Flow_m_findStateByName: Method = Method(name="findStateByName", parameters={Parameter(name='name')}, type=NamedState)
FlowDesigner_Flow_m_hasLastState: Method = Method(name="hasLastState", parameters={}, type=BooleanType)
FlowDesigner_Flow.methods={FlowDesigner_Flow_m_findStateByName, FlowDesigner_Flow_m_hasLastState}

# FlowDesigner_InitialState class attributes and methods
FlowDesigner_InitialState_initialize: Property = Property(name="initialize", type=StringType)
FlowDesigner_InitialState.attributes={FlowDesigner_InitialState_initialize}

# Source class attributes and methods

# FlowDesigner_FinalState class attributes and methods
FlowDesigner_FinalState_finalize: Property = Property(name="finalize", type=StringType)
FlowDesigner_FinalState.attributes={FlowDesigner_FinalState_finalize}

# Target class attributes and methods

# FlowDesigner_ActionState class attributes and methods

# NamedState class attributes and methods

# FlowDesigner_ViewState class attributes and methods
FlowDesigner_ViewState_view: Property = Property(name="view", type=StringType)
FlowDesigner_ViewState.attributes={FlowDesigner_ViewState_view}

# FlowDesigner_Event class attributes and methods
FlowDesigner_Event_event: Property = Property(name="event", type=StringType)
FlowDesigner_Event_action: Property = Property(name="action", type=StringType)
FlowDesigner_Event_guard: Property = Property(name="guard", type=StringType)
FlowDesigner_Event.attributes={FlowDesigner_Event_event, FlowDesigner_Event_action, FlowDesigner_Event_guard}

# FlowDesigner_Target class attributes and methods
FlowDesigner_Target_m_canBeTarget: Method = Method(name="canBeTarget", parameters={Parameter(name='source')}, type=BooleanType)
FlowDesigner_Target.methods={FlowDesigner_Target_m_canBeTarget}

# FlowDesigner_Source class attributes and methods
FlowDesigner_Source_m_canBeSource: Method = Method(name="canBeSource", parameters={Parameter(name='target')}, type=BooleanType)
FlowDesigner_Source.methods={FlowDesigner_Source_m_canBeSource}

# FlowDesigner_NamedState class attributes and methods
FlowDesigner_NamedState_exit: Property = Property(name="exit", type=StringType)
FlowDesigner_NamedState_entry: Property = Property(name="entry", type=StringType)
FlowDesigner_NamedState_name: Property = Property(name="name", type=StringType)
FlowDesigner_NamedState_activity: Property = Property(name="activity", type=StringType)
FlowDesigner_NamedState.attributes={FlowDesigner_NamedState_name, FlowDesigner_NamedState_exit, FlowDesigner_NamedState_activity, FlowDesigner_NamedState_entry}

# Relationships
nextState0: BinaryAssociation = BinaryAssociation(
    name="nextState0",
    ends={
        Property(name="FlowDesigner_Target", type=FlowDesigner_Event, multiplicity=Multiplicity(1, 1)),
        Property(name="FlowDesigner_Event", type=FlowDesigner_Target, multiplicity=Multiplicity(1, 1))
    }
)
events1: BinaryAssociation = BinaryAssociation(
    name="events1",
    ends={
        Property(name="FlowDesigner_Event2", type=FlowDesigner_Source, multiplicity=Multiplicity(1, 1)),
        Property(name="FlowDesigner_Source", type=FlowDesigner_Event, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
initialState3: BinaryAssociation = BinaryAssociation(
    name="initialState3",
    ends={
        Property(name="FlowDesigner_InitialState", type=FlowDesigner_Flow, multiplicity=Multiplicity(1, 1)),
        Property(name="FlowDesigner_Flow", type=FlowDesigner_InitialState, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
states4: BinaryAssociation = BinaryAssociation(
    name="states4",
    ends={
        Property(name="FlowDesigner_NamedState", type=FlowDesigner_Flow, multiplicity=Multiplicity(1, 1)),
        Property(name="FlowDesigner_Flow5", type=FlowDesigner_NamedState, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
finalState6: BinaryAssociation = BinaryAssociation(
    name="finalState6",
    ends={
        Property(name="FlowDesigner_FinalState", type=FlowDesigner_Flow, multiplicity=Multiplicity(1, 1)),
        Property(name="FlowDesigner_Flow7", type=FlowDesigner_FinalState, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_FlowDesigner_InitialState_Source = Generalization(general=Source, specific=FlowDesigner_InitialState)
gen_FlowDesigner_FinalState_Target = Generalization(general=Target, specific=FlowDesigner_FinalState)
gen_FlowDesigner_ActionState_NamedState = Generalization(general=NamedState, specific=FlowDesigner_ActionState)
gen_FlowDesigner_ViewState_NamedState = Generalization(general=NamedState, specific=FlowDesigner_ViewState)
gen_FlowDesigner_NamedState_Source = Generalization(general=Source, specific=FlowDesigner_NamedState)
gen_FlowDesigner_NamedState_Target = Generalization(general=Target, specific=FlowDesigner_NamedState)

# Domain Model
domain_model = DomainModel(
    name="FlowDesigner",
    types={FlowDesigner_Flow, FlowDesigner_InitialState, Source, FlowDesigner_FinalState, Target, FlowDesigner_ActionState, NamedState, FlowDesigner_ViewState, FlowDesigner_Event, FlowDesigner_Target, FlowDesigner_Source, FlowDesigner_NamedState},
    associations={nextState0, events1, initialState3, states4, finalState6},
    generalizations={gen_FlowDesigner_InitialState_Source, gen_FlowDesigner_FinalState_Target, gen_FlowDesigner_ActionState_NamedState, gen_FlowDesigner_ViewState_NamedState, gen_FlowDesigner_NamedState_Source, gen_FlowDesigner_NamedState_Target},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)