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
xDrone_Program = Class(name="xDrone::Program")
xDrone_Main = Class(name="xDrone::Main")
xDrone_Fly = Class(name="xDrone::Fly")
xDrone_Environment = Class(name="xDrone::Environment")
xDrone_SuperCommand = Class(name="xDrone::SuperCommand")
xDrone_Drone = Class(name="xDrone::Drone")
xDrone_Walls = Class(name="xDrone::Walls")
xDrone_Object = Class(name="xDrone::Object")
xDrone_Command = Class(name="xDrone::Command")
SuperCommand = Class(name="SuperCommand")
xDrone_GoTo = Class(name="xDrone::GoTo")
Command = Class(name="Command")
xDrone_Up = Class(name="xDrone::Up")
xDrone_Down = Class(name="xDrone::Down")
xDrone_Left = Class(name="xDrone::Left")
xDrone_Right = Class(name="xDrone::Right")
xDrone_Forward = Class(name="xDrone::Forward")
xDrone_Backward = Class(name="xDrone::Backward")
xDrone_RotateL = Class(name="xDrone::RotateL")
xDrone_RotateR = Class(name="xDrone::RotateR")
xDrone_Wait = Class(name="xDrone::Wait")
xDrone_Position = Class(name="xDrone::Position")
xDrone_Origin = Class(name="xDrone::Origin")
xDrone_Size = Class(name="xDrone::Size")
xDrone_Color = Class(name="xDrone::Color")
xDrone_Vector = Class(name="xDrone::Vector")
xDrone_FrontWall = Class(name="xDrone::FrontWall")
xDrone_RightWall = Class(name="xDrone::RightWall")
xDrone_BackWall = Class(name="xDrone::BackWall")
xDrone_LeftWall = Class(name="xDrone::LeftWall")
xDrone_UpWall = Class(name="xDrone::UpWall")

# xDrone_Program class attributes and methods

# xDrone_Main class attributes and methods

# xDrone_Fly class attributes and methods
xDrone_Fly_takeoff: Property = Property(name="takeoff", type=StringType)
xDrone_Fly_land: Property = Property(name="land", type=StringType)
xDrone_Fly.attributes={xDrone_Fly_takeoff, xDrone_Fly_land}

# xDrone_Environment class attributes and methods

# xDrone_SuperCommand class attributes and methods

# xDrone_Drone class attributes and methods
xDrone_Drone_rotation: Property = Property(name="rotation", type=StringType)
xDrone_Drone.attributes={xDrone_Drone_rotation}

# xDrone_Walls class attributes and methods

# xDrone_Object class attributes and methods
xDrone_Object_object_name: Property = Property(name="object_name", type=StringType)
xDrone_Object.attributes={xDrone_Object_object_name}

# xDrone_Command class attributes and methods

# SuperCommand class attributes and methods

# xDrone_GoTo class attributes and methods
xDrone_GoTo_object_name: Property = Property(name="object_name", type=StringType)
xDrone_GoTo.attributes={xDrone_GoTo_object_name}

# Command class attributes and methods

# xDrone_Up class attributes and methods
xDrone_Up_distance: Property = Property(name="distance", type=StringType)
xDrone_Up.attributes={xDrone_Up_distance}

# xDrone_Down class attributes and methods
xDrone_Down_distance: Property = Property(name="distance", type=StringType)
xDrone_Down.attributes={xDrone_Down_distance}

# xDrone_Left class attributes and methods
xDrone_Left_distance: Property = Property(name="distance", type=StringType)
xDrone_Left.attributes={xDrone_Left_distance}

# xDrone_Right class attributes and methods
xDrone_Right_distance: Property = Property(name="distance", type=StringType)
xDrone_Right.attributes={xDrone_Right_distance}

# xDrone_Forward class attributes and methods
xDrone_Forward_distance: Property = Property(name="distance", type=StringType)
xDrone_Forward.attributes={xDrone_Forward_distance}

# xDrone_Backward class attributes and methods
xDrone_Backward_distance: Property = Property(name="distance", type=StringType)
xDrone_Backward.attributes={xDrone_Backward_distance}

# xDrone_RotateL class attributes and methods
xDrone_RotateL_angle: Property = Property(name="angle", type=StringType)
xDrone_RotateL.attributes={xDrone_RotateL_angle}

# xDrone_RotateR class attributes and methods
xDrone_RotateR_angle: Property = Property(name="angle", type=StringType)
xDrone_RotateR.attributes={xDrone_RotateR_angle}

# xDrone_Wait class attributes and methods
xDrone_Wait_seconds: Property = Property(name="seconds", type=StringType)
xDrone_Wait.attributes={xDrone_Wait_seconds}

