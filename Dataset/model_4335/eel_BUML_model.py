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
Visibility: Enumeration = Enumeration(
    name="Visibility",
    literals={
            EnumerationLiteral(name="LOCAL"),
			EnumerationLiteral(name="GLOBAL")
    }
)

Type: Enumeration = Enumeration(
    name="Type",
    literals={
            EnumerationLiteral(name="Energy"),
			EnumerationLiteral(name="Duration"),
			EnumerationLiteral(name="Power"),
			EnumerationLiteral(name="Current"),
			EnumerationLiteral(name="Voltage"),
			EnumerationLiteral(name="Scalar"),
			EnumerationLiteral(name="Frequency")
    }
)

# Classes
eel_MeasurementUncertainty = Class(name="eel::MeasurementUncertainty")
eel_TypedMeasure = Class(name="eel::TypedMeasure", is_abstract=True)
Measure = Class(name="Measure")
eel_Platform = Class(name="eel::Platform")
eel_Variable = Class(name="eel::Variable")
eel_Measure = Class(name="eel::Measure", is_abstract=True)
eel_MeasureCast = Class(name="eel::MeasureCast")
eel_MeasureBinaryOperation = Class(name="eel::MeasureBinaryOperation", is_abstract=True)
eel_MeasureValue = Class(name="eel::MeasureValue")
TypedMeasure = Class(name="TypedMeasure")
eel_MeasureOCL = Class(name="eel::MeasureOCL")
MeasureValue = Class(name="MeasureValue")
eel_MeasureAttribute = Class(name="eel::MeasureAttribute")
eel_RealTimeDuration = Class(name="eel::RealTimeDuration")
eel_MeasureBinaryProductOperation = Class(name="eel::MeasureBinaryProductOperation")
MeasureBinaryOperation = Class(name="MeasureBinaryOperation")
eel_MeasureBinarySumOperation = Class(name="eel::MeasureBinarySumOperation")
eel_EnergyComputation = Class(name="eel::EnergyComputation")
MeasureBinaryProductOperation = Class(name="MeasureBinaryProductOperation")
eel_PowerComputation = Class(name="eel::PowerComputation")
eel_MeasureUnboundOperation = Class(name="eel::MeasureUnboundOperation", is_abstract=True)
eel_MeasureUnboundSumOperation = Class(name="eel::MeasureUnboundSumOperation")
MeasureUnboundOperation = Class(name="MeasureUnboundOperation")
eel_MeasureUnboundProductOperation = Class(name="eel::MeasureUnboundProductOperation")
eel_Integral = Class(name="eel::Integral")
eel_MeasurementUncertaintyInformation = Class(name="eel::MeasurementUncertaintyInformation", is_abstract=True)
eel_NormalDistribution = Class(name="eel::NormalDistribution")
MeasurementUncertaintyInformation = Class(name="MeasurementUncertaintyInformation")
eel_Interval = Class(name="eel::Interval")
eel_Sampling = Class(name="eel::Sampling")
eel_Sample = Class(name="eel::Sample")

# eel_MeasurementUncertainty class attributes and methods
eel_MeasurementUncertainty_standardUncertainty: Property = Property(name="standardUncertainty", type=StringType)
eel_MeasurementUncertainty.attributes={eel_MeasurementUncertainty_standardUncertainty}

# eel_TypedMeasure class attributes and methods
eel_TypedMeasure_type: Property = Property(name="type", type=StringType)
eel_TypedMeasure_m_type: Method = Method(name="type", parameters={}, type=StringType)
eel_TypedMeasure_m_name: Method = Method(name="name", parameters={}, type=StringType)
eel_TypedMeasure.attributes={eel_TypedMeasure_type}
eel_TypedMeasure.methods={eel_TypedMeasure_m_type, eel_TypedMeasure_m_name}

# Measure class attributes and methods

# eel_Platform class attributes and methods
eel_Platform_name: Property = Property(name="name", type=StringType)
eel_Platform.attributes={eel_Platform_name}

# eel_Variable class attributes and methods
eel_Variable_value: Property = Property(name="value", type=StringType)
eel_Variable_name: Property = Property(name="name", type=StringType)
eel_Variable_vibility: Property = Property(name="vibility", type=StringType)
eel_Variable.attributes={eel_Variable_value, eel_Variable_name, eel_Variable_vibility}

