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
Microcontroller = Class(name="Microcontroller")
Door = Class(name="Door")
Camera = Class(name="Camera")
Speakers = Class(name="Speakers")
Geyser = Class(name="Geyser")
Light = Class(name="Light")
TV = Class(name="TV")
HomeTheatre = Class(name="HomeTheatre")
Entertainment_System = Class(name="Entertainment_System")
Fan = Class(name="Fan")
GSM_Module = Class(name="GSM_Module")
User__SMS_ = Class(name="User__SMS_")

# Microcontroller class attributes and methods
Microcontroller_Status: Property = Property(name="Status", type=StringType)
Microcontroller_Update: Property = Property(name="Update", type=FloatType)
Microcontroller.attributes={Microcontroller_Update, Microcontroller_Status}

# Door class attributes and methods
Door_DoorID: Property = Property(name="DoorID", type=IntegerType)
Door.attributes={Door_DoorID}

# Camera class attributes and methods
Camera_CameraID: Property = Property(name="CameraID", type=IntegerType)
Camera.attributes={Camera_CameraID}

# Speakers class attributes and methods
Speakers_SpeakerID: Property = Property(name="SpeakerID", type=IntegerType)
Speakers.attributes={Speakers_SpeakerID}

# Geyser class attributes and methods
Geyser_GeyserID: Property = Property(name="GeyserID", type=StringType)
Geyser.attributes={Geyser_GeyserID}

# Light class attributes and methods
Light_LightID: Property = Property(name="LightID", type=StringType)
Light.attributes={Light_LightID}

# TV class attributes and methods
TV_TVID: Property = Property(name="TVID", type=IntegerType)
TV.attributes={TV_TVID}

# HomeTheatre class attributes and methods
HomeTheatre_HTID: Property = Property(name="HTID", type=StringType)
HomeTheatre.attributes={HomeTheatre_HTID}

# Entertainment_System class attributes and methods
Entertainment_System_DeviceID: Property = Property(name="DeviceID", type=IntegerType)
Entertainment_System.attributes={Entertainment_System_DeviceID}

# Fan class attributes and methods
Fan_FanID: Property = Property(name="FanID", type=StringType)
Fan.attributes={Fan_FanID}

# GSM_Module class attributes and methods
GSM_Module_Status: Property = Property(name="Status", type=StringType)
GSM_Module_Update: Property = Property(name="Update", type=FloatType)
GSM_Module_CmdMatch: Property = Property(name="CmdMatch", type=StringType)
GSM_Module.attributes={GSM_Module_Status, GSM_Module_CmdMatch, GSM_Module_Update}

# User__SMS_ class attributes and methods
User__SMS__Status: Property = Property(name="Status", type=StringType)
User__SMS_.attributes={User__SMS__Status}

# Relationships
GSM_Module_Microcontroller: BinaryAssociation = BinaryAssociation(
    name="GSM_Module_Microcontroller",
    ends={
        Property(name="microcontroller12", type=Microcontroller, multiplicity=Multiplicity(0, 1)),
        Property(name="gSM_Module13", type=GSM_Module, multiplicity=Multiplicity(0, 1))
    }
)
Light_Fan: BinaryAssociation = BinaryAssociation(
    name="Light_Fan",
    ends={
        Property(name="fan14", type=Fan, multiplicity=Multiplicity(0, 1)),
        Property(name="light15", type=Light, multiplicity=Multiplicity(0, 1))
    }
)
Door_Camera: BinaryAssociation = BinaryAssociation(
    name="Door_Camera",
    ends={
        Property(name="camera0", type=Camera, multiplicity=Multiplicity(0, 9999)),
        Property(name="door1", type=Door, multiplicity=Multiplicity(1, 1))
    }
)
HomeTheatre_TV: BinaryAssociation = BinaryAssociation(
    name="HomeTheatre_TV",
    ends={
        Property(name="tV2", type=TV, multiplicity=Multiplicity(1, 1)),
        Property(name="homeTheatre3", type=HomeTheatre, multiplicity=Multiplicity(1, 9999))
    }
)
HomeTheatre_Speakers: BinaryAssociation = BinaryAssociation(
    name="HomeTheatre_Speakers",
    ends={
        Property(name="speakers4", type=Speakers, multiplicity=Multiplicity(0, 1)),
        Property(name="homeTheatre5", type=HomeTheatre, multiplicity=Multiplicity(1, 9999))
    }
)
TV_Entertainment: BinaryAssociation = BinaryAssociation(
    name="TV_Entertainment",
    ends={
        Property(name="entertainment6", type=Entertainment_System, multiplicity=Multiplicity(1, 1)),
        Property(name="tV7", type=TV, multiplicity=Multiplicity(1, 9999))
    }
)
Speakers_Entertainment: BinaryAssociation = BinaryAssociation(
    name="Speakers_Entertainment",
    ends={
        Property(name="entertainment8", type=Entertainment_System, multiplicity=Multiplicity(1, 1)),
        Property(name="speakers9", type=Speakers, multiplicity=Multiplicity(1, 9999))
    }
)
HomeTheatre_Entertainment: BinaryAssociation = BinaryAssociation(
    name="HomeTheatre_Entertainment",
    ends={
        Property(name="entertainment10", type=Entertainment_System, multiplicity=Multiplicity(1, 1)),
        Property(name="homeTheatre11", type=HomeTheatre, multiplicity=Multiplicity(1, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="a950fe37_832b_45d9_abd1_e6b229836b14",
    types={Microcontroller, Door, Camera, Speakers, Geyser, Light, TV, HomeTheatre, Entertainment_System, Fan, GSM_Module, User__SMS_},
    associations={GSM_Module_Microcontroller, Light_Fan, Door_Camera, HomeTheatre_TV, HomeTheatre_Speakers, TV_Entertainment, Speakers_Entertainment, HomeTheatre_Entertainment},
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