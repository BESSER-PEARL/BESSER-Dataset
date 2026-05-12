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
ActorType: Enumeration = Enumeration(
    name="ActorType",
    literals={
            EnumerationLiteral(name="PERSON"),
			EnumerationLiteral(name="SYSTEM"),
			EnumerationLiteral(name="ORGANIZATION")
    }
)

CustomStepType: Enumeration = Enumeration(
    name="CustomStepType",
    literals={
            EnumerationLiteral(name="MIX"),
			EnumerationLiteral(name="INPUT"),
			EnumerationLiteral(name="OUTPUT"),
			EnumerationLiteral(name="PROCESS")
    }
)

# Classes
UseCaseDSL_AlternativeFlow = Class(name="UseCaseDSL_AlternativeFlow")
NamedFlow = Class(name="NamedFlow")
UseCaseDSL_AlternativeFlowAlternative = Class(name="UseCaseDSL_AlternativeFlowAlternative")
StepAlternative = Class(name="StepAlternative")
UseCaseDSL_NamedFlow = Class(name="UseCaseDSL_NamedFlow", is_abstract=True)
UseCaseDSL_BasicFlow = Class(name="UseCaseDSL_BasicFlow")
Flow = Class(name="Flow")
UseCaseDSL_Condition = Class(name="UseCaseDSL_Condition")
UseCaseDSL_ExceptionFlow = Class(name="UseCaseDSL_ExceptionFlow")
UseCaseDSL_Flow = Class(name="UseCaseDSL_Flow", is_abstract=True)
UseCaseDSL_Actor = Class(name="UseCaseDSL_Actor")
UseCaseDSL_NormalStep = Class(name="UseCaseDSL_NormalStep")
Step = Class(name="Step")
UseCaseDSL_Step = Class(name="UseCaseDSL_Step", is_abstract=True)
UseCaseDSL_LocalAlternative = Class(name="UseCaseDSL_LocalAlternative")
UseCaseDSL_UseCase = Class(name="UseCaseDSL_UseCase")
UseCaseDSL_PackageDeclaration = Class(name="UseCaseDSL_PackageDeclaration")
UseCaseDSL_ParallelFlow = Class(name="UseCaseDSL_ParallelFlow")
UseCaseDSL_ParallelStep = Class(name="UseCaseDSL_ParallelStep")
UseCaseDSL_StepAlternative = Class(name="UseCaseDSL_StepAlternative", is_abstract=True)
UseCaseDSL_UseCasesModel = Class(name="UseCaseDSL_UseCasesModel")

# UseCaseDSL_AlternativeFlow class attributes and methods

# NamedFlow class attributes and methods

# UseCaseDSL_AlternativeFlowAlternative class attributes and methods

# StepAlternative class attributes and methods

# UseCaseDSL_NamedFlow class attributes and methods
UseCaseDSL_NamedFlow_name: Property = Property(name="name", type=StringType)
UseCaseDSL_NamedFlow.attributes={UseCaseDSL_NamedFlow_name}

# UseCaseDSL_BasicFlow class attributes and methods

# Flow class attributes and methods

# UseCaseDSL_Condition class attributes and methods

# UseCaseDSL_ExceptionFlow class attributes and methods
UseCaseDSL_ExceptionFlow_condition: Property = Property(name="condition", type=StringType)
UseCaseDSL_ExceptionFlow.attributes={UseCaseDSL_ExceptionFlow_condition}

# UseCaseDSL_Flow class attributes and methods
UseCaseDSL_Flow_finalState: Property = Property(name="finalState", type=StringType)
UseCaseDSL_Flow.attributes={UseCaseDSL_Flow_finalState}

# UseCaseDSL_Actor class attributes and methods
UseCaseDSL_Actor_description: Property = Property(name="description", type=StringType)
UseCaseDSL_Actor_name: Property = Property(name="name", type=StringType)
UseCaseDSL_Actor_type: Property = Property(name="type", type=StringType)
UseCaseDSL_Actor.attributes={UseCaseDSL_Actor_type, UseCaseDSL_Actor_name, UseCaseDSL_Actor_description}

# UseCaseDSL_NormalStep class attributes and methods
UseCaseDSL_NormalStep_customStepType: Property = Property(name="customStepType", type=StringType)
UseCaseDSL_NormalStep.attributes={UseCaseDSL_NormalStep_customStepType}

# Step class attributes and methods

# UseCaseDSL_Step class attributes and methods
UseCaseDSL_Step_label: Property = Property(name="label", type=StringType)
UseCaseDSL_Step_name: Property = Property(name="name", type=StringType)
UseCaseDSL_Step.attributes={UseCaseDSL_Step_name, UseCaseDSL_Step_label}

# UseCaseDSL_LocalAlternative class attributes and methods
UseCaseDSL_LocalAlternative_description: Property = Property(name="description", type=StringType)
UseCaseDSL_LocalAlternative.attributes={UseCaseDSL_LocalAlternative_description}

