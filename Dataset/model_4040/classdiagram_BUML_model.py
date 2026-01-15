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
classdiagram_DataType = Class(name="classdiagram::DataType")
classdiagram_Composition = Class(name="classdiagram::Composition")
Typeable = Class(name="Typeable")
classdiagram_Attribute = Class(name="classdiagram::Attribute")
classdiagram_Operation = Class(name="classdiagram::Operation")
TypedElement = Class(name="TypedElement")
classdiagram_NamedElement = Class(name="classdiagram::NamedElement", is_abstract=True)
classdiagram_Typeable = Class(name="classdiagram::Typeable", is_abstract=True)
classdiagram_TypedElement = Class(name="classdiagram::TypedElement", is_abstract=True)
NamedElement = Class(name="NamedElement")

# classdiagram_ClassDiagram class attributes and methods

# classdiagram_Class class attributes and methods

# classdiagram_Dependency class attributes and methods
classdiagram_Dependency_name: Property = Property(name="name", type=StringType)
classdiagram_Dependency.attributes={classdiagram_Dependency_name}

# classdiagram_Association class attributes and methods
classdiagram_Association_multiplicity: Property = Property(name="multiplicity", type=StringType)
classdiagram_Association.attributes={classdiagram_Association_multiplicity}

# classdiagram_DataType class attributes and methods

# classdiagram_Composition class attributes and methods
classdiagram_Composition_multiplicity: Property = Property(name="multiplicity", type=StringType)
classdiagram_Composition.attributes={classdiagram_Composition_multiplicity}

# Typeable class attributes and methods

# classdiagram_Attribute class attributes and methods

# classdiagram_Operation class attributes and methods

# TypedElement class attributes and methods

# classdiagram_NamedElement class attributes and methods
classdiagram_NamedElement_name: Property = Property(name="name", type=StringType)
classdiagram_NamedElement.attributes={classdiagram_NamedElement_name}

# classdiagram_Typeable class attributes and methods

# classdiagram_TypedElement class attributes and methods
classdiagram_TypedElement_public: Property = Property(name="public", type=BooleanType)
classdiagram_TypedElement.attributes={classdiagram_TypedElement_public}

