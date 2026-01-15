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
            EnumerationLiteral(name="public"),
			EnumerationLiteral(name="protected"),
			EnumerationLiteral(name="private")
    }
)

# Classes
classes_ClassModel = Class(name="classes::ClassModel")
classes_Content = Class(name="classes::Content")
classes_Constant = Class(name="classes::Constant")
Content = Class(name="Content")
Description = Class(name="Description")
classes_Value = Class(name="classes::Value")
classes_Association = Class(name="classes::Association")
classes_Class = Class(name="classes::Class")
classes_Attribute = Class(name="classes::Attribute")
classes_Type = Class(name="classes::Type")
classes_BuiltInType = Class(name="classes::BuiltInType")
Type = Class(name="Type")
classes_StringType = Class(name="classes::StringType")
BuiltInType = Class(name="BuiltInType")
classes_IntegerType = Class(name="classes::IntegerType")
classes_ClassRef = Class(name="classes::ClassRef")
classes_IntegerLiteral = Class(name="classes::IntegerLiteral")
Value = Class(name="Value")
classes_ConstantRef = Class(name="classes::ConstantRef")
classes_Description = Class(name="classes::Description")

# classes_ClassModel class attributes and methods

# classes_Content class attributes and methods

# classes_Constant class attributes and methods
classes_Constant_name: Property = Property(name="name", type=StringType)
classes_Constant.attributes={classes_Constant_name}

# Content class attributes and methods

# Description class attributes and methods

# classes_Value class attributes and methods

# classes_Association class attributes and methods
classes_Association_name: Property = Property(name="name", type=StringType)
classes_Association.attributes={classes_Association_name}

# classes_Class class attributes and methods
classes_Class_name: Property = Property(name="name", type=StringType)
classes_Class.attributes={classes_Class_name}

# classes_Attribute class attributes and methods
classes_Attribute_visibility: Property = Property(name="visibility", type=StringType)
classes_Attribute_name: Property = Property(name="name", type=StringType)
classes_Attribute.attributes={classes_Attribute_visibility, classes_Attribute_name}

# classes_Type class attributes and methods

# classes_BuiltInType class attributes and methods

# Type class attributes and methods

# classes_StringType class attributes and methods

# BuiltInType class attributes and methods

# classes_IntegerType class attributes and methods

# classes_ClassRef class attributes and methods

# classes_IntegerLiteral class attributes and methods
classes_IntegerLiteral_value: Property = Property(name="value", type=IntegerType)
classes_IntegerLiteral.attributes={classes_IntegerLiteral_value}

# Value class attributes and methods

# classes_ConstantRef class attributes and methods

# classes_Description class attributes and methods
classes_Description_description: Property = Property(name="description", type=StringType)
classes_Description.attributes={classes_Description_description}

