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
softwaretraces_Model = Class(name="softwaretraces::Model")
MyNode = Class(name="MyNode")
softwaretraces_MyNode = Class(name="softwaretraces::MyNode", is_abstract=True)
softwaretraces_Feature = Class(name="softwaretraces::Feature")
softwaretraces_Trace = Class(name="softwaretraces::Trace")

# softwaretraces_Model class attributes and methods
softwaretraces_Model_resourceFileName: Property = Property(name="resourceFileName", type=StringType)
softwaretraces_Model.attributes={softwaretraces_Model_resourceFileName}

# MyNode class attributes and methods

# softwaretraces_MyNode class attributes and methods

# softwaretraces_Feature class attributes and methods
softwaretraces_Feature_name: Property = Property(name="name", type=StringType)
softwaretraces_Feature.attributes={softwaretraces_Feature_name}

# softwaretraces_Trace class attributes and methods
softwaretraces_Trace_projectName: Property = Property(name="projectName", type=StringType)
softwaretraces_Trace_fileName: Property = Property(name="fileName", type=StringType)
softwaretraces_Trace_lineNumber: Property = Property(name="lineNumber", type=IntegerType)
softwaretraces_Trace.attributes={softwaretraces_Trace_projectName, softwaretraces_Trace_fileName, softwaretraces_Trace_lineNumber}

# Relationships
features0: BinaryAssociation = BinaryAssociation(
    name="features0",
    ends={
        Property(name="softwaretraces_Feature", type=softwaretraces_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="softwaretraces_Model", type=softwaretraces_Feature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
traces1: BinaryAssociation = BinaryAssociation(
    name="traces1",
    ends={
        Property(name="softwaretraces_Trace", type=softwaretraces_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="softwaretraces_Model2", type=softwaretraces_Trace, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
features4: BinaryAssociation = BinaryAssociation(
    name="features4",
    ends={
        Property(name="softwaretraces_Feature5", type=softwaretraces_Feature, multiplicity=Multiplicity(1, 1)),
        Property(name="softwaretraces_Feature3", type=softwaretraces_Feature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
traces6: BinaryAssociation = BinaryAssociation(
    name="traces6",
    ends={
        Property(name="softwaretraces_Trace8", type=softwaretraces_Feature, multiplicity=Multiplicity(1, 1)),
        Property(name="softwaretraces_Feature7", type=softwaretraces_Trace, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
traces10: BinaryAssociation = BinaryAssociation(
    name="traces10",
    ends={
        Property(name="softwaretraces_Trace11", type=softwaretraces_Trace, multiplicity=Multiplicity(1, 1)),
        Property(name="softwaretraces_Trace9", type=softwaretraces_Trace, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_softwaretraces_Model_MyNode = Generalization(general=MyNode, specific=softwaretraces_Model)
gen_softwaretraces_Feature_MyNode = Generalization(general=MyNode, specific=softwaretraces_Feature)
gen_softwaretraces_Trace_MyNode = Generalization(general=MyNode, specific=softwaretraces_Trace)

# Domain Model
domain_model = DomainModel(
    name="softwaretraces",
    types={softwaretraces_Model, MyNode, softwaretraces_MyNode, softwaretraces_Feature, softwaretraces_Trace},
    associations={features0, traces1, features4, traces6, traces10},
    generalizations={gen_softwaretraces_Model_MyNode, gen_softwaretraces_Feature_MyNode, gen_softwaretraces_Trace_MyNode},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)