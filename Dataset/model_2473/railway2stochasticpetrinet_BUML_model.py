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
railway2stochasticpetrinet_Railway2StochasticPetriNetTrace = Class(name="railway2stochasticpetrinet::Railway2StochasticPetriNetTrace")
railway2stochasticpetrinet_RailwayContainer = Class(name="railway2stochasticpetrinet::RailwayContainer")
railway2stochasticpetrinet_PetriNetModuleTraceLink = Class(name="railway2stochasticpetrinet::PetriNetModuleTraceLink", is_abstract=True)
TraceLink = Class(name="TraceLink")
railway2stochasticpetrinet_Node = Class(name="railway2stochasticpetrinet::Node")
railway2stochasticpetrinet_Arc = Class(name="railway2stochasticpetrinet::Arc")
railway2stochasticpetrinet_Route2FailureModel = Class(name="railway2stochasticpetrinet::Route2FailureModel")
PetriNetModuleTraceLink = Class(name="PetriNetModuleTraceLink")
railway2stochasticpetrinet_Route = Class(name="railway2stochasticpetrinet::Route")
railway2stochasticpetrinet_Place = Class(name="railway2stochasticpetrinet::Place")
railway2stochasticpetrinet_ImmediateTransition = Class(name="railway2stochasticpetrinet::ImmediateTransition")
railway2stochasticpetrinet_TraceLink = Class(name="railway2stochasticpetrinet::TraceLink", is_abstract=True)
railway2stochasticpetrinet_RequiredElement2Connection = Class(name="railway2stochasticpetrinet::RequiredElement2Connection")
railway2stochasticpetrinet_RailwayContainer2PetriNet = Class(name="railway2stochasticpetrinet::RailwayContainer2PetriNet")
railway2stochasticpetrinet_PetriNet = Class(name="railway2stochasticpetrinet::PetriNet")
railway2stochasticpetrinet_RequiredElement2FailureModel = Class(name="railway2stochasticpetrinet::RequiredElement2FailureModel")
railway2stochasticpetrinet_RailwayElement = Class(name="railway2stochasticpetrinet::RailwayElement")

# railway2stochasticpetrinet_Railway2StochasticPetriNetTrace class attributes and methods

# railway2stochasticpetrinet_RailwayContainer class attributes and methods

# railway2stochasticpetrinet_PetriNetModuleTraceLink class attributes and methods

# TraceLink class attributes and methods

# railway2stochasticpetrinet_Node class attributes and methods

# railway2stochasticpetrinet_Arc class attributes and methods

# railway2stochasticpetrinet_Route2FailureModel class attributes and methods

# PetriNetModuleTraceLink class attributes and methods

# railway2stochasticpetrinet_Route class attributes and methods

# railway2stochasticpetrinet_Place class attributes and methods

# railway2stochasticpetrinet_ImmediateTransition class attributes and methods

# railway2stochasticpetrinet_TraceLink class attributes and methods

# railway2stochasticpetrinet_RequiredElement2Connection class attributes and methods

# railway2stochasticpetrinet_RailwayContainer2PetriNet class attributes and methods

# railway2stochasticpetrinet_PetriNet class attributes and methods

# railway2stochasticpetrinet_RequiredElement2FailureModel class attributes and methods

# railway2stochasticpetrinet_RailwayElement class attributes and methods

