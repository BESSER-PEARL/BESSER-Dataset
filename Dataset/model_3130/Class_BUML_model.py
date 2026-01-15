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
class_NamedElt = Class(name="class::NamedElt", is_abstract=True)
class_Attribute = Class(name="class::Attribute")
class_ClassModel = Class(name="class::ClassModel")
class_Classifier = Class(name="class::Classifier", is_abstract=True)
NamedElt = Class(name="NamedElt")
class_DataType = Class(name="class::DataType")
Classifier = Class(name="Classifier")
class_Class = Class(name="class::Class")

# class_NamedElt class attributes and methods
class_NamedElt_name: Property = Property(name="name", type=StringType)
class_NamedElt.attributes={class_NamedElt_name}

# class_Attribute class attributes and methods
class_Attribute_multiValued: Property = Property(name="multiValued", type=BooleanType)
class_Attribute.attributes={class_Attribute_multiValued}

# class_ClassModel class attributes and methods

# class_Classifier class attributes and methods

# NamedElt class attributes and methods

# class_DataType class attributes and methods

# Classifier class attributes and methods

# class_Class class attributes and methods
class_Class_isAbstract: Property = Property(name="isAbstract", type=BooleanType)
class_Class.attributes={class_Class_isAbstract}

# Relationships
super1: BinaryAssociation = BinaryAssociation(
    name="super1",
    ends={
        Property(name="class_Class", type=class_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="class_Class0", type=class_Class, multiplicity=Multiplicity(0, 9999))
    }
)
attr2: BinaryAssociation = BinaryAssociation(
    name="attr2",
    ends={
        Property(name="Attribute", type=class_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="owner", type=class_Attribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
owner3: BinaryAssociation = BinaryAssociation(
    name="owner3",
    ends={
        Property(name="Class", type=class_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="attr", type=class_Class, multiplicity=Multiplicity(1, 1))
    }
)
type4: BinaryAssociation = BinaryAssociation(
    name="type4",
    ends={
        Property(name="class_Classifier", type=class_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="class_Attribute", type=class_Classifier, multiplicity=Multiplicity(1, 1))
    }
)
elems5: BinaryAssociation = BinaryAssociation(
    name="elems5",
    ends={
        Property(name="class_NamedElt", type=class_ClassModel, multiplicity=Multiplicity(1, 1)),
        Property(name="class_ClassModel", type=class_NamedElt, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_class_Attribute_NamedElt = Generalization(general=NamedElt, specific=class_Attribute)
gen_class_Classifier_NamedElt = Generalization(general=NamedElt, specific=class_Classifier)
gen_class_DataType_Classifier = Generalization(general=Classifier, specific=class_DataType)
gen_class_Class_Classifier = Generalization(general=Classifier, specific=class_Class)

# Domain Model
domain_model = DomainModel(
    name="class",
    types={class_NamedElt, class_Attribute, class_ClassModel, class_Classifier, NamedElt, class_DataType, Classifier, class_Class},
    associations={super1, attr2, owner3, type4, elems5},
    generalizations={gen_class_Attribute_NamedElt, gen_class_Classifier_NamedElt, gen_class_DataType_Classifier, gen_class_Class_Classifier},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)