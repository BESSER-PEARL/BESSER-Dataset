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

SchedPolicyKind: Enumeration = Enumeration(
    name="SchedPolicyKind",
    literals={
            EnumerationLiteral(name="EarliestDeadlineFirst"),
			EnumerationLiteral(name="FIFO"),
			EnumerationLiteral(name="FixedPriority"),
			EnumerationLiteral(name="LeastLaxityFirst"),
			EnumerationLiteral(name="RoundRobin"),
			EnumerationLiteral(name="TimeTableDriven"),
			EnumerationLiteral(name="Undef"),
			EnumerationLiteral(name="Other")
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
			EnumerationLiteral(name="min"),
			EnumerationLiteral(name="mean"),
			EnumerationLiteral(name="range"),
			EnumerationLiteral(name="percent"),
			EnumerationLiteral(name="distrib"),
			EnumerationLiteral(name="determ"),
			EnumerationLiteral(name="other"),
			EnumerationLiteral(name="variance")
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
            EnumerationLiteral(name="UTC"),
			EnumerationLiteral(name="Local"),
			EnumerationLiteral(name="TAI"),
			EnumerationLiteral(name="UT0"),
			EnumerationLiteral(name="UT1"),
			EnumerationLiteral(name="TT"),
			EnumerationLiteral(name="TBD"),
			EnumerationLiteral(name="TCG"),
			EnumerationLiteral(name="TCB"),
			EnumerationLiteral(name="Sidereal"),
			EnumerationLiteral(name="GPS")
    }
)

