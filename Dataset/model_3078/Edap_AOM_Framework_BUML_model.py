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
smartadapters4MODERATES_Aspect = Class(name="smartadapters4MODERATES::Aspect")
smartadapters4MODERATES_PointcutModel = Class(name="smartadapters4MODERATES::PointcutModel")
smartadapters4MODERATES_AdviceModel = Class(name="smartadapters4MODERATES::AdviceModel")
smartadapters4MODERATES_InstantiationStrategy = Class(name="smartadapters4MODERATES::InstantiationStrategy", is_abstract=True)
smartadapters4MODERATES_Adaptation = Class(name="smartadapters4MODERATES::Adaptation", is_abstract=True)
smartadapters4MODERATES_CloneAdaptation = Class(name="smartadapters4MODERATES::CloneAdaptation", is_abstract=True)
Adaptation = Class(name="Adaptation")
smartadapters4MODERATES_CreateAdaptation = Class(name="smartadapters4MODERATES::CreateAdaptation", is_abstract=True)
smartadapters4MODERATES_SetAdaptation = Class(name="smartadapters4MODERATES::SetAdaptation", is_abstract=True)
smartadapters4MODERATES_UnsetAdaptation = Class(name="smartadapters4MODERATES::UnsetAdaptation", is_abstract=True)
smartadapters4MODERATES_AspectModelElement = Class(name="smartadapters4MODERATES::AspectModelElement")
smartadapters4MODERATES_GlobalInstantiation = Class(name="smartadapters4MODERATES::GlobalInstantiation")
InstantiationStrategy = Class(name="InstantiationStrategy")
smartadapters4MODERATES_ScopedInstantiation = Class(name="smartadapters4MODERATES::ScopedInstantiation", is_abstract=True)
smartadapters4MODERATES_PerRoleMatch = Class(name="smartadapters4MODERATES::PerRoleMatch")
ScopedInstantiation = Class(name="ScopedInstantiation")
smartadapters4MODERATES_PerElementMatch = Class(name="smartadapters4MODERATES::PerElementMatch")
smartadapters4MODERATES_adaptations_SetCompositeState = Class(name="smartadapters4MODERATES::adaptations::SetCompositeState")
SetAdaptation = Class(name="SetAdaptation")
adaptations_smartadapters4MODERATES_CompositeState = Class(name="adaptations::smartadapters4MODERATES::CompositeState")
adaptations_smartadapters4MODERATES_State = Class(name="adaptations::smartadapters4MODERATES::State")
smartadapters4MODERATES_adaptations_UnsetCompositeState = Class(name="smartadapters4MODERATES::adaptations::UnsetCompositeState")
UnsetAdaptation = Class(name="UnsetAdaptation")
smartadapters4MODERATES_adaptations_SetState = Class(name="smartadapters4MODERATES::adaptations::SetState")
adaptations_smartadapters4MODERATES_Transition = Class(name="adaptations::smartadapters4MODERATES::Transition")
adaptations_smartadapters4MODERATES_Action = Class(name="adaptations::smartadapters4MODERATES::Action")
adaptations_smartadapters4MODERATES_Property = Class(name="adaptations::smartadapters4MODERATES::Property")
smartadapters4MODERATES_adaptations_UnsetState = Class(name="smartadapters4MODERATES::adaptations::UnsetState")
smartadapters4MODERATES_adaptations_SetTransition = Class(name="smartadapters4MODERATES::adaptations::SetTransition")
adaptations_smartadapters4MODERATES_Event = Class(name="adaptations::smartadapters4MODERATES::Event")
adaptations_smartadapters4MODERATES_Expression = Class(name="adaptations::smartadapters4MODERATES::Expression")
smartadapters4MODERATES_adaptations_UnsetTransition = Class(name="smartadapters4MODERATES::adaptations::UnsetTransition")
smartadapters4MODERATES_adaptations_SetAnnotatedElement = Class(name="smartadapters4MODERATES::adaptations::SetAnnotatedElement")
adaptations_smartadapters4MODERATES_AnnotatedElement = Class(name="adaptations::smartadapters4MODERATES::AnnotatedElement")
adaptations_smartadapters4MODERATES_PlatformAnnotation = Class(name="adaptations::smartadapters4MODERATES::PlatformAnnotation")
smartadapters4MODERATES_adaptations_SetActionBlock = Class(name="smartadapters4MODERATES::adaptations::SetActionBlock")
adaptations_smartadapters4MODERATES_ActionBlock = Class(name="adaptations::smartadapters4MODERATES::ActionBlock")

