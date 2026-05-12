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
smoke_sensor = Class(name="smoke_sensor")
camera_records = Class(name="camera_records")
InterfaceO_Interface = Class(name="InterfaceO_Interface")
temp_sensor = Class(name="temp_sensor")
control_panel = Class(name="control_panel")
door_sensor = Class(name="door_sensor")
flood_sensor = Class(name="flood_sensor")
Notification_System = Class(name="Notification_System")
owner_details = Class(name="owner_details")
login = Class(name="login")
eventlog = Class(name="eventlog")
timelog = Class(name="timelog")
fire_alarm_system = Class(name="fire_alarm_system")
flood_alarm_system = Class(name="flood_alarm_system")
ClassJ = Class(name="ClassJ")
door_alarm_system = Class(name="door_alarm_system")

# smoke_sensor class attributes and methods
smoke_sensor_smoke_sensor_id: Property = Property(name="smoke_sensor_id", type=IntegerType)
smoke_sensor_smoke_sensor_status: Property = Property(name="smoke_sensor_status", type=BooleanType)
smoke_sensor_smoke_sensor_location: Property = Property(name="smoke_sensor_location", type=StringType)
smoke_sensor_smoke_level_breach: Property = Property(name="smoke_level_breach", type=BooleanType)
smoke_sensor.attributes={smoke_sensor_smoke_sensor_status, smoke_sensor_smoke_sensor_id, smoke_sensor_smoke_sensor_location, smoke_sensor_smoke_level_breach}

# camera_records class attributes and methods
camera_records_camera_id: Property = Property(name="camera_id", type=IntegerType)
camera_records_camera_status_on: Property = Property(name="camera_status_on", type=BooleanType)
camera_records_camera_location: Property = Property(name="camera_location", type=StringType)
camera_records.attributes={camera_records_camera_location, camera_records_camera_id, camera_records_camera_status_on}

# InterfaceO_Interface class attributes and methods

# temp_sensor class attributes and methods
temp_sensor_temp_sensor_id: Property = Property(name="temp_sensor_id", type=IntegerType)
temp_sensor_temp_sensor_status: Property = Property(name="temp_sensor_status", type=BooleanType)
temp_sensor_temp_sensor_location: Property = Property(name="temp_sensor_location", type=StringType)
temp_sensor_temp_level_breach: Property = Property(name="temp_level_breach", type=BooleanType)
temp_sensor.attributes={temp_sensor_temp_sensor_id, temp_sensor_temp_level_breach, temp_sensor_temp_sensor_location, temp_sensor_temp_sensor_status}

# control_panel class attributes and methods
control_panel_system_on: Property = Property(name="system_on", type=BooleanType)
control_panel.attributes={control_panel_system_on}

# door_sensor class attributes and methods
door_sensor_door_sensor_id: Property = Property(name="door_sensor_id", type=IntegerType)
door_sensor_door_open_status: Property = Property(name="door_open_status", type=BooleanType)
door_sensor_door_location: Property = Property(name="door_location", type=StringType)
door_sensor.attributes={door_sensor_door_sensor_id, door_sensor_door_open_status, door_sensor_door_location}

# flood_sensor class attributes and methods
flood_sensor_flood_sensor_id: Property = Property(name="flood_sensor_id", type=IntegerType)
flood_sensor_flood_sensor_status: Property = Property(name="flood_sensor_status", type=BooleanType)
flood_sensor_flood_sensor_loaction: Property = Property(name="flood_sensor_loaction", type=StringType)
flood_sensor_waterlevel_breach_status: Property = Property(name="waterlevel_breach_status", type=BooleanType)
flood_sensor.attributes={flood_sensor_flood_sensor_id, flood_sensor_flood_sensor_loaction, flood_sensor_waterlevel_breach_status, flood_sensor_flood_sensor_status}

# Notification_System class attributes and methods
Notification_System_OwnerNum__Integer: Property = Property(name="OwnerNum__Integer", type=StringType)
Notification_System_OwnerEmail: Property = Property(name="OwnerEmail", type=StringType)
Notification_System_PublicSafetyNumber: Property = Property(name="PublicSafetyNumber", type=IntegerType)
Notification_System_PublicSafetyPage: Property = Property(name="PublicSafetyPage", type=IntegerType)
Notification_System.attributes={Notification_System_PublicSafetyNumber, Notification_System_OwnerNum__Integer, Notification_System_OwnerEmail, Notification_System_PublicSafetyPage}

# owner_details class attributes and methods
owner_details_ownerName: Property = Property(name="ownerName", type=StringType)
owner_details.attributes={owner_details_ownerName}

