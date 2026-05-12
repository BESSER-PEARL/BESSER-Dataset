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
            EnumerationLiteral(name="SYSTEM"),
			EnumerationLiteral(name="PERSON"),
			EnumerationLiteral(name="ORGANIZATION")
    }
)

# Classes
useCases_UseCasesModel = Class(name="useCases_UseCasesModel")
useCases_ApplicationInstance = Class(name="useCases_ApplicationInstance")
useCases_Identifiable = Class(name="useCases_Identifiable")
useCases_NamespaceImport = Class(name="useCases_NamespaceImport")
useCases_PackageDeclaration = Class(name="useCases_PackageDeclaration")
useCases_RequirementRef = Class(name="useCases_RequirementRef")
useCases_Actor = Class(name="useCases_Actor")
useCases_UseCase = Class(name="useCases_UseCase")
useCases_Precondition = Class(name="useCases_Precondition")
useCases_Label = Class(name="useCases_Label")
useCases_BasicFlow = Class(name="useCases_BasicFlow")
useCases_AlternativeFlow = Class(name="useCases_AlternativeFlow")
useCases_ExceptionFlow = Class(name="useCases_ExceptionFlow")
useCases_CustomAttributes = Class(name="useCases_CustomAttributes")
useCases_Entity = Class(name="useCases_Entity")
useCases_PageRef = Class(name="useCases_PageRef")
useCases_Screen = Class(name="useCases_Screen")
useCases_Flow = Class(name="useCases_Flow")
useCases_Step = Class(name="useCases_Step")
useCases_ViewInstance = Class(name="useCases_ViewInstance")
Flow = Class(name="Flow")
NamedFlow = Class(name="NamedFlow")
useCases_EntityRef = Class(name="useCases_EntityRef")
useCases_NamedFlow = Class(name="useCases_NamedFlow")
useCases_CustomStepType = Class(name="useCases_CustomStepType")
useCases_Condition = Class(name="useCases_Condition")
StepAlternative = Class(name="StepAlternative")
useCases_LocalAlternative = Class(name="useCases_LocalAlternative")
useCases_StepAlternative = Class(name="useCases_StepAlternative")
useCases_Feature = Class(name="useCases_Feature")
useCases_AlternativeFlowAlternative = Class(name="useCases_AlternativeFlowAlternative")

# useCases_UseCasesModel class attributes and methods

# useCases_ApplicationInstance class attributes and methods

# useCases_Identifiable class attributes and methods

# useCases_NamespaceImport class attributes and methods

# useCases_PackageDeclaration class attributes and methods
useCases_PackageDeclaration_name: Property = Property(name="name", type=StringType)
useCases_PackageDeclaration_description: Property = Property(name="description", type=StringType)
useCases_PackageDeclaration.attributes={useCases_PackageDeclaration_description, useCases_PackageDeclaration_name}

# useCases_RequirementRef class attributes and methods

# useCases_Actor class attributes and methods
useCases_Actor_name: Property = Property(name="name", type=StringType)
useCases_Actor_type: Property = Property(name="type", type=StringType)
useCases_Actor_description: Property = Property(name="description", type=StringType)
useCases_Actor.attributes={useCases_Actor_name, useCases_Actor_type, useCases_Actor_description}

# useCases_UseCase class attributes and methods
useCases_UseCase_name: Property = Property(name="name", type=StringType)
useCases_UseCase_ucName: Property = Property(name="ucName", type=StringType)
useCases_UseCase_goals: Property = Property(name="goals", type=StringType)
useCases_UseCase.attributes={useCases_UseCase_ucName, useCases_UseCase_goals, useCases_UseCase_name}

# useCases_Precondition class attributes and methods
useCases_Precondition_name: Property = Property(name="name", type=StringType)
useCases_Precondition.attributes={useCases_Precondition_name}

# useCases_Label class attributes and methods

# useCases_BasicFlow class attributes and methods

# useCases_AlternativeFlow class attributes and methods

# useCases_ExceptionFlow class attributes and methods
useCases_ExceptionFlow_condition: Property = Property(name="condition", type=StringType)
useCases_ExceptionFlow.attributes={useCases_ExceptionFlow_condition}

# useCases_CustomAttributes class attributes and methods

# useCases_Entity class attributes and methods

# useCases_PageRef class attributes and methods

