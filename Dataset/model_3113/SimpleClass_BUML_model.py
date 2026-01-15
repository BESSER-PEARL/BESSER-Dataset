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
simpleClass_ClassModel = Class(name="simpleClass::ClassModel")
simpleClass_Association = Class(name="simpleClass::Association")
simpleClass_Class = Class(name="simpleClass::Class")
simpleClass_Classifier = Class(name="simpleClass::Classifier", is_abstract=True)
simpleClass_Attribute = Class(name="simpleClass::Attribute")
simpleClass_PrimitiveDataType = Class(name="simpleClass::PrimitiveDataType")
Classifier = Class(name="Classifier")

# simpleClass_ClassModel class attributes and methods

# simpleClass_Association class attributes and methods
simpleClass_Association_name: Property = Property(name="name", type=StringType)
simpleClass_Association.attributes={simpleClass_Association_name}

# simpleClass_Class class attributes and methods
simpleClass_Class_persistent: Property = Property(name="persistent", type=BooleanType)
simpleClass_Class.attributes={simpleClass_Class_persistent}

# simpleClass_Classifier class attributes and methods
simpleClass_Classifier_name: Property = Property(name="name", type=StringType)
simpleClass_Classifier.attributes={simpleClass_Classifier_name}

# simpleClass_Attribute class attributes and methods
simpleClass_Attribute_name: Property = Property(name="name", type=StringType)
simpleClass_Attribute_id: Property = Property(name="id", type=BooleanType)
simpleClass_Attribute.attributes={simpleClass_Attribute_id, simpleClass_Attribute_name}

# simpleClass_PrimitiveDataType class attributes and methods

# Classifier class attributes and methods

# Relationships
classifiers0: BinaryAssociation = BinaryAssociation(
    name="classifiers0",
    ends={
        Property(name="simpleClass_Classifier", type=simpleClass_ClassModel, multiplicity=Multiplicity(1, 1)),
        Property(name="simpleClass_ClassModel", type=simpleClass_Classifier, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
associations1: BinaryAssociation = BinaryAssociation(
    name="associations1",
    ends={
        Property(name="simpleClass_Association", type=simpleClass_ClassModel, multiplicity=Multiplicity(1, 1)),
        Property(name="simpleClass_ClassModel2", type=simpleClass_Association, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
source3: BinaryAssociation = BinaryAssociation(
    name="source3",
    ends={
        Property(name="simpleClass_Class", type=simpleClass_Association, multiplicity=Multiplicity(1, 1)),
        Property(name="simpleClass_Association4", type=simpleClass_Class, multiplicity=Multiplicity(1, 1))
    }
)
target5: BinaryAssociation = BinaryAssociation(
    name="target5",
    ends={
        Property(name="simpleClass_Class7", type=simpleClass_Association, multiplicity=Multiplicity(1, 1)),
        Property(name="simpleClass_Association6", type=simpleClass_Class, multiplicity=Multiplicity(1, 1))
    }
)
super9: BinaryAssociation = BinaryAssociation(
    name="super9",
    ends={
        Property(name="simpleClass_Class10", type=simpleClass_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="simpleClass_Class8", type=simpleClass_Class, multiplicity=Multiplicity(0, 1))
    }
)
attributes11: BinaryAssociation = BinaryAssociation(
    name="attributes11",
    ends={
        Property(name="simpleClass_Attribute", type=simpleClass_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="simpleClass_Class12", type=simpleClass_Attribute, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
type13: BinaryAssociation = BinaryAssociation(
    name="type13",
    ends={
        Property(name="simpleClass_Classifier15", type=simpleClass_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="simpleClass_Attribute14", type=simpleClass_Classifier, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_simpleClass_PrimitiveDataType_Classifier = Generalization(general=Classifier, specific=simpleClass_PrimitiveDataType)
gen_simpleClass_Class_Classifier = Generalization(general=Classifier, specific=simpleClass_Class)

# Domain Model
domain_model = DomainModel(
    name="simpleClass",
    types={simpleClass_ClassModel, simpleClass_Association, simpleClass_Class, simpleClass_Classifier, simpleClass_Attribute, simpleClass_PrimitiveDataType, Classifier},
    associations={classifiers0, associations1, source3, target5, super9, attributes11, type13},
    generalizations={gen_simpleClass_PrimitiveDataType_Classifier, gen_simpleClass_Class_Classifier},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)