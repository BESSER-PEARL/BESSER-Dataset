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
Class_NamedElt = Class(name="Class::NamedElt", is_abstract=True)
Class_Package = Class(name="Class::Package")
NamedElt = Class(name="NamedElt")
Class_Classifier = Class(name="Class::Classifier", is_abstract=True)
Class_DataType = Class(name="Class::DataType")
Classifier = Class(name="Classifier")
Class_Class = Class(name="Class::Class")
Class_Attribute = Class(name="Class::Attribute")

# Class_NamedElt class attributes and methods
Class_NamedElt_name: Property = Property(name="name", type=StringType)
Class_NamedElt.attributes={Class_NamedElt_name}

# Class_Package class attributes and methods

# NamedElt class attributes and methods

# Class_Classifier class attributes and methods

# Class_DataType class attributes and methods

# Classifier class attributes and methods

# Class_Class class attributes and methods
Class_Class_isAbstract: Property = Property(name="isAbstract", type=BooleanType)
Class_Class.attributes={Class_Class_isAbstract}

# Class_Attribute class attributes and methods
Class_Attribute_multiValued: Property = Property(name="multiValued", type=BooleanType)
Class_Attribute.attributes={Class_Attribute_multiValued}

# Relationships
elems0: BinaryAssociation = BinaryAssociation(
    name="elems0",
    ends={
        Property(name="Classifier", type=Class_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="package", type=Class_Classifier, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
package1: BinaryAssociation = BinaryAssociation(
    name="package1",
    ends={
        Property(name="Package", type=Class_Classifier, multiplicity=Multiplicity(1, 1)),
        Property(name="elems", type=Class_Package, multiplicity=Multiplicity(0, 1))
    }
)
type5: BinaryAssociation = BinaryAssociation(
    name="type5",
    ends={
        Property(name="Class_Classifier", type=Class_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="Class_Attribute", type=Class_Classifier, multiplicity=Multiplicity(1, 1))
    }
)
owner6: BinaryAssociation = BinaryAssociation(
    name="owner6",
    ends={
        Property(name="Class", type=Class_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="att", type=Class_Class, multiplicity=Multiplicity(1, 1))
    }
)
supers3: BinaryAssociation = BinaryAssociation(
    name="supers3",
    ends={
        Property(name="Class_Class", type=Class_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="Class_Class2", type=Class_Class, multiplicity=Multiplicity(0, 9999))
    }
)
att4: BinaryAssociation = BinaryAssociation(
    name="att4",
    ends={
        Property(name="Attribute", type=Class_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="owner", type=Class_Attribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_Class_Package_NamedElt = Generalization(general=NamedElt, specific=Class_Package)
gen_Class_Classifier_NamedElt = Generalization(general=NamedElt, specific=Class_Classifier)
gen_Class_DataType_Classifier = Generalization(general=Classifier, specific=Class_DataType)
gen_Class_Class_Classifier = Generalization(general=Classifier, specific=Class_Class)
gen_Class_Attribute_NamedElt = Generalization(general=NamedElt, specific=Class_Attribute)

# Domain Model
domain_model = DomainModel(
    name="Class",
    types={Class_NamedElt, Class_Package, NamedElt, Class_Classifier, Class_DataType, Classifier, Class_Class, Class_Attribute},
    associations={elems0, package1, type5, owner6, supers3, att4},
    generalizations={gen_Class_Package_NamedElt, gen_Class_Classifier_NamedElt, gen_Class_DataType_Classifier, gen_Class_Class_Classifier, gen_Class_Attribute_NamedElt},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)