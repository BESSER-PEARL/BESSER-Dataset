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

State: Enumeration = Enumeration(
    name="State",
    literals={
            EnumerationLiteral(name="On"),
			EnumerationLiteral(name="Off")
    }
)

ValveState: Enumeration = Enumeration(
    name="ValveState",
    literals={
            EnumerationLiteral(name="Open"),
			EnumerationLiteral(name="Closed")
    }
)

# Classes
SBCS_Transition = Class(name="SBCS_Transition")
SBCS_Snapshot = Class(name="SBCS_Snapshot")
SBCS_PumpController_ClosePump = Class(name="SBCS_PumpController_ClosePump")
Transition = Class(name="Transition")
SBCS_PumpControler = Class(name="SBCS_PumpControler")
SBCS_WaterLevelMeasurementDevice = Class(name="SBCS_WaterLevelMeasurementDevice")
SBCS_WaterLevelMeaurementDevice_getLevel = Class(name="SBCS_WaterLevelMeaurementDevice_getLevel")
SBCS_ControlProgram_Start = Class(name="SBCS_ControlProgram_Start")
SBCS_ControlProgram = Class(name="SBCS_ControlProgram")
SBCS_SteamBoiler = Class(name="SBCS_SteamBoiler")
SBCS_SteamBoiler_OpenValve = Class(name="SBCS_SteamBoiler_OpenValve")
SBCS_PumpController_OpenPump = Class(name="SBCS_PumpController_OpenPump")
SBCS_Pump = Class(name="SBCS_Pump")

# SBCS_Transition class attributes and methods

# SBCS_Snapshot class attributes and methods
SBCS_Snapshot_m_getNext: Method = Method(name="getNext", parameters={}, type=StringType)
SBCS_Snapshot.methods={SBCS_Snapshot_m_getNext}

# SBCS_PumpController_ClosePump class attributes and methods

# Transition class attributes and methods

# SBCS_PumpControler class attributes and methods

# SBCS_WaterLevelMeasurementDevice class attributes and methods
SBCS_WaterLevelMeasurementDevice_waterLevel: Property = Property(name="waterLevel", type=FloatType)
SBCS_WaterLevelMeasurementDevice.attributes={SBCS_WaterLevelMeasurementDevice_waterLevel}

# SBCS_WaterLevelMeaurementDevice_getLevel class attributes and methods
SBCS_WaterLevelMeaurementDevice_getLevel_ret: Property = Property(name="ret", type=FloatType)
SBCS_WaterLevelMeaurementDevice_getLevel.attributes={SBCS_WaterLevelMeaurementDevice_getLevel_ret}

# SBCS_ControlProgram_Start class attributes and methods

# SBCS_ControlProgram class attributes and methods
SBCS_ControlProgram_mode: Property = Property(name="mode", type=StringType)
SBCS_ControlProgram_wlmdFailure: Property = Property(name="wlmdFailure", type=BooleanType)
SBCS_ControlProgram.attributes={SBCS_ControlProgram_wlmdFailure, SBCS_ControlProgram_mode}

# SBCS_SteamBoiler class attributes and methods
SBCS_SteamBoiler_valveOpen: Property = Property(name="valveOpen", type=StringType)
SBCS_SteamBoiler.attributes={SBCS_SteamBoiler_valveOpen}

# SBCS_SteamBoiler_OpenValve class attributes and methods

# SBCS_PumpController_OpenPump class attributes and methods

# SBCS_Pump class attributes and methods
SBCS_Pump_mode: Property = Property(name="mode", type=StringType)
SBCS_Pump.attributes={SBCS_Pump_mode}

