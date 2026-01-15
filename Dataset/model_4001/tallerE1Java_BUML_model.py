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
            EnumerationLiteral(name="private"),
			EnumerationLiteral(name="public")
    }
)

# Classes
tallerE1Java_Program = Class(name="tallerE1Java::Program")
tallerE1Java_Package = Class(name="tallerE1Java::Package")
tallerE1Java_PrimitiveType = Class(name="tallerE1Java::PrimitiveType")
tallerE1Java_Container = Class(name="tallerE1Java::Container")
tallerE1Java_Class = Class(name="tallerE1Java::Class", is_abstract=True)
Type = Class(name="Type")
tallerE1Java_Attribute = Class(name="tallerE1Java::Attribute")
tallerE1Java_Type = Class(name="tallerE1Java::Type", is_abstract=True)
tallerE1Java_Annotation = Class(name="tallerE1Java::Annotation")
tallerE1Java_EntityClass = Class(name="tallerE1Java::EntityClass")
Class_ = Class(name="Class")
tallerE1Java_DAOClass = Class(name="tallerE1Java::DAOClass")
tallerE1Java_TestClass = Class(name="tallerE1Java::TestClass")

# tallerE1Java_Program class attributes and methods

# tallerE1Java_Package class attributes and methods
tallerE1Java_Package_name: Property = Property(name="name", type=StringType)
tallerE1Java_Package.attributes={tallerE1Java_Package_name}

# tallerE1Java_PrimitiveType class attributes and methods

# tallerE1Java_Container class attributes and methods
tallerE1Java_Container_type: Property = Property(name="type", type=StringType)
tallerE1Java_Container.attributes={tallerE1Java_Container_type}

# tallerE1Java_Class class attributes and methods

# Type class attributes and methods

# tallerE1Java_Attribute class attributes and methods
tallerE1Java_Attribute_name: Property = Property(name="name", type=StringType)
tallerE1Java_Attribute_visibility: Property = Property(name="visibility", type=StringType)
tallerE1Java_Attribute.attributes={tallerE1Java_Attribute_visibility, tallerE1Java_Attribute_name}

# tallerE1Java_Type class attributes and methods
tallerE1Java_Type_name: Property = Property(name="name", type=StringType)
tallerE1Java_Type.attributes={tallerE1Java_Type_name}

# tallerE1Java_Annotation class attributes and methods
tallerE1Java_Annotation_type: Property = Property(name="type", type=StringType)
tallerE1Java_Annotation_content: Property = Property(name="content", type=StringType)
tallerE1Java_Annotation.attributes={tallerE1Java_Annotation_type, tallerE1Java_Annotation_content}

# tallerE1Java_EntityClass class attributes and methods

# Class class attributes and methods

# tallerE1Java_DAOClass class attributes and methods

# tallerE1Java_TestClass class attributes and methods

