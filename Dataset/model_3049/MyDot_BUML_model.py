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
DataType: Enumeration = Enumeration(
    name="DataType",
    literals={
            EnumerationLiteral(name="string"),
			EnumerationLiteral(name="int")
    }
)

# Classes
myDot_Model = Class(name="myDot::Model")
myDot_Entity = Class(name="myDot::Entity")
myDot_Usage = Class(name="myDot::Usage")
myDot_Feature = Class(name="myDot::Feature")
myDot_Attribute = Class(name="myDot::Attribute")
Feature = Class(name="Feature")
myDot_Reference = Class(name="myDot::Reference")
myDot_Ref = Class(name="myDot::Ref")
myDot_DotExpression = Class(name="myDot::DotExpression")
Ref = Class(name="Ref")
myDot_EntityRef = Class(name="myDot::EntityRef")

# myDot_Model class attributes and methods

# myDot_Entity class attributes and methods
myDot_Entity_name: Property = Property(name="name", type=StringType)
myDot_Entity.attributes={myDot_Entity_name}

# myDot_Usage class attributes and methods

# myDot_Feature class attributes and methods
myDot_Feature_name: Property = Property(name="name", type=StringType)
myDot_Feature.attributes={myDot_Feature_name}

# myDot_Attribute class attributes and methods
myDot_Attribute_type: Property = Property(name="type", type=StringType)
myDot_Attribute.attributes={myDot_Attribute_type}

# Feature class attributes and methods

# myDot_Reference class attributes and methods

# myDot_Ref class attributes and methods

# myDot_DotExpression class attributes and methods

# Ref class attributes and methods

# myDot_EntityRef class attributes and methods

# Relationships
usages1: BinaryAssociation = BinaryAssociation(
    name="usages1",
    ends={
        Property(name="myDot_Usage", type=myDot_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="myDot_Model2", type=myDot_Usage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
entities0: BinaryAssociation = BinaryAssociation(
    name="entities0",
    ends={
        Property(name="myDot_Entity", type=myDot_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="myDot_Model", type=myDot_Entity, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ref9: BinaryAssociation = BinaryAssociation(
    name="ref9",
    ends={
        Property(name="myDot_Ref10", type=myDot_DotExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="myDot_DotExpression", type=myDot_Ref, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
tail11: BinaryAssociation = BinaryAssociation(
    name="tail11",
    ends={
        Property(name="myDot_Feature13", type=myDot_DotExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="myDot_DotExpression12", type=myDot_Feature, multiplicity=Multiplicity(0, 1))
    }
)
features3: BinaryAssociation = BinaryAssociation(
    name="features3",
    ends={
        Property(name="myDot_Feature", type=myDot_Entity, multiplicity=Multiplicity(1, 1)),
        Property(name="myDot_Entity4", type=myDot_Feature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type5: BinaryAssociation = BinaryAssociation(
    name="type5",
    ends={
        Property(name="myDot_Entity6", type=myDot_Reference, multiplicity=Multiplicity(1, 1)),
        Property(name="myDot_Reference", type=myDot_Entity, multiplicity=Multiplicity(0, 1))
    }
)
ref7: BinaryAssociation = BinaryAssociation(
    name="ref7",
    ends={
        Property(name="myDot_Ref", type=myDot_Usage, multiplicity=Multiplicity(1, 1)),
        Property(name="myDot_Usage8", type=myDot_Ref, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
entity14: BinaryAssociation = BinaryAssociation(
    name="entity14",
    ends={
        Property(name="myDot_Entity15", type=myDot_EntityRef, multiplicity=Multiplicity(1, 1)),
        Property(name="myDot_EntityRef", type=myDot_Entity, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_myDot_Attribute_Feature = Generalization(general=Feature, specific=myDot_Attribute)
gen_myDot_Reference_Feature = Generalization(general=Feature, specific=myDot_Reference)
gen_myDot_DotExpression_Ref = Generalization(general=Ref, specific=myDot_DotExpression)
gen_myDot_EntityRef_Ref = Generalization(general=Ref, specific=myDot_EntityRef)

# Domain Model
domain_model = DomainModel(
    name="myDot",
    types={myDot_Model, myDot_Entity, myDot_Usage, myDot_Feature, myDot_Attribute, Feature, myDot_Reference, myDot_Ref, myDot_DotExpression, Ref, myDot_EntityRef, DataType},
    associations={usages1, entities0, ref9, tail11, features3, type5, ref7, entity14},
    generalizations={gen_myDot_Attribute_Feature, gen_myDot_Reference_Feature, gen_myDot_DotExpression_Ref, gen_myDot_EntityRef_Ref},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)