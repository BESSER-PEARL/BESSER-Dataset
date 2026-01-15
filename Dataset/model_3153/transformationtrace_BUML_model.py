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
transformationtrace_TransformationTrace = Class(name="transformationtrace::TransformationTrace")
transformationtrace_ActivationTrace = Class(name="transformationtrace::ActivationTrace")
transformationtrace_RuleParameterTrace = Class(name="transformationtrace::RuleParameterTrace")

# transformationtrace_TransformationTrace class attributes and methods

# transformationtrace_ActivationTrace class attributes and methods
transformationtrace_ActivationTrace_ruleName: Property = Property(name="ruleName", type=StringType)
transformationtrace_ActivationTrace.attributes={transformationtrace_ActivationTrace_ruleName}

# transformationtrace_RuleParameterTrace class attributes and methods
transformationtrace_RuleParameterTrace_parameterName: Property = Property(name="parameterName", type=StringType)
transformationtrace_RuleParameterTrace_objectId: Property = Property(name="objectId", type=StringType)
transformationtrace_RuleParameterTrace.attributes={transformationtrace_RuleParameterTrace_objectId, transformationtrace_RuleParameterTrace_parameterName}

# Relationships
ruleParameterTraces1: BinaryAssociation = BinaryAssociation(
    name="ruleParameterTraces1",
    ends={
        Property(name="transformationtrace_ActivationTrace2", type=transformationtrace_RuleParameterTrace, multiplicity=Multiplicity(0, 9999), is_composite=True),
        Property(name="transformationtrace_RuleParameterTrace", type=transformationtrace_ActivationTrace, multiplicity=Multiplicity(1, 1))
    }
)
activationTraces0: BinaryAssociation = BinaryAssociation(
    name="activationTraces0",
    ends={
        Property(name="transformationtrace_ActivationTrace", type=transformationtrace_TransformationTrace, multiplicity=Multiplicity(1, 1)),
        Property(name="transformationtrace_TransformationTrace", type=transformationtrace_ActivationTrace, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="transformationtrace",
    types={transformationtrace_TransformationTrace, transformationtrace_ActivationTrace, transformationtrace_RuleParameterTrace},
    associations={ruleParameterTraces1, activationTraces0},
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