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
BehaviorKind: Enumeration = Enumeration(
    name="BehaviorKind",
    literals={
            EnumerationLiteral(name="ACTIVITY"),
			EnumerationLiteral(name="STATE_MACHINE"),
			EnumerationLiteral(name="OPAQUE_BEHAVIOR")
    }
)

# Classes
umlTransition_TransitionRule = Class(name="umlTransition_TransitionRule")
umlTransition_EventRule = Class(name="umlTransition_EventRule")
umlTransition_GuardRule = Class(name="umlTransition_GuardRule")
umlTransition_EffectRule = Class(name="umlTransition_EffectRule")
umlTransition_CallOrSignalEventRule = Class(name="umlTransition_CallOrSignalEventRule")
EventRule = Class(name="EventRule")
umlTransition_NamedElement = Class(name="umlTransition_NamedElement")
umlTransition_AnyReceiveEventRule = Class(name="umlTransition_AnyReceiveEventRule")
umlTransition_TimeEventRule = Class(name="umlTransition_TimeEventRule")
umlTransition_RelativeTimeEventRule = Class(name="umlTransition_RelativeTimeEventRule")
TimeEventRule = Class(name="TimeEventRule")
umlTransition_AbsoluteTimeEventRule = Class(name="umlTransition_AbsoluteTimeEventRule")
umlTransition_ChangeEventRule = Class(name="umlTransition_ChangeEventRule")

# umlTransition_TransitionRule class attributes and methods

# umlTransition_EventRule class attributes and methods

# umlTransition_GuardRule class attributes and methods
umlTransition_GuardRule_constraint: Property = Property(name="constraint", type=StringType)
umlTransition_GuardRule.attributes={umlTransition_GuardRule_constraint}

# umlTransition_EffectRule class attributes and methods
umlTransition_EffectRule_kind: Property = Property(name="kind", type=StringType)
umlTransition_EffectRule_behaviorName: Property = Property(name="behaviorName", type=StringType)
umlTransition_EffectRule.attributes={umlTransition_EffectRule_behaviorName, umlTransition_EffectRule_kind}

# umlTransition_CallOrSignalEventRule class attributes and methods

# EventRule class attributes and methods

# umlTransition_NamedElement class attributes and methods

# umlTransition_AnyReceiveEventRule class attributes and methods
umlTransition_AnyReceiveEventRule_isAReceiveEvent: Property = Property(name="isAReceiveEvent", type=StringType)
umlTransition_AnyReceiveEventRule.attributes={umlTransition_AnyReceiveEventRule_isAReceiveEvent}

# umlTransition_TimeEventRule class attributes and methods
umlTransition_TimeEventRule_expr: Property = Property(name="expr", type=StringType)
umlTransition_TimeEventRule.attributes={umlTransition_TimeEventRule_expr}

# umlTransition_RelativeTimeEventRule class attributes and methods

# TimeEventRule class attributes and methods

# umlTransition_AbsoluteTimeEventRule class attributes and methods

# umlTransition_ChangeEventRule class attributes and methods
umlTransition_ChangeEventRule_exp: Property = Property(name="exp", type=StringType)
umlTransition_ChangeEventRule.attributes={umlTransition_ChangeEventRule_exp}

# Relationships
triggers0: BinaryAssociation = BinaryAssociation(
    name="triggers0",
    ends={
        Property(name="umlTransition_EventRule", type=umlTransition_TransitionRule, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTransition_TransitionRule", type=umlTransition_EventRule, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
guard1: BinaryAssociation = BinaryAssociation(
    name="guard1",
    ends={
        Property(name="umlTransition_GuardRule", type=umlTransition_TransitionRule, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTransition_TransitionRule2", type=umlTransition_GuardRule, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
effect3: BinaryAssociation = BinaryAssociation(
    name="effect3",
    ends={
        Property(name="umlTransition_EffectRule", type=umlTransition_TransitionRule, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTransition_TransitionRule4", type=umlTransition_EffectRule, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
operationOrSignal5: BinaryAssociation = BinaryAssociation(
    name="operationOrSignal5",
    ends={
        Property(name="umlTransition_NamedElement", type=umlTransition_CallOrSignalEventRule, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTransition_CallOrSignalEventRule", type=umlTransition_NamedElement, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_umlTransition_CallOrSignalEventRule_EventRule = Generalization(general=EventRule, specific=umlTransition_CallOrSignalEventRule)
gen_umlTransition_AnyReceiveEventRule_EventRule = Generalization(general=EventRule, specific=umlTransition_AnyReceiveEventRule)
gen_umlTransition_TimeEventRule_EventRule = Generalization(general=EventRule, specific=umlTransition_TimeEventRule)
gen_umlTransition_RelativeTimeEventRule_TimeEventRule = Generalization(general=TimeEventRule, specific=umlTransition_RelativeTimeEventRule)
gen_umlTransition_AbsoluteTimeEventRule_TimeEventRule = Generalization(general=TimeEventRule, specific=umlTransition_AbsoluteTimeEventRule)
gen_umlTransition_ChangeEventRule_EventRule = Generalization(general=EventRule, specific=umlTransition_ChangeEventRule)

# Domain Model
domain_model = DomainModel(
    name="umlTransition",
    types={umlTransition_TransitionRule, umlTransition_EventRule, umlTransition_GuardRule, umlTransition_EffectRule, umlTransition_CallOrSignalEventRule, EventRule, umlTransition_NamedElement, umlTransition_AnyReceiveEventRule, umlTransition_TimeEventRule, umlTransition_RelativeTimeEventRule, TimeEventRule, umlTransition_AbsoluteTimeEventRule, umlTransition_ChangeEventRule, BehaviorKind},
    associations={triggers0, guard1, effect3, operationOrSignal5},
    generalizations={gen_umlTransition_CallOrSignalEventRule_EventRule, gen_umlTransition_AnyReceiveEventRule_EventRule, gen_umlTransition_TimeEventRule_EventRule, gen_umlTransition_RelativeTimeEventRule_TimeEventRule, gen_umlTransition_AbsoluteTimeEventRule_TimeEventRule, gen_umlTransition_ChangeEventRule_EventRule},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)