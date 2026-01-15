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
CLASS_NamedElement = Class(name="CLASS::NamedElement")
CLASS_System = Class(name="CLASS::System")
CLASS_Classifier = Class(name="CLASS::Classifier")
NamedElement = Class(name="NamedElement")
CLASS_DataType = Class(name="CLASS::DataType")
Classifier = Class(name="Classifier")
CLASS_Class = Class(name="CLASS::Class")
CLASS_Attribute = Class(name="CLASS::Attribute")

# CLASS_NamedElement class attributes and methods
CLASS_NamedElement_name: Property = Property(name="name", type=StringType)
CLASS_NamedElement.attributes={CLASS_NamedElement_name}

# CLASS_System class attributes and methods
CLASS_System_name: Property = Property(name="name", type=StringType)
CLASS_System.attributes={CLASS_System_name}

# CLASS_Classifier class attributes and methods

# NamedElement class attributes and methods

# CLASS_DataType class attributes and methods

# Classifier class attributes and methods

# CLASS_Class class attributes and methods
CLASS_Class_isAbstract: Property = Property(name="isAbstract", type=BooleanType)
CLASS_Class.attributes={CLASS_Class_isAbstract}

# CLASS_Attribute class attributes and methods
CLASS_Attribute_multiValued: Property = Property(name="multiValued", type=BooleanType)
CLASS_Attribute.attributes={CLASS_Attribute_multiValued}

# Relationships
system0: BinaryAssociation = BinaryAssociation(
    name="system0",
    ends={
        Property(name="System", type=CLASS_NamedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="elements", type=CLASS_System, multiplicity=Multiplicity(0, 1))
    }
)
super2: BinaryAssociation = BinaryAssociation(
    name="super2",
    ends={
        Property(name="CLASS_Class", type=CLASS_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="CLASS_Class1", type=CLASS_Class, multiplicity=Multiplicity(0, 1))
    }
)
attributes3: BinaryAssociation = BinaryAssociation(
    name="attributes3",
    ends={
        Property(name="Attribute", type=CLASS_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="owner", type=CLASS_Attribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type4: BinaryAssociation = BinaryAssociation(
    name="type4",
    ends={
        Property(name="CLASS_Classifier", type=CLASS_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="CLASS_Attribute", type=CLASS_Classifier, multiplicity=Multiplicity(0, 1))
    }
)
owner5: BinaryAssociation = BinaryAssociation(
    name="owner5",
    ends={
        Property(name="Class", type=CLASS_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="attributes", type=CLASS_Class, multiplicity=Multiplicity(0, 1))
    }
)
elements6: BinaryAssociation = BinaryAssociation(
    name="elements6",
    ends={
        Property(name="NamedElement", type=CLASS_System, multiplicity=Multiplicity(1, 1)),
        Property(name="system", type=CLASS_NamedElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_CLASS_Classifier_NamedElement = Generalization(general=NamedElement, specific=CLASS_Classifier)
gen_CLASS_DataType_Classifier = Generalization(general=Classifier, specific=CLASS_DataType)
gen_CLASS_Class_Classifier = Generalization(general=Classifier, specific=CLASS_Class)
gen_CLASS_Attribute_NamedElement = Generalization(general=NamedElement, specific=CLASS_Attribute)

# Domain Model
domain_model = DomainModel(
    name="CLASS",
    types={CLASS_NamedElement, CLASS_System, CLASS_Classifier, NamedElement, CLASS_DataType, Classifier, CLASS_Class, CLASS_Attribute},
    associations={system0, super2, attributes3, type4, owner5, elements6},
    generalizations={gen_CLASS_Classifier_NamedElement, gen_CLASS_DataType_Classifier, gen_CLASS_Class_Classifier, gen_CLASS_Attribute_NamedElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)