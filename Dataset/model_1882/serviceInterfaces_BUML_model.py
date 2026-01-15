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
CodeGenLanguage: Enumeration = Enumeration(
    name="CodeGenLanguage",
    literals={
            EnumerationLiteral(name="ACCELEO")
    }
)

InjectionMode: Enumeration = Enumeration(
    name="InjectionMode",
    literals={
            EnumerationLiteral(name="GOOGLE_JUICE"),
			EnumerationLiteral(name="PLAIN_JAVA")
    }
)

PointcutType: Enumeration = Enumeration(
    name="PointcutType",
    literals={
            EnumerationLiteral(name="BEFORE"),
			EnumerationLiteral(name="AFTER"),
			EnumerationLiteral(name="BEFORE_BODY"),
			EnumerationLiteral(name="AFTER_BODY")
    }
)

# Classes
serviceInterfaces_Interface = Class(name="serviceInterfaces::Interface", is_abstract=True)
serviceInterfaces_codegen_InjectorAcceptorInterfaceL1 = Class(name="serviceInterfaces::codegen::InjectorAcceptorInterfaceL1")
Interface = Class(name="Interface")
TransformationLibrary = Class(name="TransformationLibrary")
serviceInterfaces_codegen_TransformationLibrary = Class(name="serviceInterfaces::codegen::TransformationLibrary")
serviceInterfaces_codegen_SlotPlugInterfaceL1 = Class(name="serviceInterfaces::codegen::SlotPlugInterfaceL1")
Pointcut = Class(name="Pointcut")
serviceInterfaces_InterfaceRepository = Class(name="serviceInterfaces::InterfaceRepository")
serviceInterfaces_Packageable = Class(name="serviceInterfaces::Packageable", is_abstract=True)
serviceInterfaces_Package = Class(name="serviceInterfaces::Package")
Packageable = Class(name="Packageable")
Operation = Class(name="Operation")
serviceInterfaces_modelingenv_JavaClass = Class(name="serviceInterfaces::modelingenv::JavaClass")
serviceInterfaces_modelingenv_Operation = Class(name="serviceInterfaces::modelingenv::Operation")
serviceInterfaces_modelingenv_SlotPlugInterfaceL0 = Class(name="serviceInterfaces::modelingenv::SlotPlugInterfaceL0")
ExtensionPoint = Class(name="ExtensionPoint")
serviceInterfaces_codegen_Pointcut = Class(name="serviceInterfaces::codegen::Pointcut", is_abstract=True)
serviceInterfaces_codegen_ClassPointcut = Class(name="serviceInterfaces::codegen::ClassPointcut")
serviceInterfaces_codegen_MethodPoincut = Class(name="serviceInterfaces::codegen::MethodPoincut")
serviceInterfaces_codegen_ImportElementPointcut = Class(name="serviceInterfaces::codegen::ImportElementPointcut")
serviceInterfaces_codegen_StatementPoincut = Class(name="serviceInterfaces::codegen::StatementPoincut")
serviceInterfaces_modelingenv_InjectorAcceptorInterfaceL0 = Class(name="serviceInterfaces::modelingenv::InjectorAcceptorInterfaceL0")
JavaTypeDeclaration = Class(name="JavaTypeDeclaration")
serviceInterfaces_modelingenv_JavaTypeDeclaration = Class(name="serviceInterfaces::modelingenv::JavaTypeDeclaration", is_abstract=True)
serviceInterfaces_modelingenv_JavaInterface = Class(name="serviceInterfaces::modelingenv::JavaInterface")
serviceInterfaces_modelingenv_ExtensionPoint = Class(name="serviceInterfaces::modelingenv::ExtensionPoint")

# serviceInterfaces_Interface class attributes and methods
serviceInterfaces_Interface_qName: Property = Property(name="qName", type=StringType)
serviceInterfaces_Interface_description: Property = Property(name="description", type=StringType)
serviceInterfaces_Interface.attributes={serviceInterfaces_Interface_description, serviceInterfaces_Interface_qName}

# serviceInterfaces_codegen_InjectorAcceptorInterfaceL1 class attributes and methods

# Interface class attributes and methods

# TransformationLibrary class attributes and methods

# serviceInterfaces_codegen_TransformationLibrary class attributes and methods
serviceInterfaces_codegen_TransformationLibrary_name: Property = Property(name="name", type=StringType)
serviceInterfaces_codegen_TransformationLibrary_language: Property = Property(name="language", type=StringType)
serviceInterfaces_codegen_TransformationLibrary.attributes={serviceInterfaces_codegen_TransformationLibrary_language, serviceInterfaces_codegen_TransformationLibrary_name}

# serviceInterfaces_codegen_SlotPlugInterfaceL1 class attributes and methods

# Pointcut class attributes and methods

# serviceInterfaces_InterfaceRepository class attributes and methods

# serviceInterfaces_Packageable class attributes and methods

# serviceInterfaces_Package class attributes and methods
serviceInterfaces_Package_name: Property = Property(name="name", type=StringType)
serviceInterfaces_Package.attributes={serviceInterfaces_Package_name}

