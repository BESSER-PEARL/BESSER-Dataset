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
SBCS_Snapshot = Class(name="SBCS_Snapshot")
SBCS_ControlProgram = Class(name="SBCS_ControlProgram")
SBCS_Pump = Class(name="SBCS_Pump")
SBCS_SteamBoiler = Class(name="SBCS_SteamBoiler")
SBCS_PumpControler = Class(name="SBCS_PumpControler")
SBCS_Transition = Class(name="SBCS_Transition")
SBCS_SteamMeasurementDevice = Class(name="SBCS_SteamMeasurementDevice")
SBCS_WaterLevelMeasurementDevice = Class(name="SBCS_WaterLevelMeasurementDevice")
SBCS_ControlProgram_Start = Class(name="SBCS_ControlProgram_Start")
Transition = Class(name="Transition")
SBCS_WaterLevelMeaurementDevice_getLevel = Class(name="SBCS_WaterLevelMeaurementDevice_getLevel")
SBCS_PumpController_OpenPump = Class(name="SBCS_PumpController_OpenPump")
SBCS_SteamBoiler_OpenValve = Class(name="SBCS_SteamBoiler_OpenValve")
SBCS_PumpController_ClosePump = Class(name="SBCS_PumpController_ClosePump")

# SBCS_Snapshot class attributes and methods
SBCS_Snapshot_m_getNext: Method = Method(name="getNext", parameters={}, type=StringType)
SBCS_Snapshot_m_futureClosure: Method = Method(name="futureClosure", parameters={Parameter(name='SBCS_s', type=StringType)}, type=StringType)
SBCS_Snapshot_m_getPost: Method = Method(name="getPost", parameters={}, type=StringType)
SBCS_Snapshot_m_getPrevious: Method = Method(name="getPrevious", parameters={}, type=StringType)
SBCS_Snapshot_m_previousClosure: Method = Method(name="previousClosure", parameters={Parameter(name='SBCS_s', type=StringType)}, type=StringType)
SBCS_Snapshot_m_getPre: Method = Method(name="getPre", parameters={}, type=StringType)
SBCS_Snapshot.methods={SBCS_Snapshot_m_getPrevious, SBCS_Snapshot_m_futureClosure, SBCS_Snapshot_m_getPre, SBCS_Snapshot_m_getNext, SBCS_Snapshot_m_getPost, SBCS_Snapshot_m_previousClosure}

# SBCS_ControlProgram class attributes and methods
SBCS_ControlProgram_mode: Property = Property(name="mode", type=StringType)
SBCS_ControlProgram_ready: Property = Property(name="ready", type=BooleanType)
SBCS_ControlProgram_failureDetected: Property = Property(name="failureDetected", type=BooleanType)
SBCS_ControlProgram_wlmdFailure: Property = Property(name="wlmdFailure", type=BooleanType)
SBCS_ControlProgram_smdFailure: Property = Property(name="smdFailure", type=BooleanType)
SBCS_ControlProgram_pumpFailure: Property = Property(name="pumpFailure", type=BooleanType)
SBCS_ControlProgram_pumpControlerFailure: Property = Property(name="pumpControlerFailure", type=BooleanType)
SBCS_ControlProgram.attributes={SBCS_ControlProgram_pumpFailure, SBCS_ControlProgram_mode, SBCS_ControlProgram_failureDetected, SBCS_ControlProgram_ready, SBCS_ControlProgram_smdFailure, SBCS_ControlProgram_pumpControlerFailure, SBCS_ControlProgram_wlmdFailure}

# SBCS_Pump class attributes and methods
SBCS_Pump_ready: Property = Property(name="ready", type=BooleanType)
SBCS_Pump_capacity: Property = Property(name="capacity", type=FloatType)
SBCS_Pump_mode: Property = Property(name="mode", type=StringType)
SBCS_Pump.attributes={SBCS_Pump_ready, SBCS_Pump_capacity, SBCS_Pump_mode}

