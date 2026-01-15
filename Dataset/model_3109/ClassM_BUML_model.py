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
ClassM_Class = Class(name="ClassM::Class")
Classifier = Class(name="Classifier")
ClassM_Attribute = Class(name="ClassM::Attribute")
ClassM_Classifier = Class(name="ClassM::Classifier")
ClassM_PrimitiveType = Class(name="ClassM::PrimitiveType")
ClassM_Model = Class(name="ClassM::Model")

# ClassM_Class class attributes and methods

# Classifier class attributes and methods

# ClassM_Attribute class attributes and methods
ClassM_Attribute_name: Property = Property(name="name", type=StringType)
ClassM_Attribute_is_primary: Property = Property(name="is_primary", type=BooleanType)
ClassM_Attribute.attributes={ClassM_Attribute_is_primary, ClassM_Attribute_name}

# ClassM_Classifier class attributes and methods
ClassM_Classifier_name: Property = Property(name="name", type=StringType)
ClassM_Classifier.attributes={ClassM_Classifier_name}

# ClassM_PrimitiveType class attributes and methods

# ClassM_Model class attributes and methods

# Relationships
attrs0: BinaryAssociation = BinaryAssociation(
    name="attrs0",
    ends={
        Property(name="Attribute", type=ClassM_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="owner", type=ClassM_Attribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type1: BinaryAssociation = BinaryAssociation(
    name="type1",
    ends={
        Property(name="ClassM_Classifier", type=ClassM_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="ClassM_Attribute", type=ClassM_Classifier, multiplicity=Multiplicity(0, 1))
    }
)
owner2: BinaryAssociation = BinaryAssociation(
    name="owner2",
    ends={
        Property(name="Class", type=ClassM_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="attrs", type=ClassM_Class, multiplicity=Multiplicity(0, 1))
    }
)
classifiers3: BinaryAssociation = BinaryAssociation(
    name="classifiers3",
    ends={
        Property(name="ClassM_Classifier4", type=ClassM_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="ClassM_Model", type=ClassM_Classifier, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_ClassM_Class_Classifier = Generalization(general=Classifier, specific=ClassM_Class)
gen_ClassM_PrimitiveType_Classifier = Generalization(general=Classifier, specific=ClassM_PrimitiveType)

# Domain Model
domain_model = DomainModel(
    name="ClassM",
    types={ClassM_Class, Classifier, ClassM_Attribute, ClassM_Classifier, ClassM_PrimitiveType, ClassM_Model},
    associations={attrs0, type1, owner2, classifiers3},
    generalizations={gen_ClassM_Class_Classifier, gen_ClassM_PrimitiveType_Classifier},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)