# Packageable class attributes and methods

# Operation class attributes and methods

# serviceInterfaces_modelingenv_JavaClass class attributes and methods

# serviceInterfaces_modelingenv_Operation class attributes and methods
serviceInterfaces_modelingenv_Operation_name: Property = Property(name="name", type=StringType)
serviceInterfaces_modelingenv_Operation.attributes={serviceInterfaces_modelingenv_Operation_name}

# serviceInterfaces_modelingenv_SlotPlugInterfaceL0 class attributes and methods

# ExtensionPoint class attributes and methods

# serviceInterfaces_codegen_Pointcut class attributes and methods
serviceInterfaces_codegen_Pointcut_type: Property = Property(name="type", type=StringType)
serviceInterfaces_codegen_Pointcut.attributes={serviceInterfaces_codegen_Pointcut_type}

# serviceInterfaces_codegen_ClassPointcut class attributes and methods

# serviceInterfaces_codegen_MethodPoincut class attributes and methods

# serviceInterfaces_codegen_ImportElementPointcut class attributes and methods

# serviceInterfaces_codegen_StatementPoincut class attributes and methods

# serviceInterfaces_modelingenv_InjectorAcceptorInterfaceL0 class attributes and methods
serviceInterfaces_modelingenv_InjectorAcceptorInterfaceL0_mode: Property = Property(name="mode", type=StringType)
serviceInterfaces_modelingenv_InjectorAcceptorInterfaceL0.attributes={serviceInterfaces_modelingenv_InjectorAcceptorInterfaceL0_mode}

# JavaTypeDeclaration class attributes and methods

# serviceInterfaces_modelingenv_JavaTypeDeclaration class attributes and methods
serviceInterfaces_modelingenv_JavaTypeDeclaration_qualifiedName: Property = Property(name="qualifiedName", type=StringType)
serviceInterfaces_modelingenv_JavaTypeDeclaration.attributes={serviceInterfaces_modelingenv_JavaTypeDeclaration_qualifiedName}

# serviceInterfaces_modelingenv_JavaInterface class attributes and methods

# serviceInterfaces_modelingenv_ExtensionPoint class attributes and methods
serviceInterfaces_modelingenv_ExtensionPoint_id: Property = Property(name="id", type=StringType)
serviceInterfaces_modelingenv_ExtensionPoint.attributes={serviceInterfaces_modelingenv_ExtensionPoint_id}