# eel_Measure class attributes and methods
eel_Measure_name: Property = Property(name="name", type=StringType)
eel_Measure_subname: Property = Property(name="subname", type=StringType)
eel_Measure_targetClass: Property = Property(name="targetClass", type=StringType)
eel_Measure_targetOperation: Property = Property(name="targetOperation", type=StringType)
eel_Measure_m_name: Method = Method(name="name", parameters={}, type=StringType)
eel_Measure_m_type: Method = Method(name="type", parameters={}, type=StringType)
eel_Measure_m_value: Method = Method(name="value", parameters={}, type=StringType)
eel_Measure.attributes={eel_Measure_targetOperation, eel_Measure_name, eel_Measure_subname, eel_Measure_targetClass}
eel_Measure.methods={eel_Measure_m_name, eel_Measure_m_value, eel_Measure_m_type}

# eel_MeasureCast class attributes and methods

# eel_MeasureBinaryOperation class attributes and methods

# eel_MeasureValue class attributes and methods
eel_MeasureValue_value: Property = Property(name="value", type=StringType)
eel_MeasureValue_m_value: Method = Method(name="value", parameters={}, type=StringType)
eel_MeasureValue.attributes={eel_MeasureValue_value}
eel_MeasureValue.methods={eel_MeasureValue_m_value}

# TypedMeasure class attributes and methods

# eel_MeasureOCL class attributes and methods
eel_MeasureOCL_oclQuery: Property = Property(name="oclQuery", type=StringType)
eel_MeasureOCL.attributes={eel_MeasureOCL_oclQuery}

# MeasureValue class attributes and methods

# eel_MeasureAttribute class attributes and methods
eel_MeasureAttribute_att: Property = Property(name="att", type=StringType)
eel_MeasureAttribute.attributes={eel_MeasureAttribute_att}

# eel_RealTimeDuration class attributes and methods
eel_RealTimeDuration_m_type: Method = Method(name="type", parameters={}, type=StringType)
eel_RealTimeDuration.methods={eel_RealTimeDuration_m_type}

# eel_MeasureBinaryProductOperation class attributes and methods
eel_MeasureBinaryProductOperation_m_value: Method = Method(name="value", parameters={}, type=StringType)
eel_MeasureBinaryProductOperation.methods={eel_MeasureBinaryProductOperation_m_value}

# MeasureBinaryOperation class attributes and methods

# eel_MeasureBinarySumOperation class attributes and methods
eel_MeasureBinarySumOperation_m_value: Method = Method(name="value", parameters={}, type=StringType)
eel_MeasureBinarySumOperation.methods={eel_MeasureBinarySumOperation_m_value}

# eel_EnergyComputation class attributes and methods
eel_EnergyComputation_m_type: Method = Method(name="type", parameters={}, type=StringType)
eel_EnergyComputation_m_value: Method = Method(name="value", parameters={}, type=StringType)
eel_EnergyComputation.methods={eel_EnergyComputation_m_value, eel_EnergyComputation_m_type}

# MeasureBinaryProductOperation class attributes and methods

# eel_PowerComputation class attributes and methods
eel_PowerComputation_m_type: Method = Method(name="type", parameters={}, type=StringType)
eel_PowerComputation_m_value: Method = Method(name="value", parameters={}, type=StringType)
eel_PowerComputation.methods={eel_PowerComputation_m_type, eel_PowerComputation_m_value}

# eel_MeasureUnboundOperation class attributes and methods

# eel_MeasureUnboundSumOperation class attributes and methods
eel_MeasureUnboundSumOperation_m_value: Method = Method(name="value", parameters={}, type=StringType)
eel_MeasureUnboundSumOperation.methods={eel_MeasureUnboundSumOperation_m_value}

# MeasureUnboundOperation class attributes and methods

# eel_MeasureUnboundProductOperation class attributes and methods
eel_MeasureUnboundProductOperation_m_value: Method = Method(name="value", parameters={}, type=StringType)
eel_MeasureUnboundProductOperation.methods={eel_MeasureUnboundProductOperation_m_value}

# eel_Integral class attributes and methods
eel_Integral_function: Property = Property(name="function", type=StringType)
eel_Integral.attributes={eel_Integral_function}

# eel_MeasurementUncertaintyInformation class attributes and methods

# eel_NormalDistribution class attributes and methods
eel_NormalDistribution_meanValue: Property = Property(name="meanValue", type=StringType)
eel_NormalDistribution_standardDeviation: Property = Property(name="standardDeviation", type=StringType)
eel_NormalDistribution.attributes={eel_NormalDistribution_meanValue, eel_NormalDistribution_standardDeviation}

# MeasurementUncertaintyInformation class attributes and methods

# eel_Interval class attributes and methods

