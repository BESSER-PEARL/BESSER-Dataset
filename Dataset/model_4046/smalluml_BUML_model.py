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
smalluml_NamedElement = Class(name="smalluml::NamedElement", is_abstract=True)
smalluml_SuperType = Class(name="smalluml::SuperType", is_abstract=True)
NamedElement = Class(name="NamedElement")
smalluml_Attribute = Class(name="smalluml::Attribute")
smalluml_Role = Class(name="smalluml::Role")
smalluml_Class = Class(name="smalluml::Class")
smalluml_Association = Class(name="smalluml::Association")
smalluml_Operation = Class(name="smalluml::Operation")
smalluml_Parameter = Class(name="smalluml::Parameter")
SuperType = Class(name="SuperType")
smalluml_Type = Class(name="smalluml::Type")
smalluml_Enumeration = Class(name="smalluml::Enumeration")
smalluml_Package = Class(name="smalluml::Package")

# smalluml_NamedElement class attributes and methods
smalluml_NamedElement_name: Property = Property(name="name", type=StringType)
smalluml_NamedElement.attributes={smalluml_NamedElement_name}

# smalluml_SuperType class attributes and methods

# NamedElement class attributes and methods

# smalluml_Attribute class attributes and methods

# smalluml_Role class attributes and methods
smalluml_Role_lowerBound: Property = Property(name="lowerBound", type=IntegerType)
smalluml_Role_upperBound: Property = Property(name="upperBound", type=IntegerType)
smalluml_Role.attributes={smalluml_Role_lowerBound, smalluml_Role_upperBound}

# smalluml_Class class attributes and methods
smalluml_Class_isAbstract: Property = Property(name="isAbstract", type=BooleanType)
smalluml_Class.attributes={smalluml_Class_isAbstract}

# smalluml_Association class attributes and methods

# smalluml_Operation class attributes and methods
smalluml_Operation_isAbstract: Property = Property(name="isAbstract", type=BooleanType)
smalluml_Operation.attributes={smalluml_Operation_isAbstract}

# smalluml_Parameter class attributes and methods

# SuperType class attributes and methods

# smalluml_Type class attributes and methods

# smalluml_Enumeration class attributes and methods
smalluml_Enumeration_enumeration: Property = Property(name="enumeration", type=StringType)
smalluml_Enumeration.attributes={smalluml_Enumeration_enumeration}

# smalluml_Package class attributes and methods

# Relationships
type0: BinaryAssociation = BinaryAssociation(
    name="type0",
    ends={
        Property(name="smalluml_SuperType", type=smalluml_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="smalluml_Attribute", type=smalluml_SuperType, multiplicity=Multiplicity(1, 1))
    }
)
elements20: BinaryAssociation = BinaryAssociation(
    name="elements20",
    ends={
        Property(name="smalluml_SuperType21", type=smalluml_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="smalluml_Package", type=smalluml_SuperType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
association22: BinaryAssociation = BinaryAssociation(
    name="association22",
    ends={
        Property(name="smalluml_Association24", type=smalluml_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="smalluml_Package23", type=smalluml_Association, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
class1: BinaryAssociation = BinaryAssociation(
    name="class1",
    ends={
        Property(name="smalluml_Class", type=smalluml_Role, multiplicity=Multiplicity(1, 1)),
        Property(name="smalluml_Role", type=smalluml_Class, multiplicity=Multiplicity(1, 1))
    }
)
role2: BinaryAssociation = BinaryAssociation(
    name="role2",
    ends={
        Property(name="smalluml_Role3", type=smalluml_Association, multiplicity=Multiplicity(1, 1)),
        Property(name="smalluml_Association", type=smalluml_Role, multiplicity=Multiplicity(2, 9999), is_composite=True)
    }
)
parameters4: BinaryAssociation = BinaryAssociation(
    name="parameters4",
    ends={
        Property(name="smalluml_Parameter", type=smalluml_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="smalluml_Operation", type=smalluml_Parameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
returnType5: BinaryAssociation = BinaryAssociation(
    name="returnType5",
    ends={
        Property(name="smalluml_SuperType7", type=smalluml_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="smalluml_Operation6", type=smalluml_SuperType, multiplicity=Multiplicity(0, 1))
    }
)
type8: BinaryAssociation = BinaryAssociation(
    name="type8",
    ends={
        Property(name="smalluml_SuperType10", type=smalluml_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="smalluml_Parameter9", type=smalluml_SuperType, multiplicity=Multiplicity(1, 1))
    }
)
attribute11: BinaryAssociation = BinaryAssociation(
    name="attribute11",
    ends={
        Property(name="smalluml_Attribute13", type=smalluml_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="smalluml_Class12", type=smalluml_Attribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
operation14: BinaryAssociation = BinaryAssociation(
    name="operation14",
    ends={
        Property(name="smalluml_Operation16", type=smalluml_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="smalluml_Class15", type=smalluml_Operation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
super18: BinaryAssociation = BinaryAssociation(
    name="super18",
    ends={
        Property(name="smalluml_Class19", type=smalluml_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="smalluml_Class17", type=smalluml_Class, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_smalluml_SuperType_NamedElement = Generalization(general=NamedElement, specific=smalluml_SuperType)
gen_smalluml_Attribute_NamedElement = Generalization(general=NamedElement, specific=smalluml_Attribute)
gen_smalluml_Role_NamedElement = Generalization(general=NamedElement, specific=smalluml_Role)
gen_smalluml_Association_NamedElement = Generalization(general=NamedElement, specific=smalluml_Association)
gen_smalluml_Operation_NamedElement = Generalization(general=NamedElement, specific=smalluml_Operation)
gen_smalluml_Parameter_NamedElement = Generalization(general=NamedElement, specific=smalluml_Parameter)
gen_smalluml_Class_SuperType = Generalization(general=SuperType, specific=smalluml_Class)
gen_smalluml_Type_SuperType = Generalization(general=SuperType, specific=smalluml_Type)
gen_smalluml_Enumeration_SuperType = Generalization(general=SuperType, specific=smalluml_Enumeration)
gen_smalluml_Package_NamedElement = Generalization(general=NamedElement, specific=smalluml_Package)

# Domain Model
domain_model = DomainModel(
    name="smalluml",
    types={smalluml_NamedElement, smalluml_SuperType, NamedElement, smalluml_Attribute, smalluml_Role, smalluml_Class, smalluml_Association, smalluml_Operation, smalluml_Parameter, SuperType, smalluml_Type, smalluml_Enumeration, smalluml_Package},
    associations={type0, elements20, association22, class1, role2, parameters4, returnType5, type8, attribute11, operation14, super18},
    generalizations={gen_smalluml_SuperType_NamedElement, gen_smalluml_Attribute_NamedElement, gen_smalluml_Role_NamedElement, gen_smalluml_Association_NamedElement, gen_smalluml_Operation_NamedElement, gen_smalluml_Parameter_NamedElement, gen_smalluml_Class_SuperType, gen_smalluml_Type_SuperType, gen_smalluml_Enumeration_SuperType, gen_smalluml_Package_NamedElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)