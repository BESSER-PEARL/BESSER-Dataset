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
MetricUnit: Enumeration = Enumeration(
    name="MetricUnit",
    literals={
            EnumerationLiteral(name="minutes"),
			EnumerationLiteral(name="uc")
    }
)

MetricType: Enumeration = Enumeration(
    name="MetricType",
    literals={
            EnumerationLiteral(name="hardData"),
			EnumerationLiteral(name="softData"),
			EnumerationLiteral(name="normalizedData")
    }
)

BaseElement: Enumeration = Enumeration(
    name="BaseElement",
    literals={
            EnumerationLiteral(name="Task"),
			EnumerationLiteral(name="Activity")
    }
)

ColectType: Enumeration = Enumeration(
    name="ColectType",
    literals={
            EnumerationLiteral(name="intercalated"),
			EnumerationLiteral(name="continuous")
    }
)

# Classes
MetricModel_ActivityMetric = Class(name="MetricModel::ActivityMetric")
Metric = Class(name="Metric")
MetricModel_TaskMetric = Class(name="MetricModel::TaskMetric")
MetricModel_MetricPlanModel = Class(name="MetricModel::MetricPlanModel")
MetricModel_Metric = Class(name="MetricModel::Metric")

# MetricModel_ActivityMetric class attributes and methods
MetricModel_ActivityMetric_activityBegin: Property = Property(name="activityBegin", type=StringType)
MetricModel_ActivityMetric_activityEnd: Property = Property(name="activityEnd", type=StringType)
MetricModel_ActivityMetric.attributes={MetricModel_ActivityMetric_activityBegin, MetricModel_ActivityMetric_activityEnd}

# Metric class attributes and methods

# MetricModel_TaskMetric class attributes and methods
MetricModel_TaskMetric_tasksBase: Property = Property(name="tasksBase", type=StringType)
MetricModel_TaskMetric.attributes={MetricModel_TaskMetric_tasksBase}

# MetricModel_MetricPlanModel class attributes and methods
MetricModel_MetricPlanModel_name: Property = Property(name="name", type=StringType)
MetricModel_MetricPlanModel.attributes={MetricModel_MetricPlanModel_name}

# MetricModel_Metric class attributes and methods
MetricModel_Metric_name: Property = Property(name="name", type=StringType)
MetricModel_Metric_description: Property = Property(name="description", type=StringType)
MetricModel_Metric_type: Property = Property(name="type", type=StringType)
MetricModel_Metric_form: Property = Property(name="form", type=StringType)
MetricModel_Metric_id: Property = Property(name="id", type=StringType)
MetricModel_Metric_unit: Property = Property(name="unit", type=StringType)
MetricModel_Metric.attributes={MetricModel_Metric_name, MetricModel_Metric_unit, MetricModel_Metric_form, MetricModel_Metric_type, MetricModel_Metric_description, MetricModel_Metric_id}

# Relationships
metrics0: BinaryAssociation = BinaryAssociation(
    name="metrics0",
    ends={
        Property(name="MetricModel_Metric", type=MetricModel_MetricPlanModel, multiplicity=Multiplicity(1, 1)),
        Property(name="MetricModel_MetricPlanModel", type=MetricModel_Metric, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_MetricModel_ActivityMetric_Metric = Generalization(general=Metric, specific=MetricModel_ActivityMetric)
gen_MetricModel_TaskMetric_Metric = Generalization(general=Metric, specific=MetricModel_TaskMetric)

# Domain Model
domain_model = DomainModel(
    name="MetricModel",
    types={MetricModel_ActivityMetric, Metric, MetricModel_TaskMetric, MetricModel_MetricPlanModel, MetricModel_Metric, MetricUnit, MetricType, BaseElement, ColectType},
    associations={metrics0},
    generalizations={gen_MetricModel_ActivityMetric_Metric, gen_MetricModel_TaskMetric_Metric},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)