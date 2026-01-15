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
PowerUnitKind: Enumeration = Enumeration(
    name="PowerUnitKind",
    literals={
            EnumerationLiteral(name="W"),
			EnumerationLiteral(name="mW"),
			EnumerationLiteral(name="KW")
    }
)

FrequencyUnitKind: Enumeration = Enumeration(
    name="FrequencyUnitKind",
    literals={
            EnumerationLiteral(name="Hz"),
			EnumerationLiteral(name="KHz"),
			EnumerationLiteral(name="MHz"),
			EnumerationLiteral(name="GHz"),
			EnumerationLiteral(name="rpm")
    }
)

DataSizeUnitKind: Enumeration = Enumeration(
    name="DataSizeUnitKind",
    literals={
            EnumerationLiteral(name="bit"),
			EnumerationLiteral(name="Byte"),
			EnumerationLiteral(name="KB"),
			EnumerationLiteral(name="MB"),
			EnumerationLiteral(name="GB")
    }
)

DataTxRateUnitKind: Enumeration = Enumeration(
    name="DataTxRateUnitKind",
    literals={
            EnumerationLiteral(name="b_per_s"),
			EnumerationLiteral(name="Kb_per_s"),
			EnumerationLiteral(name="Mb_per_s")
    }
)

EnergyUnitKind: Enumeration = Enumeration(
    name="EnergyUnitKind",
    literals={
            EnumerationLiteral(name="J"),
			EnumerationLiteral(name="KJ"),
			EnumerationLiteral(name="Wh"),
			EnumerationLiteral(name="KWh"),
			EnumerationLiteral(name="mWh")
    }
)

LengthUnitKind: Enumeration = Enumeration(
    name="LengthUnitKind",
    literals={
            EnumerationLiteral(name="m"),
			EnumerationLiteral(name="cm"),
			EnumerationLiteral(name="mm")
    }
)

AreaUnitKind: Enumeration = Enumeration(
    name="AreaUnitKind",
    literals={
            EnumerationLiteral(name="mm2"),
			EnumerationLiteral(name="um2")
    }
)

WeightUnitKind: Enumeration = Enumeration(
    name="WeightUnitKind",
    literals={
            EnumerationLiteral(name="g"),
			EnumerationLiteral(name="mg"),
			EnumerationLiteral(name="kg")
    }
)

ProtectProtocolKind: Enumeration = Enumeration(
    name="ProtectProtocolKind",
    literals={
            EnumerationLiteral(name="FIFO"),
			EnumerationLiteral(name="NoPreemption"),
			EnumerationLiteral(name="PriorityCeiling"),
			EnumerationLiteral(name="PriorityInheritance"),
			EnumerationLiteral(name="StackBased"),
			EnumerationLiteral(name="Undef"),
			EnumerationLiteral(name="Other")
    }
)

PeriodicServerKind: Enumeration = Enumeration(
    name="PeriodicServerKind",
    literals={
            EnumerationLiteral(name="Sporadic"),
			EnumerationLiteral(name="Deferrable"),
			EnumerationLiteral(name="Undef"),
			EnumerationLiteral(name="Other")
    }
)

TransmModeKind: Enumeration = Enumeration(
    name="TransmModeKind",
    literals={
            EnumerationLiteral(name="simplex"),
			EnumerationLiteral(name="halfDuplex"),
			EnumerationLiteral(name="fullDuplex")
    }
)

SourceKind: Enumeration = Enumeration(
    name="SourceKind",
    literals={
            EnumerationLiteral(name="est"),
			EnumerationLiteral(name="meas"),
			EnumerationLiteral(name="calc"),
			EnumerationLiteral(name="req")
    }
)

DirectionKind: Enumeration = Enumeration(
    name="DirectionKind",
    literals={
            EnumerationLiteral(name="incr"),
			EnumerationLiteral(name="decr")
    }
)