# Relationships
content0: BinaryAssociation = BinaryAssociation(
    name="content0",
    ends={
        Property(name="classes_Content", type=classes_ClassModel, multiplicity=Multiplicity(1, 1)),
        Property(name="classes_ClassModel", type=classes_Content, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
initial1: BinaryAssociation = BinaryAssociation(
    name="initial1",
    ends={
        Property(name="classes_Value", type=classes_Constant, multiplicity=Multiplicity(1, 1)),
        Property(name="classes_Constant", type=classes_Value, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
attributes15: BinaryAssociation = BinaryAssociation(
    name="attributes15",
    ends={
        Property(name="classes_Attribute", type=classes_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="classes_Class16", type=classes_Attribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type17: BinaryAssociation = BinaryAssociation(
    name="type17",
    ends={
        Property(name="classes_Type", type=classes_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="classes_Attribute18", type=classes_Type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
lowerBound19: BinaryAssociation = BinaryAssociation(
    name="lowerBound19",
    ends={
        Property(name="classes_Value21", type=classes_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="classes_Attribute20", type=classes_Value, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
upperBound22: BinaryAssociation = BinaryAssociation(
    name="upperBound22",
    ends={
        Property(name="classes_Value24", type=classes_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="classes_Attribute23", type=classes_Value, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
target25: BinaryAssociation = BinaryAssociation(
    name="target25",
    ends={
        Property(name="classes_Class26", type=classes_ClassRef, multiplicity=Multiplicity(1, 1)),
        Property(name="classes_ClassRef", type=classes_Class, multiplicity=Multiplicity(0, 1))
    }
)
source2: BinaryAssociation = BinaryAssociation(
    name="source2",
    ends={
        Property(name="classes_Class", type=classes_Association, multiplicity=Multiplicity(1, 1)),
        Property(name="classes_Association", type=classes_Class, multiplicity=Multiplicity(0, 1))
    }
)
target3: BinaryAssociation = BinaryAssociation(
    name="target3",
    ends={
        Property(name="classes_Class5", type=classes_Association, multiplicity=Multiplicity(1, 1)),
        Property(name="classes_Association4", type=classes_Class, multiplicity=Multiplicity(0, 1))
    }
)
lowerBound6: BinaryAssociation = BinaryAssociation(
    name="lowerBound6",
    ends={
        Property(name="classes_Value8", type=classes_Association, multiplicity=Multiplicity(1, 1)),
        Property(name="classes_Association7", type=classes_Value, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
upperBound9: BinaryAssociation = BinaryAssociation(
    name="upperBound9",
    ends={
        Property(name="classes_Value11", type=classes_Association, multiplicity=Multiplicity(1, 1)),
        Property(name="classes_Association10", type=classes_Value, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
subClasses13: BinaryAssociation = BinaryAssociation(
    name="subClasses13",
    ends={
        Property(name="classes_Class14", type=classes_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="classes_Class12", type=classes_Class, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
target27: BinaryAssociation = BinaryAssociation(
    name="target27",
    ends={
        Property(name="classes_Constant28", type=classes_ConstantRef, multiplicity=Multiplicity(1, 1)),
        Property(name="classes_ConstantRef", type=classes_Constant, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_classes_Constant_Content = Generalization(general=Content, specific=classes_Constant)
gen_classes_Constant_Description = Generalization(general=Description, specific=classes_Constant)
gen_classes_Association_Content = Generalization(general=Content, specific=classes_Association)
gen_classes_Association_Description = Generalization(general=Description, specific=classes_Association)
gen_classes_Attribute_Description = Generalization(general=Description, specific=classes_Attribute)
gen_classes_BuiltInType_Type = Generalization(general=Type, specific=classes_BuiltInType)
gen_classes_StringType_BuiltInType = Generalization(general=BuiltInType, specific=classes_StringType)
gen_classes_IntegerType_BuiltInType = Generalization(general=BuiltInType, specific=classes_IntegerType)
gen_classes_ClassRef_Type = Generalization(general=Type, specific=classes_ClassRef)
gen_classes_Class_Content = Generalization(general=Content, specific=classes_Class)
gen_classes_Class_Description = Generalization(general=Description, specific=classes_Class)
gen_classes_IntegerLiteral_Value = Generalization(general=Value, specific=classes_IntegerLiteral)
gen_classes_ConstantRef_Value = Generalization(general=Value, specific=classes_ConstantRef)

# Domain Model
domain_model = DomainModel(
    name="classes",
    types={classes_ClassModel, classes_Content, classes_Constant, Content, Description, classes_Value, classes_Association, classes_Class, classes_Attribute, classes_Type, classes_BuiltInType, Type, classes_StringType, BuiltInType, classes_IntegerType, classes_ClassRef, classes_IntegerLiteral, Value, classes_ConstantRef, classes_Description, Visibility},
    associations={content0, initial1, attributes15, type17, lowerBound19, upperBound22, target25, source2, target3, lowerBound6, upperBound9, subClasses13, target27},
    generalizations={gen_classes_Constant_Content, gen_classes_Constant_Description, gen_classes_Association_Content, gen_classes_Association_Description, gen_classes_Attribute_Description, gen_classes_BuiltInType_Type, gen_classes_StringType_BuiltInType, gen_classes_IntegerType_BuiltInType, gen_classes_ClassRef_Type, gen_classes_Class_Content, gen_classes_Class_Description, gen_classes_IntegerLiteral_Value, gen_classes_ConstantRef_Value},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)