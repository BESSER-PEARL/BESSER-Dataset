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
classdiagram_ClassDiagram = Class(name="classdiagram::ClassDiagram")
classdiagram_Class = Class(name="classdiagram::Class")
classdiagram_Dependency = Class(name="classdiagram::Dependency")
classdiagram_Association = Class(name="classdiagram::Association")
NamedElement = Class(name="NamedElement")
classdiagram_Attribute = Class(name="classdiagram::Attribute")
classdiagram_Operation = Class(name="classdiagram::Operation")
TypedElement = Class(name="TypedElement")
classdiagram_NamedElement = Class(name="classdiagram::NamedElement", is_abstract=True)
classdiagram_TypedElement = Class(name="classdiagram::TypedElement", is_abstract=True)

# classdiagram_ClassDiagram class attributes and methods

# classdiagram_Class class attributes and methods

# classdiagram_Dependency class attributes and methods
classdiagram_Dependency_name: Property = Property(name="name", type=StringType)
classdiagram_Dependency.attributes={classdiagram_Dependency_name}

# classdiagram_Association class attributes and methods

# NamedElement class attributes and methods

# classdiagram_Attribute class attributes and methods

# classdiagram_Operation class attributes and methods

# TypedElement class attributes and methods

# classdiagram_NamedElement class attributes and methods
classdiagram_NamedElement_name: Property = Property(name="name", type=StringType)
classdiagram_NamedElement.attributes={classdiagram_NamedElement_name}

# classdiagram_TypedElement class attributes and methods
classdiagram_TypedElement_public: Property = Property(name="public", type=BooleanType)
classdiagram_TypedElement.attributes={classdiagram_TypedElement_public}