# smartadapters4MODERATES_Aspect class attributes and methods
smartadapters4MODERATES_Aspect_name: Property = Property(name="name", type=StringType)
smartadapters4MODERATES_Aspect.attributes={smartadapters4MODERATES_Aspect_name}

# smartadapters4MODERATES_PointcutModel class attributes and methods

# smartadapters4MODERATES_AdviceModel class attributes and methods

# smartadapters4MODERATES_InstantiationStrategy class attributes and methods

# smartadapters4MODERATES_Adaptation class attributes and methods

# smartadapters4MODERATES_CloneAdaptation class attributes and methods

# Adaptation class attributes and methods

# smartadapters4MODERATES_CreateAdaptation class attributes and methods

# smartadapters4MODERATES_SetAdaptation class attributes and methods

# smartadapters4MODERATES_UnsetAdaptation class attributes and methods

# smartadapters4MODERATES_AspectModelElement class attributes and methods

# smartadapters4MODERATES_GlobalInstantiation class attributes and methods

# InstantiationStrategy class attributes and methods

# smartadapters4MODERATES_ScopedInstantiation class attributes and methods

# smartadapters4MODERATES_PerRoleMatch class attributes and methods

# ScopedInstantiation class attributes and methods

# smartadapters4MODERATES_PerElementMatch class attributes and methods

# smartadapters4MODERATES_adaptations_SetCompositeState class attributes and methods

# SetAdaptation class attributes and methods

# adaptations_smartadapters4MODERATES_CompositeState class attributes and methods

# adaptations_smartadapters4MODERATES_State class attributes and methods

# smartadapters4MODERATES_adaptations_UnsetCompositeState class attributes and methods

# UnsetAdaptation class attributes and methods

# smartadapters4MODERATES_adaptations_SetState class attributes and methods

# adaptations_smartadapters4MODERATES_Transition class attributes and methods

# adaptations_smartadapters4MODERATES_Action class attributes and methods

# adaptations_smartadapters4MODERATES_Property class attributes and methods

# smartadapters4MODERATES_adaptations_UnsetState class attributes and methods

# smartadapters4MODERATES_adaptations_SetTransition class attributes and methods

# adaptations_smartadapters4MODERATES_Event class attributes and methods

# adaptations_smartadapters4MODERATES_Expression class attributes and methods

# smartadapters4MODERATES_adaptations_UnsetTransition class attributes and methods

# smartadapters4MODERATES_adaptations_SetAnnotatedElement class attributes and methods

# adaptations_smartadapters4MODERATES_AnnotatedElement class attributes and methods

# adaptations_smartadapters4MODERATES_PlatformAnnotation class attributes and methods

# smartadapters4MODERATES_adaptations_SetActionBlock class attributes and methods

# adaptations_smartadapters4MODERATES_ActionBlock class attributes and methods

