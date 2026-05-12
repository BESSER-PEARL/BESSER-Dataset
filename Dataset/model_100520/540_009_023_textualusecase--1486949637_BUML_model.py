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
textualusecase_UseCaseModel = Class(name="textualusecase_UseCaseModel")
textualusecase_BasicFlow = Class(name="textualusecase_BasicFlow")
textualusecase_UseCase = Class(name="textualusecase_UseCase")
textualusecase_Actor = Class(name="textualusecase_Actor")
textualusecase_Subject = Class(name="textualusecase_Subject")
textualusecase_AlternativeFlow = Class(name="textualusecase_AlternativeFlow")
textualusecase_Step = Class(name="textualusecase_Step", is_abstract=True)
textualusecase_Condition = Class(name="textualusecase_Condition")
textualusecase_Include = Class(name="textualusecase_Include")
FlowOfEvents = Class(name="FlowOfEvents")
textualusecase_Agent = Class(name="textualusecase_Agent", is_abstract=True)
textualusecase_Action = Class(name="textualusecase_Action")
textualusecase_FlowOfEvents = Class(name="textualusecase_FlowOfEvents", is_abstract=True)
textualusecase_Statement = Class(name="textualusecase_Statement", is_abstract=True)
Agent = Class(name="Agent")
Step = Class(name="Step")
textualusecase_ConditionalStatement = Class(name="textualusecase_ConditionalStatement")
Statement = Class(name="Statement")
textualusecase_LoopStatement = Class(name="textualusecase_LoopStatement")

# textualusecase_UseCaseModel class attributes and methods

# textualusecase_BasicFlow class attributes and methods

# textualusecase_UseCase class attributes and methods
textualusecase_UseCase_name: Property = Property(name="name", type=StringType)
textualusecase_UseCase_description: Property = Property(name="description", type=StringType)
textualusecase_UseCase.attributes={textualusecase_UseCase_description, textualusecase_UseCase_name}

# textualusecase_Actor class attributes and methods

# textualusecase_Subject class attributes and methods

# textualusecase_AlternativeFlow class attributes and methods

# textualusecase_Step class attributes and methods
textualusecase_Step_name: Property = Property(name="name", type=StringType)
textualusecase_Step.attributes={textualusecase_Step_name}

# textualusecase_Condition class attributes and methods
textualusecase_Condition_expression: Property = Property(name="expression", type=StringType)
textualusecase_Condition.attributes={textualusecase_Condition_expression}

# textualusecase_Include class attributes and methods

# FlowOfEvents class attributes and methods

# textualusecase_Agent class attributes and methods
textualusecase_Agent_name: Property = Property(name="name", type=StringType)
textualusecase_Agent.attributes={textualusecase_Agent_name}

# textualusecase_Action class attributes and methods
textualusecase_Action_description: Property = Property(name="description", type=StringType)
textualusecase_Action.attributes={textualusecase_Action_description}

# textualusecase_FlowOfEvents class attributes and methods
textualusecase_FlowOfEvents_name: Property = Property(name="name", type=StringType)
textualusecase_FlowOfEvents.attributes={textualusecase_FlowOfEvents_name}

# textualusecase_Statement class attributes and methods

# Agent class attributes and methods

# Step class attributes and methods

# textualusecase_ConditionalStatement class attributes and methods

# Statement class attributes and methods

# textualusecase_LoopStatement class attributes and methods

