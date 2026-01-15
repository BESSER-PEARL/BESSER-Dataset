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

# Enumerations
LED_Color: Enumeration = Enumeration(
    name="LED_Color",
    literals={
            EnumerationLiteral(name="LED_ORANGE"),
			EnumerationLiteral(name="LED_RED"),
			EnumerationLiteral(name="LED_GREEN"),
			EnumerationLiteral(name="LED_OFF")
    }
)

Color: Enumeration = Enumeration(
    name="Color",
    literals={
            EnumerationLiteral(name="COLOR_BLACK"),
			EnumerationLiteral(name="COLOR_OFF"),
			EnumerationLiteral(name="COLOR_RED"),
			EnumerationLiteral(name="COLOR_BLUE"),
			EnumerationLiteral(name="COLOR_GREEN"),
			EnumerationLiteral(name="COLOR_ORANGE"),
			EnumerationLiteral(name="COLOR_WHITE")
    }
)

# Classes
marsRover_ultra = Class(name="marsRover::ultra")
marsRover_bumpers = Class(name="marsRover::bumpers")
marsRover_detect_lakes = Class(name="marsRover::detect::lakes")
marsRover_after_action = Class(name="marsRover::after::action")
marsRover_detect_rocks = Class(name="marsRover::detect::rocks")
marsRover_Robot = Class(name="marsRover::Robot")
marsRover_mission = Class(name="marsRover::mission")
marsRover_EObject = Class(name="marsRover::EObject")
marsRover_avoid_obstacles = Class(name="marsRover::avoid::obstacles")
marsRover_avoid_lakes = Class(name="marsRover::avoid::lakes")
marsRover_push_obstacles = Class(name="marsRover::push::obstacles")
marsRover_indication = Class(name="marsRover::indication")
marsRover_sound = Class(name="marsRover::sound")
marsRover_message = Class(name="marsRover::message")
marsRover_color_indication = Class(name="marsRover::color::indication")
marsRover_park = Class(name="marsRover::park")

# marsRover_ultra class attributes and methods
marsRover_ultra_name: Property = Property(name="name", type=StringType)
marsRover_ultra_distance: Property = Property(name="distance", type=IntegerType)
marsRover_ultra.attributes={marsRover_ultra_name, marsRover_ultra_distance}

# marsRover_bumpers class attributes and methods
marsRover_bumpers_name: Property = Property(name="name", type=StringType)
marsRover_bumpers.attributes={marsRover_bumpers_name}

# marsRover_detect_lakes class attributes and methods
marsRover_detect_lakes_name: Property = Property(name="name", type=StringType)
marsRover_detect_lakes_number_of_lakes: Property = Property(name="number_of_lakes", type=IntegerType)
marsRover_detect_lakes_lakes_colors: Property = Property(name="lakes_colors", type=StringType)
marsRover_detect_lakes.attributes={marsRover_detect_lakes_lakes_colors, marsRover_detect_lakes_number_of_lakes, marsRover_detect_lakes_name}

# marsRover_after_action class attributes and methods
marsRover_after_action_action: Property = Property(name="action", type=StringType)
marsRover_after_action.attributes={marsRover_after_action_action}

# marsRover_detect_rocks class attributes and methods
marsRover_detect_rocks_name: Property = Property(name="name", type=StringType)
marsRover_detect_rocks_number_of_rocks: Property = Property(name="number_of_rocks", type=IntegerType)
marsRover_detect_rocks.attributes={marsRover_detect_rocks_number_of_rocks, marsRover_detect_rocks_name}

# marsRover_Robot class attributes and methods
marsRover_Robot_name: Property = Property(name="name", type=StringType)
marsRover_Robot_slave_address: Property = Property(name="slave_address", type=StringType)
marsRover_Robot_drive_speed: Property = Property(name="drive_speed", type=IntegerType)
marsRover_Robot_special_speed: Property = Property(name="special_speed", type=IntegerType)
marsRover_Robot.attributes={marsRover_Robot_drive_speed, marsRover_Robot_slave_address, marsRover_Robot_name, marsRover_Robot_special_speed}

# marsRover_mission class attributes and methods
marsRover_mission_name: Property = Property(name="name", type=StringType)
marsRover_mission.attributes={marsRover_mission_name}

# marsRover_EObject class attributes and methods

