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
elevator = Class(name="elevator")
door = Class(name="door")
button = Class(name="button")
elevator_s_buttons = Class(name="elevator_s_buttons")
floor_s_buttons = Class(name="floor_s_buttons")

# elevator class attributes and methods
elevator_floor: Property = Property(name="floor", type=IntegerType)
elevator.attributes={elevator_floor}

# door class attributes and methods
door_close: Property = Property(name="close", type=BooleanType)
door.attributes={door_close}

# button class attributes and methods
button_number: Property = Property(name="number", type=IntegerType)
button.attributes={button_number}

# elevator_s_buttons class attributes and methods
elevator_s_buttons_number: Property = Property(name="number", type=IntegerType)
elevator_s_buttons.attributes={elevator_s_buttons_number}

# floor_s_buttons class attributes and methods
floor_s_buttons_number: Property = Property(name="number", type=BooleanType)
floor_s_buttons.attributes={floor_s_buttons_number}

# Relationships
elevator_door: BinaryAssociation = BinaryAssociation(
    name="elevator_door",
    ends={
        Property(name="door0", type=door, multiplicity=Multiplicity(1, 1)),
        Property(name="elevator1", type=elevator, multiplicity=Multiplicity(1, 1))
    }
)
elevator_button: BinaryAssociation = BinaryAssociation(
    name="elevator_button",
    ends={
        Property(name="button2", type=button, multiplicity=Multiplicity(0, 9999)),
        Property(name="elevator3", type=elevator, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_Bq5VcGSlEeio56zSTH7puw",
    types={elevator, door, button, elevator_s_buttons, floor_s_buttons},
    associations={elevator_door, elevator_button},
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