# login class attributes and methods
login_username: Property = Property(name="username", type=StringType)
login_password: Property = Property(name="password", type=StringType)
login_loginattempt: Property = Property(name="loginattempt", type=IntegerType)
login_lockout: Property = Property(name="lockout", type=IntegerType)
login_loginapp: Property = Property(name="loginapp", type=StringType)
login_logoutapp: Property = Property(name="logoutapp", type=StringType)
login.attributes={login_logoutapp, login_username, login_lockout, login_loginattempt, login_password, login_loginapp}

# eventlog class attributes and methods
eventlog_event_id: Property = Property(name="event_id", type=IntegerType)
eventlog_event_time: Property = Property(name="event_time", type=IntegerType)
eventlog_event_info: Property = Property(name="event_info", type=StringType)
eventlog.attributes={eventlog_event_info, eventlog_event_time, eventlog_event_id}

# timelog class attributes and methods
timelog_day: Property = Property(name="day", type=IntegerType)
timelog_month: Property = Property(name="month", type=IntegerType)
timelog_year: Property = Property(name="year", type=IntegerType)
timelog_hour: Property = Property(name="hour", type=IntegerType)
timelog_minutes: Property = Property(name="minutes", type=IntegerType)
timelog_seconds: Property = Property(name="seconds", type=IntegerType)
timelog.attributes={timelog_day, timelog_year, timelog_hour, timelog_minutes, timelog_month, timelog_seconds}

# fire_alarm_system class attributes and methods
fire_alarm_system_fire_alarm_system_on: Property = Property(name="fire_alarm_system_on", type=BooleanType)
fire_alarm_system.attributes={fire_alarm_system_fire_alarm_system_on}

# flood_alarm_system class attributes and methods
flood_alarm_system_flood_alarm_system: Property = Property(name="flood_alarm_system", type=BooleanType)
flood_alarm_system.attributes={flood_alarm_system_flood_alarm_system}

# ClassJ class attributes and methods

# door_alarm_system class attributes and methods
door_alarm_system_door_alarm_system: Property = Property(name="door_alarm_system", type=BooleanType)
door_alarm_system.attributes={door_alarm_system_door_alarm_system}

