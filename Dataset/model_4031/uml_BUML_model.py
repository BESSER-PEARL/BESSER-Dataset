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
uml_association = Class(name="uml::association")
uml_attribute = Class(name="uml::attribute")
uml_ownerClassifier = Class(name="uml::ownerClassifier")
uml_attributes = Class(name="uml::attributes")
uml_class_ = Class(name="uml::class::")
uml_generalClass = Class(name="uml::generalClass")
uml_classifiersAndAssociations = Class(name="uml::classifiersAndAssociations")
uml_DocumentRoot = Class(name="uml::DocumentRoot")
uml_EStringToStringMapEntry = Class(name="uml::EStringToStringMapEntry")
uml_primitiveDataType = Class(name="uml::primitiveDataType")
uml_packages = Class(name="uml::packages")
uml_UML = Class(name="uml::UML")
uml_package_ = Class(name="uml::package::")

# uml_association class attributes and methods
uml_association_destination: Property = Property(name="destination", type=StringType)
uml_association_kind: Property = Property(name="kind", type=StringType)
uml_association_name: Property = Property(name="name", type=StringType)
uml_association_oID: Property = Property(name="oID", type=StringType)
uml_association_source: Property = Property(name="source", type=StringType)
uml_association.attributes={uml_association_destination, uml_association_kind, uml_association_name, uml_association_oID, uml_association_source}

# uml_attribute class attributes and methods
uml_attribute_kind: Property = Property(name="kind", type=StringType)
uml_attribute_name: Property = Property(name="name", type=StringType)
uml_attribute_oID: Property = Property(name="oID", type=StringType)
uml_attribute.attributes={uml_attribute_name, uml_attribute_oID, uml_attribute_kind}

# uml_ownerClassifier class attributes and methods

# uml_attributes class attributes and methods
uml_attributes_group: Property = Property(name="group", type=StringType)
uml_attributes.attributes={uml_attributes_group}

# uml_class_ class attributes and methods
uml_class__kind: Property = Property(name="kind", type=StringType)
uml_class__name: Property = Property(name="name", type=StringType)
uml_class__oID: Property = Property(name="oID", type=StringType)
uml_class_.attributes={uml_class__oID, uml_class__kind, uml_class__name}

# uml_generalClass class attributes and methods

# uml_classifiersAndAssociations class attributes and methods
uml_classifiersAndAssociations_group: Property = Property(name="group", type=StringType)
uml_classifiersAndAssociations.attributes={uml_classifiersAndAssociations_group}

# uml_DocumentRoot class attributes and methods
uml_DocumentRoot_mixed: Property = Property(name="mixed", type=StringType)
uml_DocumentRoot.attributes={uml_DocumentRoot_mixed}

# uml_EStringToStringMapEntry class attributes and methods

# uml_primitiveDataType class attributes and methods
uml_primitiveDataType_kind: Property = Property(name="kind", type=StringType)
uml_primitiveDataType_name: Property = Property(name="name", type=StringType)
uml_primitiveDataType_oID: Property = Property(name="oID", type=StringType)
uml_primitiveDataType.attributes={uml_primitiveDataType_kind, uml_primitiveDataType_oID, uml_primitiveDataType_name}

# uml_packages class attributes and methods
uml_packages_group: Property = Property(name="group", type=StringType)
uml_packages.attributes={uml_packages_group}

# uml_UML class attributes and methods

# uml_package_ class attributes and methods
uml_package__name: Property = Property(name="name", type=StringType)
uml_package__oID: Property = Property(name="oID", type=StringType)
uml_package__kind: Property = Property(name="kind", type=StringType)
uml_package_.attributes={uml_package__kind, uml_package__oID, uml_package__name}

