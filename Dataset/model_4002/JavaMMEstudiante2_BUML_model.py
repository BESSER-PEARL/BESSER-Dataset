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
JavaMM_PrimitiveType = Class(name="JavaMM::PrimitiveType")
JavaMM_Container = Class(name="JavaMM::Container")
JavaMM_Class = Class(name="JavaMM::Class", is_abstract=True)
JavaMM_Program = Class(name="JavaMM::Program")
JavaMM_Package = Class(name="JavaMM::Package")
Type = Class(name="Type")
JavaMM_Attribute = Class(name="JavaMM::Attribute")
JavaMM_Type = Class(name="JavaMM::Type", is_abstract=True)
JavaMM_Annotation = Class(name="JavaMM::Annotation")
JavaMM_EntityClass = Class(name="JavaMM::EntityClass")
Class_ = Class(name="Class")
JavaMM_DAOClass = Class(name="JavaMM::DAOClass")
JavaMM_TestClass = Class(name="JavaMM::TestClass")

# JavaMM_PrimitiveType class attributes and methods

# JavaMM_Container class attributes and methods
JavaMM_Container_type: Property = Property(name="type", type=StringType)
JavaMM_Container.attributes={JavaMM_Container_type}

# JavaMM_Class class attributes and methods

# JavaMM_Program class attributes and methods

# JavaMM_Package class attributes and methods
JavaMM_Package_name: Property = Property(name="name", type=StringType)
JavaMM_Package.attributes={JavaMM_Package_name}

# Type class attributes and methods

# JavaMM_Attribute class attributes and methods
JavaMM_Attribute_name: Property = Property(name="name", type=StringType)
JavaMM_Attribute_visibility: Property = Property(name="visibility", type=StringType)
JavaMM_Attribute.attributes={JavaMM_Attribute_visibility, JavaMM_Attribute_name}

# JavaMM_Type class attributes and methods
JavaMM_Type_name: Property = Property(name="name", type=StringType)
JavaMM_Type.attributes={JavaMM_Type_name}

# JavaMM_Annotation class attributes and methods
JavaMM_Annotation_type: Property = Property(name="type", type=StringType)
JavaMM_Annotation_content: Property = Property(name="content", type=StringType)
JavaMM_Annotation.attributes={JavaMM_Annotation_type, JavaMM_Annotation_content}

# JavaMM_EntityClass class attributes and methods

# Class class attributes and methods

# JavaMM_DAOClass class attributes and methods

# JavaMM_TestClass class attributes and methods

# Relationships
primitiveTypes1: BinaryAssociation = BinaryAssociation(
    name="primitiveTypes1",
    ends={
        Property(name="JavaMM_PrimitiveType", type=JavaMM_Program, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaMM_Program2", type=JavaMM_PrimitiveType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
containerTypes3: BinaryAssociation = BinaryAssociation(
    name="containerTypes3",
    ends={
        Property(name="JavaMM_Container", type=JavaMM_Program, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaMM_Program4", type=JavaMM_Container, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
classes5: BinaryAssociation = BinaryAssociation(
    name="classes5",
    ends={
        Property(name="JavaMM_Class", type=JavaMM_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaMM_Package6", type=JavaMM_Class, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
packages0: BinaryAssociation = BinaryAssociation(
    name="packages0",
    ends={
        Property(name="JavaMM_Package", type=JavaMM_Program, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaMM_Program", type=JavaMM_Package, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
attributes7: BinaryAssociation = BinaryAssociation(
    name="attributes7",
    ends={
        Property(name="JavaMM_Attribute", type=JavaMM_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaMM_Class8", type=JavaMM_Attribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type9: BinaryAssociation = BinaryAssociation(
    name="type9",
    ends={
        Property(name="JavaMM_Type", type=JavaMM_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaMM_Attribute10", type=JavaMM_Type, multiplicity=Multiplicity(0, 1))
    }
)
annotations11: BinaryAssociation = BinaryAssociation(
    name="annotations11",
    ends={
        Property(name="JavaMM_Annotation", type=JavaMM_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaMM_Attribute12", type=JavaMM_Annotation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
param13: BinaryAssociation = BinaryAssociation(
    name="param13",
    ends={
        Property(name="JavaMM_Type15", type=JavaMM_Container, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaMM_Container14", type=JavaMM_Type, multiplicity=Multiplicity(0, 1))
    }
)
entities16: BinaryAssociation = BinaryAssociation(
    name="entities16",
    ends={
        Property(name="JavaMM_EntityClass", type=JavaMM_DAOClass, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaMM_DAOClass", type=JavaMM_EntityClass, multiplicity=Multiplicity(0, 9999))
    }
)
dao17: BinaryAssociation = BinaryAssociation(
    name="dao17",
    ends={
        Property(name="JavaMM_DAOClass18", type=JavaMM_TestClass, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaMM_TestClass", type=JavaMM_DAOClass, multiplicity=Multiplicity(0, 1))
    }
)
entity19: BinaryAssociation = BinaryAssociation(
    name="entity19",
    ends={
        Property(name="JavaMM_EntityClass21", type=JavaMM_TestClass, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaMM_TestClass20", type=JavaMM_EntityClass, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_JavaMM_Class_Type = Generalization(general=Type, specific=JavaMM_Class)
gen_JavaMM_PrimitiveType_Type = Generalization(general=Type, specific=JavaMM_PrimitiveType)
gen_JavaMM_Container_Type = Generalization(general=Type, specific=JavaMM_Container)
gen_JavaMM_EntityClass_Class = Generalization(general=Class_, specific=JavaMM_EntityClass)
gen_JavaMM_DAOClass_Class = Generalization(general=Class_, specific=JavaMM_DAOClass)
gen_JavaMM_TestClass_Class = Generalization(general=Class_, specific=JavaMM_TestClass)

# Domain Model
domain_model = DomainModel(
    name="JavaMM",
    types={JavaMM_PrimitiveType, JavaMM_Container, JavaMM_Class, JavaMM_Program, JavaMM_Package, Type, JavaMM_Attribute, JavaMM_Type, JavaMM_Annotation, JavaMM_EntityClass, Class_, JavaMM_DAOClass, JavaMM_TestClass, Visibility},
    associations={primitiveTypes1, containerTypes3, classes5, packages0, attributes7, type9, annotations11, param13, entities16, dao17, entity19},
    generalizations={gen_JavaMM_Class_Type, gen_JavaMM_PrimitiveType_Type, gen_JavaMM_Container_Type, gen_JavaMM_EntityClass_Class, gen_JavaMM_DAOClass_Class, gen_JavaMM_TestClass_Class},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)