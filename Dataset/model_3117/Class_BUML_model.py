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
Class_Classifier = Class(name="Class::Classifier", is_abstract=True)
NamedElt = Class(name="NamedElt")
Class_NamedElt = Class(name="Class::NamedElt", is_abstract=True)
Class_DataType = Class(name="Class::DataType")
Classifier = Class(name="Classifier")
Class_Class = Class(name="Class::Class")
Class_ = Class(name="Class")
Attribute = Class(name="Attribute")
Class_Attribute = Class(name="Class::Attribute")

# Class_Classifier class attributes and methods

# NamedElt class attributes and methods

# Class_NamedElt class attributes and methods
Class_NamedElt_name: Property = Property(name="name", type=StringType)
Class_NamedElt.attributes={Class_NamedElt_name}

# Class_DataType class attributes and methods

# Classifier class attributes and methods

# Class_Class class attributes and methods
Class_Class_isAbstract: Property = Property(name="isAbstract", type=StringType)
Class_Class.attributes={Class_Class_isAbstract}

# Class class attributes and methods

# Attribute class attributes and methods

# Class_Attribute class attributes and methods
Class_Attribute_multiValued: Property = Property(name="multiValued", type=StringType)
Class_Attribute.attributes={Class_Attribute_multiValued}

# Relationships
super0: BinaryAssociation = BinaryAssociation(
    name="super0",
    ends={
        Property(name="Class", type=Class_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="Class_Class", type=Class_, multiplicity=Multiplicity(0, 9999))
    }
)
attr1: BinaryAssociation = BinaryAssociation(
    name="attr1",
    ends={
        Property(name="#", type=Class_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="1", type=Attribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type2: BinaryAssociation = BinaryAssociation(
    name="type2",
    ends={
        Property(name="Classifier", type=Class_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="Class_Attribute", type=Classifier, multiplicity=Multiplicity(1, 1))
    }
)
owner3: BinaryAssociation = BinaryAssociation(
    name="owner3",
    ends={
        Property(name="#5", type=Class_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="14", type=Class_, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_Class_Classifier_NamedElt = Generalization(general=NamedElt, specific=Class_Classifier)
gen_Class_DataType_Classifier = Generalization(general=Classifier, specific=Class_DataType)
gen_Class_Class_Classifier = Generalization(general=Classifier, specific=Class_Class)
gen_Class_Attribute_NamedElt = Generalization(general=NamedElt, specific=Class_Attribute)

# Domain Model
domain_model = DomainModel(
    name="Class",
    types={Class_Classifier, NamedElt, Class_NamedElt, Class_DataType, Classifier, Class_Class, Class_, Attribute, Class_Attribute},
    associations={super0, attr1, type2, owner3},
    generalizations={gen_Class_Classifier_NamedElt, gen_Class_DataType_Classifier, gen_Class_Class_Classifier, gen_Class_Attribute_NamedElt},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)