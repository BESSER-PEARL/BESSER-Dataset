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
			EnumerationLiteral(name="protected"),
			EnumerationLiteral(name="public")
    }
)

PrimitiveTypes: Enumeration = Enumeration(
    name="PrimitiveTypes",
    literals={
            EnumerationLiteral(name="int"),
			EnumerationLiteral(name="bool"),
			EnumerationLiteral(name="string"),
			EnumerationLiteral(name="double")
    }
)

# Classes
psample_Package = Class(name="psample::Package")
psample_TypedElement = Class(name="psample::TypedElement", is_abstract=True)
psample_Object = Class(name="psample::Object", is_abstract=True)
psample_Class = Class(name="psample::Class")
TypedElement = Class(name="TypedElement")
psample_Member = Class(name="psample::Member", is_abstract=True)
psample_PrimitiveTypeVariable = Class(name="psample::PrimitiveTypeVariable")
Type = Class(name="Type")
psample_Interface = Class(name="psample::Interface")
psample_Function = Class(name="psample::Function")
Member = Class(name="Member")
psample_Variable = Class(name="psample::Variable")
psample_Type = Class(name="psample::Type", is_abstract=True)
Object = Class(name="Object")

# psample_Package class attributes and methods
psample_Package_Name: Property = Property(name="Name", type=StringType)
psample_Package.attributes={psample_Package_Name}

# psample_TypedElement class attributes and methods

# psample_Object class attributes and methods
psample_Object_Name: Property = Property(name="Name", type=StringType)
psample_Object.attributes={psample_Object_Name}

# psample_Class class attributes and methods

# TypedElement class attributes and methods

# psample_Member class attributes and methods

# psample_PrimitiveTypeVariable class attributes and methods

# Type class attributes and methods

# psample_Interface class attributes and methods

# psample_Function class attributes and methods

# Member class attributes and methods

# psample_Variable class attributes and methods

# psample_Type class attributes and methods

# Object class attributes and methods

# Relationships
typedelement0: BinaryAssociation = BinaryAssociation(
    name="typedelement0",
    ends={
        Property(name="psample_TypedElement", type=psample_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="psample_Package", type=psample_TypedElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
member1: BinaryAssociation = BinaryAssociation(
    name="member1",
    ends={
        Property(name="psample_Member", type=psample_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="psample_Class", type=psample_Member, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
primitivetype2: BinaryAssociation = BinaryAssociation(
    name="primitivetype2",
    ends={
        Property(name="psample_PrimitiveTypeVariable", type=psample_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="psample_Class3", type=psample_PrimitiveTypeVariable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_psample_Class_TypedElement = Generalization(general=TypedElement, specific=psample_Class)
gen_psample_Member_Type = Generalization(general=Type, specific=psample_Member)
gen_psample_PrimitiveTypeVariable_Type = Generalization(general=Type, specific=psample_PrimitiveTypeVariable)
gen_psample_Interface_TypedElement = Generalization(general=TypedElement, specific=psample_Interface)
gen_psample_Function_Member = Generalization(general=Member, specific=psample_Function)
gen_psample_Variable_Member = Generalization(general=Member, specific=psample_Variable)
gen_psample_Type_Object = Generalization(general=Object, specific=psample_Type)
gen_psample_TypedElement_Object = Generalization(general=Object, specific=psample_TypedElement)

# Domain Model
domain_model = DomainModel(
    name="psample",
    types={psample_Package, psample_TypedElement, psample_Object, psample_Class, TypedElement, psample_Member, psample_PrimitiveTypeVariable, Type, psample_Interface, psample_Function, Member, psample_Variable, psample_Type, Object, Visibility, PrimitiveTypes},
    associations={typedelement0, member1, primitivetype2},
    generalizations={gen_psample_Class_TypedElement, gen_psample_Member_Type, gen_psample_PrimitiveTypeVariable_Type, gen_psample_Interface_TypedElement, gen_psample_Function_Member, gen_psample_Variable_Member, gen_psample_Type_Object, gen_psample_TypedElement_Object},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)