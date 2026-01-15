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
AggregationKind: Enumeration = Enumeration(
    name="AggregationKind",
    literals={
            EnumerationLiteral(name="none"),
			EnumerationLiteral(name="shared"),
			EnumerationLiteral(name="composite")
    }
)

# Classes
ClassDiagram_Class = Class(name="ClassDiagram::Class")
ClassDiagram_Property = Class(name="ClassDiagram::Property")
ClassDiagram_Interface = Class(name="ClassDiagram::Interface")
ClassDiagram_Classifier = Class(name="ClassDiagram::Classifier", is_abstract=True)
ClassDiagram_DataType = Class(name="ClassDiagram::DataType")
Classifier = Class(name="Classifier")
ClassDiagram_Relationship = Class(name="ClassDiagram::Relationship", is_abstract=True)
ClassDiagram_Association = Class(name="ClassDiagram::Association")
Relationship = Class(name="Relationship")
ClassDiagram_Generalization = Class(name="ClassDiagram::Generalization")
ClassDiagram_Dependency = Class(name="ClassDiagram::Dependency")
ClassDiagram_Realization = Class(name="ClassDiagram::Realization")
Dependency = Class(name="Dependency")

# ClassDiagram_Class class attributes and methods

# ClassDiagram_Property class attributes and methods
ClassDiagram_Property_name: Property = Property(name="name", type=StringType)
ClassDiagram_Property_lower: Property = Property(name="lower", type=IntegerType)
ClassDiagram_Property_upper: Property = Property(name="upper", type=StringType)
ClassDiagram_Property_aggregation: Property = Property(name="aggregation", type=StringType)
ClassDiagram_Property.attributes={ClassDiagram_Property_aggregation, ClassDiagram_Property_lower, ClassDiagram_Property_name, ClassDiagram_Property_upper}

# ClassDiagram_Interface class attributes and methods

# ClassDiagram_Classifier class attributes and methods
ClassDiagram_Classifier_name: Property = Property(name="name", type=StringType)
ClassDiagram_Classifier.attributes={ClassDiagram_Classifier_name}

# ClassDiagram_DataType class attributes and methods

# Classifier class attributes and methods

# ClassDiagram_Relationship class attributes and methods

# ClassDiagram_Association class attributes and methods
ClassDiagram_Association_name: Property = Property(name="name", type=StringType)
ClassDiagram_Association.attributes={ClassDiagram_Association_name}

# Relationship class attributes and methods

# ClassDiagram_Generalization class attributes and methods

# ClassDiagram_Dependency class attributes and methods

# ClassDiagram_Realization class attributes and methods

# Dependency class attributes and methods

# Relationships
ownedAttribute0: BinaryAssociation = BinaryAssociation(
    name="ownedAttribute0",
    ends={
        Property(name="ClassDiagram_Property", type=ClassDiagram_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="ClassDiagram_Class", type=ClassDiagram_Property, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
general7: BinaryAssociation = BinaryAssociation(
    name="general7",
    ends={
        Property(name="ClassDiagram_Classifier8", type=ClassDiagram_Generalization, multiplicity=Multiplicity(1, 1)),
        Property(name="ClassDiagram_Generalization", type=ClassDiagram_Classifier, multiplicity=Multiplicity(1, 1))
    }
)
specific9: BinaryAssociation = BinaryAssociation(
    name="specific9",
    ends={
        Property(name="ClassDiagram_Classifier11", type=ClassDiagram_Generalization, multiplicity=Multiplicity(1, 1)),
        Property(name="ClassDiagram_Generalization10", type=ClassDiagram_Classifier, multiplicity=Multiplicity(1, 1))
    }
)
ownedAttribute1: BinaryAssociation = BinaryAssociation(
    name="ownedAttribute1",
    ends={
        Property(name="ClassDiagram_Property2", type=ClassDiagram_Interface, multiplicity=Multiplicity(1, 1)),
        Property(name="ClassDiagram_Interface", type=ClassDiagram_Property, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type3: BinaryAssociation = BinaryAssociation(
    name="type3",
    ends={
        Property(name="ClassDiagram_Classifier", type=ClassDiagram_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="ClassDiagram_Property4", type=ClassDiagram_Classifier, multiplicity=Multiplicity(1, 1))
    }
)
memberEnd5: BinaryAssociation = BinaryAssociation(
    name="memberEnd5",
    ends={
        Property(name="ClassDiagram_Property6", type=ClassDiagram_Association, multiplicity=Multiplicity(1, 1)),
        Property(name="ClassDiagram_Association", type=ClassDiagram_Property, multiplicity=Multiplicity(2, 2), is_composite=True)
    }
)
supplier12: BinaryAssociation = BinaryAssociation(
    name="supplier12",
    ends={
        Property(name="ClassDiagram_Classifier13", type=ClassDiagram_Dependency, multiplicity=Multiplicity(1, 1)),
        Property(name="ClassDiagram_Dependency", type=ClassDiagram_Classifier, multiplicity=Multiplicity(1, 9999))
    }
)
client14: BinaryAssociation = BinaryAssociation(
    name="client14",
    ends={
        Property(name="ClassDiagram_Classifier16", type=ClassDiagram_Dependency, multiplicity=Multiplicity(1, 1)),
        Property(name="ClassDiagram_Dependency15", type=ClassDiagram_Classifier, multiplicity=Multiplicity(1, 9999))
    }
)

# Generalizations
gen_ClassDiagram_Class_Classifier = Generalization(general=Classifier, specific=ClassDiagram_Class)
gen_ClassDiagram_Interface_Classifier = Generalization(general=Classifier, specific=ClassDiagram_Interface)
gen_ClassDiagram_DataType_Classifier = Generalization(general=Classifier, specific=ClassDiagram_DataType)
gen_ClassDiagram_Generalization_Relationship = Generalization(general=Relationship, specific=ClassDiagram_Generalization)
gen_ClassDiagram_Association_Relationship = Generalization(general=Relationship, specific=ClassDiagram_Association)
gen_ClassDiagram_Dependency_Relationship = Generalization(general=Relationship, specific=ClassDiagram_Dependency)
gen_ClassDiagram_Realization_Dependency = Generalization(general=Dependency, specific=ClassDiagram_Realization)

# Domain Model
domain_model = DomainModel(
    name="ClassDiagram",
    types={ClassDiagram_Class, ClassDiagram_Property, ClassDiagram_Interface, ClassDiagram_Classifier, ClassDiagram_DataType, Classifier, ClassDiagram_Relationship, ClassDiagram_Association, Relationship, ClassDiagram_Generalization, ClassDiagram_Dependency, ClassDiagram_Realization, Dependency, AggregationKind},
    associations={ownedAttribute0, general7, specific9, ownedAttribute1, type3, memberEnd5, supplier12, client14},
    generalizations={gen_ClassDiagram_Class_Classifier, gen_ClassDiagram_Interface_Classifier, gen_ClassDiagram_DataType_Classifier, gen_ClassDiagram_Generalization_Relationship, gen_ClassDiagram_Association_Relationship, gen_ClassDiagram_Dependency_Relationship, gen_ClassDiagram_Realization_Dependency},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)