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
gtrace_TRequirementTrace = Class(name="gtrace::TRequirementTrace")
gtrace_TScenarioTrace = Class(name="gtrace::TScenarioTrace")
gtrace_TScenarioStepTrace = Class(name="gtrace::TScenarioStepTrace")
gtrace_TTrace = Class(name="gtrace::TTrace", is_abstract=True)
TTrace = Class(name="TTrace")
gtrace_RRequirement = Class(name="gtrace::RRequirement")
gtrace_MElement = Class(name="gtrace::MElement")
gtrace_RScenario = Class(name="gtrace::RScenario")
gtrace_MClassifier = Class(name="gtrace::MClassifier")
gtrace_MStateMachine = Class(name="gtrace::MStateMachine")
gtrace_RScenarioStep = Class(name="gtrace::RScenarioStep")
gtrace_MOperation = Class(name="gtrace::MOperation")
gtrace_MState = Class(name="gtrace::MState")
gtrace_TTraceModel = Class(name="gtrace::TTraceModel")

# gtrace_TRequirementTrace class attributes and methods

# gtrace_TScenarioTrace class attributes and methods

# gtrace_TScenarioStepTrace class attributes and methods

# gtrace_TTrace class attributes and methods
gtrace_TTrace_reviewed: Property = Property(name="reviewed", type=StringType)
gtrace_TTrace.attributes={gtrace_TTrace_reviewed}

# TTrace class attributes and methods

# gtrace_RRequirement class attributes and methods

# gtrace_MElement class attributes and methods

# gtrace_RScenario class attributes and methods

# gtrace_MClassifier class attributes and methods

# gtrace_MStateMachine class attributes and methods

# gtrace_RScenarioStep class attributes and methods

# gtrace_MOperation class attributes and methods

# gtrace_MState class attributes and methods

# gtrace_TTraceModel class attributes and methods
gtrace_TTraceModel_name: Property = Property(name="name", type=StringType)
gtrace_TTraceModel.attributes={gtrace_TTraceModel_name}

# Relationships
requirementTrace0: BinaryAssociation = BinaryAssociation(
    name="requirementTrace0",
    ends={
        Property(name="gtrace_TRequirementTrace", type=gtrace_TTraceModel, multiplicity=Multiplicity(1, 1)),
        Property(name="gtrace_TTraceModel", type=gtrace_TRequirementTrace, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
scenarioTrace1: BinaryAssociation = BinaryAssociation(
    name="scenarioTrace1",
    ends={
        Property(name="gtrace_TScenarioTrace", type=gtrace_TTraceModel, multiplicity=Multiplicity(1, 1)),
        Property(name="gtrace_TTraceModel2", type=gtrace_TScenarioTrace, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
scenarioStepTrace3: BinaryAssociation = BinaryAssociation(
    name="scenarioStepTrace3",
    ends={
        Property(name="gtrace_TScenarioStepTrace", type=gtrace_TTraceModel, multiplicity=Multiplicity(1, 1)),
        Property(name="gtrace_TTraceModel4", type=gtrace_TScenarioStepTrace, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
requirement5: BinaryAssociation = BinaryAssociation(
    name="requirement5",
    ends={
        Property(name="gtrace_RRequirement", type=gtrace_TRequirementTrace, multiplicity=Multiplicity(1, 1)),
        Property(name="gtrace_TRequirementTrace6", type=gtrace_RRequirement, multiplicity=Multiplicity(1, 1))
    }
)
structuralElement7: BinaryAssociation = BinaryAssociation(
    name="structuralElement7",
    ends={
        Property(name="gtrace_MElement", type=gtrace_TRequirementTrace, multiplicity=Multiplicity(1, 1)),
        Property(name="gtrace_TRequirementTrace8", type=gtrace_MElement, multiplicity=Multiplicity(1, 1))
    }
)
scenario9: BinaryAssociation = BinaryAssociation(
    name="scenario9",
    ends={
        Property(name="gtrace_RScenario", type=gtrace_TScenarioTrace, multiplicity=Multiplicity(1, 1)),
        Property(name="gtrace_TScenarioTrace10", type=gtrace_RScenario, multiplicity=Multiplicity(1, 1))
    }
)
classifier11: BinaryAssociation = BinaryAssociation(
    name="classifier11",
    ends={
        Property(name="gtrace_MClassifier", type=gtrace_TScenarioTrace, multiplicity=Multiplicity(1, 1)),
        Property(name="gtrace_TScenarioTrace12", type=gtrace_MClassifier, multiplicity=Multiplicity(0, 1))
    }
)
stateMachine13: BinaryAssociation = BinaryAssociation(
    name="stateMachine13",
    ends={
        Property(name="gtrace_MStateMachine", type=gtrace_TScenarioTrace, multiplicity=Multiplicity(1, 1)),
        Property(name="gtrace_TScenarioTrace14", type=gtrace_MStateMachine, multiplicity=Multiplicity(0, 1))
    }
)
scenarioStep15: BinaryAssociation = BinaryAssociation(
    name="scenarioStep15",
    ends={
        Property(name="gtrace_RScenarioStep", type=gtrace_TScenarioStepTrace, multiplicity=Multiplicity(1, 1)),
        Property(name="gtrace_TScenarioStepTrace16", type=gtrace_RScenarioStep, multiplicity=Multiplicity(1, 1))
    }
)
operation17: BinaryAssociation = BinaryAssociation(
    name="operation17",
    ends={
        Property(name="gtrace_MOperation", type=gtrace_TScenarioStepTrace, multiplicity=Multiplicity(1, 1)),
        Property(name="gtrace_TScenarioStepTrace18", type=gtrace_MOperation, multiplicity=Multiplicity(0, 1))
    }
)
state19: BinaryAssociation = BinaryAssociation(
    name="state19",
    ends={
        Property(name="gtrace_MState", type=gtrace_TScenarioStepTrace, multiplicity=Multiplicity(1, 1)),
        Property(name="gtrace_TScenarioStepTrace20", type=gtrace_MState, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_gtrace_TRequirementTrace_TTrace = Generalization(general=TTrace, specific=gtrace_TRequirementTrace)
gen_gtrace_TScenarioTrace_TTrace = Generalization(general=TTrace, specific=gtrace_TScenarioTrace)
gen_gtrace_TScenarioStepTrace_TTrace = Generalization(general=TTrace, specific=gtrace_TScenarioStepTrace)

# Domain Model
domain_model = DomainModel(
    name="gtrace",
    types={gtrace_TRequirementTrace, gtrace_TScenarioTrace, gtrace_TScenarioStepTrace, gtrace_TTrace, TTrace, gtrace_RRequirement, gtrace_MElement, gtrace_RScenario, gtrace_MClassifier, gtrace_MStateMachine, gtrace_RScenarioStep, gtrace_MOperation, gtrace_MState, gtrace_TTraceModel},
    associations={requirementTrace0, scenarioTrace1, scenarioStepTrace3, requirement5, structuralElement7, scenario9, classifier11, stateMachine13, scenarioStep15, operation17, state19},
    generalizations={gen_gtrace_TRequirementTrace_TTrace, gen_gtrace_TScenarioTrace_TTrace, gen_gtrace_TScenarioStepTrace_TTrace},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)