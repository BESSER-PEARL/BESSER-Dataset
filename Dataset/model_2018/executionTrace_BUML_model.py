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
executionTrace_MapEntry = Class(name="executionTrace::MapEntry")
executionTrace_ExecutionTrace = Class(name="executionTrace::ExecutionTrace")
executionTrace_Execution = Class(name="executionTrace::Execution", is_abstract=True)
executionTrace_StoryPatternApplication = Class(name="executionTrace::StoryPatternApplication")
executionTrace_StoryPatternObjectExecution = Class(name="executionTrace::StoryPatternObjectExecution", is_abstract=True)
executionTrace_StoryPatternObjectBound = Class(name="executionTrace::StoryPatternObjectBound")
executionTrace_StoryPatternObjectNotBound = Class(name="executionTrace::StoryPatternObjectNotBound")
executionTrace_StoryPatternObjectBindingRevoked = Class(name="executionTrace::StoryPatternObjectBindingRevoked")
executionTrace_ActivityExecution = Class(name="executionTrace::ActivityExecution")
Execution = Class(name="Execution")
executionTrace_ActivityNodeExecution = Class(name="executionTrace::ActivityNodeExecution")
executionTrace_ActivityEdgeTraversal = Class(name="executionTrace::ActivityEdgeTraversal")
executionTrace_StoryPatternExecution = Class(name="executionTrace::StoryPatternExecution", is_abstract=True)
executionTrace_StoryPatternInitialization = Class(name="executionTrace::StoryPatternInitialization")
executionTrace_StoryPatternMatching = Class(name="executionTrace::StoryPatternMatching")
executionTrace_LinkCheckSuccessful = Class(name="executionTrace::LinkCheckSuccessful")
executionTrace_LinkCheckFailed = Class(name="executionTrace::LinkCheckFailed")
executionTrace_ExpressionEvaluation = Class(name="executionTrace::ExpressionEvaluation")
executionTrace_StoryPatternLinkExecution = Class(name="executionTrace::StoryPatternLinkExecution", is_abstract=True)
executionTrace_TraversingLink = Class(name="executionTrace::TraversingLink")
executionTrace_LinkCheck = Class(name="executionTrace::LinkCheck", is_abstract=True)
executionTrace_InstanceLinkCreation = Class(name="executionTrace::InstanceLinkCreation")
executionTrace_InstanceLinkDeletion = Class(name="executionTrace::InstanceLinkDeletion")
executionTrace_AttributeValueSet = Class(name="executionTrace::AttributeValueSet")
executionTrace_InstanceObjectModification = Class(name="executionTrace::InstanceObjectModification", is_abstract=True)
executionTrace_InstanceObjectCreation = Class(name="executionTrace::InstanceObjectCreation")
executionTrace_InstanceObjectDeletion = Class(name="executionTrace::InstanceObjectDeletion")
executionTrace_InstanceLinkModification = Class(name="executionTrace::InstanceLinkModification", is_abstract=True)
executionTrace_VariableDeleted = Class(name="executionTrace::VariableDeleted")
executionTrace_VariableChanged = Class(name="executionTrace::VariableChanged")
executionTrace_StoryPatternObjectConstraintEvaluation = Class(name="executionTrace::StoryPatternObjectConstraintEvaluation", is_abstract=True)
executionTrace_VariableModification = Class(name="executionTrace::VariableModification", is_abstract=True)
executionTrace_VariableCreated = Class(name="executionTrace::VariableCreated")
executionTrace_StoryPatternObjectConstraintHolds = Class(name="executionTrace::StoryPatternObjectConstraintHolds")
executionTrace_StoryPatternObjectConstraintViolated = Class(name="executionTrace::StoryPatternObjectConstraintViolated")
executionTrace_StoryPatternConstraintEvaluation = Class(name="executionTrace::StoryPatternConstraintEvaluation", is_abstract=True)
executionTrace_StoryPatternConstraintHolds = Class(name="executionTrace::StoryPatternConstraintHolds")
executionTrace_StoryPatternConstraintViolated = Class(name="executionTrace::StoryPatternConstraintViolated")

# executionTrace_MapEntry class attributes and methods
executionTrace_MapEntry_key: Property = Property(name="key", type=StringType)
executionTrace_MapEntry_value: Property = Property(name="value", type=StringType)
executionTrace_MapEntry.attributes={executionTrace_MapEntry_value, executionTrace_MapEntry_key}

# executionTrace_ExecutionTrace class attributes and methods
executionTrace_ExecutionTrace_totalExecutionTimeMsec: Property = Property(name="totalExecutionTimeMsec", type=StringType)
executionTrace_ExecutionTrace_description: Property = Property(name="description", type=StringType)
executionTrace_ExecutionTrace_totalExecutionTime: Property = Property(name="totalExecutionTime", type=StringType)
executionTrace_ExecutionTrace.attributes={executionTrace_ExecutionTrace_totalExecutionTime, executionTrace_ExecutionTrace_description, executionTrace_ExecutionTrace_totalExecutionTimeMsec}

