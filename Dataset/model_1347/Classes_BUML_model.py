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
classes_Element = Class(name="classes::Element", is_abstract=True)
Visitable = Class(name="Visitable")
classes_NamedElement = Class(name="classes::NamedElement", is_abstract=True)
Element = Class(name="Element")
classes_Namespace = Class(name="classes::Namespace", is_abstract=True)
classes_TypedElement = Class(name="classes::TypedElement", is_abstract=True)
classes_CallExp = Class(name="classes::CallExp", is_abstract=True)
TypedElement = Class(name="TypedElement")
classes_Root = Class(name="classes::Root")
classes_Package = Class(name="classes::Package")
NamedElement = Class(name="NamedElement")
Namespace = Class(name="Namespace")
classes_Class = Class(name="classes::Class")
classes_Operation = Class(name="classes::Operation")
classes_Property = Class(name="classes::Property")
classes_Parameter = Class(name="classes::Parameter")
classes_PropertyCallExp = Class(name="classes::PropertyCallExp")
CallExp = Class(name="CallExp")
classes_OperationCallExp = Class(name="classes::OperationCallExp")
classes_Visitable = Class(name="classes::Visitable", is_abstract=True)
classes_Argument = Class(name="classes::Argument")

# classes_Element class attributes and methods

# Visitable class attributes and methods

# classes_NamedElement class attributes and methods
classes_NamedElement_name: Property = Property(name="name", type=StringType)
classes_NamedElement.attributes={classes_NamedElement_name}

# Element class attributes and methods

# classes_Namespace class attributes and methods

# classes_TypedElement class attributes and methods

# classes_CallExp class attributes and methods

# TypedElement class attributes and methods

# classes_Root class attributes and methods

# classes_Package class attributes and methods

# NamedElement class attributes and methods

# Namespace class attributes and methods

# classes_Class class attributes and methods

# classes_Operation class attributes and methods

# classes_Property class attributes and methods

# classes_Parameter class attributes and methods

# classes_PropertyCallExp class attributes and methods

# CallExp class attributes and methods

# classes_OperationCallExp class attributes and methods

# classes_Visitable class attributes and methods

# classes_Argument class attributes and methods

