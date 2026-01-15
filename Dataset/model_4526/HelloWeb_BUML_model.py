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
helloWeb_Command = Class(name="helloWeb::Command")
helloWeb_FeatureMatch = Class(name="helloWeb::FeatureMatch")
SuperCommand = Class(name="SuperCommand")
helloWeb_Snapshot = Class(name="helloWeb::Snapshot")
Command = Class(name="Command")
helloWeb_Program = Class(name="helloWeb::Program")
helloWeb_Main = Class(name="helloWeb::Main")
helloWeb_SuperCommand = Class(name="helloWeb::SuperCommand")
helloWeb_RecordedFlight = Class(name="helloWeb::RecordedFlight")
helloWeb_UserFunction = Class(name="helloWeb::UserFunction")
helloWeb_Up = Class(name="helloWeb::Up")
helloWeb_Down = Class(name="helloWeb::Down")
helloWeb_Left = Class(name="helloWeb::Left")
helloWeb_Right = Class(name="helloWeb::Right")
helloWeb_Forward = Class(name="helloWeb::Forward")
helloWeb_Backward = Class(name="helloWeb::Backward")
helloWeb_RotateL = Class(name="helloWeb::RotateL")
helloWeb_RotateR = Class(name="helloWeb::RotateR")
helloWeb_Wait = Class(name="helloWeb::Wait")
helloWeb_FunctionName = Class(name="helloWeb::FunctionName")

# helloWeb_Command class attributes and methods

# helloWeb_FeatureMatch class attributes and methods
helloWeb_FeatureMatch_image_name: Property = Property(name="image_name", type=StringType)
helloWeb_FeatureMatch.attributes={helloWeb_FeatureMatch_image_name}

# SuperCommand class attributes and methods

# helloWeb_Snapshot class attributes and methods
helloWeb_Snapshot_image_name: Property = Property(name="image_name", type=StringType)
helloWeb_Snapshot.attributes={helloWeb_Snapshot_image_name}

# Command class attributes and methods

# helloWeb_Program class attributes and methods

# helloWeb_Main class attributes and methods
helloWeb_Main_takeoff: Property = Property(name="takeoff", type=StringType)
helloWeb_Main_land: Property = Property(name="land", type=StringType)
helloWeb_Main.attributes={helloWeb_Main_takeoff, helloWeb_Main_land}

# helloWeb_SuperCommand class attributes and methods

# helloWeb_RecordedFlight class attributes and methods
helloWeb_RecordedFlight_video_name: Property = Property(name="video_name", type=StringType)
helloWeb_RecordedFlight.attributes={helloWeb_RecordedFlight_video_name}

# helloWeb_UserFunction class attributes and methods
helloWeb_UserFunction_name: Property = Property(name="name", type=StringType)
helloWeb_UserFunction.attributes={helloWeb_UserFunction_name}

# helloWeb_Up class attributes and methods
helloWeb_Up_distance: Property = Property(name="distance", type=StringType)
helloWeb_Up.attributes={helloWeb_Up_distance}

# helloWeb_Down class attributes and methods
helloWeb_Down_distance: Property = Property(name="distance", type=StringType)
helloWeb_Down.attributes={helloWeb_Down_distance}

# helloWeb_Left class attributes and methods
helloWeb_Left_distance: Property = Property(name="distance", type=StringType)
helloWeb_Left.attributes={helloWeb_Left_distance}

# helloWeb_Right class attributes and methods
helloWeb_Right_distance: Property = Property(name="distance", type=StringType)
helloWeb_Right.attributes={helloWeb_Right_distance}

# helloWeb_Forward class attributes and methods
helloWeb_Forward_distance: Property = Property(name="distance", type=StringType)
helloWeb_Forward.attributes={helloWeb_Forward_distance}

# helloWeb_Backward class attributes and methods
helloWeb_Backward_distance: Property = Property(name="distance", type=StringType)
helloWeb_Backward.attributes={helloWeb_Backward_distance}

