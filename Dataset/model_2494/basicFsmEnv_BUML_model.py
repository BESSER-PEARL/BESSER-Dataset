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
basicFsmEnv_State = Class(name="basicFsmEnv_State")
basicFsmEnv_Trans = Class(name="basicFsmEnv_Trans")
basicFsmEnv_VarDecl = Class(name="basicFsmEnv_VarDecl")
basicFsmEnv_Guard = Class(name="basicFsmEnv_Guard", is_abstract=True)
basicFsmEnv_Action = Class(name="basicFsmEnv_Action", is_abstract=True)
basicFsmEnv_InitialState = Class(name="basicFsmEnv_InitialState")
State = Class(name="State")
basicFsmEnv_Machine = Class(name="basicFsmEnv_Machine")

# basicFsmEnv_State class attributes and methods
basicFsmEnv_State_name: Property = Property(name="name", type=StringType)
basicFsmEnv_State.attributes={basicFsmEnv_State_name}

# basicFsmEnv_Trans class attributes and methods
basicFsmEnv_Trans_event: Property = Property(name="event", type=StringType)
basicFsmEnv_Trans.attributes={basicFsmEnv_Trans_event}

# basicFsmEnv_VarDecl class attributes and methods
basicFsmEnv_VarDecl_name: Property = Property(name="name", type=StringType)
basicFsmEnv_VarDecl_value: Property = Property(name="value", type=StringType)
basicFsmEnv_VarDecl.attributes={basicFsmEnv_VarDecl_value, basicFsmEnv_VarDecl_name}

# basicFsmEnv_Guard class attributes and methods

# basicFsmEnv_Action class attributes and methods

# basicFsmEnv_InitialState class attributes and methods

# State class attributes and methods

# basicFsmEnv_Machine class attributes and methods
basicFsmEnv_Machine_name: Property = Property(name="name", type=StringType)
basicFsmEnv_Machine.attributes={basicFsmEnv_Machine_name}

# Relationships
states0: BinaryAssociation = BinaryAssociation(
    name="states0",
    ends={
        Property(name="basicFsmEnv_State", type=basicFsmEnv_Machine, multiplicity=Multiplicity(1, 1)),
        Property(name="basicFsmEnv_Machine", type=basicFsmEnv_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
trans1: BinaryAssociation = BinaryAssociation(
    name="trans1",
    ends={
        Property(name="basicFsmEnv_Trans", type=basicFsmEnv_Machine, multiplicity=Multiplicity(1, 1)),
        Property(name="basicFsmEnv_Machine2", type=basicFsmEnv_Trans, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
in_3: BinaryAssociation = BinaryAssociation(
    name="in_3",
    ends={
        Property(name="Trans", type=basicFsmEnv_State, multiplicity=Multiplicity(1, 1)),
        Property(name="tgt", type=basicFsmEnv_Trans, multiplicity=Multiplicity(0, 9999))
    }
)
out4: BinaryAssociation = BinaryAssociation(
    name="out4",
    ends={
        Property(name="Trans5", type=basicFsmEnv_State, multiplicity=Multiplicity(1, 1)),
        Property(name="src", type=basicFsmEnv_Trans, multiplicity=Multiplicity(0, 9999))
    }
)
decls6: BinaryAssociation = BinaryAssociation(
    name="decls6",
    ends={
        Property(name="basicFsmEnv_VarDecl", type=basicFsmEnv_State, multiplicity=Multiplicity(1, 1)),
        Property(name="basicFsmEnv_State7", type=basicFsmEnv_VarDecl, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
tgt8: BinaryAssociation = BinaryAssociation(
    name="tgt8",
    ends={
        Property(name="State", type=basicFsmEnv_Trans, multiplicity=Multiplicity(1, 1)),
        Property(name="in_", type=basicFsmEnv_State, multiplicity=Multiplicity(1, 1))
    }
)
src9: BinaryAssociation = BinaryAssociation(
    name="src9",
    ends={
        Property(name="State10", type=basicFsmEnv_Trans, multiplicity=Multiplicity(1, 1)),
        Property(name="out", type=basicFsmEnv_State, multiplicity=Multiplicity(1, 1))
    }
)
guard11: BinaryAssociation = BinaryAssociation(
    name="guard11",
    ends={
        Property(name="basicFsmEnv_Guard", type=basicFsmEnv_Trans, multiplicity=Multiplicity(1, 1)),
        Property(name="basicFsmEnv_Trans12", type=basicFsmEnv_Guard, multiplicity=Multiplicity(0, 1))
    }
)
action13: BinaryAssociation = BinaryAssociation(
    name="action13",
    ends={
        Property(name="basicFsmEnv_Action", type=basicFsmEnv_Trans, multiplicity=Multiplicity(1, 1)),
        Property(name="basicFsmEnv_Trans14", type=basicFsmEnv_Action, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_basicFsmEnv_InitialState_State = Generalization(general=State, specific=basicFsmEnv_InitialState)

# Domain Model
domain_model = DomainModel(
    name="basicFsmEnv",
    types={basicFsmEnv_State, basicFsmEnv_Trans, basicFsmEnv_VarDecl, basicFsmEnv_Guard, basicFsmEnv_Action, basicFsmEnv_InitialState, State, basicFsmEnv_Machine},
    associations={states0, trans1, in_3, out4, decls6, tgt8, src9, guard11, action13},
    generalizations={gen_basicFsmEnv_InitialState_State},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)