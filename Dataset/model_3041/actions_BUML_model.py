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
actions_CompositeAction = Class(name="actions::CompositeAction")
CompositeProcess = Class(name="CompositeProcess")
actions_ActionResult = Class(name="actions::ActionResult")
actions_Condition = Class(name="actions::Condition")
actions_Expression = Class(name="actions::Expression")
actions_Action = Class(name="actions::Action", is_abstract=True)
Process = Class(name="Process")
actions_Role = Class(name="actions::Role")
actions_AtomicAction = Class(name="actions::AtomicAction")
Action = Class(name="Action")
AtomicProcess = Class(name="AtomicProcess")
actions_AtomicActionResult = Class(name="actions::AtomicActionResult")
actions_ActionsCollection = Class(name="actions::ActionsCollection")
ActionResult = Class(name="ActionResult")
actions_Distribution = Class(name="actions::Distribution")
actions_Participant = Class(name="actions::Participant")
actions_Parameter = Class(name="actions::Parameter")

# actions_CompositeAction class attributes and methods

# CompositeProcess class attributes and methods

# actions_ActionResult class attributes and methods
actions_ActionResult_id: Property = Property(name="id", type=IntegerType)
actions_ActionResult_version: Property = Property(name="version", type=IntegerType)
actions_ActionResult.attributes={actions_ActionResult_id, actions_ActionResult_version}

# actions_Condition class attributes and methods

# actions_Expression class attributes and methods

# actions_Action class attributes and methods

# Process class attributes and methods

# actions_Role class attributes and methods

# actions_AtomicAction class attributes and methods

# Action class attributes and methods

# AtomicProcess class attributes and methods

# actions_AtomicActionResult class attributes and methods
actions_AtomicActionResult_hasDensity: Property = Property(name="hasDensity", type=FloatType)
actions_AtomicActionResult.attributes={actions_AtomicActionResult_hasDensity}

# actions_ActionsCollection class attributes and methods
actions_ActionsCollection_ns: Property = Property(name="ns", type=StringType)
actions_ActionsCollection_id: Property = Property(name="id", type=IntegerType)
actions_ActionsCollection_version: Property = Property(name="version", type=IntegerType)
actions_ActionsCollection.attributes={actions_ActionsCollection_ns, actions_ActionsCollection_version, actions_ActionsCollection_id}

# ActionResult class attributes and methods

# actions_Distribution class attributes and methods
actions_Distribution_datapoint: Property = Property(name="datapoint", type=FloatType)
actions_Distribution_density: Property = Property(name="density", type=FloatType)
actions_Distribution_id: Property = Property(name="id", type=IntegerType)
actions_Distribution_version: Property = Property(name="version", type=IntegerType)
actions_Distribution.attributes={actions_Distribution_id, actions_Distribution_version, actions_Distribution_density, actions_Distribution_datapoint}

# actions_Participant class attributes and methods

# actions_Parameter class attributes and methods