# Relationships
classes0: BinaryAssociation = BinaryAssociation(
    name="classes0",
    ends={
        Property(name="classdiagram_Class", type=classdiagram_ClassDiagram, multiplicity=Multiplicity(1, 1)),
        Property(name="classdiagram_ClassDiagram", type=classdiagram_Class, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dependencies1: BinaryAssociation = BinaryAssociation(
    name="dependencies1",
    ends={
        Property(name="classdiagram_Dependency", type=classdiagram_ClassDiagram, multiplicity=Multiplicity(1, 1)),
        Property(name="classdiagram_ClassDiagram2", type=classdiagram_Dependency, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
associations3: BinaryAssociation = BinaryAssociation(
    name="associations3",
    ends={
        Property(name="classdiagram_Association", type=classdiagram_ClassDiagram, multiplicity=Multiplicity(1, 1)),
        Property(name="classdiagram_ClassDiagram4", type=classdiagram_Association, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedAttributes5: BinaryAssociation = BinaryAssociation(
    name="ownedAttributes5",
    ends={
        Property(name="Attribute", type=classdiagram_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="owner", type=classdiagram_Attribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedOperations6: BinaryAssociation = BinaryAssociation(
    name="ownedOperations6",
    ends={
        Property(name="Operation", type=classdiagram_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="owner7", type=classdiagram_Operation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dependenciesAsDependee8: BinaryAssociation = BinaryAssociation(
    name="dependenciesAsDependee8",
    ends={
        Property(name="Dependency", type=classdiagram_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="dependee", type=classdiagram_Dependency, multiplicity=Multiplicity(0, 9999))
    }
)
dependenciesAsDepender9: BinaryAssociation = BinaryAssociation(
    name="dependenciesAsDepender9",
    ends={
        Property(name="Dependency10", type=classdiagram_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="depender", type=classdiagram_Dependency, multiplicity=Multiplicity(0, 9999))
    }
)
nestedIn12: BinaryAssociation = BinaryAssociation(
    name="nestedIn12",
    ends={
        Property(name="Class", type=classdiagram_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="nested", type=classdiagram_Class, multiplicity=Multiplicity(0, 1))
    }
)
nested14: BinaryAssociation = BinaryAssociation(
    name="nested14",
    ends={
        Property(name="Class15", type=classdiagram_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="nestedIn", type=classdiagram_Class, multiplicity=Multiplicity(0, 9999))
    }
)
superclass17: BinaryAssociation = BinaryAssociation(
    name="superclass17",
    ends={
        Property(name="Class18", type=classdiagram_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="subclasses", type=classdiagram_Class, multiplicity=Multiplicity(0, 1))
    }
)
subclasses20: BinaryAssociation = BinaryAssociation(
    name="subclasses20",
    ends={
        Property(name="Class21", type=classdiagram_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="superclass", type=classdiagram_Class, multiplicity=Multiplicity(0, 9999))
    }
)
associationsAsSource22: BinaryAssociation = BinaryAssociation(
    name="associationsAsSource22",
    ends={
        Property(name="Association", type=classdiagram_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="source", type=classdiagram_Association, multiplicity=Multiplicity(0, 9999))
    }
)
associationsAsTarget23: BinaryAssociation = BinaryAssociation(
    name="associationsAsTarget23",
    ends={
        Property(name="Association24", type=classdiagram_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="target", type=classdiagram_Association, multiplicity=Multiplicity(0, 9999))
    }
)
owner25: BinaryAssociation = BinaryAssociation(
    name="owner25",
    ends={
        Property(name="Class26", type=classdiagram_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedAttributes", type=classdiagram_Class, multiplicity=Multiplicity(1, 1))
    }
)
owner27: BinaryAssociation = BinaryAssociation(
    name="owner27",
    ends={
        Property(name="Class28", type=classdiagram_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedOperations", type=classdiagram_Class, multiplicity=Multiplicity(1, 1))
    }
)
dependee29: BinaryAssociation = BinaryAssociation(
    name="dependee29",
    ends={
        Property(name="Class30", type=classdiagram_Dependency, multiplicity=Multiplicity(1, 1)),
        Property(name="dependenciesAsDependee", type=classdiagram_Class, multiplicity=Multiplicity(1, 1))
    }
)
depender31: BinaryAssociation = BinaryAssociation(
    name="depender31",
    ends={
        Property(name="Class32", type=classdiagram_Dependency, multiplicity=Multiplicity(1, 1)),
        Property(name="dependenciesAsDepender", type=classdiagram_Class, multiplicity=Multiplicity(1, 1))
    }
)
type33: BinaryAssociation = BinaryAssociation(
    name="type33",
    ends={
        Property(name="classdiagram_Class34", type=classdiagram_TypedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="classdiagram_TypedElement", type=classdiagram_Class, multiplicity=Multiplicity(1, 1))
    }
)
source35: BinaryAssociation = BinaryAssociation(
    name="source35",
    ends={
        Property(name="Class36", type=classdiagram_Association, multiplicity=Multiplicity(1, 1)),
        Property(name="associationsAsSource", type=classdiagram_Class, multiplicity=Multiplicity(1, 1))
    }
)
target37: BinaryAssociation = BinaryAssociation(
    name="target37",
    ends={
        Property(name="Class38", type=classdiagram_Association, multiplicity=Multiplicity(1, 1)),
        Property(name="associationsAsTarget", type=classdiagram_Class, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_classdiagram_Class_NamedElement = Generalization(general=NamedElement, specific=classdiagram_Class)
gen_classdiagram_Attribute_TypedElement = Generalization(general=TypedElement, specific=classdiagram_Attribute)
gen_classdiagram_Operation_TypedElement = Generalization(general=TypedElement, specific=classdiagram_Operation)
gen_classdiagram_TypedElement_NamedElement = Generalization(general=NamedElement, specific=classdiagram_TypedElement)
gen_classdiagram_Association_NamedElement = Generalization(general=NamedElement, specific=classdiagram_Association)

# Domain Model
domain_model = DomainModel(
    name="classdiagram",
    types={classdiagram_ClassDiagram, classdiagram_Class, classdiagram_Dependency, classdiagram_Association, NamedElement, classdiagram_Attribute, classdiagram_Operation, TypedElement, classdiagram_NamedElement, classdiagram_TypedElement},
    associations={classes0, dependencies1, associations3, ownedAttributes5, ownedOperations6, dependenciesAsDependee8, dependenciesAsDepender9, nestedIn12, nested14, superclass17, subclasses20, associationsAsSource22, associationsAsTarget23, owner25, owner27, dependee29, depender31, type33, source35, target37},
    generalizations={gen_classdiagram_Class_NamedElement, gen_classdiagram_Attribute_TypedElement, gen_classdiagram_Operation_TypedElement, gen_classdiagram_TypedElement_NamedElement, gen_classdiagram_Association_NamedElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)