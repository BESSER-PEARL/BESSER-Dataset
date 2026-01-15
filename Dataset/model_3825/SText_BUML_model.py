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
TimeEventType: Enumeration = Enumeration(
    name="TimeEventType",
    literals={
            EnumerationLiteral(name="after"),
			EnumerationLiteral(name="every")
    }
)

TimeUnit: Enumeration = Enumeration(
    name="TimeUnit",
    literals={
            EnumerationLiteral(name="second"),
			EnumerationLiteral(name="millisecond"),
			EnumerationLiteral(name="microsecond"),
			EnumerationLiteral(name="nanosecond")
    }
)

# Classes
stext_StateRoot = Class(name="stext::StateRoot")
stext_StateSpecification = Class(name="stext::StateSpecification")
stext_TransitionRoot = Class(name="stext::TransitionRoot")
stext_Root = Class(name="stext::Root")
stext_DefRoot = Class(name="stext::DefRoot")
stext_StatechartRoot = Class(name="stext::StatechartRoot")
DefRoot = Class(name="DefRoot")
stext_StatechartSpecification = Class(name="stext::StatechartSpecification")
stext_EventDefinition = Class(name="stext::EventDefinition")
Event = Class(name="Event")
stext_VariableDefinition = Class(name="stext::VariableDefinition")
Property_ = Class(name="Property")
stext_TransitionSpecification = Class(name="stext::TransitionSpecification")
ScopedElement = Class(name="ScopedElement")
stext_Scope = Class(name="stext::Scope")
stext_TransitionReaction = Class(name="stext::TransitionReaction")
stext_StatechartScope = Class(name="stext::StatechartScope")
Scope = Class(name="Scope")
stext_InterfaceScope = Class(name="stext::InterfaceScope")
StatechartScope = Class(name="StatechartScope")
NamedElement = Class(name="NamedElement")
stext_InternalScope = Class(name="stext::InternalScope")
stext_ImportScope = Class(name="stext::ImportScope")
stext_Package = Class(name="stext::Package")
stext_TimeEventSpec = Class(name="stext::TimeEventSpec")
stext_Expression = Class(name="stext::Expression")
stext_OperationDefinition = Class(name="stext::OperationDefinition")
Operation = Class(name="Operation")
stext_TypeAliasDefinition = Class(name="stext::TypeAliasDefinition")
TypeAlias = Class(name="TypeAlias")
Declaration = Class(name="Declaration")
stext_LocalReaction = Class(name="stext::LocalReaction")
Reaction = Class(name="Reaction")
stext_Guard = Class(name="stext::Guard")
stext_EntryPointSpec = Class(name="stext::EntryPointSpec")
ReactionProperty = Class(name="ReactionProperty")
stext_ExitPointSpec = Class(name="stext::ExitPointSpec")
stext_EventSpec = Class(name="stext::EventSpec")
stext_RegularEventSpec = Class(name="stext::RegularEventSpec")
EventSpec = Class(name="EventSpec")
stext_ReactionTrigger = Class(name="stext::ReactionTrigger")
Trigger = Class(name="Trigger")
stext_BuiltinEventSpec = Class(name="stext::BuiltinEventSpec")
stext_EntryEvent = Class(name="stext::EntryEvent")
BuiltinEventSpec = Class(name="BuiltinEventSpec")
stext_ExitEvent = Class(name="stext::ExitEvent")
stext_AlwaysEvent = Class(name="stext::AlwaysEvent")
stext_SimpleScope = Class(name="stext::SimpleScope")
stext_DefaultTrigger = Class(name="stext::DefaultTrigger")
stext_ReactionEffect = Class(name="stext::ReactionEffect")
Effect = Class(name="Effect")
stext_EventRaisingExpression = Class(name="stext::EventRaisingExpression")
Expression = Class(name="Expression")
stext_EventValueReferenceExpression = Class(name="stext::EventValueReferenceExpression")
stext_ActiveStateReferenceExpression = Class(name="stext::ActiveStateReferenceExpression")
stext_State = Class(name="stext::State")

# stext_StateRoot class attributes and methods

# stext_StateSpecification class attributes and methods

# stext_TransitionRoot class attributes and methods

# stext_Root class attributes and methods

# stext_DefRoot class attributes and methods

# stext_StatechartRoot class attributes and methods

# DefRoot class attributes and methods

# stext_StatechartSpecification class attributes and methods

# stext_EventDefinition class attributes and methods

# Event class attributes and methods

# stext_VariableDefinition class attributes and methods

# Property class attributes and methods

# stext_TransitionSpecification class attributes and methods

# ScopedElement class attributes and methods

# stext_Scope class attributes and methods

