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
class_DataType = Class(name="class::DataType")
class_Classifier = Class(name="class::Classifier", is_abstract=True)
Classifier = Class(name="Classifier")
class_Attribute = Class(name="class::Attribute")
class_NamedElt = Class(name="class::NamedElt", is_abstract=True)
class_Package = Class(name="class::Package")
NamedElt = Class(name="NamedElt")
class_Class = Class(name="class::Class")

# class_DataType class attributes and methods

# class_Classifier class attributes and methods

# Classifier class attributes and methods

# class_Attribute class attributes and methods
class_Attribute_multiValued: Property = Property(name="multiValued", type=BooleanType)
class_Attribute.attributes={class_Attribute_multiValued}

# class_NamedElt class attributes and methods
class_NamedElt_name: Property = Property(name="name", type=StringType)
class_NamedElt.attributes={class_NamedElt_name}

# class_Package class attributes and methods

# NamedElt class attributes and methods

# class_Class class attributes and methods
class_Class_isAbstract: Property = Property(name="isAbstract", type=BooleanType)
class_Class.attributes={class_Class_isAbstract}

# Relationships
classes0: BinaryAssociation = BinaryAssociation(
    name="classes0",
    ends={
        Property(name="class_Class", type=class_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="class_Package", type=class_Class, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
types1: BinaryAssociation = BinaryAssociation(
    name="types1",
    ends={
        Property(name="class_DataType", type=class_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="class_Package2", type=class_DataType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
super4: BinaryAssociation = BinaryAssociation(
    name="super4",
    ends={
        Property(name="class_Class5", type=class_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="class_Class3", type=class_Class, multiplicity=Multiplicity(0, 9999))
    }
)
attr6: BinaryAssociation = BinaryAssociation(
    name="attr6",
    ends={
        Property(name="Attribute", type=class_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="owner", type=class_Attribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type7: BinaryAssociation = BinaryAssociation(
    name="type7",
    ends={
        Property(name="class_Classifier", type=class_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="class_Attribute", type=class_Classifier, multiplicity=Multiplicity(1, 1))
    }
)
owner8: BinaryAssociation = BinaryAssociation(
    name="owner8",
    ends={
        Property(name="Class", type=class_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="attr", type=class_Class, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_class_Classifier_NamedElt = Generalization(general=NamedElt, specific=class_Classifier)
gen_class_DataType_Classifier = Generalization(general=Classifier, specific=class_DataType)
gen_class_Class_Classifier = Generalization(general=Classifier, specific=class_Class)
gen_class_Package_NamedElt = Generalization(general=NamedElt, specific=class_Package)
gen_class_Attribute_NamedElt = Generalization(general=NamedElt, specific=class_Attribute)

# Domain Model
domain_model = DomainModel(
    name="class",
    types={class_DataType, class_Classifier, Classifier, class_Attribute, class_NamedElt, class_Package, NamedElt, class_Class},
    associations={classes0, types1, super4, attr6, type7, owner8},
    generalizations={gen_class_Classifier_NamedElt, gen_class_DataType_Classifier, gen_class_Class_Classifier, gen_class_Package_NamedElt, gen_class_Attribute_NamedElt},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)