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
labels_TestDynamicEdgeLabel = Class(name="labels::TestDynamicEdgeLabel")
DynamicEdgeLabel = Class(name="DynamicEdgeLabel")
labels_TestDynamicLabel1 = Class(name="labels::TestDynamicLabel1")
DynamicLabel = Class(name="DynamicLabel")
labels_TestDynamicNodeLabel = Class(name="labels::TestDynamicNodeLabel")
DynamicNodeLabel = Class(name="DynamicNodeLabel")
labels_TestIntegerLabelValue = Class(name="labels::TestIntegerLabelValue")
LabelValue = Class(name="LabelValue")
labels_TestLabel = Class(name="labels::TestLabel")
Label = Class(name="Label")
labels_TestStaticEdgeLabel = Class(name="labels::TestStaticEdgeLabel")
StaticEdgeLabel = Class(name="StaticEdgeLabel")
labels_TestStaticNodeLabel = Class(name="labels::TestStaticNodeLabel")
StaticNodeLabel = Class(name="StaticNodeLabel")

# labels_TestDynamicEdgeLabel class attributes and methods
labels_TestDynamicEdgeLabel_m_increment: Method = Method(name="increment", parameters={})
labels_TestDynamicEdgeLabel.methods={labels_TestDynamicEdgeLabel_m_increment}

# DynamicEdgeLabel class attributes and methods

# labels_TestDynamicLabel1 class attributes and methods
labels_TestDynamicLabel1_m_increment: Method = Method(name="increment", parameters={})
labels_TestDynamicLabel1.methods={labels_TestDynamicLabel1_m_increment}

# DynamicLabel class attributes and methods

# labels_TestDynamicNodeLabel class attributes and methods
labels_TestDynamicNodeLabel_m_increment: Method = Method(name="increment", parameters={})
labels_TestDynamicNodeLabel.methods={labels_TestDynamicNodeLabel_m_increment}

# DynamicNodeLabel class attributes and methods

# labels_TestIntegerLabelValue class attributes and methods
labels_TestIntegerLabelValue_i: Property = Property(name="i", type=IntegerType)
labels_TestIntegerLabelValue_m_increment: Method = Method(name="increment", parameters={})
labels_TestIntegerLabelValue.attributes={labels_TestIntegerLabelValue_i}
labels_TestIntegerLabelValue.methods={labels_TestIntegerLabelValue_m_increment}

# LabelValue class attributes and methods

# labels_TestLabel class attributes and methods

# Label class attributes and methods

# labels_TestStaticEdgeLabel class attributes and methods

# StaticEdgeLabel class attributes and methods

# labels_TestStaticNodeLabel class attributes and methods

# StaticNodeLabel class attributes and methods

# Generalizations
gen_labels_TestDynamicEdgeLabel_DynamicEdgeLabel = Generalization(general=DynamicEdgeLabel, specific=labels_TestDynamicEdgeLabel)
gen_labels_TestDynamicLabel1_DynamicLabel = Generalization(general=DynamicLabel, specific=labels_TestDynamicLabel1)
gen_labels_TestDynamicNodeLabel_DynamicNodeLabel = Generalization(general=DynamicNodeLabel, specific=labels_TestDynamicNodeLabel)
gen_labels_TestIntegerLabelValue_LabelValue = Generalization(general=LabelValue, specific=labels_TestIntegerLabelValue)
gen_labels_TestLabel_Label = Generalization(general=Label, specific=labels_TestLabel)
gen_labels_TestStaticEdgeLabel_StaticEdgeLabel = Generalization(general=StaticEdgeLabel, specific=labels_TestStaticEdgeLabel)
gen_labels_TestStaticNodeLabel_StaticNodeLabel = Generalization(general=StaticNodeLabel, specific=labels_TestStaticNodeLabel)

# Domain Model
domain_model = DomainModel(
    name="labels",
    types={labels_TestDynamicEdgeLabel, DynamicEdgeLabel, labels_TestDynamicLabel1, DynamicLabel, labels_TestDynamicNodeLabel, DynamicNodeLabel, labels_TestIntegerLabelValue, LabelValue, labels_TestLabel, Label, labels_TestStaticEdgeLabel, StaticEdgeLabel, labels_TestStaticNodeLabel, StaticNodeLabel},
    associations={},
    generalizations={gen_labels_TestDynamicEdgeLabel_DynamicEdgeLabel, gen_labels_TestDynamicLabel1_DynamicLabel, gen_labels_TestDynamicNodeLabel_DynamicNodeLabel, gen_labels_TestIntegerLabelValue_LabelValue, gen_labels_TestLabel_Label, gen_labels_TestStaticEdgeLabel_StaticEdgeLabel, gen_labels_TestStaticNodeLabel_StaticNodeLabel},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)