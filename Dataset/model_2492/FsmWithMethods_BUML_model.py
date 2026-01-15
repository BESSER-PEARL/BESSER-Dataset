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
fsmWithMethods_Fsm = Class(name="fsmWithMethods::Fsm")
fsmWithMethods_State = Class(name="fsmWithMethods::State")
Referentiable = Class(name="Referentiable")
fsmWithMethods_Referentiable = Class(name="fsmWithMethods::Referentiable")
fsmWithMethods_Method = Class(name="fsmWithMethods::Method")
FExpression = Class(name="FExpression")
fsmWithMethods_MethodCall = Class(name="fsmWithMethods::MethodCall")
fsmWithMethods_Transition = Class(name="fsmWithMethods::Transition")
fsmWithMethods_FExpression = Class(name="fsmWithMethods::FExpression")
fsmWithMethods_Event = Class(name="fsmWithMethods::Event")

# fsmWithMethods_Fsm class attributes and methods
fsmWithMethods_Fsm_name: Property = Property(name="name", type=StringType)
fsmWithMethods_Fsm.attributes={fsmWithMethods_Fsm_name}

# fsmWithMethods_State class attributes and methods

# Referentiable class attributes and methods

# fsmWithMethods_Referentiable class attributes and methods

# fsmWithMethods_Method class attributes and methods

# FExpression class attributes and methods

# fsmWithMethods_MethodCall class attributes and methods

# fsmWithMethods_Transition class attributes and methods

# fsmWithMethods_FExpression class attributes and methods
fsmWithMethods_FExpression_name: Property = Property(name="name", type=StringType)
fsmWithMethods_FExpression.attributes={fsmWithMethods_FExpression_name}

# fsmWithMethods_Event class attributes and methods

# Relationships
expressions1: BinaryAssociation = BinaryAssociation(
    name="expressions1",
    ends={
        Property(name="fsmWithMethods_FExpression", type=fsmWithMethods_Fsm, multiplicity=Multiplicity(1, 1)),
        Property(name="fsmWithMethods_Fsm2", type=fsmWithMethods_FExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
params3: BinaryAssociation = BinaryAssociation(
    name="params3",
    ends={
        Property(name="fsmWithMethods_FExpression4", type=fsmWithMethods_Method, multiplicity=Multiplicity(1, 1)),
        Property(name="fsmWithMethods_Method", type=fsmWithMethods_FExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expressions5: BinaryAssociation = BinaryAssociation(
    name="expressions5",
    ends={
        Property(name="fsmWithMethods_FExpression7", type=fsmWithMethods_Method, multiplicity=Multiplicity(1, 1)),
        Property(name="fsmWithMethods_Method6", type=fsmWithMethods_FExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
method8: BinaryAssociation = BinaryAssociation(
    name="method8",
    ends={
        Property(name="fsmWithMethods_Method9", type=fsmWithMethods_MethodCall, multiplicity=Multiplicity(1, 1)),
        Property(name="fsmWithMethods_MethodCall", type=fsmWithMethods_Method, multiplicity=Multiplicity(0, 1))
    }
)
params10: BinaryAssociation = BinaryAssociation(
    name="params10",
    ends={
        Property(name="fsmWithMethods_Referentiable", type=fsmWithMethods_MethodCall, multiplicity=Multiplicity(1, 1)),
        Property(name="fsmWithMethods_MethodCall11", type=fsmWithMethods_Referentiable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
state0: BinaryAssociation = BinaryAssociation(
    name="state0",
    ends={
        Property(name="fsmWithMethods_State", type=fsmWithMethods_Fsm, multiplicity=Multiplicity(1, 1)),
        Property(name="fsmWithMethods_Fsm", type=fsmWithMethods_State, multiplicity=Multiplicity(0, 1))
    }
)
from14: BinaryAssociation = BinaryAssociation(
    name="from14",
    ends={
        Property(name="fsmWithMethods_FExpression16", type=fsmWithMethods_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="fsmWithMethods_Transition15", type=fsmWithMethods_FExpression, multiplicity=Multiplicity(0, 1))
    }
)
to17: BinaryAssociation = BinaryAssociation(
    name="to17",
    ends={
        Property(name="fsmWithMethods_FExpression19", type=fsmWithMethods_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="fsmWithMethods_Transition18", type=fsmWithMethods_FExpression, multiplicity=Multiplicity(0, 1))
    }
)
event12: BinaryAssociation = BinaryAssociation(
    name="event12",
    ends={
        Property(name="fsmWithMethods_FExpression13", type=fsmWithMethods_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="fsmWithMethods_Transition", type=fsmWithMethods_FExpression, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_fsmWithMethods_FExpression_Referentiable = Generalization(general=Referentiable, specific=fsmWithMethods_FExpression)
gen_fsmWithMethods_Method_FExpression = Generalization(general=FExpression, specific=fsmWithMethods_Method)
gen_fsmWithMethods_MethodCall_FExpression = Generalization(general=FExpression, specific=fsmWithMethods_MethodCall)
gen_fsmWithMethods_State_FExpression = Generalization(general=FExpression, specific=fsmWithMethods_State)
gen_fsmWithMethods_Transition_FExpression = Generalization(general=FExpression, specific=fsmWithMethods_Transition)
gen_fsmWithMethods_Event_FExpression = Generalization(general=FExpression, specific=fsmWithMethods_Event)

# Domain Model
domain_model = DomainModel(
    name="fsmWithMethods",
    types={fsmWithMethods_Fsm, fsmWithMethods_State, Referentiable, fsmWithMethods_Referentiable, fsmWithMethods_Method, FExpression, fsmWithMethods_MethodCall, fsmWithMethods_Transition, fsmWithMethods_FExpression, fsmWithMethods_Event},
    associations={expressions1, params3, expressions5, method8, params10, state0, from14, to17, event12},
    generalizations={gen_fsmWithMethods_FExpression_Referentiable, gen_fsmWithMethods_Method_FExpression, gen_fsmWithMethods_MethodCall_FExpression, gen_fsmWithMethods_State_FExpression, gen_fsmWithMethods_Transition_FExpression, gen_fsmWithMethods_Event_FExpression},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)