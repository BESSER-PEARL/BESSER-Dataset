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
UseCaseCodeAdapter_FileToUseCasesModel = Class(name="UseCaseCodeAdapter_FileToUseCasesModel")
UseCaseCodeAdapter_NodeToFlow = Class(name="UseCaseCodeAdapter_NodeToFlow")
UseCaseCodeAdapter_NodeToStep = Class(name="UseCaseCodeAdapter_NodeToStep")
UseCaseCodeAdapter_NodeToPackageDeclaration = Class(name="UseCaseCodeAdapter_NodeToPackageDeclaration")
UseCaseCodeAdapter_NodeToActor = Class(name="UseCaseCodeAdapter_NodeToActor")
UseCaseCodeAdapter_NodeToUseCase = Class(name="UseCaseCodeAdapter_NodeToUseCase")
UseCaseCodeAdapter_Rules_UseCasesRule = Class(name="UseCaseCodeAdapter_Rules_UseCasesRule")
UseCaseCodeAdapter_Rules_UseCaseRule = Class(name="UseCaseCodeAdapter_Rules_UseCaseRule")
UseCaseCodeAdapter_Rules_UseCaseDescRule = Class(name="UseCaseCodeAdapter_Rules_UseCaseDescRule")
UseCaseCodeAdapter_Rules_UseCaseDescPreCondRule = Class(name="UseCaseCodeAdapter_Rules_UseCaseDescPreCondRule")
UseCaseCodeAdapter_Rules_ParallelStepRule = Class(name="UseCaseCodeAdapter_Rules_ParallelStepRule")
UseCaseCodeAdapter_Rules_UseCasePreCondRule = Class(name="UseCaseCodeAdapter_Rules_UseCasePreCondRule")
UseCaseCodeAdapter_Rules_BasicFlowRule = Class(name="UseCaseCodeAdapter_Rules_BasicFlowRule")
UseCaseCodeAdapter_NodeToAlternativeFlowAlternative = Class(name="UseCaseCodeAdapter_NodeToAlternativeFlowAlternative")
UseCaseCodeAdapter_Rules_FileToUCModel = Class(name="UseCaseCodeAdapter_Rules_FileToUCModel")
UseCaseCodeAdapter_Rules_PackageRule = Class(name="UseCaseCodeAdapter_Rules_PackageRule")
UseCaseCodeAdapter_Rules_ActorsRule = Class(name="UseCaseCodeAdapter_Rules_ActorsRule")
UseCaseCodeAdapter_Rules_ActorRule = Class(name="UseCaseCodeAdapter_Rules_ActorRule")
UseCaseCodeAdapter_Rules_ActorDescRule = Class(name="UseCaseCodeAdapter_Rules_ActorDescRule")
UseCaseCodeAdapter_Rules_UseCaseExtendsRule = Class(name="UseCaseCodeAdapter_Rules_UseCaseExtendsRule")
UseCaseCodeAdapter_Rules_AltFlowAltContinueRule = Class(name="UseCaseCodeAdapter_Rules_AltFlowAltContinueRule")
UseCaseCodeAdapter_Rules_ParallelFlowInvokeRule = Class(name="UseCaseCodeAdapter_Rules_ParallelFlowInvokeRule")
UseCaseCodeAdapter_Rules_ParallelStepInvokeRefRule = Class(name="UseCaseCodeAdapter_Rules_ParallelStepInvokeRefRule")
UseCaseCodeAdapter_Rules_AlternativeFlowRule = Class(name="UseCaseCodeAdapter_Rules_AlternativeFlowRule")
UseCaseCodeAdapter_Rules_ParallelFlowRule = Class(name="UseCaseCodeAdapter_Rules_ParallelFlowRule")
UseCaseCodeAdapter_Rules_BasicFlowFinalStateRule = Class(name="UseCaseCodeAdapter_Rules_BasicFlowFinalStateRule")
UseCaseCodeAdapter_Rules_ActorExtendsRule = Class(name="UseCaseCodeAdapter_Rules_ActorExtendsRule")
UseCaseCodeAdapter_Rules_AltFlowFinalStateRule = Class(name="UseCaseCodeAdapter_Rules_AltFlowFinalStateRule")
UseCaseCodeAdapter_Rules_ParallelFlowFinalStateRule = Class(name="UseCaseCodeAdapter_Rules_ParallelFlowFinalStateRule")
UseCaseCodeAdapter_Rules_StepRule = Class(name="UseCaseCodeAdapter_Rules_StepRule")
UseCaseCodeAdapter_Rules_StepDescRule = Class(name="UseCaseCodeAdapter_Rules_StepDescRule")
UseCaseCodeAdapter_Rules_ParallelStepDescRule = Class(name="UseCaseCodeAdapter_Rules_ParallelStepDescRule")
UseCaseCodeAdapter_Rules_StepAlternativesRule = Class(name="UseCaseCodeAdapter_Rules_StepAlternativesRule")
UseCaseCodeAdapter_Rules_AltFlowAltRule = Class(name="UseCaseCodeAdapter_Rules_AltFlowAltRule")

# UseCaseCodeAdapter_FileToUseCasesModel class attributes and methods