# Relationships
owner_details_login: BinaryAssociation = BinaryAssociation(
    name="owner_details_login",
    ends={
        Property(name="owner_details_login_00", type=login, multiplicity=Multiplicity(1, 1)),
        Property(name="owner_details_login_11", type=owner_details, multiplicity=Multiplicity(1, 1))
    }
)
assoc__U4MOxJiYEeqEM7mFKilpXw: BinaryAssociation = BinaryAssociation(
    name="assoc__U4MOxJiYEeqEM7mFKilpXw",
    ends={
        Property(name="assoc_02", type=login, multiplicity=Multiplicity(0, 1)),
        Property(name="assoc_13", type=eventlog, multiplicity=Multiplicity(1, 1))
    }
)
fire_alarm_system_smoke_sensor: BinaryAssociation = BinaryAssociation(
    name="fire_alarm_system_smoke_sensor",
    ends={
        Property(name="smoke_sensor4", type=smoke_sensor, multiplicity=Multiplicity(1, 9999)),
        Property(name="fire_alarm_system5", type=fire_alarm_system, multiplicity=Multiplicity(1, 1))
    }
)
fire_alarm_system_temp_sensor: BinaryAssociation = BinaryAssociation(
    name="fire_alarm_system_temp_sensor",
    ends={
        Property(name="temp_sensor6", type=temp_sensor, multiplicity=Multiplicity(1, 9999)),
        Property(name="fire_alarm_system7", type=fire_alarm_system, multiplicity=Multiplicity(1, 1))
    }
)
flood_alarm_system_flood_sensor: BinaryAssociation = BinaryAssociation(
    name="flood_alarm_system_flood_sensor",
    ends={
        Property(name="flood_sensor8", type=flood_sensor, multiplicity=Multiplicity(1, 9999)),
        Property(name="flood_alarm_system9", type=flood_alarm_system, multiplicity=Multiplicity(1, 1))
    }
)
door_alarm_system_door_sensor: BinaryAssociation = BinaryAssociation(
    name="door_alarm_system_door_sensor",
    ends={
        Property(name="door_sensor10", type=door_sensor, multiplicity=Multiplicity(1, 9999)),
        Property(name="door_alarm_system11", type=door_alarm_system, multiplicity=Multiplicity(1, 1))
    }
)
eventlog_fire_alarm_system: BinaryAssociation = BinaryAssociation(
    name="eventlog_fire_alarm_system",
    ends={
        Property(name="fire_alarm_system12", type=fire_alarm_system, multiplicity=Multiplicity(0, 1)),
        Property(name="eventlog13", type=eventlog, multiplicity=Multiplicity(0, 1))
    }
)
eventlog_flood_alarm_system: BinaryAssociation = BinaryAssociation(
    name="eventlog_flood_alarm_system",
    ends={
        Property(name="flood_alarm_system14", type=flood_alarm_system, multiplicity=Multiplicity(0, 1)),
        Property(name="eventlog15", type=eventlog, multiplicity=Multiplicity(0, 1))
    }
)
door_alarm_system_eventlog: BinaryAssociation = BinaryAssociation(
    name="door_alarm_system_eventlog",
    ends={
        Property(name="eventlog16", type=eventlog, multiplicity=Multiplicity(0, 1)),
        Property(name="door_alarm_system17", type=door_alarm_system, multiplicity=Multiplicity(0, 1))
    }
)
Notification_System_control_panel: BinaryAssociation = BinaryAssociation(
    name="Notification_System_control_panel",
    ends={
        Property(name="control_panel18", type=control_panel, multiplicity=Multiplicity(0, 1)),
        Property(name="notification_System19", type=Notification_System, multiplicity=Multiplicity(0, 1))
    }
)
eventlog_timelog: BinaryAssociation = BinaryAssociation(
    name="eventlog_timelog",
    ends={
        Property(name="timelog20", type=timelog, multiplicity=Multiplicity(0, 1)),
        Property(name="eventlog21", type=eventlog, multiplicity=Multiplicity(0, 1))
    }
)
timelog_Notification_System: BinaryAssociation = BinaryAssociation(
    name="timelog_Notification_System",
    ends={
        Property(name="notification_System22", type=Notification_System, multiplicity=Multiplicity(0, 1)),
        Property(name="timelog23", type=timelog, multiplicity=Multiplicity(0, 1))
    }
)
fire_alarm_system_fire_alarm_system: BinaryAssociation = BinaryAssociation(
    name="fire_alarm_system_fire_alarm_system",
    ends={
        Property(name="fire_alarm_system24", type=fire_alarm_system, multiplicity=Multiplicity(0, 1)),
        Property(name="fire_alarm_system25", type=fire_alarm_system, multiplicity=Multiplicity(0, 1))
    }
)
fire_alarm_system_control_panel: BinaryAssociation = BinaryAssociation(
    name="fire_alarm_system_control_panel",
    ends={
        Property(name="control_panel26", type=control_panel, multiplicity=Multiplicity(0, 1)),
        Property(name="fire_alarm_system27", type=fire_alarm_system, multiplicity=Multiplicity(0, 9999))
    }
)
flood_alarm_system_control_panel: BinaryAssociation = BinaryAssociation(
    name="flood_alarm_system_control_panel",
    ends={
        Property(name="control_panel28", type=control_panel, multiplicity=Multiplicity(0, 1)),
        Property(name="flood_alarm_system29", type=flood_alarm_system, multiplicity=Multiplicity(0, 9999))
    }
)
door_alarm_system_control_panel: BinaryAssociation = BinaryAssociation(
    name="door_alarm_system_control_panel",
    ends={
        Property(name="control_panel30", type=control_panel, multiplicity=Multiplicity(0, 1)),
        Property(name="door_alarm_system31", type=door_alarm_system, multiplicity=Multiplicity(0, 9999))
    }
)
camera_records_control_panel: BinaryAssociation = BinaryAssociation(
    name="camera_records_control_panel",
    ends={
        Property(name="control_panel32", type=control_panel, multiplicity=Multiplicity(0, 1)),
        Property(name="camera_records33", type=camera_records, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_4687f839_8bbd_44c7_a0ab_cd56e8cf35c2",
    types={smoke_sensor, camera_records, InterfaceO_Interface, temp_sensor, control_panel, door_sensor, flood_sensor, Notification_System, owner_details, login, eventlog, timelog, fire_alarm_system, flood_alarm_system, ClassJ, door_alarm_system},
    associations={owner_details_login, assoc__U4MOxJiYEeqEM7mFKilpXw, fire_alarm_system_smoke_sensor, fire_alarm_system_temp_sensor, flood_alarm_system_flood_sensor, door_alarm_system_door_sensor, eventlog_fire_alarm_system, eventlog_flood_alarm_system, door_alarm_system_eventlog, Notification_System_control_panel, eventlog_timelog, timelog_Notification_System, fire_alarm_system_fire_alarm_system, fire_alarm_system_control_panel, flood_alarm_system_control_panel, door_alarm_system_control_panel, camera_records_control_panel},
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