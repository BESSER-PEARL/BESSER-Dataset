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
Elevator_Controller = Class(name="Elevator_Controller")
_unnamed = Class(name="_unnamed")
Elevator_Controller_2 = Class(name="Elevator_Controller_2")
_unnamed1 = Class(name="_unnamed1")
Elevator = Class(name="Elevator")
Door = Class(name="Door")
Button = Class(name="Button")
Elevator_button = Class(name="Elevator_button")
Floor_button = Class(name="Floor_button")

# Elevator_Controller class attributes and methods
Elevator_Controller_Floor_ID: Property = Property(name="Floor_ID", type=IntegerType)
Elevator_Controller_Position: Property = Property(name="Position", type=IntegerType)
Elevator_Controller_Direction: Property = Property(name="Direction", type=BooleanType)
Elevator_Controller_attribute: Property = Property(name="attribute", type=StringType)
Elevator_Controller.attributes={Elevator_Controller_Position, Elevator_Controller_Floor_ID, Elevator_Controller_attribute, Elevator_Controller_Direction}

# _unnamed class attributes and methods

# Elevator_Controller_2 class attributes and methods
Elevator_Controller_2_Floor_ID: Property = Property(name="Floor_ID", type=IntegerType)
Elevator_Controller_2_Position: Property = Property(name="Position", type=IntegerType)
Elevator_Controller_2_Direction: Property = Property(name="Direction", type=BooleanType)
Elevator_Controller_2_attribute: Property = Property(name="attribute", type=StringType)
Elevator_Controller_2.attributes={Elevator_Controller_2_Direction, Elevator_Controller_2_Position, Elevator_Controller_2_attribute, Elevator_Controller_2_Floor_ID}

# _unnamed1 class attributes and methods

# Elevator class attributes and methods
Elevator_Direction: Property = Property(name="Direction", type=BooleanType)
Elevator_Current_Floor: Property = Property(name="Current_Floor", type=IntegerType)
Elevator_attribute3: Property = Property(name="attribute3", type=StringType)
Elevator.attributes={Elevator_Direction, Elevator_attribute3, Elevator_Current_Floor}

# Door class attributes and methods
Door_Close: Property = Property(name="Close", type=StringType)
Door.attributes={Door_Close}

# Button class attributes and methods
Button_illuminate: Property = Property(name="illuminate", type=StringType)
Button.attributes={Button_illuminate}

# Elevator_button class attributes and methods
Elevator_button_Floor_num: Property = Property(name="Floor_num", type=IntegerType)
Elevator_button.attributes={Elevator_button_Floor_num}

# Floor_button class attributes and methods
Floor_button_Floor_num: Property = Property(name="Floor_num", type=IntegerType)
Floor_button_Direction: Property = Property(name="Direction", type=BooleanType)
Floor_button.attributes={Floor_button_Direction, Floor_button_Floor_num}

# Relationships
Elevator_Elevator_Controller: BinaryAssociation = BinaryAssociation(
    name="Elevator_Elevator_Controller",
    ends={
        Property(name="elevator_Controller0", type=Elevator_Controller, multiplicity=Multiplicity(0, 1)),
        Property(name="elevator1", type=Elevator, multiplicity=Multiplicity(0, 1))
    }
)
Elevator_Controller__Door: BinaryAssociation = BinaryAssociation(
    name="Elevator_Controller__Door",
    ends={
        Property(name="N2", type=Door, multiplicity=Multiplicity(0, 1)),
        Property(name="elevator_Controller3", type=Elevator_Controller, multiplicity=Multiplicity(0, 1))
    }
)
Elevator_Elevator_Controller_2: BinaryAssociation = BinaryAssociation(
    name="Elevator_Elevator_Controller_2",
    ends={
        Property(name="_14", type=Elevator_Controller, multiplicity=Multiplicity(0, 1)),
        Property(name="n5", type=Elevator, multiplicity=Multiplicity(0, 1))
    }
)
Elevator_Controller__Button: BinaryAssociation = BinaryAssociation(
    name="Elevator_Controller__Button",
    ends={
        Property(name="_16", type=Button, multiplicity=Multiplicity(0, 1)),
        Property(name="m7", type=Elevator_Controller, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_HO3HYGc6EemNlbg3QBOQDg",
    types={Elevator_Controller, _unnamed, Elevator_Controller_2, _unnamed1, Elevator, Door, Button, Elevator_button, Floor_button},
    associations={Elevator_Elevator_Controller, Elevator_Controller__Door, Elevator_Elevator_Controller_2, Elevator_Controller__Button},
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