# Relationships
ownedCallExp2: BinaryAssociation = BinaryAssociation(
    name="ownedCallExp2",
    ends={
        Property(name="CallExp", type=classes_CallExp, multiplicity=Multiplicity(1, 1)),
        Property(name="owningSource", type=classes_CallExp, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
owningSource4: BinaryAssociation = BinaryAssociation(
    name="owningSource4",
    ends={
        Property(name="CallExp5", type=classes_CallExp, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedCallExp", type=classes_CallExp, multiplicity=Multiplicity(0, 1))
    }
)
ownedPackages6: BinaryAssociation = BinaryAssociation(
    name="ownedPackages6",
    ends={
        Property(name="classes_Package", type=classes_Root, multiplicity=Multiplicity(1, 1)),
        Property(name="classes_Root", type=classes_Package, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type0: BinaryAssociation = BinaryAssociation(
    name="type0",
    ends={
        Property(name="classes_Class", type=classes_TypedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="classes_TypedElement", type=classes_Class, multiplicity=Multiplicity(0, 1))
    }
)
ownedClasses7: BinaryAssociation = BinaryAssociation(
    name="ownedClasses7",
    ends={
        Property(name="classes_Class9", type=classes_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="classes_Package8", type=classes_Class, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedPackages11: BinaryAssociation = BinaryAssociation(
    name="ownedPackages11",
    ends={
        Property(name="classes_Package12", type=classes_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="classes_Package10", type=classes_Package, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
superClass14: BinaryAssociation = BinaryAssociation(
    name="superClass14",
    ends={
        Property(name="classes_Class15", type=classes_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="classes_Class13", type=classes_Class, multiplicity=Multiplicity(0, 1))
    }
)
ownedOperations16: BinaryAssociation = BinaryAssociation(
    name="ownedOperations16",
    ends={
        Property(name="classes_Operation", type=classes_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="classes_Class17", type=classes_Operation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedProperties18: BinaryAssociation = BinaryAssociation(
    name="ownedProperties18",
    ends={
        Property(name="classes_Property", type=classes_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="classes_Class19", type=classes_Property, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedParameters20: BinaryAssociation = BinaryAssociation(
    name="ownedParameters20",
    ends={
        Property(name="classes_Parameter", type=classes_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="classes_Operation21", type=classes_Parameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedExpressions22: BinaryAssociation = BinaryAssociation(
    name="ownedExpressions22",
    ends={
        Property(name="classes_CallExp", type=classes_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="classes_Operation23", type=classes_CallExp, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
referredProperty24: BinaryAssociation = BinaryAssociation(
    name="referredProperty24",
    ends={
        Property(name="classes_Property25", type=classes_PropertyCallExp, multiplicity=Multiplicity(1, 1)),
        Property(name="classes_PropertyCallExp", type=classes_Property, multiplicity=Multiplicity(0, 1))
    }
)
ownedArguments26: BinaryAssociation = BinaryAssociation(
    name="ownedArguments26",
    ends={
        Property(name="classes_Argument", type=classes_OperationCallExp, multiplicity=Multiplicity(1, 1)),
        Property(name="classes_OperationCallExp", type=classes_Argument, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
referredOperation27: BinaryAssociation = BinaryAssociation(
    name="referredOperation27",
    ends={
        Property(name="classes_Operation29", type=classes_OperationCallExp, multiplicity=Multiplicity(1, 1)),
        Property(name="classes_OperationCallExp28", type=classes_Operation, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_classes_Element_Visitable = Generalization(general=Visitable, specific=classes_Element)
gen_classes_NamedElement_Element = Generalization(general=Element, specific=classes_NamedElement)
gen_classes_Namespace_Element = Generalization(general=Element, specific=classes_Namespace)
gen_classes_TypedElement_Element = Generalization(general=Element, specific=classes_TypedElement)
gen_classes_CallExp_TypedElement = Generalization(general=TypedElement, specific=classes_CallExp)
gen_classes_Root_Element = Generalization(general=Element, specific=classes_Root)
gen_classes_Package_NamedElement = Generalization(general=NamedElement, specific=classes_Package)
gen_classes_Class_NamedElement = Generalization(general=NamedElement, specific=classes_Class)
gen_classes_Package_Namespace = Generalization(general=Namespace, specific=classes_Package)
gen_classes_Operation_NamedElement = Generalization(general=NamedElement, specific=classes_Operation)
gen_classes_Operation_TypedElement = Generalization(general=TypedElement, specific=classes_Operation)
gen_classes_Parameter_NamedElement = Generalization(general=NamedElement, specific=classes_Parameter)
gen_classes_PropertyCallExp_CallExp = Generalization(general=CallExp, specific=classes_PropertyCallExp)
gen_classes_OperationCallExp_CallExp = Generalization(general=CallExp, specific=classes_OperationCallExp)
gen_classes_Property_NamedElement = Generalization(general=NamedElement, specific=classes_Property)
gen_classes_Property_TypedElement = Generalization(general=TypedElement, specific=classes_Property)
gen_classes_Argument_NamedElement = Generalization(general=NamedElement, specific=classes_Argument)

# Domain Model
domain_model = DomainModel(
    name="classes",
    types={classes_Element, Visitable, classes_NamedElement, Element, classes_Namespace, classes_TypedElement, classes_CallExp, TypedElement, classes_Root, classes_Package, NamedElement, Namespace, classes_Class, classes_Operation, classes_Property, classes_Parameter, classes_PropertyCallExp, CallExp, classes_OperationCallExp, classes_Visitable, classes_Argument},
    associations={ownedCallExp2, owningSource4, ownedPackages6, type0, ownedClasses7, ownedPackages11, superClass14, ownedOperations16, ownedProperties18, ownedParameters20, ownedExpressions22, referredProperty24, ownedArguments26, referredOperation27},
    generalizations={gen_classes_Element_Visitable, gen_classes_NamedElement_Element, gen_classes_Namespace_Element, gen_classes_TypedElement_Element, gen_classes_CallExp_TypedElement, gen_classes_Root_Element, gen_classes_Package_NamedElement, gen_classes_Class_NamedElement, gen_classes_Package_Namespace, gen_classes_Operation_NamedElement, gen_classes_Operation_TypedElement, gen_classes_Parameter_NamedElement, gen_classes_PropertyCallExp_CallExp, gen_classes_OperationCallExp_CallExp, gen_classes_Property_NamedElement, gen_classes_Property_TypedElement, gen_classes_Argument_NamedElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)