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
FSMModel_State = Class(name="FSMModel_State")
NamedElement = Class(name="NamedElement")
FSMModel_Transition = Class(name="FSMModel_Transition")
FSMModel_AbstractAction = Class(name="FSMModel_AbstractAction", is_abstract=True)
FSMModel_StateMachineDefinition = Class(name="FSMModel_StateMachineDefinition")
FSMModel_DeclarationBlock = Class(name="FSMModel_DeclarationBlock")
FSMModel_AbstractGuard = Class(name="FSMModel_AbstractGuard", is_abstract=True)
FSMModel_AbstractTrigger = Class(name="FSMModel_AbstractTrigger", is_abstract=True)
FSMModel_Guard = Class(name="FSMModel_Guard")
AbstractGuard = Class(name="AbstractGuard")
ClassicalExpression_BooleanExpression = Class(name="ClassicalExpression_BooleanExpression")
FSMModel_Trigger = Class(name="FSMModel_Trigger")
ClockExpressionAndRelation_ConcreteEntity = Class(name="ClockExpressionAndRelation_ConcreteEntity")
ClassicalExpression_ClassicalExpression = Class(name="ClassicalExpression_ClassicalExpression")
AbstractTrigger = Class(name="AbstractTrigger")
ClockExpressionAndRelation_BindableEntity = Class(name="ClockExpressionAndRelation_BindableEntity")
FSMModel_IntegerAssignement = Class(name="FSMModel_IntegerAssignement")
ClassicalExpression_BinaryIntegerExpression = Class(name="ClassicalExpression_BinaryIntegerExpression")
AbstractAction = Class(name="AbstractAction")

# FSMModel_State class attributes and methods

# NamedElement class attributes and methods

# FSMModel_Transition class attributes and methods

# FSMModel_AbstractAction class attributes and methods

# FSMModel_StateMachineDefinition class attributes and methods

# FSMModel_DeclarationBlock class attributes and methods

# FSMModel_AbstractGuard class attributes and methods

# FSMModel_AbstractTrigger class attributes and methods

# FSMModel_Guard class attributes and methods

# AbstractGuard class attributes and methods

# ClassicalExpression_BooleanExpression class attributes and methods

# FSMModel_Trigger class attributes and methods

# ClockExpressionAndRelation_ConcreteEntity class attributes and methods

# ClassicalExpression_ClassicalExpression class attributes and methods

# AbstractTrigger class attributes and methods

# ClockExpressionAndRelation_BindableEntity class attributes and methods

# FSMModel_IntegerAssignement class attributes and methods

# ClassicalExpression_BinaryIntegerExpression class attributes and methods

# AbstractAction class attributes and methods