# xDrone_Position class attributes and methods

# xDrone_Origin class attributes and methods

# xDrone_Size class attributes and methods

# xDrone_Color class attributes and methods
xDrone_Color_color_value: Property = Property(name="color_value", type=StringType)
xDrone_Color.attributes={xDrone_Color_color_value}

# xDrone_Vector class attributes and methods
xDrone_Vector_x: Property = Property(name="x", type=StringType)
xDrone_Vector_y: Property = Property(name="y", type=StringType)
xDrone_Vector_z: Property = Property(name="z", type=StringType)
xDrone_Vector.attributes={xDrone_Vector_y, xDrone_Vector_x, xDrone_Vector_z}

# xDrone_FrontWall class attributes and methods
xDrone_FrontWall_value: Property = Property(name="value", type=StringType)
xDrone_FrontWall.attributes={xDrone_FrontWall_value}

# xDrone_RightWall class attributes and methods
xDrone_RightWall_value: Property = Property(name="value", type=StringType)
xDrone_RightWall.attributes={xDrone_RightWall_value}

# xDrone_BackWall class attributes and methods
xDrone_BackWall_value: Property = Property(name="value", type=StringType)
xDrone_BackWall.attributes={xDrone_BackWall_value}

# xDrone_LeftWall class attributes and methods
xDrone_LeftWall_value: Property = Property(name="value", type=StringType)
xDrone_LeftWall.attributes={xDrone_LeftWall_value}

# xDrone_UpWall class attributes and methods
xDrone_UpWall_value: Property = Property(name="value", type=StringType)
xDrone_UpWall.attributes={xDrone_UpWall_value}

