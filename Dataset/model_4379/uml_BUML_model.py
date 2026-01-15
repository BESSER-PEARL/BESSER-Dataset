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
euml_Package = Class(name="euml::Package")
NamedElement = Class(name="NamedElement")
euml_Class = Class(name="euml::Class")
euml_Dependecy = Class(name="euml::Dependecy")
euml_Attribute = Class(name="euml::Attribute")
euml_Generalization = Class(name="euml::Generalization")
euml_Operation = Class(name="euml::Operation")
euml_Realization = Class(name="euml::Realization")
Relations = Class(name="Relations")
euml_NamedElement = Class(name="euml::NamedElement", is_abstract=True)
euml_Relations = Class(name="euml::Relations", is_abstract=True)

# euml_Package class attributes and methods

# NamedElement class attributes and methods

# euml_Class class attributes and methods

# euml_Dependecy class attributes and methods

# euml_Attribute class attributes and methods

# euml_Generalization class attributes and methods

# euml_Operation class attributes and methods

# euml_Realization class attributes and methods

# Relations class attributes and methods

# euml_NamedElement class attributes and methods
euml_NamedElement_name: Property = Property(name="name", type=StringType)
euml_NamedElement.attributes={euml_NamedElement_name}

# euml_Relations class attributes and methods

# Relationships
classes0: BinaryAssociation = BinaryAssociation(
    name="classes0",
    ends={
        Property(name="euml_Class", type=euml_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="euml_Package", type=euml_Class, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
packages2: BinaryAssociation = BinaryAssociation(
    name="packages2",
    ends={
        Property(name="euml_Package3", type=euml_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="euml_Package1", type=euml_Package, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dependencies4: BinaryAssociation = BinaryAssociation(
    name="dependencies4",
    ends={
        Property(name="euml_Dependecy", type=euml_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="euml_Class5", type=euml_Dependecy, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
attributes6: BinaryAssociation = BinaryAssociation(
    name="attributes6",
    ends={
        Property(name="euml_Attribute", type=euml_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="euml_Class7", type=euml_Attribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
generalizations12: BinaryAssociation = BinaryAssociation(
    name="generalizations12",
    ends={
        Property(name="euml_Generalization", type=euml_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="euml_Class13", type=euml_Generalization, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
operations8: BinaryAssociation = BinaryAssociation(
    name="operations8",
    ends={
        Property(name="euml_Operation", type=euml_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="euml_Class9", type=euml_Operation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
realizations10: BinaryAssociation = BinaryAssociation(
    name="realizations10",
    ends={
        Property(name="euml_Realization", type=euml_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="euml_Class11", type=euml_Realization, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type14: BinaryAssociation = BinaryAssociation(
    name="type14",
    ends={
        Property(name="euml_Class16", type=euml_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="euml_Attribute15", type=euml_Class, multiplicity=Multiplicity(0, 1))
    }
)
target20: BinaryAssociation = BinaryAssociation(
    name="target20",
    ends={
        Property(name="euml_NamedElement", type=euml_Relations, multiplicity=Multiplicity(1, 1)),
        Property(name="euml_Relations", type=euml_NamedElement, multiplicity=Multiplicity(0, 1))
    }
)
returnType17: BinaryAssociation = BinaryAssociation(
    name="returnType17",
    ends={
        Property(name="euml_Class19", type=euml_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="euml_Operation18", type=euml_Class, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_euml_Package_NamedElement = Generalization(general=NamedElement, specific=euml_Package)
gen_euml_Class_NamedElement = Generalization(general=NamedElement, specific=euml_Class)
gen_euml_Dependecy_Relations = Generalization(general=Relations, specific=euml_Dependecy)
gen_euml_Attribute_NamedElement = Generalization(general=NamedElement, specific=euml_Attribute)
gen_euml_Generalization_Relations = Generalization(general=Relations, specific=euml_Generalization)
gen_euml_Realization_Relations = Generalization(general=Relations, specific=euml_Realization)
gen_euml_Operation_NamedElement = Generalization(general=NamedElement, specific=euml_Operation)

# Domain Model
domain_model = DomainModel(
    name="euml",
    types={euml_Package, NamedElement, euml_Class, euml_Dependecy, euml_Attribute, euml_Generalization, euml_Operation, euml_Realization, Relations, euml_NamedElement, euml_Relations},
    associations={classes0, packages2, dependencies4, attributes6, generalizations12, operations8, realizations10, type14, target20, returnType17},
    generalizations={gen_euml_Package_NamedElement, gen_euml_Class_NamedElement, gen_euml_Dependecy_Relations, gen_euml_Attribute_NamedElement, gen_euml_Generalization_Relations, gen_euml_Realization_Relations, gen_euml_Operation_NamedElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)