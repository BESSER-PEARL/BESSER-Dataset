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
actions_ActionReference = Class(name="actions::ActionReference")
PreGenerationAction = Class(name="PreGenerationAction")
actions_StandAloneAction = Class(name="actions::StandAloneAction")
actions_EObject = Class(name="actions::EObject")
core_AbstractModelElement = Class(name="core::AbstractModelElement")
core_ITopLevelElement = Class(name="core::ITopLevelElement")
actions_PreGenerationAction = Class(name="actions::PreGenerationAction", is_abstract=True)
IContextVariable = Class(name="IContextVariable")
actions_TimedConditionAction = Class(name="actions::TimedConditionAction")
rules_IRealTimeConsumer = Class(name="rules::IRealTimeConsumer")
ILogicFunction = Class(name="ILogicFunction")
actions_Action = Class(name="actions::Action", is_abstract=True)
actions_PostGenerationAction = Class(name="actions::PostGenerationAction", is_abstract=True)
actions_PreGenerationSequence = Class(name="actions::PreGenerationSequence")
actions_PostGenerationSequence = Class(name="actions::PostGenerationSequence")
PostGenerationAction = Class(name="PostGenerationAction")
actions_ThrowAction = Class(name="actions::ThrowAction")
actions_TermAction = Class(name="actions::TermAction")
actions_Term = Class(name="actions::Term")
actions_ReconfigurationAction = Class(name="actions::ReconfigurationAction", is_abstract=True)
actions_SetDataAction = Class(name="actions::SetDataAction")
ReconfigurationAction = Class(name="ReconfigurationAction")
IValueFunction = Class(name="IValueFunction")
IDataNodeFunction = Class(name="IDataNodeFunction")
Action = Class(name="Action")
actions_RemoveBagAction = Class(name="actions::RemoveBagAction")
DataBag = Class(name="DataBag")
IArithmetricFunction = Class(name="IArithmetricFunction")
actions_ActivateFeatureAction = Class(name="actions::ActivateFeatureAction")
IFeature = Class(name="IFeature")
FeatureVersion = Class(name="FeatureVersion")
actions_DeactivateFeatureAction = Class(name="actions::DeactivateFeatureAction")
actions_SetPropertyAction = Class(name="actions::SetPropertyAction")
DataLeaf = Class(name="DataLeaf")
actions_GetDataAction = Class(name="actions::GetDataAction")
actions_FailAction = Class(name="actions::FailAction")
actions_TimeAction = Class(name="actions::TimeAction")
ITimeConsumer = Class(name="ITimeConsumer")
actions_DependentAction = Class(name="actions::DependentAction", is_abstract=True)
actions_GetPropertyAction = Class(name="actions::GetPropertyAction")
DependentAction = Class(name="DependentAction")
actions_GetRealTimeAction = Class(name="actions::GetRealTimeAction")
actions_GetFeatureStateAction = Class(name="actions::GetFeatureStateAction")
DataElement = Class(name="DataElement")

# actions_ActionReference class attributes and methods

# PreGenerationAction class attributes and methods

# actions_StandAloneAction class attributes and methods

# actions_EObject class attributes and methods

# core_AbstractModelElement class attributes and methods

# core_ITopLevelElement class attributes and methods

# actions_PreGenerationAction class attributes and methods

# IContextVariable class attributes and methods

# actions_TimedConditionAction class attributes and methods
actions_TimedConditionAction_frequency: Property = Property(name="frequency", type=IntegerType)
actions_TimedConditionAction.attributes={actions_TimedConditionAction_frequency}

# rules_IRealTimeConsumer class attributes and methods

# ILogicFunction class attributes and methods

# actions_Action class attributes and methods

# actions_PostGenerationAction class attributes and methods

# actions_PreGenerationSequence class attributes and methods

# actions_PostGenerationSequence class attributes and methods

# PostGenerationAction class attributes and methods