# Relationships
strategies3: BinaryAssociation = BinaryAssociation(
    name="strategies3",
    ends={
        Property(name="smartadapters4MODERATES_InstantiationStrategy", type=smartadapters4MODERATES_Aspect, multiplicity=Multiplicity(1, 1)),
        Property(name="smartadapters4MODERATES_Aspect4", type=smartadapters4MODERATES_InstantiationStrategy, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
pointcut0: BinaryAssociation = BinaryAssociation(
    name="pointcut0",
    ends={
        Property(name="smartadapters4MODERATES_PointcutModel", type=smartadapters4MODERATES_Aspect, multiplicity=Multiplicity(1, 1)),
        Property(name="smartadapters4MODERATES_Aspect", type=smartadapters4MODERATES_PointcutModel, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
advice1: BinaryAssociation = BinaryAssociation(
    name="advice1",
    ends={
        Property(name="smartadapters4MODERATES_AdviceModel", type=smartadapters4MODERATES_Aspect, multiplicity=Multiplicity(1, 1)),
        Property(name="smartadapters4MODERATES_Aspect2", type=smartadapters4MODERATES_AdviceModel, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
adapt5: BinaryAssociation = BinaryAssociation(
    name="adapt5",
    ends={
        Property(name="smartadapters4MODERATES_Adaptation", type=smartadapters4MODERATES_Aspect, multiplicity=Multiplicity(1, 1)),
        Property(name="smartadapters4MODERATES_Aspect6", type=smartadapters4MODERATES_Adaptation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
content7: BinaryAssociation = BinaryAssociation(
    name="content7",
    ends={
        Property(name="smartadapters4MODERATES_AspectModelElement", type=smartadapters4MODERATES_AdviceModel, multiplicity=Multiplicity(1, 1)),
        Property(name="smartadapters4MODERATES_AdviceModel8", type=smartadapters4MODERATES_AspectModelElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
content9: BinaryAssociation = BinaryAssociation(
    name="content9",
    ends={
        Property(name="smartadapters4MODERATES_AspectModelElement11", type=smartadapters4MODERATES_PointcutModel, multiplicity=Multiplicity(1, 1)),
        Property(name="smartadapters4MODERATES_PointcutModel10", type=smartadapters4MODERATES_AspectModelElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
adviceElements12: BinaryAssociation = BinaryAssociation(
    name="adviceElements12",
    ends={
        Property(name="smartadapters4MODERATES_AspectModelElement14", type=smartadapters4MODERATES_InstantiationStrategy, multiplicity=Multiplicity(1, 1)),
        Property(name="smartadapters4MODERATES_InstantiationStrategy13", type=smartadapters4MODERATES_AspectModelElement, multiplicity=Multiplicity(0, 9999))
    }
)
pointcutElements15: BinaryAssociation = BinaryAssociation(
    name="pointcutElements15",
    ends={
        Property(name="smartadapters4MODERATES_AspectModelElement16", type=smartadapters4MODERATES_ScopedInstantiation, multiplicity=Multiplicity(1, 1)),
        Property(name="smartadapters4MODERATES_ScopedInstantiation", type=smartadapters4MODERATES_AspectModelElement, multiplicity=Multiplicity(0, 9999))
    }
)
CompositeStateToSet17: BinaryAssociation = BinaryAssociation(
    name="CompositeStateToSet17",
    ends={
        Property(name="adaptations_smartadapters4MODERATES_CompositeState", type=smartadapters4MODERATES_adaptations_SetCompositeState, multiplicity=Multiplicity(1, 1)),
        Property(name="smartadapters4MODERATES_adaptations_SetCompositeState", type=adaptations_smartadapters4MODERATES_CompositeState, multiplicity=Multiplicity(1, 1))
    }
)
substate18: BinaryAssociation = BinaryAssociation(
    name="substate18",
    ends={
        Property(name="adaptations_smartadapters4MODERATES_State", type=smartadapters4MODERATES_adaptations_SetCompositeState, multiplicity=Multiplicity(1, 1)),
        Property(name="smartadapters4MODERATES_adaptations_SetCompositeState19", type=adaptations_smartadapters4MODERATES_State, multiplicity=Multiplicity(0, 9999))
    }
)
initial20: BinaryAssociation = BinaryAssociation(
    name="initial20",
    ends={
        Property(name="adaptations_smartadapters4MODERATES_State22", type=smartadapters4MODERATES_adaptations_SetCompositeState, multiplicity=Multiplicity(1, 1)),
        Property(name="smartadapters4MODERATES_adaptations_SetCompositeState21", type=adaptations_smartadapters4MODERATES_State, multiplicity=Multiplicity(0, 1))
    }
)
CompositeStateToUnset23: BinaryAssociation = BinaryAssociation(
    name="CompositeStateToUnset23",
    ends={
        Property(name="adaptations_smartadapters4MODERATES_CompositeState24", type=smartadapters4MODERATES_adaptations_UnsetCompositeState, multiplicity=Multiplicity(1, 1)),
        Property(name="smartadapters4MODERATES_adaptations_UnsetCompositeState", type=adaptations_smartadapters4MODERATES_CompositeState, multiplicity=Multiplicity(1, 1))
    }
)
substate25: BinaryAssociation = BinaryAssociation(
    name="substate25",
    ends={
        Property(name="adaptations_smartadapters4MODERATES_State27", type=smartadapters4MODERATES_adaptations_UnsetCompositeState, multiplicity=Multiplicity(1, 1)),
        Property(name="smartadapters4MODERATES_adaptations_UnsetCompositeState26", type=adaptations_smartadapters4MODERATES_State, multiplicity=Multiplicity(0, 9999))
    }
)
initial28: BinaryAssociation = BinaryAssociation(
    name="initial28",
    ends={
        Property(name="adaptations_smartadapters4MODERATES_State30", type=smartadapters4MODERATES_adaptations_UnsetCompositeState, multiplicity=Multiplicity(1, 1)),
        Property(name="smartadapters4MODERATES_adaptations_UnsetCompositeState29", type=adaptations_smartadapters4MODERATES_State, multiplicity=Multiplicity(0, 1))
    }
)
StateToSet31: BinaryAssociation = BinaryAssociation(
    name="StateToSet31",
    ends={
        Property(name="adaptations_smartadapters4MODERATES_State32", type=smartadapters4MODERATES_adaptations_SetState, multiplicity=Multiplicity(1, 1)),
        Property(name="smartadapters4MODERATES_adaptations_SetState", type=adaptations_smartadapters4MODERATES_State, multiplicity=Multiplicity(1, 1))
    }
)
outgoing33: BinaryAssociation = BinaryAssociation(
    name="outgoing33",
    ends={
        Property(name="adaptations_smartadapters4MODERATES_Transition", type=smartadapters4MODERATES_adaptations_SetState, multiplicity=Multiplicity(1, 1)),
        Property(name="smartadapters4MODERATES_adaptations_SetState34", type=adaptations_smartadapters4MODERATES_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
incoming35: BinaryAssociation = BinaryAssociation(
    name="incoming35",
    ends={
        Property(name="adaptations_smartadapters4MODERATES_Transition37", type=smartadapters4MODERATES_adaptations_SetState, multiplicity=Multiplicity(1, 1)),
        Property(name="smartadapters4MODERATES_adaptations_SetState36", type=adaptations_smartadapters4MODERATES_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
entry38: BinaryAssociation = BinaryAssociation(
    name="entry38",
    ends={
        Property(name="adaptations_smartadapters4MODERATES_Action", type=smartadapters4MODERATES_adaptations_SetState, multiplicity=Multiplicity(1, 1)),
        Property(name="smartadapters4MODERATES_adaptations_SetState39", type=adaptations_smartadapters4MODERATES_Action, multiplicity=Multiplicity(0, 1))
    }
)
exit40: BinaryAssociation = BinaryAssociation(
    name="exit40",
    ends={
        Property(name="adaptations_smartadapters4MODERATES_Action42", type=smartadapters4MODERATES_adaptations_SetState, multiplicity=Multiplicity(1, 1)),
        Property(name="smartadapters4MODERATES_adaptations_SetState41", type=adaptations_smartadapters4MODERATES_Action, multiplicity=Multiplicity(0, 1))
    }
)
properties43: BinaryAssociation = BinaryAssociation(
    name="properties43",
    ends={
        Property(name="adaptations_smartadapters4MODERATES_Property", type=smartadapters4MODERATES_adaptations_SetState, multiplicity=Multiplicity(1, 1)),
        Property(name="smartadapters4MODERATES_adaptations_SetState44", type=adaptations_smartadapters4MODERATES_Property, multiplicity=Multiplicity(0, 9999))
    }
)
StateToUnset45: BinaryAssociation = BinaryAssociation(
    name="StateToUnset45",
    ends={
        Property(name="adaptations_smartadapters4MODERATES_State46", type=smartadapters4MODERATES_adaptations_UnsetState, multiplicity=Multiplicity(1, 1)),
        Property(name="smartadapters4MODERATES_adaptations_UnsetState", type=adaptations_smartadapters4MODERATES_State, multiplicity=Multiplicity(1, 1))
    }
)
outgoing47: BinaryAssociation = BinaryAssociation(
    name="outgoing47",
    ends={
        Property(name="adaptations_smartadapters4MODERATES_Transition49", type=smartadapters4MODERATES_adaptations_UnsetState, multiplicity=Multiplicity(1, 1)),
        Property(name="smartadapters4MODERATES_adaptations_UnsetState48", type=adaptations_smartadapters4MODERATES_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
incoming50: BinaryAssociation = BinaryAssociation(
    name="incoming50",
    ends={
        Property(name="adaptations_smartadapters4MODERATES_Transition52", type=smartadapters4MODERATES_adaptations_UnsetState, multiplicity=Multiplicity(1, 1)),
        Property(name="smartadapters4MODERATES_adaptations_UnsetState51", type=adaptations_smartadapters4MODERATES_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
entry53: BinaryAssociation = BinaryAssociation(
    name="entry53",
    ends={
        Property(name="adaptations_smartadapters4MODERATES_Action55", type=smartadapters4MODERATES_adaptations_UnsetState, multiplicity=Multiplicity(1, 1)),
        Property(name="smartadapters4MODERATES_adaptations_UnsetState54", type=adaptations_smartadapters4MODERATES_Action, multiplicity=Multiplicity(0, 1))
    }
)
exit56: BinaryAssociation = BinaryAssociation(
    name="exit56",
    ends={
        Property(name="adaptations_smartadapters4MODERATES_Action58", type=smartadapters4MODERATES_adaptations_UnsetState, multiplicity=Multiplicity(1, 1)),
        Property(name="smartadapters4MODERATES_adaptations_UnsetState57", type=adaptations_smartadapters4MODERATES_Action, multiplicity=Multiplicity(0, 1))
    }
)
properties59: BinaryAssociation = BinaryAssociation(
    name="properties59",
    ends={
        Property(name="adaptations_smartadapters4MODERATES_Property61", type=smartadapters4MODERATES_adaptations_UnsetState, multiplicity=Multiplicity(1, 1)),
        Property(name="smartadapters4MODERATES_adaptations_UnsetState60", type=adaptations_smartadapters4MODERATES_Property, multiplicity=Multiplicity(0, 9999))
    }
)
TransitionToSet62: BinaryAssociation = BinaryAssociation(
    name="TransitionToSet62",
    ends={
        Property(name="adaptations_smartadapters4MODERATES_Transition63", type=smartadapters4MODERATES_adaptations_SetTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="smartadapters4MODERATES_adaptations_SetTransition", type=adaptations_smartadapters4MODERATES_Transition, multiplicity=Multiplicity(1, 1))
    }
)
event64: BinaryAssociation = BinaryAssociation(
    name="event64",
    ends={
        Property(name="adaptations_smartadapters4MODERATES_Event", type=smartadapters4MODERATES_adaptations_SetTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="smartadapters4MODERATES_adaptations_SetTransition65", type=adaptations_smartadapters4MODERATES_Event, multiplicity=Multiplicity(0, 9999))
    }
)
guard66: BinaryAssociation = BinaryAssociation(
    name="guard66",
    ends={
        Property(name="adaptations_smartadapters4MODERATES_Expression", type=smartadapters4MODERATES_adaptations_SetTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="smartadapters4MODERATES_adaptations_SetTransition67", type=adaptations_smartadapters4MODERATES_Expression, multiplicity=Multiplicity(0, 1))
    }
)
action68: BinaryAssociation = BinaryAssociation(
    name="action68",
    ends={
        Property(name="adaptations_smartadapters4MODERATES_Action70", type=smartadapters4MODERATES_adaptations_SetTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="smartadapters4MODERATES_adaptations_SetTransition69", type=adaptations_smartadapters4MODERATES_Action, multiplicity=Multiplicity(0, 1))
    }
)
target71: BinaryAssociation = BinaryAssociation(
    name="target71",
    ends={
        Property(name="adaptations_smartadapters4MODERATES_State73", type=smartadapters4MODERATES_adaptations_SetTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="smartadapters4MODERATES_adaptations_SetTransition72", type=adaptations_smartadapters4MODERATES_State, multiplicity=Multiplicity(0, 1))
    }
)
source74: BinaryAssociation = BinaryAssociation(
    name="source74",
    ends={
        Property(name="adaptations_smartadapters4MODERATES_State76", type=smartadapters4MODERATES_adaptations_SetTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="smartadapters4MODERATES_adaptations_SetTransition75", type=adaptations_smartadapters4MODERATES_State, multiplicity=Multiplicity(0, 1))
    }
)
TransitionToUnset77: BinaryAssociation = BinaryAssociation(
    name="TransitionToUnset77",
    ends={
        Property(name="adaptations_smartadapters4MODERATES_Transition78", type=smartadapters4MODERATES_adaptations_UnsetTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="smartadapters4MODERATES_adaptations_UnsetTransition", type=adaptations_smartadapters4MODERATES_Transition, multiplicity=Multiplicity(1, 1))
    }
)
event79: BinaryAssociation = BinaryAssociation(
    name="event79",
    ends={
        Property(name="adaptations_smartadapters4MODERATES_Event81", type=smartadapters4MODERATES_adaptations_UnsetTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="smartadapters4MODERATES_adaptations_UnsetTransition80", type=adaptations_smartadapters4MODERATES_Event, multiplicity=Multiplicity(0, 9999))
    }
)
guard82: BinaryAssociation = BinaryAssociation(
    name="guard82",
    ends={
        Property(name="adaptations_smartadapters4MODERATES_Expression84", type=smartadapters4MODERATES_adaptations_UnsetTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="smartadapters4MODERATES_adaptations_UnsetTransition83", type=adaptations_smartadapters4MODERATES_Expression, multiplicity=Multiplicity(0, 1))
    }
)
action85: BinaryAssociation = BinaryAssociation(
    name="action85",
    ends={
        Property(name="adaptations_smartadapters4MODERATES_Action87", type=smartadapters4MODERATES_adaptations_UnsetTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="smartadapters4MODERATES_adaptations_UnsetTransition86", type=adaptations_smartadapters4MODERATES_Action, multiplicity=Multiplicity(0, 1))
    }
)
target88: BinaryAssociation = BinaryAssociation(
    name="target88",
    ends={
        Property(name="adaptations_smartadapters4MODERATES_State90", type=smartadapters4MODERATES_adaptations_UnsetTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="smartadapters4MODERATES_adaptations_UnsetTransition89", type=adaptations_smartadapters4MODERATES_State, multiplicity=Multiplicity(0, 1))
    }
)
source91: BinaryAssociation = BinaryAssociation(
    name="source91",
    ends={
        Property(name="adaptations_smartadapters4MODERATES_State93", type=smartadapters4MODERATES_adaptations_UnsetTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="smartadapters4MODERATES_adaptations_UnsetTransition92", type=adaptations_smartadapters4MODERATES_State, multiplicity=Multiplicity(0, 1))
    }
)
AnnotatedElementToSet94: BinaryAssociation = BinaryAssociation(
    name="AnnotatedElementToSet94",
    ends={
        Property(name="adaptations_smartadapters4MODERATES_AnnotatedElement", type=smartadapters4MODERATES_adaptations_SetAnnotatedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="smartadapters4MODERATES_adaptations_SetAnnotatedElement", type=adaptations_smartadapters4MODERATES_AnnotatedElement, multiplicity=Multiplicity(1, 1))
    }
)
annotations95: BinaryAssociation = BinaryAssociation(
    name="annotations95",
    ends={
        Property(name="adaptations_smartadapters4MODERATES_PlatformAnnotation", type=smartadapters4MODERATES_adaptations_SetAnnotatedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="smartadapters4MODERATES_adaptations_SetAnnotatedElement96", type=adaptations_smartadapters4MODERATES_PlatformAnnotation, multiplicity=Multiplicity(0, 9999))
    }
)
blockToSet97: BinaryAssociation = BinaryAssociation(
    name="blockToSet97",
    ends={
        Property(name="adaptations_smartadapters4MODERATES_ActionBlock", type=smartadapters4MODERATES_adaptations_SetActionBlock, multiplicity=Multiplicity(1, 1)),
        Property(name="smartadapters4MODERATES_adaptations_SetActionBlock", type=adaptations_smartadapters4MODERATES_ActionBlock, multiplicity=Multiplicity(1, 1))
    }
)
actions98: BinaryAssociation = BinaryAssociation(
    name="actions98",
    ends={
        Property(name="adaptations_smartadapters4MODERATES_Action100", type=smartadapters4MODERATES_adaptations_SetActionBlock, multiplicity=Multiplicity(1, 1)),
        Property(name="smartadapters4MODERATES_adaptations_SetActionBlock99", type=adaptations_smartadapters4MODERATES_Action, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_smartadapters4MODERATES_CloneAdaptation_Adaptation = Generalization(general=Adaptation, specific=smartadapters4MODERATES_CloneAdaptation)
gen_smartadapters4MODERATES_CreateAdaptation_Adaptation = Generalization(general=Adaptation, specific=smartadapters4MODERATES_CreateAdaptation)
gen_smartadapters4MODERATES_SetAdaptation_Adaptation = Generalization(general=Adaptation, specific=smartadapters4MODERATES_SetAdaptation)
gen_smartadapters4MODERATES_UnsetAdaptation_Adaptation = Generalization(general=Adaptation, specific=smartadapters4MODERATES_UnsetAdaptation)
gen_smartadapters4MODERATES_GlobalInstantiation_InstantiationStrategy = Generalization(general=InstantiationStrategy, specific=smartadapters4MODERATES_GlobalInstantiation)
gen_smartadapters4MODERATES_ScopedInstantiation_InstantiationStrategy = Generalization(general=InstantiationStrategy, specific=smartadapters4MODERATES_ScopedInstantiation)
gen_smartadapters4MODERATES_PerRoleMatch_ScopedInstantiation = Generalization(general=ScopedInstantiation, specific=smartadapters4MODERATES_PerRoleMatch)
gen_smartadapters4MODERATES_PerElementMatch_ScopedInstantiation = Generalization(general=ScopedInstantiation, specific=smartadapters4MODERATES_PerElementMatch)
gen_smartadapters4MODERATES_adaptations_SetCompositeState_SetAdaptation = Generalization(general=SetAdaptation, specific=smartadapters4MODERATES_adaptations_SetCompositeState)
gen_smartadapters4MODERATES_adaptations_UnsetCompositeState_UnsetAdaptation = Generalization(general=UnsetAdaptation, specific=smartadapters4MODERATES_adaptations_UnsetCompositeState)
gen_smartadapters4MODERATES_adaptations_SetState_SetAdaptation = Generalization(general=SetAdaptation, specific=smartadapters4MODERATES_adaptations_SetState)
gen_smartadapters4MODERATES_adaptations_UnsetState_UnsetAdaptation = Generalization(general=UnsetAdaptation, specific=smartadapters4MODERATES_adaptations_UnsetState)
gen_smartadapters4MODERATES_adaptations_SetTransition_SetAdaptation = Generalization(general=SetAdaptation, specific=smartadapters4MODERATES_adaptations_SetTransition)
gen_smartadapters4MODERATES_adaptations_UnsetTransition_UnsetAdaptation = Generalization(general=UnsetAdaptation, specific=smartadapters4MODERATES_adaptations_UnsetTransition)
gen_smartadapters4MODERATES_adaptations_SetAnnotatedElement_SetAdaptation = Generalization(general=SetAdaptation, specific=smartadapters4MODERATES_adaptations_SetAnnotatedElement)
gen_smartadapters4MODERATES_adaptations_SetActionBlock_SetAdaptation = Generalization(general=SetAdaptation, specific=smartadapters4MODERATES_adaptations_SetActionBlock)

# Domain Model
domain_model = DomainModel(
    name="smartadapters4MODERATES",
    types={smartadapters4MODERATES_Aspect, smartadapters4MODERATES_PointcutModel, smartadapters4MODERATES_AdviceModel, smartadapters4MODERATES_InstantiationStrategy, smartadapters4MODERATES_Adaptation, smartadapters4MODERATES_CloneAdaptation, Adaptation, smartadapters4MODERATES_CreateAdaptation, smartadapters4MODERATES_SetAdaptation, smartadapters4MODERATES_UnsetAdaptation, smartadapters4MODERATES_AspectModelElement, smartadapters4MODERATES_GlobalInstantiation, InstantiationStrategy, smartadapters4MODERATES_ScopedInstantiation, smartadapters4MODERATES_PerRoleMatch, ScopedInstantiation, smartadapters4MODERATES_PerElementMatch, smartadapters4MODERATES_adaptations_SetCompositeState, SetAdaptation, adaptations_smartadapters4MODERATES_CompositeState, adaptations_smartadapters4MODERATES_State, smartadapters4MODERATES_adaptations_UnsetCompositeState, UnsetAdaptation, smartadapters4MODERATES_adaptations_SetState, adaptations_smartadapters4MODERATES_Transition, adaptations_smartadapters4MODERATES_Action, adaptations_smartadapters4MODERATES_Property, smartadapters4MODERATES_adaptations_UnsetState, smartadapters4MODERATES_adaptations_SetTransition, adaptations_smartadapters4MODERATES_Event, adaptations_smartadapters4MODERATES_Expression, smartadapters4MODERATES_adaptations_UnsetTransition, smartadapters4MODERATES_adaptations_SetAnnotatedElement, adaptations_smartadapters4MODERATES_AnnotatedElement, adaptations_smartadapters4MODERATES_PlatformAnnotation, smartadapters4MODERATES_adaptations_SetActionBlock, adaptations_smartadapters4MODERATES_ActionBlock},
    associations={strategies3, pointcut0, advice1, adapt5, content7, content9, adviceElements12, pointcutElements15, CompositeStateToSet17, substate18, initial20, CompositeStateToUnset23, substate25, initial28, StateToSet31, outgoing33, incoming35, entry38, exit40, properties43, StateToUnset45, outgoing47, incoming50, entry53, exit56, properties59, TransitionToSet62, event64, guard66, action68, target71, source74, TransitionToUnset77, event79, guard82, action85, target88, source91, AnnotatedElementToSet94, annotations95, blockToSet97, actions98},
    generalizations={gen_smartadapters4MODERATES_CloneAdaptation_Adaptation, gen_smartadapters4MODERATES_CreateAdaptation_Adaptation, gen_smartadapters4MODERATES_SetAdaptation_Adaptation, gen_smartadapters4MODERATES_UnsetAdaptation_Adaptation, gen_smartadapters4MODERATES_GlobalInstantiation_InstantiationStrategy, gen_smartadapters4MODERATES_ScopedInstantiation_InstantiationStrategy, gen_smartadapters4MODERATES_PerRoleMatch_ScopedInstantiation, gen_smartadapters4MODERATES_PerElementMatch_ScopedInstantiation, gen_smartadapters4MODERATES_adaptations_SetCompositeState_SetAdaptation, gen_smartadapters4MODERATES_adaptations_UnsetCompositeState_UnsetAdaptation, gen_smartadapters4MODERATES_adaptations_SetState_SetAdaptation, gen_smartadapters4MODERATES_adaptations_UnsetState_UnsetAdaptation, gen_smartadapters4MODERATES_adaptations_SetTransition_SetAdaptation, gen_smartadapters4MODERATES_adaptations_UnsetTransition_UnsetAdaptation, gen_smartadapters4MODERATES_adaptations_SetAnnotatedElement_SetAdaptation, gen_smartadapters4MODERATES_adaptations_SetActionBlock_SetAdaptation},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)