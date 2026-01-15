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
classDiagram_Type = Class(name="classDiagram::Type")
classDiagram_ModelingConcept = Class(name="classDiagram::ModelingConcept", is_abstract=True)
ModelingConcept = Class(name="ModelingConcept")
classDiagram_Class = Class(name="classDiagram::Class")
Classifier = Class(name="Classifier")
classDiagram_Method = Class(name="classDiagram::Method")
classDiagram_ElementType = Class(name="classDiagram::ElementType")
classDiagram_Classifier = Class(name="classDiagram::Classifier", is_abstract=True)
classDiagram_Attribute = Class(name="classDiagram::Attribute")

# classDiagram_ClassModel class attributes and methods

# classDiagram_Package class attributes and methods

# classDiagram_Type class attributes and methods

# classDiagram_ModelingConcept class attributes and methods
classDiagram_ModelingConcept_name: Property = Property(name="name", type=StringType)
classDiagram_ModelingConcept.attributes={classDiagram_ModelingConcept_name}

# ModelingConcept class attributes and methods

# classDiagram_Class class attributes and methods
classDiagram_Class_isStatic: Property = Property(name="isStatic", type=BooleanType)
classDiagram_Class_accessModifier: Property = Property(name="accessModifier", type=StringType)
classDiagram_Class_isAbstract: Property = Property(name="isAbstract", type=BooleanType)
classDiagram_Class.attributes={classDiagram_Class_isAbstract, classDiagram_Class_accessModifier, classDiagram_Class_isStatic}

# Classifier class attributes and methods

# classDiagram_Method class attributes and methods
classDiagram_Method_accessModifier: Property = Property(name="accessModifier", type=StringType)
classDiagram_Method_isStatic: Property = Property(name="isStatic", type=BooleanType)
classDiagram_Method_isAbstract: Property = Property(name="isAbstract", type=BooleanType)
classDiagram_Method_body: Property = Property(name="body", type=StringType)
classDiagram_Method.attributes={classDiagram_Method_isStatic, classDiagram_Method_body, classDiagram_Method_accessModifier, classDiagram_Method_isAbstract}

# classDiagram_ElementType class attributes and methods
classDiagram_ElementType_isCollection: Property = Property(name="isCollection", type=BooleanType)
classDiagram_ElementType.attributes={classDiagram_ElementType_isCollection}

# classDiagram_Classifier class attributes and methods

# classDiagram_Attribute class attributes and methods
classDiagram_Attribute_isStatic: Property = Property(name="isStatic", type=BooleanType)
classDiagram_Attribute_accessModifier: Property = Property(name="accessModifier", type=StringType)
classDiagram_Attribute.attributes={classDiagram_Attribute_accessModifier, classDiagram_Attribute_isStatic}