# Relationships
basicFlow5: BinaryAssociation = BinaryAssociation(
    name="basicFlow5",
    ends={
        Property(name="BasicFlow", type=textualusecase_UseCase, multiplicity=Multiplicity(1, 1)),
        Property(name="useCase6", type=textualusecase_BasicFlow, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
actor7: BinaryAssociation = BinaryAssociation(
    name="actor7",
    ends={
        Property(name="Actor9", type=textualusecase_UseCase, multiplicity=Multiplicity(1, 1)),
        Property(name="useCase8", type=textualusecase_Actor, multiplicity=Multiplicity(1, 9999))
    }
)
useCase0: BinaryAssociation = BinaryAssociation(
    name="useCase0",
    ends={
        Property(name="UseCase", type=textualusecase_UseCaseModel, multiplicity=Multiplicity(1, 1)),
        Property(name="useCaseModel", type=textualusecase_UseCase, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
actor1: BinaryAssociation = BinaryAssociation(
    name="actor1",
    ends={
        Property(name="Actor", type=textualusecase_UseCaseModel, multiplicity=Multiplicity(1, 1)),
        Property(name="useCaseModel2", type=textualusecase_Actor, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
subject3: BinaryAssociation = BinaryAssociation(
    name="subject3",
    ends={
        Property(name="Subject", type=textualusecase_UseCaseModel, multiplicity=Multiplicity(1, 1)),
        Property(name="useCasemodel", type=textualusecase_Subject, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
alternativeFlow4: BinaryAssociation = BinaryAssociation(
    name="alternativeFlow4",
    ends={
        Property(name="AlternativeFlow", type=textualusecase_UseCase, multiplicity=Multiplicity(1, 1)),
        Property(name="useCase", type=textualusecase_AlternativeFlow, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
branchingStep18: BinaryAssociation = BinaryAssociation(
    name="branchingStep18",
    ends={
        Property(name="Step", type=textualusecase_AlternativeFlow, multiplicity=Multiplicity(1, 1)),
        Property(name="alternativeFlow", type=textualusecase_Step, multiplicity=Multiplicity(1, 1))
    }
)
condition19: BinaryAssociation = BinaryAssociation(
    name="condition19",
    ends={
        Property(name="textualusecase_Condition20", type=textualusecase_AlternativeFlow, multiplicity=Multiplicity(1, 1)),
        Property(name="textualusecase_AlternativeFlow", type=textualusecase_Condition, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
useCase21: BinaryAssociation = BinaryAssociation(
    name="useCase21",
    ends={
        Property(name="UseCase23", type=textualusecase_AlternativeFlow, multiplicity=Multiplicity(1, 1)),
        Property(name="alternativeFlow22", type=textualusecase_UseCase, multiplicity=Multiplicity(1, 1))
    }
)
postCondition10: BinaryAssociation = BinaryAssociation(
    name="postCondition10",
    ends={
        Property(name="textualusecase_Condition", type=textualusecase_UseCase, multiplicity=Multiplicity(1, 1)),
        Property(name="textualusecase_UseCase", type=textualusecase_Condition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
preCondition11: BinaryAssociation = BinaryAssociation(
    name="preCondition11",
    ends={
        Property(name="textualusecase_Condition13", type=textualusecase_UseCase, multiplicity=Multiplicity(1, 1)),
        Property(name="textualusecase_UseCase12", type=textualusecase_Condition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
useCaseModel14: BinaryAssociation = BinaryAssociation(
    name="useCaseModel14",
    ends={
        Property(name="UseCaseModel", type=textualusecase_UseCase, multiplicity=Multiplicity(1, 1)),
        Property(name="useCase15", type=textualusecase_UseCaseModel, multiplicity=Multiplicity(1, 1))
    }
)
includes16: BinaryAssociation = BinaryAssociation(
    name="includes16",
    ends={
        Property(name="Include", type=textualusecase_UseCase, multiplicity=Multiplicity(1, 1)),
        Property(name="useCase17", type=textualusecase_Include, multiplicity=Multiplicity(0, 9999))
    }
)
flowOfEvents29: BinaryAssociation = BinaryAssociation(
    name="flowOfEvents29",
    ends={
        Property(name="FlowOfEvents", type=textualusecase_Step, multiplicity=Multiplicity(1, 1)),
        Property(name="steps30", type=textualusecase_FlowOfEvents, multiplicity=Multiplicity(0, 1))
    }
)
steps24: BinaryAssociation = BinaryAssociation(
    name="steps24",
    ends={
        Property(name="Step25", type=textualusecase_FlowOfEvents, multiplicity=Multiplicity(1, 1)),
        Property(name="flowOfEvents", type=textualusecase_Step, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
alternativeFlow26: BinaryAssociation = BinaryAssociation(
    name="alternativeFlow26",
    ends={
        Property(name="AlternativeFlow27", type=textualusecase_Step, multiplicity=Multiplicity(1, 1)),
        Property(name="branchingStep", type=textualusecase_AlternativeFlow, multiplicity=Multiplicity(0, 9999))
    }
)
statement28: BinaryAssociation = BinaryAssociation(
    name="statement28",
    ends={
        Property(name="Statement", type=textualusecase_Step, multiplicity=Multiplicity(1, 1)),
        Property(name="steps", type=textualusecase_Statement, multiplicity=Multiplicity(0, 1))
    }
)
useCase36: BinaryAssociation = BinaryAssociation(
    name="useCase36",
    ends={
        Property(name="UseCase37", type=textualusecase_BasicFlow, multiplicity=Multiplicity(1, 1)),
        Property(name="basicFlow", type=textualusecase_UseCase, multiplicity=Multiplicity(1, 1))
    }
)
useCaseModel38: BinaryAssociation = BinaryAssociation(
    name="useCaseModel38",
    ends={
        Property(name="UseCaseModel39", type=textualusecase_Actor, multiplicity=Multiplicity(1, 1)),
        Property(name="actor", type=textualusecase_UseCaseModel, multiplicity=Multiplicity(1, 1))
    }
)
actions31: BinaryAssociation = BinaryAssociation(
    name="actions31",
    ends={
        Property(name="Action", type=textualusecase_Agent, multiplicity=Multiplicity(1, 1)),
        Property(name="agent", type=textualusecase_Action, multiplicity=Multiplicity(0, 9999))
    }
)
condition32: BinaryAssociation = BinaryAssociation(
    name="condition32",
    ends={
        Property(name="textualusecase_Condition33", type=textualusecase_Statement, multiplicity=Multiplicity(1, 1)),
        Property(name="textualusecase_Statement", type=textualusecase_Condition, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
steps34: BinaryAssociation = BinaryAssociation(
    name="steps34",
    ends={
        Property(name="Step35", type=textualusecase_Statement, multiplicity=Multiplicity(1, 1)),
        Property(name="statement", type=textualusecase_Step, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
useCase46: BinaryAssociation = BinaryAssociation(
    name="useCase46",
    ends={
        Property(name="UseCase47", type=textualusecase_Include, multiplicity=Multiplicity(1, 1)),
        Property(name="includes", type=textualusecase_UseCase, multiplicity=Multiplicity(1, 1))
    }
)
useCase40: BinaryAssociation = BinaryAssociation(
    name="useCase40",
    ends={
        Property(name="UseCase42", type=textualusecase_Actor, multiplicity=Multiplicity(1, 1)),
        Property(name="actor41", type=textualusecase_UseCase, multiplicity=Multiplicity(0, 9999))
    }
)
useCasemodel43: BinaryAssociation = BinaryAssociation(
    name="useCasemodel43",
    ends={
        Property(name="UseCaseModel44", type=textualusecase_Subject, multiplicity=Multiplicity(1, 1)),
        Property(name="subject", type=textualusecase_UseCaseModel, multiplicity=Multiplicity(1, 1))
    }
)
agent45: BinaryAssociation = BinaryAssociation(
    name="agent45",
    ends={
        Property(name="Agent", type=textualusecase_Action, multiplicity=Multiplicity(1, 1)),
        Property(name="actions", type=textualusecase_Agent, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_textualusecase_AlternativeFlow_FlowOfEvents = Generalization(general=FlowOfEvents, specific=textualusecase_AlternativeFlow)
gen_textualusecase_Actor_Agent = Generalization(general=Agent, specific=textualusecase_Actor)
gen_textualusecase_Statement_Step = Generalization(general=Step, specific=textualusecase_Statement)
gen_textualusecase_BasicFlow_FlowOfEvents = Generalization(general=FlowOfEvents, specific=textualusecase_BasicFlow)
gen_textualusecase_Include_Step = Generalization(general=Step, specific=textualusecase_Include)
gen_textualusecase_Subject_Agent = Generalization(general=Agent, specific=textualusecase_Subject)
gen_textualusecase_Action_Step = Generalization(general=Step, specific=textualusecase_Action)
gen_textualusecase_ConditionalStatement_Statement = Generalization(general=Statement, specific=textualusecase_ConditionalStatement)
gen_textualusecase_LoopStatement_Statement = Generalization(general=Statement, specific=textualusecase_LoopStatement)

# Domain Model
domain_model = DomainModel(
    name="textualusecase",
    types={textualusecase_UseCaseModel, textualusecase_BasicFlow, textualusecase_UseCase, textualusecase_Actor, textualusecase_Subject, textualusecase_AlternativeFlow, textualusecase_Step, textualusecase_Condition, textualusecase_Include, FlowOfEvents, textualusecase_Agent, textualusecase_Action, textualusecase_FlowOfEvents, textualusecase_Statement, Agent, Step, textualusecase_ConditionalStatement, Statement, textualusecase_LoopStatement},
    associations={basicFlow5, actor7, useCase0, actor1, subject3, alternativeFlow4, branchingStep18, condition19, useCase21, postCondition10, preCondition11, useCaseModel14, includes16, flowOfEvents29, steps24, alternativeFlow26, statement28, useCase36, useCaseModel38, actions31, condition32, steps34, useCase46, useCase40, useCasemodel43, agent45},
    generalizations={gen_textualusecase_AlternativeFlow_FlowOfEvents, gen_textualusecase_Actor_Agent, gen_textualusecase_Statement_Step, gen_textualusecase_BasicFlow_FlowOfEvents, gen_textualusecase_Include_Step, gen_textualusecase_Subject_Agent, gen_textualusecase_Action_Step, gen_textualusecase_ConditionalStatement_Statement, gen_textualusecase_LoopStatement_Statement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)