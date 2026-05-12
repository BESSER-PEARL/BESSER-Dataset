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
Mode: Enumeration = Enumeration(
    name="Mode",
    literals={
            EnumerationLiteral(name="Initialization"),
			EnumerationLiteral(name="Rescue"),
			EnumerationLiteral(name="EmergencyStop"),
			EnumerationLiteral(name="Normal"),
			EnumerationLiteral(name="Dameged"),
			EnumerationLiteral(name="Degraded")
    }
)

ValveState: Enumeration = Enumeration(
    name="ValveState",
    literals={
            EnumerationLiteral(name="Open"),
			EnumerationLiteral(name="Closed")
    }
)

State: Enumeration = Enumeration(
    name="State",
    literals={
            EnumerationLiteral(name="On"),
			EnumerationLiteral(name="Off")
    }
)

# Classes
SBCS_SteamBoiler_OpenValve = Class(name="SBCS_SteamBoiler_OpenValve")
Transition = Class(name="Transition")
SBCS_SteamBoiler = Class(name="SBCS_SteamBoiler")
SBCS_PumpController_OpenPump = Class(name="SBCS_PumpController_OpenPump")
SBCS_PumpControler = Class(name="SBCS_PumpControler")
SBCS_Snapshot = Class(name="SBCS_Snapshot")
SBCS_ControlProgram = Class(name="SBCS_ControlProgram")
SBCS_Pump = Class(name="SBCS_Pump")
SBCS_WaterLevelMeaurementDevice_getLevel = Class(name="SBCS_WaterLevelMeaurementDevice_getLevel")
SBCS_Transition = Class(name="SBCS_Transition")
SBCS_ControlProgram_Start = Class(name="SBCS_ControlProgram_Start")
SBCS_WaterLevelMeasurementDevice = Class(name="SBCS_WaterLevelMeasurementDevice")
SBCS_PumpController_ClosePump = Class(name="SBCS_PumpController_ClosePump")

# SBCS_SteamBoiler_OpenValve class attributes and methods

# Transition class attributes and methods

# SBCS_SteamBoiler class attributes and methods
SBCS_SteamBoiler_capacity: Property = Property(name="capacity", type=FloatType)
SBCS_SteamBoiler_maximalNormal: Property = Property(name="maximalNormal", type=FloatType)
SBCS_SteamBoiler_valveOpen: Property = Property(name="valveOpen", type=StringType)
SBCS_SteamBoiler.attributes={SBCS_SteamBoiler_capacity, SBCS_SteamBoiler_maximalNormal, SBCS_SteamBoiler_valveOpen}

# SBCS_PumpController_OpenPump class attributes and methods

# SBCS_PumpControler class attributes and methods

# SBCS_Snapshot class attributes and methods
SBCS_Snapshot_m_getNext: Method = Method(name="getNext", parameters={}, type=StringType)
SBCS_Snapshot_m_futureClosure: Method = Method(name="futureClosure", parameters={Parameter(name='SBCS_s', type=StringType)}, type=StringType)
SBCS_Snapshot_m_getPost: Method = Method(name="getPost", parameters={}, type=StringType)
SBCS_Snapshot.methods={SBCS_Snapshot_m_getNext, SBCS_Snapshot_m_futureClosure, SBCS_Snapshot_m_getPost}

# SBCS_ControlProgram class attributes and methods
SBCS_ControlProgram_mode: Property = Property(name="mode", type=StringType)
SBCS_ControlProgram.attributes={SBCS_ControlProgram_mode}

# SBCS_Pump class attributes and methods
SBCS_Pump_mode: Property = Property(name="mode", type=StringType)
SBCS_Pump.attributes={SBCS_Pump_mode}

# SBCS_WaterLevelMeaurementDevice_getLevel class attributes and methods
SBCS_WaterLevelMeaurementDevice_getLevel_ret: Property = Property(name="ret", type=FloatType)
SBCS_WaterLevelMeaurementDevice_getLevel.attributes={SBCS_WaterLevelMeaurementDevice_getLevel_ret}

# SBCS_Transition class attributes and methods

# SBCS_ControlProgram_Start class attributes and methods

# SBCS_WaterLevelMeasurementDevice class attributes and methods
SBCS_WaterLevelMeasurementDevice_waterLevel: Property = Property(name="waterLevel", type=FloatType)
SBCS_WaterLevelMeasurementDevice.attributes={SBCS_WaterLevelMeasurementDevice_waterLevel}

# SBCS_PumpController_ClosePump class attributes and methods

