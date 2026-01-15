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
metricDSL_MetricModel = Class(name="metricDSL::MetricModel")
metricDSL_Metric = Class(name="metricDSL::Metric")
metricDSL_ExternalMetric = Class(name="metricDSL::ExternalMetric")
Metric = Class(name="Metric")
metricDSL_InternalMetric = Class(name="metricDSL::InternalMetric")
metricDSL_Number = Class(name="metricDSL::Number")
metricDSL_MetricDefinition = Class(name="metricDSL::MetricDefinition")
metricDSL_Parameter = Class(name="metricDSL::Parameter")
Number = Class(name="Number")
metricDSL_Constant = Class(name="metricDSL::Constant")
metricDSL_WeightedMetric = Class(name="metricDSL::WeightedMetric")
MetricDefinition = Class(name="MetricDefinition")
metricDSL_MetricAndWeight = Class(name="metricDSL::MetricAndWeight")
metricDSL_StepwiseMetric = Class(name="metricDSL::StepwiseMetric")
metricDSL_BoundAndWeight = Class(name="metricDSL::BoundAndWeight")
metricDSL_RatioMetric = Class(name="metricDSL::RatioMetric")

# metricDSL_MetricModel class attributes and methods
metricDSL_MetricModel_importURI: Property = Property(name="importURI", type=StringType)
metricDSL_MetricModel.attributes={metricDSL_MetricModel_importURI}

# metricDSL_Metric class attributes and methods
metricDSL_Metric_name: Property = Property(name="name", type=StringType)
metricDSL_Metric.attributes={metricDSL_Metric_name}

# metricDSL_ExternalMetric class attributes and methods

# Metric class attributes and methods

# metricDSL_InternalMetric class attributes and methods
metricDSL_InternalMetric_shortName: Property = Property(name="shortName", type=StringType)
metricDSL_InternalMetric_description: Property = Property(name="description", type=StringType)
metricDSL_InternalMetric.attributes={metricDSL_InternalMetric_description, metricDSL_InternalMetric_shortName}

# metricDSL_Number class attributes and methods
metricDSL_Number_name: Property = Property(name="name", type=StringType)
metricDSL_Number.attributes={metricDSL_Number_name}

# metricDSL_MetricDefinition class attributes and methods

# metricDSL_Parameter class attributes and methods
metricDSL_Parameter_shortname: Property = Property(name="shortname", type=StringType)
metricDSL_Parameter_description: Property = Property(name="description", type=StringType)
metricDSL_Parameter_defaultValue: Property = Property(name="defaultValue", type=FloatType)
metricDSL_Parameter.attributes={metricDSL_Parameter_shortname, metricDSL_Parameter_description, metricDSL_Parameter_defaultValue}

# Number class attributes and methods

# metricDSL_Constant class attributes and methods
metricDSL_Constant_value: Property = Property(name="value", type=FloatType)
metricDSL_Constant.attributes={metricDSL_Constant_value}

# metricDSL_WeightedMetric class attributes and methods

# MetricDefinition class attributes and methods

# metricDSL_MetricAndWeight class attributes and methods

# metricDSL_StepwiseMetric class attributes and methods

# metricDSL_BoundAndWeight class attributes and methods

# metricDSL_RatioMetric class attributes and methods

