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
dependability2stochasticpetrinet_Dependability2StochasticPetriNetTrace = Class(name="dependability2stochasticpetrinet::Dependability2StochasticPetriNetTrace")
dependability2stochasticpetrinet_DependabilityModel = Class(name="dependability2stochasticpetrinet::DependabilityModel")
dependability2stochasticpetrinet_TraceLink = Class(name="dependability2stochasticpetrinet::TraceLink", is_abstract=True)
dependability2stochasticpetrinet_ErrorModel2PetriNetModule = Class(name="dependability2stochasticpetrinet::ErrorModel2PetriNetModule")
PetriNetModuleTraceLink = Class(name="PetriNetModuleTraceLink")
dependability2stochasticpetrinet_RailwayContainer = Class(name="dependability2stochasticpetrinet::RailwayContainer")
dependability2stochasticpetrinet_Place = Class(name="dependability2stochasticpetrinet::Place")
dependability2stochasticpetrinet_Transition = Class(name="dependability2stochasticpetrinet::Transition")
dependability2stochasticpetrinet_RailwayContainer2PetriNet = Class(name="dependability2stochasticpetrinet::RailwayContainer2PetriNet")
TraceLink = Class(name="TraceLink")
dependability2stochasticpetrinet_ErrorModel = Class(name="dependability2stochasticpetrinet::ErrorModel")
dependability2stochasticpetrinet_PetriNet = Class(name="dependability2stochasticpetrinet::PetriNet")
dependability2stochasticpetrinet_PetriNetModuleTraceLink = Class(name="dependability2stochasticpetrinet::PetriNetModuleTraceLink", is_abstract=True)
dependability2stochasticpetrinet_Node = Class(name="dependability2stochasticpetrinet::Node")
dependability2stochasticpetrinet_Arc = Class(name="dependability2stochasticpetrinet::Arc")
dependability2stochasticpetrinet_RequiredElement2Connection = Class(name="dependability2stochasticpetrinet::RequiredElement2Connection")

# dependability2stochasticpetrinet_Dependability2StochasticPetriNetTrace class attributes and methods

# dependability2stochasticpetrinet_DependabilityModel class attributes and methods

# dependability2stochasticpetrinet_TraceLink class attributes and methods

# dependability2stochasticpetrinet_ErrorModel2PetriNetModule class attributes and methods

# PetriNetModuleTraceLink class attributes and methods

# dependability2stochasticpetrinet_RailwayContainer class attributes and methods

# dependability2stochasticpetrinet_Place class attributes and methods

# dependability2stochasticpetrinet_Transition class attributes and methods

# dependability2stochasticpetrinet_RailwayContainer2PetriNet class attributes and methods

# TraceLink class attributes and methods

# dependability2stochasticpetrinet_ErrorModel class attributes and methods

# dependability2stochasticpetrinet_PetriNet class attributes and methods

# dependability2stochasticpetrinet_PetriNetModuleTraceLink class attributes and methods

# dependability2stochasticpetrinet_Node class attributes and methods

# dependability2stochasticpetrinet_Arc class attributes and methods

# dependability2stochasticpetrinet_RequiredElement2Connection class attributes and methods