# Relationships
inCondition2: BinaryAssociation = BinaryAssociation(
    name="inCondition2",
    ends={
        Property(name="actions_Condition", type=actions_ActionResult, multiplicity=Multiplicity(1, 1)),
        Property(name="actions_ActionResult", type=actions_Condition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
hasAddEffect3: BinaryAssociation = BinaryAssociation(
    name="hasAddEffect3",
    ends={
        Property(name="actions_Expression", type=actions_ActionResult, multiplicity=Multiplicity(1, 1)),
        Property(name="actions_ActionResult4", type=actions_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
performedByRole0: BinaryAssociation = BinaryAssociation(
    name="performedByRole0",
    ends={
        Property(name="actions_Role", type=actions_Action, multiplicity=Multiplicity(1, 1)),
        Property(name="actions_Action", type=actions_Role, multiplicity=Multiplicity(0, 9999))
    }
)
hasAtomicActionResult1: BinaryAssociation = BinaryAssociation(
    name="hasAtomicActionResult1",
    ends={
        Property(name="actions_AtomicActionResult", type=actions_AtomicAction, multiplicity=Multiplicity(1, 1)),
        Property(name="actions_AtomicAction", type=actions_AtomicActionResult, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
hasDeleteEffect5: BinaryAssociation = BinaryAssociation(
    name="hasDeleteEffect5",
    ends={
        Property(name="actions_Expression7", type=actions_ActionResult, multiplicity=Multiplicity(1, 1)),
        Property(name="actions_ActionResult6", type=actions_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
hasCostDistribution8: BinaryAssociation = BinaryAssociation(
    name="hasCostDistribution8",
    ends={
        Property(name="actions_Distribution", type=actions_AtomicActionResult, multiplicity=Multiplicity(1, 1)),
        Property(name="actions_AtomicActionResult9", type=actions_Distribution, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
hasDurationDistribution10: BinaryAssociation = BinaryAssociation(
    name="hasDurationDistribution10",
    ends={
        Property(name="actions_Distribution12", type=actions_AtomicActionResult, multiplicity=Multiplicity(1, 1)),
        Property(name="actions_AtomicActionResult11", type=actions_Distribution, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
hasQualityDistribution13: BinaryAssociation = BinaryAssociation(
    name="hasQualityDistribution13",
    ends={
        Property(name="actions_Distribution15", type=actions_AtomicActionResult, multiplicity=Multiplicity(1, 1)),
        Property(name="actions_AtomicActionResult14", type=actions_Distribution, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
actions16: BinaryAssociation = BinaryAssociation(
    name="actions16",
    ends={
        Property(name="actions_Action17", type=actions_ActionsCollection, multiplicity=Multiplicity(1, 1)),
        Property(name="actions_ActionsCollection", type=actions_Action, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
participants18: BinaryAssociation = BinaryAssociation(
    name="participants18",
    ends={
        Property(name="actions_Participant", type=actions_ActionsCollection, multiplicity=Multiplicity(1, 1)),
        Property(name="actions_ActionsCollection19", type=actions_Participant, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parameters20: BinaryAssociation = BinaryAssociation(
    name="parameters20",
    ends={
        Property(name="actions_Parameter", type=actions_ActionsCollection, multiplicity=Multiplicity(1, 1)),
        Property(name="actions_ActionsCollection21", type=actions_Parameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_actions_CompositeAction_Action = Generalization(general=Action, specific=actions_CompositeAction)
gen_actions_CompositeAction_CompositeProcess = Generalization(general=CompositeProcess, specific=actions_CompositeAction)
gen_actions_Action_Process = Generalization(general=Process, specific=actions_Action)
gen_actions_AtomicAction_Action = Generalization(general=Action, specific=actions_AtomicAction)
gen_actions_AtomicAction_AtomicProcess = Generalization(general=AtomicProcess, specific=actions_AtomicAction)
gen_actions_AtomicActionResult_ActionResult = Generalization(general=ActionResult, specific=actions_AtomicActionResult)

# Domain Model
domain_model = DomainModel(
    name="actions",
    types={actions_CompositeAction, CompositeProcess, actions_ActionResult, actions_Condition, actions_Expression, actions_Action, Process, actions_Role, actions_AtomicAction, Action, AtomicProcess, actions_AtomicActionResult, actions_ActionsCollection, ActionResult, actions_Distribution, actions_Participant, actions_Parameter},
    associations={inCondition2, hasAddEffect3, performedByRole0, hasAtomicActionResult1, hasDeleteEffect5, hasCostDistribution8, hasDurationDistribution10, hasQualityDistribution13, actions16, participants18, parameters20},
    generalizations={gen_actions_CompositeAction_Action, gen_actions_CompositeAction_CompositeProcess, gen_actions_Action_Process, gen_actions_AtomicAction_Action, gen_actions_AtomicAction_AtomicProcess, gen_actions_AtomicActionResult_ActionResult},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)