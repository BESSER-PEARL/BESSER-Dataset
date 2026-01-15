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
stateChart_Variable = Class(name="stateChart::Variable")
stateChart_Node = Class(name="stateChart::Node")
stateChart_Transition = Class(name="stateChart::Transition")
stateChart_Model = Class(name="stateChart::Model")

# stateChart_Variable class attributes and methods
stateChart_Variable_name: Property = Property(name="name", type=StringType)
stateChart_Variable_type: Property = Property(name="type", type=StringType)
stateChart_Variable.attributes={stateChart_Variable_name, stateChart_Variable_type}

# stateChart_Node class attributes and methods
stateChart_Node_name: Property = Property(name="name", type=StringType)
stateChart_Node_label: Property = Property(name="label", type=StringType)
stateChart_Node_type: Property = Property(name="type", type=StringType)
stateChart_Node_activity: Property = Property(name="activity", type=StringType)
stateChart_Node_actions: Property = Property(name="actions", type=StringType)
stateChart_Node_metadata: Property = Property(name="metadata", type=StringType)
stateChart_Node.attributes={stateChart_Node_type, stateChart_Node_metadata, stateChart_Node_actions, stateChart_Node_label, stateChart_Node_activity, stateChart_Node_name}

# stateChart_Transition class attributes and methods
stateChart_Transition_TE: Property = Property(name="TE", type=StringType)
stateChart_Transition_name: Property = Property(name="name", type=StringType)
stateChart_Transition_metadata: Property = Property(name="metadata", type=StringType)
stateChart_Transition.attributes={stateChart_Transition_TE, stateChart_Transition_name, stateChart_Transition_metadata}

# stateChart_Model class attributes and methods
stateChart_Model_name: Property = Property(name="name", type=StringType)
stateChart_Model_description: Property = Property(name="description", type=StringType)
stateChart_Model_metadata: Property = Property(name="metadata", type=StringType)
stateChart_Model.attributes={stateChart_Model_metadata, stateChart_Model_description, stateChart_Model_name}

# Relationships
variables0: BinaryAssociation = BinaryAssociation(
    name="variables0",
    ends={
        Property(name="stateChart_Variable", type=stateChart_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="stateChart_Node", type=stateChart_Variable, multiplicity=Multiplicity(0, 9999))
    }
)
Children2: BinaryAssociation = BinaryAssociation(
    name="Children2",
    ends={
        Property(name="Node", type=stateChart_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="Father", type=stateChart_Node, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Father4: BinaryAssociation = BinaryAssociation(
    name="Father4",
    ends={
        Property(name="Node5", type=stateChart_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="Children", type=stateChart_Node, multiplicity=Multiplicity(0, 1))
    }
)
child6: BinaryAssociation = BinaryAssociation(
    name="child6",
    ends={
        Property(name="stateChart_Transition", type=stateChart_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="stateChart_Node7", type=stateChart_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parent8: BinaryAssociation = BinaryAssociation(
    name="parent8",
    ends={
        Property(name="stateChart_Transition10", type=stateChart_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="stateChart_Node9", type=stateChart_Transition, multiplicity=Multiplicity(0, 1))
    }
)
nodes11: BinaryAssociation = BinaryAssociation(
    name="nodes11",
    ends={
        Property(name="stateChart_Node12", type=stateChart_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="stateChart_Model", type=stateChart_Node, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
variables13: BinaryAssociation = BinaryAssociation(
    name="variables13",
    ends={
        Property(name="stateChart_Variable15", type=stateChart_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="stateChart_Model14", type=stateChart_Variable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transitions16: BinaryAssociation = BinaryAssociation(
    name="transitions16",
    ends={
        Property(name="stateChart_Transition18", type=stateChart_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="stateChart_Model17", type=stateChart_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
source19: BinaryAssociation = BinaryAssociation(
    name="source19",
    ends={
        Property(name="stateChart_Node21", type=stateChart_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="stateChart_Transition20", type=stateChart_Node, multiplicity=Multiplicity(0, 1))
    }
)
target22: BinaryAssociation = BinaryAssociation(
    name="target22",
    ends={
        Property(name="stateChart_Node24", type=stateChart_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="stateChart_Transition23", type=stateChart_Node, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="stateChart",
    types={stateChart_Variable, stateChart_Node, stateChart_Transition, stateChart_Model},
    associations={variables0, Children2, Father4, child6, parent8, nodes11, variables13, transitions16, source19, target22},
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