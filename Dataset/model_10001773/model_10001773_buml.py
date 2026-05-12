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
Owner = Class(name="Owner")
Login = Class(name="Login")
system = Class(name="system")
Appliances = Class(name="Appliances")
Fire_Alarm_system = Class(name="Fire_Alarm_system")
Home_Security_System = Class(name="Home_Security_System")
Department = Class(name="Department")
smokeAlarm = Class(name="smokeAlarm")
Police = Class(name="Police")
securityAlarm = Class(name="securityAlarm")
FireAlarm = Class(name="FireAlarm")

# Owner class attributes and methods
Owner_name: Property = Property(name="name", type=StringType)
Owner.attributes={Owner_name}

# Login class attributes and methods
Login_name: Property = Property(name="name", type=StringType)
Login_password: Property = Property(name="password", type=StringType)
Login.attributes={Login_name, Login_password}

# system class attributes and methods
system_status: Property = Property(name="status", type=BooleanType)
system.attributes={system_status}

# Appliances class attributes and methods
Appliances_On_status: Property = Property(name="On_status", type=BooleanType)
Appliances_Off_status: Property = Property(name="Off_status", type=BooleanType)
Appliances.attributes={Appliances_On_status, Appliances_Off_status}

# Fire_Alarm_system class attributes and methods
Fire_Alarm_system_system_On: Property = Property(name="system_On", type=BooleanType)
Fire_Alarm_system_system_Off: Property = Property(name="system_Off", type=BooleanType)
Fire_Alarm_system.attributes={Fire_Alarm_system_system_Off, Fire_Alarm_system_system_On}

# Home_Security_System class attributes and methods
Home_Security_System_system_On: Property = Property(name="system_On", type=BooleanType)
Home_Security_System_system_Off: Property = Property(name="system_Off", type=BooleanType)
Home_Security_System.attributes={Home_Security_System_system_Off, Home_Security_System_system_On}

# Department class attributes and methods
Department_name: Property = Property(name="name", type=StringType)
Department.attributes={Department_name}

# smokeAlarm class attributes and methods
smokeAlarm_status: Property = Property(name="status", type=BooleanType)
smokeAlarm.attributes={smokeAlarm_status}

# Police class attributes and methods
Police_name: Property = Property(name="name", type=StringType)
Police.attributes={Police_name}

# securityAlarm class attributes and methods
securityAlarm_status: Property = Property(name="status", type=BooleanType)
securityAlarm.attributes={securityAlarm_status}

# FireAlarm class attributes and methods
FireAlarm_status: Property = Property(name="status", type=BooleanType)
FireAlarm.attributes={FireAlarm_status}

# Relationships
access: BinaryAssociation = BinaryAssociation(
    name="access",
    ends={
        Property(name="login0", type=Login, multiplicity=Multiplicity(0, 1)),
        Property(name="owner1", type=Owner, multiplicity=Multiplicity(0, 1))
    }
)
handle: BinaryAssociation = BinaryAssociation(
    name="handle",
    ends={
        Property(name="system2", type=system, multiplicity=Multiplicity(0, 1)),
        Property(name="login23", type=Login, multiplicity=Multiplicity(0, 1))
    }
)
Department_Fire_Alarm_system: BinaryAssociation = BinaryAssociation(
    name="Department_Fire_Alarm_system",
    ends={
        Property(name="fire_Alarm_system4", type=Fire_Alarm_system, multiplicity=Multiplicity(0, 1)),
        Property(name="department5", type=Department, multiplicity=Multiplicity(0, 1))
    }
)
smokeAlarm_Fire_Alarm_system: BinaryAssociation = BinaryAssociation(
    name="smokeAlarm_Fire_Alarm_system",
    ends={
        Property(name="fire_Alarm_system6", type=Fire_Alarm_system, multiplicity=Multiplicity(0, 1)),
        Property(name="smokeAlarm7", type=smokeAlarm, multiplicity=Multiplicity(0, 1))
    }
)
Police_Home_Security_System: BinaryAssociation = BinaryAssociation(
    name="Police_Home_Security_System",
    ends={
        Property(name="home_Security_System8", type=Home_Security_System, multiplicity=Multiplicity(0, 1)),
        Property(name="police9", type=Police, multiplicity=Multiplicity(0, 1))
    }
)
securityAlarm_Home_Security_System: BinaryAssociation = BinaryAssociation(
    name="securityAlarm_Home_Security_System",
    ends={
        Property(name="home_Security_System10", type=Home_Security_System, multiplicity=Multiplicity(0, 1)),
        Property(name="securityAlarm11", type=securityAlarm, multiplicity=Multiplicity(0, 1))
    }
)
Fire_Alarm_system_FireAlarm: BinaryAssociation = BinaryAssociation(
    name="Fire_Alarm_system_FireAlarm",
    ends={
        Property(name="fireAlarm12", type=FireAlarm, multiplicity=Multiplicity(0, 1)),
        Property(name="fire_Alarm_system13", type=Fire_Alarm_system, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_UcHTQNkyEemDUejBZMo4Qg",
    types={Owner, Login, system, Appliances, Fire_Alarm_system, Home_Security_System, Department, smokeAlarm, Police, securityAlarm, FireAlarm},
    associations={access, handle, Department_Fire_Alarm_system, smokeAlarm_Fire_Alarm_system, Police_Home_Security_System, securityAlarm_Home_Security_System, Fire_Alarm_system_FireAlarm},
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