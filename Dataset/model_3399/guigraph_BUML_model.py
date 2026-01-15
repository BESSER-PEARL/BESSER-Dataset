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
TimingType: Enumeration = Enumeration(
    name="TimingType",
    literals={
            EnumerationLiteral(name="DelayUntilStart"),
			EnumerationLiteral(name="Interval")
    }
)

# Classes
guigraph_GuiGraph = Class(name="guigraph::GuiGraph")
AbstractModelElement = Class(name="AbstractModelElement")
guigraph_Arc = Class(name="guigraph::Arc", is_abstract=True)
guigraph_GuiGraphNode = Class(name="guigraph::GuiGraphNode", is_abstract=True)
Predicate = Class(name="Predicate")
guigraph_Page = Class(name="guigraph::Page")
GuiGraph = Class(name="GuiGraph")
guigraph_Widget = Class(name="guigraph::Widget")
guigraph_Form = Class(name="guigraph::Form")
Widget = Class(name="Widget")
Place = Class(name="Place")
guigraph_Transition = Class(name="guigraph::Transition", is_abstract=True)
GuiGraphNode = Class(name="GuiGraphNode")
rules_IRealTimeConsumer = Class(name="rules::IRealTimeConsumer")
guigraph_NoWidgetNode = Class(name="guigraph::NoWidgetNode")
guigraph_Place = Class(name="guigraph::Place", is_abstract=True)
guigraph_ConditionActionTransition = Class(name="guigraph::ConditionActionTransition")
Transition = Class(name="Transition")
guigraph_PreGenerationSequence = Class(name="guigraph::PreGenerationSequence")
guigraph_TimerTransition = Class(name="guigraph::TimerTransition")
ITimeConsumer = Class(name="ITimeConsumer")
guigraph_StandardArc = Class(name="guigraph::StandardArc")
Arc = Class(name="Arc")
guigraph_InhibitorArc = Class(name="guigraph::InhibitorArc")
guigraph_PageTransition = Class(name="guigraph::PageTransition")

# guigraph_GuiGraph class attributes and methods
guigraph_GuiGraph_invariantText: Property = Property(name="invariantText", type=StringType)
guigraph_GuiGraph.attributes={guigraph_GuiGraph_invariantText}

# AbstractModelElement class attributes and methods

# guigraph_Arc class attributes and methods

# guigraph_GuiGraphNode class attributes and methods

# Predicate class attributes and methods

# guigraph_Page class attributes and methods

# GuiGraph class attributes and methods

# guigraph_Widget class attributes and methods
guigraph_Widget_image: Property = Property(name="image", type=StringType)
guigraph_Widget.attributes={guigraph_Widget_image}

# guigraph_Form class attributes and methods

# Widget class attributes and methods

# Place class attributes and methods

# guigraph_Transition class attributes and methods
guigraph_Transition_rate: Property = Property(name="rate", type=IntegerType)
guigraph_Transition_faultImpact: Property = Property(name="faultImpact", type=FloatType)
guigraph_Transition_faultProbability: Property = Property(name="faultProbability", type=FloatType)
guigraph_Transition_terminates: Property = Property(name="terminates", type=BooleanType)
guigraph_Transition_timeMin: Property = Property(name="timeMin", type=StringType)
guigraph_Transition_timeMax: Property = Property(name="timeMax", type=StringType)
guigraph_Transition_timingType: Property = Property(name="timingType", type=StringType)
guigraph_Transition.attributes={guigraph_Transition_timeMax, guigraph_Transition_timeMin, guigraph_Transition_faultImpact, guigraph_Transition_rate, guigraph_Transition_timingType, guigraph_Transition_terminates, guigraph_Transition_faultProbability}

# GuiGraphNode class attributes and methods

# rules_IRealTimeConsumer class attributes and methods

# guigraph_NoWidgetNode class attributes and methods

