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
TKinter_Canvas = Class(name="TKinter_Canvas")
TKinter_Frame = Class(name="TKinter_Frame")
TKinter_Button = Class(name="TKinter_Button")
TKinter_TK = Class(name="TKinter_TK")
TKinter_Text = Class(name="TKinter_Text")
Panel_Panel = Class(name="Panel_Panel")
Elevator_Elevator = Class(name="Elevator_Elevator")
Floor_Floor = Class(name="Floor_Floor")
Building = Class(name="Building")

# TKinter_Canvas class attributes and methods

# TKinter_Frame class attributes and methods

# TKinter_Button class attributes and methods

# TKinter_TK class attributes and methods

# TKinter_Text class attributes and methods

# Panel_Panel class attributes and methods
Panel_Panel_flag_list: Property = Property(name="flag_list", type=BooleanType)
Panel_Panel_canvas: Property = Property(name="canvas", type=TKinter_Canvas)
Panel_Panel_button_list: Property = Property(name="button_list", type=TKinter_Button)
Panel_Panel.attributes={Panel_Panel_canvas, Panel_Panel_button_list, Panel_Panel_flag_list}

# Elevator_Elevator class attributes and methods
Elevator_Elevator_Width: Property = Property(name="Width", type=IntegerType)
Elevator_Elevator_Height: Property = Property(name="Height", type=IntegerType)
Elevator_Elevator_Velocity: Property = Property(name="Velocity", type=IntegerType)
Elevator_Elevator_building: Property = Property(name="building", type=TKinter_Canvas)
Elevator_Elevator_name: Property = Property(name="name", type=IntegerType)
Elevator_Elevator_destination: Property = Property(name="destination", type=IntegerType)
Elevator_Elevator_body: Property = Property(name="body", type=TKinter_Canvas)
Elevator_Elevator_call_queue: Property = Property(name="call_queue", type=Floor_Floor)
Elevator_Elevator_move_direction: Property = Property(name="move_direction", type=StringType)
Elevator_Elevator_gate_status: Property = Property(name="gate_status", type=StringType)
Elevator_Elevator_people: Property = Property(name="people", type=IntegerType)
Elevator_Elevator_ready: Property = Property(name="ready", type=BooleanType)
Elevator_Elevator_floor_list: Property = Property(name="floor_list", type=Floor_Floor)
Elevator_Elevator.attributes={Elevator_Elevator_Height, Elevator_Elevator_destination, Elevator_Elevator_gate_status, Elevator_Elevator_call_queue, Elevator_Elevator_move_direction, Elevator_Elevator_building, Elevator_Elevator_body, Elevator_Elevator_floor_list, Elevator_Elevator_Width, Elevator_Elevator_ready, Elevator_Elevator_people, Elevator_Elevator_Velocity, Elevator_Elevator_name}

# Floor_Floor class attributes and methods
Floor_Floor_name: Property = Property(name="name", type=IntegerType)
Floor_Floor_canvas: Property = Property(name="canvas", type=TKinter_Canvas)
Floor_Floor_up_status: Property = Property(name="up_status", type=StringType)
Floor_Floor_down_status: Property = Property(name="down_status", type=StringType)
Floor_Floor.attributes={Floor_Floor_canvas, Floor_Floor_down_status, Floor_Floor_up_status, Floor_Floor_name}

# Building class attributes and methods
Building_Building: Property = Property(name="Building", type=TKinter_Canvas)
Building_Panel: Property = Property(name="Panel", type=TKinter_Canvas)
Building_Elevator_list: Property = Property(name="Elevator_list", type=Elevator_Elevator)
Building_Panel_list: Property = Property(name="Panel_list", type=Panel_Panel)
Building.attributes={Building_Building, Building_Panel, Building_Elevator_list, Building_Panel_list}

# Relationships
Panel_Elevator: BinaryAssociation = BinaryAssociation(
    name="Panel_Elevator",
    ends={
        Property(name="elevator0", type=Elevator_Elevator, multiplicity=Multiplicity(0, 1)),
        Property(name="panel1", type=Panel_Panel, multiplicity=Multiplicity(0, 1))
    }
)
Floor_Elevator: BinaryAssociation = BinaryAssociation(
    name="Floor_Elevator",
    ends={
        Property(name="elevator2", type=Elevator_Elevator, multiplicity=Multiplicity(0, 1)),
        Property(name="floor3", type=Floor_Floor, multiplicity=Multiplicity(0, 1))
    }
)
Building_Panel: BinaryAssociation = BinaryAssociation(
    name="Building_Panel",
    ends={
        Property(name="panel4", type=Panel_Panel, multiplicity=Multiplicity(0, 1)),
        Property(name="building5", type=Building, multiplicity=Multiplicity(0, 1))
    }
)
Building_Elevator: BinaryAssociation = BinaryAssociation(
    name="Building_Elevator",
    ends={
        Property(name="elevator6", type=Elevator_Elevator, multiplicity=Multiplicity(0, 1)),
        Property(name="building7", type=Building, multiplicity=Multiplicity(0, 1))
    }
)
Building_Floor: BinaryAssociation = BinaryAssociation(
    name="Building_Floor",
    ends={
        Property(name="floor8", type=Floor_Floor, multiplicity=Multiplicity(0, 1)),
        Property(name="building9", type=Building, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_5d001fd4_1c48_4c10_bcbc_b1c8d15498c2",
    types={TKinter_Canvas, TKinter_Frame, TKinter_Button, TKinter_TK, TKinter_Text, Panel_Panel, Elevator_Elevator, Floor_Floor, Building},
    associations={Panel_Elevator, Floor_Elevator, Building_Panel, Building_Elevator, Building_Floor},
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