# stext_TransitionReaction class attributes and methods

# stext_StatechartScope class attributes and methods

# Scope class attributes and methods

# stext_InterfaceScope class attributes and methods

# StatechartScope class attributes and methods

# NamedElement class attributes and methods

# stext_InternalScope class attributes and methods

# stext_ImportScope class attributes and methods

# stext_Package class attributes and methods

# stext_TimeEventSpec class attributes and methods
stext_TimeEventSpec_type: Property = Property(name="type", type=StringType)
stext_TimeEventSpec_unit: Property = Property(name="unit", type=StringType)
stext_TimeEventSpec.attributes={stext_TimeEventSpec_unit, stext_TimeEventSpec_type}

# stext_Expression class attributes and methods

# stext_OperationDefinition class attributes and methods

# Operation class attributes and methods

# stext_TypeAliasDefinition class attributes and methods

# TypeAlias class attributes and methods

# Declaration class attributes and methods

# stext_LocalReaction class attributes and methods

# Reaction class attributes and methods

# stext_Guard class attributes and methods

# stext_EntryPointSpec class attributes and methods
stext_EntryPointSpec_entrypoint: Property = Property(name="entrypoint", type=StringType)
stext_EntryPointSpec.attributes={stext_EntryPointSpec_entrypoint}

# ReactionProperty class attributes and methods

# stext_ExitPointSpec class attributes and methods
stext_ExitPointSpec_exitpoint: Property = Property(name="exitpoint", type=StringType)
stext_ExitPointSpec.attributes={stext_ExitPointSpec_exitpoint}

# stext_EventSpec class attributes and methods

# stext_RegularEventSpec class attributes and methods

# EventSpec class attributes and methods

# stext_ReactionTrigger class attributes and methods

# Trigger class attributes and methods

# stext_BuiltinEventSpec class attributes and methods

# stext_EntryEvent class attributes and methods

# BuiltinEventSpec class attributes and methods

# stext_ExitEvent class attributes and methods

# stext_AlwaysEvent class attributes and methods

# stext_SimpleScope class attributes and methods

# stext_DefaultTrigger class attributes and methods

# stext_ReactionEffect class attributes and methods

# Effect class attributes and methods

# stext_EventRaisingExpression class attributes and methods

# Expression class attributes and methods

# stext_EventValueReferenceExpression class attributes and methods

# stext_ActiveStateReferenceExpression class attributes and methods

# stext_State class attributes and methods

