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
dft_GalileoFaultTreeNode = Class(name="dft::GalileoFaultTreeNode")
dft_GalileoDft = Class(name="dft::GalileoDft")
dft_Named = Class(name="dft::Named")
GalileoNodeType = Class(name="GalileoNodeType")
dft_Observer = Class(name="dft::Observer")
dft_Parametrized = Class(name="dft::Parametrized")
dft_GalileoNodeType = Class(name="dft::GalileoNodeType")

# dft_GalileoFaultTreeNode class attributes and methods
dft_GalileoFaultTreeNode_name: Property = Property(name="name", type=StringType)
dft_GalileoFaultTreeNode_lambda: Property = Property(name="lambda", type=StringType)
dft_GalileoFaultTreeNode_dorm: Property = Property(name="dorm", type=StringType)
dft_GalileoFaultTreeNode_repair: Property = Property(name="repair", type=StringType)
dft_GalileoFaultTreeNode.attributes={dft_GalileoFaultTreeNode_name, dft_GalileoFaultTreeNode_lambda, dft_GalileoFaultTreeNode_repair, dft_GalileoFaultTreeNode_dorm}

# dft_GalileoDft class attributes and methods

# dft_Named class attributes and methods
dft_Named_typeName: Property = Property(name="typeName", type=StringType)
dft_Named.attributes={dft_Named_typeName}

# GalileoNodeType class attributes and methods

# dft_Observer class attributes and methods
dft_Observer_observationRate: Property = Property(name="observationRate", type=StringType)
dft_Observer.attributes={dft_Observer_observationRate}

# dft_Parametrized class attributes and methods
dft_Parametrized_typeName: Property = Property(name="typeName", type=StringType)
dft_Parametrized_parameter: Property = Property(name="parameter", type=StringType)
dft_Parametrized.attributes={dft_Parametrized_parameter, dft_Parametrized_typeName}

# dft_GalileoNodeType class attributes and methods

# Relationships
root0: BinaryAssociation = BinaryAssociation(
    name="root0",
    ends={
        Property(name="dft_GalileoFaultTreeNode", type=dft_GalileoDft, multiplicity=Multiplicity(1, 1)),
        Property(name="dft_GalileoDft", type=dft_GalileoFaultTreeNode, multiplicity=Multiplicity(0, 1))
    }
)
gates1: BinaryAssociation = BinaryAssociation(
    name="gates1",
    ends={
        Property(name="dft_GalileoFaultTreeNode3", type=dft_GalileoDft, multiplicity=Multiplicity(1, 1)),
        Property(name="dft_GalileoDft2", type=dft_GalileoFaultTreeNode, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
basicEvents4: BinaryAssociation = BinaryAssociation(
    name="basicEvents4",
    ends={
        Property(name="dft_GalileoFaultTreeNode6", type=dft_GalileoDft, multiplicity=Multiplicity(1, 1)),
        Property(name="dft_GalileoDft5", type=dft_GalileoFaultTreeNode, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
observables12: BinaryAssociation = BinaryAssociation(
    name="observables12",
    ends={
        Property(name="dft_GalileoFaultTreeNode13", type=dft_Observer, multiplicity=Multiplicity(1, 1)),
        Property(name="dft_Observer", type=dft_GalileoFaultTreeNode, multiplicity=Multiplicity(0, 9999))
    }
)
type7: BinaryAssociation = BinaryAssociation(
    name="type7",
    ends={
        Property(name="dft_GalileoNodeType", type=dft_GalileoFaultTreeNode, multiplicity=Multiplicity(1, 1)),
        Property(name="dft_GalileoFaultTreeNode8", type=dft_GalileoNodeType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
children10: BinaryAssociation = BinaryAssociation(
    name="children10",
    ends={
        Property(name="dft_GalileoFaultTreeNode11", type=dft_GalileoFaultTreeNode, multiplicity=Multiplicity(1, 1)),
        Property(name="dft_GalileoFaultTreeNode9", type=dft_GalileoFaultTreeNode, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_dft_Named_GalileoNodeType = Generalization(general=GalileoNodeType, specific=dft_Named)
gen_dft_Observer_GalileoNodeType = Generalization(general=GalileoNodeType, specific=dft_Observer)
gen_dft_Parametrized_GalileoNodeType = Generalization(general=GalileoNodeType, specific=dft_Parametrized)

# Domain Model
domain_model = DomainModel(
    name="dft",
    types={dft_GalileoFaultTreeNode, dft_GalileoDft, dft_Named, GalileoNodeType, dft_Observer, dft_Parametrized, dft_GalileoNodeType},
    associations={root0, gates1, basicEvents4, observables12, type7, children10},
    generalizations={gen_dft_Named_GalileoNodeType, gen_dft_Observer_GalileoNodeType, gen_dft_Parametrized_GalileoNodeType},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)