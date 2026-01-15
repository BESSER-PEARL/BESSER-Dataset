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
MetaModel_EvolutionStyle = Class(name="MetaModel::EvolutionStyle")
MetaModel_Transition = Class(name="MetaModel::Transition")
MetaModel_InitialState = Class(name="MetaModel::InitialState")
MetaModel_IntermidiateState = Class(name="MetaModel::IntermidiateState")
MetaModel_FinalState = Class(name="MetaModel::FinalState")
MetaModel_Operation = Class(name="MetaModel::Operation")
MetaModel_State = Class(name="MetaModel::State", is_abstract=True)
State = Class(name="State")

# MetaModel_EvolutionStyle class attributes and methods
MetaModel_EvolutionStyle_name: Property = Property(name="name", type=StringType)
MetaModel_EvolutionStyle.attributes={MetaModel_EvolutionStyle_name}

# MetaModel_Transition class attributes and methods
MetaModel_Transition_name: Property = Property(name="name", type=StringType)
MetaModel_Transition_description: Property = Property(name="description", type=StringType)
MetaModel_Transition.attributes={MetaModel_Transition_description, MetaModel_Transition_name}

# MetaModel_InitialState class attributes and methods

# MetaModel_IntermidiateState class attributes and methods

# MetaModel_FinalState class attributes and methods

# MetaModel_Operation class attributes and methods
MetaModel_Operation_name: Property = Property(name="name", type=StringType)
MetaModel_Operation_cost: Property = Property(name="cost", type=StringType)
MetaModel_Operation_time: Property = Property(name="time", type=StringType)
MetaModel_Operation.attributes={MetaModel_Operation_cost, MetaModel_Operation_name, MetaModel_Operation_time}

# MetaModel_State class attributes and methods
MetaModel_State_name: Property = Property(name="name", type=StringType)
MetaModel_State.attributes={MetaModel_State_name}

# State class attributes and methods

# Relationships
next14: BinaryAssociation = BinaryAssociation(
    name="next14",
    ends={
        Property(name="MetaModel_State16", type=MetaModel_InitialState, multiplicity=Multiplicity(1, 1)),
        Property(name="MetaModel_InitialState15", type=MetaModel_State, multiplicity=Multiplicity(1, 9999))
    }
)
next17: BinaryAssociation = BinaryAssociation(
    name="next17",
    ends={
        Property(name="MetaModel_State19", type=MetaModel_IntermidiateState, multiplicity=Multiplicity(1, 1)),
        Property(name="MetaModel_IntermidiateState18", type=MetaModel_State, multiplicity=Multiplicity(1, 9999))
    }
)
prev20: BinaryAssociation = BinaryAssociation(
    name="prev20",
    ends={
        Property(name="MetaModel_State22", type=MetaModel_IntermidiateState, multiplicity=Multiplicity(1, 1)),
        Property(name="MetaModel_IntermidiateState21", type=MetaModel_State, multiplicity=Multiplicity(1, 9999))
    }
)
prev23: BinaryAssociation = BinaryAssociation(
    name="prev23",
    ends={
        Property(name="MetaModel_State25", type=MetaModel_FinalState, multiplicity=Multiplicity(1, 1)),
        Property(name="MetaModel_FinalState24", type=MetaModel_State, multiplicity=Multiplicity(1, 9999))
    }
)
transitions0: BinaryAssociation = BinaryAssociation(
    name="transitions0",
    ends={
        Property(name="MetaModel_Transition", type=MetaModel_EvolutionStyle, multiplicity=Multiplicity(1, 1)),
        Property(name="MetaModel_EvolutionStyle", type=MetaModel_Transition, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
InitialArchitecture1: BinaryAssociation = BinaryAssociation(
    name="InitialArchitecture1",
    ends={
        Property(name="MetaModel_InitialState", type=MetaModel_EvolutionStyle, multiplicity=Multiplicity(1, 1)),
        Property(name="MetaModel_EvolutionStyle2", type=MetaModel_InitialState, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
states3: BinaryAssociation = BinaryAssociation(
    name="states3",
    ends={
        Property(name="MetaModel_IntermidiateState", type=MetaModel_EvolutionStyle, multiplicity=Multiplicity(1, 1)),
        Property(name="MetaModel_EvolutionStyle4", type=MetaModel_IntermidiateState, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
finalArchitecture5: BinaryAssociation = BinaryAssociation(
    name="finalArchitecture5",
    ends={
        Property(name="MetaModel_FinalState", type=MetaModel_EvolutionStyle, multiplicity=Multiplicity(1, 1)),
        Property(name="MetaModel_EvolutionStyle6", type=MetaModel_FinalState, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
operations7: BinaryAssociation = BinaryAssociation(
    name="operations7",
    ends={
        Property(name="MetaModel_Operation", type=MetaModel_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="MetaModel_Transition8", type=MetaModel_Operation, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
source9: BinaryAssociation = BinaryAssociation(
    name="source9",
    ends={
        Property(name="MetaModel_State", type=MetaModel_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="MetaModel_Transition10", type=MetaModel_State, multiplicity=Multiplicity(1, 1))
    }
)
target11: BinaryAssociation = BinaryAssociation(
    name="target11",
    ends={
        Property(name="MetaModel_State13", type=MetaModel_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="MetaModel_Transition12", type=MetaModel_State, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_MetaModel_IntermidiateState_State = Generalization(general=State, specific=MetaModel_IntermidiateState)
gen_MetaModel_FinalState_State = Generalization(general=State, specific=MetaModel_FinalState)
gen_MetaModel_InitialState_State = Generalization(general=State, specific=MetaModel_InitialState)

# Domain Model
domain_model = DomainModel(
    name="MetaModel",
    types={MetaModel_EvolutionStyle, MetaModel_Transition, MetaModel_InitialState, MetaModel_IntermidiateState, MetaModel_FinalState, MetaModel_Operation, MetaModel_State, State},
    associations={next14, next17, prev20, prev23, transitions0, InitialArchitecture1, states3, finalArchitecture5, operations7, source9, target11},
    generalizations={gen_MetaModel_IntermidiateState_State, gen_MetaModel_FinalState_State, gen_MetaModel_InitialState_State},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)