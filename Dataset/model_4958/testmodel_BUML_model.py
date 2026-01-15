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
testmodel_Model = Class(name="testmodel::Model")
testmodel_ModelElement = Class(name="testmodel::ModelElement", is_abstract=True)
testmodel_NamedElement = Class(name="testmodel::NamedElement", is_abstract=True)
NamedElement = Class(name="NamedElement")
testmodel_TypedElement = Class(name="testmodel::TypedElement")
testmodel_Class = Class(name="testmodel::Class")
ModelElement = Class(name="ModelElement")
testmodel_Attribute = Class(name="testmodel::Attribute")
TypedElement = Class(name="TypedElement")
testmodel_Group = Class(name="testmodel::Group")
Model = Class(name="Model")
testmodel_Association = Class(name="testmodel::Association")

# testmodel_Model class attributes and methods

# testmodel_ModelElement class attributes and methods

# testmodel_NamedElement class attributes and methods
testmodel_NamedElement_name: Property = Property(name="name", type=StringType)
testmodel_NamedElement.attributes={testmodel_NamedElement_name}

# NamedElement class attributes and methods

# testmodel_TypedElement class attributes and methods

# testmodel_Class class attributes and methods

# ModelElement class attributes and methods

# testmodel_Attribute class attributes and methods

# TypedElement class attributes and methods

# testmodel_Group class attributes and methods

# Model class attributes and methods

# testmodel_Association class attributes and methods
testmodel_Association_firstLabel: Property = Property(name="firstLabel", type=StringType)
testmodel_Association_secondLabel: Property = Property(name="secondLabel", type=StringType)
testmodel_Association.attributes={testmodel_Association_firstLabel, testmodel_Association_secondLabel}

# Relationships
elements0: BinaryAssociation = BinaryAssociation(
    name="elements0",
    ends={
        Property(name="testmodel_ModelElement", type=testmodel_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="testmodel_Model", type=testmodel_ModelElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type1: BinaryAssociation = BinaryAssociation(
    name="type1",
    ends={
        Property(name="testmodel_Class", type=testmodel_TypedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="testmodel_TypedElement", type=testmodel_Class, multiplicity=Multiplicity(1, 1))
    }
)
attributes2: BinaryAssociation = BinaryAssociation(
    name="attributes2",
    ends={
        Property(name="Attribute", type=testmodel_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="owner", type=testmodel_Attribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
owner3: BinaryAssociation = BinaryAssociation(
    name="owner3",
    ends={
        Property(name="Class", type=testmodel_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="attributes", type=testmodel_Class, multiplicity=Multiplicity(1, 1))
    }
)
first4: BinaryAssociation = BinaryAssociation(
    name="first4",
    ends={
        Property(name="testmodel_Class5", type=testmodel_Association, multiplicity=Multiplicity(1, 1)),
        Property(name="testmodel_Association", type=testmodel_Class, multiplicity=Multiplicity(1, 1))
    }
)
second6: BinaryAssociation = BinaryAssociation(
    name="second6",
    ends={
        Property(name="testmodel_Class8", type=testmodel_Association, multiplicity=Multiplicity(1, 1)),
        Property(name="testmodel_Association7", type=testmodel_Class, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_testmodel_ModelElement_NamedElement = Generalization(general=NamedElement, specific=testmodel_ModelElement)
gen_testmodel_TypedElement_NamedElement = Generalization(general=NamedElement, specific=testmodel_TypedElement)
gen_testmodel_Class_ModelElement = Generalization(general=ModelElement, specific=testmodel_Class)
gen_testmodel_Attribute_TypedElement = Generalization(general=TypedElement, specific=testmodel_Attribute)
gen_testmodel_Group_ModelElement = Generalization(general=ModelElement, specific=testmodel_Group)
gen_testmodel_Group_Model = Generalization(general=Model, specific=testmodel_Group)
gen_testmodel_Association_ModelElement = Generalization(general=ModelElement, specific=testmodel_Association)

# Domain Model
domain_model = DomainModel(
    name="testmodel",
    types={testmodel_Model, testmodel_ModelElement, testmodel_NamedElement, NamedElement, testmodel_TypedElement, testmodel_Class, ModelElement, testmodel_Attribute, TypedElement, testmodel_Group, Model, testmodel_Association},
    associations={elements0, type1, attributes2, owner3, first4, second6},
    generalizations={gen_testmodel_ModelElement_NamedElement, gen_testmodel_TypedElement_NamedElement, gen_testmodel_Class_ModelElement, gen_testmodel_Attribute_TypedElement, gen_testmodel_Group_ModelElement, gen_testmodel_Group_Model, gen_testmodel_Association_ModelElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)