# helloWeb_RotateL class attributes and methods
helloWeb_RotateL_angle: Property = Property(name="angle", type=IntegerType)
helloWeb_RotateL.attributes={helloWeb_RotateL_angle}

# helloWeb_RotateR class attributes and methods
helloWeb_RotateR_angle: Property = Property(name="angle", type=IntegerType)
helloWeb_RotateR.attributes={helloWeb_RotateR_angle}

# helloWeb_Wait class attributes and methods
helloWeb_Wait_seconds: Property = Property(name="seconds", type=StringType)
helloWeb_Wait.attributes={helloWeb_Wait_seconds}

# helloWeb_FunctionName class attributes and methods
helloWeb_FunctionName_func_name: Property = Property(name="func_name", type=StringType)
helloWeb_FunctionName.attributes={helloWeb_FunctionName_func_name}

# Relationships
func3: BinaryAssociation = BinaryAssociation(
    name="func3",
    ends={
        Property(name="helloWeb_Command", type=helloWeb_UserFunction, multiplicity=Multiplicity(1, 1)),
        Property(name="helloWeb_UserFunction", type=helloWeb_Command, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
main0: BinaryAssociation = BinaryAssociation(
    name="main0",
    ends={
        Property(name="helloWeb_Main", type=helloWeb_Program, multiplicity=Multiplicity(1, 1)),
        Property(name="helloWeb_Program", type=helloWeb_Main, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
commands1: BinaryAssociation = BinaryAssociation(
    name="commands1",
    ends={
        Property(name="helloWeb_SuperCommand", type=helloWeb_Main, multiplicity=Multiplicity(1, 1)),
        Property(name="helloWeb_Main2", type=helloWeb_SuperCommand, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_helloWeb_Command_SuperCommand = Generalization(general=SuperCommand, specific=helloWeb_Command)
gen_helloWeb_Snapshot_Command = Generalization(general=Command, specific=helloWeb_Snapshot)
gen_helloWeb_Up_Command = Generalization(general=Command, specific=helloWeb_Up)
gen_helloWeb_Down_Command = Generalization(general=Command, specific=helloWeb_Down)
gen_helloWeb_Left_Command = Generalization(general=Command, specific=helloWeb_Left)
gen_helloWeb_Right_Command = Generalization(general=Command, specific=helloWeb_Right)
gen_helloWeb_Forward_Command = Generalization(general=Command, specific=helloWeb_Forward)
gen_helloWeb_Backward_Command = Generalization(general=Command, specific=helloWeb_Backward)
gen_helloWeb_RotateL_Command = Generalization(general=Command, specific=helloWeb_RotateL)
gen_helloWeb_RotateR_Command = Generalization(general=Command, specific=helloWeb_RotateR)
gen_helloWeb_Wait_Command = Generalization(general=Command, specific=helloWeb_Wait)
gen_helloWeb_FunctionName_SuperCommand = Generalization(general=SuperCommand, specific=helloWeb_FunctionName)

# Domain Model
domain_model = DomainModel(
    name="helloWeb",
    types={helloWeb_Command, helloWeb_FeatureMatch, SuperCommand, helloWeb_Snapshot, Command, helloWeb_Program, helloWeb_Main, helloWeb_SuperCommand, helloWeb_RecordedFlight, helloWeb_UserFunction, helloWeb_Up, helloWeb_Down, helloWeb_Left, helloWeb_Right, helloWeb_Forward, helloWeb_Backward, helloWeb_RotateL, helloWeb_RotateR, helloWeb_Wait, helloWeb_FunctionName},
    associations={func3, main0, commands1},
    generalizations={gen_helloWeb_Command_SuperCommand, gen_helloWeb_Snapshot_Command, gen_helloWeb_Up_Command, gen_helloWeb_Down_Command, gen_helloWeb_Left_Command, gen_helloWeb_Right_Command, gen_helloWeb_Forward_Command, gen_helloWeb_Backward_Command, gen_helloWeb_RotateL_Command, gen_helloWeb_RotateR_Command, gen_helloWeb_Wait_Command, gen_helloWeb_FunctionName_SuperCommand},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)