# Relationships
PCPre4: BinaryAssociation = BinaryAssociation(
    name="PCPre4",
    ends={
        Property(name="SBCS_PumpControler", type=SBCS_PumpController_OpenPump, multiplicity=Multiplicity(1, 1)),
        Property(name="SBCS_PumpController_OpenPump", type=SBCS_PumpControler, multiplicity=Multiplicity(0, 1))
    }
)
PCPost5: BinaryAssociation = BinaryAssociation(
    name="PCPost5",
    ends={
        Property(name="SBCS_PumpControler7", type=SBCS_PumpController_OpenPump, multiplicity=Multiplicity(1, 1)),
        Property(name="SBCS_PumpController_OpenPump6", type=SBCS_PumpControler, multiplicity=Multiplicity(0, 1))
    }
)
SnapshotSteamBoiler8: BinaryAssociation = BinaryAssociation(
    name="SnapshotSteamBoiler8",
    ends={
        Property(name="SBCS_Snapshot", type=SBCS_SteamBoiler, multiplicity=Multiplicity(1, 1)),
        Property(name="SBCS_SteamBoiler9", type=SBCS_Snapshot, multiplicity=Multiplicity(1, 1))
    }
)
SteamBoilerControlProgram10: BinaryAssociation = BinaryAssociation(
    name="SteamBoilerControlProgram10",
    ends={
        Property(name="SBCS_ControlProgram", type=SBCS_SteamBoiler, multiplicity=Multiplicity(1, 1)),
        Property(name="SBCS_SteamBoiler11", type=SBCS_ControlProgram, multiplicity=Multiplicity(1, 1))
    }
)
PumpControlerPump12: BinaryAssociation = BinaryAssociation(
    name="PumpControlerPump12",
    ends={
        Property(name="SBCS_Pump", type=SBCS_PumpControler, multiplicity=Multiplicity(1, 1)),
        Property(name="SBCS_PumpControler13", type=SBCS_Pump, multiplicity=Multiplicity(1, 1))
    }
)
SBPre0: BinaryAssociation = BinaryAssociation(
    name="SBPre0",
    ends={
        Property(name="SBCS_SteamBoiler", type=SBCS_SteamBoiler_OpenValve, multiplicity=Multiplicity(1, 1)),
        Property(name="SBCS_SteamBoiler_OpenValve", type=SBCS_SteamBoiler, multiplicity=Multiplicity(0, 1))
    }
)
SBPost1: BinaryAssociation = BinaryAssociation(
    name="SBPost1",
    ends={
        Property(name="SBCS_SteamBoiler3", type=SBCS_SteamBoiler_OpenValve, multiplicity=Multiplicity(1, 1)),
        Property(name="SBCS_SteamBoiler_OpenValve2", type=SBCS_SteamBoiler, multiplicity=Multiplicity(0, 1))
    }
)
wlmdPost14: BinaryAssociation = BinaryAssociation(
    name="wlmdPost14",
    ends={
        Property(name="SBCS_WaterLevelMeasurementDevice", type=SBCS_WaterLevelMeaurementDevice_getLevel, multiplicity=Multiplicity(1, 1)),
        Property(name="SBCS_WaterLevelMeaurementDevice_getLevel", type=SBCS_WaterLevelMeasurementDevice, multiplicity=Multiplicity(0, 1))
    }
)
WLMDSnapshot15: BinaryAssociation = BinaryAssociation(
    name="WLMDSnapshot15",
    ends={
        Property(name="SBCS_WaterLevelMeasurementDevice17", type=SBCS_Snapshot, multiplicity=Multiplicity(1, 1)),
        Property(name="SBCS_Snapshot16", type=SBCS_WaterLevelMeasurementDevice, multiplicity=Multiplicity(1, 1))
    }
)
AfterTrans18: BinaryAssociation = BinaryAssociation(
    name="AfterTrans18",
    ends={
        Property(name="SBCS_Transition", type=SBCS_Snapshot, multiplicity=Multiplicity(1, 1)),
        Property(name="SBCS_Snapshot19", type=SBCS_Transition, multiplicity=Multiplicity(1, 1))
    }
)
WLMDSteamBoiler20: BinaryAssociation = BinaryAssociation(
    name="WLMDSteamBoiler20",
    ends={
        Property(name="SBCS_SteamBoiler22", type=SBCS_WaterLevelMeasurementDevice, multiplicity=Multiplicity(1, 1)),
        Property(name="SBCS_WaterLevelMeasurementDevice21", type=SBCS_SteamBoiler, multiplicity=Multiplicity(1, 1))
    }
)
AfterTrans25: BinaryAssociation = BinaryAssociation(
    name="AfterTrans25",
    ends={
        Property(name="SBCS_Snapshot27", type=SBCS_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="SBCS_Transition26", type=SBCS_Snapshot, multiplicity=Multiplicity(1, 1))
    }
)
PCPre28: BinaryAssociation = BinaryAssociation(
    name="PCPre28",
    ends={
        Property(name="SBCS_PumpControler29", type=SBCS_PumpController_ClosePump, multiplicity=Multiplicity(1, 1)),
        Property(name="SBCS_PumpController_ClosePump", type=SBCS_PumpControler, multiplicity=Multiplicity(0, 1))
    }
)
PCPost30: BinaryAssociation = BinaryAssociation(
    name="PCPost30",
    ends={
        Property(name="SBCS_PumpControler32", type=SBCS_PumpController_ClosePump, multiplicity=Multiplicity(1, 1)),
        Property(name="SBCS_PumpController_ClosePump31", type=SBCS_PumpControler, multiplicity=Multiplicity(0, 1))
    }
)
CPPost23: BinaryAssociation = BinaryAssociation(
    name="CPPost23",
    ends={
        Property(name="SBCS_ControlProgram24", type=SBCS_ControlProgram_Start, multiplicity=Multiplicity(1, 1)),
        Property(name="SBCS_ControlProgram_Start", type=SBCS_ControlProgram, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_SBCS_SteamBoiler_OpenValve_Transition = Generalization(general=Transition, specific=SBCS_SteamBoiler_OpenValve)
gen_SBCS_PumpController_OpenPump_Transition = Generalization(general=Transition, specific=SBCS_PumpController_OpenPump)
gen_SBCS_WaterLevelMeaurementDevice_getLevel_Transition = Generalization(general=Transition, specific=SBCS_WaterLevelMeaurementDevice_getLevel)
gen_SBCS_ControlProgram_Start_Transition = Generalization(general=Transition, specific=SBCS_ControlProgram_Start)
gen_SBCS_PumpController_ClosePump_Transition = Generalization(general=Transition, specific=SBCS_PumpController_ClosePump)


# OCL Constraints
ClosePump: Constraint = Constraint(
    name="ClosePump",
    context=SBCS_PumpController_ClosePump,
    expression="context PumpController_ClosePump inv: PCPre.PumpControlerPump.mode = State_On implies PCPost.PumpControlerPump.mode = State_Off",
    language="OCL"
)
OpenValve: Constraint = Constraint(
    name="OpenValve",
    context=SBCS_SteamBoiler_OpenValve,
    expression="context SteamBoiler_OpenValve inv: SBPre.valveOpen = ValveState_Closed implies SBPost.valveOpen = ValveState_Open",
    language="OCL"
)
TP4: Constraint = Constraint(
    name="TP4",
    context=SBCS_SteamBoiler_OpenValve,
    expression="context SteamBoiler inv: let CS:Snapshot = self.SnapshotSteamBoiler in let FS: Set(Snapshot)= CS.getPost()in self.valveOpen = ValveState_Open implies FS->exists(s:Snapshot | s.WLMDSnapshot.waterLevel <= maximalNormal)",
    language="OCL"
)
WMD: Constraint = Constraint(
    name="WMD",
    context=SBCS_WaterLevelMeasurementDevice,
    expression="context WaterLevelMeasurementDevice inv: self.waterLevel < self.WLMDSteamBoiler.capacity",
    language="OCL"
)
Start: Constraint = Constraint(
    name="Start",
    context=SBCS_ControlProgram_Start,
    expression="context ControlProgram_Start inv: CPPost.mode = Mode_Normal",
    language="OCL"
)
getLevel: Constraint = Constraint(
    name="getLevel",
    context=SBCS_WaterLevelMeaurementDevice_getLevel,
    expression="context WaterLevelMeaurementDevice_getLevel inv: wlmdPost.waterLevel = ret",
    language="OCL"
)
SB: Constraint = Constraint(
    name="SB",
    context=SBCS_SteamBoiler_OpenValve,
    expression="context SteamBoiler inv: self.valveOpen=ValveState_Open implies self.SteamBoilerControlProgram.mode=Mode_Initialization",
    language="OCL"
)
OpenPump: Constraint = Constraint(
    name="OpenPump",
    context=SBCS_PumpController_OpenPump,
    expression="context PumpController_OpenPump inv: PCPre.PumpControlerPump.mode = State_Off implies PCPost.PumpControlerPump.mode = State_On",
    language="OCL"
)

# Domain Model
domain_model = DomainModel(
    name="SBCS",
    types={SBCS_SteamBoiler_OpenValve, Transition, SBCS_SteamBoiler, SBCS_PumpController_OpenPump, SBCS_PumpControler, SBCS_Snapshot, SBCS_ControlProgram, SBCS_Pump, SBCS_WaterLevelMeaurementDevice_getLevel, SBCS_Transition, SBCS_ControlProgram_Start, SBCS_WaterLevelMeasurementDevice, SBCS_PumpController_ClosePump, Mode, ValveState, State},
    associations={PCPre4, PCPost5, SnapshotSteamBoiler8, SteamBoilerControlProgram10, PumpControlerPump12, SBPre0, SBPost1, wlmdPost14, WLMDSnapshot15, AfterTrans18, WLMDSteamBoiler20, AfterTrans25, PCPre28, PCPost30, CPPost23},
    constraints={ClosePump, OpenValve, TP4, WMD, Start, getLevel, SB, OpenPump},
    generalizations={gen_SBCS_SteamBoiler_OpenValve_Transition, gen_SBCS_PumpController_OpenPump_Transition, gen_SBCS_WaterLevelMeaurementDevice_getLevel_Transition, gen_SBCS_ControlProgram_Start_Transition, gen_SBCS_PumpController_ClosePump_Transition},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)