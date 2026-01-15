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
smachDSL_PrimitivePackage = Class(name="smachDSL::PrimitivePackage")
smachDSL_StateMachine = Class(name="smachDSL::StateMachine")
smachDSL_Test = Class(name="smachDSL::Test")
smachDSL_ActionClient = Class(name="smachDSL::ActionClient")
smachDSL_ServiceClient = Class(name="smachDSL::ServiceClient")
smachDSL_ActionState = Class(name="smachDSL::ActionState")
smachDSL_Transition = Class(name="smachDSL::Transition")

# smachDSL_PrimitivePackage class attributes and methods

# smachDSL_StateMachine class attributes and methods
smachDSL_StateMachine_name: Property = Property(name="name", type=StringType)
smachDSL_StateMachine.attributes={smachDSL_StateMachine_name}

# smachDSL_Test class attributes and methods
smachDSL_Test_ros: Property = Property(name="ros", type=StringType)
smachDSL_Test.attributes={smachDSL_Test_ros}

# smachDSL_ActionClient class attributes and methods
smachDSL_ActionClient_name: Property = Property(name="name", type=StringType)
smachDSL_ActionClient_actionname: Property = Property(name="actionname", type=StringType)
smachDSL_ActionClient_actiontype: Property = Property(name="actiontype", type=StringType)
smachDSL_ActionClient.attributes={smachDSL_ActionClient_actiontype, smachDSL_ActionClient_actionname, smachDSL_ActionClient_name}

# smachDSL_ServiceClient class attributes and methods
smachDSL_ServiceClient_name: Property = Property(name="name", type=StringType)
smachDSL_ServiceClient_servicename: Property = Property(name="servicename", type=StringType)
smachDSL_ServiceClient_servicesrv: Property = Property(name="servicesrv", type=StringType)
smachDSL_ServiceClient.attributes={smachDSL_ServiceClient_servicename, smachDSL_ServiceClient_name, smachDSL_ServiceClient_servicesrv}

# smachDSL_ActionState class attributes and methods
smachDSL_ActionState_name: Property = Property(name="name", type=StringType)
smachDSL_ActionState.attributes={smachDSL_ActionState_name}

# smachDSL_Transition class attributes and methods
smachDSL_Transition_outcome: Property = Property(name="outcome", type=StringType)
smachDSL_Transition.attributes={smachDSL_Transition_outcome}

# Relationships
statemachines0: BinaryAssociation = BinaryAssociation(
    name="statemachines0",
    ends={
        Property(name="smachDSL_StateMachine", type=smachDSL_PrimitivePackage, multiplicity=Multiplicity(1, 1)),
        Property(name="smachDSL_PrimitivePackage", type=smachDSL_StateMachine, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
actionclients1: BinaryAssociation = BinaryAssociation(
    name="actionclients1",
    ends={
        Property(name="smachDSL_ActionClient", type=smachDSL_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="smachDSL_StateMachine2", type=smachDSL_ActionClient, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
serviceclients3: BinaryAssociation = BinaryAssociation(
    name="serviceclients3",
    ends={
        Property(name="smachDSL_ServiceClient", type=smachDSL_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="smachDSL_StateMachine4", type=smachDSL_ServiceClient, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
actionsstates5: BinaryAssociation = BinaryAssociation(
    name="actionsstates5",
    ends={
        Property(name="smachDSL_ActionState", type=smachDSL_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="smachDSL_StateMachine6", type=smachDSL_ActionState, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
state12: BinaryAssociation = BinaryAssociation(
    name="state12",
    ends={
        Property(name="smachDSL_ActionState14", type=smachDSL_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="smachDSL_Transition13", type=smachDSL_ActionState, multiplicity=Multiplicity(0, 1))
    }
)
clientname7: BinaryAssociation = BinaryAssociation(
    name="clientname7",
    ends={
        Property(name="smachDSL_ActionClient9", type=smachDSL_ActionState, multiplicity=Multiplicity(1, 1)),
        Property(name="smachDSL_ActionState8", type=smachDSL_ActionClient, multiplicity=Multiplicity(0, 1))
    }
)
transitions10: BinaryAssociation = BinaryAssociation(
    name="transitions10",
    ends={
        Property(name="smachDSL_Transition", type=smachDSL_ActionState, multiplicity=Multiplicity(1, 1)),
        Property(name="smachDSL_ActionState11", type=smachDSL_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="smachDSL",
    types={smachDSL_PrimitivePackage, smachDSL_StateMachine, smachDSL_Test, smachDSL_ActionClient, smachDSL_ServiceClient, smachDSL_ActionState, smachDSL_Transition},
    associations={statemachines0, actionclients1, serviceclients3, actionsstates5, state12, clientname7, transitions10},
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