TUK: Enumeration = Enumeration(
    name="TUK",
    literals={
            
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
MARTE_Library_GRM_BasicTypes_EDF_Parameters = Class(name="MARTE::Library::GRM::BasicTypes::EDF::Parameters")
NFP_Duration = Class(name="NFP::Duration")
PoolingParameters = Class(name="PoolingParameters")
MARTE_Library_GRM_BasicTypes_SchedParameters = Class(name="MARTE::Library::GRM::BasicTypes::SchedParameters")
EDF_Parameters = Class(name="EDF::Parameters")
FixedPriorityParameters = Class(name="FixedPriorityParameters")
PeriodicServerParameters = Class(name="PeriodicServerParameters")
MARTE_Library_GRM_BasicTypes_FixedPriorityParameters = Class(name="MARTE::Library::GRM::BasicTypes::FixedPriorityParameters")
NFP_Integer = Class(name="NFP::Integer")
MARTE_Library_GRM_BasicTypes_PoolingParameters = Class(name="MARTE::Library::GRM::BasicTypes::PoolingParameters")
MARTE_Library_GRM_BasicTypes_PeriodicServerParameters = Class(name="MARTE::Library::GRM::BasicTypes::PeriodicServerParameters")
MARTE_Library_BasicNFP_Types_NFP_CommonType = Class(name="MARTE::Library::BasicNFP::Types::NFP::CommonType")
MARTE_Library_BasicNFP_Types_NFP_Boolean = Class(name="MARTE::Library::BasicNFP::Types::NFP::Boolean")
MARTE_Library_BasicNFP_Types_NFP_Frequency = Class(name="MARTE::Library::BasicNFP::Types::NFP::Frequency")
NFP_Real = Class(name="NFP::Real")
MARTE_Library_BasicNFP_Types_NFP_Real = Class(name="MARTE::Library::BasicNFP::Types::NFP::Real")
NFP_CommonType = Class(name="NFP::CommonType")
MARTE_Library_BasicNFP_Types_NFP_Natural = Class(name="MARTE::Library::BasicNFP::Types::NFP::Natural")
MARTE_Library_BasicNFP_Types_NFP_Energy = Class(name="MARTE::Library::BasicNFP::Types::NFP::Energy")
MARTE_Library_BasicNFP_Types_NFP_String = Class(name="MARTE::Library::BasicNFP::Types::NFP::String")
MARTE_Library_BasicNFP_Types_NFP_Integer = Class(name="MARTE::Library::BasicNFP::Types::NFP::Integer")
MARTE_Library_BasicNFP_Types_NFP_DateTime = Class(name="MARTE::Library::BasicNFP::Types::NFP::DateTime")
MARTE_Library_BasicNFP_Types_NFP_DataTxRate = Class(name="MARTE::Library::BasicNFP::Types::NFP::DataTxRate")
MARTE_Library_BasicNFP_Types_NFP_Power = Class(name="MARTE::Library::BasicNFP::Types::NFP::Power")
MARTE_Library_BasicNFP_Types_NFP_DataSize = Class(name="MARTE::Library::BasicNFP::Types::NFP::DataSize")
SporadicPattern = Class(name="SporadicPattern")
MARTE_Library_BasicNFP_Types_NFP_Length = Class(name="MARTE::Library::BasicNFP::Types::NFP::Length")
MARTE_Library_BasicNFP_Types_NFP_Area = Class(name="MARTE::Library::BasicNFP::Types::NFP::Area")
MARTE_Library_BasicNFP_Types_ArrivalPattern = Class(name="MARTE::Library::BasicNFP::Types::ArrivalPattern")
PeriodicPattern = Class(name="PeriodicPattern")
AperiodicPattern = Class(name="AperiodicPattern")
BurstPattern = Class(name="BurstPattern")
IrregularPattern = Class(name="IrregularPattern")
ClosedPattern = Class(name="ClosedPattern")
OpenPattern = Class(name="OpenPattern")
MARTE_Library_BasicNFP_Types_PeriodicPattern = Class(name="MARTE::Library::BasicNFP::Types::PeriodicPattern")
MARTE_Library_BasicNFP_Types_AperiodicPattern = Class(name="MARTE::Library::BasicNFP::Types::AperiodicPattern")
MARTE_Library_BasicNFP_Types_BurstPattern = Class(name="MARTE::Library::BasicNFP::Types::BurstPattern")
MARTE_Library_BasicNFP_Types_IrregularPattern = Class(name="MARTE::Library::BasicNFP::Types::IrregularPattern")
MARTE_Library_BasicNFP_Types_ClosedPattern = Class(name="MARTE::Library::BasicNFP::Types::ClosedPattern")
MARTE_Library_BasicNFP_Types_SporadicPattern = Class(name="MARTE::Library::BasicNFP::Types::SporadicPattern")
MARTE_Library_BasicNFP_Types_OpenPattern = Class(name="MARTE::Library::BasicNFP::Types::OpenPattern")
NFP_Frequency = Class(name="NFP::Frequency")
MARTE_Library_BasicNFP_Types_NFP_Percentage = Class(name="MARTE::Library::BasicNFP::Types::NFP::Percentage")
MARTE_Library_BasicNFP_Types_NFP_Price = Class(name="MARTE::Library::BasicNFP::Types::NFP::Price")
MARTE_Library_BasicNFP_Types_NFP_Weight = Class(name="MARTE::Library::BasicNFP::Types::NFP::Weight")
MARTE_Library_BasicNFP_Types_NFP_Duration = Class(name="MARTE::Library::BasicNFP::Types::NFP::Duration")
MARTE_Library_MARTE_DataTypes_IntegerVector = Class(name="MARTE::Library::MARTE::DataTypes::IntegerVector")
MARTE_Library_MARTE_DataTypes_IntegerMatrix = Class(name="MARTE::Library::MARTE::DataTypes::IntegerMatrix")
IntegerVector = Class(name="IntegerVector")
MARTE_Library_MARTE_DataTypes_IntegerInterval = Class(name="MARTE::Library::MARTE::DataTypes::IntegerInterval")
MARTE_Library_MARTE_DataTypes_UtilityType = Class(name="MARTE::Library::MARTE::DataTypes::UtilityType")
MARTE_Library_MARTE_DataTypes_NFP_NaturalInterval = Class(name="MARTE::Library::MARTE::DataTypes::NFP::NaturalInterval")
MARTE_Library_MARTE_DataTypes_Array = Class(name="MARTE::Library::MARTE::DataTypes::Array")
MARTE_Library_MARTE_DataTypes_Interval = Class(name="MARTE::Library::MARTE::DataTypes::Interval")
MARTE_Library_MARTE_DataTypes_Realnterval = Class(name="MARTE::Library::MARTE::DataTypes::Realnterval")
MARTE_Library_MARTE_DataTypes_NFP_FrequencyInterval = Class(name="MARTE::Library::MARTE::DataTypes::NFP::FrequencyInterval")
NFP_Natural = Class(name="NFP::Natural")
MARTE_Library_MARTE_DataTypes_RealVector = Class(name="MARTE::Library::MARTE::DataTypes::RealVector")
MARTE_Library_MARTE_DataTypes_RealMatrix = Class(name="MARTE::Library::MARTE::DataTypes::RealMatrix")
MARTE_Library_TimeLibrary_TimedValueType = Class(name="MARTE::Library::TimeLibrary::TimedValueType")
MARTE_Library_RS_Library_TilerSpecification = Class(name="MARTE::Library::RS::Library::TilerSpecification")
MARTE_Library_TimeLibrary_IdealClock = Class(name="MARTE::Library::TimeLibrary::IdealClock")
IntegerMatrix = Class(name="IntegerMatrix")
MARTE_Library_RS_Library_ShapeSpecification = Class(name="MARTE::Library::RS::Library::ShapeSpecification")

# MARTE_Library_GRM_BasicTypes_EDF_Parameters class attributes and methods

# NFP_Duration class attributes and methods

# PoolingParameters class attributes and methods

# MARTE_Library_GRM_BasicTypes_SchedParameters class attributes and methods
MARTE_Library_GRM_BasicTypes_SchedParameters_tableEntry: Property = Property(name="tableEntry", type=StringType)
MARTE_Library_GRM_BasicTypes_SchedParameters.attributes={MARTE_Library_GRM_BasicTypes_SchedParameters_tableEntry}

# EDF_Parameters class attributes and methods

# FixedPriorityParameters class attributes and methods

# PeriodicServerParameters class attributes and methods

# MARTE_Library_GRM_BasicTypes_FixedPriorityParameters class attributes and methods

# NFP_Integer class attributes and methods

# MARTE_Library_GRM_BasicTypes_PoolingParameters class attributes and methods

# MARTE_Library_GRM_BasicTypes_PeriodicServerParameters class attributes and methods
MARTE_Library_GRM_BasicTypes_PeriodicServerParameters_kind: Property = Property(name="kind", type=StringType)
MARTE_Library_GRM_BasicTypes_PeriodicServerParameters_backgroundPriority: Property = Property(name="backgroundPriority", type=StringType)
MARTE_Library_GRM_BasicTypes_PeriodicServerParameters.attributes={MARTE_Library_GRM_BasicTypes_PeriodicServerParameters_backgroundPriority, MARTE_Library_GRM_BasicTypes_PeriodicServerParameters_kind}

# MARTE_Library_BasicNFP_Types_NFP_CommonType class attributes and methods
MARTE_Library_BasicNFP_Types_NFP_CommonType_expr: Property = Property(name="expr", type=StringType)
MARTE_Library_BasicNFP_Types_NFP_CommonType_source: Property = Property(name="source", type=StringType)
MARTE_Library_BasicNFP_Types_NFP_CommonType_statQ: Property = Property(name="statQ", type=StringType)
MARTE_Library_BasicNFP_Types_NFP_CommonType_dir: Property = Property(name="dir", type=StringType)
MARTE_Library_BasicNFP_Types_NFP_CommonType_mode: Property = Property(name="mode", type=StringType)
MARTE_Library_BasicNFP_Types_NFP_CommonType_m_bernoulli: Method = Method(name="bernoulli", parameters={Parameter(name='prob')})
MARTE_Library_BasicNFP_Types_NFP_CommonType_m_binomial: Method = Method(name="binomial", parameters={Parameter(name='trials'), Parameter(name='prob')})
MARTE_Library_BasicNFP_Types_NFP_CommonType_m_exp: Method = Method(name="exp", parameters={Parameter(name='mean')})
MARTE_Library_BasicNFP_Types_NFP_CommonType_m_gamma: Method = Method(name="gamma", parameters={Parameter(name='k'), Parameter(name='mean')})
MARTE_Library_BasicNFP_Types_NFP_CommonType_m_normal: Method = Method(name="normal", parameters={Parameter(name='mean'), Parameter(name='standDev')})
MARTE_Library_BasicNFP_Types_NFP_CommonType_m_poisson: Method = Method(name="poisson", parameters={Parameter(name='mean')})
MARTE_Library_BasicNFP_Types_NFP_CommonType_m_uniform: Method = Method(name="uniform", parameters={Parameter(name='max'), Parameter(name='min')})
MARTE_Library_BasicNFP_Types_NFP_CommonType_m_gamma: Method = Method(name="gamma", parameters={Parameter(name='mean'), Parameter(name='k')})
MARTE_Library_BasicNFP_Types_NFP_CommonType_m_geometric: Method = Method(name="geometric", parameters={Parameter(name='p')})
MARTE_Library_BasicNFP_Types_NFP_CommonType_m_triangular: Method = Method(name="triangular", parameters={Parameter(name='max'), Parameter(name='min'), Parameter(name='mode')})
MARTE_Library_BasicNFP_Types_NFP_CommonType_m_logarithmic: Method = Method(name="logarithmic", parameters={Parameter(name='theta')})
MARTE_Library_BasicNFP_Types_NFP_CommonType.attributes={MARTE_Library_BasicNFP_Types_NFP_CommonType_dir, MARTE_Library_BasicNFP_Types_NFP_CommonType_source, MARTE_Library_BasicNFP_Types_NFP_CommonType_statQ, MARTE_Library_BasicNFP_Types_NFP_CommonType_expr, MARTE_Library_BasicNFP_Types_NFP_CommonType_mode}
MARTE_Library_BasicNFP_Types_NFP_CommonType.methods={MARTE_Library_BasicNFP_Types_NFP_CommonType_m_exp, MARTE_Library_BasicNFP_Types_NFP_CommonType_m_gamma, MARTE_Library_BasicNFP_Types_NFP_CommonType_m_triangular, MARTE_Library_BasicNFP_Types_NFP_CommonType_m_bernoulli, MARTE_Library_BasicNFP_Types_NFP_CommonType_m_uniform, MARTE_Library_BasicNFP_Types_NFP_CommonType_m_geometric, MARTE_Library_BasicNFP_Types_NFP_CommonType_m_normal, MARTE_Library_BasicNFP_Types_NFP_CommonType_m_gamma, MARTE_Library_BasicNFP_Types_NFP_CommonType_m_binomial, MARTE_Library_BasicNFP_Types_NFP_CommonType_m_poisson, MARTE_Library_BasicNFP_Types_NFP_CommonType_m_logarithmic}

# MARTE_Library_BasicNFP_Types_NFP_Boolean class attributes and methods
MARTE_Library_BasicNFP_Types_NFP_Boolean_value: Property = Property(name="value", type=StringType)
MARTE_Library_BasicNFP_Types_NFP_Boolean.attributes={MARTE_Library_BasicNFP_Types_NFP_Boolean_value}

# MARTE_Library_BasicNFP_Types_NFP_Frequency class attributes and methods
MARTE_Library_BasicNFP_Types_NFP_Frequency_unit: Property = Property(name="unit", type=StringType)
MARTE_Library_BasicNFP_Types_NFP_Frequency_precision: Property = Property(name="precision", type=StringType)
MARTE_Library_BasicNFP_Types_NFP_Frequency.attributes={MARTE_Library_BasicNFP_Types_NFP_Frequency_unit, MARTE_Library_BasicNFP_Types_NFP_Frequency_precision}

# NFP_Real class attributes and methods

# MARTE_Library_BasicNFP_Types_NFP_Real class attributes and methods
MARTE_Library_BasicNFP_Types_NFP_Real_value: Property = Property(name="value", type=StringType)
MARTE_Library_BasicNFP_Types_NFP_Real.attributes={MARTE_Library_BasicNFP_Types_NFP_Real_value}

# NFP_CommonType class attributes and methods

# MARTE_Library_BasicNFP_Types_NFP_Natural class attributes and methods
MARTE_Library_BasicNFP_Types_NFP_Natural_value: Property = Property(name="value", type=StringType)
MARTE_Library_BasicNFP_Types_NFP_Natural.attributes={MARTE_Library_BasicNFP_Types_NFP_Natural_value}

# MARTE_Library_BasicNFP_Types_NFP_Energy class attributes and methods
MARTE_Library_BasicNFP_Types_NFP_Energy_unit: Property = Property(name="unit", type=StringType)
MARTE_Library_BasicNFP_Types_NFP_Energy_precision: Property = Property(name="precision", type=StringType)
MARTE_Library_BasicNFP_Types_NFP_Energy.attributes={MARTE_Library_BasicNFP_Types_NFP_Energy_precision, MARTE_Library_BasicNFP_Types_NFP_Energy_unit}

# MARTE_Library_BasicNFP_Types_NFP_String class attributes and methods
MARTE_Library_BasicNFP_Types_NFP_String_value: Property = Property(name="value", type=StringType)
MARTE_Library_BasicNFP_Types_NFP_String.attributes={MARTE_Library_BasicNFP_Types_NFP_String_value}

# MARTE_Library_BasicNFP_Types_NFP_Integer class attributes and methods
MARTE_Library_BasicNFP_Types_NFP_Integer_value: Property = Property(name="value", type=StringType)
MARTE_Library_BasicNFP_Types_NFP_Integer.attributes={MARTE_Library_BasicNFP_Types_NFP_Integer_value}

# MARTE_Library_BasicNFP_Types_NFP_DateTime class attributes and methods
MARTE_Library_BasicNFP_Types_NFP_DateTime_value: Property = Property(name="value", type=StringType)
MARTE_Library_BasicNFP_Types_NFP_DateTime.attributes={MARTE_Library_BasicNFP_Types_NFP_DateTime_value}

# MARTE_Library_BasicNFP_Types_NFP_DataTxRate class attributes and methods
MARTE_Library_BasicNFP_Types_NFP_DataTxRate_unit: Property = Property(name="unit", type=StringType)
MARTE_Library_BasicNFP_Types_NFP_DataTxRate_precision: Property = Property(name="precision", type=StringType)
MARTE_Library_BasicNFP_Types_NFP_DataTxRate.attributes={MARTE_Library_BasicNFP_Types_NFP_DataTxRate_unit, MARTE_Library_BasicNFP_Types_NFP_DataTxRate_precision}

# MARTE_Library_BasicNFP_Types_NFP_Power class attributes and methods
MARTE_Library_BasicNFP_Types_NFP_Power_unit: Property = Property(name="unit", type=StringType)
MARTE_Library_BasicNFP_Types_NFP_Power_precision: Property = Property(name="precision", type=StringType)
MARTE_Library_BasicNFP_Types_NFP_Power.attributes={MARTE_Library_BasicNFP_Types_NFP_Power_precision, MARTE_Library_BasicNFP_Types_NFP_Power_unit}

# MARTE_Library_BasicNFP_Types_NFP_DataSize class attributes and methods
MARTE_Library_BasicNFP_Types_NFP_DataSize_unit: Property = Property(name="unit", type=StringType)
MARTE_Library_BasicNFP_Types_NFP_DataSize_precision: Property = Property(name="precision", type=StringType)
MARTE_Library_BasicNFP_Types_NFP_DataSize.attributes={MARTE_Library_BasicNFP_Types_NFP_DataSize_precision, MARTE_Library_BasicNFP_Types_NFP_DataSize_unit}

# SporadicPattern class attributes and methods

# MARTE_Library_BasicNFP_Types_NFP_Length class attributes and methods
MARTE_Library_BasicNFP_Types_NFP_Length_unit: Property = Property(name="unit", type=StringType)
MARTE_Library_BasicNFP_Types_NFP_Length_precision: Property = Property(name="precision", type=StringType)
MARTE_Library_BasicNFP_Types_NFP_Length.attributes={MARTE_Library_BasicNFP_Types_NFP_Length_unit, MARTE_Library_BasicNFP_Types_NFP_Length_precision}

# MARTE_Library_BasicNFP_Types_NFP_Area class attributes and methods
MARTE_Library_BasicNFP_Types_NFP_Area_unit: Property = Property(name="unit", type=StringType)
MARTE_Library_BasicNFP_Types_NFP_Area_precision: Property = Property(name="precision", type=StringType)
MARTE_Library_BasicNFP_Types_NFP_Area.attributes={MARTE_Library_BasicNFP_Types_NFP_Area_precision, MARTE_Library_BasicNFP_Types_NFP_Area_unit}

# MARTE_Library_BasicNFP_Types_ArrivalPattern class attributes and methods

# PeriodicPattern class attributes and methods

# AperiodicPattern class attributes and methods

# BurstPattern class attributes and methods

# IrregularPattern class attributes and methods

# ClosedPattern class attributes and methods

# OpenPattern class attributes and methods

# MARTE_Library_BasicNFP_Types_PeriodicPattern class attributes and methods

# MARTE_Library_BasicNFP_Types_AperiodicPattern class attributes and methods

# MARTE_Library_BasicNFP_Types_BurstPattern class attributes and methods

# MARTE_Library_BasicNFP_Types_IrregularPattern class attributes and methods

# MARTE_Library_BasicNFP_Types_ClosedPattern class attributes and methods

# MARTE_Library_BasicNFP_Types_SporadicPattern class attributes and methods

# MARTE_Library_BasicNFP_Types_OpenPattern class attributes and methods
MARTE_Library_BasicNFP_Types_OpenPattern_arrivalProcess: Property = Property(name="arrivalProcess", type=StringType)
MARTE_Library_BasicNFP_Types_OpenPattern.attributes={MARTE_Library_BasicNFP_Types_OpenPattern_arrivalProcess}

# NFP_Frequency class attributes and methods

# MARTE_Library_BasicNFP_Types_NFP_Percentage class attributes and methods
MARTE_Library_BasicNFP_Types_NFP_Percentage_unit: Property = Property(name="unit", type=StringType)
MARTE_Library_BasicNFP_Types_NFP_Percentage.attributes={MARTE_Library_BasicNFP_Types_NFP_Percentage_unit}

# MARTE_Library_BasicNFP_Types_NFP_Price class attributes and methods
MARTE_Library_BasicNFP_Types_NFP_Price_unit: Property = Property(name="unit", type=StringType)
MARTE_Library_BasicNFP_Types_NFP_Price.attributes={MARTE_Library_BasicNFP_Types_NFP_Price_unit}

# MARTE_Library_BasicNFP_Types_NFP_Weight class attributes and methods
MARTE_Library_BasicNFP_Types_NFP_Weight_unit: Property = Property(name="unit", type=StringType)
MARTE_Library_BasicNFP_Types_NFP_Weight_precision: Property = Property(name="precision", type=StringType)
MARTE_Library_BasicNFP_Types_NFP_Weight.attributes={MARTE_Library_BasicNFP_Types_NFP_Weight_precision, MARTE_Library_BasicNFP_Types_NFP_Weight_unit}

# MARTE_Library_BasicNFP_Types_NFP_Duration class attributes and methods
MARTE_Library_BasicNFP_Types_NFP_Duration_unit: Property = Property(name="unit", type=StringType)
MARTE_Library_BasicNFP_Types_NFP_Duration_clock: Property = Property(name="clock", type=StringType)
MARTE_Library_BasicNFP_Types_NFP_Duration_precision: Property = Property(name="precision", type=StringType)
MARTE_Library_BasicNFP_Types_NFP_Duration_worst: Property = Property(name="worst", type=StringType)
MARTE_Library_BasicNFP_Types_NFP_Duration_best: Property = Property(name="best", type=StringType)
MARTE_Library_BasicNFP_Types_NFP_Duration.attributes={MARTE_Library_BasicNFP_Types_NFP_Duration_clock, MARTE_Library_BasicNFP_Types_NFP_Duration_worst, MARTE_Library_BasicNFP_Types_NFP_Duration_unit, MARTE_Library_BasicNFP_Types_NFP_Duration_best, MARTE_Library_BasicNFP_Types_NFP_Duration_precision}

# MARTE_Library_MARTE_DataTypes_IntegerVector class attributes and methods
MARTE_Library_MARTE_DataTypes_IntegerVector_vectorElem: Property = Property(name="vectorElem", type=StringType)
MARTE_Library_MARTE_DataTypes_IntegerVector_m_at: Method = Method(name="at", parameters={Parameter(name='i')}, type=StringType)
MARTE_Library_MARTE_DataTypes_IntegerVector.attributes={MARTE_Library_MARTE_DataTypes_IntegerVector_vectorElem}
MARTE_Library_MARTE_DataTypes_IntegerVector.methods={MARTE_Library_MARTE_DataTypes_IntegerVector_m_at}

# MARTE_Library_MARTE_DataTypes_IntegerMatrix class attributes and methods
MARTE_Library_MARTE_DataTypes_IntegerMatrix_m_at: Method = Method(name="at", parameters={Parameter(name='i')}, type=StringType)
MARTE_Library_MARTE_DataTypes_IntegerMatrix.methods={MARTE_Library_MARTE_DataTypes_IntegerMatrix_m_at}

# IntegerVector class attributes and methods

# MARTE_Library_MARTE_DataTypes_IntegerInterval class attributes and methods
MARTE_Library_MARTE_DataTypes_IntegerInterval_bound: Property = Property(name="bound", type=StringType)
MARTE_Library_MARTE_DataTypes_IntegerInterval.attributes={MARTE_Library_MARTE_DataTypes_IntegerInterval_bound}

# MARTE_Library_MARTE_DataTypes_UtilityType class attributes and methods
MARTE_Library_MARTE_DataTypes_UtilityType_m_le: Method = Method(name="le", parameters={Parameter(name='u')}, type=StringType)
MARTE_Library_MARTE_DataTypes_UtilityType_m_eq: Method = Method(name="eq", parameters={Parameter(name='u')}, type=StringType)
MARTE_Library_MARTE_DataTypes_UtilityType_m_lt: Method = Method(name="lt", parameters={Parameter(name='u')}, type=StringType)
MARTE_Library_MARTE_DataTypes_UtilityType_m_gt: Method = Method(name="gt", parameters={Parameter(name='u')}, type=StringType)
MARTE_Library_MARTE_DataTypes_UtilityType_m_ge: Method = Method(name="ge", parameters={Parameter(name='u')}, type=StringType)
MARTE_Library_MARTE_DataTypes_UtilityType_m_ne: Method = Method(name="ne", parameters={Parameter(name='u')}, type=StringType)
MARTE_Library_MARTE_DataTypes_UtilityType.methods={MARTE_Library_MARTE_DataTypes_UtilityType_m_le, MARTE_Library_MARTE_DataTypes_UtilityType_m_lt, MARTE_Library_MARTE_DataTypes_UtilityType_m_gt, MARTE_Library_MARTE_DataTypes_UtilityType_m_ne, MARTE_Library_MARTE_DataTypes_UtilityType_m_ge, MARTE_Library_MARTE_DataTypes_UtilityType_m_eq}

# MARTE_Library_MARTE_DataTypes_NFP_NaturalInterval class attributes and methods

# MARTE_Library_MARTE_DataTypes_Array class attributes and methods
MARTE_Library_MARTE_DataTypes_Array_m_at: Method = Method(name="at", parameters={Parameter(name='i')})
MARTE_Library_MARTE_DataTypes_Array.methods={MARTE_Library_MARTE_DataTypes_Array_m_at}

# MARTE_Library_MARTE_DataTypes_Interval class attributes and methods

# MARTE_Library_MARTE_DataTypes_Realnterval class attributes and methods
MARTE_Library_MARTE_DataTypes_Realnterval_bound: Property = Property(name="bound", type=StringType)
MARTE_Library_MARTE_DataTypes_Realnterval.attributes={MARTE_Library_MARTE_DataTypes_Realnterval_bound}

# MARTE_Library_MARTE_DataTypes_NFP_FrequencyInterval class attributes and methods

# NFP_Natural class attributes and methods

# MARTE_Library_MARTE_DataTypes_RealVector class attributes and methods
MARTE_Library_MARTE_DataTypes_RealVector_vectorElem: Property = Property(name="vectorElem", type=StringType)
MARTE_Library_MARTE_DataTypes_RealVector_m_at: Method = Method(name="at", parameters={Parameter(name='i')}, type=StringType)
MARTE_Library_MARTE_DataTypes_RealVector.attributes={MARTE_Library_MARTE_DataTypes_RealVector_vectorElem}
MARTE_Library_MARTE_DataTypes_RealVector.methods={MARTE_Library_MARTE_DataTypes_RealVector_m_at}

# MARTE_Library_MARTE_DataTypes_RealMatrix class attributes and methods
MARTE_Library_MARTE_DataTypes_RealMatrix_matrixElem: Property = Property(name="matrixElem", type=StringType)
MARTE_Library_MARTE_DataTypes_RealMatrix_m_at: Method = Method(name="at", parameters={Parameter(name='i'), Parameter(name='p')})
MARTE_Library_MARTE_DataTypes_RealMatrix.attributes={MARTE_Library_MARTE_DataTypes_RealMatrix_matrixElem}
MARTE_Library_MARTE_DataTypes_RealMatrix.methods={MARTE_Library_MARTE_DataTypes_RealMatrix_m_at}

# MARTE_Library_TimeLibrary_TimedValueType class attributes and methods
MARTE_Library_TimeLibrary_TimedValueType_onClock: Property = Property(name="onClock", type=StringType)
MARTE_Library_TimeLibrary_TimedValueType_unit: Property = Property(name="unit", type=StringType)
MARTE_Library_TimeLibrary_TimedValueType_value: Property = Property(name="value", type=StringType)
MARTE_Library_TimeLibrary_TimedValueType_expr: Property = Property(name="expr", type=StringType)
MARTE_Library_TimeLibrary_TimedValueType.attributes={MARTE_Library_TimeLibrary_TimedValueType_unit, MARTE_Library_TimeLibrary_TimedValueType_expr, MARTE_Library_TimeLibrary_TimedValueType_onClock, MARTE_Library_TimeLibrary_TimedValueType_value}

# MARTE_Library_RS_Library_TilerSpecification class attributes and methods

# MARTE_Library_TimeLibrary_IdealClock class attributes and methods
MARTE_Library_TimeLibrary_IdealClock_m_currentTime: Method = Method(name="currentTime", parameters={}, type=StringType)
MARTE_Library_TimeLibrary_IdealClock.methods={MARTE_Library_TimeLibrary_IdealClock_m_currentTime}

# IntegerMatrix class attributes and methods

# MARTE_Library_RS_Library_ShapeSpecification class attributes and methods
MARTE_Library_RS_Library_ShapeSpecification_size: Property = Property(name="size", type=StringType)
MARTE_Library_RS_Library_ShapeSpecification.attributes={MARTE_Library_RS_Library_ShapeSpecification_size}

# Relationships
deadline0: BinaryAssociation = BinaryAssociation(
    name="deadline0",
    ends={
        Property(name="NFP_Duration", type=MARTE_Library_GRM_BasicTypes_EDF_Parameters, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_Library_GRM_BasicTypes_EDF_Parameters", type=NFP_Duration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
edf1: BinaryAssociation = BinaryAssociation(
    name="edf1",
    ends={
        Property(name="EDF_Parameters", type=MARTE_Library_GRM_BasicTypes_SchedParameters, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_Library_GRM_BasicTypes_SchedParameters", type=EDF_Parameters, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
fp2: BinaryAssociation = BinaryAssociation(
    name="fp2",
    ends={
        Property(name="FixedPriorityParameters", type=MARTE_Library_GRM_BasicTypes_SchedParameters, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_Library_GRM_BasicTypes_SchedParameters3", type=FixedPriorityParameters, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
replenishPeriod16: BinaryAssociation = BinaryAssociation(
    name="replenishPeriod16",
    ends={
        Property(name="NFP_Duration18", type=MARTE_Library_GRM_BasicTypes_PeriodicServerParameters, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_Library_GRM_BasicTypes_PeriodicServerParameters17", type=NFP_Duration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
pooling4: BinaryAssociation = BinaryAssociation(
    name="pooling4",
    ends={
        Property(name="PoolingParameters", type=MARTE_Library_GRM_BasicTypes_SchedParameters, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_Library_GRM_BasicTypes_SchedParameters5", type=PoolingParameters, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
server6: BinaryAssociation = BinaryAssociation(
    name="server6",
    ends={
        Property(name="PeriodicServerParameters", type=MARTE_Library_GRM_BasicTypes_SchedParameters, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_Library_GRM_BasicTypes_SchedParameters7", type=PeriodicServerParameters, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
priority8: BinaryAssociation = BinaryAssociation(
    name="priority8",
    ends={
        Property(name="NFP_Integer", type=MARTE_Library_GRM_BasicTypes_FixedPriorityParameters, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_Library_GRM_BasicTypes_FixedPriorityParameters", type=NFP_Integer, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
period9: BinaryAssociation = BinaryAssociation(
    name="period9",
    ends={
        Property(name="NFP_Duration10", type=MARTE_Library_GRM_BasicTypes_PoolingParameters, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_Library_GRM_BasicTypes_PoolingParameters", type=NFP_Duration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
overhead11: BinaryAssociation = BinaryAssociation(
    name="overhead11",
    ends={
        Property(name="NFP_Duration13", type=MARTE_Library_GRM_BasicTypes_PoolingParameters, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_Library_GRM_BasicTypes_PoolingParameters12", type=NFP_Duration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
initialBudget14: BinaryAssociation = BinaryAssociation(
    name="initialBudget14",
    ends={
        Property(name="NFP_Duration15", type=MARTE_Library_GRM_BasicTypes_PeriodicServerParameters, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_Library_GRM_BasicTypes_PeriodicServerParameters", type=NFP_Duration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
maxPendingReplenish19: BinaryAssociation = BinaryAssociation(
    name="maxPendingReplenish19",
    ends={
        Property(name="NFP_Integer21", type=MARTE_Library_GRM_BasicTypes_PeriodicServerParameters, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_Library_GRM_BasicTypes_PeriodicServerParameters20", type=NFP_Integer, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
sporadic31: BinaryAssociation = BinaryAssociation(
    name="sporadic31",
    ends={
        Property(name="SporadicPattern", type=MARTE_Library_BasicNFP_Types_ArrivalPattern, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_Library_BasicNFP_Types_ArrivalPattern32", type=SporadicPattern, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
periodic22: BinaryAssociation = BinaryAssociation(
    name="periodic22",
    ends={
        Property(name="PeriodicPattern", type=MARTE_Library_BasicNFP_Types_ArrivalPattern, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_Library_BasicNFP_Types_ArrivalPattern", type=PeriodicPattern, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
aperiodic23: BinaryAssociation = BinaryAssociation(
    name="aperiodic23",
    ends={
        Property(name="AperiodicPattern", type=MARTE_Library_BasicNFP_Types_ArrivalPattern, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_Library_BasicNFP_Types_ArrivalPattern24", type=AperiodicPattern, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
burst25: BinaryAssociation = BinaryAssociation(
    name="burst25",
    ends={
        Property(name="BurstPattern", type=MARTE_Library_BasicNFP_Types_ArrivalPattern, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_Library_BasicNFP_Types_ArrivalPattern26", type=BurstPattern, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
irregular27: BinaryAssociation = BinaryAssociation(
    name="irregular27",
    ends={
        Property(name="IrregularPattern", type=MARTE_Library_BasicNFP_Types_ArrivalPattern, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_Library_BasicNFP_Types_ArrivalPattern28", type=IrregularPattern, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
closed29: BinaryAssociation = BinaryAssociation(
    name="closed29",
    ends={
        Property(name="ClosedPattern", type=MARTE_Library_BasicNFP_Types_ArrivalPattern, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_Library_BasicNFP_Types_ArrivalPattern30", type=ClosedPattern, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
minEventInterval52: BinaryAssociation = BinaryAssociation(
    name="minEventInterval52",
    ends={
        Property(name="NFP_Duration54", type=MARTE_Library_BasicNFP_Types_BurstPattern, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_Library_BasicNFP_Types_BurstPattern53", type=NFP_Duration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
open33: BinaryAssociation = BinaryAssociation(
    name="open33",
    ends={
        Property(name="OpenPattern", type=MARTE_Library_BasicNFP_Types_ArrivalPattern, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_Library_BasicNFP_Types_ArrivalPattern34", type=OpenPattern, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
period35: BinaryAssociation = BinaryAssociation(
    name="period35",
    ends={
        Property(name="NFP_Duration36", type=MARTE_Library_BasicNFP_Types_PeriodicPattern, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_Library_BasicNFP_Types_PeriodicPattern", type=NFP_Duration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
jitter37: BinaryAssociation = BinaryAssociation(
    name="jitter37",
    ends={
        Property(name="NFP_Duration39", type=MARTE_Library_BasicNFP_Types_PeriodicPattern, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_Library_BasicNFP_Types_PeriodicPattern38", type=NFP_Duration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
phase40: BinaryAssociation = BinaryAssociation(
    name="phase40",
    ends={
        Property(name="NFP_Duration42", type=MARTE_Library_BasicNFP_Types_PeriodicPattern, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_Library_BasicNFP_Types_PeriodicPattern41", type=NFP_Duration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
occurrences43: BinaryAssociation = BinaryAssociation(
    name="occurrences43",
    ends={
        Property(name="NFP_Integer45", type=MARTE_Library_BasicNFP_Types_PeriodicPattern, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_Library_BasicNFP_Types_PeriodicPattern44", type=NFP_Integer, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
distribution46: BinaryAssociation = BinaryAssociation(
    name="distribution46",
    ends={
        Property(name="NFP_CommonType", type=MARTE_Library_BasicNFP_Types_AperiodicPattern, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_Library_BasicNFP_Types_AperiodicPattern", type=NFP_CommonType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
minInterarrival47: BinaryAssociation = BinaryAssociation(
    name="minInterarrival47",
    ends={
        Property(name="NFP_Duration48", type=MARTE_Library_BasicNFP_Types_BurstPattern, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_Library_BasicNFP_Types_BurstPattern", type=NFP_Duration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
maxInterarrival49: BinaryAssociation = BinaryAssociation(
    name="maxInterarrival49",
    ends={
        Property(name="NFP_Duration51", type=MARTE_Library_BasicNFP_Types_BurstPattern, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_Library_BasicNFP_Types_BurstPattern50", type=NFP_Duration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
maxInterarrival73: BinaryAssociation = BinaryAssociation(
    name="maxInterarrival73",
    ends={
        Property(name="NFP_Duration75", type=MARTE_Library_BasicNFP_Types_SporadicPattern, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_Library_BasicNFP_Types_SporadicPattern74", type=NFP_Duration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
maxEventInterval55: BinaryAssociation = BinaryAssociation(
    name="maxEventInterval55",
    ends={
        Property(name="NFP_Duration57", type=MARTE_Library_BasicNFP_Types_BurstPattern, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_Library_BasicNFP_Types_BurstPattern56", type=NFP_Duration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
burstSize58: BinaryAssociation = BinaryAssociation(
    name="burstSize58",
    ends={
        Property(name="NFP_Integer60", type=MARTE_Library_BasicNFP_Types_BurstPattern, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_Library_BasicNFP_Types_BurstPattern59", type=NFP_Integer, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
phase61: BinaryAssociation = BinaryAssociation(
    name="phase61",
    ends={
        Property(name="NFP_Duration62", type=MARTE_Library_BasicNFP_Types_IrregularPattern, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_Library_BasicNFP_Types_IrregularPattern", type=NFP_Duration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
interarrivals63: BinaryAssociation = BinaryAssociation(
    name="interarrivals63",
    ends={
        Property(name="NFP_Duration65", type=MARTE_Library_BasicNFP_Types_IrregularPattern, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_Library_BasicNFP_Types_IrregularPattern64", type=NFP_Duration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
population66: BinaryAssociation = BinaryAssociation(
    name="population66",
    ends={
        Property(name="NFP_Integer67", type=MARTE_Library_BasicNFP_Types_ClosedPattern, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_Library_BasicNFP_Types_ClosedPattern", type=NFP_Integer, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
extDelay68: BinaryAssociation = BinaryAssociation(
    name="extDelay68",
    ends={
        Property(name="NFP_Duration70", type=MARTE_Library_BasicNFP_Types_ClosedPattern, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_Library_BasicNFP_Types_ClosedPattern69", type=NFP_Duration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
minInterarrival71: BinaryAssociation = BinaryAssociation(
    name="minInterarrival71",
    ends={
        Property(name="NFP_Duration72", type=MARTE_Library_BasicNFP_Types_SporadicPattern, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_Library_BasicNFP_Types_SporadicPattern", type=NFP_Duration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
jitter76: BinaryAssociation = BinaryAssociation(
    name="jitter76",
    ends={
        Property(name="NFP_Duration78", type=MARTE_Library_BasicNFP_Types_SporadicPattern, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_Library_BasicNFP_Types_SporadicPattern77", type=NFP_Duration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
interArrivalTime79: BinaryAssociation = BinaryAssociation(
    name="interArrivalTime79",
    ends={
        Property(name="NFP_Duration80", type=MARTE_Library_BasicNFP_Types_OpenPattern, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_Library_BasicNFP_Types_OpenPattern", type=NFP_Duration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
arrivalRate81: BinaryAssociation = BinaryAssociation(
    name="arrivalRate81",
    ends={
        Property(name="NFP_Frequency", type=MARTE_Library_BasicNFP_Types_OpenPattern, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_Library_BasicNFP_Types_OpenPattern82", type=NFP_Frequency, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
matrixElem83: BinaryAssociation = BinaryAssociation(
    name="matrixElem83",
    ends={
        Property(name="IntegerVector", type=MARTE_Library_MARTE_DataTypes_IntegerMatrix, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_Library_MARTE_DataTypes_IntegerMatrix", type=IntegerVector, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
bound84: BinaryAssociation = BinaryAssociation(
    name="bound84",
    ends={
        Property(name="NFP_Frequency85", type=MARTE_Library_MARTE_DataTypes_NFP_FrequencyInterval, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_Library_MARTE_DataTypes_NFP_FrequencyInterval", type=NFP_Frequency, multiplicity=Multiplicity(2, 2), is_composite=True)
    }
)
bound86: BinaryAssociation = BinaryAssociation(
    name="bound86",
    ends={
        Property(name="NFP_Natural", type=MARTE_Library_MARTE_DataTypes_NFP_NaturalInterval, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_Library_MARTE_DataTypes_NFP_NaturalInterval", type=NFP_Natural, multiplicity=Multiplicity(2, 2), is_composite=True)
    }
)
origin87: BinaryAssociation = BinaryAssociation(
    name="origin87",
    ends={
        Property(name="IntegerVector88", type=MARTE_Library_RS_Library_TilerSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_Library_RS_Library_TilerSpecification", type=IntegerVector, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
paving89: BinaryAssociation = BinaryAssociation(
    name="paving89",
    ends={
        Property(name="IntegerMatrix", type=MARTE_Library_RS_Library_TilerSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_Library_RS_Library_TilerSpecification90", type=IntegerMatrix, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
fitting91: BinaryAssociation = BinaryAssociation(
    name="fitting91",
    ends={
        Property(name="IntegerVector93", type=MARTE_Library_RS_Library_TilerSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_Library_RS_Library_TilerSpecification92", type=IntegerVector, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_MARTE_Library_GRM_BasicTypes_PoolingParameters_FixedPriorityParameters = Generalization(general=FixedPriorityParameters, specific=MARTE_Library_GRM_BasicTypes_PoolingParameters)
gen_MARTE_Library_GRM_BasicTypes_PeriodicServerParameters_FixedPriorityParameters = Generalization(general=FixedPriorityParameters, specific=MARTE_Library_GRM_BasicTypes_PeriodicServerParameters)
gen_MARTE_Library_BasicNFP_Types_NFP_Boolean_NFP_CommonType = Generalization(general=NFP_CommonType, specific=MARTE_Library_BasicNFP_Types_NFP_Boolean)
gen_MARTE_Library_BasicNFP_Types_NFP_Frequency_NFP_Real = Generalization(general=NFP_Real, specific=MARTE_Library_BasicNFP_Types_NFP_Frequency)
gen_MARTE_Library_BasicNFP_Types_NFP_Real_NFP_CommonType = Generalization(general=NFP_CommonType, specific=MARTE_Library_BasicNFP_Types_NFP_Real)
gen_MARTE_Library_BasicNFP_Types_NFP_Natural_NFP_CommonType = Generalization(general=NFP_CommonType, specific=MARTE_Library_BasicNFP_Types_NFP_Natural)
gen_MARTE_Library_BasicNFP_Types_NFP_Energy_NFP_Real = Generalization(general=NFP_Real, specific=MARTE_Library_BasicNFP_Types_NFP_Energy)
gen_MARTE_Library_BasicNFP_Types_NFP_String_NFP_CommonType = Generalization(general=NFP_CommonType, specific=MARTE_Library_BasicNFP_Types_NFP_String)
gen_MARTE_Library_BasicNFP_Types_NFP_Integer_NFP_CommonType = Generalization(general=NFP_CommonType, specific=MARTE_Library_BasicNFP_Types_NFP_Integer)
gen_MARTE_Library_BasicNFP_Types_NFP_DateTime_NFP_CommonType = Generalization(general=NFP_CommonType, specific=MARTE_Library_BasicNFP_Types_NFP_DateTime)
gen_MARTE_Library_BasicNFP_Types_NFP_DataTxRate_NFP_Real = Generalization(general=NFP_Real, specific=MARTE_Library_BasicNFP_Types_NFP_DataTxRate)
gen_MARTE_Library_BasicNFP_Types_NFP_Power_NFP_Real = Generalization(general=NFP_Real, specific=MARTE_Library_BasicNFP_Types_NFP_Power)
gen_MARTE_Library_BasicNFP_Types_NFP_DataSize_NFP_Real = Generalization(general=NFP_Real, specific=MARTE_Library_BasicNFP_Types_NFP_DataSize)
gen_MARTE_Library_BasicNFP_Types_NFP_Length_NFP_Real = Generalization(general=NFP_Real, specific=MARTE_Library_BasicNFP_Types_NFP_Length)
gen_MARTE_Library_BasicNFP_Types_NFP_Area_NFP_Real = Generalization(general=NFP_Real, specific=MARTE_Library_BasicNFP_Types_NFP_Area)
gen_MARTE_Library_BasicNFP_Types_BurstPattern_AperiodicPattern = Generalization(general=AperiodicPattern, specific=MARTE_Library_BasicNFP_Types_BurstPattern)
gen_MARTE_Library_BasicNFP_Types_IrregularPattern_AperiodicPattern = Generalization(general=AperiodicPattern, specific=MARTE_Library_BasicNFP_Types_IrregularPattern)
gen_MARTE_Library_BasicNFP_Types_SporadicPattern_AperiodicPattern = Generalization(general=AperiodicPattern, specific=MARTE_Library_BasicNFP_Types_SporadicPattern)
gen_MARTE_Library_BasicNFP_Types_NFP_Percentage_NFP_Real = Generalization(general=NFP_Real, specific=MARTE_Library_BasicNFP_Types_NFP_Percentage)
gen_MARTE_Library_BasicNFP_Types_NFP_Price_NFP_Real = Generalization(general=NFP_Real, specific=MARTE_Library_BasicNFP_Types_NFP_Price)
gen_MARTE_Library_BasicNFP_Types_NFP_Weight_NFP_Real = Generalization(general=NFP_Real, specific=MARTE_Library_BasicNFP_Types_NFP_Weight)
gen_MARTE_Library_BasicNFP_Types_NFP_Duration_NFP_Real = Generalization(general=NFP_Real, specific=MARTE_Library_BasicNFP_Types_NFP_Duration)

# Domain Model
domain_model = DomainModel(
    name="MARTE_Library",
    types={MARTE_Library_GRM_BasicTypes_EDF_Parameters, NFP_Duration, PoolingParameters, MARTE_Library_GRM_BasicTypes_SchedParameters, EDF_Parameters, FixedPriorityParameters, PeriodicServerParameters, MARTE_Library_GRM_BasicTypes_FixedPriorityParameters, NFP_Integer, MARTE_Library_GRM_BasicTypes_PoolingParameters, MARTE_Library_GRM_BasicTypes_PeriodicServerParameters, MARTE_Library_BasicNFP_Types_NFP_CommonType, MARTE_Library_BasicNFP_Types_NFP_Boolean, MARTE_Library_BasicNFP_Types_NFP_Frequency, NFP_Real, MARTE_Library_BasicNFP_Types_NFP_Real, NFP_CommonType, MARTE_Library_BasicNFP_Types_NFP_Natural, MARTE_Library_BasicNFP_Types_NFP_Energy, MARTE_Library_BasicNFP_Types_NFP_String, MARTE_Library_BasicNFP_Types_NFP_Integer, MARTE_Library_BasicNFP_Types_NFP_DateTime, MARTE_Library_BasicNFP_Types_NFP_DataTxRate, MARTE_Library_BasicNFP_Types_NFP_Power, MARTE_Library_BasicNFP_Types_NFP_DataSize, SporadicPattern, MARTE_Library_BasicNFP_Types_NFP_Length, MARTE_Library_BasicNFP_Types_NFP_Area, MARTE_Library_BasicNFP_Types_ArrivalPattern, PeriodicPattern, AperiodicPattern, BurstPattern, IrregularPattern, ClosedPattern, OpenPattern, MARTE_Library_BasicNFP_Types_PeriodicPattern, MARTE_Library_BasicNFP_Types_AperiodicPattern, MARTE_Library_BasicNFP_Types_BurstPattern, MARTE_Library_BasicNFP_Types_IrregularPattern, MARTE_Library_BasicNFP_Types_ClosedPattern, MARTE_Library_BasicNFP_Types_SporadicPattern, MARTE_Library_BasicNFP_Types_OpenPattern, NFP_Frequency, MARTE_Library_BasicNFP_Types_NFP_Percentage, MARTE_Library_BasicNFP_Types_NFP_Price, MARTE_Library_BasicNFP_Types_NFP_Weight, MARTE_Library_BasicNFP_Types_NFP_Duration, MARTE_Library_MARTE_DataTypes_IntegerVector, MARTE_Library_MARTE_DataTypes_IntegerMatrix, IntegerVector, MARTE_Library_MARTE_DataTypes_IntegerInterval, MARTE_Library_MARTE_DataTypes_UtilityType, MARTE_Library_MARTE_DataTypes_NFP_NaturalInterval, MARTE_Library_MARTE_DataTypes_Array, MARTE_Library_MARTE_DataTypes_Interval, MARTE_Library_MARTE_DataTypes_Realnterval, MARTE_Library_MARTE_DataTypes_NFP_FrequencyInterval, NFP_Natural, MARTE_Library_MARTE_DataTypes_RealVector, MARTE_Library_MARTE_DataTypes_RealMatrix, MARTE_Library_TimeLibrary_TimedValueType, MARTE_Library_RS_Library_TilerSpecification, MARTE_Library_TimeLibrary_IdealClock, IntegerMatrix, MARTE_Library_RS_Library_ShapeSpecification, DataSizeUnitKind, PowerUnitKind, FrequencyUnitKind, DataTxRateUnitKind, EnergyUnitKind, LengthUnitKind, AreaUnitKind, WeightUnitKind, SchedPolicyKind, ProtectProtocolKind, PeriodicServerKind, SourceKind, DirectionKind, StatisticalQualifierKind, TransmModeKind, TimeNatureKind, TimeInterpretationKind, EventKind, TimeStandardKind, TUK, TimeUnitKind, LogicalTimeUnit},
    associations={deadline0, edf1, fp2, replenishPeriod16, pooling4, server6, priority8, period9, overhead11, initialBudget14, maxPendingReplenish19, sporadic31, periodic22, aperiodic23, burst25, irregular27, closed29, minEventInterval52, open33, period35, jitter37, phase40, occurrences43, distribution46, minInterarrival47, maxInterarrival49, maxInterarrival73, maxEventInterval55, burstSize58, phase61, interarrivals63, population66, extDelay68, minInterarrival71, jitter76, interArrivalTime79, arrivalRate81, matrixElem83, bound84, bound86, origin87, paving89, fitting91},
    generalizations={gen_MARTE_Library_GRM_BasicTypes_PoolingParameters_FixedPriorityParameters, gen_MARTE_Library_GRM_BasicTypes_PeriodicServerParameters_FixedPriorityParameters, gen_MARTE_Library_BasicNFP_Types_NFP_Boolean_NFP_CommonType, gen_MARTE_Library_BasicNFP_Types_NFP_Frequency_NFP_Real, gen_MARTE_Library_BasicNFP_Types_NFP_Real_NFP_CommonType, gen_MARTE_Library_BasicNFP_Types_NFP_Natural_NFP_CommonType, gen_MARTE_Library_BasicNFP_Types_NFP_Energy_NFP_Real, gen_MARTE_Library_BasicNFP_Types_NFP_String_NFP_CommonType, gen_MARTE_Library_BasicNFP_Types_NFP_Integer_NFP_CommonType, gen_MARTE_Library_BasicNFP_Types_NFP_DateTime_NFP_CommonType, gen_MARTE_Library_BasicNFP_Types_NFP_DataTxRate_NFP_Real, gen_MARTE_Library_BasicNFP_Types_NFP_Power_NFP_Real, gen_MARTE_Library_BasicNFP_Types_NFP_DataSize_NFP_Real, gen_MARTE_Library_BasicNFP_Types_NFP_Length_NFP_Real, gen_MARTE_Library_BasicNFP_Types_NFP_Area_NFP_Real, gen_MARTE_Library_BasicNFP_Types_BurstPattern_AperiodicPattern, gen_MARTE_Library_BasicNFP_Types_IrregularPattern_AperiodicPattern, gen_MARTE_Library_BasicNFP_Types_SporadicPattern_AperiodicPattern, gen_MARTE_Library_BasicNFP_Types_NFP_Percentage_NFP_Real, gen_MARTE_Library_BasicNFP_Types_NFP_Price_NFP_Real, gen_MARTE_Library_BasicNFP_Types_NFP_Weight_NFP_Real, gen_MARTE_Library_BasicNFP_Types_NFP_Duration_NFP_Real},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)