# marsRover_avoid_obstacles class attributes and methods
marsRover_avoid_obstacles_name: Property = Property(name="name", type=StringType)
marsRover_avoid_obstacles.attributes={marsRover_avoid_obstacles_name}

# marsRover_avoid_lakes class attributes and methods
marsRover_avoid_lakes_name: Property = Property(name="name", type=StringType)
marsRover_avoid_lakes.attributes={marsRover_avoid_lakes_name}

# marsRover_push_obstacles class attributes and methods
marsRover_push_obstacles_name: Property = Property(name="name", type=StringType)
marsRover_push_obstacles.attributes={marsRover_push_obstacles_name}

# marsRover_indication class attributes and methods
marsRover_indication_name: Property = Property(name="name", type=StringType)
marsRover_indication.attributes={marsRover_indication_name}

# marsRover_sound class attributes and methods
marsRover_sound_name: Property = Property(name="name", type=StringType)
marsRover_sound_duration: Property = Property(name="duration", type=IntegerType)
marsRover_sound_frequency: Property = Property(name="frequency", type=IntegerType)
marsRover_sound.attributes={marsRover_sound_name, marsRover_sound_frequency, marsRover_sound_duration}

# marsRover_message class attributes and methods
marsRover_message_name: Property = Property(name="name", type=StringType)
marsRover_message_msg: Property = Property(name="msg", type=StringType)
marsRover_message.attributes={marsRover_message_name, marsRover_message_msg}

# marsRover_color_indication class attributes and methods
marsRover_color_indication_name: Property = Property(name="name", type=StringType)
marsRover_color_indication_color: Property = Property(name="color", type=StringType)
marsRover_color_indication.attributes={marsRover_color_indication_name, marsRover_color_indication_color}

# marsRover_park class attributes and methods
marsRover_park_name: Property = Property(name="name", type=StringType)
marsRover_park.attributes={marsRover_park_name}

# Relationships
after_examinating5: BinaryAssociation = BinaryAssociation(
    name="after_examinating5",
    ends={
        Property(name="marsRover_after_action", type=marsRover_detect_lakes, multiplicity=Multiplicity(1, 1)),
        Property(name="marsRover_detect_lakes", type=marsRover_after_action, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
missions0: BinaryAssociation = BinaryAssociation(
    name="missions0",
    ends={
        Property(name="marsRover_mission", type=marsRover_Robot, multiplicity=Multiplicity(1, 1)),
        Property(name="marsRover_Robot", type=marsRover_mission, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type1: BinaryAssociation = BinaryAssociation(
    name="type1",
    ends={
        Property(name="marsRover_EObject", type=marsRover_mission, multiplicity=Multiplicity(1, 1)),
        Property(name="marsRover_mission2", type=marsRover_EObject, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
sensors3: BinaryAssociation = BinaryAssociation(
    name="sensors3",
    ends={
        Property(name="marsRover_EObject4", type=marsRover_avoid_obstacles, multiplicity=Multiplicity(1, 1)),
        Property(name="marsRover_avoid_obstacles", type=marsRover_EObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
after_examinating6: BinaryAssociation = BinaryAssociation(
    name="after_examinating6",
    ends={
        Property(name="marsRover_after_action7", type=marsRover_detect_rocks, multiplicity=Multiplicity(1, 1)),
        Property(name="marsRover_detect_rocks", type=marsRover_after_action, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
indicate8: BinaryAssociation = BinaryAssociation(
    name="indicate8",
    ends={
        Property(name="marsRover_indication", type=marsRover_after_action, multiplicity=Multiplicity(1, 1)),
        Property(name="marsRover_after_action9", type=marsRover_indication, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type10: BinaryAssociation = BinaryAssociation(
    name="type10",
    ends={
        Property(name="marsRover_EObject12", type=marsRover_indication, multiplicity=Multiplicity(1, 1)),
        Property(name="marsRover_indication11", type=marsRover_EObject, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="marsRover",
    types={marsRover_ultra, marsRover_bumpers, marsRover_detect_lakes, marsRover_after_action, marsRover_detect_rocks, marsRover_Robot, marsRover_mission, marsRover_EObject, marsRover_avoid_obstacles, marsRover_avoid_lakes, marsRover_push_obstacles, marsRover_indication, marsRover_sound, marsRover_message, marsRover_color_indication, marsRover_park, LED_Color, Color},
    associations={after_examinating5, missions0, type1, sensors3, after_examinating6, indicate8, type10},
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