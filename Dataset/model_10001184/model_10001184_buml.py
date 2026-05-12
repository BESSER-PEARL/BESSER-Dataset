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
Abstract_Door = Class(name="Abstract_Door")
Abstract_Component = Class(name="Abstract_Component")
Rolling = Class(name="Rolling")
Swing_out = Class(name="Swing_out")
Locks_Handles = Class(name="Locks_Handles")
Coil_Spring_Cables = Class(name="Coil_Spring_Cables")
Remote_Controller_Interface = Class(name="Remote_Controller_Interface")
Motor = Class(name="Motor")
Rollers_Rails = Class(name="Rollers_Rails")
Controlling_Circuit = Class(name="Controlling_Circuit")
T = Class(name="T")
In_house_Component = Class(name="In_house_Component")
External_Component = Class(name="External_Component")
Door_Status = Class(name="Door_Status")
Light_Motion = Class(name="Light_Motion")
Break_in = Class(name="Break_in")

# Abstract_Door class attributes and methods
Abstract_Door_Automatic: Property = Property(name="Automatic", type=StringType)
Abstract_Door_Materials: Property = Property(name="Materials", type=StringType)
Abstract_Door_Security: Property = Property(name="Security", type=StringType)
Abstract_Door.attributes={Abstract_Door_Security, Abstract_Door_Automatic, Abstract_Door_Materials}

# Abstract_Component class attributes and methods
Abstract_Component_Type_Of_Component: Property = Property(name="Type_Of_Component", type=StringType)
Abstract_Component.attributes={Abstract_Component_Type_Of_Component}

# Rolling class attributes and methods
Rolling_Minimum_Space: Property = Property(name="Minimum_Space", type=StringType)
Rolling.attributes={Rolling_Minimum_Space}

# Swing_out class attributes and methods
Swing_out_Space_Clearance: Property = Property(name="Space_Clearance", type=StringType)
Swing_out.attributes={Swing_out_Space_Clearance}

# Locks_Handles class attributes and methods
Locks_Handles_Durable: Property = Property(name="Durable", type=StringType)
Locks_Handles_Secure: Property = Property(name="Secure", type=StringType)
Locks_Handles.attributes={Locks_Handles_Durable, Locks_Handles_Secure}

# Coil_Spring_Cables class attributes and methods
Coil_Spring_Cables_Spring_Stiffness: Property = Property(name="Spring_Stiffness", type=StringType)
Coil_Spring_Cables.attributes={Coil_Spring_Cables_Spring_Stiffness}

# Remote_Controller_Interface class attributes and methods
Remote_Controller_Interface_Bluebooth: Property = Property(name="Bluebooth", type=StringType)
Remote_Controller_Interface_Control_Garade_Door: Property = Property(name="Control_Garade_Door", type=StringType)
Remote_Controller_Interface.attributes={Remote_Controller_Interface_Bluebooth, Remote_Controller_Interface_Control_Garade_Door}

# Motor class attributes and methods
Motor_Durable: Property = Property(name="Durable", type=StringType)
Motor_Suitable_Speed: Property = Property(name="Suitable_Speed", type=StringType)
Motor.attributes={Motor_Durable, Motor_Suitable_Speed}

# Rollers_Rails class attributes and methods
Rollers_Rails_Good_Quality: Property = Property(name="Good_Quality", type=StringType)
Rollers_Rails.attributes={Rollers_Rails_Good_Quality}

# Controlling_Circuit class attributes and methods
Controlling_Circuit_MIcro_processor: Property = Property(name="MIcro_processor", type=StringType)
Controlling_Circuit_Software: Property = Property(name="Software", type=StringType)
Controlling_Circuit.attributes={Controlling_Circuit_Software, Controlling_Circuit_MIcro_processor}

# T class attributes and methods

# In_house_Component class attributes and methods
In_house_Component_Manufacture_Product: Property = Property(name="Manufacture_Product", type=StringType)
In_house_Component_Quality: Property = Property(name="Quality", type=StringType)
In_house_Component.attributes={In_house_Component_Manufacture_Product, In_house_Component_Quality}

# External_Component class attributes and methods
External_Component_Sensor: Property = Property(name="Sensor", type=BooleanType)
External_Component.attributes={External_Component_Sensor}

# Door_Status class attributes and methods
Door_Status_Door_Open: Property = Property(name="Door_Open", type=BooleanType)
Door_Status_Door_Close: Property = Property(name="Door_Close", type=StringType)
Door_Status.attributes={Door_Status_Door_Open, Door_Status_Door_Close}

# Light_Motion class attributes and methods
Light_Motion_Detects_Obstruction: Property = Property(name="Detects_Obstruction", type=BooleanType)
Light_Motion.attributes={Light_Motion_Detects_Obstruction}

# Break_in class attributes and methods
Break_in_Detect_Froce: Property = Property(name="Detect_Froce", type=BooleanType)
Break_in.attributes={Break_in_Detect_Froce}

# Domain Model
domain_model = DomainModel(
    name="_8f17289f_33e3_419d_b198_314bb07e5b67",
    types={Abstract_Door, Abstract_Component, Rolling, Swing_out, Locks_Handles, Coil_Spring_Cables, Remote_Controller_Interface, Motor, Rollers_Rails, Controlling_Circuit, T, In_house_Component, External_Component, Door_Status, Light_Motion, Break_in},
    associations={},
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