# useCases_Screen class attributes and methods

# useCases_Flow class attributes and methods
useCases_Flow_finalState: Property = Property(name="finalState", type=StringType)
useCases_Flow.attributes={useCases_Flow_finalState}

# useCases_Step class attributes and methods
useCases_Step_name: Property = Property(name="name", type=StringType)
useCases_Step_label: Property = Property(name="label", type=StringType)
useCases_Step_description: Property = Property(name="description", type=StringType)
useCases_Step.attributes={useCases_Step_label, useCases_Step_name, useCases_Step_description}

# useCases_ViewInstance class attributes and methods

# Flow class attributes and methods

# NamedFlow class attributes and methods

# useCases_EntityRef class attributes and methods

# useCases_NamedFlow class attributes and methods
useCases_NamedFlow_name: Property = Property(name="name", type=StringType)
useCases_NamedFlow.attributes={useCases_NamedFlow_name}

# useCases_CustomStepType class attributes and methods

# useCases_Condition class attributes and methods
useCases_Condition_condition: Property = Property(name="condition", type=StringType)
useCases_Condition.attributes={useCases_Condition_condition}

# StepAlternative class attributes and methods

# useCases_LocalAlternative class attributes and methods
useCases_LocalAlternative_description: Property = Property(name="description", type=StringType)
useCases_LocalAlternative.attributes={useCases_LocalAlternative_description}

# useCases_StepAlternative class attributes and methods
useCases_StepAlternative_finalizeFlow: Property = Property(name="finalizeFlow", type=BooleanType)
useCases_StepAlternative_finalState: Property = Property(name="finalState", type=StringType)
useCases_StepAlternative.attributes={useCases_StepAlternative_finalizeFlow, useCases_StepAlternative_finalState}

# useCases_Feature class attributes and methods

# useCases_AlternativeFlowAlternative class attributes and methods