# Relationships
outputTransitions1: BinaryAssociation = BinaryAssociation(
    name="outputTransitions1",
    ends={
        Property(name="Transition2", type=FSMModel_State, multiplicity=Multiplicity(1, 1)),
        Property(name="source", type=FSMModel_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
source3: BinaryAssociation = BinaryAssociation(
    name="source3",
    ends={
        Property(name="State", type=FSMModel_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="outputTransitions", type=FSMModel_State, multiplicity=Multiplicity(1, 1))
    }
)
inputTransitions0: BinaryAssociation = BinaryAssociation(
    name="inputTransitions0",
    ends={
        Property(name="Transition", type=FSMModel_State, multiplicity=Multiplicity(1, 1)),
        Property(name="target", type=FSMModel_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
actions9: BinaryAssociation = BinaryAssociation(
    name="actions9",
    ends={
        Property(name="FSMModel_AbstractAction", type=FSMModel_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="FSMModel_Transition10", type=FSMModel_AbstractAction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
declarationBlock11: BinaryAssociation = BinaryAssociation(
    name="declarationBlock11",
    ends={
        Property(name="FSMModel_DeclarationBlock", type=FSMModel_StateMachineDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="FSMModel_StateMachineDefinition", type=FSMModel_DeclarationBlock, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
transitions12: BinaryAssociation = BinaryAssociation(
    name="transitions12",
    ends={
        Property(name="FSMModel_Transition14", type=FSMModel_StateMachineDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="FSMModel_StateMachineDefinition13", type=FSMModel_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
target4: BinaryAssociation = BinaryAssociation(
    name="target4",
    ends={
        Property(name="State5", type=FSMModel_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="inputTransitions", type=FSMModel_State, multiplicity=Multiplicity(1, 1))
    }
)
guard6: BinaryAssociation = BinaryAssociation(
    name="guard6",
    ends={
        Property(name="FSMModel_AbstractGuard", type=FSMModel_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="FSMModel_Transition", type=FSMModel_AbstractGuard, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
trigger7: BinaryAssociation = BinaryAssociation(
    name="trigger7",
    ends={
        Property(name="FSMModel_AbstractTrigger", type=FSMModel_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="FSMModel_Transition8", type=FSMModel_AbstractTrigger, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
value23: BinaryAssociation = BinaryAssociation(
    name="value23",
    ends={
        Property(name="ClassicalExpression_BooleanExpression", type=FSMModel_Guard, multiplicity=Multiplicity(1, 1)),
        Property(name="FSMModel_Guard", type=ClassicalExpression_BooleanExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
states15: BinaryAssociation = BinaryAssociation(
    name="states15",
    ends={
        Property(name="FSMModel_State", type=FSMModel_StateMachineDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="FSMModel_StateMachineDefinition16", type=FSMModel_State, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
initialStates17: BinaryAssociation = BinaryAssociation(
    name="initialStates17",
    ends={
        Property(name="FSMModel_State19", type=FSMModel_StateMachineDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="FSMModel_StateMachineDefinition18", type=FSMModel_State, multiplicity=Multiplicity(1, 9999))
    }
)
finalStates20: BinaryAssociation = BinaryAssociation(
    name="finalStates20",
    ends={
        Property(name="FSMModel_State22", type=FSMModel_StateMachineDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="FSMModel_StateMachineDefinition21", type=FSMModel_State, multiplicity=Multiplicity(0, 9999))
    }
)
concreteEntities28: BinaryAssociation = BinaryAssociation(
    name="concreteEntities28",
    ends={
        Property(name="ClockExpressionAndRelation_ConcreteEntity", type=FSMModel_DeclarationBlock, multiplicity=Multiplicity(1, 1)),
        Property(name="FSMModel_DeclarationBlock29", type=ClockExpressionAndRelation_ConcreteEntity, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
classicalExpressions30: BinaryAssociation = BinaryAssociation(
    name="classicalExpressions30",
    ends={
        Property(name="ClassicalExpression_ClassicalExpression", type=FSMModel_DeclarationBlock, multiplicity=Multiplicity(1, 1)),
        Property(name="FSMModel_DeclarationBlock31", type=ClassicalExpression_ClassicalExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
trueTriggers24: BinaryAssociation = BinaryAssociation(
    name="trueTriggers24",
    ends={
        Property(name="ClockExpressionAndRelation_BindableEntity", type=FSMModel_Trigger, multiplicity=Multiplicity(1, 1)),
        Property(name="FSMModel_Trigger", type=ClockExpressionAndRelation_BindableEntity, multiplicity=Multiplicity(0, 9999))
    }
)
falseTriggers25: BinaryAssociation = BinaryAssociation(
    name="falseTriggers25",
    ends={
        Property(name="ClockExpressionAndRelation_BindableEntity27", type=FSMModel_Trigger, multiplicity=Multiplicity(1, 1)),
        Property(name="FSMModel_Trigger26", type=ClockExpressionAndRelation_BindableEntity, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_FSMModel_Transition_NamedElement = Generalization(general=NamedElement, specific=FSMModel_Transition)
gen_FSMModel_State_NamedElement = Generalization(general=NamedElement, specific=FSMModel_State)
gen_FSMModel_StateMachineDefinition_NamedElement = Generalization(general=NamedElement, specific=FSMModel_StateMachineDefinition)
gen_FSMModel_Guard_AbstractGuard = Generalization(general=AbstractGuard, specific=FSMModel_Guard)
gen_FSMModel_Trigger_AbstractTrigger = Generalization(general=AbstractTrigger, specific=FSMModel_Trigger)
gen_FSMModel_IntegerAssignement_ClassicalExpression_BinaryIntegerExpression = Generalization(general=ClassicalExpression_BinaryIntegerExpression, specific=FSMModel_IntegerAssignement)
gen_FSMModel_IntegerAssignement_AbstractAction = Generalization(general=AbstractAction, specific=FSMModel_IntegerAssignement)

# Domain Model
domain_model = DomainModel(
    name="FSMModel",
    types={FSMModel_State, NamedElement, FSMModel_Transition, FSMModel_AbstractAction, FSMModel_StateMachineDefinition, FSMModel_DeclarationBlock, FSMModel_AbstractGuard, FSMModel_AbstractTrigger, FSMModel_Guard, AbstractGuard, ClassicalExpression_BooleanExpression, FSMModel_Trigger, ClockExpressionAndRelation_ConcreteEntity, ClassicalExpression_ClassicalExpression, AbstractTrigger, ClockExpressionAndRelation_BindableEntity, FSMModel_IntegerAssignement, ClassicalExpression_BinaryIntegerExpression, AbstractAction},
    associations={outputTransitions1, source3, inputTransitions0, actions9, declarationBlock11, transitions12, target4, guard6, trigger7, value23, states15, initialStates17, finalStates20, concreteEntities28, classicalExpressions30, trueTriggers24, falseTriggers25},
    generalizations={gen_FSMModel_Transition_NamedElement, gen_FSMModel_State_NamedElement, gen_FSMModel_StateMachineDefinition_NamedElement, gen_FSMModel_Guard_AbstractGuard, gen_FSMModel_Trigger_AbstractTrigger, gen_FSMModel_IntegerAssignement_ClassicalExpression_BinaryIntegerExpression, gen_FSMModel_IntegerAssignement_AbstractAction},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)