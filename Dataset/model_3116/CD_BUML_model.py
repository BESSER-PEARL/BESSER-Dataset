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
CD_NamedElt = Class(name="CD::NamedElt", is_abstract=True)
CD_Classifier = Class(name="CD::Classifier", is_abstract=True)
NamedElt = Class(name="NamedElt")
CD_DataType = Class(name="CD::DataType")
Classifier = Class(name="Classifier")
CD_Class = Class(name="CD::Class")
CD_Attribute = Class(name="CD::Attribute")
CD_Package = Class(name="CD::Package")

# CD_NamedElt class attributes and methods
CD_NamedElt_name: Property = Property(name="name", type=StringType)
CD_NamedElt.attributes={CD_NamedElt_name}

# CD_Classifier class attributes and methods

# NamedElt class attributes and methods

# CD_DataType class attributes and methods

# Classifier class attributes and methods

# CD_Class class attributes and methods
CD_Class_isAbstract: Property = Property(name="isAbstract", type=StringType)
CD_Class.attributes={CD_Class_isAbstract}

# CD_Attribute class attributes and methods
CD_Attribute_multiValued: Property = Property(name="multiValued", type=StringType)
CD_Attribute.attributes={CD_Attribute_multiValued}

# CD_Package class attributes and methods

# Relationships
super1: BinaryAssociation = BinaryAssociation(
    name="super1",
    ends={
        Property(name="CD_Class", type=CD_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="CD_Class0", type=CD_Class, multiplicity=Multiplicity(0, 9999))
    }
)
attr2: BinaryAssociation = BinaryAssociation(
    name="attr2",
    ends={
        Property(name="Attribute", type=CD_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="owner", type=CD_Attribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type3: BinaryAssociation = BinaryAssociation(
    name="type3",
    ends={
        Property(name="CD_Classifier", type=CD_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="CD_Attribute", type=CD_Classifier, multiplicity=Multiplicity(1, 1))
    }
)
owner4: BinaryAssociation = BinaryAssociation(
    name="owner4",
    ends={
        Property(name="Class", type=CD_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="attr", type=CD_Class, multiplicity=Multiplicity(1, 1))
    }
)
classifiers5: BinaryAssociation = BinaryAssociation(
    name="classifiers5",
    ends={
        Property(name="CD_Classifier6", type=CD_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="CD_Package", type=CD_Classifier, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_CD_Attribute_NamedElt = Generalization(general=NamedElt, specific=CD_Attribute)
gen_CD_Classifier_NamedElt = Generalization(general=NamedElt, specific=CD_Classifier)
gen_CD_DataType_Classifier = Generalization(general=Classifier, specific=CD_DataType)
gen_CD_Class_Classifier = Generalization(general=Classifier, specific=CD_Class)
gen_CD_Package_Classifier = Generalization(general=Classifier, specific=CD_Package)

# Domain Model
domain_model = DomainModel(
    name="CD",
    types={CD_NamedElt, CD_Classifier, NamedElt, CD_DataType, Classifier, CD_Class, CD_Attribute, CD_Package},
    associations={super1, attr2, type3, owner4, classifiers5},
    generalizations={gen_CD_Attribute_NamedElt, gen_CD_Classifier_NamedElt, gen_CD_DataType_Classifier, gen_CD_Class_Classifier, gen_CD_Package_Classifier},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)