# eel_Sampling class attributes and methods
eel_Sampling_measurementProcedure: Property = Property(name="measurementProcedure", type=StringType)
eel_Sampling.attributes={eel_Sampling_measurementProcedure}

# eel_Sample class attributes and methods

# Relationships
uncertainty3: BinaryAssociation = BinaryAssociation(
    name="uncertainty3",
    ends={
        Property(name="eel_MeasurementUncertainty", type=eel_Measure, multiplicity=Multiplicity(1, 1)),
        Property(name="eel_Measure4", type=eel_MeasurementUncertainty, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
variables0: BinaryAssociation = BinaryAssociation(
    name="variables0",
    ends={
        Property(name="eel_Variable", type=eel_Platform, multiplicity=Multiplicity(1, 1)),
        Property(name="eel_Platform", type=eel_Variable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
measures1: BinaryAssociation = BinaryAssociation(
    name="measures1",
    ends={
        Property(name="eel_Measure", type=eel_Platform, multiplicity=Multiplicity(1, 1)),
        Property(name="eel_Platform2", type=eel_Measure, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
measure5: BinaryAssociation = BinaryAssociation(
    name="measure5",
    ends={
        Property(name="eel_Measure6", type=eel_MeasureCast, multiplicity=Multiplicity(1, 1)),
        Property(name="eel_MeasureCast", type=eel_Measure, multiplicity=Multiplicity(1, 1))
    }
)
left7: BinaryAssociation = BinaryAssociation(
    name="left7",
    ends={
        Property(name="eel_Measure8", type=eel_MeasureBinaryOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="eel_MeasureBinaryOperation", type=eel_Measure, multiplicity=Multiplicity(0, 1))
    }
)
right9: BinaryAssociation = BinaryAssociation(
    name="right9",
    ends={
        Property(name="eel_Measure11", type=eel_MeasureBinaryOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="eel_MeasureBinaryOperation10", type=eel_Measure, multiplicity=Multiplicity(0, 1))
    }
)
measures12: BinaryAssociation = BinaryAssociation(
    name="measures12",
    ends={
        Property(name="eel_Measure13", type=eel_MeasureUnboundOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="eel_MeasureUnboundOperation", type=eel_Measure, multiplicity=Multiplicity(1, 9999))
    }
)
interval22: BinaryAssociation = BinaryAssociation(
    name="interval22",
    ends={
        Property(name="eel_Interval23", type=eel_Integral, multiplicity=Multiplicity(1, 1)),
        Property(name="eel_Integral", type=eel_Interval, multiplicity=Multiplicity(1, 1))
    }
)
quantity24: BinaryAssociation = BinaryAssociation(
    name="quantity24",
    ends={
        Property(name="eel_Measure26", type=eel_Sample, multiplicity=Multiplicity(1, 1)),
        Property(name="eel_Sample25", type=eel_Measure, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
information14: BinaryAssociation = BinaryAssociation(
    name="information14",
    ends={
        Property(name="eel_MeasurementUncertaintyInformation", type=eel_MeasurementUncertainty, multiplicity=Multiplicity(1, 1)),
        Property(name="eel_MeasurementUncertainty15", type=eel_MeasurementUncertaintyInformation, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
lowerEndpoint16: BinaryAssociation = BinaryAssociation(
    name="lowerEndpoint16",
    ends={
        Property(name="eel_Measure17", type=eel_Interval, multiplicity=Multiplicity(1, 1)),
        Property(name="eel_Interval", type=eel_Measure, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
upperEndpoint18: BinaryAssociation = BinaryAssociation(
    name="upperEndpoint18",
    ends={
        Property(name="eel_Measure20", type=eel_Interval, multiplicity=Multiplicity(1, 1)),
        Property(name="eel_Interval19", type=eel_Measure, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
samples21: BinaryAssociation = BinaryAssociation(
    name="samples21",
    ends={
        Property(name="eel_Sample", type=eel_Sampling, multiplicity=Multiplicity(1, 1)),
        Property(name="eel_Sampling", type=eel_Sample, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_eel_TypedMeasure_Measure = Generalization(general=Measure, specific=eel_TypedMeasure)
gen_eel_MeasureCast_TypedMeasure = Generalization(general=TypedMeasure, specific=eel_MeasureCast)
gen_eel_MeasureBinaryOperation_TypedMeasure = Generalization(general=TypedMeasure, specific=eel_MeasureBinaryOperation)
gen_eel_MeasureValue_TypedMeasure = Generalization(general=TypedMeasure, specific=eel_MeasureValue)
gen_eel_MeasureOCL_MeasureValue = Generalization(general=MeasureValue, specific=eel_MeasureOCL)
gen_eel_MeasureAttribute_MeasureValue = Generalization(general=MeasureValue, specific=eel_MeasureAttribute)
gen_eel_MeasureBinaryProductOperation_MeasureBinaryOperation = Generalization(general=MeasureBinaryOperation, specific=eel_MeasureBinaryProductOperation)
gen_eel_MeasureBinarySumOperation_MeasureBinaryOperation = Generalization(general=MeasureBinaryOperation, specific=eel_MeasureBinarySumOperation)
gen_eel_EnergyComputation_MeasureBinaryProductOperation = Generalization(general=MeasureBinaryProductOperation, specific=eel_EnergyComputation)
gen_eel_PowerComputation_MeasureBinaryProductOperation = Generalization(general=MeasureBinaryProductOperation, specific=eel_PowerComputation)
gen_eel_RealTimeDuration_MeasureValue = Generalization(general=MeasureValue, specific=eel_RealTimeDuration)
gen_eel_MeasureUnboundOperation_TypedMeasure = Generalization(general=TypedMeasure, specific=eel_MeasureUnboundOperation)
gen_eel_MeasureUnboundSumOperation_MeasureUnboundOperation = Generalization(general=MeasureUnboundOperation, specific=eel_MeasureUnboundSumOperation)
gen_eel_MeasureUnboundProductOperation_MeasureUnboundOperation = Generalization(general=MeasureUnboundOperation, specific=eel_MeasureUnboundProductOperation)
gen_eel_Integral_MeasurementUncertaintyInformation = Generalization(general=MeasurementUncertaintyInformation, specific=eel_Integral)
gen_eel_NormalDistribution_MeasurementUncertaintyInformation = Generalization(general=MeasurementUncertaintyInformation, specific=eel_NormalDistribution)
gen_eel_Interval_MeasurementUncertaintyInformation = Generalization(general=MeasurementUncertaintyInformation, specific=eel_Interval)
gen_eel_Sampling_MeasurementUncertaintyInformation = Generalization(general=MeasurementUncertaintyInformation, specific=eel_Sampling)

# Domain Model
domain_model = DomainModel(
    name="eel",
    types={eel_MeasurementUncertainty, eel_TypedMeasure, Measure, eel_Platform, eel_Variable, eel_Measure, eel_MeasureCast, eel_MeasureBinaryOperation, eel_MeasureValue, TypedMeasure, eel_MeasureOCL, MeasureValue, eel_MeasureAttribute, eel_RealTimeDuration, eel_MeasureBinaryProductOperation, MeasureBinaryOperation, eel_MeasureBinarySumOperation, eel_EnergyComputation, MeasureBinaryProductOperation, eel_PowerComputation, eel_MeasureUnboundOperation, eel_MeasureUnboundSumOperation, MeasureUnboundOperation, eel_MeasureUnboundProductOperation, eel_Integral, eel_MeasurementUncertaintyInformation, eel_NormalDistribution, MeasurementUncertaintyInformation, eel_Interval, eel_Sampling, eel_Sample, Visibility, Type},
    associations={uncertainty3, variables0, measures1, measure5, left7, right9, measures12, interval22, quantity24, information14, lowerEndpoint16, upperEndpoint18, samples21},
    generalizations={gen_eel_TypedMeasure_Measure, gen_eel_MeasureCast_TypedMeasure, gen_eel_MeasureBinaryOperation_TypedMeasure, gen_eel_MeasureValue_TypedMeasure, gen_eel_MeasureOCL_MeasureValue, gen_eel_MeasureAttribute_MeasureValue, gen_eel_MeasureBinaryProductOperation_MeasureBinaryOperation, gen_eel_MeasureBinarySumOperation_MeasureBinaryOperation, gen_eel_EnergyComputation_MeasureBinaryProductOperation, gen_eel_PowerComputation_MeasureBinaryProductOperation, gen_eel_RealTimeDuration_MeasureValue, gen_eel_MeasureUnboundOperation_TypedMeasure, gen_eel_MeasureUnboundSumOperation_MeasureUnboundOperation, gen_eel_MeasureUnboundProductOperation_MeasureUnboundOperation, gen_eel_Integral_MeasurementUncertaintyInformation, gen_eel_NormalDistribution_MeasurementUncertaintyInformation, gen_eel_Interval_MeasurementUncertaintyInformation, gen_eel_Sampling_MeasurementUncertaintyInformation},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)