# UseCaseDSL_UseCase class attributes and methods
UseCaseDSL_UseCase_description: Property = Property(name="description", type=StringType)
UseCaseDSL_UseCase_name: Property = Property(name="name", type=StringType)
UseCaseDSL_UseCase_postcondition: Property = Property(name="postcondition", type=StringType)
UseCaseDSL_UseCase_preConditions: Property = Property(name="preConditions", type=StringType)
UseCaseDSL_UseCase.attributes={UseCaseDSL_UseCase_preConditions, UseCaseDSL_UseCase_name, UseCaseDSL_UseCase_description, UseCaseDSL_UseCase_postcondition}

# UseCaseDSL_PackageDeclaration class attributes and methods
UseCaseDSL_PackageDeclaration_description: Property = Property(name="description", type=StringType)
UseCaseDSL_PackageDeclaration_name: Property = Property(name="name", type=StringType)
UseCaseDSL_PackageDeclaration.attributes={UseCaseDSL_PackageDeclaration_name, UseCaseDSL_PackageDeclaration_description}

# UseCaseDSL_ParallelFlow class attributes and methods

# UseCaseDSL_ParallelStep class attributes and methods

# UseCaseDSL_StepAlternative class attributes and methods
UseCaseDSL_StepAlternative_condition: Property = Property(name="condition", type=StringType)
UseCaseDSL_StepAlternative.attributes={UseCaseDSL_StepAlternative_condition}

# UseCaseDSL_UseCasesModel class attributes and methods

