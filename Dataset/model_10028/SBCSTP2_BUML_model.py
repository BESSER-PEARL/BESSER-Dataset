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
State: Enumeration = Enumeration(
    name="State",
    literals={
            EnumerationLiteral(name="On"),
			EnumerationLiteral(name="Off")
    }
)

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

# Classes
SBCS_WaterLevelMeasurementDevice = Class(name="SBCS_WaterLevelMeasurementDevice")
SBCS_Pump = Class(name="SBCS_Pump")
SBCS_PumpController_OpenPump = Class(name="SBCS_PumpController_OpenPump")
Transition = Class(name="Transition")
SBCS_PumpControler = Class(name="SBCS_PumpControler")
SBCS_Snapshot = Class(name="SBCS_Snapshot")
SBCS_SteamBoiler_OpenValve = Class(name="SBCS_SteamBoiler_OpenValve")
SBCS_ControlProgram = Class(name="SBCS_ControlProgram")
SBCS_Transition = Class(name="SBCS_Transition")
SBCS_PumpController_ClosePump = Class(name="SBCS_PumpController_ClosePump")
SBCS_SteamBoiler = Class(name="SBCS_SteamBoiler")
SBCS_ControlProgram_Start = Class(name="SBCS_ControlProgram_Start")
SBCS_WaterLevelMeaurementDevice_getLevel = Class(name="SBCS_WaterLevelMeaurementDevice_getLevel")

# SBCS_WaterLevelMeasurementDevice class attributes and methods
SBCS_WaterLevelMeasurementDevice_waterLevel: Property = Property(name="waterLevel", type=FloatType)
SBCS_WaterLevelMeasurementDevice.attributes={SBCS_WaterLevelMeasurementDevice_waterLevel}

# SBCS_Pump class attributes and methods
SBCS_Pump_mode: Property = Property(name="mode", type=StringType)
SBCS_Pump.attributes={SBCS_Pump_mode}

# SBCS_PumpController_OpenPump class attributes and methods

# Transition class attributes and methods

# SBCS_PumpControler class attributes and methods

# SBCS_Snapshot class attributes and methods
SBCS_Snapshot_m_getNext: Method = Method(name="getNext", parameters={}, type=StringType)
SBCS_Snapshot.methods={SBCS_Snapshot_m_getNext}

# SBCS_SteamBoiler_OpenValve class attributes and methods

# SBCS_ControlProgram class attributes and methods
SBCS_ControlProgram_mode: Property = Property(name="mode", type=StringType)
SBCS_ControlProgram_smdFailure: Property = Property(name="smdFailure", type=BooleanType)
SBCS_ControlProgram_pumpFailure: Property = Property(name="pumpFailure", type=BooleanType)
SBCS_ControlProgram_pumpControlerFailure: Property = Property(name="pumpControlerFailure", type=BooleanType)
SBCS_ControlProgram.attributes={SBCS_ControlProgram_pumpFailure, SBCS_ControlProgram_smdFailure, SBCS_ControlProgram_mode, SBCS_ControlProgram_pumpControlerFailure}

# SBCS_Transition class attributes and methods

# SBCS_PumpController_ClosePump class attributes and methods

# SBCS_SteamBoiler class attributes and methods
SBCS_SteamBoiler_valveOpen: Property = Property(name="valveOpen", type=StringType)
SBCS_SteamBoiler.attributes={SBCS_SteamBoiler_valveOpen}

# SBCS_ControlProgram_Start class attributes and methods

# SBCS_WaterLevelMeaurementDevice_getLevel class attributes and methods
SBCS_WaterLevelMeaurementDevice_getLevel_ret: Property = Property(name="ret", type=FloatType)
SBCS_WaterLevelMeaurementDevice_getLevel.attributes={SBCS_WaterLevelMeaurementDevice_getLevel_ret}

