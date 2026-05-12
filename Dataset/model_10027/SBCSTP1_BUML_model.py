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

ValveState: Enumeration = Enumeration(
    name="ValveState",
    literals={
            EnumerationLiteral(name="Open"),
			EnumerationLiteral(name="Closed")
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

# Classes
SBCS_WaterLevelMeasurementDevice = Class(name="SBCS_WaterLevelMeasurementDevice")
SBCS_SteamBoiler_OpenValve = Class(name="SBCS_SteamBoiler_OpenValve")
SBCS_SteamBoiler = Class(name="SBCS_SteamBoiler")
SBCS_Pump = Class(name="SBCS_Pump")
SBCS_Snapshot = Class(name="SBCS_Snapshot")
SBCS_ControlProgram = Class(name="SBCS_ControlProgram")
SBCS_Transition = Class(name="SBCS_Transition")
SBCS_PumpController_OpenPump = Class(name="SBCS_PumpController_OpenPump")
Transition = Class(name="Transition")
SBCS_PumpControler = Class(name="SBCS_PumpControler")
SBCS_WaterLevelMeaurementDevice_getLevel = Class(name="SBCS_WaterLevelMeaurementDevice_getLevel")
SBCS_PumpController_ClosePump = Class(name="SBCS_PumpController_ClosePump")
SBCS_ControlProgram_Start = Class(name="SBCS_ControlProgram_Start")

# SBCS_WaterLevelMeasurementDevice class attributes and methods
SBCS_WaterLevelMeasurementDevice_waterLevel: Property = Property(name="waterLevel", type=FloatType)
SBCS_WaterLevelMeasurementDevice.attributes={SBCS_WaterLevelMeasurementDevice_waterLevel}

# SBCS_SteamBoiler_OpenValve class attributes and methods

# SBCS_SteamBoiler class attributes and methods
SBCS_SteamBoiler_valveOpen: Property = Property(name="valveOpen", type=StringType)
SBCS_SteamBoiler.attributes={SBCS_SteamBoiler_valveOpen}

# SBCS_Pump class attributes and methods
SBCS_Pump_mode: Property = Property(name="mode", type=StringType)
SBCS_Pump.attributes={SBCS_Pump_mode}

# SBCS_Snapshot class attributes and methods
SBCS_Snapshot_m_getNext: Method = Method(name="getNext", parameters={}, type=StringType)
SBCS_Snapshot.methods={SBCS_Snapshot_m_getNext}

# SBCS_ControlProgram class attributes and methods
SBCS_ControlProgram_mode: Property = Property(name="mode", type=StringType)
SBCS_ControlProgram_wlmdFailure: Property = Property(name="wlmdFailure", type=BooleanType)
SBCS_ControlProgram.attributes={SBCS_ControlProgram_mode, SBCS_ControlProgram_wlmdFailure}

# SBCS_Transition class attributes and methods

# SBCS_PumpController_OpenPump class attributes and methods

# Transition class attributes and methods

# SBCS_PumpControler class attributes and methods

# SBCS_WaterLevelMeaurementDevice_getLevel class attributes and methods
SBCS_WaterLevelMeaurementDevice_getLevel_ret: Property = Property(name="ret", type=FloatType)
SBCS_WaterLevelMeaurementDevice_getLevel.attributes={SBCS_WaterLevelMeaurementDevice_getLevel_ret}

# SBCS_PumpController_ClosePump class attributes and methods

# SBCS_ControlProgram_Start class attributes and methods

# Relationships
PCPre0: BinaryAssociation = BinaryAssociation(
    name="PCPre0",
    ends={
        Property(name="SBCS_PumpController_OpenPump", type=SBCS_PumpControler, multiplicity=Multiplicity(0, 1)),
        Property(name="SBCS_PumpControler", type=SBCS_PumpController_OpenPump, multiplicity=Multiplicity(1, 1))
    }
)
PCPost1: BinaryAssociation = BinaryAssociation(
    name="PCPost1",
    ends={
        Property(name="SBCS_PumpControler3", type=SBCS_PumpController_OpenPump, multiplicity=Multiplicity(1, 1)),
        Property(name="SBCS_PumpController_OpenPump2", type=SBCS_PumpControler, multiplicity=Multiplicity(0, 1))
    }
)
SBPre4: BinaryAssociation = BinaryAssociation(
    name="SBPre4",
    ends={
        Property(name="SBCS_SteamBoiler", type=SBCS_SteamBoiler_OpenValve, multiplicity=Multiplicity(1, 1)),
        Property(name="SBCS_SteamBoiler_OpenValve", type=SBCS_SteamBoiler, multiplicity=Multiplicity(0, 1))
    }
)
SBPost5: BinaryAssociation = BinaryAssociation(
    name="SBPost5",
    ends={
        Property(name="SBCS_SteamBoiler7", type=SBCS_SteamBoiler_OpenValve, multiplicity=Multiplicity(1, 1)),
        Property(name="SBCS_SteamBoiler_OpenValve6", type=SBCS_SteamBoiler, multiplicity=Multiplicity(0, 1))
    }
)
PumpControlerPump8: BinaryAssociation = BinaryAssociation(
    name="PumpControlerPump8",
    ends={
        Property(name="SBCS_Pump", type=SBCS_PumpControler, multiplicity=Multiplicity(1, 1)),
        Property(name="SBCS_PumpControler9", type=SBCS_Pump, multiplicity=Multiplicity(1, 1))
    }
)
ControlProgramSnapshot10: BinaryAssociation = BinaryAssociation(
    name="ControlProgramSnapshot10",
    ends={
        Property(name="SBCS_ControlProgram", type=SBCS_Snapshot, multiplicity=Multiplicity(1, 1)),
        Property(name="SBCS_Snapshot", type=SBCS_ControlProgram, multiplicity=Multiplicity(1, 1))
    }
)
AfterTrans11: BinaryAssociation = BinaryAssociation(
    name="AfterTrans11",
    ends={
        Property(name="SBCS_Transition", type=SBCS_Snapshot, multiplicity=Multiplicity(1, 1)),
        Property(name="SBCS_Snapshot12", type=SBCS_Transition, multiplicity=Multiplicity(1, 1))
    }
)
AfterTrans18: BinaryAssociation = BinaryAssociation(
    name="AfterTrans18",
    ends={
        Property(name="SBCS_Snapshot20", type=SBCS_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="SBCS_Transition19", type=SBCS_Snapshot, multiplicity=Multiplicity(1, 1))
    }
)
wlmdPost21: BinaryAssociation = BinaryAssociation(
    name="wlmdPost21",
    ends={
        Property(name="SBCS_WaterLevelMeasurementDevice", type=SBCS_WaterLevelMeaurementDevice_getLevel, multiplicity=Multiplicity(1, 1)),
        Property(name="SBCS_WaterLevelMeaurementDevice_getLevel", type=SBCS_WaterLevelMeasurementDevice, multiplicity=Multiplicity(0, 1))
    }
)
SnapshotControlProgram22: BinaryAssociation = BinaryAssociation(
    name="SnapshotControlProgram22",
    ends={
        Property(name="SBCS_Snapshot24", type=SBCS_ControlProgram, multiplicity=Multiplicity(1, 1)),
        Property(name="SBCS_ControlProgram23", type=SBCS_Snapshot, multiplicity=Multiplicity(1, 1))
    }
)
PCPre25: BinaryAssociation = BinaryAssociation(
    name="PCPre25",
    ends={
        Property(name="SBCS_PumpControler26", type=SBCS_PumpController_ClosePump, multiplicity=Multiplicity(1, 1)),
        Property(name="SBCS_PumpController_ClosePump", type=SBCS_PumpControler, multiplicity=Multiplicity(0, 1))
    }
)
PCPost27: BinaryAssociation = BinaryAssociation(
    name="PCPost27",
    ends={
        Property(name="SBCS_PumpControler29", type=SBCS_PumpController_ClosePump, multiplicity=Multiplicity(1, 1)),
        Property(name="SBCS_PumpController_ClosePump28", type=SBCS_PumpControler, multiplicity=Multiplicity(0, 1))
    }
)
CPPost13: BinaryAssociation = BinaryAssociation(
    name="CPPost13",
    ends={
        Property(name="SBCS_ControlProgram14", type=SBCS_ControlProgram_Start, multiplicity=Multiplicity(1, 1)),
        Property(name="SBCS_ControlProgram_Start", type=SBCS_ControlProgram, multiplicity=Multiplicity(0, 1))
    }
)
SteamBoilerControlProgram15: BinaryAssociation = BinaryAssociation(
    name="SteamBoilerControlProgram15",
    ends={
        Property(name="SBCS_ControlProgram17", type=SBCS_SteamBoiler, multiplicity=Multiplicity(1, 1)),
        Property(name="SBCS_SteamBoiler16", type=SBCS_ControlProgram, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_SBCS_SteamBoiler_OpenValve_Transition = Generalization(general=Transition, specific=SBCS_SteamBoiler_OpenValve)
gen_SBCS_PumpController_OpenPump_Transition = Generalization(general=Transition, specific=SBCS_PumpController_OpenPump)
gen_SBCS_WaterLevelMeaurementDevice_getLevel_Transition = Generalization(general=Transition, specific=SBCS_WaterLevelMeaurementDevice_getLevel)
gen_SBCS_PumpController_ClosePump_Transition = Generalization(general=Transition, specific=SBCS_PumpController_ClosePump)
gen_SBCS_ControlProgram_Start_Transition = Generalization(general=Transition, specific=SBCS_ControlProgram_Start)


# OCL Constraints
ClosePump: Constraint = Constraint(
    name="ClosePump",
    context=SBCS_PumpController_ClosePump,
    expression="context PumpController_ClosePump inv: PCPre.PumpControlerPump.mode = State_On implies PCPost.PumpControlerPump.mode = State_Off",
    language="OCL"
)
TP1: Constraint = Constraint(
    name="TP1",
    context=SBCS_ControlProgram,
    expression="context ControlProgram inv: let CS:Snapshot = self.SnapshotControlProgram in let NS: Snapshot= CS.getNext()in self.wlmdFailure implies NS.ControlProgramSnapshot.mode = Mode_Rescue",
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
    types={SBCS_WaterLevelMeasurementDevice, SBCS_SteamBoiler_OpenValve, SBCS_SteamBoiler, SBCS_Pump, SBCS_Snapshot, SBCS_ControlProgram, SBCS_Transition, SBCS_PumpController_OpenPump, Transition, SBCS_PumpControler, SBCS_WaterLevelMeaurementDevice_getLevel, SBCS_PumpController_ClosePump, SBCS_ControlProgram_Start, State, ValveState, Mode},
    associations={PCPre0, PCPost1, SBPre4, SBPost5, PumpControlerPump8, ControlProgramSnapshot10, AfterTrans11, AfterTrans18, wlmdPost21, SnapshotControlProgram22, PCPre25, PCPost27, CPPost13, SteamBoilerControlProgram15},
    constraints={ClosePump, TP1, OpenValve, Start, getLevel, SB, OpenPump},
    generalizations={gen_SBCS_SteamBoiler_OpenValve_Transition, gen_SBCS_PumpController_OpenPump_Transition, gen_SBCS_WaterLevelMeaurementDevice_getLevel_Transition, gen_SBCS_PumpController_ClosePump_Transition, gen_SBCS_ControlProgram_Start_Transition},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)