# NamedElement class attributes and methods

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
datatypes5: BinaryAssociation = BinaryAssociation(
    name="datatypes5",
    ends={
        Property(name="classdiagram_DataType", type=classdiagram_ClassDiagram, multiplicity=Multiplicity(1, 1)),
        Property(name="classdiagram_ClassDiagram6", type=classdiagram_DataType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
compositions7: BinaryAssociation = BinaryAssociation(
    name="compositions7",
    ends={
        Property(name="classdiagram_Composition", type=classdiagram_ClassDiagram, multiplicity=Multiplicity(1, 1)),
        Property(name="classdiagram_ClassDiagram8", type=classdiagram_Composition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedAttributes9: BinaryAssociation = BinaryAssociation(
    name="ownedAttributes9",
    ends={
        Property(name="Attribute", type=classdiagram_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="owner", type=classdiagram_Attribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedOperations10: BinaryAssociation = BinaryAssociation(
    name="ownedOperations10",
    ends={
        Property(name="Operation", type=classdiagram_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="owner11", type=classdiagram_Operation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dependenciesAsDependee12: BinaryAssociation = BinaryAssociation(
    name="dependenciesAsDependee12",
    ends={
        Property(name="Dependency", type=classdiagram_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="dependee", type=classdiagram_Dependency, multiplicity=Multiplicity(0, 9999))
    }
)
subclasses24: BinaryAssociation = BinaryAssociation(
    name="subclasses24",
    ends={
        Property(name="Class25", type=classdiagram_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="superclass", type=classdiagram_Class, multiplicity=Multiplicity(0, 9999))
    }
)
associationsAsSource26: BinaryAssociation = BinaryAssociation(
    name="associationsAsSource26",
    ends={
        Property(name="Association", type=classdiagram_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="source", type=classdiagram_Association, multiplicity=Multiplicity(0, 9999))
    }
)
associationsAsTarget27: BinaryAssociation = BinaryAssociation(
    name="associationsAsTarget27",
    ends={
        Property(name="Association28", type=classdiagram_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="target", type=classdiagram_Association, multiplicity=Multiplicity(0, 9999))
    }
)
compositionsAsConstituent29: BinaryAssociation = BinaryAssociation(
    name="compositionsAsConstituent29",
    ends={
        Property(name="Composition", type=classdiagram_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="constituent", type=classdiagram_Composition, multiplicity=Multiplicity(0, 9999))
    }
)
compositionsAsComposite30: BinaryAssociation = BinaryAssociation(
    name="compositionsAsComposite30",
    ends={
        Property(name="Composition31", type=classdiagram_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="composite", type=classdiagram_Composition, multiplicity=Multiplicity(0, 9999))
    }
)
owner32: BinaryAssociation = BinaryAssociation(
    name="owner32",
    ends={
        Property(name="Class33", type=classdiagram_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedAttributes", type=classdiagram_Class, multiplicity=Multiplicity(1, 1))
    }
)
owner34: BinaryAssociation = BinaryAssociation(
    name="owner34",
    ends={
        Property(name="Class35", type=classdiagram_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedOperations", type=classdiagram_Class, multiplicity=Multiplicity(1, 1))
    }
)
parameterTypes36: BinaryAssociation = BinaryAssociation(
    name="parameterTypes36",
    ends={
        Property(name="classdiagram_Typeable", type=classdiagram_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="classdiagram_Operation", type=classdiagram_Typeable, multiplicity=Multiplicity(0, 9999))
    }
)
dependenciesAsDepender13: BinaryAssociation = BinaryAssociation(
    name="dependenciesAsDepender13",
    ends={
        Property(name="Dependency14", type=classdiagram_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="depender", type=classdiagram_Dependency, multiplicity=Multiplicity(0, 9999))
    }
)
nestedIn16: BinaryAssociation = BinaryAssociation(
    name="nestedIn16",
    ends={
        Property(name="Class", type=classdiagram_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="nested", type=classdiagram_Class, multiplicity=Multiplicity(0, 1))
    }
)
nested18: BinaryAssociation = BinaryAssociation(
    name="nested18",
    ends={
        Property(name="Class19", type=classdiagram_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="nestedIn", type=classdiagram_Class, multiplicity=Multiplicity(0, 9999))
    }
)
superclass21: BinaryAssociation = BinaryAssociation(
    name="superclass21",
    ends={
        Property(name="Class22", type=classdiagram_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="subclasses", type=classdiagram_Class, multiplicity=Multiplicity(0, 1))
    }
)
source43: BinaryAssociation = BinaryAssociation(
    name="source43",
    ends={
        Property(name="Class44", type=classdiagram_Association, multiplicity=Multiplicity(1, 1)),
        Property(name="associationsAsSource", type=classdiagram_Class, multiplicity=Multiplicity(1, 1))
    }
)
target45: BinaryAssociation = BinaryAssociation(
    name="target45",
    ends={
        Property(name="Class46", type=classdiagram_Association, multiplicity=Multiplicity(1, 1)),
        Property(name="associationsAsTarget", type=classdiagram_Class, multiplicity=Multiplicity(1, 1))
    }
)
constituent47: BinaryAssociation = BinaryAssociation(
    name="constituent47",
    ends={
        Property(name="Class48", type=classdiagram_Composition, multiplicity=Multiplicity(1, 1)),
        Property(name="compositionsAsConstituent", type=classdiagram_Class, multiplicity=Multiplicity(1, 1))
    }
)
composite49: BinaryAssociation = BinaryAssociation(
    name="composite49",
    ends={
        Property(name="Class50", type=classdiagram_Composition, multiplicity=Multiplicity(1, 1)),
        Property(name="compositionsAsComposite", type=classdiagram_Class, multiplicity=Multiplicity(1, 1))
    }
)
dependee37: BinaryAssociation = BinaryAssociation(
    name="dependee37",
    ends={
        Property(name="Class38", type=classdiagram_Dependency, multiplicity=Multiplicity(1, 1)),
        Property(name="dependenciesAsDependee", type=classdiagram_Class, multiplicity=Multiplicity(1, 1))
    }
)
depender39: BinaryAssociation = BinaryAssociation(
    name="depender39",
    ends={
        Property(name="Class40", type=classdiagram_Dependency, multiplicity=Multiplicity(1, 1)),
        Property(name="dependenciesAsDepender", type=classdiagram_Class, multiplicity=Multiplicity(1, 1))
    }
)
type41: BinaryAssociation = BinaryAssociation(
    name="type41",
    ends={
        Property(name="classdiagram_Typeable42", type=classdiagram_TypedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="classdiagram_TypedElement", type=classdiagram_Typeable, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_classdiagram_Class_Typeable = Generalization(general=Typeable, specific=classdiagram_Class)
gen_classdiagram_Attribute_TypedElement = Generalization(general=TypedElement, specific=classdiagram_Attribute)
gen_classdiagram_Operation_TypedElement = Generalization(general=TypedElement, specific=classdiagram_Operation)
gen_classdiagram_Typeable_NamedElement = Generalization(general=NamedElement, specific=classdiagram_Typeable)
gen_classdiagram_DataType_Typeable = Generalization(general=Typeable, specific=classdiagram_DataType)
gen_classdiagram_Composition_NamedElement = Generalization(general=NamedElement, specific=classdiagram_Composition)
gen_classdiagram_TypedElement_NamedElement = Generalization(general=NamedElement, specific=classdiagram_TypedElement)
gen_classdiagram_Association_NamedElement = Generalization(general=NamedElement, specific=classdiagram_Association)

# Domain Model
domain_model = DomainModel(
    name="classdiagram",
    types={classdiagram_ClassDiagram, classdiagram_Class, classdiagram_Dependency, classdiagram_Association, classdiagram_DataType, classdiagram_Composition, Typeable, classdiagram_Attribute, classdiagram_Operation, TypedElement, classdiagram_NamedElement, classdiagram_Typeable, classdiagram_TypedElement, NamedElement},
    associations={classes0, dependencies1, associations3, datatypes5, compositions7, ownedAttributes9, ownedOperations10, dependenciesAsDependee12, subclasses24, associationsAsSource26, associationsAsTarget27, compositionsAsConstituent29, compositionsAsComposite30, owner32, owner34, parameterTypes36, dependenciesAsDepender13, nestedIn16, nested18, superclass21, source43, target45, constituent47, composite49, dependee37, depender39, type41},
    generalizations={gen_classdiagram_Class_Typeable, gen_classdiagram_Attribute_TypedElement, gen_classdiagram_Operation_TypedElement, gen_classdiagram_Typeable_NamedElement, gen_classdiagram_DataType_Typeable, gen_classdiagram_Composition_NamedElement, gen_classdiagram_TypedElement_NamedElement, gen_classdiagram_Association_NamedElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)