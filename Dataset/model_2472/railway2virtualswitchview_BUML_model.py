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
railway2virtualswitchview_VirtualSwitch = Class(name="railway2virtualswitchview::VirtualSwitch")
railway2virtualswitchview_Railway2VirtualSwitchViewTrace = Class(name="railway2virtualswitchview::Railway2VirtualSwitchViewTrace")
railway2virtualswitchview_RailwayContainer = Class(name="railway2virtualswitchview::RailwayContainer")
railway2virtualswitchview_Switch2VirtualSwitch = Class(name="railway2virtualswitchview::Switch2VirtualSwitch")
railway2virtualswitchview_Switch = Class(name="railway2virtualswitchview::Switch")

# railway2virtualswitchview_VirtualSwitch class attributes and methods

# railway2virtualswitchview_Railway2VirtualSwitchViewTrace class attributes and methods

# railway2virtualswitchview_RailwayContainer class attributes and methods

# railway2virtualswitchview_Switch2VirtualSwitch class attributes and methods

# railway2virtualswitchview_Switch class attributes and methods

# Relationships
virtualSwitch1: BinaryAssociation = BinaryAssociation(
    name="virtualSwitch1",
    ends={
        Property(name="railway2virtualswitchview_VirtualSwitch", type=railway2virtualswitchview_Switch2VirtualSwitch, multiplicity=Multiplicity(1, 1)),
        Property(name="railway2virtualswitchview_Switch2VirtualSwitch2", type=railway2virtualswitchview_VirtualSwitch, multiplicity=Multiplicity(0, 1))
    }
)
traceLinks3: BinaryAssociation = BinaryAssociation(
    name="traceLinks3",
    ends={
        Property(name="railway2virtualswitchview_Switch2VirtualSwitch4", type=railway2virtualswitchview_Railway2VirtualSwitchViewTrace, multiplicity=Multiplicity(1, 1)),
        Property(name="railway2virtualswitchview_Railway2VirtualSwitchViewTrace", type=railway2virtualswitchview_Switch2VirtualSwitch, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
source5: BinaryAssociation = BinaryAssociation(
    name="source5",
    ends={
        Property(name="railway2virtualswitchview_RailwayContainer", type=railway2virtualswitchview_Railway2VirtualSwitchViewTrace, multiplicity=Multiplicity(1, 1)),
        Property(name="railway2virtualswitchview_Railway2VirtualSwitchViewTrace6", type=railway2virtualswitchview_RailwayContainer, multiplicity=Multiplicity(0, 1))
    }
)
switch0: BinaryAssociation = BinaryAssociation(
    name="switch0",
    ends={
        Property(name="railway2virtualswitchview_Switch", type=railway2virtualswitchview_Switch2VirtualSwitch, multiplicity=Multiplicity(1, 1)),
        Property(name="railway2virtualswitchview_Switch2VirtualSwitch", type=railway2virtualswitchview_Switch, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="railway2virtualswitchview",
    types={railway2virtualswitchview_VirtualSwitch, railway2virtualswitchview_Railway2VirtualSwitchViewTrace, railway2virtualswitchview_RailwayContainer, railway2virtualswitchview_Switch2VirtualSwitch, railway2virtualswitchview_Switch},
    associations={virtualSwitch1, traceLinks3, source5, switch0},
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