# Relationships
main0: BinaryAssociation = BinaryAssociation(
    name="main0",
    ends={
        Property(name="xDrone_Main", type=xDrone_Program, multiplicity=Multiplicity(1, 1)),
        Property(name="xDrone_Program", type=xDrone_Main, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
fly1: BinaryAssociation = BinaryAssociation(
    name="fly1",
    ends={
        Property(name="xDrone_Fly", type=xDrone_Main, multiplicity=Multiplicity(1, 1)),
        Property(name="xDrone_Main2", type=xDrone_Fly, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
environment3: BinaryAssociation = BinaryAssociation(
    name="environment3",
    ends={
        Property(name="xDrone_Environment", type=xDrone_Main, multiplicity=Multiplicity(1, 1)),
        Property(name="xDrone_Main4", type=xDrone_Environment, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
commands5: BinaryAssociation = BinaryAssociation(
    name="commands5",
    ends={
        Property(name="xDrone_SuperCommand", type=xDrone_Fly, multiplicity=Multiplicity(1, 1)),
        Property(name="xDrone_Fly6", type=xDrone_SuperCommand, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
drone7: BinaryAssociation = BinaryAssociation(
    name="drone7",
    ends={
        Property(name="xDrone_Drone", type=xDrone_Environment, multiplicity=Multiplicity(1, 1)),
        Property(name="xDrone_Environment8", type=xDrone_Drone, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
walls9: BinaryAssociation = BinaryAssociation(
    name="walls9",
    ends={
        Property(name="xDrone_Walls", type=xDrone_Environment, multiplicity=Multiplicity(1, 1)),
        Property(name="xDrone_Environment10", type=xDrone_Walls, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
objects11: BinaryAssociation = BinaryAssociation(
    name="objects11",
    ends={
        Property(name="xDrone_Object", type=xDrone_Environment, multiplicity=Multiplicity(1, 1)),
        Property(name="xDrone_Environment12", type=xDrone_Object, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
position13: BinaryAssociation = BinaryAssociation(
    name="position13",
    ends={
        Property(name="xDrone_Position", type=xDrone_Drone, multiplicity=Multiplicity(1, 1)),
        Property(name="xDrone_Drone14", type=xDrone_Position, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
origin15: BinaryAssociation = BinaryAssociation(
    name="origin15",
    ends={
        Property(name="xDrone_Origin", type=xDrone_Object, multiplicity=Multiplicity(1, 1)),
        Property(name="xDrone_Object16", type=xDrone_Origin, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
size17: BinaryAssociation = BinaryAssociation(
    name="size17",
    ends={
        Property(name="xDrone_Size", type=xDrone_Object, multiplicity=Multiplicity(1, 1)),
        Property(name="xDrone_Object18", type=xDrone_Size, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
color19: BinaryAssociation = BinaryAssociation(
    name="color19",
    ends={
        Property(name="xDrone_Color", type=xDrone_Object, multiplicity=Multiplicity(1, 1)),
        Property(name="xDrone_Object20", type=xDrone_Color, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
vector21: BinaryAssociation = BinaryAssociation(
    name="vector21",
    ends={
        Property(name="xDrone_Vector", type=xDrone_Origin, multiplicity=Multiplicity(1, 1)),
        Property(name="xDrone_Origin22", type=xDrone_Vector, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
vector23: BinaryAssociation = BinaryAssociation(
    name="vector23",
    ends={
        Property(name="xDrone_Vector25", type=xDrone_Size, multiplicity=Multiplicity(1, 1)),
        Property(name="xDrone_Size24", type=xDrone_Vector, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
vector26: BinaryAssociation = BinaryAssociation(
    name="vector26",
    ends={
        Property(name="xDrone_Vector28", type=xDrone_Position, multiplicity=Multiplicity(1, 1)),
        Property(name="xDrone_Position27", type=xDrone_Vector, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
front29: BinaryAssociation = BinaryAssociation(
    name="front29",
    ends={
        Property(name="xDrone_FrontWall", type=xDrone_Walls, multiplicity=Multiplicity(1, 1)),
        Property(name="xDrone_Walls30", type=xDrone_FrontWall, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right31: BinaryAssociation = BinaryAssociation(
    name="right31",
    ends={
        Property(name="xDrone_RightWall", type=xDrone_Walls, multiplicity=Multiplicity(1, 1)),
        Property(name="xDrone_Walls32", type=xDrone_RightWall, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
back33: BinaryAssociation = BinaryAssociation(
    name="back33",
    ends={
        Property(name="xDrone_BackWall", type=xDrone_Walls, multiplicity=Multiplicity(1, 1)),
        Property(name="xDrone_Walls34", type=xDrone_BackWall, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left35: BinaryAssociation = BinaryAssociation(
    name="left35",
    ends={
        Property(name="xDrone_LeftWall", type=xDrone_Walls, multiplicity=Multiplicity(1, 1)),
        Property(name="xDrone_Walls36", type=xDrone_LeftWall, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
up37: BinaryAssociation = BinaryAssociation(
    name="up37",
    ends={
        Property(name="xDrone_UpWall", type=xDrone_Walls, multiplicity=Multiplicity(1, 1)),
        Property(name="xDrone_Walls38", type=xDrone_UpWall, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_xDrone_Command_SuperCommand = Generalization(general=SuperCommand, specific=xDrone_Command)
gen_xDrone_GoTo_Command = Generalization(general=Command, specific=xDrone_GoTo)
gen_xDrone_Up_Command = Generalization(general=Command, specific=xDrone_Up)
gen_xDrone_Down_Command = Generalization(general=Command, specific=xDrone_Down)
gen_xDrone_Left_Command = Generalization(general=Command, specific=xDrone_Left)
gen_xDrone_Right_Command = Generalization(general=Command, specific=xDrone_Right)
gen_xDrone_Forward_Command = Generalization(general=Command, specific=xDrone_Forward)
gen_xDrone_Backward_Command = Generalization(general=Command, specific=xDrone_Backward)
gen_xDrone_RotateL_Command = Generalization(general=Command, specific=xDrone_RotateL)
gen_xDrone_RotateR_Command = Generalization(general=Command, specific=xDrone_RotateR)
gen_xDrone_Wait_Command = Generalization(general=Command, specific=xDrone_Wait)

# Domain Model
domain_model = DomainModel(
    name="xDrone",
    types={xDrone_Program, xDrone_Main, xDrone_Fly, xDrone_Environment, xDrone_SuperCommand, xDrone_Drone, xDrone_Walls, xDrone_Object, xDrone_Command, SuperCommand, xDrone_GoTo, Command, xDrone_Up, xDrone_Down, xDrone_Left, xDrone_Right, xDrone_Forward, xDrone_Backward, xDrone_RotateL, xDrone_RotateR, xDrone_Wait, xDrone_Position, xDrone_Origin, xDrone_Size, xDrone_Color, xDrone_Vector, xDrone_FrontWall, xDrone_RightWall, xDrone_BackWall, xDrone_LeftWall, xDrone_UpWall},
    associations={main0, fly1, environment3, commands5, drone7, walls9, objects11, position13, origin15, size17, color19, vector21, vector23, vector26, front29, right31, back33, left35, up37},
    generalizations={gen_xDrone_Command_SuperCommand, gen_xDrone_GoTo_Command, gen_xDrone_Up_Command, gen_xDrone_Down_Command, gen_xDrone_Left_Command, gen_xDrone_Right_Command, gen_xDrone_Forward_Command, gen_xDrone_Backward_Command, gen_xDrone_RotateL_Command, gen_xDrone_RotateR_Command, gen_xDrone_Wait_Command},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)