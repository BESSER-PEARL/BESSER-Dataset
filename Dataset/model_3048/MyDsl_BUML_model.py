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

# Enumerations
Type: Enumeration = Enumeration(
    name="Type",
    literals={
            EnumerationLiteral(name="string"),
			EnumerationLiteral(name="int")
    }
)

# Classes
myDsl_Model = Class(name="myDsl::Model")
myDsl_Entity = Class(name="myDsl::Entity")
myDsl_Feature = Class(name="myDsl::Feature")
myDsl_Attribute = Class(name="myDsl::Attribute")
Feature = Class(name="Feature")
myDsl_Reference = Class(name="myDsl::Reference")

# myDsl_Model class attributes and methods

# myDsl_Entity class attributes and methods
myDsl_Entity_name: Property = Property(name="name", type=StringType)
myDsl_Entity.attributes={myDsl_Entity_name}

# myDsl_Feature class attributes and methods
myDsl_Feature_name: Property = Property(name="name", type=StringType)
myDsl_Feature.attributes={myDsl_Feature_name}

# myDsl_Attribute class attributes and methods
myDsl_Attribute_type: Property = Property(name="type", type=StringType)
myDsl_Attribute.attributes={myDsl_Attribute_type}

# Feature class attributes and methods

# myDsl_Reference class attributes and methods

# Relationships
entities0: BinaryAssociation = BinaryAssociation(
    name="entities0",
    ends={
        Property(name="myDsl_Entity", type=myDsl_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Model", type=myDsl_Entity, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
features1: BinaryAssociation = BinaryAssociation(
    name="features1",
    ends={
        Property(name="myDsl_Feature", type=myDsl_Entity, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Entity2", type=myDsl_Feature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type3: BinaryAssociation = BinaryAssociation(
    name="type3",
    ends={
        Property(name="myDsl_Entity4", type=myDsl_Reference, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Reference", type=myDsl_Entity, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_myDsl_Attribute_Feature = Generalization(general=Feature, specific=myDsl_Attribute)
gen_myDsl_Reference_Feature = Generalization(general=Feature, specific=myDsl_Reference)

# Domain Model
domain_model = DomainModel(
    name="myDsl",
    types={myDsl_Model, myDsl_Entity, myDsl_Feature, myDsl_Attribute, Feature, myDsl_Reference, Type},
    associations={entities0, features1, type3},
    generalizations={gen_myDsl_Attribute_Feature, gen_myDsl_Reference_Feature},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)