# SBCS_SteamBoiler class attributes and methods
SBCS_SteamBoiler_ready: Property = Property(name="ready", type=BooleanType)
SBCS_SteamBoiler_capacity: Property = Property(name="capacity", type=FloatType)
SBCS_SteamBoiler_minimalNormal: Property = Property(name="minimalNormal", type=FloatType)
SBCS_SteamBoiler_maximalNormal: Property = Property(name="maximalNormal", type=FloatType)
SBCS_SteamBoiler_maximumIncrease: Property = Property(name="maximumIncrease", type=FloatType)
SBCS_SteamBoiler_maximumDecrease: Property = Property(name="maximumDecrease", type=FloatType)
SBCS_SteamBoiler_minimalLimit: Property = Property(name="minimalLimit", type=FloatType)
SBCS_SteamBoiler_maximalLimit: Property = Property(name="maximalLimit", type=FloatType)
SBCS_SteamBoiler_valveOpen: Property = Property(name="valveOpen", type=StringType)
SBCS_SteamBoiler.attributes={SBCS_SteamBoiler_maximalNormal, SBCS_SteamBoiler_capacity, SBCS_SteamBoiler_maximalLimit, SBCS_SteamBoiler_minimalLimit, SBCS_SteamBoiler_minimalNormal, SBCS_SteamBoiler_maximumIncrease, SBCS_SteamBoiler_ready, SBCS_SteamBoiler_valveOpen, SBCS_SteamBoiler_maximumDecrease}

# SBCS_PumpControler class attributes and methods
SBCS_PumpControler_ready: Property = Property(name="ready", type=BooleanType)
SBCS_PumpControler_circulating: Property = Property(name="circulating", type=BooleanType)
SBCS_PumpControler.attributes={SBCS_PumpControler_ready, SBCS_PumpControler_circulating}

# SBCS_Transition class attributes and methods

# SBCS_SteamMeasurementDevice class attributes and methods
SBCS_SteamMeasurementDevice_ready: Property = Property(name="ready", type=BooleanType)
SBCS_SteamMeasurementDevice_evaporationRate: Property = Property(name="evaporationRate", type=BooleanType)
SBCS_SteamMeasurementDevice_waterLevel: Property = Property(name="waterLevel", type=FloatType)
SBCS_SteamMeasurementDevice.attributes={SBCS_SteamMeasurementDevice_waterLevel, SBCS_SteamMeasurementDevice_ready, SBCS_SteamMeasurementDevice_evaporationRate}

# SBCS_WaterLevelMeasurementDevice class attributes and methods
SBCS_WaterLevelMeasurementDevice_ready: Property = Property(name="ready", type=BooleanType)
SBCS_WaterLevelMeasurementDevice_waterLevel: Property = Property(name="waterLevel", type=FloatType)
SBCS_WaterLevelMeasurementDevice.attributes={SBCS_WaterLevelMeasurementDevice_waterLevel, SBCS_WaterLevelMeasurementDevice_ready}

# SBCS_ControlProgram_Start class attributes and methods

# Transition class attributes and methods

# SBCS_WaterLevelMeaurementDevice_getLevel class attributes and methods
SBCS_WaterLevelMeaurementDevice_getLevel_ret: Property = Property(name="ret", type=FloatType)
SBCS_WaterLevelMeaurementDevice_getLevel.attributes={SBCS_WaterLevelMeaurementDevice_getLevel_ret}

# SBCS_PumpController_OpenPump class attributes and methods

# SBCS_SteamBoiler_OpenValve class attributes and methods

# SBCS_PumpController_ClosePump class attributes and methods