# Relationships
dependabilityModel1: BinaryAssociation = BinaryAssociation(
    name="dependabilityModel1",
    ends={
        Property(name="dependability2stochasticpetrinet_DependabilityModel", type=dependability2stochasticpetrinet_Dependability2StochasticPetriNetTrace, multiplicity=Multiplicity(1, 1)),
        Property(name="dependability2stochasticpetrinet_Dependability2StochasticPetriNetTrace2", type=dependability2stochasticpetrinet_DependabilityModel, multiplicity=Multiplicity(1, 1))
    }
)
traceLinks3: BinaryAssociation = BinaryAssociation(
    name="traceLinks3",
    ends={
        Property(name="dependability2stochasticpetrinet_TraceLink", type=dependability2stochasticpetrinet_Dependability2StochasticPetriNetTrace, multiplicity=Multiplicity(1, 1)),
        Property(name="dependability2stochasticpetrinet_Dependability2StochasticPetriNetTrace4", type=dependability2stochasticpetrinet_TraceLink, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
railwayContainer0: BinaryAssociation = BinaryAssociation(
    name="railwayContainer0",
    ends={
        Property(name="dependability2stochasticpetrinet_RailwayContainer", type=dependability2stochasticpetrinet_Dependability2StochasticPetriNetTrace, multiplicity=Multiplicity(1, 1)),
        Property(name="dependability2stochasticpetrinet_Dependability2StochasticPetriNetTrace", type=dependability2stochasticpetrinet_RailwayContainer, multiplicity=Multiplicity(1, 1))
    }
)
up6: BinaryAssociation = BinaryAssociation(
    name="up6",
    ends={
        Property(name="dependability2stochasticpetrinet_Place", type=dependability2stochasticpetrinet_ErrorModel2PetriNetModule, multiplicity=Multiplicity(1, 1)),
        Property(name="dependability2stochasticpetrinet_ErrorModel2PetriNetModule7", type=dependability2stochasticpetrinet_Place, multiplicity=Multiplicity(1, 1))
    }
)
down8: BinaryAssociation = BinaryAssociation(
    name="down8",
    ends={
        Property(name="dependability2stochasticpetrinet_Place10", type=dependability2stochasticpetrinet_ErrorModel2PetriNetModule, multiplicity=Multiplicity(1, 1)),
        Property(name="dependability2stochasticpetrinet_ErrorModel2PetriNetModule9", type=dependability2stochasticpetrinet_Place, multiplicity=Multiplicity(1, 1))
    }
)
repair11: BinaryAssociation = BinaryAssociation(
    name="repair11",
    ends={
        Property(name="dependability2stochasticpetrinet_Transition", type=dependability2stochasticpetrinet_ErrorModel2PetriNetModule, multiplicity=Multiplicity(1, 1)),
        Property(name="dependability2stochasticpetrinet_ErrorModel2PetriNetModule12", type=dependability2stochasticpetrinet_Transition, multiplicity=Multiplicity(1, 1))
    }
)
errorModel5: BinaryAssociation = BinaryAssociation(
    name="errorModel5",
    ends={
        Property(name="dependability2stochasticpetrinet_ErrorModel", type=dependability2stochasticpetrinet_ErrorModel2PetriNetModule, multiplicity=Multiplicity(1, 1)),
        Property(name="dependability2stochasticpetrinet_ErrorModel2PetriNetModule", type=dependability2stochasticpetrinet_ErrorModel, multiplicity=Multiplicity(1, 1))
    }
)
petriNet15: BinaryAssociation = BinaryAssociation(
    name="petriNet15",
    ends={
        Property(name="dependability2stochasticpetrinet_PetriNet", type=dependability2stochasticpetrinet_RailwayContainer2PetriNet, multiplicity=Multiplicity(1, 1)),
        Property(name="dependability2stochasticpetrinet_RailwayContainer2PetriNet16", type=dependability2stochasticpetrinet_PetriNet, multiplicity=Multiplicity(1, 1))
    }
)
nodes17: BinaryAssociation = BinaryAssociation(
    name="nodes17",
    ends={
        Property(name="dependability2stochasticpetrinet_Node", type=dependability2stochasticpetrinet_PetriNetModuleTraceLink, multiplicity=Multiplicity(1, 1)),
        Property(name="dependability2stochasticpetrinet_PetriNetModuleTraceLink", type=dependability2stochasticpetrinet_Node, multiplicity=Multiplicity(0, 9999))
    }
)
arcs18: BinaryAssociation = BinaryAssociation(
    name="arcs18",
    ends={
        Property(name="dependability2stochasticpetrinet_Arc", type=dependability2stochasticpetrinet_PetriNetModuleTraceLink, multiplicity=Multiplicity(1, 1)),
        Property(name="dependability2stochasticpetrinet_PetriNetModuleTraceLink19", type=dependability2stochasticpetrinet_Arc, multiplicity=Multiplicity(0, 9999))
    }
)
railwayContainer13: BinaryAssociation = BinaryAssociation(
    name="railwayContainer13",
    ends={
        Property(name="dependability2stochasticpetrinet_RailwayContainer14", type=dependability2stochasticpetrinet_RailwayContainer2PetriNet, multiplicity=Multiplicity(1, 1)),
        Property(name="dependability2stochasticpetrinet_RailwayContainer2PetriNet", type=dependability2stochasticpetrinet_RailwayContainer, multiplicity=Multiplicity(1, 1))
    }
)
source20: BinaryAssociation = BinaryAssociation(
    name="source20",
    ends={
        Property(name="dependability2stochasticpetrinet_RequiredElement2Connection", type=dependability2stochasticpetrinet_ErrorModel, multiplicity=Multiplicity(1, 1)),
        Property(name="dependability2stochasticpetrinet_ErrorModel21", type=dependability2stochasticpetrinet_RequiredElement2Connection, multiplicity=Multiplicity(1, 1))
    }
)
target22: BinaryAssociation = BinaryAssociation(
    name="target22",
    ends={
        Property(name="dependability2stochasticpetrinet_ErrorModel24", type=dependability2stochasticpetrinet_RequiredElement2Connection, multiplicity=Multiplicity(1, 1)),
        Property(name="dependability2stochasticpetrinet_RequiredElement2Connection23", type=dependability2stochasticpetrinet_ErrorModel, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_dependability2stochasticpetrinet_ErrorModel2PetriNetModule_PetriNetModuleTraceLink = Generalization(general=PetriNetModuleTraceLink, specific=dependability2stochasticpetrinet_ErrorModel2PetriNetModule)
gen_dependability2stochasticpetrinet_RailwayContainer2PetriNet_TraceLink = Generalization(general=TraceLink, specific=dependability2stochasticpetrinet_RailwayContainer2PetriNet)
gen_dependability2stochasticpetrinet_PetriNetModuleTraceLink_TraceLink = Generalization(general=TraceLink, specific=dependability2stochasticpetrinet_PetriNetModuleTraceLink)
gen_dependability2stochasticpetrinet_RequiredElement2Connection_PetriNetModuleTraceLink = Generalization(general=PetriNetModuleTraceLink, specific=dependability2stochasticpetrinet_RequiredElement2Connection)

# Domain Model
domain_model = DomainModel(
    name="dependability2stochasticpetrinet",
    types={dependability2stochasticpetrinet_Dependability2StochasticPetriNetTrace, dependability2stochasticpetrinet_DependabilityModel, dependability2stochasticpetrinet_TraceLink, dependability2stochasticpetrinet_ErrorModel2PetriNetModule, PetriNetModuleTraceLink, dependability2stochasticpetrinet_RailwayContainer, dependability2stochasticpetrinet_Place, dependability2stochasticpetrinet_Transition, dependability2stochasticpetrinet_RailwayContainer2PetriNet, TraceLink, dependability2stochasticpetrinet_ErrorModel, dependability2stochasticpetrinet_PetriNet, dependability2stochasticpetrinet_PetriNetModuleTraceLink, dependability2stochasticpetrinet_Node, dependability2stochasticpetrinet_Arc, dependability2stochasticpetrinet_RequiredElement2Connection},
    associations={dependabilityModel1, traceLinks3, railwayContainer0, up6, down8, repair11, errorModel5, petriNet15, nodes17, arcs18, railwayContainer13, source20, target22},
    generalizations={gen_dependability2stochasticpetrinet_ErrorModel2PetriNetModule_PetriNetModuleTraceLink, gen_dependability2stochasticpetrinet_RailwayContainer2PetriNet_TraceLink, gen_dependability2stochasticpetrinet_PetriNetModuleTraceLink_TraceLink, gen_dependability2stochasticpetrinet_RequiredElement2Connection_PetriNetModuleTraceLink},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)