# guigraph_Place class attributes and methods
guigraph_Place_initialTokens: Property = Property(name="initialTokens", type=IntegerType)
guigraph_Place.attributes={guigraph_Place_initialTokens}

# guigraph_ConditionActionTransition class attributes and methods
guigraph_ConditionActionTransition_applicationConditionText: Property = Property(name="applicationConditionText", type=StringType)
guigraph_ConditionActionTransition_actionsText: Property = Property(name="actionsText", type=StringType)
guigraph_ConditionActionTransition.attributes={guigraph_ConditionActionTransition_actionsText, guigraph_ConditionActionTransition_applicationConditionText}

# Transition class attributes and methods

# guigraph_PreGenerationSequence class attributes and methods

# guigraph_TimerTransition class attributes and methods
guigraph_TimerTransition_duration: Property = Property(name="duration", type=IntegerType)
guigraph_TimerTransition.attributes={guigraph_TimerTransition_duration}

# ITimeConsumer class attributes and methods

# guigraph_StandardArc class attributes and methods
guigraph_StandardArc_weight: Property = Property(name="weight", type=IntegerType)
guigraph_StandardArc.attributes={guigraph_StandardArc_weight}

# Arc class attributes and methods

# guigraph_InhibitorArc class attributes and methods

# guigraph_PageTransition class attributes and methods