# Relationships
ownerClassifier0: BinaryAssociation = BinaryAssociation(
    name="ownerClassifier0",
    ends={
        Property(name="uml_ownerClassifier", type=uml_attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_attribute", type=uml_ownerClassifier, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
attribute1: BinaryAssociation = BinaryAssociation(
    name="attribute1",
    ends={
        Property(name="uml_attribute2", type=uml_attributes, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_attributes", type=uml_attribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
generalClass3: BinaryAssociation = BinaryAssociation(
    name="generalClass3",
    ends={
        Property(name="uml_generalClass", type=uml_class_, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_class_", type=uml_generalClass, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
attributes4: BinaryAssociation = BinaryAssociation(
    name="attributes4",
    ends={
        Property(name="uml_attributes6", type=uml_class_, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_class_5", type=uml_attributes, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
association11: BinaryAssociation = BinaryAssociation(
    name="association11",
    ends={
        Property(name="uml_association", type=uml_classifiersAndAssociations, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_classifiersAndAssociations12", type=uml_association, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
xMLNSPrefixMap13: BinaryAssociation = BinaryAssociation(
    name="xMLNSPrefixMap13",
    ends={
        Property(name="uml_EStringToStringMapEntry", type=uml_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_DocumentRoot", type=uml_EStringToStringMapEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
class7: BinaryAssociation = BinaryAssociation(
    name="class7",
    ends={
        Property(name="uml_class_8", type=uml_classifiersAndAssociations, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_classifiersAndAssociations", type=uml_class_, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
primitiveDataType9: BinaryAssociation = BinaryAssociation(
    name="primitiveDataType9",
    ends={
        Property(name="uml_primitiveDataType", type=uml_classifiersAndAssociations, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_classifiersAndAssociations10", type=uml_primitiveDataType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
xSISchemaLocation14: BinaryAssociation = BinaryAssociation(
    name="xSISchemaLocation14",
    ends={
        Property(name="uml_EStringToStringMapEntry16", type=uml_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_DocumentRoot15", type=uml_EStringToStringMapEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
association17: BinaryAssociation = BinaryAssociation(
    name="association17",
    ends={
        Property(name="uml_association19", type=uml_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_DocumentRoot18", type=uml_association, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
attribute20: BinaryAssociation = BinaryAssociation(
    name="attribute20",
    ends={
        Property(name="uml_attribute22", type=uml_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_DocumentRoot21", type=uml_attribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
attributes23: BinaryAssociation = BinaryAssociation(
    name="attributes23",
    ends={
        Property(name="uml_attributes25", type=uml_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_DocumentRoot24", type=uml_attributes, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
class26: BinaryAssociation = BinaryAssociation(
    name="class26",
    ends={
        Property(name="uml_class_28", type=uml_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_DocumentRoot27", type=uml_class_, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
classifiersAndAssociations29: BinaryAssociation = BinaryAssociation(
    name="classifiersAndAssociations29",
    ends={
        Property(name="uml_classifiersAndAssociations31", type=uml_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_DocumentRoot30", type=uml_classifiersAndAssociations, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
generalClass32: BinaryAssociation = BinaryAssociation(
    name="generalClass32",
    ends={
        Property(name="uml_generalClass34", type=uml_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_DocumentRoot33", type=uml_generalClass, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
packages40: BinaryAssociation = BinaryAssociation(
    name="packages40",
    ends={
        Property(name="uml_packages", type=uml_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_DocumentRoot41", type=uml_packages, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
primitiveDataType42: BinaryAssociation = BinaryAssociation(
    name="primitiveDataType42",
    ends={
        Property(name="uml_primitiveDataType44", type=uml_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_DocumentRoot43", type=uml_primitiveDataType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uML45: BinaryAssociation = BinaryAssociation(
    name="uML45",
    ends={
        Property(name="uml_UML", type=uml_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_DocumentRoot46", type=uml_UML, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
class47: BinaryAssociation = BinaryAssociation(
    name="class47",
    ends={
        Property(name="uml_class_49", type=uml_generalClass, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_generalClass48", type=uml_class_, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
class50: BinaryAssociation = BinaryAssociation(
    name="class50",
    ends={
        Property(name="uml_class_52", type=uml_ownerClassifier, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_ownerClassifier51", type=uml_class_, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
primitiveDataType53: BinaryAssociation = BinaryAssociation(
    name="primitiveDataType53",
    ends={
        Property(name="uml_primitiveDataType55", type=uml_ownerClassifier, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_ownerClassifier54", type=uml_primitiveDataType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ownerClassifier35: BinaryAssociation = BinaryAssociation(
    name="ownerClassifier35",
    ends={
        Property(name="uml_ownerClassifier37", type=uml_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_DocumentRoot36", type=uml_ownerClassifier, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
package38: BinaryAssociation = BinaryAssociation(
    name="package38",
    ends={
        Property(name="uml_package_", type=uml_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_DocumentRoot39", type=uml_package_, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
package59: BinaryAssociation = BinaryAssociation(
    name="package59",
    ends={
        Property(name="uml_package_61", type=uml_packages, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_packages60", type=uml_package_, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
packages62: BinaryAssociation = BinaryAssociation(
    name="packages62",
    ends={
        Property(name="uml_packages64", type=uml_UML, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_UML63", type=uml_packages, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
classifiersAndAssociations56: BinaryAssociation = BinaryAssociation(
    name="classifiersAndAssociations56",
    ends={
        Property(name="uml_classifiersAndAssociations58", type=uml_package_, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_package_57", type=uml_classifiersAndAssociations, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="uml",
    types={uml_association, uml_attribute, uml_ownerClassifier, uml_attributes, uml_class_, uml_generalClass, uml_classifiersAndAssociations, uml_DocumentRoot, uml_EStringToStringMapEntry, uml_primitiveDataType, uml_packages, uml_UML, uml_package_},
    associations={ownerClassifier0, attribute1, generalClass3, attributes4, association11, xMLNSPrefixMap13, class7, primitiveDataType9, xSISchemaLocation14, association17, attribute20, attributes23, class26, classifiersAndAssociations29, generalClass32, packages40, primitiveDataType42, uML45, class47, class50, primitiveDataType53, ownerClassifier35, package38, package59, packages62, classifiersAndAssociations56},
    generalizations={},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)