# Relationships
ref2: BinaryAssociation = BinaryAssociation(
    name="ref2",
    ends={
        Property(name="UseCaseDSL_NamedFlow", type=UseCaseDSL_AlternativeFlowAlternative, multiplicity=Multiplicity(1, 1)),
        Property(name="UseCaseDSL_AlternativeFlowAlternative", type=UseCaseDSL_NamedFlow, multiplicity=Multiplicity(0, 1))
    }
)
extends1: BinaryAssociation = BinaryAssociation(
    name="extends1",
    ends={
        Property(name="UseCaseDSL_Actor", type=UseCaseDSL_Actor, multiplicity=Multiplicity(1, 1)),
        Property(name="UseCaseDSL_Actor0", type=UseCaseDSL_Actor, multiplicity=Multiplicity(0, 1))
    }
)
steps3: BinaryAssociation = BinaryAssociation(
    name="steps3",
    ends={
        Property(name="UseCaseDSL_Step", type=UseCaseDSL_Flow, multiplicity=Multiplicity(1, 1)),
        Property(name="UseCaseDSL_Flow", type=UseCaseDSL_Step, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
invokedUseCase4: BinaryAssociation = BinaryAssociation(
    name="invokedUseCase4",
    ends={
        Property(name="UseCaseDSL_UseCase", type=UseCaseDSL_LocalAlternative, multiplicity=Multiplicity(1, 1)),
        Property(name="UseCaseDSL_LocalAlternative", type=UseCaseDSL_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
actor6: BinaryAssociation = BinaryAssociation(
    name="actor6",
    ends={
        Property(name="UseCaseDSL_Actor8", type=UseCaseDSL_NormalStep, multiplicity=Multiplicity(1, 1)),
        Property(name="UseCaseDSL_NormalStep7", type=UseCaseDSL_Actor, multiplicity=Multiplicity(0, 1))
    }
)
useCases9: BinaryAssociation = BinaryAssociation(
    name="useCases9",
    ends={
        Property(name="UseCaseDSL_UseCase10", type=UseCaseDSL_PackageDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="UseCaseDSL_PackageDeclaration", type=UseCaseDSL_UseCase, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
actors11: BinaryAssociation = BinaryAssociation(
    name="actors11",
    ends={
        Property(name="UseCaseDSL_Actor13", type=UseCaseDSL_PackageDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="UseCaseDSL_PackageDeclaration12", type=UseCaseDSL_Actor, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
stepAlternative5: BinaryAssociation = BinaryAssociation(
    name="stepAlternative5",
    ends={
        Property(name="UseCaseDSL_StepAlternative", type=UseCaseDSL_NormalStep, multiplicity=Multiplicity(1, 1)),
        Property(name="UseCaseDSL_NormalStep", type=UseCaseDSL_StepAlternative, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
continuation21: BinaryAssociation = BinaryAssociation(
    name="continuation21",
    ends={
        Property(name="UseCaseDSL_Step23", type=UseCaseDSL_StepAlternative, multiplicity=Multiplicity(1, 1)),
        Property(name="UseCaseDSL_StepAlternative22", type=UseCaseDSL_Step, multiplicity=Multiplicity(0, 1))
    }
)
superCase25: BinaryAssociation = BinaryAssociation(
    name="superCase25",
    ends={
        Property(name="UseCaseDSL_UseCase26", type=UseCaseDSL_UseCase, multiplicity=Multiplicity(1, 1)),
        Property(name="UseCaseDSL_UseCase24", type=UseCaseDSL_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
flows27: BinaryAssociation = BinaryAssociation(
    name="flows27",
    ends={
        Property(name="UseCaseDSL_Flow29", type=UseCaseDSL_UseCase, multiplicity=Multiplicity(1, 1)),
        Property(name="UseCaseDSL_UseCase28", type=UseCaseDSL_Flow, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
invokedFlows14: BinaryAssociation = BinaryAssociation(
    name="invokedFlows14",
    ends={
        Property(name="UseCaseDSL_ParallelFlow", type=UseCaseDSL_ParallelStep, multiplicity=Multiplicity(1, 1)),
        Property(name="UseCaseDSL_ParallelStep", type=UseCaseDSL_ParallelFlow, multiplicity=Multiplicity(0, 9999))
    }
)
next16: BinaryAssociation = BinaryAssociation(
    name="next16",
    ends={
        Property(name="UseCaseDSL_Step17", type=UseCaseDSL_Step, multiplicity=Multiplicity(1, 1)),
        Property(name="UseCaseDSL_Step15", type=UseCaseDSL_Step, multiplicity=Multiplicity(0, 1))
    }
)
invokedUseCase18: BinaryAssociation = BinaryAssociation(
    name="invokedUseCase18",
    ends={
        Property(name="UseCaseDSL_UseCase20", type=UseCaseDSL_Step, multiplicity=Multiplicity(1, 1)),
        Property(name="UseCaseDSL_Step19", type=UseCaseDSL_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
packages30: BinaryAssociation = BinaryAssociation(
    name="packages30",
    ends={
        Property(name="UseCaseDSL_PackageDeclaration31", type=UseCaseDSL_UseCasesModel, multiplicity=Multiplicity(1, 1)),
        Property(name="UseCaseDSL_UseCasesModel", type=UseCaseDSL_PackageDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_UseCaseDSL_AlternativeFlow_NamedFlow = Generalization(general=NamedFlow, specific=UseCaseDSL_AlternativeFlow)
gen_UseCaseDSL_AlternativeFlowAlternative_StepAlternative = Generalization(general=StepAlternative, specific=UseCaseDSL_AlternativeFlowAlternative)
gen_UseCaseDSL_BasicFlow_Flow = Generalization(general=Flow, specific=UseCaseDSL_BasicFlow)
gen_UseCaseDSL_Condition_StepAlternative = Generalization(general=StepAlternative, specific=UseCaseDSL_Condition)
gen_UseCaseDSL_ExceptionFlow_NamedFlow = Generalization(general=NamedFlow, specific=UseCaseDSL_ExceptionFlow)
gen_UseCaseDSL_NamedFlow_Flow = Generalization(general=Flow, specific=UseCaseDSL_NamedFlow)
gen_UseCaseDSL_NormalStep_Step = Generalization(general=Step, specific=UseCaseDSL_NormalStep)
gen_UseCaseDSL_LocalAlternative_StepAlternative = Generalization(general=StepAlternative, specific=UseCaseDSL_LocalAlternative)
gen_UseCaseDSL_ParallelFlow_NamedFlow = Generalization(general=NamedFlow, specific=UseCaseDSL_ParallelFlow)
gen_UseCaseDSL_ParallelStep_Step = Generalization(general=Step, specific=UseCaseDSL_ParallelStep)

# Domain Model
domain_model = DomainModel(
    name="UseCaseDSL",
    types={UseCaseDSL_AlternativeFlow, NamedFlow, UseCaseDSL_AlternativeFlowAlternative, StepAlternative, UseCaseDSL_NamedFlow, UseCaseDSL_BasicFlow, Flow, UseCaseDSL_Condition, UseCaseDSL_ExceptionFlow, UseCaseDSL_Flow, UseCaseDSL_Actor, UseCaseDSL_NormalStep, Step, UseCaseDSL_Step, UseCaseDSL_LocalAlternative, UseCaseDSL_UseCase, UseCaseDSL_PackageDeclaration, UseCaseDSL_ParallelFlow, UseCaseDSL_ParallelStep, UseCaseDSL_StepAlternative, UseCaseDSL_UseCasesModel, ActorType, CustomStepType},
    associations={ref2, extends1, steps3, invokedUseCase4, actor6, useCases9, actors11, stepAlternative5, continuation21, superCase25, flows27, invokedFlows14, next16, invokedUseCase18, packages30},
    generalizations={gen_UseCaseDSL_AlternativeFlow_NamedFlow, gen_UseCaseDSL_AlternativeFlowAlternative_StepAlternative, gen_UseCaseDSL_BasicFlow_Flow, gen_UseCaseDSL_Condition_StepAlternative, gen_UseCaseDSL_ExceptionFlow_NamedFlow, gen_UseCaseDSL_NamedFlow_Flow, gen_UseCaseDSL_NormalStep_Step, gen_UseCaseDSL_LocalAlternative_StepAlternative, gen_UseCaseDSL_ParallelFlow_NamedFlow, gen_UseCaseDSL_ParallelStep_Step},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)