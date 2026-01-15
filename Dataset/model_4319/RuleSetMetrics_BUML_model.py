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
metrics_RuleSetMetrics = Class(name="metrics::RuleSetMetrics")
metrics_RuleMetrics = Class(name="metrics::RuleMetrics")
metrics_Rule = Class(name="metrics::Rule")

# metrics_RuleSetMetrics class attributes and methods
metrics_RuleSetMetrics_numberOfRules: Property = Property(name="numberOfRules", type=IntegerType)
metrics_RuleSetMetrics_totalNumberOfNodes: Property = Property(name="totalNumberOfNodes", type=IntegerType)
metrics_RuleSetMetrics_totalNumberOfEdges: Property = Property(name="totalNumberOfEdges", type=IntegerType)
metrics_RuleSetMetrics_totalNumberOfAttributes: Property = Property(name="totalNumberOfAttributes", type=IntegerType)
metrics_RuleSetMetrics_m_findRuleMetrics: Method = Method(name="findRuleMetrics", parameters={Parameter(name='rule')}, type=StringType)
metrics_RuleSetMetrics_m_createPresentationString: Method = Method(name="createPresentationString", parameters={}, type=StringType)
metrics_RuleSetMetrics.attributes={metrics_RuleSetMetrics_totalNumberOfAttributes, metrics_RuleSetMetrics_numberOfRules, metrics_RuleSetMetrics_totalNumberOfEdges, metrics_RuleSetMetrics_totalNumberOfNodes}
metrics_RuleSetMetrics.methods={metrics_RuleSetMetrics_m_createPresentationString, metrics_RuleSetMetrics_m_findRuleMetrics}

# metrics_RuleMetrics class attributes and methods
metrics_RuleMetrics_numberOfNodes: Property = Property(name="numberOfNodes", type=IntegerType)
metrics_RuleMetrics_numberOfEdges: Property = Property(name="numberOfEdges", type=IntegerType)
metrics_RuleMetrics_numberOfAttributes: Property = Property(name="numberOfAttributes", type=IntegerType)
metrics_RuleMetrics.attributes={metrics_RuleMetrics_numberOfEdges, metrics_RuleMetrics_numberOfAttributes, metrics_RuleMetrics_numberOfNodes}

# metrics_Rule class attributes and methods

# Relationships
ruleMetrics0: BinaryAssociation = BinaryAssociation(
    name="ruleMetrics0",
    ends={
        Property(name="metrics_RuleMetrics", type=metrics_RuleSetMetrics, multiplicity=Multiplicity(1, 1)),
        Property(name="metrics_RuleSetMetrics", type=metrics_RuleMetrics, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ruleSet1: BinaryAssociation = BinaryAssociation(
    name="ruleSet1",
    ends={
        Property(name="metrics_Rule", type=metrics_RuleSetMetrics, multiplicity=Multiplicity(1, 1)),
        Property(name="metrics_RuleSetMetrics2", type=metrics_Rule, multiplicity=Multiplicity(0, 9999))
    }
)
rule3: BinaryAssociation = BinaryAssociation(
    name="rule3",
    ends={
        Property(name="metrics_Rule5", type=metrics_RuleMetrics, multiplicity=Multiplicity(1, 1)),
        Property(name="metrics_RuleMetrics4", type=metrics_Rule, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="metrics",
    types={metrics_RuleSetMetrics, metrics_RuleMetrics, metrics_Rule},
    associations={ruleMetrics0, ruleSet1, rule3},
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