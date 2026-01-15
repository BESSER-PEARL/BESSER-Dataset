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
basicfsm_State = Class(name="basicfsm::State")
basicfsm_Trans = Class(name="basicfsm::Trans")
basicfsm_Machine = Class(name="basicfsm::Machine")
basicfsm_VarDecl = Class(name="basicfsm::VarDecl")
basicfsm_Guard = Class(name="basicfsm::Guard", is_abstract=True)
basicfsm_Action = Class(name="basicfsm::Action", is_abstract=True)
basicfsm_InitialState = Class(name="basicfsm::InitialState")
State = Class(name="State")

# basicfsm_State class attributes and methods
basicfsm_State_name: Property = Property(name="name", type=StringType)
basicfsm_State.attributes={basicfsm_State_name}

# basicfsm_Trans class attributes and methods
basicfsm_Trans_event: Property = Property(name="event", type=StringType)
basicfsm_Trans.attributes={basicfsm_Trans_event}

# basicfsm_Machine class attributes and methods
basicfsm_Machine_name: Property = Property(name="name", type=StringType)
basicfsm_Machine.attributes={basicfsm_Machine_name}

# basicfsm_VarDecl class attributes and methods
basicfsm_VarDecl_name: Property = Property(name="name", type=StringType)
basicfsm_VarDecl_value: Property = Property(name="value", type=StringType)
basicfsm_VarDecl.attributes={basicfsm_VarDecl_name, basicfsm_VarDecl_value}

# basicfsm_Guard class attributes and methods

# basicfsm_Action class attributes and methods

# basicfsm_InitialState class attributes and methods

# State class attributes and methods

# Relationships
states0: BinaryAssociation = BinaryAssociation(
    name="states0",
    ends={
        Property(name="basicfsm_State", type=basicfsm_Machine, multiplicity=Multiplicity(1, 1)),
        Property(name="basicfsm_Machine", type=basicfsm_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
trans1: BinaryAssociation = BinaryAssociation(
    name="trans1",
    ends={
        Property(name="basicfsm_Trans", type=basicfsm_Machine, multiplicity=Multiplicity(1, 1)),
        Property(name="basicfsm_Machine2", type=basicfsm_Trans, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
out4: BinaryAssociation = BinaryAssociation(
    name="out4",
    ends={
        Property(name="Trans5", type=basicfsm_State, multiplicity=Multiplicity(1, 1)),
        Property(name="src", type=basicfsm_Trans, multiplicity=Multiplicity(0, 9999))
    }
)
decls6: BinaryAssociation = BinaryAssociation(
    name="decls6",
    ends={
        Property(name="basicfsm_VarDecl", type=basicfsm_State, multiplicity=Multiplicity(1, 1)),
        Property(name="basicfsm_State7", type=basicfsm_VarDecl, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
src8: BinaryAssociation = BinaryAssociation(
    name="src8",
    ends={
        Property(name="State", type=basicfsm_Trans, multiplicity=Multiplicity(1, 1)),
        Property(name="out", type=basicfsm_State, multiplicity=Multiplicity(0, 1))
    }
)
in3: BinaryAssociation = BinaryAssociation(
    name="in3",
    ends={
        Property(name="Trans", type=basicfsm_State, multiplicity=Multiplicity(1, 1)),
        Property(name="tgt", type=basicfsm_Trans, multiplicity=Multiplicity(0, 9999))
    }
)
tgt9: BinaryAssociation = BinaryAssociation(
    name="tgt9",
    ends={
        Property(name="in", type=basicfsm_State, multiplicity=Multiplicity(0, 1)),
        Property(name="State10", type=basicfsm_Trans, multiplicity=Multiplicity(1, 1))
    }
)
guard11: BinaryAssociation = BinaryAssociation(
    name="guard11",
    ends={
        Property(name="basicfsm_Guard", type=basicfsm_Trans, multiplicity=Multiplicity(1, 1)),
        Property(name="basicfsm_Trans12", type=basicfsm_Guard, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
action13: BinaryAssociation = BinaryAssociation(
    name="action13",
    ends={
        Property(name="basicfsm_Action", type=basicfsm_Trans, multiplicity=Multiplicity(1, 1)),
        Property(name="basicfsm_Trans14", type=basicfsm_Action, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_basicfsm_InitialState_State = Generalization(general=State, specific=basicfsm_InitialState)

# Domain Model
domain_model = DomainModel(
    name="basicfsm",
    types={basicfsm_State, basicfsm_Trans, basicfsm_Machine, basicfsm_VarDecl, basicfsm_Guard, basicfsm_Action, basicfsm_InitialState, State},
    associations={states0, trans1, out4, decls6, src8, in3, tgt9, guard11, action13},
    generalizations={gen_basicfsm_InitialState_State},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)