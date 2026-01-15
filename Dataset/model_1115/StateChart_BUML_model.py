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
statechart_Model = Class(name="statechart::Model")
statechart_Node = Class(name="statechart::Node")
statechart_Transition = Class(name="statechart::Transition")
statechart_Variable = Class(name="statechart::Variable")

# statechart_Model class attributes and methods
statechart_Model_name: Property = Property(name="name", type=StringType)
statechart_Model_description: Property = Property(name="description", type=StringType)
statechart_Model_metadata: Property = Property(name="metadata", type=StringType)
statechart_Model.attributes={statechart_Model_name, statechart_Model_metadata, statechart_Model_description}

# statechart_Node class attributes and methods
statechart_Node_name: Property = Property(name="name", type=StringType)
statechart_Node_actions: Property = Property(name="actions", type=StringType)
statechart_Node_metadata: Property = Property(name="metadata", type=StringType)
statechart_Node_label: Property = Property(name="label", type=StringType)
statechart_Node_type: Property = Property(name="type", type=StringType)
statechart_Node_activity: Property = Property(name="activity", type=StringType)
statechart_Node.attributes={statechart_Node_label, statechart_Node_type, statechart_Node_metadata, statechart_Node_name, statechart_Node_activity, statechart_Node_actions}

# statechart_Transition class attributes and methods
statechart_Transition_TE: Property = Property(name="TE", type=StringType)
statechart_Transition_name: Property = Property(name="name", type=StringType)
statechart_Transition_metadata: Property = Property(name="metadata", type=StringType)
statechart_Transition.attributes={statechart_Transition_metadata, statechart_Transition_TE, statechart_Transition_name}

# statechart_Variable class attributes and methods
statechart_Variable_name: Property = Property(name="name", type=StringType)
statechart_Variable_type: Property = Property(name="type", type=StringType)
statechart_Variable.attributes={statechart_Variable_type, statechart_Variable_name}

# Relationships
nodes0: BinaryAssociation = BinaryAssociation(
    name="nodes0",
    ends={
        Property(name="statechart_Node", type=statechart_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="statechart_Model", type=statechart_Node, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transitions1: BinaryAssociation = BinaryAssociation(
    name="transitions1",
    ends={
        Property(name="statechart_Transition", type=statechart_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="statechart_Model2", type=statechart_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
variables3: BinaryAssociation = BinaryAssociation(
    name="variables3",
    ends={
        Property(name="statechart_Variable", type=statechart_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="statechart_Model4", type=statechart_Variable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Father11: BinaryAssociation = BinaryAssociation(
    name="Father11",
    ends={
        Property(name="Node12", type=statechart_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="Children", type=statechart_Node, multiplicity=Multiplicity(0, 1))
    }
)
source13: BinaryAssociation = BinaryAssociation(
    name="source13",
    ends={
        Property(name="statechart_Node15", type=statechart_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="statechart_Transition14", type=statechart_Node, multiplicity=Multiplicity(0, 1))
    }
)
target16: BinaryAssociation = BinaryAssociation(
    name="target16",
    ends={
        Property(name="statechart_Node18", type=statechart_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="statechart_Transition17", type=statechart_Node, multiplicity=Multiplicity(0, 1))
    }
)
variables5: BinaryAssociation = BinaryAssociation(
    name="variables5",
    ends={
        Property(name="statechart_Variable7", type=statechart_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="statechart_Node6", type=statechart_Variable, multiplicity=Multiplicity(0, 9999))
    }
)
Children9: BinaryAssociation = BinaryAssociation(
    name="Children9",
    ends={
        Property(name="Node", type=statechart_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="Father", type=statechart_Node, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="statechart",
    types={statechart_Model, statechart_Node, statechart_Transition, statechart_Variable},
    associations={nodes0, transitions1, variables3, Father11, source13, target16, variables5, Children9},
    generalizations={},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)