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
model_Decorator = Class(name="model::Decorator")
model_DynamicLabel = Class(name="model::DynamicLabel")
model_Graph = Class(name="model::Graph")
model_EdgeDecorator = Class(name="model::EdgeDecorator")
Decorator = Class(name="Decorator")
Identifiable = Class(name="Identifiable")
model_NodeDecorator = Class(name="model::NodeDecorator")
model_GraphDecorator = Class(name="model::GraphDecorator")
model_Model = Class(name="model::Model")
model_STEMTime = Class(name="model::STEMTime")
model_Comparable = Class(name="model::Comparable", is_abstract=True)

# model_Decorator class attributes and methods
model_Decorator_enabled: Property = Property(name="enabled", type=BooleanType)
model_Decorator_graphDecorated: Property = Property(name="graphDecorated", type=BooleanType)
model_Decorator_progress: Property = Property(name="progress", type=FloatType)
model_Decorator_m_prepare: Method = Method(name="prepare", parameters={Parameter(name='model'), Parameter(name='time')})
model_Decorator_m_decorateGraph: Method = Method(name="decorateGraph", parameters={Parameter(name='time')}, type=BooleanType)
model_Decorator_m_updateLabels: Method = Method(name="updateLabels", parameters={Parameter(name='timerPeriod'), Parameter(name='cycle'), Parameter(name='time')})
model_Decorator_m_resetLabels: Method = Method(name="resetLabels", parameters={})
model_Decorator_m_getLabelsToUpdate: Method = Method(name="getLabelsToUpdate", parameters={Parameter(name='partition'), Parameter(name='max')})
model_Decorator.attributes={model_Decorator_graphDecorated, model_Decorator_progress, model_Decorator_enabled}
model_Decorator.methods={model_Decorator_m_resetLabels, model_Decorator_m_updateLabels, model_Decorator_m_prepare, model_Decorator_m_getLabelsToUpdate, model_Decorator_m_decorateGraph}

# model_DynamicLabel class attributes and methods

# model_Graph class attributes and methods

# model_EdgeDecorator class attributes and methods

# Decorator class attributes and methods

# Identifiable class attributes and methods

# model_NodeDecorator class attributes and methods

# model_GraphDecorator class attributes and methods

# model_Model class attributes and methods
model_Model_m_getCanonicalGraph: Method = Method(name="getCanonicalGraph", parameters={Parameter(name='uri'), Parameter(name='time'), Parameter(name='filter')}, type=StringType)
model_Model_m_prepare: Method = Method(name="prepare", parameters={Parameter(name='time')})
model_Model.methods={model_Model_m_getCanonicalGraph, model_Model_m_prepare}

# model_STEMTime class attributes and methods
model_STEMTime_time: Property = Property(name="time", type=DateType)
model_STEMTime_m_addIncrement: Method = Method(name="addIncrement", parameters={Parameter(name='timeIncrement')}, type=StringType)
model_STEMTime_m_hashCode: Method = Method(name="hashCode", parameters={}, type=IntegerType)
model_STEMTime_m_equals: Method = Method(name="equals", parameters={Parameter(name='obj')}, type=BooleanType)
model_STEMTime.attributes={model_STEMTime_time}
model_STEMTime.methods={model_STEMTime_m_addIncrement, model_STEMTime_m_equals, model_STEMTime_m_hashCode}

# model_Comparable class attributes and methods

# Relationships
labelsToUpdate0: BinaryAssociation = BinaryAssociation(
    name="labelsToUpdate0",
    ends={
        Property(name="graph.ecoreDynamicLabel", type=model_Decorator, multiplicity=Multiplicity(1, 1)),
        Property(name="decorator", type=model_DynamicLabel, multiplicity=Multiplicity(0, 9999))
    }
)
graph1: BinaryAssociation = BinaryAssociation(
    name="graph1",
    ends={
        Property(name="graph.ecoreGraph", type=model_Decorator, multiplicity=Multiplicity(1, 1)),
        Property(name="decorators", type=model_Graph, multiplicity=Multiplicity(0, 1))
    }
)
models3: BinaryAssociation = BinaryAssociation(
    name="models3",
    ends={
        Property(name="model_Model", type=model_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Model2", type=model_Model, multiplicity=Multiplicity(0, 9999))
    }
)
graphs4: BinaryAssociation = BinaryAssociation(
    name="graphs4",
    ends={
        Property(name="model_Graph", type=model_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Model5", type=model_Graph, multiplicity=Multiplicity(0, 9999))
    }
)
graphDecorators6: BinaryAssociation = BinaryAssociation(
    name="graphDecorators6",
    ends={
        Property(name="model_GraphDecorator", type=model_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Model7", type=model_GraphDecorator, multiplicity=Multiplicity(0, 9999))
    }
)
nodeDecorators8: BinaryAssociation = BinaryAssociation(
    name="nodeDecorators8",
    ends={
        Property(name="model_NodeDecorator", type=model_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Model9", type=model_NodeDecorator, multiplicity=Multiplicity(0, 9999))
    }
)
edgeDecorators10: BinaryAssociation = BinaryAssociation(
    name="edgeDecorators10",
    ends={
        Property(name="model_EdgeDecorator", type=model_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Model11", type=model_EdgeDecorator, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_model_EdgeDecorator_Decorator = Generalization(general=Decorator, specific=model_EdgeDecorator)
gen_model_Decorator_Identifiable = Generalization(general=Identifiable, specific=model_Decorator)
gen_model_GraphDecorator_Decorator = Generalization(general=Decorator, specific=model_GraphDecorator)
gen_model_Model_Identifiable = Generalization(general=Identifiable, specific=model_Model)
gen_model_NodeDecorator_Decorator = Generalization(general=Decorator, specific=model_NodeDecorator)

# Domain Model
domain_model = DomainModel(
    name="model",
    types={model_Decorator, model_DynamicLabel, model_Graph, model_EdgeDecorator, Decorator, Identifiable, model_NodeDecorator, model_GraphDecorator, model_Model, model_STEMTime, model_Comparable},
    associations={labelsToUpdate0, graph1, models3, graphs4, graphDecorators6, nodeDecorators8, edgeDecorators10},
    generalizations={gen_model_EdgeDecorator_Decorator, gen_model_Decorator_Identifiable, gen_model_GraphDecorator_Decorator, gen_model_Model_Identifiable, gen_model_NodeDecorator_Decorator},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)