# Relationships
def2: BinaryAssociation = BinaryAssociation(
    name="def2",
    ends={
        Property(name="stext_StateSpecification", type=stext_StateRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="stext_StateRoot", type=stext_StateSpecification, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
roots0: BinaryAssociation = BinaryAssociation(
    name="roots0",
    ends={
        Property(name="stext_DefRoot", type=stext_Root, multiplicity=Multiplicity(1, 1)),
        Property(name="stext_Root", type=stext_DefRoot, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
def1: BinaryAssociation = BinaryAssociation(
    name="def1",
    ends={
        Property(name="stext_StatechartSpecification", type=stext_StatechartRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="stext_StatechartRoot", type=stext_StatechartSpecification, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
imports8: BinaryAssociation = BinaryAssociation(
    name="imports8",
    ends={
        Property(name="stext_ImportScope", type=stext_Package, multiplicity=Multiplicity(0, 9999)),
        Property(name="stext_Package", type=stext_ImportScope, multiplicity=Multiplicity(1, 1))
    }
)
def3: BinaryAssociation = BinaryAssociation(
    name="def3",
    ends={
        Property(name="stext_TransitionSpecification", type=stext_TransitionRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="stext_TransitionRoot", type=stext_TransitionSpecification, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
scope4: BinaryAssociation = BinaryAssociation(
    name="scope4",
    ends={
        Property(name="stext_Scope", type=stext_StateSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="stext_StateSpecification5", type=stext_Scope, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
reaction6: BinaryAssociation = BinaryAssociation(
    name="reaction6",
    ends={
        Property(name="stext_TransitionReaction", type=stext_TransitionSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="stext_TransitionSpecification7", type=stext_TransitionReaction, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
event12: BinaryAssociation = BinaryAssociation(
    name="event12",
    ends={
        Property(name="stext_Expression13", type=stext_RegularEventSpec, multiplicity=Multiplicity(1, 1)),
        Property(name="stext_RegularEventSpec", type=stext_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
initialValue9: BinaryAssociation = BinaryAssociation(
    name="initialValue9",
    ends={
        Property(name="stext_Expression", type=stext_VariableDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="stext_VariableDefinition", type=stext_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression10: BinaryAssociation = BinaryAssociation(
    name="expression10",
    ends={
        Property(name="stext_Expression11", type=stext_Guard, multiplicity=Multiplicity(1, 1)),
        Property(name="stext_Guard", type=stext_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
triggers16: BinaryAssociation = BinaryAssociation(
    name="triggers16",
    ends={
        Property(name="stext_EventSpec", type=stext_ReactionTrigger, multiplicity=Multiplicity(1, 1)),
        Property(name="stext_ReactionTrigger", type=stext_EventSpec, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
value14: BinaryAssociation = BinaryAssociation(
    name="value14",
    ends={
        Property(name="stext_Expression15", type=stext_TimeEventSpec, multiplicity=Multiplicity(1, 1)),
        Property(name="stext_TimeEventSpec", type=stext_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
value29: BinaryAssociation = BinaryAssociation(
    name="value29",
    ends={
        Property(name="stext_ActiveStateReferenceExpression", type=stext_State, multiplicity=Multiplicity(0, 1)),
        Property(name="stext_State", type=stext_ActiveStateReferenceExpression, multiplicity=Multiplicity(1, 1))
    }
)
guard17: BinaryAssociation = BinaryAssociation(
    name="guard17",
    ends={
        Property(name="stext_Guard19", type=stext_ReactionTrigger, multiplicity=Multiplicity(1, 1)),
        Property(name="stext_ReactionTrigger18", type=stext_Guard, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
actions20: BinaryAssociation = BinaryAssociation(
    name="actions20",
    ends={
        Property(name="stext_Expression21", type=stext_ReactionEffect, multiplicity=Multiplicity(1, 1)),
        Property(name="stext_ReactionEffect", type=stext_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
event22: BinaryAssociation = BinaryAssociation(
    name="event22",
    ends={
        Property(name="stext_Expression23", type=stext_EventRaisingExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="stext_EventRaisingExpression", type=stext_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
value24: BinaryAssociation = BinaryAssociation(
    name="value24",
    ends={
        Property(name="stext_Expression26", type=stext_EventRaisingExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="stext_EventRaisingExpression25", type=stext_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
value27: BinaryAssociation = BinaryAssociation(
    name="value27",
    ends={
        Property(name="stext_Expression28", type=stext_EventValueReferenceExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="stext_EventValueReferenceExpression", type=stext_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_stext_StateRoot_DefRoot = Generalization(general=DefRoot, specific=stext_StateRoot)
gen_stext_StatechartRoot_DefRoot = Generalization(general=DefRoot, specific=stext_StatechartRoot)
gen_stext_EventDefinition_Event = Generalization(general=Event, specific=stext_EventDefinition)
gen_stext_VariableDefinition_Property = Generalization(general=Property_, specific=stext_VariableDefinition)
gen_stext_TransitionRoot_DefRoot = Generalization(general=DefRoot, specific=stext_TransitionRoot)
gen_stext_StatechartSpecification_ScopedElement = Generalization(general=ScopedElement, specific=stext_StatechartSpecification)
gen_stext_StatechartScope_Scope = Generalization(general=Scope, specific=stext_StatechartScope)
gen_stext_InterfaceScope_StatechartScope = Generalization(general=StatechartScope, specific=stext_InterfaceScope)
gen_stext_InterfaceScope_NamedElement = Generalization(general=NamedElement, specific=stext_InterfaceScope)
gen_stext_InternalScope_StatechartScope = Generalization(general=StatechartScope, specific=stext_InternalScope)
gen_stext_ImportScope_StatechartScope = Generalization(general=StatechartScope, specific=stext_ImportScope)
gen_stext_RegularEventSpec_EventSpec = Generalization(general=EventSpec, specific=stext_RegularEventSpec)
gen_stext_TimeEventSpec_EventSpec = Generalization(general=EventSpec, specific=stext_TimeEventSpec)
gen_stext_OperationDefinition_Operation = Generalization(general=Operation, specific=stext_OperationDefinition)
gen_stext_TypeAliasDefinition_TypeAlias = Generalization(general=TypeAlias, specific=stext_TypeAliasDefinition)
gen_stext_TypeAliasDefinition_Declaration = Generalization(general=Declaration, specific=stext_TypeAliasDefinition)
gen_stext_LocalReaction_Reaction = Generalization(general=Reaction, specific=stext_LocalReaction)
gen_stext_TransitionReaction_Reaction = Generalization(general=Reaction, specific=stext_TransitionReaction)
gen_stext_EntryPointSpec_ReactionProperty = Generalization(general=ReactionProperty, specific=stext_EntryPointSpec)
gen_stext_ExitPointSpec_ReactionProperty = Generalization(general=ReactionProperty, specific=stext_ExitPointSpec)
gen_stext_ReactionTrigger_Trigger = Generalization(general=Trigger, specific=stext_ReactionTrigger)
gen_stext_BuiltinEventSpec_EventSpec = Generalization(general=EventSpec, specific=stext_BuiltinEventSpec)
gen_stext_EntryEvent_BuiltinEventSpec = Generalization(general=BuiltinEventSpec, specific=stext_EntryEvent)
gen_stext_ExitEvent_BuiltinEventSpec = Generalization(general=BuiltinEventSpec, specific=stext_ExitEvent)
gen_stext_AlwaysEvent_BuiltinEventSpec = Generalization(general=BuiltinEventSpec, specific=stext_AlwaysEvent)
gen_stext_SimpleScope_Scope = Generalization(general=Scope, specific=stext_SimpleScope)
gen_stext_DefaultTrigger_Trigger = Generalization(general=Trigger, specific=stext_DefaultTrigger)
gen_stext_ReactionEffect_Effect = Generalization(general=Effect, specific=stext_ReactionEffect)
gen_stext_EventRaisingExpression_Expression = Generalization(general=Expression, specific=stext_EventRaisingExpression)
gen_stext_EventValueReferenceExpression_Expression = Generalization(general=Expression, specific=stext_EventValueReferenceExpression)
gen_stext_ActiveStateReferenceExpression_Expression = Generalization(general=Expression, specific=stext_ActiveStateReferenceExpression)

# Domain Model
domain_model = DomainModel(
    name="stext",
    types={stext_StateRoot, stext_StateSpecification, stext_TransitionRoot, stext_Root, stext_DefRoot, stext_StatechartRoot, DefRoot, stext_StatechartSpecification, stext_EventDefinition, Event, stext_VariableDefinition, Property_, stext_TransitionSpecification, ScopedElement, stext_Scope, stext_TransitionReaction, stext_StatechartScope, Scope, stext_InterfaceScope, StatechartScope, NamedElement, stext_InternalScope, stext_ImportScope, stext_Package, stext_TimeEventSpec, stext_Expression, stext_OperationDefinition, Operation, stext_TypeAliasDefinition, TypeAlias, Declaration, stext_LocalReaction, Reaction, stext_Guard, stext_EntryPointSpec, ReactionProperty, stext_ExitPointSpec, stext_EventSpec, stext_RegularEventSpec, EventSpec, stext_ReactionTrigger, Trigger, stext_BuiltinEventSpec, stext_EntryEvent, BuiltinEventSpec, stext_ExitEvent, stext_AlwaysEvent, stext_SimpleScope, stext_DefaultTrigger, stext_ReactionEffect, Effect, stext_EventRaisingExpression, Expression, stext_EventValueReferenceExpression, stext_ActiveStateReferenceExpression, stext_State, TimeEventType, TimeUnit},
    associations={def2, roots0, def1, imports8, def3, scope4, reaction6, event12, initialValue9, expression10, triggers16, value14, value29, guard17, actions20, event22, value24, value27},
    generalizations={gen_stext_StateRoot_DefRoot, gen_stext_StatechartRoot_DefRoot, gen_stext_EventDefinition_Event, gen_stext_VariableDefinition_Property, gen_stext_TransitionRoot_DefRoot, gen_stext_StatechartSpecification_ScopedElement, gen_stext_StatechartScope_Scope, gen_stext_InterfaceScope_StatechartScope, gen_stext_InterfaceScope_NamedElement, gen_stext_InternalScope_StatechartScope, gen_stext_ImportScope_StatechartScope, gen_stext_RegularEventSpec_EventSpec, gen_stext_TimeEventSpec_EventSpec, gen_stext_OperationDefinition_Operation, gen_stext_TypeAliasDefinition_TypeAlias, gen_stext_TypeAliasDefinition_Declaration, gen_stext_LocalReaction_Reaction, gen_stext_TransitionReaction_Reaction, gen_stext_EntryPointSpec_ReactionProperty, gen_stext_ExitPointSpec_ReactionProperty, gen_stext_ReactionTrigger_Trigger, gen_stext_BuiltinEventSpec_EventSpec, gen_stext_EntryEvent_BuiltinEventSpec, gen_stext_ExitEvent_BuiltinEventSpec, gen_stext_AlwaysEvent_BuiltinEventSpec, gen_stext_SimpleScope_Scope, gen_stext_DefaultTrigger_Trigger, gen_stext_ReactionEffect_Effect, gen_stext_EventRaisingExpression_Expression, gen_stext_EventValueReferenceExpression_Expression, gen_stext_ActiveStateReferenceExpression_Expression},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)