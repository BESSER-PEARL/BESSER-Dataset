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
simpleUML_Classifier = Class(name="simpleUML::Classifier")
simpleUML_DataType = Class(name="simpleUML::DataType")
simpleUML_NamedElement = Class(name="simpleUML::NamedElement")
simpleUML_Package = Class(name="simpleUML::Package")
simpleUML_Class = Class(name="simpleUML::Class")
Classifier = Class(name="Classifier")
simpleUML_Attribute = Class(name="simpleUML::Attribute")
simpleUML_Association = Class(name="simpleUML::Association")
NamedElement = Class(name="NamedElement")

# simpleUML_Classifier class attributes and methods

# simpleUML_DataType class attributes and methods

# simpleUML_NamedElement class attributes and methods
simpleUML_NamedElement_name: Property = Property(name="name", type=StringType)
simpleUML_NamedElement.attributes={simpleUML_NamedElement_name}

# simpleUML_Package class attributes and methods

# simpleUML_Class class attributes and methods

# Classifier class attributes and methods

# simpleUML_Attribute class attributes and methods

# simpleUML_Association class attributes and methods

# NamedElement class attributes and methods

# Relationships
type7: BinaryAssociation = BinaryAssociation(
    name="type7",
    ends={
        Property(name="simpleUML_Classifier", type=simpleUML_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="simpleUML_Attribute8", type=simpleUML_Classifier, multiplicity=Multiplicity(1, 1))
    }
)
ownedElements10: BinaryAssociation = BinaryAssociation(
    name="ownedElements10",
    ends={
        Property(name="Classifier", type=simpleUML_Classifier, multiplicity=Multiplicity(1, 1)),
        Property(name="owner", type=simpleUML_Classifier, multiplicity=Multiplicity(0, 9999))
    }
)
owner12: BinaryAssociation = BinaryAssociation(
    name="owner12",
    ends={
        Property(name="Classifier13", type=simpleUML_Classifier, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedElements", type=simpleUML_Classifier, multiplicity=Multiplicity(0, 1))
    }
)
superClasses1: BinaryAssociation = BinaryAssociation(
    name="superClasses1",
    ends={
        Property(name="simpleUML_Class", type=simpleUML_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="simpleUML_Class0", type=simpleUML_Class, multiplicity=Multiplicity(0, 9999))
    }
)
attributes2: BinaryAssociation = BinaryAssociation(
    name="attributes2",
    ends={
        Property(name="simpleUML_Attribute", type=simpleUML_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="simpleUML_Class3", type=simpleUML_Attribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
sourceAssociations4: BinaryAssociation = BinaryAssociation(
    name="sourceAssociations4",
    ends={
        Property(name="Association", type=simpleUML_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="source", type=simpleUML_Association, multiplicity=Multiplicity(0, 9999))
    }
)
navigableAssociationTargets5: BinaryAssociation = BinaryAssociation(
    name="navigableAssociationTargets5",
    ends={
        Property(name="simpleUML_Association", type=simpleUML_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="simpleUML_Class6", type=simpleUML_Association, multiplicity=Multiplicity(0, 9999))
    }
)
source14: BinaryAssociation = BinaryAssociation(
    name="source14",
    ends={
        Property(name="Class", type=simpleUML_Association, multiplicity=Multiplicity(1, 1)),
        Property(name="sourceAssociations", type=simpleUML_Class, multiplicity=Multiplicity(0, 1))
    }
)
target15: BinaryAssociation = BinaryAssociation(
    name="target15",
    ends={
        Property(name="simpleUML_Class17", type=simpleUML_Association, multiplicity=Multiplicity(1, 1)),
        Property(name="simpleUML_Association16", type=simpleUML_Class, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_simpleUML_Classifier_NamedElement = Generalization(general=NamedElement, specific=simpleUML_Classifier)
gen_simpleUML_DataType_Classifier = Generalization(general=Classifier, specific=simpleUML_DataType)
gen_simpleUML_Package_Classifier = Generalization(general=Classifier, specific=simpleUML_Package)
gen_simpleUML_Association_Classifier = Generalization(general=Classifier, specific=simpleUML_Association)
gen_simpleUML_Class_Classifier = Generalization(general=Classifier, specific=simpleUML_Class)
gen_simpleUML_Attribute_NamedElement = Generalization(general=NamedElement, specific=simpleUML_Attribute)

# Domain Model
domain_model = DomainModel(
    name="simpleUML",
    types={simpleUML_Classifier, simpleUML_DataType, simpleUML_NamedElement, simpleUML_Package, simpleUML_Class, Classifier, simpleUML_Attribute, simpleUML_Association, NamedElement},
    associations={type7, ownedElements10, owner12, superClasses1, attributes2, sourceAssociations4, navigableAssociationTargets5, source14, target15},
    generalizations={gen_simpleUML_Classifier_NamedElement, gen_simpleUML_DataType_Classifier, gen_simpleUML_Package_Classifier, gen_simpleUML_Association_Classifier, gen_simpleUML_Class_Classifier, gen_simpleUML_Attribute_NamedElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)