# Relationships
PCPost1: BinaryAssociation = BinaryAssociation(
    name="PCPost1",
    ends={
        Property(name="SBCS_PumpControler3", type=SBCS_PumpController_OpenPump, multiplicity=Multiplicity(1, 1)),
        Property(name="SBCS_PumpController_OpenPump2", type=SBCS_PumpControler, multiplicity=Multiplicity(0, 1))
    }
)
PCPre0: BinaryAssociation = BinaryAssociation(
    name="PCPre0",
    ends={
        Property(name="SBCS_PumpControler", type=SBCS_PumpController_OpenPump, multiplicity=Multiplicity(1, 1)),
        Property(name="SBCS_PumpController_OpenPump", type=SBCS_PumpControler, multiplicity=Multiplicity(0, 1))
    }
)
SBPre18: BinaryAssociation = BinaryAssociation(
    name="SBPre18",
    ends={
        Property(name="SBCS_SteamBoiler19", type=SBCS_SteamBoiler_OpenValve, multiplicity=Multiplicity(1, 1)),
        Property(name="SBCS_SteamBoiler_OpenValve", type=SBCS_SteamBoiler, multiplicity=Multiplicity(0, 1))
    }
)
SBPost20: BinaryAssociation = BinaryAssociation(
    name="SBPost20",
    ends={
        Property(name="SBCS_SteamBoiler22", type=SBCS_SteamBoiler_OpenValve, multiplicity=Multiplicity(1, 1)),
        Property(name="SBCS_SteamBoiler_OpenValve21", type=SBCS_SteamBoiler, multiplicity=Multiplicity(0, 1))
    }
)
ControlProgramSnapshot4: BinaryAssociation = BinaryAssociation(
    name="ControlProgramSnapshot4",
    ends={
        Property(name="SBCS_ControlProgram", type=SBCS_Snapshot, multiplicity=Multiplicity(1, 1)),
        Property(name="SBCS_Snapshot", type=SBCS_ControlProgram, multiplicity=Multiplicity(1, 1))
    }
)
AfterTrans5: BinaryAssociation = BinaryAssociation(
    name="AfterTrans5",
    ends={
        Property(name="SBCS_Transition", type=SBCS_Snapshot, multiplicity=Multiplicity(1, 1)),
        Property(name="SBCS_Snapshot6", type=SBCS_Transition, multiplicity=Multiplicity(1, 1))
    }
)
PCPre7: BinaryAssociation = BinaryAssociation(
    name="PCPre7",
    ends={
        Property(name="SBCS_PumpControler8", type=SBCS_PumpController_ClosePump, multiplicity=Multiplicity(1, 1)),
        Property(name="SBCS_PumpController_ClosePump", type=SBCS_PumpControler, multiplicity=Multiplicity(0, 1))
    }
)
PCPost9: BinaryAssociation = BinaryAssociation(
    name="PCPost9",
    ends={
        Property(name="SBCS_PumpControler11", type=SBCS_PumpController_ClosePump, multiplicity=Multiplicity(1, 1)),
        Property(name="SBCS_PumpController_ClosePump10", type=SBCS_PumpControler, multiplicity=Multiplicity(0, 1))
    }
)
PumpControlerPump12: BinaryAssociation = BinaryAssociation(
    name="PumpControlerPump12",
    ends={
        Property(name="SBCS_Pump", type=SBCS_PumpControler, multiplicity=Multiplicity(1, 1)),
        Property(name="SBCS_PumpControler13", type=SBCS_Pump, multiplicity=Multiplicity(1, 1))
    }
)
SteamBoilerControlProgram14: BinaryAssociation = BinaryAssociation(
    name="SteamBoilerControlProgram14",
    ends={
        Property(name="SBCS_ControlProgram15", type=SBCS_SteamBoiler, multiplicity=Multiplicity(1, 1)),
        Property(name="SBCS_SteamBoiler", type=SBCS_ControlProgram, multiplicity=Multiplicity(1, 1))
    }
)
CPPost16: BinaryAssociation = BinaryAssociation(
    name="CPPost16",
    ends={
        Property(name="SBCS_ControlProgram17", type=SBCS_ControlProgram_Start, multiplicity=Multiplicity(1, 1)),
        Property(name="SBCS_ControlProgram_Start", type=SBCS_ControlProgram, multiplicity=Multiplicity(0, 1))
    }
)
SnapshotControlProgram23: BinaryAssociation = BinaryAssociation(
    name="SnapshotControlProgram23",
    ends={
        Property(name="SBCS_Snapshot25", type=SBCS_ControlProgram, multiplicity=Multiplicity(1, 1)),
        Property(name="SBCS_ControlProgram24", type=SBCS_Snapshot, multiplicity=Multiplicity(1, 1))
    }
)
wlmdPost26: BinaryAssociation = BinaryAssociation(
    name="wlmdPost26",
    ends={
        Property(name="SBCS_WaterLevelMeasurementDevice", type=SBCS_WaterLevelMeaurementDevice_getLevel, multiplicity=Multiplicity(1, 1)),
        Property(name="SBCS_WaterLevelMeaurementDevice_getLevel", type=SBCS_WaterLevelMeasurementDevice, multiplicity=Multiplicity(0, 1))
    }
)
AfterTrans27: BinaryAssociation = BinaryAssociation(
    name="AfterTrans27",
    ends={
        Property(name="SBCS_Snapshot29", type=SBCS_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="SBCS_Transition28", type=SBCS_Snapshot, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_SBCS_PumpController_OpenPump_Transition = Generalization(general=Transition, specific=SBCS_PumpController_OpenPump)
gen_SBCS_SteamBoiler_OpenValve_Transition = Generalization(general=Transition, specific=SBCS_SteamBoiler_OpenValve)
gen_SBCS_PumpController_ClosePump_Transition = Generalization(general=Transition, specific=SBCS_PumpController_ClosePump)
gen_SBCS_ControlProgram_Start_Transition = Generalization(general=Transition, specific=SBCS_ControlProgram_Start)
gen_SBCS_WaterLevelMeaurementDevice_getLevel_Transition = Generalization(general=Transition, specific=SBCS_WaterLevelMeaurementDevice_getLevel)


# OCL Constraints
ClosePump: Constraint = Constraint(
    name="ClosePump",
    context=SBCS_PumpController_ClosePump,
    expression="context PumpController_ClosePump inv: PCPre.PumpControlerPump.mode = State_On implies PCPost.PumpControlerPump.mode = State_Off",
    language="OCL"
)
TP2: Constraint = Constraint(
    name="TP2",
    context=SBCS_ControlProgram,
    expression="context ControlProgram inv: let CS:Snapshot = self.SnapshotControlProgram in let NS: Snapshot= CS.getNext()in (self.smdFailure or self.pumpFailure or self.pumpControlerFailure) implies NS.ControlProgramSnapshot.mode= Mode_Degraded",
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
    types={SBCS_WaterLevelMeasurementDevice, SBCS_Pump, SBCS_PumpController_OpenPump, Transition, SBCS_PumpControler, SBCS_Snapshot, SBCS_SteamBoiler_OpenValve, SBCS_ControlProgram, SBCS_Transition, SBCS_PumpController_ClosePump, SBCS_SteamBoiler, SBCS_ControlProgram_Start, SBCS_WaterLevelMeaurementDevice_getLevel, State, Mode, ValveState},
    associations={PCPost1, PCPre0, SBPre18, SBPost20, ControlProgramSnapshot4, AfterTrans5, PCPre7, PCPost9, PumpControlerPump12, SteamBoilerControlProgram14, CPPost16, SnapshotControlProgram23, wlmdPost26, AfterTrans27},
    constraints={ClosePump, TP2, OpenValve, Start, getLevel, SB, OpenPump},
    generalizations={gen_SBCS_PumpController_OpenPump_Transition, gen_SBCS_SteamBoiler_OpenValve_Transition, gen_SBCS_PumpController_ClosePump_Transition, gen_SBCS_ControlProgram_Start_Transition, gen_SBCS_WaterLevelMeaurementDevice_getLevel_Transition},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)