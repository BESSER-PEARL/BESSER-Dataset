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
MessageKind: Enumeration = Enumeration(
    name="MessageKind",
    literals={
            EnumerationLiteral(name="UNSET"),
			EnumerationLiteral(name="ASYNCHRONOUS_CALL"),
			EnumerationLiteral(name="SYNCHRONOUS_CALL"),
			EnumerationLiteral(name="REPLY"),
			EnumerationLiteral(name="DELETE"),
			EnumerationLiteral(name="CREATE"),
			EnumerationLiteral(name="TIMER")
    }
)

ScenarioKind: Enumeration = Enumeration(
    name="ScenarioKind",
    literals={
            EnumerationLiteral(name="UNSET"),
			EnumerationLiteral(name="INTERFACE"),
			EnumerationLiteral(name="DATA_FLOW"),
			EnumerationLiteral(name="INTERACTION"),
			EnumerationLiteral(name="FUNCTIONAL")
    }
)

InteractionOperatorKind: Enumeration = Enumeration(
    name="InteractionOperatorKind",
    literals={
            EnumerationLiteral(name="ALT"),
			EnumerationLiteral(name="OPT"),
			EnumerationLiteral(name="PAR"),
			EnumerationLiteral(name="LOOP"),
			EnumerationLiteral(name="CRITICAL"),
			EnumerationLiteral(name="NEG"),
			EnumerationLiteral(name="ASSERT"),
			EnumerationLiteral(name="STRICT"),
			EnumerationLiteral(name="SEQ"),
			EnumerationLiteral(name="IGNORE"),
			EnumerationLiteral(name="CONSIDER"),
			EnumerationLiteral(name="UNSET")
    }
)

# Classes
interaction_SequenceMessage = Class(name="interaction::SequenceMessage")
NamedElement = Class(name="NamedElement")
interaction_Constraint = Class(name="interaction::Constraint")
interaction_AbstractEventOperation = Class(name="interaction::AbstractEventOperation")
interaction_ExchangeItem = Class(name="interaction::ExchangeItem")
interaction_Part = Class(name="interaction::Part")
interaction_AbstractFunction = Class(name="interaction::AbstractFunction")
interaction_AbstractCapability = Class(name="interaction::AbstractCapability", is_abstract=True)
Structure = Class(name="Structure")
AbstractFunctionalChainContainer = Class(name="AbstractFunctionalChainContainer")
CapellaElement = Class(name="CapellaElement")
interaction_State = Class(name="interaction::State")
interaction_FunctionalChain = Class(name="interaction::FunctionalChain")
interaction_CombinedFragment = Class(name="interaction::CombinedFragment")
interaction_SequenceMessageValuation = Class(name="interaction::SequenceMessageValuation")
interaction_Scenario = Class(name="interaction::Scenario")
Namespace = Class(name="Namespace")
AbstractBehavior = Class(name="AbstractBehavior")
interaction_InteractionOperand = Class(name="interaction::InteractionOperand")
interaction_ExchangeItemElement = Class(name="interaction::ExchangeItemElement")
interaction_ValueSpecification = Class(name="interaction::ValueSpecification")

# interaction_SequenceMessage class attributes and methods
interaction_SequenceMessage_kind: Property = Property(name="kind", type=StringType)
interaction_SequenceMessage.attributes={interaction_SequenceMessage_kind}

# NamedElement class attributes and methods

# interaction_Constraint class attributes and methods

# interaction_AbstractEventOperation class attributes and methods

# interaction_ExchangeItem class attributes and methods

# interaction_Part class attributes and methods

# interaction_AbstractFunction class attributes and methods

# interaction_AbstractCapability class attributes and methods

# Structure class attributes and methods

# AbstractFunctionalChainContainer class attributes and methods

# CapellaElement class attributes and methods

# interaction_State class attributes and methods

# interaction_FunctionalChain class attributes and methods

# interaction_CombinedFragment class attributes and methods
interaction_CombinedFragment_operator: Property = Property(name="operator", type=StringType)
interaction_CombinedFragment.attributes={interaction_CombinedFragment_operator}

# interaction_SequenceMessageValuation class attributes and methods

# interaction_Scenario class attributes and methods
interaction_Scenario_kind: Property = Property(name="kind", type=StringType)
interaction_Scenario_merged: Property = Property(name="merged", type=BooleanType)
interaction_Scenario.attributes={interaction_Scenario_kind, interaction_Scenario_merged}