# actions_ThrowAction class attributes and methods
actions_ThrowAction_eventID: Property = Property(name="eventID", type=StringType)
actions_ThrowAction.attributes={actions_ThrowAction_eventID}

# actions_TermAction class attributes and methods

# actions_Term class attributes and methods

# actions_ReconfigurationAction class attributes and methods

# actions_SetDataAction class attributes and methods

# ReconfigurationAction class attributes and methods

# IValueFunction class attributes and methods

# IDataNodeFunction class attributes and methods

# Action class attributes and methods

# actions_RemoveBagAction class attributes and methods

# DataBag class attributes and methods

# IArithmetricFunction class attributes and methods

# actions_ActivateFeatureAction class attributes and methods

# IFeature class attributes and methods

# FeatureVersion class attributes and methods

# actions_DeactivateFeatureAction class attributes and methods

# actions_SetPropertyAction class attributes and methods

# DataLeaf class attributes and methods

# actions_GetDataAction class attributes and methods

# actions_FailAction class attributes and methods

# actions_TimeAction class attributes and methods
actions_TimeAction_time: Property = Property(name="time", type=IntegerType)
actions_TimeAction.attributes={actions_TimeAction_time}

# ITimeConsumer class attributes and methods

# actions_DependentAction class attributes and methods

# actions_GetPropertyAction class attributes and methods

# DependentAction class attributes and methods

# actions_GetRealTimeAction class attributes and methods
actions_GetRealTimeAction_timeHint: Property = Property(name="timeHint", type=StringType)
actions_GetRealTimeAction.attributes={actions_GetRealTimeAction_timeHint}

# actions_GetFeatureStateAction class attributes and methods

# DataElement class attributes and methods

