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
simpleClass_Model = Class(name="simpleClass::Model")
simpleClass_Class = Class(name="simpleClass::Class")
simpleClass_Attribute = Class(name="simpleClass::Attribute")

# simpleClass_Model class attributes and methods

# simpleClass_Class class attributes and methods
simpleClass_Class_name: Property = Property(name="name", type=StringType)
simpleClass_Class.attributes={simpleClass_Class_name}

# simpleClass_Attribute class attributes and methods
simpleClass_Attribute_isPublic: Property = Property(name="isPublic", type=BooleanType)
simpleClass_Attribute_name: Property = Property(name="name", type=StringType)
simpleClass_Attribute.attributes={simpleClass_Attribute_name, simpleClass_Attribute_isPublic}

# Relationships
classes0: BinaryAssociation = BinaryAssociation(
    name="classes0",
    ends={
        Property(name="simpleClass_Class", type=simpleClass_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="simpleClass_Model", type=simpleClass_Class, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
superclasses2: BinaryAssociation = BinaryAssociation(
    name="superclasses2",
    ends={
        Property(name="simpleClass_Class3", type=simpleClass_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="simpleClass_Class1", type=simpleClass_Class, multiplicity=Multiplicity(0, 9999))
    }
)
attributes4: BinaryAssociation = BinaryAssociation(
    name="attributes4",
    ends={
        Property(name="simpleClass_Attribute", type=simpleClass_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="simpleClass_Class5", type=simpleClass_Attribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type6: BinaryAssociation = BinaryAssociation(
    name="type6",
    ends={
        Property(name="simpleClass_Class8", type=simpleClass_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="simpleClass_Attribute7", type=simpleClass_Class, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="simpleClass",
    types={simpleClass_Model, simpleClass_Class, simpleClass_Attribute},
    associations={classes0, superclasses2, attributes4, type6},
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