# Namespace class attributes and methods

# AbstractBehavior class attributes and methods

# interaction_InteractionOperand class attributes and methods

# interaction_ExchangeItemElement class attributes and methods

# interaction_ValueSpecification class attributes and methods

# Relationships
exchangeContext0: BinaryAssociation = BinaryAssociation(
    name="exchangeContext0",
    ends={
        Property(name="interaction_Constraint", type=interaction_SequenceMessage, multiplicity=Multiplicity(1, 1)),
        Property(name="interaction_SequenceMessage", type=interaction_Constraint, multiplicity=Multiplicity(0, 1))
    }
)
invokedOperation1: BinaryAssociation = BinaryAssociation(
    name="invokedOperation1",
    ends={
        Property(name="interaction_AbstractEventOperation", type=interaction_SequenceMessage, multiplicity=Multiplicity(1, 1)),
        Property(name="interaction_SequenceMessage2", type=interaction_AbstractEventOperation, multiplicity=Multiplicity(0, 1))
    }
)
exchangedItems3: BinaryAssociation = BinaryAssociation(
    name="exchangedItems3",
    ends={
        Property(name="interaction_ExchangeItem", type=interaction_SequenceMessage, multiplicity=Multiplicity(1, 1)),
        Property(name="interaction_SequenceMessage4", type=interaction_ExchangeItem, multiplicity=Multiplicity(0, 9999))
    }
)
sendingPart5: BinaryAssociation = BinaryAssociation(
    name="sendingPart5",
    ends={
        Property(name="interaction_Part", type=interaction_SequenceMessage, multiplicity=Multiplicity(1, 1)),
        Property(name="interaction_SequenceMessage6", type=interaction_Part, multiplicity=Multiplicity(0, 1))
    }
)
receivingPart7: BinaryAssociation = BinaryAssociation(
    name="receivingPart7",
    ends={
        Property(name="interaction_Part9", type=interaction_SequenceMessage, multiplicity=Multiplicity(1, 1)),
        Property(name="interaction_SequenceMessage8", type=interaction_Part, multiplicity=Multiplicity(0, 1))
    }
)
sendingFunction10: BinaryAssociation = BinaryAssociation(
    name="sendingFunction10",
    ends={
        Property(name="interaction_AbstractFunction", type=interaction_SequenceMessage, multiplicity=Multiplicity(1, 1)),
        Property(name="interaction_SequenceMessage11", type=interaction_AbstractFunction, multiplicity=Multiplicity(0, 1))
    }
)
receivingFunction12: BinaryAssociation = BinaryAssociation(
    name="receivingFunction12",
    ends={
        Property(name="interaction_AbstractFunction14", type=interaction_SequenceMessage, multiplicity=Multiplicity(1, 1)),
        Property(name="interaction_SequenceMessage13", type=interaction_AbstractFunction, multiplicity=Multiplicity(0, 1))
    }
)
realizedScenarios35: BinaryAssociation = BinaryAssociation(
    name="realizedScenarios35",
    ends={
        Property(name="interaction_Scenario36", type=interaction_Scenario, multiplicity=Multiplicity(1, 1)),
        Property(name="interaction_Scenario34", type=interaction_Scenario, multiplicity=Multiplicity(0, 9999))
    }
)
preCondition37: BinaryAssociation = BinaryAssociation(
    name="preCondition37",
    ends={
        Property(name="interaction_Constraint38", type=interaction_AbstractCapability, multiplicity=Multiplicity(1, 1)),
        Property(name="interaction_AbstractCapability", type=interaction_Constraint, multiplicity=Multiplicity(0, 1))
    }
)
postCondition39: BinaryAssociation = BinaryAssociation(
    name="postCondition39",
    ends={
        Property(name="interaction_Constraint41", type=interaction_AbstractCapability, multiplicity=Multiplicity(1, 1)),
        Property(name="interaction_AbstractCapability40", type=interaction_Constraint, multiplicity=Multiplicity(0, 1))
    }
)
ownedScenarios42: BinaryAssociation = BinaryAssociation(
    name="ownedScenarios42",
    ends={
        Property(name="interaction_Scenario44", type=interaction_AbstractCapability, multiplicity=Multiplicity(1, 1)),
        Property(name="interaction_AbstractCapability43", type=interaction_Scenario, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
super46: BinaryAssociation = BinaryAssociation(
    name="super46",
    ends={
        Property(name="interaction_AbstractCapability47", type=interaction_AbstractCapability, multiplicity=Multiplicity(1, 1)),
        Property(name="interaction_AbstractCapability45", type=interaction_AbstractCapability, multiplicity=Multiplicity(0, 9999))
    }
)
includedAbstractCapabilities49: BinaryAssociation = BinaryAssociation(
    name="includedAbstractCapabilities49",
    ends={
        Property(name="interaction_AbstractCapability50", type=interaction_AbstractCapability, multiplicity=Multiplicity(1, 1)),
        Property(name="interaction_AbstractCapability48", type=interaction_AbstractCapability, multiplicity=Multiplicity(0, 9999))
    }
)
extendedAbstractCapabilities52: BinaryAssociation = BinaryAssociation(
    name="extendedAbstractCapabilities52",
    ends={
        Property(name="interaction_AbstractCapability53", type=interaction_AbstractCapability, multiplicity=Multiplicity(1, 1)),
        Property(name="interaction_AbstractCapability51", type=interaction_AbstractCapability, multiplicity=Multiplicity(0, 9999))
    }
)
availableInStates54: BinaryAssociation = BinaryAssociation(
    name="availableInStates54",
    ends={
        Property(name="interaction_State", type=interaction_AbstractCapability, multiplicity=Multiplicity(1, 1)),
        Property(name="interaction_AbstractCapability55", type=interaction_State, multiplicity=Multiplicity(0, 9999))
    }
)
involvedAbstractFunctions56: BinaryAssociation = BinaryAssociation(
    name="involvedAbstractFunctions56",
    ends={
        Property(name="interaction_AbstractFunction58", type=interaction_AbstractCapability, multiplicity=Multiplicity(1, 1)),
        Property(name="interaction_AbstractCapability57", type=interaction_AbstractFunction, multiplicity=Multiplicity(0, 9999))
    }
)
involvedFunctionalChains59: BinaryAssociation = BinaryAssociation(
    name="involvedFunctionalChains59",
    ends={
        Property(name="interaction_FunctionalChain", type=interaction_AbstractCapability, multiplicity=Multiplicity(1, 1)),
        Property(name="interaction_AbstractCapability60", type=interaction_FunctionalChain, multiplicity=Multiplicity(0, 9999))
    }
)
ownedSequenceMessageValuations15: BinaryAssociation = BinaryAssociation(
    name="ownedSequenceMessageValuations15",
    ends={
        Property(name="interaction_SequenceMessageValuation", type=interaction_SequenceMessage, multiplicity=Multiplicity(1, 1)),
        Property(name="interaction_SequenceMessage16", type=interaction_SequenceMessageValuation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
preCondition17: BinaryAssociation = BinaryAssociation(
    name="preCondition17",
    ends={
        Property(name="interaction_Constraint18", type=interaction_Scenario, multiplicity=Multiplicity(1, 1)),
        Property(name="interaction_Scenario", type=interaction_Constraint, multiplicity=Multiplicity(0, 1))
    }
)
postCondition19: BinaryAssociation = BinaryAssociation(
    name="postCondition19",
    ends={
        Property(name="interaction_Constraint21", type=interaction_Scenario, multiplicity=Multiplicity(1, 1)),
        Property(name="interaction_Scenario20", type=interaction_Constraint, multiplicity=Multiplicity(0, 1))
    }
)
ownedMessages22: BinaryAssociation = BinaryAssociation(
    name="ownedMessages22",
    ends={
        Property(name="interaction_SequenceMessage24", type=interaction_Scenario, multiplicity=Multiplicity(1, 1)),
        Property(name="interaction_Scenario23", type=interaction_SequenceMessage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
containedFunctions25: BinaryAssociation = BinaryAssociation(
    name="containedFunctions25",
    ends={
        Property(name="interaction_AbstractFunction27", type=interaction_Scenario, multiplicity=Multiplicity(1, 1)),
        Property(name="interaction_Scenario26", type=interaction_AbstractFunction, multiplicity=Multiplicity(0, 9999))
    }
)
containedParts28: BinaryAssociation = BinaryAssociation(
    name="containedParts28",
    ends={
        Property(name="interaction_Part30", type=interaction_Scenario, multiplicity=Multiplicity(1, 1)),
        Property(name="interaction_Scenario29", type=interaction_Part, multiplicity=Multiplicity(0, 9999))
    }
)
referencedScenarios32: BinaryAssociation = BinaryAssociation(
    name="referencedScenarios32",
    ends={
        Property(name="interaction_Scenario33", type=interaction_Scenario, multiplicity=Multiplicity(1, 1)),
        Property(name="interaction_Scenario31", type=interaction_Scenario, multiplicity=Multiplicity(0, 9999))
    }
)
guard61: BinaryAssociation = BinaryAssociation(
    name="guard61",
    ends={
        Property(name="interaction_Constraint62", type=interaction_InteractionOperand, multiplicity=Multiplicity(1, 1)),
        Property(name="interaction_InteractionOperand", type=interaction_Constraint, multiplicity=Multiplicity(0, 1))
    }
)
exchangeItemElement63: BinaryAssociation = BinaryAssociation(
    name="exchangeItemElement63",
    ends={
        Property(name="interaction_ExchangeItemElement", type=interaction_SequenceMessageValuation, multiplicity=Multiplicity(1, 1)),
        Property(name="interaction_SequenceMessageValuation64", type=interaction_ExchangeItemElement, multiplicity=Multiplicity(0, 1))
    }
)
value65: BinaryAssociation = BinaryAssociation(
    name="value65",
    ends={
        Property(name="interaction_ValueSpecification", type=interaction_SequenceMessageValuation, multiplicity=Multiplicity(1, 1)),
        Property(name="interaction_SequenceMessageValuation66", type=interaction_ValueSpecification, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_interaction_SequenceMessage_NamedElement = Generalization(general=NamedElement, specific=interaction_SequenceMessage)
gen_interaction_AbstractCapability_Structure = Generalization(general=Structure, specific=interaction_AbstractCapability)
gen_interaction_AbstractCapability_AbstractFunctionalChainContainer = Generalization(general=AbstractFunctionalChainContainer, specific=interaction_AbstractCapability)
gen_interaction_AbstractCapability_CapellaElement = Generalization(general=CapellaElement, specific=interaction_AbstractCapability)
gen_interaction_CombinedFragment_NamedElement = Generalization(general=NamedElement, specific=interaction_CombinedFragment)
gen_interaction_Scenario_Namespace = Generalization(general=Namespace, specific=interaction_Scenario)
gen_interaction_Scenario_AbstractBehavior = Generalization(general=AbstractBehavior, specific=interaction_Scenario)
gen_interaction_InteractionOperand_NamedElement = Generalization(general=NamedElement, specific=interaction_InteractionOperand)
gen_interaction_SequenceMessageValuation_CapellaElement = Generalization(general=CapellaElement, specific=interaction_SequenceMessageValuation)

# Domain Model
domain_model = DomainModel(
    name="interaction",
    types={interaction_SequenceMessage, NamedElement, interaction_Constraint, interaction_AbstractEventOperation, interaction_ExchangeItem, interaction_Part, interaction_AbstractFunction, interaction_AbstractCapability, Structure, AbstractFunctionalChainContainer, CapellaElement, interaction_State, interaction_FunctionalChain, interaction_CombinedFragment, interaction_SequenceMessageValuation, interaction_Scenario, Namespace, AbstractBehavior, interaction_InteractionOperand, interaction_ExchangeItemElement, interaction_ValueSpecification, MessageKind, ScenarioKind, InteractionOperatorKind},
    associations={exchangeContext0, invokedOperation1, exchangedItems3, sendingPart5, receivingPart7, sendingFunction10, receivingFunction12, realizedScenarios35, preCondition37, postCondition39, ownedScenarios42, super46, includedAbstractCapabilities49, extendedAbstractCapabilities52, availableInStates54, involvedAbstractFunctions56, involvedFunctionalChains59, ownedSequenceMessageValuations15, preCondition17, postCondition19, ownedMessages22, containedFunctions25, containedParts28, referencedScenarios32, guard61, exchangeItemElement63, value65},
    generalizations={gen_interaction_SequenceMessage_NamedElement, gen_interaction_AbstractCapability_Structure, gen_interaction_AbstractCapability_AbstractFunctionalChainContainer, gen_interaction_AbstractCapability_CapellaElement, gen_interaction_CombinedFragment_NamedElement, gen_interaction_Scenario_Namespace, gen_interaction_Scenario_AbstractBehavior, gen_interaction_InteractionOperand_NamedElement, gen_interaction_SequenceMessageValuation_CapellaElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)