# UseCaseCodeAdapter_NodeToFlow class attributes and methods

# UseCaseCodeAdapter_NodeToStep class attributes and methods

# UseCaseCodeAdapter_NodeToPackageDeclaration class attributes and methods

# UseCaseCodeAdapter_NodeToActor class attributes and methods

# UseCaseCodeAdapter_NodeToUseCase class attributes and methods

# UseCaseCodeAdapter_Rules_UseCasesRule class attributes and methods

# UseCaseCodeAdapter_Rules_UseCaseRule class attributes and methods

# UseCaseCodeAdapter_Rules_UseCaseDescRule class attributes and methods

# UseCaseCodeAdapter_Rules_UseCaseDescPreCondRule class attributes and methods

# UseCaseCodeAdapter_Rules_ParallelStepRule class attributes and methods

# UseCaseCodeAdapter_Rules_UseCasePreCondRule class attributes and methods

# UseCaseCodeAdapter_Rules_BasicFlowRule class attributes and methods

# UseCaseCodeAdapter_NodeToAlternativeFlowAlternative class attributes and methods

# UseCaseCodeAdapter_Rules_FileToUCModel class attributes and methods

# UseCaseCodeAdapter_Rules_PackageRule class attributes and methods

# UseCaseCodeAdapter_Rules_ActorsRule class attributes and methods

# UseCaseCodeAdapter_Rules_ActorRule class attributes and methods

# UseCaseCodeAdapter_Rules_ActorDescRule class attributes and methods

# UseCaseCodeAdapter_Rules_UseCaseExtendsRule class attributes and methods

# UseCaseCodeAdapter_Rules_AltFlowAltContinueRule class attributes and methods

# UseCaseCodeAdapter_Rules_ParallelFlowInvokeRule class attributes and methods

# UseCaseCodeAdapter_Rules_ParallelStepInvokeRefRule class attributes and methods

# UseCaseCodeAdapter_Rules_AlternativeFlowRule class attributes and methods

# UseCaseCodeAdapter_Rules_ParallelFlowRule class attributes and methods

# UseCaseCodeAdapter_Rules_BasicFlowFinalStateRule class attributes and methods

# UseCaseCodeAdapter_Rules_ActorExtendsRule class attributes and methods

# UseCaseCodeAdapter_Rules_AltFlowFinalStateRule class attributes and methods

# UseCaseCodeAdapter_Rules_ParallelFlowFinalStateRule class attributes and methods

# UseCaseCodeAdapter_Rules_StepRule class attributes and methods

# UseCaseCodeAdapter_Rules_StepDescRule class attributes and methods

# UseCaseCodeAdapter_Rules_ParallelStepDescRule class attributes and methods

# UseCaseCodeAdapter_Rules_StepAlternativesRule class attributes and methods

# UseCaseCodeAdapter_Rules_AltFlowAltRule class attributes and methods

# Domain Model
domain_model = DomainModel(
    name="UseCaseCodeAdapter",
    types={UseCaseCodeAdapter_FileToUseCasesModel, UseCaseCodeAdapter_NodeToFlow, UseCaseCodeAdapter_NodeToStep, UseCaseCodeAdapter_NodeToPackageDeclaration, UseCaseCodeAdapter_NodeToActor, UseCaseCodeAdapter_NodeToUseCase, UseCaseCodeAdapter_Rules_UseCasesRule, UseCaseCodeAdapter_Rules_UseCaseRule, UseCaseCodeAdapter_Rules_UseCaseDescRule, UseCaseCodeAdapter_Rules_UseCaseDescPreCondRule, UseCaseCodeAdapter_Rules_ParallelStepRule, UseCaseCodeAdapter_Rules_UseCasePreCondRule, UseCaseCodeAdapter_Rules_BasicFlowRule, UseCaseCodeAdapter_NodeToAlternativeFlowAlternative, UseCaseCodeAdapter_Rules_FileToUCModel, UseCaseCodeAdapter_Rules_PackageRule, UseCaseCodeAdapter_Rules_ActorsRule, UseCaseCodeAdapter_Rules_ActorRule, UseCaseCodeAdapter_Rules_ActorDescRule, UseCaseCodeAdapter_Rules_UseCaseExtendsRule, UseCaseCodeAdapter_Rules_AltFlowAltContinueRule, UseCaseCodeAdapter_Rules_ParallelFlowInvokeRule, UseCaseCodeAdapter_Rules_ParallelStepInvokeRefRule, UseCaseCodeAdapter_Rules_AlternativeFlowRule, UseCaseCodeAdapter_Rules_ParallelFlowRule, UseCaseCodeAdapter_Rules_BasicFlowFinalStateRule, UseCaseCodeAdapter_Rules_ActorExtendsRule, UseCaseCodeAdapter_Rules_AltFlowFinalStateRule, UseCaseCodeAdapter_Rules_ParallelFlowFinalStateRule, UseCaseCodeAdapter_Rules_StepRule, UseCaseCodeAdapter_Rules_StepDescRule, UseCaseCodeAdapter_Rules_ParallelStepDescRule, UseCaseCodeAdapter_Rules_StepAlternativesRule, UseCaseCodeAdapter_Rules_AltFlowAltRule},
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