# Relationships
AfterTrans0: BinaryAssociation = BinaryAssociation(
    name="AfterTrans0",
    ends={
        Property(name="SBCS_Snapshot", type=SBCS_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="SBCS_Transition", type=SBCS_Snapshot, multiplicity=Multiplicity(1, 1))
    }
)
PCPre1: BinaryAssociation = BinaryAssociation(
    name="PCPre1",
    ends={
        Property(name="SBCS_PumpControler", type=SBCS_PumpController_ClosePump, multiplicity=Multiplicity(1, 1)),
        Property(name="SBCS_PumpController_ClosePump", type=SBCS_PumpControler, multiplicity=Multiplicity(0, 1))
    }
)
PCPost2: BinaryAssociation = BinaryAssociation(
    name="PCPost2",
    ends={
        Property(name="SBCS_PumpControler4", type=SBCS_PumpController_ClosePump, multiplicity=Multiplicity(1, 1)),
        Property(name="SBCS_PumpController_ClosePump3", type=SBCS_PumpControler, multiplicity=Multiplicity(0, 1))
    }
)
wlmdPost5: BinaryAssociation = BinaryAssociation(
    name="wlmdPost5",
    ends={
        Property(name="SBCS_WaterLevelMeasurementDevice", type=SBCS_WaterLevelMeaurementDevice_getLevel, multiplicity=Multiplicity(1, 1)),
        Property(name="SBCS_WaterLevelMeaurementDevice_getLevel", type=SBCS_WaterLevelMeasurementDevice, multiplicity=Multiplicity(0, 1))
    }
)
CPPost6: BinaryAssociation = BinaryAssociation(
    name="CPPost6",
    ends={
        Property(name="SBCS_ControlProgram", type=SBCS_ControlProgram_Start, multiplicity=Multiplicity(1, 1)),
        Property(name="SBCS_ControlProgram_Start", type=SBCS_ControlProgram, multiplicity=Multiplicity(0, 1))
    }
)
SteamBoilerControlProgram7: BinaryAssociation = BinaryAssociation(
    name="SteamBoilerControlProgram7",
    ends={
        Property(name="SBCS_ControlProgram8", type=SBCS_SteamBoiler, multiplicity=Multiplicity(1, 1)),
        Property(name="SBCS_SteamBoiler", type=SBCS_ControlProgram, multiplicity=Multiplicity(1, 1))
    }
)
ControlProgramSnapshot9: BinaryAssociation = BinaryAssociation(
    name="ControlProgramSnapshot9",
    ends={
        Property(name="SBCS_ControlProgram11", type=SBCS_Snapshot, multiplicity=Multiplicity(1, 1)),
        Property(name="SBCS_Snapshot10", type=SBCS_ControlProgram, multiplicity=Multiplicity(1, 1))
    }
)
AfterTrans12: BinaryAssociation = BinaryAssociation(
    name="AfterTrans12",
    ends={
        Property(name="SBCS_Transition14", type=SBCS_Snapshot, multiplicity=Multiplicity(1, 1)),
        Property(name="SBCS_Snapshot13", type=SBCS_Transition, multiplicity=Multiplicity(1, 1))
    }
)
SBPre15: BinaryAssociation = BinaryAssociation(
    name="SBPre15",
    ends={
        Property(name="SBCS_SteamBoiler16", type=SBCS_SteamBoiler_OpenValve, multiplicity=Multiplicity(1, 1)),
        Property(name="SBCS_SteamBoiler_OpenValve", type=SBCS_SteamBoiler, multiplicity=Multiplicity(0, 1))
    }
)
PCPre20: BinaryAssociation = BinaryAssociation(
    name="PCPre20",
    ends={
        Property(name="SBCS_PumpControler21", type=SBCS_PumpController_OpenPump, multiplicity=Multiplicity(1, 1)),
        Property(name="SBCS_PumpController_OpenPump", type=SBCS_PumpControler, multiplicity=Multiplicity(0, 1))
    }
)
PCPost22: BinaryAssociation = BinaryAssociation(
    name="PCPost22",
    ends={
        Property(name="SBCS_PumpControler24", type=SBCS_PumpController_OpenPump, multiplicity=Multiplicity(1, 1)),
        Property(name="SBCS_PumpController_OpenPump23", type=SBCS_PumpControler, multiplicity=Multiplicity(0, 1))
    }
)
SnapshotControlProgram25: BinaryAssociation = BinaryAssociation(
    name="SnapshotControlProgram25",
    ends={
        Property(name="SBCS_Snapshot27", type=SBCS_ControlProgram, multiplicity=Multiplicity(1, 1)),
        Property(name="SBCS_ControlProgram26", type=SBCS_Snapshot, multiplicity=Multiplicity(1, 1))
    }
)
PumpControlerPump28: BinaryAssociation = BinaryAssociation(
    name="PumpControlerPump28",
    ends={
        Property(name="SBCS_Pump", type=SBCS_PumpControler, multiplicity=Multiplicity(1, 1)),
        Property(name="SBCS_PumpControler29", type=SBCS_Pump, multiplicity=Multiplicity(1, 1))
    }
)
SBPost17: BinaryAssociation = BinaryAssociation(
    name="SBPost17",
    ends={
        Property(name="SBCS_SteamBoiler19", type=SBCS_SteamBoiler_OpenValve, multiplicity=Multiplicity(1, 1)),
        Property(name="SBCS_SteamBoiler_OpenValve18", type=SBCS_SteamBoiler, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_SBCS_PumpController_ClosePump_Transition = Generalization(general=Transition, specific=SBCS_PumpController_ClosePump)
gen_SBCS_ControlProgram_Start_Transition = Generalization(general=Transition, specific=SBCS_ControlProgram_Start)
gen_SBCS_SteamBoiler_OpenValve_Transition = Generalization(general=Transition, specific=SBCS_SteamBoiler_OpenValve)
gen_SBCS_WaterLevelMeaurementDevice_getLevel_Transition = Generalization(general=Transition, specific=SBCS_WaterLevelMeaurementDevice_getLevel)
gen_SBCS_PumpController_OpenPump_Transition = Generalization(general=Transition, specific=SBCS_PumpController_OpenPump)


# OCL Constraints
ClosePump: Constraint = Constraint(
    name="ClosePump",
    context=SBCS_PumpController_ClosePump,
    expression="context PumpController_ClosePump inv: PCPre.PumpControlerPump.mode = State_On implies PCPost.PumpControlerPump.mode = State_Off",
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
TP5: Constraint = Constraint(
    name="TP5",
    context=SBCS_ControlProgram_Start,
    expression="context ControlProgram inv: let CS:Snapshot = self.SnapshotControlProgram in let NS: Snapshot= CS.getNext()in (self.mode=Mode_Initialization and self.wlmdFailure) implies NS.ControlProgramSnapshot.mode=Mode_EmergencyStop",
    language="OCL"
)
OpenValve: Constraint = Constraint(
    name="OpenValve",
    context=SBCS_SteamBoiler_OpenValve,
    expression="context SteamBoiler_OpenValve inv: SBPre.valveOpen = ValveState_Closed implies SBPost.valveOpen = ValveState_Open",
    language="OCL"
)
Start: Constraint = Constraint(
    name="Start",
    context=SBCS_ControlProgram_Start,
    expression="context ControlProgram_Start inv: CPPost.mode = Mode_Normal",
    language="OCL"
)

# Domain Model
domain_model = DomainModel(
    name="SBCS",
    types={SBCS_Transition, SBCS_Snapshot, SBCS_PumpController_ClosePump, Transition, SBCS_PumpControler, SBCS_WaterLevelMeasurementDevice, SBCS_WaterLevelMeaurementDevice_getLevel, SBCS_ControlProgram_Start, SBCS_ControlProgram, SBCS_SteamBoiler, SBCS_SteamBoiler_OpenValve, SBCS_PumpController_OpenPump, SBCS_Pump, Mode, State, ValveState},
    associations={AfterTrans0, PCPre1, PCPost2, wlmdPost5, CPPost6, SteamBoilerControlProgram7, ControlProgramSnapshot9, AfterTrans12, SBPre15, PCPre20, PCPost22, SnapshotControlProgram25, PumpControlerPump28, SBPost17},
    constraints={ClosePump, getLevel, SB, OpenPump, TP5, OpenValve, Start},
    generalizations={gen_SBCS_PumpController_ClosePump_Transition, gen_SBCS_ControlProgram_Start_Transition, gen_SBCS_SteamBoiler_OpenValve_Transition, gen_SBCS_WaterLevelMeaurementDevice_getLevel_Transition, gen_SBCS_PumpController_OpenPump_Transition},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)