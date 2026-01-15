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
testmodel_cont = Class(name="testmodel::cont")
testmodel_Node = Class(name="testmodel::Node")
testmodel_Val = Class(name="testmodel::Val")

# testmodel_cont class attributes and methods

# testmodel_Node class attributes and methods
testmodel_Node_nodename: Property = Property(name="nodename", type=StringType)
testmodel_Node.attributes={testmodel_Node_nodename}

# testmodel_Val class attributes and methods
testmodel_Val_intvl: Property = Property(name="intvl", type=IntegerType)
testmodel_Val_valname: Property = Property(name="valname", type=StringType)
testmodel_Val_intlist: Property = Property(name="intlist", type=IntegerType)
testmodel_Val.attributes={testmodel_Val_valname, testmodel_Val_intlist, testmodel_Val_intvl}

# Relationships
containsNode0: BinaryAssociation = BinaryAssociation(
    name="containsNode0",
    ends={
        Property(name="testmodel_Node", type=testmodel_cont, multiplicity=Multiplicity(1, 1)),
        Property(name="testmodel_cont", type=testmodel_Node, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
childNodes9: BinaryAssociation = BinaryAssociation(
    name="childNodes9",
    ends={
        Property(name="Node10", type=testmodel_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="parentNode", type=testmodel_Node, multiplicity=Multiplicity(0, 9999))
    }
)
containsVal1: BinaryAssociation = BinaryAssociation(
    name="containsVal1",
    ends={
        Property(name="testmodel_Val", type=testmodel_cont, multiplicity=Multiplicity(1, 1)),
        Property(name="testmodel_cont2", type=testmodel_Val, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
hasVals3: BinaryAssociation = BinaryAssociation(
    name="hasVals3",
    ends={
        Property(name="testmodel_Val5", type=testmodel_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="testmodel_Node4", type=testmodel_Val, multiplicity=Multiplicity(0, 9999))
    }
)
parentNode7: BinaryAssociation = BinaryAssociation(
    name="parentNode7",
    ends={
        Property(name="Node", type=testmodel_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="childNodes", type=testmodel_Node, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="testmodel",
    types={testmodel_cont, testmodel_Node, testmodel_Val},
    associations={containsNode0, childNodes9, containsVal1, hasVals3, parentNode7},
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