# Relationships
traceLinks0: BinaryAssociation = BinaryAssociation(
    name="traceLinks0",
    ends={
        Property(name="railway2stochasticpetrinet_TraceLink", type=railway2stochasticpetrinet_Railway2StochasticPetriNetTrace, multiplicity=Multiplicity(1, 1)),
        Property(name="railway2stochasticpetrinet_Railway2StochasticPetriNetTrace", type=railway2stochasticpetrinet_TraceLink, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
source1: BinaryAssociation = BinaryAssociation(
    name="source1",
    ends={
        Property(name="railway2stochasticpetrinet_RailwayContainer", type=railway2stochasticpetrinet_Railway2StochasticPetriNetTrace, multiplicity=Multiplicity(1, 1)),
        Property(name="railway2stochasticpetrinet_Railway2StochasticPetriNetTrace2", type=railway2stochasticpetrinet_RailwayContainer, multiplicity=Multiplicity(0, 1))
    }
)
nodes3: BinaryAssociation = BinaryAssociation(
    name="nodes3",
    ends={
        Property(name="railway2stochasticpetrinet_Node", type=railway2stochasticpetrinet_PetriNetModuleTraceLink, multiplicity=Multiplicity(1, 1)),
        Property(name="railway2stochasticpetrinet_PetriNetModuleTraceLink", type=railway2stochasticpetrinet_Node, multiplicity=Multiplicity(0, 9999))
    }
)
arcs4: BinaryAssociation = BinaryAssociation(
    name="arcs4",
    ends={
        Property(name="railway2stochasticpetrinet_Arc", type=railway2stochasticpetrinet_PetriNetModuleTraceLink, multiplicity=Multiplicity(1, 1)),
        Property(name="railway2stochasticpetrinet_PetriNetModuleTraceLink5", type=railway2stochasticpetrinet_Arc, multiplicity=Multiplicity(0, 9999))
    }
)
route6: BinaryAssociation = BinaryAssociation(
    name="route6",
    ends={
        Property(name="railway2stochasticpetrinet_Route", type=railway2stochasticpetrinet_Route2FailureModel, multiplicity=Multiplicity(1, 1)),
        Property(name="railway2stochasticpetrinet_Route2FailureModel", type=railway2stochasticpetrinet_Route, multiplicity=Multiplicity(0, 1))
    }
)
operational7: BinaryAssociation = BinaryAssociation(
    name="operational7",
    ends={
        Property(name="railway2stochasticpetrinet_Place", type=railway2stochasticpetrinet_Route2FailureModel, multiplicity=Multiplicity(1, 1)),
        Property(name="railway2stochasticpetrinet_Route2FailureModel8", type=railway2stochasticpetrinet_Place, multiplicity=Multiplicity(0, 1))
    }
)
failed9: BinaryAssociation = BinaryAssociation(
    name="failed9",
    ends={
        Property(name="railway2stochasticpetrinet_Place11", type=railway2stochasticpetrinet_Route2FailureModel, multiplicity=Multiplicity(1, 1)),
        Property(name="railway2stochasticpetrinet_Route2FailureModel10", type=railway2stochasticpetrinet_Place, multiplicity=Multiplicity(0, 1))
    }
)
repair12: BinaryAssociation = BinaryAssociation(
    name="repair12",
    ends={
        Property(name="railway2stochasticpetrinet_ImmediateTransition", type=railway2stochasticpetrinet_Route2FailureModel, multiplicity=Multiplicity(1, 1)),
        Property(name="railway2stochasticpetrinet_Route2FailureModel13", type=railway2stochasticpetrinet_ImmediateTransition, multiplicity=Multiplicity(0, 1))
    }
)
railwayElement14: BinaryAssociation = BinaryAssociation(
    name="railwayElement14",
    ends={
        Property(name="railway2stochasticpetrinet_RailwayElement", type=railway2stochasticpetrinet_RequiredElement2FailureModel, multiplicity=Multiplicity(1, 1)),
        Property(name="railway2stochasticpetrinet_RequiredElement2FailureModel", type=railway2stochasticpetrinet_RailwayElement, multiplicity=Multiplicity(0, 1))
    }
)
operational15: BinaryAssociation = BinaryAssociation(
    name="operational15",
    ends={
        Property(name="railway2stochasticpetrinet_Place17", type=railway2stochasticpetrinet_RequiredElement2FailureModel, multiplicity=Multiplicity(1, 1)),
        Property(name="railway2stochasticpetrinet_RequiredElement2FailureModel16", type=railway2stochasticpetrinet_Place, multiplicity=Multiplicity(0, 1))
    }
)
failed18: BinaryAssociation = BinaryAssociation(
    name="failed18",
    ends={
        Property(name="railway2stochasticpetrinet_Place20", type=railway2stochasticpetrinet_RequiredElement2FailureModel, multiplicity=Multiplicity(1, 1)),
        Property(name="railway2stochasticpetrinet_RequiredElement2FailureModel19", type=railway2stochasticpetrinet_Place, multiplicity=Multiplicity(0, 1))
    }
)
route21: BinaryAssociation = BinaryAssociation(
    name="route21",
    ends={
        Property(name="railway2stochasticpetrinet_Route22", type=railway2stochasticpetrinet_RequiredElement2Connection, multiplicity=Multiplicity(1, 1)),
        Property(name="railway2stochasticpetrinet_RequiredElement2Connection", type=railway2stochasticpetrinet_Route, multiplicity=Multiplicity(0, 1))
    }
)
railwayElement23: BinaryAssociation = BinaryAssociation(
    name="railwayElement23",
    ends={
        Property(name="railway2stochasticpetrinet_RailwayElement25", type=railway2stochasticpetrinet_RequiredElement2Connection, multiplicity=Multiplicity(1, 1)),
        Property(name="railway2stochasticpetrinet_RequiredElement2Connection24", type=railway2stochasticpetrinet_RailwayElement, multiplicity=Multiplicity(0, 1))
    }
)
railwayContainer26: BinaryAssociation = BinaryAssociation(
    name="railwayContainer26",
    ends={
        Property(name="railway2stochasticpetrinet_RailwayContainer27", type=railway2stochasticpetrinet_RailwayContainer2PetriNet, multiplicity=Multiplicity(1, 1)),
        Property(name="railway2stochasticpetrinet_RailwayContainer2PetriNet", type=railway2stochasticpetrinet_RailwayContainer, multiplicity=Multiplicity(0, 1))
    }
)
petriNet28: BinaryAssociation = BinaryAssociation(
    name="petriNet28",
    ends={
        Property(name="railway2stochasticpetrinet_PetriNet", type=railway2stochasticpetrinet_RailwayContainer2PetriNet, multiplicity=Multiplicity(1, 1)),
        Property(name="railway2stochasticpetrinet_RailwayContainer2PetriNet29", type=railway2stochasticpetrinet_PetriNet, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_railway2stochasticpetrinet_PetriNetModuleTraceLink_TraceLink = Generalization(general=TraceLink, specific=railway2stochasticpetrinet_PetriNetModuleTraceLink)
gen_railway2stochasticpetrinet_Route2FailureModel_PetriNetModuleTraceLink = Generalization(general=PetriNetModuleTraceLink, specific=railway2stochasticpetrinet_Route2FailureModel)
gen_railway2stochasticpetrinet_RequiredElement2Connection_PetriNetModuleTraceLink = Generalization(general=PetriNetModuleTraceLink, specific=railway2stochasticpetrinet_RequiredElement2Connection)
gen_railway2stochasticpetrinet_RailwayContainer2PetriNet_TraceLink = Generalization(general=TraceLink, specific=railway2stochasticpetrinet_RailwayContainer2PetriNet)
gen_railway2stochasticpetrinet_RequiredElement2FailureModel_PetriNetModuleTraceLink = Generalization(general=PetriNetModuleTraceLink, specific=railway2stochasticpetrinet_RequiredElement2FailureModel)

# Domain Model
domain_model = DomainModel(
    name="railway2stochasticpetrinet",
    types={railway2stochasticpetrinet_Railway2StochasticPetriNetTrace, railway2stochasticpetrinet_RailwayContainer, railway2stochasticpetrinet_PetriNetModuleTraceLink, TraceLink, railway2stochasticpetrinet_Node, railway2stochasticpetrinet_Arc, railway2stochasticpetrinet_Route2FailureModel, PetriNetModuleTraceLink, railway2stochasticpetrinet_Route, railway2stochasticpetrinet_Place, railway2stochasticpetrinet_ImmediateTransition, railway2stochasticpetrinet_TraceLink, railway2stochasticpetrinet_RequiredElement2Connection, railway2stochasticpetrinet_RailwayContainer2PetriNet, railway2stochasticpetrinet_PetriNet, railway2stochasticpetrinet_RequiredElement2FailureModel, railway2stochasticpetrinet_RailwayElement},
    associations={traceLinks0, source1, nodes3, arcs4, route6, operational7, failed9, repair12, railwayElement14, operational15, failed18, route21, railwayElement23, railwayContainer26, petriNet28},
    generalizations={gen_railway2stochasticpetrinet_PetriNetModuleTraceLink_TraceLink, gen_railway2stochasticpetrinet_Route2FailureModel_PetriNetModuleTraceLink, gen_railway2stochasticpetrinet_RequiredElement2Connection_PetriNetModuleTraceLink, gen_railway2stochasticpetrinet_RailwayContainer2PetriNet_TraceLink, gen_railway2stochasticpetrinet_RequiredElement2FailureModel_PetriNetModuleTraceLink},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)