# executionTrace_Execution class attributes and methods
executionTrace_Execution_executionStartedTimeStamp: Property = Property(name="executionStartedTimeStamp", type=StringType)
executionTrace_Execution_executionFinishedTimeStamp: Property = Property(name="executionFinishedTimeStamp", type=StringType)
executionTrace_Execution_executionTime: Property = Property(name="executionTime", type=StringType)
executionTrace_Execution_executionTimeMsec: Property = Property(name="executionTimeMsec", type=StringType)
executionTrace_Execution.attributes={executionTrace_Execution_executionFinishedTimeStamp, executionTrace_Execution_executionTime, executionTrace_Execution_executionStartedTimeStamp, executionTrace_Execution_executionTimeMsec}

# executionTrace_StoryPatternApplication class attributes and methods

# executionTrace_StoryPatternObjectExecution class attributes and methods

# executionTrace_StoryPatternObjectBound class attributes and methods
executionTrace_StoryPatternObjectBound_value: Property = Property(name="value", type=StringType)
executionTrace_StoryPatternObjectBound.attributes={executionTrace_StoryPatternObjectBound_value}

# executionTrace_StoryPatternObjectNotBound class attributes and methods

# executionTrace_StoryPatternObjectBindingRevoked class attributes and methods
executionTrace_StoryPatternObjectBindingRevoked_previousValue: Property = Property(name="previousValue", type=StringType)
executionTrace_StoryPatternObjectBindingRevoked.attributes={executionTrace_StoryPatternObjectBindingRevoked_previousValue}

# executionTrace_ActivityExecution class attributes and methods

# Execution class attributes and methods

# executionTrace_ActivityNodeExecution class attributes and methods

# executionTrace_ActivityEdgeTraversal class attributes and methods

# executionTrace_StoryPatternExecution class attributes and methods

# executionTrace_StoryPatternInitialization class attributes and methods

# executionTrace_StoryPatternMatching class attributes and methods
executionTrace_StoryPatternMatching_successful: Property = Property(name="successful", type=BooleanType)
executionTrace_StoryPatternMatching.attributes={executionTrace_StoryPatternMatching_successful}

# executionTrace_LinkCheckSuccessful class attributes and methods

# executionTrace_LinkCheckFailed class attributes and methods

# executionTrace_ExpressionEvaluation class attributes and methods
executionTrace_ExpressionEvaluation_result: Property = Property(name="result", type=StringType)
executionTrace_ExpressionEvaluation.attributes={executionTrace_ExpressionEvaluation_result}

# executionTrace_StoryPatternLinkExecution class attributes and methods
executionTrace_StoryPatternLinkExecution_sourceObject: Property = Property(name="sourceObject", type=StringType)
executionTrace_StoryPatternLinkExecution.attributes={executionTrace_StoryPatternLinkExecution_sourceObject}

# executionTrace_TraversingLink class attributes and methods

# executionTrace_LinkCheck class attributes and methods
executionTrace_LinkCheck_targetObject: Property = Property(name="targetObject", type=StringType)
executionTrace_LinkCheck.attributes={executionTrace_LinkCheck_targetObject}

# executionTrace_InstanceLinkCreation class attributes and methods

# executionTrace_InstanceLinkDeletion class attributes and methods

# executionTrace_AttributeValueSet class attributes and methods
executionTrace_AttributeValueSet_instanceObject: Property = Property(name="instanceObject", type=StringType)
executionTrace_AttributeValueSet_newValue: Property = Property(name="newValue", type=StringType)
executionTrace_AttributeValueSet.attributes={executionTrace_AttributeValueSet_instanceObject, executionTrace_AttributeValueSet_newValue}

# executionTrace_InstanceObjectModification class attributes and methods
executionTrace_InstanceObjectModification_instanceObject: Property = Property(name="instanceObject", type=StringType)
executionTrace_InstanceObjectModification.attributes={executionTrace_InstanceObjectModification_instanceObject}

# executionTrace_InstanceObjectCreation class attributes and methods

# executionTrace_InstanceObjectDeletion class attributes and methods

# executionTrace_InstanceLinkModification class attributes and methods
executionTrace_InstanceLinkModification_sourceInstanceObject: Property = Property(name="sourceInstanceObject", type=StringType)
executionTrace_InstanceLinkModification_targetInstanceObject: Property = Property(name="targetInstanceObject", type=StringType)
executionTrace_InstanceLinkModification.attributes={executionTrace_InstanceLinkModification_sourceInstanceObject, executionTrace_InstanceLinkModification_targetInstanceObject}

# executionTrace_VariableDeleted class attributes and methods

# executionTrace_VariableChanged class attributes and methods
executionTrace_VariableChanged_oldValue: Property = Property(name="oldValue", type=StringType)
executionTrace_VariableChanged.attributes={executionTrace_VariableChanged_oldValue}

# executionTrace_StoryPatternObjectConstraintEvaluation class attributes and methods

# executionTrace_VariableModification class attributes and methods
executionTrace_VariableModification_variableName: Property = Property(name="variableName", type=StringType)
executionTrace_VariableModification_value: Property = Property(name="value", type=StringType)
executionTrace_VariableModification.attributes={executionTrace_VariableModification_value, executionTrace_VariableModification_variableName}