# Relationships
packages0: BinaryAssociation = BinaryAssociation(
    name="packages0",
    ends={
        Property(name="classDiagram_Package", type=classDiagram_ClassModel, multiplicity=Multiplicity(1, 1)),
        Property(name="classDiagram_ClassModel", type=classDiagram_Package, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
types1: BinaryAssociation = BinaryAssociation(
    name="types1",
    ends={
        Property(name="classDiagram_Type", type=classDiagram_ClassModel, multiplicity=Multiplicity(1, 1)),
        Property(name="classDiagram_ClassModel2", type=classDiagram_Type, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elements3: BinaryAssociation = BinaryAssociation(
    name="elements3",
    ends={
        Property(name="classDiagram_ModelingConcept", type=classDiagram_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="classDiagram_Package4", type=classDiagram_ModelingConcept, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
package6: BinaryAssociation = BinaryAssociation(
    name="package6",
    ends={
        Property(name="Package", type=classDiagram_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="subpackages", type=classDiagram_Package, multiplicity=Multiplicity(0, 1))
    }
)
subpackages8: BinaryAssociation = BinaryAssociation(
    name="subpackages8",
    ends={
        Property(name="Package9", type=classDiagram_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="package", type=classDiagram_Package, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
classes10: BinaryAssociation = BinaryAssociation(
    name="classes10",
    ends={
        Property(name="classDiagram_Class", type=classDiagram_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="classDiagram_Package11", type=classDiagram_Class, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
methods19: BinaryAssociation = BinaryAssociation(
    name="methods19",
    ends={
        Property(name="classDiagram_Method", type=classDiagram_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="classDiagram_Class20", type=classDiagram_Method, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type21: BinaryAssociation = BinaryAssociation(
    name="type21",
    ends={
        Property(name="classDiagram_ElementType", type=classDiagram_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="classDiagram_Attribute22", type=classDiagram_ElementType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
returnType23: BinaryAssociation = BinaryAssociation(
    name="returnType23",
    ends={
        Property(name="classDiagram_ElementType25", type=classDiagram_Method, multiplicity=Multiplicity(1, 1)),
        Property(name="classDiagram_Method24", type=classDiagram_ElementType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parameters26: BinaryAssociation = BinaryAssociation(
    name="parameters26",
    ends={
        Property(name="classDiagram_Attribute28", type=classDiagram_Method, multiplicity=Multiplicity(1, 1)),
        Property(name="classDiagram_Method27", type=classDiagram_Attribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type29: BinaryAssociation = BinaryAssociation(
    name="type29",
    ends={
        Property(name="classDiagram_Classifier", type=classDiagram_ElementType, multiplicity=Multiplicity(1, 1)),
        Property(name="classDiagram_ElementType30", type=classDiagram_Classifier, multiplicity=Multiplicity(1, 1))
    }
)
fields12: BinaryAssociation = BinaryAssociation(
    name="fields12",
    ends={
        Property(name="classDiagram_Attribute", type=classDiagram_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="classDiagram_Class13", type=classDiagram_Attribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
supertypes15: BinaryAssociation = BinaryAssociation(
    name="supertypes15",
    ends={
        Property(name="Class", type=classDiagram_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="subtypes", type=classDiagram_Class, multiplicity=Multiplicity(0, 9999))
    }
)
subtypes17: BinaryAssociation = BinaryAssociation(
    name="subtypes17",
    ends={
        Property(name="Class18", type=classDiagram_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="supertypes", type=classDiagram_Class, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_classDiagram_Package_ModelingConcept = Generalization(general=ModelingConcept, specific=classDiagram_Package)
gen_classDiagram_Class_Classifier = Generalization(general=Classifier, specific=classDiagram_Class)
gen_classDiagram_Attribute_ModelingConcept = Generalization(general=ModelingConcept, specific=classDiagram_Attribute)
gen_classDiagram_Type_Classifier = Generalization(general=Classifier, specific=classDiagram_Type)
gen_classDiagram_Classifier_ModelingConcept = Generalization(general=ModelingConcept, specific=classDiagram_Classifier)
gen_classDiagram_Method_ModelingConcept = Generalization(general=ModelingConcept, specific=classDiagram_Method)

# Domain Model
domain_model = DomainModel(
    name="classDiagram",
    types={classDiagram_ClassModel, classDiagram_Package, classDiagram_Type, classDiagram_ModelingConcept, ModelingConcept, classDiagram_Class, Classifier, classDiagram_Method, classDiagram_ElementType, classDiagram_Classifier, classDiagram_Attribute, AccessModifier},
    associations={packages0, types1, elements3, package6, subpackages8, classes10, methods19, type21, returnType23, parameters26, type29, fields12, supertypes15, subtypes17},
    generalizations={gen_classDiagram_Package_ModelingConcept, gen_classDiagram_Class_Classifier, gen_classDiagram_Attribute_ModelingConcept, gen_classDiagram_Type_Classifier, gen_classDiagram_Classifier_ModelingConcept, gen_classDiagram_Method_ModelingConcept},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)