StatisticalQualifierKind: Enumeration = Enumeration(
    name="StatisticalQualifierKind",
    literals={
            EnumerationLiteral(name="max"),
			EnumerationLiteral(name="other"),
			EnumerationLiteral(name="variance"),
			EnumerationLiteral(name="min"),
			EnumerationLiteral(name="mean"),
			EnumerationLiteral(name="range"),
			EnumerationLiteral(name="percent"),
			EnumerationLiteral(name="distrib"),
			EnumerationLiteral(name="determ")
    }
)

SchedPolicyKind: Enumeration = Enumeration(
    name="SchedPolicyKind",
    literals={
            EnumerationLiteral(name="LeastLaxityFirst"),
			EnumerationLiteral(name="RoundRobin"),
			EnumerationLiteral(name="TimeTableDriven"),
			EnumerationLiteral(name="Undef"),
			EnumerationLiteral(name="Other"),
			EnumerationLiteral(name="EarliestDeadlineFirst"),
			EnumerationLiteral(name="FIFO"),
			EnumerationLiteral(name="FixedPriority")
    }
)

TimeNatureKind: Enumeration = Enumeration(
    name="TimeNatureKind",
    literals={
            EnumerationLiteral(name="discrete"),
			EnumerationLiteral(name="dense")
    }
)

TimeInterpretationKind: Enumeration = Enumeration(
    name="TimeInterpretationKind",
    literals={
            EnumerationLiteral(name="duration"),
			EnumerationLiteral(name="instant")
    }
)

EventKind: Enumeration = Enumeration(
    name="EventKind",
    literals={
            EnumerationLiteral(name="start"),
			EnumerationLiteral(name="finish"),
			EnumerationLiteral(name="send"),
			EnumerationLiteral(name="receive"),
			EnumerationLiteral(name="consume")
    }
)

TimeStandardKind: Enumeration = Enumeration(
    name="TimeStandardKind",
    literals={
            EnumerationLiteral(name="TAI"),
			EnumerationLiteral(name="UT0"),
			EnumerationLiteral(name="UT1"),
			EnumerationLiteral(name="UTC"),
			EnumerationLiteral(name="Local"),
			EnumerationLiteral(name="TT"),
			EnumerationLiteral(name="TBD"),
			EnumerationLiteral(name="TCG"),
			EnumerationLiteral(name="Sidereal"),
			EnumerationLiteral(name="GPS"),
			EnumerationLiteral(name="TCB")
    }
)

TimeUnitKind: Enumeration = Enumeration(
    name="TimeUnitKind",
    literals={
            EnumerationLiteral(name="s"),
			EnumerationLiteral(name="ms"),
			EnumerationLiteral(name="us"),
			EnumerationLiteral(name="ns"),
			EnumerationLiteral(name="min"),
			EnumerationLiteral(name="hrs"),
			EnumerationLiteral(name="day")
    }
)

LogicalTimeUnit: Enumeration = Enumeration(
    name="LogicalTimeUnit",
    literals={
            EnumerationLiteral(name="tick")
    }
)

# Classes
MARTE_Library_TimeLibrary_IdealClock = Class(name="MARTE::Library::TimeLibrary::IdealClock")

# MARTE_Library_TimeLibrary_IdealClock class attributes and methods
MARTE_Library_TimeLibrary_IdealClock_m_currentTime: Method = Method(name="currentTime", parameters={}, type=StringType)
MARTE_Library_TimeLibrary_IdealClock.methods={MARTE_Library_TimeLibrary_IdealClock_m_currentTime}

# Domain Model
domain_model = DomainModel(
    name="MARTE_Library",
    types={MARTE_Library_TimeLibrary_IdealClock, PowerUnitKind, FrequencyUnitKind, DataSizeUnitKind, DataTxRateUnitKind, EnergyUnitKind, LengthUnitKind, AreaUnitKind, WeightUnitKind, ProtectProtocolKind, PeriodicServerKind, TransmModeKind, SourceKind, DirectionKind, StatisticalQualifierKind, SchedPolicyKind, TimeNatureKind, TimeInterpretationKind, EventKind, TimeStandardKind, TimeUnitKind, LogicalTimeUnit},
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