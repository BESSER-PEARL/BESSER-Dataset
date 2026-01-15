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
AccessModifier: Enumeration = Enumeration(
    name="AccessModifier",
    literals={
            EnumerationLiteral(name="default"),
			EnumerationLiteral(name="private"),
			EnumerationLiteral(name="protected"),
			EnumerationLiteral(name="public")
    }
)

# Classes
classDiagram_ClassModel = Class(name="classDiagram::ClassModel")
classDiagram_Package = Class(name="classDiagram::Package")
classDiagram_ModelingConcept = Class(name="classDiagram::ModelingConcept", is_abstract=True)
ModelingConcept = Class(name="ModelingConcept")
classDiagram_Class = Class(name="classDiagram::Class")
Classifier = Class(name="Classifier")
classDiagram_Attribute = Class(name="classDiagram::Attribute")
classDiagram_Function = Class(name="classDiagram::Function")
classDiagram_Classifier = Class(name="classDiagram::Classifier", is_abstract=True)
classDiagram_Type = Class(name="classDiagram::Type")

# classDiagram_ClassModel class attributes and methods

# classDiagram_Package class attributes and methods

# classDiagram_ModelingConcept class attributes and methods
classDiagram_ModelingConcept_name: Property = Property(name="name", type=StringType)
classDiagram_ModelingConcept.attributes={classDiagram_ModelingConcept_name}

# ModelingConcept class attributes and methods

# classDiagram_Class class attributes and methods
classDiagram_Class_isAbstract: Property = Property(name="isAbstract", type=BooleanType)
classDiagram_Class_isStatic: Property = Property(name="isStatic", type=BooleanType)
classDiagram_Class_accessModifier: Property = Property(name="accessModifier", type=StringType)
classDiagram_Class.attributes={classDiagram_Class_isAbstract, classDiagram_Class_accessModifier, classDiagram_Class_isStatic}

# Classifier class attributes and methods

# classDiagram_Attribute class attributes and methods
classDiagram_Attribute_isStatic: Property = Property(name="isStatic", type=BooleanType)
classDiagram_Attribute_accessModifier: Property = Property(name="accessModifier", type=StringType)
classDiagram_Attribute.attributes={classDiagram_Attribute_isStatic, classDiagram_Attribute_accessModifier}

# classDiagram_Function class attributes and methods
classDiagram_Function_isAbstract: Property = Property(name="isAbstract", type=BooleanType)
classDiagram_Function_body: Property = Property(name="body", type=StringType)
classDiagram_Function_accessModifier: Property = Property(name="accessModifier", type=StringType)
classDiagram_Function_isStatic: Property = Property(name="isStatic", type=BooleanType)
classDiagram_Function.attributes={classDiagram_Function_body, classDiagram_Function_accessModifier, classDiagram_Function_isAbstract, classDiagram_Function_isStatic}

# classDiagram_Classifier class attributes and methods

# classDiagram_Type class attributes and methods

# Relationships
packages0: BinaryAssociation = BinaryAssociation(
    name="packages0",
    ends={
        Property(name="classDiagram_Package", type=classDiagram_ClassModel, multiplicity=Multiplicity(1, 1)),
        Property(name="classDiagram_ClassModel", type=classDiagram_Package, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
elements1: BinaryAssociation = BinaryAssociation(
    name="elements1",
    ends={
        Property(name="classDiagram_ModelingConcept", type=classDiagram_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="classDiagram_Package2", type=classDiagram_ModelingConcept, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
fields3: BinaryAssociation = BinaryAssociation(
    name="fields3",
    ends={
        Property(name="classDiagram_Attribute", type=classDiagram_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="classDiagram_Class", type=classDiagram_Attribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
supertypes5: BinaryAssociation = BinaryAssociation(
    name="supertypes5",
    ends={
        Property(name="Class", type=classDiagram_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="subtypes", type=classDiagram_Class, multiplicity=Multiplicity(0, 9999))
    }
)
subtypes7: BinaryAssociation = BinaryAssociation(
    name="subtypes7",
    ends={
        Property(name="Class8", type=classDiagram_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="supertypes", type=classDiagram_Class, multiplicity=Multiplicity(0, 9999))
    }
)
methods9: BinaryAssociation = BinaryAssociation(
    name="methods9",
    ends={
        Property(name="classDiagram_Function", type=classDiagram_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="classDiagram_Class10", type=classDiagram_Function, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type11: BinaryAssociation = BinaryAssociation(
    name="type11",
    ends={
        Property(name="classDiagram_Classifier", type=classDiagram_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="classDiagram_Attribute12", type=classDiagram_Classifier, multiplicity=Multiplicity(1, 1))
    }
)
returnType13: BinaryAssociation = BinaryAssociation(
    name="returnType13",
    ends={
        Property(name="classDiagram_Classifier15", type=classDiagram_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="classDiagram_Function14", type=classDiagram_Classifier, multiplicity=Multiplicity(1, 1))
    }
)
parameters16: BinaryAssociation = BinaryAssociation(
    name="parameters16",
    ends={
        Property(name="classDiagram_Attribute18", type=classDiagram_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="classDiagram_Function17", type=classDiagram_Attribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_classDiagram_Package_ModelingConcept = Generalization(general=ModelingConcept, specific=classDiagram_Package)
gen_classDiagram_Class_Classifier = Generalization(general=Classifier, specific=classDiagram_Class)
gen_classDiagram_Attribute_ModelingConcept = Generalization(general=ModelingConcept, specific=classDiagram_Attribute)
gen_classDiagram_Type_Classifier = Generalization(general=Classifier, specific=classDiagram_Type)
gen_classDiagram_Classifier_ModelingConcept = Generalization(general=ModelingConcept, specific=classDiagram_Classifier)
gen_classDiagram_Function_ModelingConcept = Generalization(general=ModelingConcept, specific=classDiagram_Function)

# Domain Model
domain_model = DomainModel(
    name="classDiagram",
    types={classDiagram_ClassModel, classDiagram_Package, classDiagram_ModelingConcept, ModelingConcept, classDiagram_Class, Classifier, classDiagram_Attribute, classDiagram_Function, classDiagram_Classifier, classDiagram_Type, AccessModifier},
    associations={packages0, elements1, fields3, supertypes5, subtypes7, methods9, type11, returnType13, parameters16},
    generalizations={gen_classDiagram_Package_ModelingConcept, gen_classDiagram_Class_Classifier, gen_classDiagram_Attribute_ModelingConcept, gen_classDiagram_Type_Classifier, gen_classDiagram_Classifier_ModelingConcept, gen_classDiagram_Function_ModelingConcept},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)