# Relationships
contents1: BinaryAssociation = BinaryAssociation(
    name="contents1",
    ends={
        Property(name="serviceInterfaces_Packageable2", type=serviceInterfaces_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="serviceInterfaces_Package", type=serviceInterfaces_Packageable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
injectorProvides3: BinaryAssociation = BinaryAssociation(
    name="injectorProvides3",
    ends={
        Property(name="TransformationLibrary", type=serviceInterfaces_codegen_InjectorAcceptorInterfaceL1, multiplicity=Multiplicity(1, 1)),
        Property(name="serviceInterfaces_codegen_InjectorAcceptorInterfaceL1", type=TransformationLibrary, multiplicity=Multiplicity(0, 1))
    }
)
contents0: BinaryAssociation = BinaryAssociation(
    name="contents0",
    ends={
        Property(name="serviceInterfaces_Packageable", type=serviceInterfaces_InterfaceRepository, multiplicity=Multiplicity(1, 1)),
        Property(name="serviceInterfaces_InterfaceRepository", type=serviceInterfaces_Packageable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
operations6: BinaryAssociation = BinaryAssociation(
    name="operations6",
    ends={
        Property(name="Operation", type=serviceInterfaces_modelingenv_JavaInterface, multiplicity=Multiplicity(1, 1)),
        Property(name="serviceInterfaces_modelingenv_JavaInterface", type=Operation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
operations7: BinaryAssociation = BinaryAssociation(
    name="operations7",
    ends={
        Property(name="Operation8", type=serviceInterfaces_modelingenv_JavaClass, multiplicity=Multiplicity(1, 1)),
        Property(name="serviceInterfaces_modelingenv_JavaClass", type=Operation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
slot9: BinaryAssociation = BinaryAssociation(
    name="slot9",
    ends={
        Property(name="ExtensionPoint", type=serviceInterfaces_modelingenv_SlotPlugInterfaceL0, multiplicity=Multiplicity(1, 1)),
        Property(name="serviceInterfaces_modelingenv_SlotPlugInterfaceL0", type=ExtensionPoint, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
pointcuts4: BinaryAssociation = BinaryAssociation(
    name="pointcuts4",
    ends={
        Property(name="Pointcut", type=serviceInterfaces_codegen_SlotPlugInterfaceL1, multiplicity=Multiplicity(1, 1)),
        Property(name="serviceInterfaces_codegen_SlotPlugInterfaceL1", type=Pointcut, multiplicity=Multiplicity(0, 1))
    }
)
injectorImplements5: BinaryAssociation = BinaryAssociation(
    name="injectorImplements5",
    ends={
        Property(name="JavaTypeDeclaration", type=serviceInterfaces_modelingenv_InjectorAcceptorInterfaceL0, multiplicity=Multiplicity(1, 1)),
        Property(name="serviceInterfaces_modelingenv_InjectorAcceptorInterfaceL0", type=JavaTypeDeclaration, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)

# Generalizations
gen_serviceInterfaces_Interface_Packageable = Generalization(general=Packageable, specific=serviceInterfaces_Interface)
gen_serviceInterfaces_codegen_InjectorAcceptorInterfaceL1_Interface = Generalization(general=Interface, specific=serviceInterfaces_codegen_InjectorAcceptorInterfaceL1)
gen_serviceInterfaces_codegen_SlotPlugInterfaceL1_Interface = Generalization(general=Interface, specific=serviceInterfaces_codegen_SlotPlugInterfaceL1)
gen_serviceInterfaces_Package_Packageable = Generalization(general=Packageable, specific=serviceInterfaces_Package)
gen_serviceInterfaces_modelingenv_JavaClass_JavaTypeDeclaration = Generalization(general=JavaTypeDeclaration, specific=serviceInterfaces_modelingenv_JavaClass)
gen_serviceInterfaces_modelingenv_SlotPlugInterfaceL0_Interface = Generalization(general=Interface, specific=serviceInterfaces_modelingenv_SlotPlugInterfaceL0)
gen_serviceInterfaces_codegen_ClassPointcut_Pointcut = Generalization(general=Pointcut, specific=serviceInterfaces_codegen_ClassPointcut)
gen_serviceInterfaces_codegen_MethodPoincut_Pointcut = Generalization(general=Pointcut, specific=serviceInterfaces_codegen_MethodPoincut)
gen_serviceInterfaces_codegen_ImportElementPointcut_Pointcut = Generalization(general=Pointcut, specific=serviceInterfaces_codegen_ImportElementPointcut)
gen_serviceInterfaces_codegen_StatementPoincut_Pointcut = Generalization(general=Pointcut, specific=serviceInterfaces_codegen_StatementPoincut)
gen_serviceInterfaces_modelingenv_InjectorAcceptorInterfaceL0_Interface = Generalization(general=Interface, specific=serviceInterfaces_modelingenv_InjectorAcceptorInterfaceL0)
gen_serviceInterfaces_modelingenv_JavaInterface_JavaTypeDeclaration = Generalization(general=JavaTypeDeclaration, specific=serviceInterfaces_modelingenv_JavaInterface)

# Domain Model
domain_model = DomainModel(
    name="serviceInterfaces",
    types={serviceInterfaces_Interface, serviceInterfaces_codegen_InjectorAcceptorInterfaceL1, Interface, TransformationLibrary, serviceInterfaces_codegen_TransformationLibrary, serviceInterfaces_codegen_SlotPlugInterfaceL1, Pointcut, serviceInterfaces_InterfaceRepository, serviceInterfaces_Packageable, serviceInterfaces_Package, Packageable, Operation, serviceInterfaces_modelingenv_JavaClass, serviceInterfaces_modelingenv_Operation, serviceInterfaces_modelingenv_SlotPlugInterfaceL0, ExtensionPoint, serviceInterfaces_codegen_Pointcut, serviceInterfaces_codegen_ClassPointcut, serviceInterfaces_codegen_MethodPoincut, serviceInterfaces_codegen_ImportElementPointcut, serviceInterfaces_codegen_StatementPoincut, serviceInterfaces_modelingenv_InjectorAcceptorInterfaceL0, JavaTypeDeclaration, serviceInterfaces_modelingenv_JavaTypeDeclaration, serviceInterfaces_modelingenv_JavaInterface, serviceInterfaces_modelingenv_ExtensionPoint, CodeGenLanguage, InjectionMode, PointcutType},
    associations={contents1, injectorProvides3, contents0, operations6, operations7, slot9, pointcuts4, injectorImplements5},
    generalizations={gen_serviceInterfaces_Interface_Packageable, gen_serviceInterfaces_codegen_InjectorAcceptorInterfaceL1_Interface, gen_serviceInterfaces_codegen_SlotPlugInterfaceL1_Interface, gen_serviceInterfaces_Package_Packageable, gen_serviceInterfaces_modelingenv_JavaClass_JavaTypeDeclaration, gen_serviceInterfaces_modelingenv_SlotPlugInterfaceL0_Interface, gen_serviceInterfaces_codegen_ClassPointcut_Pointcut, gen_serviceInterfaces_codegen_MethodPoincut_Pointcut, gen_serviceInterfaces_codegen_ImportElementPointcut_Pointcut, gen_serviceInterfaces_codegen_StatementPoincut_Pointcut, gen_serviceInterfaces_modelingenv_InjectorAcceptorInterfaceL0_Interface, gen_serviceInterfaces_modelingenv_JavaInterface_JavaTypeDeclaration},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)