# executionTrace_VariableCreated class attributes and methods

# executionTrace_StoryPatternObjectConstraintHolds class attributes and methods

# executionTrace_StoryPatternObjectConstraintViolated class attributes and methods

# executionTrace_StoryPatternConstraintEvaluation class attributes and methods

# executionTrace_StoryPatternConstraintHolds class attributes and methods

# executionTrace_StoryPatternConstraintViolated class attributes and methods

# Relationships
executions0: BinaryAssociation = BinaryAssociation(
    name="executions0",
    ends={
        Property(name="executionTrace_Execution", type=executionTrace_ExecutionTrace, multiplicity=Multiplicity(1, 1)),
        Property(name="executionTrace_ExecutionTrace", type=executionTrace_Execution, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elements2: BinaryAssociation = BinaryAssociation(
    name="elements2",
    ends={
        Property(name="Execution", type=executionTrace_Execution, multiplicity=Multiplicity(1, 1)),
        Property(name="container", type=executionTrace_Execution, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
container4: BinaryAssociation = BinaryAssociation(
    name="container4",
    ends={
        Property(name="Execution5", type=executionTrace_Execution, multiplicity=Multiplicity(1, 1)),
        Property(name="elements", type=executionTrace_Execution, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_executionTrace_StoryPatternObjectExecution_Execution = Generalization(general=Execution, specific=executionTrace_StoryPatternObjectExecution)
gen_executionTrace_ActivityExecution_Execution = Generalization(general=Execution, specific=executionTrace_ActivityExecution)
gen_executionTrace_ActivityNodeExecution_Execution = Generalization(general=Execution, specific=executionTrace_ActivityNodeExecution)
gen_executionTrace_ActivityEdgeTraversal_Execution = Generalization(general=Execution, specific=executionTrace_ActivityEdgeTraversal)
gen_executionTrace_StoryPatternExecution_Execution = Generalization(general=Execution, specific=executionTrace_StoryPatternExecution)
gen_executionTrace_ExpressionEvaluation_Execution = Generalization(general=Execution, specific=executionTrace_ExpressionEvaluation)
gen_executionTrace_StoryPatternLinkExecution_Execution = Generalization(general=Execution, specific=executionTrace_StoryPatternLinkExecution)
gen_executionTrace_InstanceObjectModification_Execution = Generalization(general=Execution, specific=executionTrace_InstanceObjectModification)
gen_executionTrace_InstanceLinkModification_Execution = Generalization(general=Execution, specific=executionTrace_InstanceLinkModification)
gen_executionTrace_AttributeValueSet_Execution = Generalization(general=Execution, specific=executionTrace_AttributeValueSet)
gen_executionTrace_VariableModification_Execution = Generalization(general=Execution, specific=executionTrace_VariableModification)

# Domain Model
domain_model = DomainModel(
    name="executionTrace",
    types={executionTrace_MapEntry, executionTrace_ExecutionTrace, executionTrace_Execution, executionTrace_StoryPatternApplication, executionTrace_StoryPatternObjectExecution, executionTrace_StoryPatternObjectBound, executionTrace_StoryPatternObjectNotBound, executionTrace_StoryPatternObjectBindingRevoked, executionTrace_ActivityExecution, Execution, executionTrace_ActivityNodeExecution, executionTrace_ActivityEdgeTraversal, executionTrace_StoryPatternExecution, executionTrace_StoryPatternInitialization, executionTrace_StoryPatternMatching, executionTrace_LinkCheckSuccessful, executionTrace_LinkCheckFailed, executionTrace_ExpressionEvaluation, executionTrace_StoryPatternLinkExecution, executionTrace_TraversingLink, executionTrace_LinkCheck, executionTrace_InstanceLinkCreation, executionTrace_InstanceLinkDeletion, executionTrace_AttributeValueSet, executionTrace_InstanceObjectModification, executionTrace_InstanceObjectCreation, executionTrace_InstanceObjectDeletion, executionTrace_InstanceLinkModification, executionTrace_VariableDeleted, executionTrace_VariableChanged, executionTrace_StoryPatternObjectConstraintEvaluation, executionTrace_VariableModification, executionTrace_VariableCreated, executionTrace_StoryPatternObjectConstraintHolds, executionTrace_StoryPatternObjectConstraintViolated, executionTrace_StoryPatternConstraintEvaluation, executionTrace_StoryPatternConstraintHolds, executionTrace_StoryPatternConstraintViolated},
    associations={executions0, elements2, container4},
    generalizations={gen_executionTrace_StoryPatternObjectExecution_Execution, gen_executionTrace_ActivityExecution_Execution, gen_executionTrace_ActivityNodeExecution_Execution, gen_executionTrace_ActivityEdgeTraversal_Execution, gen_executionTrace_StoryPatternExecution_Execution, gen_executionTrace_ExpressionEvaluation_Execution, gen_executionTrace_StoryPatternLinkExecution_Execution, gen_executionTrace_InstanceObjectModification_Execution, gen_executionTrace_InstanceLinkModification_Execution, gen_executionTrace_AttributeValueSet_Execution, gen_executionTrace_VariableModification_Execution},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)