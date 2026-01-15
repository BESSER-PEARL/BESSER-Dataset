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

# Enumerations
Visibility: Enumeration = Enumeration(
    name="Visibility",
    literals={
            EnumerationLiteral(name="protected"),
			EnumerationLiteral(name="package"),
			EnumerationLiteral(name="public"),
			EnumerationLiteral(name="private")
    }
)

# Classes
classmm_Class = Class(name="classmm::Class")
classmm_Attribute = Class(name="classmm::Attribute")
classmm_Package = Class(name="classmm::Package")
classmm_Method = Class(name="classmm::Method")
classmm_NamedElt = Class(name="classmm::NamedElt")
classmm_Classifier = Class(name="classmm::Classifier")
NamedElt = Class(name="NamedElt")
classmm_DataType = Class(name="classmm::DataType")
Classifier = Class(name="Classifier")
classmm_Parameter = Class(name="classmm::Parameter")

# classmm_Class class attributes and methods
classmm_Class_isAbstract: Property = Property(name="isAbstract", type=BooleanType)
classmm_Class_visibility: Property = Property(name="visibility", type=StringType)
classmm_Class.attributes={classmm_Class_visibility, classmm_Class_isAbstract}

# classmm_Attribute class attributes and methods
classmm_Attribute_multivalued: Property = Property(name="multivalued", type=BooleanType)
classmm_Attribute_visibility: Property = Property(name="visibility", type=StringType)
classmm_Attribute.attributes={classmm_Attribute_multivalued, classmm_Attribute_visibility}

# classmm_Package class attributes and methods

# classmm_Method class attributes and methods

# classmm_NamedElt class attributes and methods
classmm_NamedElt_name: Property = Property(name="name", type=StringType)
classmm_NamedElt.attributes={classmm_NamedElt_name}

# classmm_Classifier class attributes and methods

# NamedElt class attributes and methods

# classmm_DataType class attributes and methods

# Classifier class attributes and methods

# classmm_Parameter class attributes and methods

# Relationships
att0: BinaryAssociation = BinaryAssociation(
    name="att0",
    ends={
        Property(name="Attribute", type=classmm_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="owner", type=classmm_Attribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
super2: BinaryAssociation = BinaryAssociation(
    name="super2",
    ends={
        Property(name="classmm_Class", type=classmm_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="classmm_Class1", type=classmm_Class, multiplicity=Multiplicity(0, 9999))
    }
)
package3: BinaryAssociation = BinaryAssociation(
    name="package3",
    ends={
        Property(name="Package", type=classmm_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="classes", type=classmm_Package, multiplicity=Multiplicity(1, 1))
    }
)
methods4: BinaryAssociation = BinaryAssociation(
    name="methods4",
    ends={
        Property(name="Method", type=classmm_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="owner5", type=classmm_Method, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type6: BinaryAssociation = BinaryAssociation(
    name="type6",
    ends={
        Property(name="classmm_Classifier", type=classmm_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="classmm_Attribute", type=classmm_Classifier, multiplicity=Multiplicity(1, 1))
    }
)
owner7: BinaryAssociation = BinaryAssociation(
    name="owner7",
    ends={
        Property(name="Class", type=classmm_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="att", type=classmm_Class, multiplicity=Multiplicity(1, 1))
    }
)
classes8: BinaryAssociation = BinaryAssociation(
    name="classes8",
    ends={
        Property(name="Class9", type=classmm_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="package", type=classmm_Class, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
owner10: BinaryAssociation = BinaryAssociation(
    name="owner10",
    ends={
        Property(name="Class11", type=classmm_Method, multiplicity=Multiplicity(1, 1)),
        Property(name="methods", type=classmm_Class, multiplicity=Multiplicity(1, 1))
    }
)
params12: BinaryAssociation = BinaryAssociation(
    name="params12",
    ends={
        Property(name="Parameter", type=classmm_Method, multiplicity=Multiplicity(1, 1)),
        Property(name="owner13", type=classmm_Parameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type14: BinaryAssociation = BinaryAssociation(
    name="type14",
    ends={
        Property(name="classmm_Classifier15", type=classmm_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="classmm_Parameter", type=classmm_Classifier, multiplicity=Multiplicity(1, 1))
    }
)
owner16: BinaryAssociation = BinaryAssociation(
    name="owner16",
    ends={
        Property(name="Method17", type=classmm_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="params", type=classmm_Method, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_classmm_Class_Classifier = Generalization(general=Classifier, specific=classmm_Class)
gen_classmm_Attribute_NamedElt = Generalization(general=NamedElt, specific=classmm_Attribute)
gen_classmm_Package_NamedElt = Generalization(general=NamedElt, specific=classmm_Package)
gen_classmm_Classifier_NamedElt = Generalization(general=NamedElt, specific=classmm_Classifier)
gen_classmm_DataType_Classifier = Generalization(general=Classifier, specific=classmm_DataType)
gen_classmm_Method_NamedElt = Generalization(general=NamedElt, specific=classmm_Method)
gen_classmm_Parameter_NamedElt = Generalization(general=NamedElt, specific=classmm_Parameter)

# Domain Model
domain_model = DomainModel(
    name="classmm",
    types={classmm_Class, classmm_Attribute, classmm_Package, classmm_Method, classmm_NamedElt, classmm_Classifier, NamedElt, classmm_DataType, Classifier, classmm_Parameter, Visibility},
    associations={att0, super2, package3, methods4, type6, owner7, classes8, owner10, params12, type14, owner16},
    generalizations={gen_classmm_Class_Classifier, gen_classmm_Attribute_NamedElt, gen_classmm_Package_NamedElt, gen_classmm_Classifier_NamedElt, gen_classmm_DataType_Classifier, gen_classmm_Method_NamedElt, gen_classmm_Parameter_NamedElt},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)