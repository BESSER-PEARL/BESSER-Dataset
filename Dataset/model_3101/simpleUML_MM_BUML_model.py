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
simpleUML_MM_PrimitiveDataType = Class(name="simpleUML::MM::PrimitiveDataType")
simpleUML_MM_ClassModel = Class(name="simpleUML::MM::ClassModel")
simpleUML_MM_Classifier = Class(name="simpleUML::MM::Classifier", is_abstract=True)
simpleUML_MM_Association = Class(name="simpleUML::MM::Association")
simpleUML_MM_Class = Class(name="simpleUML::MM::Class")
simpleUML_MM_Attribute = Class(name="simpleUML::MM::Attribute")
Classifier = Class(name="Classifier")

# simpleUML_MM_PrimitiveDataType class attributes and methods

# simpleUML_MM_ClassModel class attributes and methods

# simpleUML_MM_Classifier class attributes and methods
simpleUML_MM_Classifier_name: Property = Property(name="name", type=StringType)
simpleUML_MM_Classifier.attributes={simpleUML_MM_Classifier_name}

# simpleUML_MM_Association class attributes and methods
simpleUML_MM_Association_name: Property = Property(name="name", type=StringType)
simpleUML_MM_Association.attributes={simpleUML_MM_Association_name}

# simpleUML_MM_Class class attributes and methods
simpleUML_MM_Class_is_persistent: Property = Property(name="is_persistent", type=BooleanType)
simpleUML_MM_Class.attributes={simpleUML_MM_Class_is_persistent}

# simpleUML_MM_Attribute class attributes and methods
simpleUML_MM_Attribute_name: Property = Property(name="name", type=StringType)
simpleUML_MM_Attribute_is_primary: Property = Property(name="is_primary", type=BooleanType)
simpleUML_MM_Attribute.attributes={simpleUML_MM_Attribute_is_primary, simpleUML_MM_Attribute_name}

# Classifier class attributes and methods

# Relationships
attrs5: BinaryAssociation = BinaryAssociation(
    name="attrs5",
    ends={
        Property(name="simpleUML_MM_Attribute7", type=simpleUML_MM_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="simpleUML_MM_Class6", type=simpleUML_MM_Attribute, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
parent9: BinaryAssociation = BinaryAssociation(
    name="parent9",
    ends={
        Property(name="simpleUML_MM_Class10", type=simpleUML_MM_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="simpleUML_MM_Class8", type=simpleUML_MM_Class, multiplicity=Multiplicity(0, 1))
    }
)
classifier11: BinaryAssociation = BinaryAssociation(
    name="classifier11",
    ends={
        Property(name="simpleUML_MM_Classifier12", type=simpleUML_MM_ClassModel, multiplicity=Multiplicity(1, 1)),
        Property(name="simpleUML_MM_ClassModel", type=simpleUML_MM_Classifier, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
src0: BinaryAssociation = BinaryAssociation(
    name="src0",
    ends={
        Property(name="simpleUML_MM_Class", type=simpleUML_MM_Association, multiplicity=Multiplicity(1, 1)),
        Property(name="simpleUML_MM_Association", type=simpleUML_MM_Class, multiplicity=Multiplicity(1, 1))
    }
)
dest1: BinaryAssociation = BinaryAssociation(
    name="dest1",
    ends={
        Property(name="simpleUML_MM_Class3", type=simpleUML_MM_Association, multiplicity=Multiplicity(1, 1)),
        Property(name="simpleUML_MM_Association2", type=simpleUML_MM_Class, multiplicity=Multiplicity(1, 1))
    }
)
type4: BinaryAssociation = BinaryAssociation(
    name="type4",
    ends={
        Property(name="simpleUML_MM_Classifier", type=simpleUML_MM_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="simpleUML_MM_Attribute", type=simpleUML_MM_Classifier, multiplicity=Multiplicity(1, 1))
    }
)
association13: BinaryAssociation = BinaryAssociation(
    name="association13",
    ends={
        Property(name="simpleUML_MM_Association15", type=simpleUML_MM_ClassModel, multiplicity=Multiplicity(1, 1)),
        Property(name="simpleUML_MM_ClassModel14", type=simpleUML_MM_Association, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_simpleUML_MM_PrimitiveDataType_Classifier = Generalization(general=Classifier, specific=simpleUML_MM_PrimitiveDataType)
gen_simpleUML_MM_Class_Classifier = Generalization(general=Classifier, specific=simpleUML_MM_Class)

# Domain Model
domain_model = DomainModel(
    name="simpleUML_MM",
    types={simpleUML_MM_PrimitiveDataType, simpleUML_MM_ClassModel, simpleUML_MM_Classifier, simpleUML_MM_Association, simpleUML_MM_Class, simpleUML_MM_Attribute, Classifier},
    associations={attrs5, parent9, classifier11, src0, dest1, type4, association13},
    generalizations={gen_simpleUML_MM_PrimitiveDataType_Classifier, gen_simpleUML_MM_Class_Classifier},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)