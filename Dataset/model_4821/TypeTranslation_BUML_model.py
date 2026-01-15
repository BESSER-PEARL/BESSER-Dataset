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
MyEnumeration: Enumeration = Enumeration(
    name="MyEnumeration",
    literals={
            
    }
)

# Classes
typetranslation_MyClass = Class(name="typetranslation::MyClass")
typetranslation_AbstractClass = Class(name="typetranslation::AbstractClass", is_abstract=True)

# typetranslation_MyClass class attributes and methods
typetranslation_MyClass_ocl_string_single: Property = Property(name="ocl_string_single", type=StringType)
typetranslation_MyClass_ocl_string_multi: Property = Property(name="ocl_string_multi", type=StringType)
typetranslation_MyClass_ocl_integer_single: Property = Property(name="ocl_integer_single", type=StringType)
typetranslation_MyClass_ocl_integer_multi: Property = Property(name="ocl_integer_multi", type=StringType)
typetranslation_MyClass_ocl_real_single: Property = Property(name="ocl_real_single", type=StringType)
typetranslation_MyClass_ocl_real_multi: Property = Property(name="ocl_real_multi", type=StringType)
typetranslation_MyClass_ocl_boolean_single: Property = Property(name="ocl_boolean_single", type=StringType)
typetranslation_MyClass_ocl_boolean_multi: Property = Property(name="ocl_boolean_multi", type=StringType)
typetranslation_MyClass_ecore_ebigdecimal_single: Property = Property(name="ecore_ebigdecimal_single", type=StringType)
typetranslation_MyClass_ecore_ebigdecimal_multi: Property = Property(name="ecore_ebigdecimal_multi", type=StringType)
typetranslation_MyClass_ecore_ebiginteger_single: Property = Property(name="ecore_ebiginteger_single", type=StringType)
typetranslation_MyClass_ecore_ebiginteger_multi: Property = Property(name="ecore_ebiginteger_multi", type=StringType)
typetranslation_MyClass_ecore_eboolean_single: Property = Property(name="ecore_eboolean_single", type=BooleanType)
typetranslation_MyClass_ecore_eboolean_multi: Property = Property(name="ecore_eboolean_multi", type=BooleanType)
typetranslation_MyClass_ecore_ebooleanobject_single: Property = Property(name="ecore_ebooleanobject_single", type=StringType)
typetranslation_MyClass_ecore_ebooleanobject_multi: Property = Property(name="ecore_ebooleanobject_multi", type=StringType)
typetranslation_MyClass_ecore_ebyte_single: Property = Property(name="ecore_ebyte_single", type=StringType)
typetranslation_MyClass_ecore_ebyte_multi: Property = Property(name="ecore_ebyte_multi", type=StringType)
typetranslation_MyClass_ecore_ebytearray_single: Property = Property(name="ecore_ebytearray_single", type=StringType)
typetranslation_MyClass_ecore_ebytearray_multi: Property = Property(name="ecore_ebytearray_multi", type=StringType)
typetranslation_MyClass_ecore_ebyteobject_single: Property = Property(name="ecore_ebyteobject_single", type=StringType)
typetranslation_MyClass_ecore_ebyteobject_multi: Property = Property(name="ecore_ebyteobject_multi", type=StringType)
typetranslation_MyClass_ecore_echar_single: Property = Property(name="ecore_echar_single", type=StringType)
typetranslation_MyClass_ecore_echar_multi: Property = Property(name="ecore_echar_multi", type=StringType)
typetranslation_MyClass_ecore_echaracterobject_single: Property = Property(name="ecore_echaracterobject_single", type=StringType)
typetranslation_MyClass_ecore_echaracterobject_multi: Property = Property(name="ecore_echaracterobject_multi", type=StringType)
typetranslation_MyClass_ecore_edate_single: Property = Property(name="ecore_edate_single", type=DateType)
typetranslation_MyClass_ecore_edate_multi: Property = Property(name="ecore_edate_multi", type=DateType)
typetranslation_MyClass_ecore_ediagnosticchain_single: Property = Property(name="ecore_ediagnosticchain_single", type=StringType)
typetranslation_MyClass_ecore_ediagnosticchain_multi: Property = Property(name="ecore_ediagnosticchain_multi", type=StringType)
typetranslation_MyClass_ecore_edouble_single: Property = Property(name="ecore_edouble_single", type=FloatType)
typetranslation_MyClass_ecore_edouble_multi: Property = Property(name="ecore_edouble_multi", type=FloatType)
typetranslation_MyClass_ecore_edoubleobject_single: Property = Property(name="ecore_edoubleobject_single", type=StringType)
typetranslation_MyClass_ecore_edoubleobject_multi: Property = Property(name="ecore_edoubleobject_multi", type=StringType)
typetranslation_MyClass_ecore_eelist_multi: Property = Property(name="ecore_eelist_multi", type=StringType)
typetranslation_MyClass_ecore_eenumerator_single: Property = Property(name="ecore_eenumerator_single", type=StringType)
typetranslation_MyClass_ecore_eenumerator_multi: Property = Property(name="ecore_eenumerator_multi", type=StringType)
typetranslation_MyClass_ecore_efeaturemap_single: Property = Property(name="ecore_efeaturemap_single", type=StringType)
typetranslation_MyClass_ecore_efeaturemap_multi: Property = Property(name="ecore_efeaturemap_multi", type=StringType)
typetranslation_MyClass_ecore_efeaturemapentry_single: Property = Property(name="ecore_efeaturemapentry_single", type=StringType)
typetranslation_MyClass_ecore_efeaturemapentry_multi: Property = Property(name="ecore_efeaturemapentry_multi", type=StringType)
typetranslation_MyClass_ecore_efloat_single: Property = Property(name="ecore_efloat_single", type=FloatType)
typetranslation_MyClass_ecore_efloat_multi: Property = Property(name="ecore_efloat_multi", type=FloatType)
typetranslation_MyClass_ecore_efloatobject_single: Property = Property(name="ecore_efloatobject_single", type=StringType)
typetranslation_MyClass_ecore_efloatobject_multi: Property = Property(name="ecore_efloatobject_multi", type=StringType)
typetranslation_MyClass_ecore_eint_single: Property = Property(name="ecore_eint_single", type=IntegerType)
typetranslation_MyClass_ecore_eint_multi: Property = Property(name="ecore_eint_multi", type=IntegerType)
typetranslation_MyClass_ecore_eintegerobject_single: Property = Property(name="ecore_eintegerobject_single", type=StringType)
typetranslation_MyClass_ecore_eintegerobject_multi: Property = Property(name="ecore_eintegerobject_multi", type=StringType)
typetranslation_MyClass_ecore_ejavaclass_single: Property = Property(name="ecore_ejavaclass_single", type=StringType)
typetranslation_MyClass_ecore_ejavaclass_multi: Property = Property(name="ecore_ejavaclass_multi", type=StringType)
typetranslation_MyClass_ecore_ejavaobject_single: Property = Property(name="ecore_ejavaobject_single", type=StringType)
typetranslation_MyClass_ecore_ejavaobject_multi: Property = Property(name="ecore_ejavaobject_multi", type=StringType)
typetranslation_MyClass_ecore_elong_single: Property = Property(name="ecore_elong_single", type=StringType)
typetranslation_MyClass_ecore_elong_multi: Property = Property(name="ecore_elong_multi", type=StringType)
typetranslation_MyClass_ecore_elongobject_single: Property = Property(name="ecore_elongobject_single", type=StringType)
typetranslation_MyClass_ecore_elongobject_multi: Property = Property(name="ecore_elongobject_multi", type=StringType)
typetranslation_MyClass_ecore_emap_single: Property = Property(name="ecore_emap_single", type=StringType)
typetranslation_MyClass_ecore_emap_multi: Property = Property(name="ecore_emap_multi", type=StringType)
typetranslation_MyClass_ecore_eresource_single: Property = Property(name="ecore_eresource_single", type=StringType)
typetranslation_MyClass_ecore_eresource_multi: Property = Property(name="ecore_eresource_multi", type=StringType)
typetranslation_MyClass_ecore_eelist_single: Property = Property(name="ecore_eelist_single", type=StringType)
typetranslation_MyClass_ecore_eresourceset_single: Property = Property(name="ecore_eresourceset_single", type=StringType)
typetranslation_MyClass_ecore_eresourceset_multi: Property = Property(name="ecore_eresourceset_multi", type=StringType)
typetranslation_MyClass_ecore_eshort_single: Property = Property(name="ecore_eshort_single", type=StringType)
typetranslation_MyClass_ecore_eshort_multi: Property = Property(name="ecore_eshort_multi", type=StringType)
typetranslation_MyClass_ecore_eshortobject_single: Property = Property(name="ecore_eshortobject_single", type=StringType)
typetranslation_MyClass_ecore_eshortobject_multi: Property = Property(name="ecore_eshortobject_multi", type=StringType)
typetranslation_MyClass_ecore_estring_single: Property = Property(name="ecore_estring_single", type=StringType)
typetranslation_MyClass_ecore_estring_multi: Property = Property(name="ecore_estring_multi", type=StringType)
typetranslation_MyClass_ecore_etreeiterator_single: Property = Property(name="ecore_etreeiterator_single", type=StringType)
typetranslation_MyClass_ecore_etreeiterator_multi: Property = Property(name="ecore_etreeiterator_multi", type=StringType)
typetranslation_MyClass_ecore_einvocationtargetexception_single: Property = Property(name="ecore_einvocationtargetexception_single", type=StringType)
typetranslation_MyClass_ecore_einvocationtargetexception_multi: Property = Property(name="ecore_einvocationtargetexception_multi", type=StringType)
typetranslation_MyClass_m_operation_void: Method = Method(name="operation_void", parameters={})
typetranslation_MyClass_m_operation_ebigdecimal: Method = Method(name="operation_ebigdecimal", parameters={}, type=StringType)
typetranslation_MyClass_m_operation_ebiginteger: Method = Method(name="operation_ebiginteger", parameters={}, type=StringType)
typetranslation_MyClass_m_operation_eboolean: Method = Method(name="operation_eboolean", parameters={}, type=BooleanType)
typetranslation_MyClass_m_operation_ebooleanobject: Method = Method(name="operation_ebooleanobject", parameters={}, type=StringType)
typetranslation_MyClass_m_operation_ebyte: Method = Method(name="operation_ebyte", parameters={}, type=StringType)
typetranslation_MyClass_m_operation_ebytearray: Method = Method(name="operation_ebytearray", parameters={}, type=StringType)
typetranslation_MyClass_m_operation_ebyteobject: Method = Method(name="operation_ebyteobject", parameters={}, type=StringType)
typetranslation_MyClass_m_operation_echar: Method = Method(name="operation_echar", parameters={}, type=StringType)
typetranslation_MyClass_m_operation_echaracterobject: Method = Method(name="operation_echaracterobject", parameters={}, type=StringType)
typetranslation_MyClass_m_operation_edate: Method = Method(name="operation_edate", parameters={}, type=DateType)
typetranslation_MyClass_m_operation_ediagnosticchain: Method = Method(name="operation_ediagnosticchain", parameters={}, type=StringType)
typetranslation_MyClass_m_operation_edouble: Method = Method(name="operation_edouble", parameters={}, type=FloatType)
typetranslation_MyClass_m_operation_edoubleobject: Method = Method(name="operation_edoubleobject", parameters={}, type=StringType)
typetranslation_MyClass_m_operation_eelist: Method = Method(name="operation_eelist", parameters={}, type=StringType)
typetranslation_MyClass_m_operation_eenumerator: Method = Method(name="operation_eenumerator", parameters={}, type=StringType)
typetranslation_MyClass_m_operation_efeaturemap: Method = Method(name="operation_efeaturemap", parameters={}, type=StringType)
typetranslation_MyClass_m_operation_efeaturemapentry: Method = Method(name="operation_efeaturemapentry", parameters={}, type=StringType)
typetranslation_MyClass_m_operation_efloat: Method = Method(name="operation_efloat", parameters={}, type=FloatType)
typetranslation_MyClass_m_operation_efloatobject: Method = Method(name="operation_efloatobject", parameters={}, type=StringType)
typetranslation_MyClass_m_operation_eint: Method = Method(name="operation_eint", parameters={}, type=IntegerType)
typetranslation_MyClass_m_operation_eintegerobject: Method = Method(name="operation_eintegerobject", parameters={}, type=StringType)
typetranslation_MyClass_m_operation_ejavaclass: Method = Method(name="operation_ejavaclass", parameters={}, type=StringType)
typetranslation_MyClass_m_operation_ejavaobject: Method = Method(name="operation_ejavaobject", parameters={}, type=StringType)
typetranslation_MyClass_m_operation_elong: Method = Method(name="operation_elong", parameters={}, type=StringType)
typetranslation_MyClass_m_operation_elongobject: Method = Method(name="operation_elongobject", parameters={}, type=StringType)
typetranslation_MyClass_m_operation_emap: Method = Method(name="operation_emap", parameters={}, type=StringType)
typetranslation_MyClass_m_operation_eresource: Method = Method(name="operation_eresource", parameters={}, type=StringType)
typetranslation_MyClass_m_operation_eresourceset: Method = Method(name="operation_eresourceset", parameters={}, type=StringType)
typetranslation_MyClass_m_operation_eshort: Method = Method(name="operation_eshort", parameters={}, type=StringType)
typetranslation_MyClass_m_operation_eshortobject: Method = Method(name="operation_eshortobject", parameters={}, type=StringType)
typetranslation_MyClass_m_operation_estring: Method = Method(name="operation_estring", parameters={}, type=StringType)
typetranslation_MyClass_m_operation_etreeiterator: Method = Method(name="operation_etreeiterator", parameters={}, type=StringType)
typetranslation_MyClass_m_operation_einvocationtargetexception: Method = Method(name="operation_einvocationtargetexception", parameters={}, type=StringType)
typetranslation_MyClass.attributes={typetranslation_MyClass_ecore_efloatobject_multi, typetranslation_MyClass_ecore_eshortobject_multi, typetranslation_MyClass_ecore_ediagnosticchain_multi, typetranslation_MyClass_ocl_string_single, typetranslation_MyClass_ecore_edoubleobject_single, typetranslation_MyClass_ecore_elongobject_multi, typetranslation_MyClass_ecore_eshortobject_single, typetranslation_MyClass_ecore_ebiginteger_multi, typetranslation_MyClass_ecore_eint_multi, typetranslation_MyClass_ecore_etreeiterator_multi, typetranslation_MyClass_ecore_eintegerobject_multi, typetranslation_MyClass_ecore_eenumerator_multi, typetranslation_MyClass_ecore_eint_single, typetranslation_MyClass_ocl_integer_multi, typetranslation_MyClass_ecore_eboolean_single, typetranslation_MyClass_ecore_ebooleanobject_multi, typetranslation_MyClass_ecore_eresourceset_multi, typetranslation_MyClass_ecore_ejavaobject_single, typetranslation_MyClass_ecore_eresource_single, typetranslation_MyClass_ecore_ejavaobject_multi, typetranslation_MyClass_ecore_emap_single, typetranslation_MyClass_ecore_edate_single, typetranslation_MyClass_ecore_eshort_multi, typetranslation_MyClass_ecore_edoubleobject_multi, typetranslation_MyClass_ecore_ebyteobject_single, typetranslation_MyClass_ecore_ebooleanobject_single, typetranslation_MyClass_ecore_echaracterobject_multi, typetranslation_MyClass_ecore_efloat_single, typetranslation_MyClass_ecore_etreeiterator_single, typetranslation_MyClass_ecore_ejavaclass_single, typetranslation_MyClass_ecore_eresource_multi, typetranslation_MyClass_ocl_boolean_single, typetranslation_MyClass_ocl_real_single, typetranslation_MyClass_ecore_edouble_multi, typetranslation_MyClass_ecore_emap_multi, typetranslation_MyClass_ecore_ebiginteger_single, typetranslation_MyClass_ecore_efeaturemap_single, typetranslation_MyClass_ecore_eboolean_multi, typetranslation_MyClass_ecore_ebytearray_multi, typetranslation_MyClass_ecore_eelist_multi, typetranslation_MyClass_ecore_elong_single, typetranslation_MyClass_ecore_elong_multi, typetranslation_MyClass_ecore_efloat_multi, typetranslation_MyClass_ecore_ebyteobject_multi, typetranslation_MyClass_ecore_ediagnosticchain_single, typetranslation_MyClass_ocl_boolean_multi, typetranslation_MyClass_ecore_efloatobject_single, typetranslation_MyClass_ecore_efeaturemapentry_single, typetranslation_MyClass_ecore_einvocationtargetexception_multi, typetranslation_MyClass_ecore_edouble_single, typetranslation_MyClass_ocl_integer_single, typetranslation_MyClass_ecore_efeaturemapentry_multi, typetranslation_MyClass_ecore_eintegerobject_single, typetranslation_MyClass_ecore_eenumerator_single, typetranslation_MyClass_ecore_eresourceset_single, typetranslation_MyClass_ecore_ebytearray_single, typetranslation_MyClass_ecore_eshort_single, typetranslation_MyClass_ocl_string_multi, typetranslation_MyClass_ecore_ebyte_single, typetranslation_MyClass_ecore_efeaturemap_multi, typetranslation_MyClass_ecore_ebigdecimal_multi, typetranslation_MyClass_ecore_ejavaclass_multi, typetranslation_MyClass_ecore_estring_single, typetranslation_MyClass_ecore_edate_multi, typetranslation_MyClass_ocl_real_multi, typetranslation_MyClass_ecore_echar_single, typetranslation_MyClass_ecore_echar_multi, typetranslation_MyClass_ecore_estring_multi, typetranslation_MyClass_ecore_elongobject_single, typetranslation_MyClass_ecore_einvocationtargetexception_single, typetranslation_MyClass_ecore_ebyte_multi, typetranslation_MyClass_ecore_eelist_single, typetranslation_MyClass_ecore_ebigdecimal_single, typetranslation_MyClass_ecore_echaracterobject_single}
typetranslation_MyClass.methods={typetranslation_MyClass_m_operation_efloatobject, typetranslation_MyClass_m_operation_eintegerobject, typetranslation_MyClass_m_operation_etreeiterator, typetranslation_MyClass_m_operation_edoubleobject, typetranslation_MyClass_m_operation_ejavaclass, typetranslation_MyClass_m_operation_estring, typetranslation_MyClass_m_operation_eelist, typetranslation_MyClass_m_operation_eenumerator, typetranslation_MyClass_m_operation_echaracterobject, typetranslation_MyClass_m_operation_ediagnosticchain, typetranslation_MyClass_m_operation_ebyteobject, typetranslation_MyClass_m_operation_eresourceset, typetranslation_MyClass_m_operation_ebigdecimal, typetranslation_MyClass_m_operation_ebiginteger, typetranslation_MyClass_m_operation_efeaturemap, typetranslation_MyClass_m_operation_efeaturemapentry, typetranslation_MyClass_m_operation_ejavaobject, typetranslation_MyClass_m_operation_edouble, typetranslation_MyClass_m_operation_einvocationtargetexception, typetranslation_MyClass_m_operation_void, typetranslation_MyClass_m_operation_eint, typetranslation_MyClass_m_operation_elongobject, typetranslation_MyClass_m_operation_eshort, typetranslation_MyClass_m_operation_emap, typetranslation_MyClass_m_operation_eshortobject, typetranslation_MyClass_m_operation_elong, typetranslation_MyClass_m_operation_efloat, typetranslation_MyClass_m_operation_ebyte, typetranslation_MyClass_m_operation_ebytearray, typetranslation_MyClass_m_operation_edate, typetranslation_MyClass_m_operation_eboolean, typetranslation_MyClass_m_operation_echar, typetranslation_MyClass_m_operation_ebooleanobject, typetranslation_MyClass_m_operation_eresource}

# typetranslation_AbstractClass class attributes and methods

# Domain Model
domain_model = DomainModel(
    name="typetranslation",
    types={typetranslation_MyClass, typetranslation_AbstractClass, MyEnumeration},
    associations={},
    generalizations={},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)