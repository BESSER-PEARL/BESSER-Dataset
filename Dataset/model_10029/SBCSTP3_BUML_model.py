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
SBCS_Snapshot = Class(name="SBCS_Snapshot")
SBCS_WaterLevelMeasurementDevice = Class(name="SBCS_WaterLevelMeasurementDevice")
SBCS_PumpControler = Class(name="SBCS_PumpControler")
SBCS_Pump = Class(name="SBCS_Pump")
SBCS_ControlProgram_Start = Class(name="SBCS_ControlProgram_Start")
Transition = Class(name="Transition")
SBCS_ControlProgram = Class(name="SBCS_ControlProgram")
SBCS_SteamBoiler = Class(name="SBCS_SteamBoiler")
SBCS_Transition = Class(name="SBCS_Transition")
SBCS_WaterLevelMeaurementDevice_getLevel = Class(name="SBCS_WaterLevelMeaurementDevice_getLevel")
SBCS_PumpController_ClosePump = Class(name="SBCS_PumpController_ClosePump")
SBCS_SteamBoiler_OpenValve = Class(name="SBCS_SteamBoiler_OpenValve")
SBCS_PumpController_OpenPump = Class(name="SBCS_PumpController_OpenPump")

# SBCS_Snapshot class attributes and methods
SBCS_Snapshot_m_getNext: Method = Method(name="getNext", parameters={}, type=StringType)
SBCS_Snapshot.methods={SBCS_Snapshot_m_getNext}

# SBCS_WaterLevelMeasurementDevice class attributes and methods
SBCS_WaterLevelMeasurementDevice_waterLevel: Property = Property(name="waterLevel", type=FloatType)
SBCS_WaterLevelMeasurementDevice.attributes={SBCS_WaterLevelMeasurementDevice_waterLevel}

# SBCS_PumpControler class attributes and methods

# SBCS_Pump class attributes and methods
SBCS_Pump_mode: Property = Property(name="mode", type=StringType)
SBCS_Pump.attributes={SBCS_Pump_mode}

# SBCS_ControlProgram_Start class attributes and methods

# Transition class attributes and methods

# SBCS_ControlProgram class attributes and methods
SBCS_ControlProgram_mode: Property = Property(name="mode", type=StringType)
SBCS_ControlProgram.attributes={SBCS_ControlProgram_mode}

# SBCS_SteamBoiler class attributes and methods
SBCS_SteamBoiler_minimalNormal: Property = Property(name="minimalNormal", type=FloatType)
SBCS_SteamBoiler_maximalNormal: Property = Property(name="maximalNormal", type=FloatType)
SBCS_SteamBoiler_valveOpen: Property = Property(name="valveOpen", type=StringType)
SBCS_SteamBoiler_capacity: Property = Property(name="capacity", type=FloatType)
SBCS_SteamBoiler.attributes={SBCS_SteamBoiler_maximalNormal, SBCS_SteamBoiler_minimalNormal, SBCS_SteamBoiler_valveOpen, SBCS_SteamBoiler_capacity}

# SBCS_Transition class attributes and methods

# SBCS_WaterLevelMeaurementDevice_getLevel class attributes and methods
SBCS_WaterLevelMeaurementDevice_getLevel_ret: Property = Property(name="ret", type=FloatType)
SBCS_WaterLevelMeaurementDevice_getLevel.attributes={SBCS_WaterLevelMeaurementDevice_getLevel_ret}

# SBCS_PumpController_ClosePump class attributes and methods

# SBCS_SteamBoiler_OpenValve class attributes and methods

# SBCS_PumpController_OpenPump class attributes and methods