# Relationships
arcs0: BinaryAssociation = BinaryAssociation(
    name="arcs0",
    ends={
        Property(name="guigraph_Arc", type=guigraph_GuiGraph, multiplicity=Multiplicity(1, 1)),
        Property(name="guigraph_GuiGraph", type=guigraph_Arc, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
nodes1: BinaryAssociation = BinaryAssociation(
    name="nodes1",
    ends={
        Property(name="guigraph_GuiGraphNode", type=guigraph_GuiGraph, multiplicity=Multiplicity(1, 1)),
        Property(name="guigraph_GuiGraph2", type=guigraph_GuiGraphNode, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
invariant3: BinaryAssociation = BinaryAssociation(
    name="invariant3",
    ends={
        Property(name="Predicate", type=guigraph_GuiGraph, multiplicity=Multiplicity(1, 1)),
        Property(name="guigraph_GuiGraph4", type=Predicate, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
children6: BinaryAssociation = BinaryAssociation(
    name="children6",
    ends={
        Property(name="guigraph_Widget", type=guigraph_Widget, multiplicity=Multiplicity(1, 1)),
        Property(name="guigraph_Widget5", type=guigraph_Widget, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
applicationCondition7: BinaryAssociation = BinaryAssociation(
    name="applicationCondition7",
    ends={
        Property(name="Predicate8", type=guigraph_ConditionActionTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="guigraph_ConditionActionTransition", type=Predicate, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
actions9: BinaryAssociation = BinaryAssociation(
    name="actions9",
    ends={
        Property(name="guigraph_PreGenerationSequence", type=guigraph_ConditionActionTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="guigraph_ConditionActionTransition10", type=guigraph_PreGenerationSequence, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
consumer11: BinaryAssociation = BinaryAssociation(
    name="consumer11",
    ends={
        Property(name="ITimeConsumer", type=guigraph_TimerTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="guigraph_TimerTransition", type=ITimeConsumer, multiplicity=Multiplicity(1, 1))
    }
)
source12: BinaryAssociation = BinaryAssociation(
    name="source12",
    ends={
        Property(name="guigraph_GuiGraphNode14", type=guigraph_Arc, multiplicity=Multiplicity(1, 1)),
        Property(name="guigraph_Arc13", type=guigraph_GuiGraphNode, multiplicity=Multiplicity(1, 1))
    }
)
target15: BinaryAssociation = BinaryAssociation(
    name="target15",
    ends={
        Property(name="guigraph_GuiGraphNode17", type=guigraph_Arc, multiplicity=Multiplicity(1, 1)),
        Property(name="guigraph_Arc16", type=guigraph_GuiGraphNode, multiplicity=Multiplicity(1, 1))
    }
)
page18: BinaryAssociation = BinaryAssociation(
    name="page18",
    ends={
        Property(name="guigraph_Page", type=guigraph_PageTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="guigraph_PageTransition", type=guigraph_Page, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_guigraph_GuiGraph_AbstractModelElement = Generalization(general=AbstractModelElement, specific=guigraph_GuiGraph)
gen_guigraph_Page_GuiGraph = Generalization(general=GuiGraph, specific=guigraph_Page)
gen_guigraph_Widget_AbstractModelElement = Generalization(general=AbstractModelElement, specific=guigraph_Widget)
gen_guigraph_Form_Widget = Generalization(general=Widget, specific=guigraph_Form)
gen_guigraph_Form_Place = Generalization(general=Place, specific=guigraph_Form)
gen_guigraph_Transition_GuiGraphNode = Generalization(general=GuiGraphNode, specific=guigraph_Transition)
gen_guigraph_Transition_rules_IRealTimeConsumer = Generalization(general=rules_IRealTimeConsumer, specific=guigraph_Transition)
gen_guigraph_GuiGraphNode_AbstractModelElement = Generalization(general=AbstractModelElement, specific=guigraph_GuiGraphNode)
gen_guigraph_NoWidgetNode_Place = Generalization(general=Place, specific=guigraph_NoWidgetNode)
gen_guigraph_Place_GuiGraphNode = Generalization(general=GuiGraphNode, specific=guigraph_Place)
gen_guigraph_ConditionActionTransition_Transition = Generalization(general=Transition, specific=guigraph_ConditionActionTransition)
gen_guigraph_TimerTransition_Transition = Generalization(general=Transition, specific=guigraph_TimerTransition)
gen_guigraph_Arc_AbstractModelElement = Generalization(general=AbstractModelElement, specific=guigraph_Arc)
gen_guigraph_StandardArc_Arc = Generalization(general=Arc, specific=guigraph_StandardArc)
gen_guigraph_InhibitorArc_Arc = Generalization(general=Arc, specific=guigraph_InhibitorArc)
gen_guigraph_PageTransition_Transition = Generalization(general=Transition, specific=guigraph_PageTransition)

# Domain Model
domain_model = DomainModel(
    name="guigraph",
    types={guigraph_GuiGraph, AbstractModelElement, guigraph_Arc, guigraph_GuiGraphNode, Predicate, guigraph_Page, GuiGraph, guigraph_Widget, guigraph_Form, Widget, Place, guigraph_Transition, GuiGraphNode, rules_IRealTimeConsumer, guigraph_NoWidgetNode, guigraph_Place, guigraph_ConditionActionTransition, Transition, guigraph_PreGenerationSequence, guigraph_TimerTransition, ITimeConsumer, guigraph_StandardArc, Arc, guigraph_InhibitorArc, guigraph_PageTransition, TimingType},
    associations={arcs0, nodes1, invariant3, children6, applicationCondition7, actions9, consumer11, source12, target15, page18},
    generalizations={gen_guigraph_GuiGraph_AbstractModelElement, gen_guigraph_Page_GuiGraph, gen_guigraph_Widget_AbstractModelElement, gen_guigraph_Form_Widget, gen_guigraph_Form_Place, gen_guigraph_Transition_GuiGraphNode, gen_guigraph_Transition_rules_IRealTimeConsumer, gen_guigraph_GuiGraphNode_AbstractModelElement, gen_guigraph_NoWidgetNode_Place, gen_guigraph_Place_GuiGraphNode, gen_guigraph_ConditionActionTransition_Transition, gen_guigraph_TimerTransition_Transition, gen_guigraph_Arc_AbstractModelElement, gen_guigraph_StandardArc_Arc, gen_guigraph_InhibitorArc_Arc, gen_guigraph_PageTransition_Transition},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)