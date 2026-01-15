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
platoon_Model = Class(name="platoon::Model")
platoon_Platoon = Class(name="platoon::Platoon")
platoon_Route = Class(name="platoon::Route")
platoon_Constraints = Class(name="platoon::Constraints")
platoon_LV = Class(name="platoon::LV")
platoon_FV = Class(name="platoon::FV")
platoon_Vehicle = Class(name="platoon::Vehicle")
platoon_Action = Class(name="platoon::Action")
Vehicle = Class(name="Vehicle")
platoon_Turn = Class(name="platoon::Turn")
Action = Class(name="Action")
platoon_Forward = Class(name="platoon::Forward")
platoon_Left = Class(name="platoon::Left")
Turn = Class(name="Turn")
platoon_Right = Class(name="platoon::Right")

# platoon_Model class attributes and methods

# platoon_Platoon class attributes and methods

# platoon_Route class attributes and methods
platoon_Route_name: Property = Property(name="name", type=StringType)
platoon_Route.attributes={platoon_Route_name}

# platoon_Constraints class attributes and methods
platoon_Constraints_minHeadway: Property = Property(name="minHeadway", type=IntegerType)
platoon_Constraints_maxHeadway: Property = Property(name="maxHeadway", type=IntegerType)
platoon_Constraints.attributes={platoon_Constraints_minHeadway, platoon_Constraints_maxHeadway}

# platoon_LV class attributes and methods

# platoon_FV class attributes and methods

# platoon_Vehicle class attributes and methods
platoon_Vehicle_name: Property = Property(name="name", type=StringType)
platoon_Vehicle.attributes={platoon_Vehicle_name}

# platoon_Action class attributes and methods

# Vehicle class attributes and methods

# platoon_Turn class attributes and methods

# Action class attributes and methods

# platoon_Forward class attributes and methods
platoon_Forward_distance: Property = Property(name="distance", type=IntegerType)
platoon_Forward.attributes={platoon_Forward_distance}

# platoon_Left class attributes and methods

# Turn class attributes and methods

# platoon_Right class attributes and methods

# Relationships
platoons0: BinaryAssociation = BinaryAssociation(
    name="platoons0",
    ends={
        Property(name="platoon_Platoon", type=platoon_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="platoon_Model", type=platoon_Platoon, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
routes1: BinaryAssociation = BinaryAssociation(
    name="routes1",
    ends={
        Property(name="platoon_Route", type=platoon_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="platoon_Model2", type=platoon_Route, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
constraints3: BinaryAssociation = BinaryAssociation(
    name="constraints3",
    ends={
        Property(name="platoon_Constraints", type=platoon_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="platoon_Model4", type=platoon_Constraints, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
first5: BinaryAssociation = BinaryAssociation(
    name="first5",
    ends={
        Property(name="platoon_LV", type=platoon_Platoon, multiplicity=Multiplicity(1, 1)),
        Property(name="platoon_Platoon6", type=platoon_LV, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
followers7: BinaryAssociation = BinaryAssociation(
    name="followers7",
    ends={
        Property(name="platoon_FV", type=platoon_Platoon, multiplicity=Multiplicity(1, 1)),
        Property(name="platoon_Platoon8", type=platoon_FV, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
pulledBy9: BinaryAssociation = BinaryAssociation(
    name="pulledBy9",
    ends={
        Property(name="platoon_Vehicle", type=platoon_FV, multiplicity=Multiplicity(1, 1)),
        Property(name="platoon_FV10", type=platoon_Vehicle, multiplicity=Multiplicity(0, 1))
    }
)
route11: BinaryAssociation = BinaryAssociation(
    name="route11",
    ends={
        Property(name="platoon_Route13", type=platoon_LV, multiplicity=Multiplicity(1, 1)),
        Property(name="platoon_LV12", type=platoon_Route, multiplicity=Multiplicity(0, 1))
    }
)
actions14: BinaryAssociation = BinaryAssociation(
    name="actions14",
    ends={
        Property(name="platoon_Action", type=platoon_Route, multiplicity=Multiplicity(1, 1)),
        Property(name="platoon_Route15", type=platoon_Action, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_platoon_LV_Vehicle = Generalization(general=Vehicle, specific=platoon_LV)
gen_platoon_FV_Vehicle = Generalization(general=Vehicle, specific=platoon_FV)
gen_platoon_Turn_Action = Generalization(general=Action, specific=platoon_Turn)
gen_platoon_Forward_Action = Generalization(general=Action, specific=platoon_Forward)
gen_platoon_Left_Turn = Generalization(general=Turn, specific=platoon_Left)
gen_platoon_Right_Turn = Generalization(general=Turn, specific=platoon_Right)

# Domain Model
domain_model = DomainModel(
    name="platoon",
    types={platoon_Model, platoon_Platoon, platoon_Route, platoon_Constraints, platoon_LV, platoon_FV, platoon_Vehicle, platoon_Action, Vehicle, platoon_Turn, Action, platoon_Forward, platoon_Left, Turn, platoon_Right},
    associations={platoons0, routes1, constraints3, first5, followers7, pulledBy9, route11, actions14},
    generalizations={gen_platoon_LV_Vehicle, gen_platoon_FV_Vehicle, gen_platoon_Turn_Action, gen_platoon_Forward_Action, gen_platoon_Left_Turn, gen_platoon_Right_Turn},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)