# Relationships
SnapshotSteamBoiler1: BinaryAssociation = BinaryAssociation(
    name="SnapshotSteamBoiler1",
    ends={
        Property(name="SBCS_Snapshot", type=SBCS_SteamBoiler, multiplicity=Multiplicity(1, 1)),
        Property(name="SBCS_SteamBoiler", type=SBCS_Snapshot, multiplicity=Multiplicity(1, 1))
    }
)
SteamBoilerControlProgram2: BinaryAssociation = BinaryAssociation(
    name="SteamBoilerControlProgram2",
    ends={
        Property(name="SBCS_ControlProgram4", type=SBCS_SteamBoiler, multiplicity=Multiplicity(1, 1)),
        Property(name="SBCS_SteamBoiler3", type=SBCS_ControlProgram, multiplicity=Multiplicity(1, 1))
    }
)
SteamBoilerWLMD5: BinaryAssociation = BinaryAssociation(
    name="SteamBoilerWLMD5",
    ends={
        Property(name="SBCS_WaterLevelMeasurementDevice", type=SBCS_SteamBoiler, multiplicity=Multiplicity(1, 1)),
        Property(name="SBCS_SteamBoiler6", type=SBCS_WaterLevelMeasurementDevice, multiplicity=Multiplicity(1, 1))
    }
)
PumpControlerPump7: BinaryAssociation = BinaryAssociation(
    name="PumpControlerPump7",
    ends={
        Property(name="SBCS_Pump", type=SBCS_PumpControler, multiplicity=Multiplicity(1, 1)),
        Property(name="SBCS_PumpControler", type=SBCS_Pump, multiplicity=Multiplicity(1, 1))
    }
)
CPPost0: BinaryAssociation = BinaryAssociation(
    name="CPPost0",
    ends={
        Property(name="SBCS_ControlProgram", type=SBCS_ControlProgram_Start, multiplicity=Multiplicity(1, 1)),
        Property(name="SBCS_ControlProgram_Start", type=SBCS_ControlProgram, multiplicity=Multiplicity(0, 1))
    }
)
SBPost15: BinaryAssociation = BinaryAssociation(
    name="SBPost15",
    ends={
        Property(name="SBCS_SteamBoiler17", type=SBCS_SteamBoiler_OpenValve, multiplicity=Multiplicity(1, 1)),
        Property(name="SBCS_SteamBoiler_OpenValve16", type=SBCS_SteamBoiler, multiplicity=Multiplicity(0, 1))
    }
)
AfterTrans18: BinaryAssociation = BinaryAssociation(
    name="AfterTrans18",
    ends={
        Property(name="SBCS_Snapshot19", type=SBCS_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="SBCS_Transition", type=SBCS_Snapshot, multiplicity=Multiplicity(1, 1))
    }
)
wlmdPost20: BinaryAssociation = BinaryAssociation(
    name="wlmdPost20",
    ends={
        Property(name="SBCS_WaterLevelMeasurementDevice21", type=SBCS_WaterLevelMeaurementDevice_getLevel, multiplicity=Multiplicity(1, 1)),
        Property(name="SBCS_WaterLevelMeaurementDevice_getLevel", type=SBCS_WaterLevelMeasurementDevice, multiplicity=Multiplicity(0, 1))
    }
)
WLMDSteamBoiler22: BinaryAssociation = BinaryAssociation(
    name="WLMDSteamBoiler22",
    ends={
        Property(name="SBCS_SteamBoiler24", type=SBCS_WaterLevelMeasurementDevice, multiplicity=Multiplicity(1, 1)),
        Property(name="SBCS_WaterLevelMeasurementDevice23", type=SBCS_SteamBoiler, multiplicity=Multiplicity(1, 1))
    }
)
PCPre8: BinaryAssociation = BinaryAssociation(
    name="PCPre8",
    ends={
        Property(name="SBCS_PumpControler9", type=SBCS_PumpController_ClosePump, multiplicity=Multiplicity(1, 1)),
        Property(name="SBCS_PumpController_ClosePump", type=SBCS_PumpControler, multiplicity=Multiplicity(0, 1))
    }
)
PCPost10: BinaryAssociation = BinaryAssociation(
    name="PCPost10",
    ends={
        Property(name="SBCS_PumpControler12", type=SBCS_PumpController_ClosePump, multiplicity=Multiplicity(1, 1)),
        Property(name="SBCS_PumpController_ClosePump11", type=SBCS_PumpControler, multiplicity=Multiplicity(0, 1))
    }
)
SBPre13: BinaryAssociation = BinaryAssociation(
    name="SBPre13",
    ends={
        Property(name="SBCS_SteamBoiler14", type=SBCS_SteamBoiler_OpenValve, multiplicity=Multiplicity(1, 1)),
        Property(name="SBCS_SteamBoiler_OpenValve", type=SBCS_SteamBoiler, multiplicity=Multiplicity(0, 1))
    }
)
ControlProgramSnapshot25: BinaryAssociation = BinaryAssociation(
    name="ControlProgramSnapshot25",
    ends={
        Property(name="SBCS_ControlProgram27", type=SBCS_Snapshot, multiplicity=Multiplicity(1, 1)),
        Property(name="SBCS_Snapshot26", type=SBCS_ControlProgram, multiplicity=Multiplicity(1, 1))
    }
)
AfterTrans28: BinaryAssociation = BinaryAssociation(
    name="AfterTrans28",
    ends={
        Property(name="SBCS_Transition30", type=SBCS_Snapshot, multiplicity=Multiplicity(1, 1)),
        Property(name="SBCS_Snapshot29", type=SBCS_Transition, multiplicity=Multiplicity(1, 1))
    }
)
PCPre31: BinaryAssociation = BinaryAssociation(
    name="PCPre31",
    ends={
        Property(name="SBCS_PumpControler32", type=SBCS_PumpController_OpenPump, multiplicity=Multiplicity(1, 1)),
        Property(name="SBCS_PumpController_OpenPump", type=SBCS_PumpControler, multiplicity=Multiplicity(0, 1))
    }
)
PCPost33: BinaryAssociation = BinaryAssociation(
    name="PCPost33",
    ends={
        Property(name="SBCS_PumpControler35", type=SBCS_PumpController_OpenPump, multiplicity=Multiplicity(1, 1)),
        Property(name="SBCS_PumpController_OpenPump34", type=SBCS_PumpControler, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_SBCS_ControlProgram_Start_Transition = Generalization(general=Transition, specific=SBCS_ControlProgram_Start)
gen_SBCS_WaterLevelMeaurementDevice_getLevel_Transition = Generalization(general=Transition, specific=SBCS_WaterLevelMeaurementDevice_getLevel)
gen_SBCS_PumpController_ClosePump_Transition = Generalization(general=Transition, specific=SBCS_PumpController_ClosePump)
gen_SBCS_SteamBoiler_OpenValve_Transition = Generalization(general=Transition, specific=SBCS_SteamBoiler_OpenValve)
gen_SBCS_PumpController_OpenPump_Transition = Generalization(general=Transition, specific=SBCS_PumpController_OpenPump)


# OCL Constraints
ClosePump: Constraint = Constraint(
    name="ClosePump",
    context=SBCS_PumpController_ClosePump,
    expression="context PumpController_ClosePump inv: PCPre.PumpControlerPump.mode = State_On implies PCPost.PumpControlerPump.mode = State_Off",
    language="OCL"
)
TP3: Constraint = Constraint(
    name="TP3",
    context=SBCS_SteamBoiler,
    expression="context SteamBoiler inv: let CS:Snapshot = self.SnapshotSteamBoiler in let NS: Snapshot= CS.getNext()in (self.SteamBoilerWLMD.waterLevel > self.maximalNormal or self.SteamBoilerWLMD.waterLevel < self.minimalNormal)implies NS.ControlProgramSnapshot.mode= Mode_EmergencyStop",
    language="OCL"
)
OpenValve: Constraint = Constraint(
    name="OpenValve",
    context=SBCS_SteamBoiler_OpenValve,
    expression="context SteamBoiler_OpenValve inv: SBPre.valveOpen = ValveState_Closed implies SBPost.valveOpen = ValveState_Open",
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
    context=SBCS_SteamBoiler,
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
    types={SBCS_Snapshot, SBCS_WaterLevelMeasurementDevice, SBCS_PumpControler, SBCS_Pump, SBCS_ControlProgram_Start, Transition, SBCS_ControlProgram, SBCS_SteamBoiler, SBCS_Transition, SBCS_WaterLevelMeaurementDevice_getLevel, SBCS_PumpController_ClosePump, SBCS_SteamBoiler_OpenValve, SBCS_PumpController_OpenPump, Mode, ValveState, State},
    associations={SnapshotSteamBoiler1, SteamBoilerControlProgram2, SteamBoilerWLMD5, PumpControlerPump7, CPPost0, SBPost15, AfterTrans18, wlmdPost20, WLMDSteamBoiler22, PCPre8, PCPost10, SBPre13, ControlProgramSnapshot25, AfterTrans28, PCPre31, PCPost33},
    constraints={ClosePump, TP3, OpenValve, WMD, Start, getLevel, SB, OpenPump},
    generalizations={gen_SBCS_ControlProgram_Start_Transition, gen_SBCS_WaterLevelMeaurementDevice_getLevel_Transition, gen_SBCS_PumpController_ClosePump_Transition, gen_SBCS_SteamBoiler_OpenValve_Transition, gen_SBCS_PumpController_OpenPump_Transition},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)