# Relationships
packages0: BinaryAssociation = BinaryAssociation(
    name="packages0",
    ends={
        Property(name="tallerE1Java_Package", type=tallerE1Java_Program, multiplicity=Multiplicity(1, 1)),
        Property(name="tallerE1Java_Program", type=tallerE1Java_Package, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
primitiveTypes1: BinaryAssociation = BinaryAssociation(
    name="primitiveTypes1",
    ends={
        Property(name="tallerE1Java_PrimitiveType", type=tallerE1Java_Program, multiplicity=Multiplicity(1, 1)),
        Property(name="tallerE1Java_Program2", type=tallerE1Java_PrimitiveType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
containerTypes3: BinaryAssociation = BinaryAssociation(
    name="containerTypes3",
    ends={
        Property(name="tallerE1Java_Container", type=tallerE1Java_Program, multiplicity=Multiplicity(1, 1)),
        Property(name="tallerE1Java_Program4", type=tallerE1Java_Container, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
classes5: BinaryAssociation = BinaryAssociation(
    name="classes5",
    ends={
        Property(name="tallerE1Java_Class", type=tallerE1Java_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="tallerE1Java_Package6", type=tallerE1Java_Class, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
attributes7: BinaryAssociation = BinaryAssociation(
    name="attributes7",
    ends={
        Property(name="tallerE1Java_Attribute", type=tallerE1Java_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="tallerE1Java_Class8", type=tallerE1Java_Attribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type9: BinaryAssociation = BinaryAssociation(
    name="type9",
    ends={
        Property(name="tallerE1Java_Type", type=tallerE1Java_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="tallerE1Java_Attribute10", type=tallerE1Java_Type, multiplicity=Multiplicity(0, 1))
    }
)
annotations11: BinaryAssociation = BinaryAssociation(
    name="annotations11",
    ends={
        Property(name="tallerE1Java_Annotation", type=tallerE1Java_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="tallerE1Java_Attribute12", type=tallerE1Java_Annotation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
param13: BinaryAssociation = BinaryAssociation(
    name="param13",
    ends={
        Property(name="tallerE1Java_Type15", type=tallerE1Java_Container, multiplicity=Multiplicity(1, 1)),
        Property(name="tallerE1Java_Container14", type=tallerE1Java_Type, multiplicity=Multiplicity(0, 1))
    }
)
entities16: BinaryAssociation = BinaryAssociation(
    name="entities16",
    ends={
        Property(name="tallerE1Java_EntityClass", type=tallerE1Java_DAOClass, multiplicity=Multiplicity(1, 1)),
        Property(name="tallerE1Java_DAOClass", type=tallerE1Java_EntityClass, multiplicity=Multiplicity(0, 9999))
    }
)
dao17: BinaryAssociation = BinaryAssociation(
    name="dao17",
    ends={
        Property(name="tallerE1Java_DAOClass18", type=tallerE1Java_TestClass, multiplicity=Multiplicity(1, 1)),
        Property(name="tallerE1Java_TestClass", type=tallerE1Java_DAOClass, multiplicity=Multiplicity(0, 1))
    }
)
entity19: BinaryAssociation = BinaryAssociation(
    name="entity19",
    ends={
        Property(name="tallerE1Java_EntityClass21", type=tallerE1Java_TestClass, multiplicity=Multiplicity(1, 1)),
        Property(name="tallerE1Java_TestClass20", type=tallerE1Java_EntityClass, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_tallerE1Java_Class_Type = Generalization(general=Type, specific=tallerE1Java_Class)
gen_tallerE1Java_PrimitiveType_Type = Generalization(general=Type, specific=tallerE1Java_PrimitiveType)
gen_tallerE1Java_Container_Type = Generalization(general=Type, specific=tallerE1Java_Container)
gen_tallerE1Java_EntityClass_Class = Generalization(general=Class_, specific=tallerE1Java_EntityClass)
gen_tallerE1Java_DAOClass_Class = Generalization(general=Class_, specific=tallerE1Java_DAOClass)
gen_tallerE1Java_TestClass_Class = Generalization(general=Class_, specific=tallerE1Java_TestClass)

# Domain Model
domain_model = DomainModel(
    name="tallerE1Java",
    types={tallerE1Java_Program, tallerE1Java_Package, tallerE1Java_PrimitiveType, tallerE1Java_Container, tallerE1Java_Class, Type, tallerE1Java_Attribute, tallerE1Java_Type, tallerE1Java_Annotation, tallerE1Java_EntityClass, Class_, tallerE1Java_DAOClass, tallerE1Java_TestClass, Visibility},
    associations={packages0, primitiveTypes1, containerTypes3, classes5, attributes7, type9, annotations11, param13, entities16, dao17, entity19},
    generalizations={gen_tallerE1Java_Class_Type, gen_tallerE1Java_PrimitiveType_Type, gen_tallerE1Java_Container_Type, gen_tallerE1Java_EntityClass_Class, gen_tallerE1Java_DAOClass_Class, gen_tallerE1Java_TestClass_Class},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)