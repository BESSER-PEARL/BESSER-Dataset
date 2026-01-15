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
mindmap_MindMap = Class(name="mindmap::MindMap")
mindmap_CentralTopic = Class(name="mindmap::CentralTopic")
mindmap_Topic = Class(name="mindmap::Topic", is_abstract=True)
Topic = Class(name="Topic")
mindmap_MainTopic = Class(name="mindmap::MainTopic")
mindmap_SubTopic = Class(name="mindmap::SubTopic")

# mindmap_MindMap class attributes and methods
mindmap_MindMap_title: Property = Property(name="title", type=StringType)
mindmap_MindMap.attributes={mindmap_MindMap_title}

# mindmap_CentralTopic class attributes and methods

# mindmap_Topic class attributes and methods
mindmap_Topic_name: Property = Property(name="name", type=StringType)
mindmap_Topic_marker: Property = Property(name="marker", type=IntegerType)
mindmap_Topic.attributes={mindmap_Topic_marker, mindmap_Topic_name}

# Topic class attributes and methods

# mindmap_MainTopic class attributes and methods

# mindmap_SubTopic class attributes and methods

# Relationships
topic0: BinaryAssociation = BinaryAssociation(
    name="topic0",
    ends={
        Property(name="mindmap_CentralTopic", type=mindmap_MindMap, multiplicity=Multiplicity(1, 1)),
        Property(name="mindmap_MindMap", type=mindmap_CentralTopic, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
maintopics1: BinaryAssociation = BinaryAssociation(
    name="maintopics1",
    ends={
        Property(name="mindmap_MainTopic", type=mindmap_CentralTopic, multiplicity=Multiplicity(1, 1)),
        Property(name="mindmap_CentralTopic2", type=mindmap_MainTopic, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
subtopics3: BinaryAssociation = BinaryAssociation(
    name="subtopics3",
    ends={
        Property(name="mindmap_SubTopic", type=mindmap_MainTopic, multiplicity=Multiplicity(1, 1)),
        Property(name="mindmap_MainTopic4", type=mindmap_SubTopic, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
subsubtopics6: BinaryAssociation = BinaryAssociation(
    name="subsubtopics6",
    ends={
        Property(name="mindmap_SubTopic7", type=mindmap_SubTopic, multiplicity=Multiplicity(1, 1)),
        Property(name="mindmap_SubTopic5", type=mindmap_SubTopic, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_mindmap_MainTopic_Topic = Generalization(general=Topic, specific=mindmap_MainTopic)
gen_mindmap_CentralTopic_Topic = Generalization(general=Topic, specific=mindmap_CentralTopic)
gen_mindmap_SubTopic_Topic = Generalization(general=Topic, specific=mindmap_SubTopic)

# Domain Model
domain_model = DomainModel(
    name="mindmap",
    types={mindmap_MindMap, mindmap_CentralTopic, mindmap_Topic, Topic, mindmap_MainTopic, mindmap_SubTopic},
    associations={topic0, maintopics1, subtopics3, subsubtopics6},
    generalizations={gen_mindmap_MainTopic_Topic, gen_mindmap_CentralTopic_Topic, gen_mindmap_SubTopic_Topic},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)