# Relationships
refEntityImportedNamespace3: BinaryAssociation = BinaryAssociation(
    name="refEntityImportedNamespace3",
    ends={
        Property(name="useCases_PackageDeclaration5", type=useCases_NamespaceImport, multiplicity=Multiplicity(1, 1)),
        Property(name="useCases_NamespaceImport4", type=useCases_PackageDeclaration, multiplicity=Multiplicity(0, 1))
    }
)
refViewInstanceImportedNamespace6: BinaryAssociation = BinaryAssociation(
    name="refViewInstanceImportedNamespace6",
    ends={
        Property(name="useCases_ApplicationInstance", type=useCases_NamespaceImport, multiplicity=Multiplicity(1, 1)),
        Property(name="useCases_NamespaceImport7", type=useCases_ApplicationInstance, multiplicity=Multiplicity(0, 1))
    }
)
refRequirementImportedNamespace8: BinaryAssociation = BinaryAssociation(
    name="refRequirementImportedNamespace8",
    ends={
        Property(name="useCases_Identifiable", type=useCases_NamespaceImport, multiplicity=Multiplicity(1, 1)),
        Property(name="useCases_NamespaceImport9", type=useCases_Identifiable, multiplicity=Multiplicity(0, 1))
    }
)
refUseCaseImportedNamespace10: BinaryAssociation = BinaryAssociation(
    name="refUseCaseImportedNamespace10",
    ends={
        Property(name="useCases_PackageDeclaration12", type=useCases_NamespaceImport, multiplicity=Multiplicity(1, 1)),
        Property(name="useCases_NamespaceImport11", type=useCases_PackageDeclaration, multiplicity=Multiplicity(0, 1))
    }
)
refActorImportedNamespace13: BinaryAssociation = BinaryAssociation(
    name="refActorImportedNamespace13",
    ends={
        Property(name="useCases_PackageDeclaration15", type=useCases_NamespaceImport, multiplicity=Multiplicity(1, 1)),
        Property(name="useCases_NamespaceImport14", type=useCases_PackageDeclaration, multiplicity=Multiplicity(0, 1))
    }
)
namespaceImports16: BinaryAssociation = BinaryAssociation(
    name="namespaceImports16",
    ends={
        Property(name="useCases_NamespaceImport18", type=useCases_PackageDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="useCases_PackageDeclaration17", type=useCases_NamespaceImport, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
namespaceImports0: BinaryAssociation = BinaryAssociation(
    name="namespaceImports0",
    ends={
        Property(name="useCases_NamespaceImport", type=useCases_UseCasesModel, multiplicity=Multiplicity(1, 1)),
        Property(name="useCases_UseCasesModel", type=useCases_NamespaceImport, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
packages1: BinaryAssociation = BinaryAssociation(
    name="packages1",
    ends={
        Property(name="useCases_PackageDeclaration", type=useCases_UseCasesModel, multiplicity=Multiplicity(1, 1)),
        Property(name="useCases_UseCasesModel2", type=useCases_PackageDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
extends24: BinaryAssociation = BinaryAssociation(
    name="extends24",
    ends={
        Property(name="useCases_Actor25", type=useCases_Actor, multiplicity=Multiplicity(1, 1)),
        Property(name="useCases_Actor23", type=useCases_Actor, multiplicity=Multiplicity(0, 1))
    }
)
requirements26: BinaryAssociation = BinaryAssociation(
    name="requirements26",
    ends={
        Property(name="useCases_RequirementRef", type=useCases_UseCase, multiplicity=Multiplicity(1, 1)),
        Property(name="useCases_UseCase27", type=useCases_RequirementRef, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
actors19: BinaryAssociation = BinaryAssociation(
    name="actors19",
    ends={
        Property(name="useCases_Actor", type=useCases_PackageDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="useCases_PackageDeclaration20", type=useCases_Actor, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
useCases21: BinaryAssociation = BinaryAssociation(
    name="useCases21",
    ends={
        Property(name="useCases_UseCase", type=useCases_PackageDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="useCases_PackageDeclaration22", type=useCases_UseCase, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
preConditions35: BinaryAssociation = BinaryAssociation(
    name="preConditions35",
    ends={
        Property(name="useCases_Precondition", type=useCases_UseCase, multiplicity=Multiplicity(1, 1)),
        Property(name="useCases_UseCase36", type=useCases_Precondition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
commonLabels37: BinaryAssociation = BinaryAssociation(
    name="commonLabels37",
    ends={
        Property(name="useCases_Label", type=useCases_UseCase, multiplicity=Multiplicity(1, 1)),
        Property(name="useCases_UseCase38", type=useCases_Label, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
basicFlow39: BinaryAssociation = BinaryAssociation(
    name="basicFlow39",
    ends={
        Property(name="useCases_BasicFlow", type=useCases_UseCase, multiplicity=Multiplicity(1, 1)),
        Property(name="useCases_UseCase40", type=useCases_BasicFlow, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
alternativeFlows41: BinaryAssociation = BinaryAssociation(
    name="alternativeFlows41",
    ends={
        Property(name="useCases_AlternativeFlow", type=useCases_UseCase, multiplicity=Multiplicity(1, 1)),
        Property(name="useCases_UseCase42", type=useCases_AlternativeFlow, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
exceptionFlows43: BinaryAssociation = BinaryAssociation(
    name="exceptionFlows43",
    ends={
        Property(name="useCases_ExceptionFlow", type=useCases_UseCase, multiplicity=Multiplicity(1, 1)),
        Property(name="useCases_UseCase44", type=useCases_ExceptionFlow, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
customAttributes45: BinaryAssociation = BinaryAssociation(
    name="customAttributes45",
    ends={
        Property(name="useCases_CustomAttributes", type=useCases_UseCase, multiplicity=Multiplicity(1, 1)),
        Property(name="useCases_UseCase46", type=useCases_CustomAttributes, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
actors28: BinaryAssociation = BinaryAssociation(
    name="actors28",
    ends={
        Property(name="useCases_Actor30", type=useCases_UseCase, multiplicity=Multiplicity(1, 1)),
        Property(name="useCases_UseCase29", type=useCases_Actor, multiplicity=Multiplicity(0, 9999))
    }
)
entities31: BinaryAssociation = BinaryAssociation(
    name="entities31",
    ends={
        Property(name="useCases_Entity", type=useCases_UseCase, multiplicity=Multiplicity(1, 1)),
        Property(name="useCases_UseCase32", type=useCases_Entity, multiplicity=Multiplicity(0, 9999))
    }
)
pages33: BinaryAssociation = BinaryAssociation(
    name="pages33",
    ends={
        Property(name="useCases_PageRef", type=useCases_UseCase, multiplicity=Multiplicity(1, 1)),
        Property(name="useCases_UseCase34", type=useCases_PageRef, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
screens49: BinaryAssociation = BinaryAssociation(
    name="screens49",
    ends={
        Property(name="useCases_Screen", type=useCases_PageRef, multiplicity=Multiplicity(1, 1)),
        Property(name="useCases_PageRef50", type=useCases_Screen, multiplicity=Multiplicity(0, 9999))
    }
)
requires51: BinaryAssociation = BinaryAssociation(
    name="requires51",
    ends={
        Property(name="useCases_UseCase53", type=useCases_Precondition, multiplicity=Multiplicity(1, 1)),
        Property(name="useCases_Precondition52", type=useCases_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
page47: BinaryAssociation = BinaryAssociation(
    name="page47",
    ends={
        Property(name="useCases_ViewInstance", type=useCases_PageRef, multiplicity=Multiplicity(1, 1)),
        Property(name="useCases_PageRef48", type=useCases_ViewInstance, multiplicity=Multiplicity(0, 1))
    }
)
actor55: BinaryAssociation = BinaryAssociation(
    name="actor55",
    ends={
        Property(name="useCases_Actor57", type=useCases_Step, multiplicity=Multiplicity(1, 1)),
        Property(name="useCases_Step56", type=useCases_Actor, multiplicity=Multiplicity(0, 1))
    }
)
entityRefs58: BinaryAssociation = BinaryAssociation(
    name="entityRefs58",
    ends={
        Property(name="useCases_EntityRef", type=useCases_Step, multiplicity=Multiplicity(1, 1)),
        Property(name="useCases_Step59", type=useCases_EntityRef, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
steps54: BinaryAssociation = BinaryAssociation(
    name="steps54",
    ends={
        Property(name="useCases_Step", type=useCases_Flow, multiplicity=Multiplicity(1, 1)),
        Property(name="useCases_Flow", type=useCases_Step, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
customStepType68: BinaryAssociation = BinaryAssociation(
    name="customStepType68",
    ends={
        Property(name="useCases_CustomStepType", type=useCases_Step, multiplicity=Multiplicity(1, 1)),
        Property(name="useCases_Step69", type=useCases_CustomStepType, multiplicity=Multiplicity(0, 1))
    }
)
continuation70: BinaryAssociation = BinaryAssociation(
    name="continuation70",
    ends={
        Property(name="useCases_Step72", type=useCases_StepAlternative, multiplicity=Multiplicity(1, 1)),
        Property(name="useCases_StepAlternative71", type=useCases_Step, multiplicity=Multiplicity(0, 1))
    }
)
customStepType73: BinaryAssociation = BinaryAssociation(
    name="customStepType73",
    ends={
        Property(name="useCases_CustomStepType75", type=useCases_StepAlternative, multiplicity=Multiplicity(1, 1)),
        Property(name="useCases_StepAlternative74", type=useCases_CustomStepType, multiplicity=Multiplicity(0, 1))
    }
)
condition76: BinaryAssociation = BinaryAssociation(
    name="condition76",
    ends={
        Property(name="useCases_Condition", type=useCases_LocalAlternative, multiplicity=Multiplicity(1, 1)),
        Property(name="useCases_LocalAlternative", type=useCases_Condition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
screen60: BinaryAssociation = BinaryAssociation(
    name="screen60",
    ends={
        Property(name="useCases_Screen62", type=useCases_Step, multiplicity=Multiplicity(1, 1)),
        Property(name="useCases_Step61", type=useCases_Screen, multiplicity=Multiplicity(0, 1))
    }
)
invokedUseCase63: BinaryAssociation = BinaryAssociation(
    name="invokedUseCase63",
    ends={
        Property(name="useCases_UseCase65", type=useCases_Step, multiplicity=Multiplicity(1, 1)),
        Property(name="useCases_Step64", type=useCases_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
alternatives66: BinaryAssociation = BinaryAssociation(
    name="alternatives66",
    ends={
        Property(name="useCases_StepAlternative", type=useCases_Step, multiplicity=Multiplicity(1, 1)),
        Property(name="useCases_Step67", type=useCases_StepAlternative, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ref82: BinaryAssociation = BinaryAssociation(
    name="ref82",
    ends={
        Property(name="useCases_NamedFlow", type=useCases_AlternativeFlowAlternative, multiplicity=Multiplicity(1, 1)),
        Property(name="useCases_AlternativeFlowAlternative83", type=useCases_NamedFlow, multiplicity=Multiplicity(0, 1))
    }
)
entity84: BinaryAssociation = BinaryAssociation(
    name="entity84",
    ends={
        Property(name="useCases_Entity86", type=useCases_EntityRef, multiplicity=Multiplicity(1, 1)),
        Property(name="useCases_EntityRef85", type=useCases_Entity, multiplicity=Multiplicity(0, 1))
    }
)
features87: BinaryAssociation = BinaryAssociation(
    name="features87",
    ends={
        Property(name="useCases_Feature", type=useCases_EntityRef, multiplicity=Multiplicity(1, 1)),
        Property(name="useCases_EntityRef88", type=useCases_Feature, multiplicity=Multiplicity(0, 9999))
    }
)
invokedUseCase77: BinaryAssociation = BinaryAssociation(
    name="invokedUseCase77",
    ends={
        Property(name="useCases_UseCase79", type=useCases_LocalAlternative, multiplicity=Multiplicity(1, 1)),
        Property(name="useCases_LocalAlternative78", type=useCases_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
condition80: BinaryAssociation = BinaryAssociation(
    name="condition80",
    ends={
        Property(name="useCases_Condition81", type=useCases_AlternativeFlowAlternative, multiplicity=Multiplicity(1, 1)),
        Property(name="useCases_AlternativeFlowAlternative", type=useCases_Condition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_useCases_NamedFlow_Flow = Generalization(general=Flow, specific=useCases_NamedFlow)
gen_useCases_BasicFlow_Flow = Generalization(general=Flow, specific=useCases_BasicFlow)
gen_useCases_AlternativeFlow_NamedFlow = Generalization(general=NamedFlow, specific=useCases_AlternativeFlow)
gen_useCases_ExceptionFlow_NamedFlow = Generalization(general=NamedFlow, specific=useCases_ExceptionFlow)
gen_useCases_Condition_StepAlternative = Generalization(general=StepAlternative, specific=useCases_Condition)
gen_useCases_LocalAlternative_StepAlternative = Generalization(general=StepAlternative, specific=useCases_LocalAlternative)
gen_useCases_AlternativeFlowAlternative_StepAlternative = Generalization(general=StepAlternative, specific=useCases_AlternativeFlowAlternative)

# Domain Model
domain_model = DomainModel(
    name="useCases",
    types={useCases_UseCasesModel, useCases_ApplicationInstance, useCases_Identifiable, useCases_NamespaceImport, useCases_PackageDeclaration, useCases_RequirementRef, useCases_Actor, useCases_UseCase, useCases_Precondition, useCases_Label, useCases_BasicFlow, useCases_AlternativeFlow, useCases_ExceptionFlow, useCases_CustomAttributes, useCases_Entity, useCases_PageRef, useCases_Screen, useCases_Flow, useCases_Step, useCases_ViewInstance, Flow, NamedFlow, useCases_EntityRef, useCases_NamedFlow, useCases_CustomStepType, useCases_Condition, StepAlternative, useCases_LocalAlternative, useCases_StepAlternative, useCases_Feature, useCases_AlternativeFlowAlternative, ActorType},
    associations={refEntityImportedNamespace3, refViewInstanceImportedNamespace6, refRequirementImportedNamespace8, refUseCaseImportedNamespace10, refActorImportedNamespace13, namespaceImports16, namespaceImports0, packages1, extends24, requirements26, actors19, useCases21, preConditions35, commonLabels37, basicFlow39, alternativeFlows41, exceptionFlows43, customAttributes45, actors28, entities31, pages33, screens49, requires51, page47, actor55, entityRefs58, steps54, customStepType68, continuation70, customStepType73, condition76, screen60, invokedUseCase63, alternatives66, ref82, entity84, features87, invokedUseCase77, condition80},
    generalizations={gen_useCases_NamedFlow_Flow, gen_useCases_BasicFlow_Flow, gen_useCases_AlternativeFlow_NamedFlow, gen_useCases_ExceptionFlow_NamedFlow, gen_useCases_Condition_StepAlternative, gen_useCases_LocalAlternative_StepAlternative, gen_useCases_AlternativeFlowAlternative_StepAlternative},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)