# Relationships
metrics0: BinaryAssociation = BinaryAssociation(
    name="metrics0",
    ends={
        Property(name="metricDSL_Metric", type=metricDSL_MetricModel, multiplicity=Multiplicity(1, 1)),
        Property(name="metricDSL_MetricModel", type=metricDSL_Metric, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parameter1: BinaryAssociation = BinaryAssociation(
    name="parameter1",
    ends={
        Property(name="metricDSL_Number", type=metricDSL_InternalMetric, multiplicity=Multiplicity(1, 1)),
        Property(name="metricDSL_InternalMetric", type=metricDSL_Number, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
definition2: BinaryAssociation = BinaryAssociation(
    name="definition2",
    ends={
        Property(name="metricDSL_MetricDefinition", type=metricDSL_InternalMetric, multiplicity=Multiplicity(1, 1)),
        Property(name="metricDSL_InternalMetric3", type=metricDSL_MetricDefinition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
weights4: BinaryAssociation = BinaryAssociation(
    name="weights4",
    ends={
        Property(name="metricDSL_MetricAndWeight", type=metricDSL_WeightedMetric, multiplicity=Multiplicity(1, 1)),
        Property(name="metricDSL_WeightedMetric", type=metricDSL_MetricAndWeight, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
innerMetric5: BinaryAssociation = BinaryAssociation(
    name="innerMetric5",
    ends={
        Property(name="metricDSL_Metric6", type=metricDSL_StepwiseMetric, multiplicity=Multiplicity(1, 1)),
        Property(name="metricDSL_StepwiseMetric", type=metricDSL_Metric, multiplicity=Multiplicity(0, 1))
    }
)
steps7: BinaryAssociation = BinaryAssociation(
    name="steps7",
    ends={
        Property(name="metricDSL_BoundAndWeight", type=metricDSL_StepwiseMetric, multiplicity=Multiplicity(1, 1)),
        Property(name="metricDSL_StepwiseMetric8", type=metricDSL_BoundAndWeight, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
nominatorMetric9: BinaryAssociation = BinaryAssociation(
    name="nominatorMetric9",
    ends={
        Property(name="metricDSL_Metric10", type=metricDSL_RatioMetric, multiplicity=Multiplicity(1, 1)),
        Property(name="metricDSL_RatioMetric", type=metricDSL_Metric, multiplicity=Multiplicity(0, 1))
    }
)
denominatorMetric11: BinaryAssociation = BinaryAssociation(
    name="denominatorMetric11",
    ends={
        Property(name="metricDSL_Metric13", type=metricDSL_RatioMetric, multiplicity=Multiplicity(1, 1)),
        Property(name="metricDSL_RatioMetric12", type=metricDSL_Metric, multiplicity=Multiplicity(0, 1))
    }
)
upperBound14: BinaryAssociation = BinaryAssociation(
    name="upperBound14",
    ends={
        Property(name="metricDSL_Number16", type=metricDSL_BoundAndWeight, multiplicity=Multiplicity(1, 1)),
        Property(name="metricDSL_BoundAndWeight15", type=metricDSL_Number, multiplicity=Multiplicity(0, 1))
    }
)
weight17: BinaryAssociation = BinaryAssociation(
    name="weight17",
    ends={
        Property(name="metricDSL_Number19", type=metricDSL_BoundAndWeight, multiplicity=Multiplicity(1, 1)),
        Property(name="metricDSL_BoundAndWeight18", type=metricDSL_Number, multiplicity=Multiplicity(0, 1))
    }
)
metric20: BinaryAssociation = BinaryAssociation(
    name="metric20",
    ends={
        Property(name="metricDSL_Metric22", type=metricDSL_MetricAndWeight, multiplicity=Multiplicity(1, 1)),
        Property(name="metricDSL_MetricAndWeight21", type=metricDSL_Metric, multiplicity=Multiplicity(0, 1))
    }
)
weight23: BinaryAssociation = BinaryAssociation(
    name="weight23",
    ends={
        Property(name="metricDSL_Number25", type=metricDSL_MetricAndWeight, multiplicity=Multiplicity(1, 1)),
        Property(name="metricDSL_MetricAndWeight24", type=metricDSL_Number, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_metricDSL_ExternalMetric_Metric = Generalization(general=Metric, specific=metricDSL_ExternalMetric)
gen_metricDSL_InternalMetric_Metric = Generalization(general=Metric, specific=metricDSL_InternalMetric)
gen_metricDSL_Parameter_Number = Generalization(general=Number, specific=metricDSL_Parameter)
gen_metricDSL_Constant_Number = Generalization(general=Number, specific=metricDSL_Constant)
gen_metricDSL_WeightedMetric_MetricDefinition = Generalization(general=MetricDefinition, specific=metricDSL_WeightedMetric)
gen_metricDSL_StepwiseMetric_MetricDefinition = Generalization(general=MetricDefinition, specific=metricDSL_StepwiseMetric)
gen_metricDSL_RatioMetric_MetricDefinition = Generalization(general=MetricDefinition, specific=metricDSL_RatioMetric)

# Domain Model
domain_model = DomainModel(
    name="metricDSL",
    types={metricDSL_MetricModel, metricDSL_Metric, metricDSL_ExternalMetric, Metric, metricDSL_InternalMetric, metricDSL_Number, metricDSL_MetricDefinition, metricDSL_Parameter, Number, metricDSL_Constant, metricDSL_WeightedMetric, MetricDefinition, metricDSL_MetricAndWeight, metricDSL_StepwiseMetric, metricDSL_BoundAndWeight, metricDSL_RatioMetric},
    associations={metrics0, parameter1, definition2, weights4, innerMetric5, steps7, nominatorMetric9, denominatorMetric11, upperBound14, weight17, metric20, weight23},
    generalizations={gen_metricDSL_ExternalMetric_Metric, gen_metricDSL_InternalMetric_Metric, gen_metricDSL_Parameter_Number, gen_metricDSL_Constant_Number, gen_metricDSL_WeightedMetric_MetricDefinition, gen_metricDSL_StepwiseMetric_MetricDefinition, gen_metricDSL_RatioMetric_MetricDefinition},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)