# Relationships
action0: BinaryAssociation = BinaryAssociation(
    name="action0",
    ends={
        Property(name="actions_StandAloneAction", type=actions_ActionReference, multiplicity=Multiplicity(1, 1)),
        Property(name="actions_ActionReference", type=actions_StandAloneAction, multiplicity=Multiplicity(1, 1))
    }
)
parameters1: BinaryAssociation = BinaryAssociation(
    name="parameters1",
    ends={
        Property(name="actions_EObject", type=actions_ActionReference, multiplicity=Multiplicity(1, 1)),
        Property(name="actions_ActionReference2", type=actions_EObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
action3: BinaryAssociation = BinaryAssociation(
    name="action3",
    ends={
        Property(name="actions_PreGenerationAction", type=actions_StandAloneAction, multiplicity=Multiplicity(1, 1)),
        Property(name="actions_StandAloneAction4", type=actions_PreGenerationAction, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
parameters5: BinaryAssociation = BinaryAssociation(
    name="parameters5",
    ends={
        Property(name="IContextVariable", type=actions_StandAloneAction, multiplicity=Multiplicity(1, 1)),
        Property(name="actions_StandAloneAction6", type=IContextVariable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
action7: BinaryAssociation = BinaryAssociation(
    name="action7",
    ends={
        Property(name="actions_PreGenerationAction8", type=actions_TimedConditionAction, multiplicity=Multiplicity(1, 1)),
        Property(name="actions_TimedConditionAction", type=actions_PreGenerationAction, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
condition9: BinaryAssociation = BinaryAssociation(
    name="condition9",
    ends={
        Property(name="ILogicFunction", type=actions_TimedConditionAction, multiplicity=Multiplicity(1, 1)),
        Property(name="actions_TimedConditionAction10", type=ILogicFunction, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
actions11: BinaryAssociation = BinaryAssociation(
    name="actions11",
    ends={
        Property(name="actions_PreGenerationAction12", type=actions_PreGenerationSequence, multiplicity=Multiplicity(1, 1)),
        Property(name="actions_PreGenerationSequence", type=actions_PreGenerationAction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
actions13: BinaryAssociation = BinaryAssociation(
    name="actions13",
    ends={
        Property(name="actions_PostGenerationAction", type=actions_PostGenerationSequence, multiplicity=Multiplicity(1, 1)),
        Property(name="actions_PostGenerationSequence", type=actions_PostGenerationAction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
term14: BinaryAssociation = BinaryAssociation(
    name="term14",
    ends={
        Property(name="actions_Term", type=actions_TermAction, multiplicity=Multiplicity(1, 1)),
        Property(name="actions_TermAction", type=actions_Term, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
values15: BinaryAssociation = BinaryAssociation(
    name="values15",
    ends={
        Property(name="IValueFunction", type=actions_SetDataAction, multiplicity=Multiplicity(1, 1)),
        Property(name="actions_SetDataAction", type=IValueFunction, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
node16: BinaryAssociation = BinaryAssociation(
    name="node16",
    ends={
        Property(name="IDataNodeFunction", type=actions_SetDataAction, multiplicity=Multiplicity(1, 1)),
        Property(name="actions_SetDataAction17", type=IDataNodeFunction, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
node18: BinaryAssociation = BinaryAssociation(
    name="node18",
    ends={
        Property(name="IDataNodeFunction19", type=actions_GetDataAction, multiplicity=Multiplicity(1, 1)),
        Property(name="actions_GetDataAction", type=IDataNodeFunction, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
bag20: BinaryAssociation = BinaryAssociation(
    name="bag20",
    ends={
        Property(name="DataBag", type=actions_RemoveBagAction, multiplicity=Multiplicity(1, 1)),
        Property(name="actions_RemoveBagAction", type=DataBag, multiplicity=Multiplicity(1, 1))
    }
)
index21: BinaryAssociation = BinaryAssociation(
    name="index21",
    ends={
        Property(name="IArithmetricFunction", type=actions_RemoveBagAction, multiplicity=Multiplicity(1, 1)),
        Property(name="actions_RemoveBagAction22", type=IArithmetricFunction, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
feature23: BinaryAssociation = BinaryAssociation(
    name="feature23",
    ends={
        Property(name="IFeature", type=actions_ActivateFeatureAction, multiplicity=Multiplicity(1, 1)),
        Property(name="actions_ActivateFeatureAction", type=IFeature, multiplicity=Multiplicity(1, 1))
    }
)
version24: BinaryAssociation = BinaryAssociation(
    name="version24",
    ends={
        Property(name="FeatureVersion", type=actions_ActivateFeatureAction, multiplicity=Multiplicity(1, 1)),
        Property(name="actions_ActivateFeatureAction25", type=FeatureVersion, multiplicity=Multiplicity(0, 1))
    }
)
feature26: BinaryAssociation = BinaryAssociation(
    name="feature26",
    ends={
        Property(name="IFeature27", type=actions_DeactivateFeatureAction, multiplicity=Multiplicity(1, 1)),
        Property(name="actions_DeactivateFeatureAction", type=IFeature, multiplicity=Multiplicity(1, 1))
    }
)
consumer31: BinaryAssociation = BinaryAssociation(
    name="consumer31",
    ends={
        Property(name="ITimeConsumer", type=actions_TimeAction, multiplicity=Multiplicity(1, 1)),
        Property(name="actions_TimeAction", type=ITimeConsumer, multiplicity=Multiplicity(0, 1))
    }
)
property32: BinaryAssociation = BinaryAssociation(
    name="property32",
    ends={
        Property(name="DataLeaf33", type=actions_GetPropertyAction, multiplicity=Multiplicity(1, 1)),
        Property(name="actions_GetPropertyAction", type=DataLeaf, multiplicity=Multiplicity(1, 1))
    }
)
feature34: BinaryAssociation = BinaryAssociation(
    name="feature34",
    ends={
        Property(name="IFeature35", type=actions_GetFeatureStateAction, multiplicity=Multiplicity(1, 1)),
        Property(name="actions_GetFeatureStateAction", type=IFeature, multiplicity=Multiplicity(1, 1))
    }
)
property28: BinaryAssociation = BinaryAssociation(
    name="property28",
    ends={
        Property(name="DataLeaf", type=actions_SetPropertyAction, multiplicity=Multiplicity(1, 1)),
        Property(name="actions_SetPropertyAction", type=DataLeaf, multiplicity=Multiplicity(1, 1))
    }
)
value29: BinaryAssociation = BinaryAssociation(
    name="value29",
    ends={
        Property(name="DataElement", type=actions_SetPropertyAction, multiplicity=Multiplicity(1, 1)),
        Property(name="actions_SetPropertyAction30", type=DataElement, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_actions_ActionReference_PreGenerationAction = Generalization(general=PreGenerationAction, specific=actions_ActionReference)
gen_actions_StandAloneAction_core_AbstractModelElement = Generalization(general=core_AbstractModelElement, specific=actions_StandAloneAction)
gen_actions_StandAloneAction_core_ITopLevelElement = Generalization(general=core_ITopLevelElement, specific=actions_StandAloneAction)
gen_actions_TimedConditionAction_core_AbstractModelElement = Generalization(general=core_AbstractModelElement, specific=actions_TimedConditionAction)
gen_actions_TimedConditionAction_core_ITopLevelElement = Generalization(general=core_ITopLevelElement, specific=actions_TimedConditionAction)
gen_actions_TimedConditionAction_rules_IRealTimeConsumer = Generalization(general=rules_IRealTimeConsumer, specific=actions_TimedConditionAction)
gen_actions_PostGenerationAction_Action = Generalization(general=Action, specific=actions_PostGenerationAction)
gen_actions_PreGenerationSequence_PreGenerationAction = Generalization(general=PreGenerationAction, specific=actions_PreGenerationSequence)
gen_actions_PostGenerationSequence_PostGenerationAction = Generalization(general=PostGenerationAction, specific=actions_PostGenerationSequence)
gen_actions_ThrowAction_PreGenerationAction = Generalization(general=PreGenerationAction, specific=actions_ThrowAction)
gen_actions_TermAction_PostGenerationAction = Generalization(general=PostGenerationAction, specific=actions_TermAction)
gen_actions_TermAction_PreGenerationAction = Generalization(general=PreGenerationAction, specific=actions_TermAction)
gen_actions_ReconfigurationAction_PreGenerationAction = Generalization(general=PreGenerationAction, specific=actions_ReconfigurationAction)
gen_actions_SetDataAction_ReconfigurationAction = Generalization(general=ReconfigurationAction, specific=actions_SetDataAction)
gen_actions_PreGenerationAction_Action = Generalization(general=Action, specific=actions_PreGenerationAction)
gen_actions_RemoveBagAction_ReconfigurationAction = Generalization(general=ReconfigurationAction, specific=actions_RemoveBagAction)
gen_actions_ActivateFeatureAction_PostGenerationAction = Generalization(general=PostGenerationAction, specific=actions_ActivateFeatureAction)
gen_actions_ActivateFeatureAction_ReconfigurationAction = Generalization(general=ReconfigurationAction, specific=actions_ActivateFeatureAction)
gen_actions_DeactivateFeatureAction_PostGenerationAction = Generalization(general=PostGenerationAction, specific=actions_DeactivateFeatureAction)
gen_actions_DeactivateFeatureAction_ReconfigurationAction = Generalization(general=ReconfigurationAction, specific=actions_DeactivateFeatureAction)
gen_actions_SetPropertyAction_PostGenerationAction = Generalization(general=PostGenerationAction, specific=actions_SetPropertyAction)
gen_actions_GetDataAction_PreGenerationAction = Generalization(general=PreGenerationAction, specific=actions_GetDataAction)
gen_actions_FailAction_PostGenerationAction = Generalization(general=PostGenerationAction, specific=actions_FailAction)
gen_actions_FailAction_PreGenerationAction = Generalization(general=PreGenerationAction, specific=actions_FailAction)
gen_actions_TimeAction_PreGenerationAction = Generalization(general=PreGenerationAction, specific=actions_TimeAction)
gen_actions_DependentAction_PostGenerationAction = Generalization(general=PostGenerationAction, specific=actions_DependentAction)
gen_actions_GetPropertyAction_DependentAction = Generalization(general=DependentAction, specific=actions_GetPropertyAction)
gen_actions_GetRealTimeAction_DependentAction = Generalization(general=DependentAction, specific=actions_GetRealTimeAction)
gen_actions_GetRealTimeAction_PreGenerationAction = Generalization(general=PreGenerationAction, specific=actions_GetRealTimeAction)
gen_actions_GetFeatureStateAction_DependentAction = Generalization(general=DependentAction, specific=actions_GetFeatureStateAction)
gen_actions_GetFeatureStateAction_PreGenerationAction = Generalization(general=PreGenerationAction, specific=actions_GetFeatureStateAction)

# Domain Model
domain_model = DomainModel(
    name="actions",
    types={actions_ActionReference, PreGenerationAction, actions_StandAloneAction, actions_EObject, core_AbstractModelElement, core_ITopLevelElement, actions_PreGenerationAction, IContextVariable, actions_TimedConditionAction, rules_IRealTimeConsumer, ILogicFunction, actions_Action, actions_PostGenerationAction, actions_PreGenerationSequence, actions_PostGenerationSequence, PostGenerationAction, actions_ThrowAction, actions_TermAction, actions_Term, actions_ReconfigurationAction, actions_SetDataAction, ReconfigurationAction, IValueFunction, IDataNodeFunction, Action, actions_RemoveBagAction, DataBag, IArithmetricFunction, actions_ActivateFeatureAction, IFeature, FeatureVersion, actions_DeactivateFeatureAction, actions_SetPropertyAction, DataLeaf, actions_GetDataAction, actions_FailAction, actions_TimeAction, ITimeConsumer, actions_DependentAction, actions_GetPropertyAction, DependentAction, actions_GetRealTimeAction, actions_GetFeatureStateAction, DataElement},
    associations={action0, parameters1, action3, parameters5, action7, condition9, actions11, actions13, term14, values15, node16, node18, bag20, index21, feature23, version24, feature26, consumer31, property32, feature34, property28, value29},
    generalizations={gen_actions_ActionReference_PreGenerationAction, gen_actions_StandAloneAction_core_AbstractModelElement, gen_actions_StandAloneAction_core_ITopLevelElement, gen_actions_TimedConditionAction_core_AbstractModelElement, gen_actions_TimedConditionAction_core_ITopLevelElement, gen_actions_TimedConditionAction_rules_IRealTimeConsumer, gen_actions_PostGenerationAction_Action, gen_actions_PreGenerationSequence_PreGenerationAction, gen_actions_PostGenerationSequence_PostGenerationAction, gen_actions_ThrowAction_PreGenerationAction, gen_actions_TermAction_PostGenerationAction, gen_actions_TermAction_PreGenerationAction, gen_actions_ReconfigurationAction_PreGenerationAction, gen_actions_SetDataAction_ReconfigurationAction, gen_actions_PreGenerationAction_Action, gen_actions_RemoveBagAction_ReconfigurationAction, gen_actions_ActivateFeatureAction_PostGenerationAction, gen_actions_ActivateFeatureAction_ReconfigurationAction, gen_actions_DeactivateFeatureAction_PostGenerationAction, gen_actions_DeactivateFeatureAction_ReconfigurationAction, gen_actions_SetPropertyAction_PostGenerationAction, gen_actions_GetDataAction_PreGenerationAction, gen_actions_FailAction_PostGenerationAction, gen_actions_FailAction_PreGenerationAction, gen_actions_TimeAction_PreGenerationAction, gen_actions_DependentAction_PostGenerationAction, gen_actions_GetPropertyAction_DependentAction, gen_actions_GetRealTimeAction_DependentAction, gen_actions_GetRealTimeAction_PreGenerationAction, gen_actions_GetFeatureStateAction_DependentAction, gen_actions_GetFeatureStateAction_PreGenerationAction},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)