# Relationships
SnapshotSteamBoiler0: BinaryAssociation = BinaryAssociation(
    name="SnapshotSteamBoiler0",
    ends={
        Property(name="Snapshot", type=SBCS_SteamBoiler, multiplicity=Multiplicity(1, 1)),
        Property(name="SteamBoilerSnapshot", type=SBCS_Snapshot, multiplicity=Multiplicity(1, 1))
    }
)
SteamBoilerControlProgram1: BinaryAssociation = BinaryAssociation(
    name="SteamBoilerControlProgram1",
    ends={
        Property(name="ControlProgram", type=SBCS_SteamBoiler, multiplicity=Multiplicity(1, 1)),
        Property(name="ControlProgramSteamBoiler", type=SBCS_ControlProgram, multiplicity=Multiplicity(1, 1))
    }
)
SteamBoilerMeasurementDeviceSnapshot12: BinaryAssociation = BinaryAssociation(
    name="SteamBoilerMeasurementDeviceSnapshot12",
    ends={
        Property(name="SteamMeasurementDevice13", type=SBCS_Snapshot, multiplicity=Multiplicity(1, 1)),
        Property(name="SnapshotSBMD", type=SBCS_SteamMeasurementDevice, multiplicity=Multiplicity(1, 1))
    }
)
PumpControlSnapshot14: BinaryAssociation = BinaryAssociation(
    name="PumpControlSnapshot14",
    ends={
        Property(name="PumpControler", type=SBCS_Snapshot, multiplicity=Multiplicity(1, 1)),
        Property(name="SnapshotPumpControl", type=SBCS_PumpControler, multiplicity=Multiplicity(1, 1))
    }
)
BeforeTrans15: BinaryAssociation = BinaryAssociation(
    name="BeforeTrans15",
    ends={
        Property(name="Transition", type=SBCS_Snapshot, multiplicity=Multiplicity(1, 1)),
        Property(name="BeforeTrans", type=SBCS_Transition, multiplicity=Multiplicity(1, 1))
    }
)
AfterTrans16: BinaryAssociation = BinaryAssociation(
    name="AfterTrans16",
    ends={
        Property(name="Transition17", type=SBCS_Snapshot, multiplicity=Multiplicity(1, 1)),
        Property(name="AfterTrans", type=SBCS_Transition, multiplicity=Multiplicity(1, 1))
    }
)
SnapshotControlProgram18: BinaryAssociation = BinaryAssociation(
    name="SnapshotControlProgram18",
    ends={
        Property(name="Snapshot19", type=SBCS_ControlProgram, multiplicity=Multiplicity(1, 1)),
        Property(name="ControlProgramSnapshot", type=SBCS_Snapshot, multiplicity=Multiplicity(1, 1))
    }
)
ControlProgramPump20: BinaryAssociation = BinaryAssociation(
    name="ControlProgramPump20",
    ends={
        Property(name="Pump21", type=SBCS_ControlProgram, multiplicity=Multiplicity(1, 1)),
        Property(name="PumpControlProgram", type=SBCS_Pump, multiplicity=Multiplicity(1, 1))
    }
)
ControlProgramWLMD22: BinaryAssociation = BinaryAssociation(
    name="ControlProgramWLMD22",
    ends={
        Property(name="WaterLevelMeasurementDevice23", type=SBCS_ControlProgram, multiplicity=Multiplicity(1, 1)),
        Property(name="WLMDControlProgram", type=SBCS_WaterLevelMeasurementDevice, multiplicity=Multiplicity(1, 1))
    }
)
ControlProgramSMD24: BinaryAssociation = BinaryAssociation(
    name="ControlProgramSMD24",
    ends={
        Property(name="SteamMeasurementDevice25", type=SBCS_ControlProgram, multiplicity=Multiplicity(1, 1)),
        Property(name="SMDControlProgram", type=SBCS_SteamMeasurementDevice, multiplicity=Multiplicity(1, 1))
    }
)
SteqmBoilerPump2: BinaryAssociation = BinaryAssociation(
    name="SteqmBoilerPump2",
    ends={
        Property(name="Pump", type=SBCS_SteamBoiler, multiplicity=Multiplicity(1, 1)),
        Property(name="PumpSteamBoiler", type=SBCS_Pump, multiplicity=Multiplicity(1, 1))
    }
)
SteamBoilerSMD3: BinaryAssociation = BinaryAssociation(
    name="SteamBoilerSMD3",
    ends={
        Property(name="SteamMeasurementDevice", type=SBCS_SteamBoiler, multiplicity=Multiplicity(1, 1)),
        Property(name="SMDSteamBoiler", type=SBCS_SteamMeasurementDevice, multiplicity=Multiplicity(1, 1))
    }
)
SteamBoilerWLMD4: BinaryAssociation = BinaryAssociation(
    name="SteamBoilerWLMD4",
    ends={
        Property(name="WaterLevelMeasurementDevice", type=SBCS_SteamBoiler, multiplicity=Multiplicity(1, 1)),
        Property(name="WLMDSteamBoiler", type=SBCS_WaterLevelMeasurementDevice, multiplicity=Multiplicity(1, 1))
    }
)
SteamBoilerSnapshot5: BinaryAssociation = BinaryAssociation(
    name="SteamBoilerSnapshot5",
    ends={
        Property(name="SteamBoiler", type=SBCS_Snapshot, multiplicity=Multiplicity(1, 1)),
        Property(name="SnapshotSteamBoiler", type=SBCS_SteamBoiler, multiplicity=Multiplicity(0, 1))
    }
)
ControlProgramSnapshot6: BinaryAssociation = BinaryAssociation(
    name="ControlProgramSnapshot6",
    ends={
        Property(name="ControlProgram7", type=SBCS_Snapshot, multiplicity=Multiplicity(1, 1)),
        Property(name="SnapshotControlProgram", type=SBCS_ControlProgram, multiplicity=Multiplicity(1, 1))
    }
)
PumpSnapshot8: BinaryAssociation = BinaryAssociation(
    name="PumpSnapshot8",
    ends={
        Property(name="Pump9", type=SBCS_Snapshot, multiplicity=Multiplicity(1, 1)),
        Property(name="PumpSnapshot", type=SBCS_Pump, multiplicity=Multiplicity(1, 1))
    }
)
WLMDSnapshot10: BinaryAssociation = BinaryAssociation(
    name="WLMDSnapshot10",
    ends={
        Property(name="WaterLevelMeasurementDevice11", type=SBCS_Snapshot, multiplicity=Multiplicity(1, 1)),
        Property(name="SnapshotWLMD", type=SBCS_WaterLevelMeasurementDevice, multiplicity=Multiplicity(1, 1))
    }
)
PumpSteamBoiler37: BinaryAssociation = BinaryAssociation(
    name="PumpSteamBoiler37",
    ends={
        Property(name="SteamBoiler38", type=SBCS_Pump, multiplicity=Multiplicity(1, 1)),
        Property(name="SteqmBoilerPump", type=SBCS_SteamBoiler, multiplicity=Multiplicity(1, 1))
    }
)
BeforeTrans39: BinaryAssociation = BinaryAssociation(
    name="BeforeTrans39",
    ends={
        Property(name="Snapshot41", type=SBCS_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="BeforeTrans40", type=SBCS_Snapshot, multiplicity=Multiplicity(1, 1))
    }
)
AfterTrans42: BinaryAssociation = BinaryAssociation(
    name="AfterTrans42",
    ends={
        Property(name="Snapshot44", type=SBCS_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="AfterTrans43", type=SBCS_Snapshot, multiplicity=Multiplicity(1, 1))
    }
)
SnapshotPumpControl45: BinaryAssociation = BinaryAssociation(
    name="SnapshotPumpControl45",
    ends={
        Property(name="Snapshot46", type=SBCS_PumpControler, multiplicity=Multiplicity(1, 1)),
        Property(name="PumpControlSnapshot", type=SBCS_Snapshot, multiplicity=Multiplicity(1, 1))
    }
)
ControlProgramSteamBoiler26: BinaryAssociation = BinaryAssociation(
    name="ControlProgramSteamBoiler26",
    ends={
        Property(name="SteamBoiler27", type=SBCS_ControlProgram, multiplicity=Multiplicity(1, 1)),
        Property(name="SteamBoilerControlProgram", type=SBCS_SteamBoiler, multiplicity=Multiplicity(1, 1))
    }
)
ControlProgramPumpControler28: BinaryAssociation = BinaryAssociation(
    name="ControlProgramPumpControler28",
    ends={
        Property(name="PumpControler29", type=SBCS_ControlProgram, multiplicity=Multiplicity(1, 1)),
        Property(name="PumpControlerControlProgram", type=SBCS_PumpControler, multiplicity=Multiplicity(1, 1))
    }
)
PumpSnapshot30: BinaryAssociation = BinaryAssociation(
    name="PumpSnapshot30",
    ends={
        Property(name="Snapshot32", type=SBCS_Pump, multiplicity=Multiplicity(1, 1)),
        Property(name="PumpSnapshot31", type=SBCS_Snapshot, multiplicity=Multiplicity(1, 1))
    }
)
PumpControlProgram33: BinaryAssociation = BinaryAssociation(
    name="PumpControlProgram33",
    ends={
        Property(name="ControlProgram34", type=SBCS_Pump, multiplicity=Multiplicity(1, 1)),
        Property(name="ControlProgramPump", type=SBCS_ControlProgram, multiplicity=Multiplicity(1, 1))
    }
)
CPPre63: BinaryAssociation = BinaryAssociation(
    name="CPPre63",
    ends={
        Property(name="SBCS_ControlProgram", type=SBCS_ControlProgram_Start, multiplicity=Multiplicity(1, 1)),
        Property(name="SBCS_ControlProgram_Start", type=SBCS_ControlProgram, multiplicity=Multiplicity(0, 1))
    }
)
PumpPumpControler35: BinaryAssociation = BinaryAssociation(
    name="PumpPumpControler35",
    ends={
        Property(name="PumpControler36", type=SBCS_Pump, multiplicity=Multiplicity(1, 1)),
        Property(name="PumpControlerPump", type=SBCS_PumpControler, multiplicity=Multiplicity(1, 1))
    }
)
CPPost64: BinaryAssociation = BinaryAssociation(
    name="CPPost64",
    ends={
        Property(name="SBCS_ControlProgram66", type=SBCS_ControlProgram_Start, multiplicity=Multiplicity(1, 1)),
        Property(name="SBCS_ControlProgram_Start65", type=SBCS_ControlProgram, multiplicity=Multiplicity(0, 1))
    }
)
wlmdPre67: BinaryAssociation = BinaryAssociation(
    name="wlmdPre67",
    ends={
        Property(name="SBCS_WaterLevelMeasurementDevice", type=SBCS_WaterLevelMeaurementDevice_getLevel, multiplicity=Multiplicity(1, 1)),
        Property(name="SBCS_WaterLevelMeaurementDevice_getLevel", type=SBCS_WaterLevelMeasurementDevice, multiplicity=Multiplicity(0, 1))
    }
)
wlmdPost68: BinaryAssociation = BinaryAssociation(
    name="wlmdPost68",
    ends={
        Property(name="SBCS_WaterLevelMeasurementDevice70", type=SBCS_WaterLevelMeaurementDevice_getLevel, multiplicity=Multiplicity(1, 1)),
        Property(name="SBCS_WaterLevelMeaurementDevice_getLevel69", type=SBCS_WaterLevelMeasurementDevice, multiplicity=Multiplicity(0, 1))
    }
)
PumpControlerControlProgram47: BinaryAssociation = BinaryAssociation(
    name="PumpControlerControlProgram47",
    ends={
        Property(name="ControlProgram48", type=SBCS_PumpControler, multiplicity=Multiplicity(1, 1)),
        Property(name="ControlProgramPumpControler", type=SBCS_ControlProgram, multiplicity=Multiplicity(1, 1))
    }
)
PumpControlerPump49: BinaryAssociation = BinaryAssociation(
    name="PumpControlerPump49",
    ends={
        Property(name="Pump50", type=SBCS_PumpControler, multiplicity=Multiplicity(1, 1)),
        Property(name="PumpPumpControler", type=SBCS_Pump, multiplicity=Multiplicity(1, 1))
    }
)
SnapshotSBMD51: BinaryAssociation = BinaryAssociation(
    name="SnapshotSBMD51",
    ends={
        Property(name="Snapshot52", type=SBCS_SteamMeasurementDevice, multiplicity=Multiplicity(1, 1)),
        Property(name="SteamBoilerMeasurementDeviceSnapshot", type=SBCS_Snapshot, multiplicity=Multiplicity(1, 1))
    }
)
SMDControlProgram53: BinaryAssociation = BinaryAssociation(
    name="SMDControlProgram53",
    ends={
        Property(name="ControlProgram54", type=SBCS_SteamMeasurementDevice, multiplicity=Multiplicity(1, 1)),
        Property(name="ControlProgramSMD", type=SBCS_ControlProgram, multiplicity=Multiplicity(1, 1))
    }
)
SMDSteamBoiler55: BinaryAssociation = BinaryAssociation(
    name="SMDSteamBoiler55",
    ends={
        Property(name="SteamBoiler56", type=SBCS_SteamMeasurementDevice, multiplicity=Multiplicity(1, 1)),
        Property(name="SteamBoilerSMD", type=SBCS_SteamBoiler, multiplicity=Multiplicity(1, 1))
    }
)
SnapshotWLMD57: BinaryAssociation = BinaryAssociation(
    name="SnapshotWLMD57",
    ends={
        Property(name="Snapshot58", type=SBCS_WaterLevelMeasurementDevice, multiplicity=Multiplicity(1, 1)),
        Property(name="WLMDSnapshot", type=SBCS_Snapshot, multiplicity=Multiplicity(1, 1))
    }
)
WLMDControlProgram59: BinaryAssociation = BinaryAssociation(
    name="WLMDControlProgram59",
    ends={
        Property(name="ControlProgram60", type=SBCS_WaterLevelMeasurementDevice, multiplicity=Multiplicity(1, 1)),
        Property(name="ControlProgramWLMD", type=SBCS_ControlProgram, multiplicity=Multiplicity(1, 1))
    }
)
WLMDSteamBoiler61: BinaryAssociation = BinaryAssociation(
    name="WLMDSteamBoiler61",
    ends={
        Property(name="SteamBoiler62", type=SBCS_WaterLevelMeasurementDevice, multiplicity=Multiplicity(1, 1)),
        Property(name="SteamBoilerWLMD", type=SBCS_SteamBoiler, multiplicity=Multiplicity(1, 1))
    }
)
PCPre79: BinaryAssociation = BinaryAssociation(
    name="PCPre79",
    ends={
        Property(name="SBCS_PumpControler80", type=SBCS_PumpController_OpenPump, multiplicity=Multiplicity(1, 1)),
        Property(name="SBCS_PumpController_OpenPump", type=SBCS_PumpControler, multiplicity=Multiplicity(0, 1))
    }
)
PCPost81: BinaryAssociation = BinaryAssociation(
    name="PCPost81",
    ends={
        Property(name="SBCS_PumpControler83", type=SBCS_PumpController_OpenPump, multiplicity=Multiplicity(1, 1)),
        Property(name="SBCS_PumpController_OpenPump82", type=SBCS_PumpControler, multiplicity=Multiplicity(0, 1))
    }
)
SBPre71: BinaryAssociation = BinaryAssociation(
    name="SBPre71",
    ends={
        Property(name="SBCS_SteamBoiler", type=SBCS_SteamBoiler_OpenValve, multiplicity=Multiplicity(1, 1)),
        Property(name="SBCS_SteamBoiler_OpenValve", type=SBCS_SteamBoiler, multiplicity=Multiplicity(0, 1))
    }
)
SBPost72: BinaryAssociation = BinaryAssociation(
    name="SBPost72",
    ends={
        Property(name="SBCS_SteamBoiler74", type=SBCS_SteamBoiler_OpenValve, multiplicity=Multiplicity(1, 1)),
        Property(name="SBCS_SteamBoiler_OpenValve73", type=SBCS_SteamBoiler, multiplicity=Multiplicity(0, 1))
    }
)
PCPre75: BinaryAssociation = BinaryAssociation(
    name="PCPre75",
    ends={
        Property(name="SBCS_PumpControler", type=SBCS_PumpController_ClosePump, multiplicity=Multiplicity(1, 1)),
        Property(name="SBCS_PumpController_ClosePump", type=SBCS_PumpControler, multiplicity=Multiplicity(0, 1))
    }
)
PCPost76: BinaryAssociation = BinaryAssociation(
    name="PCPost76",
    ends={
        Property(name="SBCS_PumpControler78", type=SBCS_PumpController_ClosePump, multiplicity=Multiplicity(1, 1)),
        Property(name="SBCS_PumpController_ClosePump77", type=SBCS_PumpControler, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_SBCS_ControlProgram_Start_Transition = Generalization(general=Transition, specific=SBCS_ControlProgram_Start)
gen_SBCS_WaterLevelMeaurementDevice_getLevel_Transition = Generalization(general=Transition, specific=SBCS_WaterLevelMeaurementDevice_getLevel)
gen_SBCS_PumpController_OpenPump_Transition = Generalization(general=Transition, specific=SBCS_PumpController_OpenPump)
gen_SBCS_SteamBoiler_OpenValve_Transition = Generalization(general=Transition, specific=SBCS_SteamBoiler_OpenValve)
gen_SBCS_PumpController_ClosePump_Transition = Generalization(general=Transition, specific=SBCS_PumpController_ClosePump)

# Domain Model
domain_model = DomainModel(
    name="SBCS",
    types={SBCS_Snapshot, SBCS_ControlProgram, SBCS_Pump, SBCS_SteamBoiler, SBCS_PumpControler, SBCS_Transition, SBCS_SteamMeasurementDevice, SBCS_WaterLevelMeasurementDevice, SBCS_ControlProgram_Start, Transition, SBCS_WaterLevelMeaurementDevice_getLevel, SBCS_PumpController_OpenPump, SBCS_SteamBoiler_OpenValve, SBCS_PumpController_ClosePump, Mode, State, ValveState},
    associations={SnapshotSteamBoiler0, SteamBoilerControlProgram1, SteamBoilerMeasurementDeviceSnapshot12, PumpControlSnapshot14, BeforeTrans15, AfterTrans16, SnapshotControlProgram18, ControlProgramPump20, ControlProgramWLMD22, ControlProgramSMD24, SteqmBoilerPump2, SteamBoilerSMD3, SteamBoilerWLMD4, SteamBoilerSnapshot5, ControlProgramSnapshot6, PumpSnapshot8, WLMDSnapshot10, PumpSteamBoiler37, BeforeTrans39, AfterTrans42, SnapshotPumpControl45, ControlProgramSteamBoiler26, ControlProgramPumpControler28, PumpSnapshot30, PumpControlProgram33, CPPre63, PumpPumpControler35, CPPost64, wlmdPre67, wlmdPost68, PumpControlerControlProgram47, PumpControlerPump49, SnapshotSBMD51, SMDControlProgram53, SMDSteamBoiler55, SnapshotWLMD57, WLMDControlProgram59, WLMDSteamBoiler61, PCPre79, PCPost81, SBPre71, SBPost72, PCPre75, PCPost76},
    generalizations={gen_SBCS_ControlProgram_Start_Transition, gen_SBCS_WaterLevelMeaurementDevice_getLevel_Transition, gen_SBCS_PumpController_OpenPump_Transition, gen_SBCS_SteamBoiler_OpenValve_Transition, gen_SBCS_PumpController_ClosePump_Transition},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)