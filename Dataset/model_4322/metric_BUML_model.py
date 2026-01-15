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
metric_Metric = Class(name="metric::Metric")
metric_ConstraintMetrics = Class(name="metric::ConstraintMetrics")
ConstraintMetric = Class(name="ConstraintMetric")
metric_ConstraintMetric = Class(name="metric::ConstraintMetric")
metric_Constraint = Class(name="metric::Constraint")
Metric = Class(name="Metric")

# metric_Metric class attributes and methods
metric_Metric_m_getReport: Method = Method(name="getReport", parameters={}, type=StringType)
metric_Metric.methods={metric_Metric_m_getReport}

# metric_ConstraintMetrics class attributes and methods
metric_ConstraintMetrics_numberOfConstraintsByKind: Property = Property(name="numberOfConstraintsByKind", type=StringType)
metric_ConstraintMetrics_m_getConstraintCount: Method = Method(name="getConstraintCount", parameters={}, type=IntegerType)
metric_ConstraintMetrics_m_getExpressionCount: Method = Method(name="getExpressionCount", parameters={}, type=IntegerType)
metric_ConstraintMetrics_m_getAvgExpressionCount: Method = Method(name="getAvgExpressionCount", parameters={}, type=FloatType)
metric_ConstraintMetrics_m_getAvgExpressionDepth: Method = Method(name="getAvgExpressionDepth", parameters={}, type=FloatType)
metric_ConstraintMetrics_m_getMinExpressionCount: Method = Method(name="getMinExpressionCount", parameters={}, type=IntegerType)
metric_ConstraintMetrics_m_getMinExpressionDepth: Method = Method(name="getMinExpressionDepth", parameters={}, type=IntegerType)
metric_ConstraintMetrics_m_getMaxExpressionCount: Method = Method(name="getMaxExpressionCount", parameters={}, type=IntegerType)
metric_ConstraintMetrics_m_getMaxExpressionDepth: Method = Method(name="getMaxExpressionDepth", parameters={}, type=IntegerType)
metric_ConstraintMetrics_m_getMeanExpressionCount: Method = Method(name="getMeanExpressionCount", parameters={}, type=IntegerType)
metric_ConstraintMetrics_m_getMeanExpressionDepth: Method = Method(name="getMeanExpressionDepth", parameters={}, type=IntegerType)
metric_ConstraintMetrics.attributes={metric_ConstraintMetrics_numberOfConstraintsByKind}
metric_ConstraintMetrics.methods={metric_ConstraintMetrics_m_getMinExpressionCount, metric_ConstraintMetrics_m_getMinExpressionDepth, metric_ConstraintMetrics_m_getMaxExpressionCount, metric_ConstraintMetrics_m_getMaxExpressionDepth, metric_ConstraintMetrics_m_getAvgExpressionDepth, metric_ConstraintMetrics_m_getAvgExpressionCount, metric_ConstraintMetrics_m_getMeanExpressionDepth, metric_ConstraintMetrics_m_getMeanExpressionCount, metric_ConstraintMetrics_m_getExpressionCount, metric_ConstraintMetrics_m_getConstraintCount}

# ConstraintMetric class attributes and methods

# metric_ConstraintMetric class attributes and methods
metric_ConstraintMetric_calledOperations: Property = Property(name="calledOperations", type=StringType)
metric_ConstraintMetric_calledProperties: Property = Property(name="calledProperties", type=StringType)
metric_ConstraintMetric_numberOfIfExpressions: Property = Property(name="numberOfIfExpressions", type=IntegerType)
metric_ConstraintMetric_numberOfLetExpressions: Property = Property(name="numberOfLetExpressions", type=IntegerType)
metric_ConstraintMetric_usedIterators: Property = Property(name="usedIterators", type=StringType)
metric_ConstraintMetric_usedLiterals: Property = Property(name="usedLiterals", type=StringType)
metric_ConstraintMetric_expressionCount: Property = Property(name="expressionCount", type=IntegerType)
metric_ConstraintMetric_expressionDepth: Property = Property(name="expressionDepth", type=IntegerType)
metric_ConstraintMetric.attributes={metric_ConstraintMetric_numberOfLetExpressions, metric_ConstraintMetric_calledOperations, metric_ConstraintMetric_expressionDepth, metric_ConstraintMetric_numberOfIfExpressions, metric_ConstraintMetric_calledProperties, metric_ConstraintMetric_expressionCount, metric_ConstraintMetric_usedIterators, metric_ConstraintMetric_usedLiterals}

# metric_Constraint class attributes and methods

# Metric class attributes and methods

# Relationships
referredConstraint3: BinaryAssociation = BinaryAssociation(
    name="referredConstraint3",
    ends={
        Property(name="metric_Constraint5", type=metric_ConstraintMetric, multiplicity=Multiplicity(1, 1)),
        Property(name="metric_ConstraintMetric4", type=metric_Constraint, multiplicity=Multiplicity(0, 1))
    }
)
constraintMetrics0: BinaryAssociation = BinaryAssociation(
    name="constraintMetrics0",
    ends={
        Property(name="metric_ConstraintMetric", type=metric_ConstraintMetrics, multiplicity=Multiplicity(1, 1)),
        Property(name="metric_ConstraintMetrics", type=metric_ConstraintMetric, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
constraints1: BinaryAssociation = BinaryAssociation(
    name="constraints1",
    ends={
        Property(name="metric_Constraint", type=metric_ConstraintMetrics, multiplicity=Multiplicity(1, 1)),
        Property(name="metric_ConstraintMetrics2", type=metric_Constraint, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_metric_ConstraintMetrics_ConstraintMetric = Generalization(general=ConstraintMetric, specific=metric_ConstraintMetrics)
gen_metric_ConstraintMetric_Metric = Generalization(general=Metric, specific=metric_ConstraintMetric)

# Domain Model
domain_model = DomainModel(
    name="metric",
    types={metric_Metric, metric_ConstraintMetrics, ConstraintMetric, metric_ConstraintMetric, metric_Constraint, Metric},
    associations={referredConstraint3, constraintMetrics0, constraints1},
    generalizations={gen_metric_ConstraintMetrics_ConstraintMetric, gen_metric_ConstraintMetric_Metric},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)