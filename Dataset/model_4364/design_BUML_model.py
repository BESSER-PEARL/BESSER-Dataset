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
Languages: Enumeration = Enumeration(
    name="Languages",
    literals={
            EnumerationLiteral(name="Java"),
			EnumerationLiteral(name="CS"),
			EnumerationLiteral(name="Python"),
			EnumerationLiteral(name="CPP")
    }
)

Types: Enumeration = Enumeration(
    name="Types",
    literals={
            EnumerationLiteral(name="int"),
			EnumerationLiteral(name="long"),
			EnumerationLiteral(name="double"),
			EnumerationLiteral(name="float"),
			EnumerationLiteral(name="string"),
			EnumerationLiteral(name="boolean"),
			EnumerationLiteral(name="void")
    }
)

AccessModifiers: Enumeration = Enumeration(
    name="AccessModifiers",
    literals={
            EnumerationLiteral(name="public"),
			EnumerationLiteral(name="protected"),
			EnumerationLiteral(name="private")
    }
)

# Classes
design_Class = Class(name="design::Class")
Classifier = Class(name="Classifier")
design_Attribute = Class(name="design::Attribute")
design_Operation = Class(name="design::Operation")
design_Association = Class(name="design::Association")
Relation = Class(name="Relation")
design_Generalization = Class(name="design::Generalization")
design_Dependency = Class(name="design::Dependency")
design_Composition = Class(name="design::Composition")
design_Aggregation = Class(name="design::Aggregation")
design_Realization = Class(name="design::Realization")
design_Interface = Class(name="design::Interface")
design_Design = Class(name="design::Design")
design_Classifier = Class(name="design::Classifier", is_abstract=True)
design_Relation = Class(name="design::Relation", is_abstract=True)

# design_Class class attributes and methods

# Classifier class attributes and methods

# design_Attribute class attributes and methods
design_Attribute_name: Property = Property(name="name", type=StringType)
design_Attribute_type: Property = Property(name="type", type=StringType)
design_Attribute.attributes={design_Attribute_name, design_Attribute_type}

# design_Operation class attributes and methods
design_Operation_name: Property = Property(name="name", type=StringType)
design_Operation_returnType: Property = Property(name="returnType", type=StringType)
design_Operation.attributes={design_Operation_returnType, design_Operation_name}

# design_Association class attributes and methods

# Relation class attributes and methods

# design_Generalization class attributes and methods

# design_Dependency class attributes and methods

# design_Composition class attributes and methods

# design_Aggregation class attributes and methods

# design_Realization class attributes and methods

# design_Interface class attributes and methods

# design_Design class attributes and methods
design_Design_language: Property = Property(name="language", type=StringType)
design_Design.attributes={design_Design_language}

# design_Classifier class attributes and methods
design_Classifier_accessModifier: Property = Property(name="accessModifier", type=StringType)
design_Classifier_name: Property = Property(name="name", type=StringType)
design_Classifier.attributes={design_Classifier_name, design_Classifier_accessModifier}

# design_Relation class attributes and methods

# Relationships
source3: BinaryAssociation = BinaryAssociation(
    name="source3",
    ends={
        Property(name="design_Classifier5", type=design_Relation, multiplicity=Multiplicity(1, 1)),
        Property(name="design_Relation4", type=design_Classifier, multiplicity=Multiplicity(0, 1))
    }
)
target6: BinaryAssociation = BinaryAssociation(
    name="target6",
    ends={
        Property(name="design_Classifier8", type=design_Relation, multiplicity=Multiplicity(1, 1)),
        Property(name="design_Relation7", type=design_Classifier, multiplicity=Multiplicity(0, 1))
    }
)
attributes9: BinaryAssociation = BinaryAssociation(
    name="attributes9",
    ends={
        Property(name="design_Attribute", type=design_Classifier, multiplicity=Multiplicity(1, 1)),
        Property(name="design_Classifier10", type=design_Attribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
operations11: BinaryAssociation = BinaryAssociation(
    name="operations11",
    ends={
        Property(name="design_Operation", type=design_Classifier, multiplicity=Multiplicity(1, 1)),
        Property(name="design_Classifier12", type=design_Operation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elements0: BinaryAssociation = BinaryAssociation(
    name="elements0",
    ends={
        Property(name="design_Classifier", type=design_Design, multiplicity=Multiplicity(1, 1)),
        Property(name="design_Design", type=design_Classifier, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
relations1: BinaryAssociation = BinaryAssociation(
    name="relations1",
    ends={
        Property(name="design_Relation", type=design_Design, multiplicity=Multiplicity(1, 1)),
        Property(name="design_Design2", type=design_Relation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_design_Class_Classifier = Generalization(general=Classifier, specific=design_Class)
gen_design_Association_Relation = Generalization(general=Relation, specific=design_Association)
gen_design_Generalization_Relation = Generalization(general=Relation, specific=design_Generalization)
gen_design_Dependency_Relation = Generalization(general=Relation, specific=design_Dependency)
gen_design_Composition_Relation = Generalization(general=Relation, specific=design_Composition)
gen_design_Aggregation_Relation = Generalization(general=Relation, specific=design_Aggregation)
gen_design_Realization_Relation = Generalization(general=Relation, specific=design_Realization)
gen_design_Interface_Classifier = Generalization(general=Classifier, specific=design_Interface)

# Domain Model
domain_model = DomainModel(
    name="design",
    types={design_Class, Classifier, design_Attribute, design_Operation, design_Association, Relation, design_Generalization, design_Dependency, design_Composition, design_Aggregation, design_Realization, design_Interface, design_Design, design_Classifier, design_Relation, Languages, Types, AccessModifiers},
    associations={source3, target6, attributes9, operations11, elements0, relations1},
    generalizations={gen_design_Class_Classifier, gen_design_Association_Relation, gen_design_Generalization_Relation, gen_design_Dependency_Relation, gen_design_Composition_Relation, gen_design_Aggregation_Relation, gen_design_Realization_Relation, gen_design_Interface_Classifier},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)