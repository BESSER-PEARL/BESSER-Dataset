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
AttributeType: Enumeration = Enumeration(
    name="AttributeType",
    literals={
            EnumerationLiteral(name="primaryKey"),
			EnumerationLiteral(name="ordinary")
    }
)

Multiplicity_enum: Enumeration = Enumeration(
    name="Multiplicity",
    literals={
            EnumerationLiteral(name="one_to_many"),
			EnumerationLiteral(name="many_to_one"),
			EnumerationLiteral(name="one_to_one")
    }
)

TipoModelElementEntity: Enumeration = Enumeration(
    name="TipoModelElementEntity",
    literals={
            EnumerationLiteral(name="entity"),
			EnumerationLiteral(name="relation")
    }
)

Type: Enumeration = Enumeration(
    name="Type",
    literals={
            EnumerationLiteral(name="string"),
			EnumerationLiteral(name="int"),
			EnumerationLiteral(name="float"),
			EnumerationLiteral(name="date")
    }
)

NombreCampo: Enumeration = Enumeration(
    name="NombreCampo",
    literals={
            EnumerationLiteral(name="ID"),
			EnumerationLiteral(name="ESTADO_TRANSACCION"),
			EnumerationLiteral(name="HORA"),
			EnumerationLiteral(name="TIPO"),
			EnumerationLiteral(name="DESCRIPCION"),
			EnumerationLiteral(name="CATEGORIA"),
			EnumerationLiteral(name="VALOR"),
			EnumerationLiteral(name="CADENA_TRAMA"),
			EnumerationLiteral(name="NUMERO_MOVIL"),
			EnumerationLiteral(name="FECHA"),
			EnumerationLiteral(name="CEDULA_CONDUCTOR"),
			EnumerationLiteral(name="CONDUCTOR"),
			EnumerationLiteral(name="TOTAL"),
			EnumerationLiteral(name="TOTAL_RECAUDO_BRUTO"),
			EnumerationLiteral(name="TOTAL_RECAUDO_NETO"),
			EnumerationLiteral(name="TOTAL_DEPOSITO"),
			EnumerationLiteral(name="TOTAL_GASTOS"),
			EnumerationLiteral(name="LIQUIDADO"),
			EnumerationLiteral(name="USUARIO"),
			EnumerationLiteral(name="NOMBRE_PERSONA"),
			EnumerationLiteral(name="APELLIDO"),
			EnumerationLiteral(name="CEDULA"),
			EnumerationLiteral(name="HORA_MODIFICACION"),
			EnumerationLiteral(name="NOMBRE"),
			EnumerationLiteral(name="REGISTRO"),
			EnumerationLiteral(name="TOTAL_RECAUDO_TARIFA"),
			EnumerationLiteral(name="REGISTRO_RECAUDO"),
			EnumerationLiteral(name="COSTO_TARIFA"),
			EnumerationLiteral(name="RUTA_DESPACHO"),
			EnumerationLiteral(name="HORA_DESPACHO"),
			EnumerationLiteral(name="REGISTRO_CONSOLIDADO"),
			EnumerationLiteral(name="TOTAL_RECAUDO_RUTO"),
			EnumerationLiteral(name="TOTAL_RECAUDO_DESPACHO"),
			EnumerationLiteral(name="ESTADO_CONSOLIDADO"),
			EnumerationLiteral(name="ESTADO_IMPRESION"),
			EnumerationLiteral(name="default")
    }
)

# Classes
gestionmodelosconsultas_ModelFactory = Class(name="gestionmodelosconsultas_ModelFactory")
factoryrules_RulesFactory = Class(name="factoryrules_RulesFactory")
FactoryModeloConsulta = Class(name="FactoryModeloConsulta")
DiagramEntity = Class(name="DiagramEntity")
gestionmodelosconsultas_factoryrules_RulesFactory = Class(name="gestionmodelosconsultas_factoryrules_RulesFactory")
factoryrules_gestionmodelosconsultas_ModelFactory = Class(name="factoryrules_gestionmodelosconsultas_ModelFactory")
factoryrules_Rule = Class(name="factoryrules_Rule")
factoryrules_ChildRule = Class(name="factoryrules_ChildRule")
gestionmodelosconsultas_factoryrules_ChildRule = Class(name="gestionmodelosconsultas_factoryrules_ChildRule", is_abstract=True)
gestionmodelosconsultas_factoryrules_EntityName = Class(name="gestionmodelosconsultas_factoryrules_EntityName")
ChildRule = Class(name="ChildRule")
gestionmodelosconsultas_factoryrules_RelationName = Class(name="gestionmodelosconsultas_factoryrules_RelationName")
gestionmodelosconsultas_entitymodel_Entity = Class(name="gestionmodelosconsultas_entitymodel_Entity")
ModelElementEntity = Class(name="ModelElementEntity")
Attribute = Class(name="Attribute")
gestionmodelosconsultas_entitymodel_EntityRelation = Class(name="gestionmodelosconsultas_entitymodel_EntityRelation")
Entity = Class(name="Entity")
gestionmodelosconsultas_factoryrules_Rule = Class(name="gestionmodelosconsultas_factoryrules_Rule")
ElementoRealizacionValueAttribute = Class(name="ElementoRealizacionValueAttribute")
ElementoRealizacionVisibleAttribute = Class(name="ElementoRealizacionVisibleAttribute")
gestionmodelosconsultas_entitymodel_ModelElementEntity = Class(name="gestionmodelosconsultas_entitymodel_ModelElementEntity", is_abstract=True)
ElementoRealizacionDiagramEntity = Class(name="ElementoRealizacionDiagramEntity")
gestionmodelosconsultas_entitymodel_DiagramEntity = Class(name="gestionmodelosconsultas_entitymodel_DiagramEntity")
entitymodel_gestionmodelosconsultas_ModelFactory = Class(name="entitymodel_gestionmodelosconsultas_ModelFactory")
gestionmodelosconsultas_entitymodel_RealizacionDiagramEntity = Class(name="gestionmodelosconsultas_entitymodel_RealizacionDiagramEntity")
ModeloConsulta = Class(name="ModeloConsulta")
gestionmodelosconsultas_entitymodel_SimpleRelation = Class(name="gestionmodelosconsultas_entitymodel_SimpleRelation")
EntityRelation = Class(name="EntityRelation")
gestionmodelosconsultas_entitymodel_AssociativeEntity = Class(name="gestionmodelosconsultas_entitymodel_AssociativeEntity")
gestionmodelosconsultas_entitymodel_Attribute = Class(name="gestionmodelosconsultas_entitymodel_Attribute")
RealizacionDiagramEntity = Class(name="RealizacionDiagramEntity")
gestionmodelosconsultas_entitymodel_ElementoRealizacionValueAttribute = Class(name="gestionmodelosconsultas_entitymodel_ElementoRealizacionValueAttribute")
Value = Class(name="Value")
gestionmodelosconsultas_entitymodel_ElementoRealizacionDiagramEntity = Class(name="gestionmodelosconsultas_entitymodel_ElementoRealizacionDiagramEntity")
gestionmodelosconsultas_entitymodel_Value = Class(name="gestionmodelosconsultas_entitymodel_Value")
gestionmodelosconsultas_modeloconsultas_ModeloConsulta = Class(name="gestionmodelosconsultas_modeloconsultas_ModeloConsulta")
model_EADiagram = Class(name="model_EADiagram")
resultset_Resultado = Class(name="resultset_Resultado")
gestionmodelosconsultas_modeloconsultas_FactoryModeloConsulta = Class(name="gestionmodelosconsultas_modeloconsultas_FactoryModeloConsulta")
modeloconsultas_gestionmodelosconsultas_ModelFactory = Class(name="modeloconsultas_gestionmodelosconsultas_ModelFactory")
gestionmodelosconsultas_model_Relacion = Class(name="gestionmodelosconsultas_model_Relacion")
ElementoModelo = Class(name="ElementoModelo")
gestionmodelosconsultas_entitymodel_ElementoRealizacionVisibleAttribute = Class(name="gestionmodelosconsultas_entitymodel_ElementoRealizacionVisibleAttribute")
gestionmodelosconsultas_model_Campo = Class(name="gestionmodelosconsultas_model_Campo")
gestionmodelosconsultas_model_EADiagram = Class(name="gestionmodelosconsultas_model_EADiagram", is_abstract=True)
model_ElementoConsulta = Class(name="model_ElementoConsulta")
gestionmodelosconsultas_model_ViewModel = Class(name="gestionmodelosconsultas_model_ViewModel")
EADiagram = Class(name="EADiagram")
gestionmodelosconsultas_model_ElementoConsulta = Class(name="gestionmodelosconsultas_model_ElementoConsulta", is_abstract=True)
model_Campo = Class(name="model_Campo")
gestionmodelosconsultas_model_Proyeccion = Class(name="gestionmodelosconsultas_model_Proyeccion")
gestionmodelosconsultas_model_ElementoModelo = Class(name="gestionmodelosconsultas_model_ElementoModelo")
model_ElementoModelo = Class(name="model_ElementoModelo")
gestionmodelosconsultas_resultset_Resultado = Class(name="gestionmodelosconsultas_resultset_Resultado")
resultset_ResultElement = Class(name="resultset_ResultElement")
gestionmodelosconsultas_resultset_ElementoModeloResultado = Class(name="gestionmodelosconsultas_resultset_ElementoModeloResultado", is_abstract=True)
ResultElement = Class(name="ResultElement")
resultset_ElementoModeloResultado = Class(name="resultset_ElementoModeloResultado")
model_Relacion = Class(name="model_Relacion")
ElementoModeloResultado = Class(name="ElementoModeloResultado")
gestionmodelosconsultas_resultcotracir_Trama = Class(name="gestionmodelosconsultas_resultcotracir_Trama")
gestionmodelosconsultas_resultcotracir_Consolidado = Class(name="gestionmodelosconsultas_resultcotracir_Consolidado")
gestionmodelosconsultas_resultcotracir_Propietario = Class(name="gestionmodelosconsultas_resultcotracir_Propietario")
gestionmodelosconsultas_resultcotracir_Planilla = Class(name="gestionmodelosconsultas_resultcotracir_Planilla")
gestionmodelosconsultas_resultset_ResultElement = Class(name="gestionmodelosconsultas_resultset_ResultElement", is_abstract=True)
gestionmodelosconsultas_resultcotracir_Transaccion = Class(name="gestionmodelosconsultas_resultcotracir_Transaccion")
gestionmodelosconsultas_resultcotracir_NewClass = Class(name="gestionmodelosconsultas_resultcotracir_NewClass")
gestionmodelosconsultas_resultcotracir_Detallado = Class(name="gestionmodelosconsultas_resultcotracir_Detallado")
gestionmodelosconsultas_cotracir_Planilla = Class(name="gestionmodelosconsultas_cotracir_Planilla")
gestionmodelosconsultas_cotracir_Transaccion = Class(name="gestionmodelosconsultas_cotracir_Transaccion")
gestionmodelosconsultas_cotracir_Trama = Class(name="gestionmodelosconsultas_cotracir_Trama")
gestionmodelosconsultas_cotracir_Propietario = Class(name="gestionmodelosconsultas_cotracir_Propietario")
gestionmodelosconsultas_cotracir_Detallado = Class(name="gestionmodelosconsultas_cotracir_Detallado")
ElementoConsulta = Class(name="ElementoConsulta")
gestionmodelosconsultas_cotracir_Consolidado = Class(name="gestionmodelosconsultas_cotracir_Consolidado")

# gestionmodelosconsultas_ModelFactory class attributes and methods
gestionmodelosconsultas_ModelFactory_m_cargar: Method = Method(name="cargar", parameters={}, type=StringType)
gestionmodelosconsultas_ModelFactory_m_salvar: Method = Method(name="salvar", parameters={})
gestionmodelosconsultas_ModelFactory.methods={gestionmodelosconsultas_ModelFactory_m_cargar, gestionmodelosconsultas_ModelFactory_m_salvar}

# factoryrules_RulesFactory class attributes and methods

# FactoryModeloConsulta class attributes and methods

# DiagramEntity class attributes and methods

# gestionmodelosconsultas_factoryrules_RulesFactory class attributes and methods

# factoryrules_gestionmodelosconsultas_ModelFactory class attributes and methods

# factoryrules_Rule class attributes and methods

# factoryrules_ChildRule class attributes and methods

# gestionmodelosconsultas_factoryrules_ChildRule class attributes and methods
gestionmodelosconsultas_factoryrules_ChildRule_name: Property = Property(name="name", type=StringType)
gestionmodelosconsultas_factoryrules_ChildRule.attributes={gestionmodelosconsultas_factoryrules_ChildRule_name}

# gestionmodelosconsultas_factoryrules_EntityName class attributes and methods

# ChildRule class attributes and methods

# gestionmodelosconsultas_factoryrules_RelationName class attributes and methods

# gestionmodelosconsultas_entitymodel_Entity class attributes and methods

# ModelElementEntity class attributes and methods

# Attribute class attributes and methods

# gestionmodelosconsultas_entitymodel_EntityRelation class attributes and methods
gestionmodelosconsultas_entitymodel_EntityRelation_atributteForeingKeySource: Property = Property(name="atributteForeingKeySource", type=StringType)
gestionmodelosconsultas_entitymodel_EntityRelation_atributtePrimaryKeyTarget: Property = Property(name="atributtePrimaryKeyTarget", type=StringType)
gestionmodelosconsultas_entitymodel_EntityRelation_multiplicitySource: Property = Property(name="multiplicitySource", type=StringType)
gestionmodelosconsultas_entitymodel_EntityRelation_multiplicityTarget: Property = Property(name="multiplicityTarget", type=StringType)
gestionmodelosconsultas_entitymodel_EntityRelation.attributes={gestionmodelosconsultas_entitymodel_EntityRelation_atributtePrimaryKeyTarget, gestionmodelosconsultas_entitymodel_EntityRelation_atributteForeingKeySource, gestionmodelosconsultas_entitymodel_EntityRelation_multiplicityTarget, gestionmodelosconsultas_entitymodel_EntityRelation_multiplicitySource}

# Entity class attributes and methods

# gestionmodelosconsultas_factoryrules_Rule class attributes and methods
gestionmodelosconsultas_factoryrules_Rule_name: Property = Property(name="name", type=StringType)
gestionmodelosconsultas_factoryrules_Rule.attributes={gestionmodelosconsultas_factoryrules_Rule_name}

# ElementoRealizacionValueAttribute class attributes and methods

# ElementoRealizacionVisibleAttribute class attributes and methods

# gestionmodelosconsultas_entitymodel_ModelElementEntity class attributes and methods
gestionmodelosconsultas_entitymodel_ModelElementEntity_name: Property = Property(name="name", type=StringType)
gestionmodelosconsultas_entitymodel_ModelElementEntity_stereotype: Property = Property(name="stereotype", type=StringType)
gestionmodelosconsultas_entitymodel_ModelElementEntity.attributes={gestionmodelosconsultas_entitymodel_ModelElementEntity_name, gestionmodelosconsultas_entitymodel_ModelElementEntity_stereotype}

# ElementoRealizacionDiagramEntity class attributes and methods

# gestionmodelosconsultas_entitymodel_DiagramEntity class attributes and methods

# entitymodel_gestionmodelosconsultas_ModelFactory class attributes and methods

# gestionmodelosconsultas_entitymodel_RealizacionDiagramEntity class attributes and methods

# ModeloConsulta class attributes and methods

# gestionmodelosconsultas_entitymodel_SimpleRelation class attributes and methods

# EntityRelation class attributes and methods

# gestionmodelosconsultas_entitymodel_AssociativeEntity class attributes and methods

# gestionmodelosconsultas_entitymodel_Attribute class attributes and methods
gestionmodelosconsultas_entitymodel_Attribute_type: Property = Property(name="type", type=StringType)
gestionmodelosconsultas_entitymodel_Attribute_value: Property = Property(name="value", type=StringType)
gestionmodelosconsultas_entitymodel_Attribute_visible: Property = Property(name="visible", type=BooleanType)
gestionmodelosconsultas_entitymodel_Attribute_attributeType: Property = Property(name="attributeType", type=StringType)
gestionmodelosconsultas_entitymodel_Attribute_name: Property = Property(name="name", type=StringType)
gestionmodelosconsultas_entitymodel_Attribute.attributes={gestionmodelosconsultas_entitymodel_Attribute_visible, gestionmodelosconsultas_entitymodel_Attribute_type, gestionmodelosconsultas_entitymodel_Attribute_name, gestionmodelosconsultas_entitymodel_Attribute_value, gestionmodelosconsultas_entitymodel_Attribute_attributeType}

# RealizacionDiagramEntity class attributes and methods

# gestionmodelosconsultas_entitymodel_ElementoRealizacionValueAttribute class attributes and methods
gestionmodelosconsultas_entitymodel_ElementoRealizacionValueAttribute_nombre: Property = Property(name="nombre", type=StringType)
gestionmodelosconsultas_entitymodel_ElementoRealizacionValueAttribute.attributes={gestionmodelosconsultas_entitymodel_ElementoRealizacionValueAttribute_nombre}

# Value class attributes and methods

# gestionmodelosconsultas_entitymodel_ElementoRealizacionDiagramEntity class attributes and methods
gestionmodelosconsultas_entitymodel_ElementoRealizacionDiagramEntity_nombreModelElementEntity: Property = Property(name="nombreModelElementEntity", type=StringType)
gestionmodelosconsultas_entitymodel_ElementoRealizacionDiagramEntity_tipo: Property = Property(name="tipo", type=StringType)
gestionmodelosconsultas_entitymodel_ElementoRealizacionDiagramEntity.attributes={gestionmodelosconsultas_entitymodel_ElementoRealizacionDiagramEntity_nombreModelElementEntity, gestionmodelosconsultas_entitymodel_ElementoRealizacionDiagramEntity_tipo}

# gestionmodelosconsultas_entitymodel_Value class attributes and methods
gestionmodelosconsultas_entitymodel_Value_value: Property = Property(name="value", type=StringType)
gestionmodelosconsultas_entitymodel_Value.attributes={gestionmodelosconsultas_entitymodel_Value_value}

# gestionmodelosconsultas_modeloconsultas_ModeloConsulta class attributes and methods
gestionmodelosconsultas_modeloconsultas_ModeloConsulta_nombre: Property = Property(name="nombre", type=StringType)
gestionmodelosconsultas_modeloconsultas_ModeloConsulta.attributes={gestionmodelosconsultas_modeloconsultas_ModeloConsulta_nombre}

# model_EADiagram class attributes and methods

# resultset_Resultado class attributes and methods

# gestionmodelosconsultas_modeloconsultas_FactoryModeloConsulta class attributes and methods

# modeloconsultas_gestionmodelosconsultas_ModelFactory class attributes and methods

# gestionmodelosconsultas_model_Relacion class attributes and methods
gestionmodelosconsultas_model_Relacion_estereotipo: Property = Property(name="estereotipo", type=StringType)
gestionmodelosconsultas_model_Relacion_order: Property = Property(name="order", type=StringType)
gestionmodelosconsultas_model_Relacion.attributes={gestionmodelosconsultas_model_Relacion_order, gestionmodelosconsultas_model_Relacion_estereotipo}

# ElementoModelo class attributes and methods

# gestionmodelosconsultas_entitymodel_ElementoRealizacionVisibleAttribute class attributes and methods
gestionmodelosconsultas_entitymodel_ElementoRealizacionVisibleAttribute_nombre: Property = Property(name="nombre", type=StringType)
gestionmodelosconsultas_entitymodel_ElementoRealizacionVisibleAttribute.attributes={gestionmodelosconsultas_entitymodel_ElementoRealizacionVisibleAttribute_nombre}

# gestionmodelosconsultas_model_Campo class attributes and methods
gestionmodelosconsultas_model_Campo_nombreCampo: Property = Property(name="nombreCampo", type=StringType)
gestionmodelosconsultas_model_Campo_criterio: Property = Property(name="criterio", type=StringType)
gestionmodelosconsultas_model_Campo_seleccion: Property = Property(name="seleccion", type=BooleanType)
gestionmodelosconsultas_model_Campo.attributes={gestionmodelosconsultas_model_Campo_seleccion, gestionmodelosconsultas_model_Campo_criterio, gestionmodelosconsultas_model_Campo_nombreCampo}

# gestionmodelosconsultas_model_EADiagram class attributes and methods
gestionmodelosconsultas_model_EADiagram_nombre: Property = Property(name="nombre", type=StringType)
gestionmodelosconsultas_model_EADiagram.attributes={gestionmodelosconsultas_model_EADiagram_nombre}

# model_ElementoConsulta class attributes and methods

# gestionmodelosconsultas_model_ViewModel class attributes and methods

# EADiagram class attributes and methods

# gestionmodelosconsultas_model_ElementoConsulta class attributes and methods
gestionmodelosconsultas_model_ElementoConsulta_order: Property = Property(name="order", type=StringType)
gestionmodelosconsultas_model_ElementoConsulta.attributes={gestionmodelosconsultas_model_ElementoConsulta_order}

# model_Campo class attributes and methods

# gestionmodelosconsultas_model_Proyeccion class attributes and methods

# gestionmodelosconsultas_model_ElementoModelo class attributes and methods
gestionmodelosconsultas_model_ElementoModelo_nombre: Property = Property(name="nombre", type=StringType)
gestionmodelosconsultas_model_ElementoModelo.attributes={gestionmodelosconsultas_model_ElementoModelo_nombre}

# model_ElementoModelo class attributes and methods

# gestionmodelosconsultas_resultset_Resultado class attributes and methods
gestionmodelosconsultas_resultset_Resultado_nombre: Property = Property(name="nombre", type=StringType)
gestionmodelosconsultas_resultset_Resultado.attributes={gestionmodelosconsultas_resultset_Resultado_nombre}

# resultset_ResultElement class attributes and methods

# gestionmodelosconsultas_resultset_ElementoModeloResultado class attributes and methods
gestionmodelosconsultas_resultset_ElementoModeloResultado_key: Property = Property(name="key", type=StringType)
gestionmodelosconsultas_resultset_ElementoModeloResultado.attributes={gestionmodelosconsultas_resultset_ElementoModeloResultado_key}

# ResultElement class attributes and methods

# resultset_ElementoModeloResultado class attributes and methods

# model_Relacion class attributes and methods

# ElementoModeloResultado class attributes and methods

# gestionmodelosconsultas_resultcotracir_Trama class attributes and methods
gestionmodelosconsultas_resultcotracir_Trama_ID: Property = Property(name="ID", type=StringType)
gestionmodelosconsultas_resultcotracir_Trama_CADENA_TRAMA: Property = Property(name="CADENA_TRAMA", type=StringType)
gestionmodelosconsultas_resultcotracir_Trama.attributes={gestionmodelosconsultas_resultcotracir_Trama_ID, gestionmodelosconsultas_resultcotracir_Trama_CADENA_TRAMA}

# gestionmodelosconsultas_resultcotracir_Consolidado class attributes and methods
gestionmodelosconsultas_resultcotracir_Consolidado_ID: Property = Property(name="ID", type=StringType)
gestionmodelosconsultas_resultcotracir_Consolidado_RUTA_DESPACHO: Property = Property(name="RUTA_DESPACHO", type=StringType)
gestionmodelosconsultas_resultcotracir_Consolidado_HORA_DESPACHO: Property = Property(name="HORA_DESPACHO", type=StringType)
gestionmodelosconsultas_resultcotracir_Consolidado_REGISTRO_CONSOLIDADO: Property = Property(name="REGISTRO_CONSOLIDADO", type=StringType)
gestionmodelosconsultas_resultcotracir_Consolidado_TOTAL_RECAUDO_BRUTO: Property = Property(name="TOTAL_RECAUDO_BRUTO", type=StringType)
gestionmodelosconsultas_resultcotracir_Consolidado_TOTAL_RECAUDO_DESPACHO: Property = Property(name="TOTAL_RECAUDO_DESPACHO", type=StringType)
gestionmodelosconsultas_resultcotracir_Consolidado_ESTADO_CONSOLIDADO: Property = Property(name="ESTADO_CONSOLIDADO", type=StringType)
gestionmodelosconsultas_resultcotracir_Consolidado_ESTADO_IMPRESION: Property = Property(name="ESTADO_IMPRESION", type=StringType)
gestionmodelosconsultas_resultcotracir_Consolidado.attributes={gestionmodelosconsultas_resultcotracir_Consolidado_REGISTRO_CONSOLIDADO, gestionmodelosconsultas_resultcotracir_Consolidado_ESTADO_IMPRESION, gestionmodelosconsultas_resultcotracir_Consolidado_RUTA_DESPACHO, gestionmodelosconsultas_resultcotracir_Consolidado_HORA_DESPACHO, gestionmodelosconsultas_resultcotracir_Consolidado_ESTADO_CONSOLIDADO, gestionmodelosconsultas_resultcotracir_Consolidado_ID, gestionmodelosconsultas_resultcotracir_Consolidado_TOTAL_RECAUDO_BRUTO, gestionmodelosconsultas_resultcotracir_Consolidado_TOTAL_RECAUDO_DESPACHO}

# gestionmodelosconsultas_resultcotracir_Propietario class attributes and methods
gestionmodelosconsultas_resultcotracir_Propietario_ID: Property = Property(name="ID", type=StringType)
gestionmodelosconsultas_resultcotracir_Propietario_NOMBRE: Property = Property(name="NOMBRE", type=StringType)
gestionmodelosconsultas_resultcotracir_Propietario_CEDULA: Property = Property(name="CEDULA", type=StringType)
gestionmodelosconsultas_resultcotracir_Propietario.attributes={gestionmodelosconsultas_resultcotracir_Propietario_CEDULA, gestionmodelosconsultas_resultcotracir_Propietario_NOMBRE, gestionmodelosconsultas_resultcotracir_Propietario_ID}

# gestionmodelosconsultas_resultcotracir_Planilla class attributes and methods
gestionmodelosconsultas_resultcotracir_Planilla_ID: Property = Property(name="ID", type=StringType)
gestionmodelosconsultas_resultcotracir_Planilla_NUMERO_MOVIL: Property = Property(name="NUMERO_MOVIL", type=StringType)
gestionmodelosconsultas_resultcotracir_Planilla_FECHA: Property = Property(name="FECHA", type=StringType)
gestionmodelosconsultas_resultcotracir_Planilla_CEDULA_CONDUCTOR: Property = Property(name="CEDULA_CONDUCTOR", type=StringType)
gestionmodelosconsultas_resultcotracir_Planilla_CONDUCTOR: Property = Property(name="CONDUCTOR", type=StringType)
gestionmodelosconsultas_resultcotracir_Planilla_TOTAL: Property = Property(name="TOTAL", type=StringType)
gestionmodelosconsultas_resultcotracir_Planilla_TOTAL_RECAUDO_BRUTO: Property = Property(name="TOTAL_RECAUDO_BRUTO", type=StringType)
gestionmodelosconsultas_resultcotracir_Planilla_TOTAL_RECAUDO_NETO: Property = Property(name="TOTAL_RECAUDO_NETO", type=StringType)
gestionmodelosconsultas_resultcotracir_Planilla_TOTAL_GASTOS: Property = Property(name="TOTAL_GASTOS", type=StringType)
gestionmodelosconsultas_resultcotracir_Planilla_LIQUIDADO: Property = Property(name="LIQUIDADO", type=StringType)
gestionmodelosconsultas_resultcotracir_Planilla_USUARIO: Property = Property(name="USUARIO", type=StringType)
gestionmodelosconsultas_resultcotracir_Planilla_NOMBRE_PERSONA: Property = Property(name="NOMBRE_PERSONA", type=StringType)
gestionmodelosconsultas_resultcotracir_Planilla_APELLIDO: Property = Property(name="APELLIDO", type=StringType)
gestionmodelosconsultas_resultcotracir_Planilla_CEDULA: Property = Property(name="CEDULA", type=StringType)
gestionmodelosconsultas_resultcotracir_Planilla_HORA_MODIFICACION: Property = Property(name="HORA_MODIFICACION", type=StringType)
gestionmodelosconsultas_resultcotracir_Planilla_TOTAL_DEPOSITO: Property = Property(name="TOTAL_DEPOSITO", type=StringType)
gestionmodelosconsultas_resultcotracir_Planilla.attributes={gestionmodelosconsultas_resultcotracir_Planilla_TOTAL_RECAUDO_NETO, gestionmodelosconsultas_resultcotracir_Planilla_TOTAL_DEPOSITO, gestionmodelosconsultas_resultcotracir_Planilla_USUARIO, gestionmodelosconsultas_resultcotracir_Planilla_APELLIDO, gestionmodelosconsultas_resultcotracir_Planilla_TOTAL, gestionmodelosconsultas_resultcotracir_Planilla_NOMBRE_PERSONA, gestionmodelosconsultas_resultcotracir_Planilla_HORA_MODIFICACION, gestionmodelosconsultas_resultcotracir_Planilla_TOTAL_RECAUDO_BRUTO, gestionmodelosconsultas_resultcotracir_Planilla_CEDULA_CONDUCTOR, gestionmodelosconsultas_resultcotracir_Planilla_NUMERO_MOVIL, gestionmodelosconsultas_resultcotracir_Planilla_CEDULA, gestionmodelosconsultas_resultcotracir_Planilla_TOTAL_GASTOS, gestionmodelosconsultas_resultcotracir_Planilla_LIQUIDADO, gestionmodelosconsultas_resultcotracir_Planilla_CONDUCTOR, gestionmodelosconsultas_resultcotracir_Planilla_FECHA, gestionmodelosconsultas_resultcotracir_Planilla_ID}

# gestionmodelosconsultas_resultset_ResultElement class attributes and methods

# gestionmodelosconsultas_resultcotracir_Transaccion class attributes and methods
gestionmodelosconsultas_resultcotracir_Transaccion_ESTADO_TRANSACCION: Property = Property(name="ESTADO_TRANSACCION", type=StringType)
gestionmodelosconsultas_resultcotracir_Transaccion_HORA: Property = Property(name="HORA", type=StringType)
gestionmodelosconsultas_resultcotracir_Transaccion_TIPO: Property = Property(name="TIPO", type=StringType)
gestionmodelosconsultas_resultcotracir_Transaccion_DESCRIPCION: Property = Property(name="DESCRIPCION", type=StringType)
gestionmodelosconsultas_resultcotracir_Transaccion_CATEGORIA: Property = Property(name="CATEGORIA", type=StringType)
gestionmodelosconsultas_resultcotracir_Transaccion_ID: Property = Property(name="ID", type=StringType)
gestionmodelosconsultas_resultcotracir_Transaccion_VALOR: Property = Property(name="VALOR", type=StringType)
gestionmodelosconsultas_resultcotracir_Transaccion.attributes={gestionmodelosconsultas_resultcotracir_Transaccion_VALOR, gestionmodelosconsultas_resultcotracir_Transaccion_HORA, gestionmodelosconsultas_resultcotracir_Transaccion_ID, gestionmodelosconsultas_resultcotracir_Transaccion_TIPO, gestionmodelosconsultas_resultcotracir_Transaccion_DESCRIPCION, gestionmodelosconsultas_resultcotracir_Transaccion_CATEGORIA, gestionmodelosconsultas_resultcotracir_Transaccion_ESTADO_TRANSACCION}

# gestionmodelosconsultas_resultcotracir_NewClass class attributes and methods

# gestionmodelosconsultas_resultcotracir_Detallado class attributes and methods
gestionmodelosconsultas_resultcotracir_Detallado_ID: Property = Property(name="ID", type=StringType)
gestionmodelosconsultas_resultcotracir_Detallado_NOMBRE: Property = Property(name="NOMBRE", type=StringType)
gestionmodelosconsultas_resultcotracir_Detallado_REGISTRO: Property = Property(name="REGISTRO", type=StringType)
gestionmodelosconsultas_resultcotracir_Detallado_TOTAL_RECAUDO_TARIFA: Property = Property(name="TOTAL_RECAUDO_TARIFA", type=StringType)
gestionmodelosconsultas_resultcotracir_Detallado_REGISTRO_RECAUDO: Property = Property(name="REGISTRO_RECAUDO", type=StringType)
gestionmodelosconsultas_resultcotracir_Detallado_COSTO_TARIFA: Property = Property(name="COSTO_TARIFA", type=StringType)
gestionmodelosconsultas_resultcotracir_Detallado.attributes={gestionmodelosconsultas_resultcotracir_Detallado_ID, gestionmodelosconsultas_resultcotracir_Detallado_COSTO_TARIFA, gestionmodelosconsultas_resultcotracir_Detallado_REGISTRO, gestionmodelosconsultas_resultcotracir_Detallado_REGISTRO_RECAUDO, gestionmodelosconsultas_resultcotracir_Detallado_NOMBRE, gestionmodelosconsultas_resultcotracir_Detallado_TOTAL_RECAUDO_TARIFA}

# gestionmodelosconsultas_cotracir_Planilla class attributes and methods

# gestionmodelosconsultas_cotracir_Transaccion class attributes and methods

# gestionmodelosconsultas_cotracir_Trama class attributes and methods

# gestionmodelosconsultas_cotracir_Propietario class attributes and methods

# gestionmodelosconsultas_cotracir_Detallado class attributes and methods

# ElementoConsulta class attributes and methods

# gestionmodelosconsultas_cotracir_Consolidado class attributes and methods

# Relationships
rulesFactory0: BinaryAssociation = BinaryAssociation(
    name="rulesFactory0",
    ends={
        Property(name="RulesFactory", type=gestionmodelosconsultas_ModelFactory, multiplicity=Multiplicity(1, 1)),
        Property(name="ModelFactory", type=factoryrules_RulesFactory, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
factoryModeloConsultas1: BinaryAssociation = BinaryAssociation(
    name="factoryModeloConsultas1",
    ends={
        Property(name="FactoryModeloConsulta", type=gestionmodelosconsultas_ModelFactory, multiplicity=Multiplicity(1, 1)),
        Property(name="ModelFactory2", type=FactoryModeloConsulta, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
diagramEntity3: BinaryAssociation = BinaryAssociation(
    name="diagramEntity3",
    ends={
        Property(name="DiagramEntity", type=gestionmodelosconsultas_ModelFactory, multiplicity=Multiplicity(1, 1)),
        Property(name="ModelFactory4", type=DiagramEntity, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
ModelFactory5: BinaryAssociation = BinaryAssociation(
    name="ModelFactory5",
    ends={
        Property(name="ModelFactory6", type=gestionmodelosconsultas_factoryrules_RulesFactory, multiplicity=Multiplicity(1, 1)),
        Property(name="rulesFactory", type=factoryrules_gestionmodelosconsultas_ModelFactory, multiplicity=Multiplicity(0, 1))
    }
)
listRuleDiagramEntity7: BinaryAssociation = BinaryAssociation(
    name="listRuleDiagramEntity7",
    ends={
        Property(name="Rule", type=gestionmodelosconsultas_factoryrules_RulesFactory, multiplicity=Multiplicity(1, 1)),
        Property(name="RulesFactory8", type=factoryrules_Rule, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
listChildRule11: BinaryAssociation = BinaryAssociation(
    name="listChildRule11",
    ends={
        Property(name="ChildRule", type=gestionmodelosconsultas_factoryrules_Rule, multiplicity=Multiplicity(1, 1)),
        Property(name="Rule12", type=factoryrules_ChildRule, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Rule13: BinaryAssociation = BinaryAssociation(
    name="Rule13",
    ends={
        Property(name="Rule14", type=gestionmodelosconsultas_factoryrules_ChildRule, multiplicity=Multiplicity(1, 1)),
        Property(name="listChildRule", type=factoryrules_Rule, multiplicity=Multiplicity(0, 1))
    }
)
ownedByFactoryEntity15: BinaryAssociation = BinaryAssociation(
    name="ownedByFactoryEntity15",
    ends={
        Property(name="DiagramEntity16", type=gestionmodelosconsultas_entitymodel_Entity, multiplicity=Multiplicity(1, 1)),
        Property(name="listEntity", type=DiagramEntity, multiplicity=Multiplicity(0, 1))
    }
)
listAttributes17: BinaryAssociation = BinaryAssociation(
    name="listAttributes17",
    ends={
        Property(name="Attribute", type=gestionmodelosconsultas_entitymodel_Entity, multiplicity=Multiplicity(1, 1)),
        Property(name="Entity", type=Attribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
theFactoryEntity18: BinaryAssociation = BinaryAssociation(
    name="theFactoryEntity18",
    ends={
        Property(name="DiagramEntity19", type=gestionmodelosconsultas_entitymodel_EntityRelation, multiplicity=Multiplicity(1, 1)),
        Property(name="listEntityRelation", type=DiagramEntity, multiplicity=Multiplicity(0, 1))
    }
)
source20: BinaryAssociation = BinaryAssociation(
    name="source20",
    ends={
        Property(name="Entity21", type=gestionmodelosconsultas_entitymodel_EntityRelation, multiplicity=Multiplicity(1, 1)),
        Property(name="gestionmodelosconsultas_entitymodel_EntityRelation", type=Entity, multiplicity=Multiplicity(1, 1))
    }
)
RulesFactory9: BinaryAssociation = BinaryAssociation(
    name="RulesFactory9",
    ends={
        Property(name="RulesFactory10", type=gestionmodelosconsultas_factoryrules_Rule, multiplicity=Multiplicity(1, 1)),
        Property(name="listRuleDiagramEntity", type=factoryrules_RulesFactory, multiplicity=Multiplicity(0, 1))
    }
)
Entity25: BinaryAssociation = BinaryAssociation(
    name="Entity25",
    ends={
        Property(name="Entity26", type=gestionmodelosconsultas_entitymodel_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="listAttributes", type=Entity, multiplicity=Multiplicity(0, 1))
    }
)
ElementoRealizacionValueAttribute27: BinaryAssociation = BinaryAssociation(
    name="ElementoRealizacionValueAttribute27",
    ends={
        Property(name="ElementoRealizacionValueAttribute", type=gestionmodelosconsultas_entitymodel_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="valueAttribute", type=ElementoRealizacionValueAttribute, multiplicity=Multiplicity(0, 9999))
    }
)
ElementoRealizacionVisibleAttribute28: BinaryAssociation = BinaryAssociation(
    name="ElementoRealizacionVisibleAttribute28",
    ends={
        Property(name="ElementoRealizacionVisibleAttribute", type=gestionmodelosconsultas_entitymodel_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="visibleAttribute", type=ElementoRealizacionVisibleAttribute, multiplicity=Multiplicity(0, 9999))
    }
)
ElementoRealizacionDiagramEntity29: BinaryAssociation = BinaryAssociation(
    name="ElementoRealizacionDiagramEntity29",
    ends={
        Property(name="ElementoRealizacionDiagramEntity", type=gestionmodelosconsultas_entitymodel_ModelElementEntity, multiplicity=Multiplicity(1, 1)),
        Property(name="modelElementEntity", type=ElementoRealizacionDiagramEntity, multiplicity=Multiplicity(0, 9999))
    }
)
ModelFactory30: BinaryAssociation = BinaryAssociation(
    name="ModelFactory30",
    ends={
        Property(name="ModelFactory31", type=gestionmodelosconsultas_entitymodel_DiagramEntity, multiplicity=Multiplicity(1, 1)),
        Property(name="diagramEntity", type=entitymodel_gestionmodelosconsultas_ModelFactory, multiplicity=Multiplicity(0, 1))
    }
)
listEntity32: BinaryAssociation = BinaryAssociation(
    name="listEntity32",
    ends={
        Property(name="Entity33", type=gestionmodelosconsultas_entitymodel_DiagramEntity, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedByFactoryEntity", type=Entity, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
listEntityRelation34: BinaryAssociation = BinaryAssociation(
    name="listEntityRelation34",
    ends={
        Property(name="EntityRelation", type=gestionmodelosconsultas_entitymodel_DiagramEntity, multiplicity=Multiplicity(1, 1)),
        Property(name="theFactoryEntity", type=EntityRelation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ModeloConsulta35: BinaryAssociation = BinaryAssociation(
    name="ModeloConsulta35",
    ends={
        Property(name="ModeloConsulta", type=gestionmodelosconsultas_entitymodel_RealizacionDiagramEntity, multiplicity=Multiplicity(1, 1)),
        Property(name="realizacionDiagramEntity", type=ModeloConsulta, multiplicity=Multiplicity(0, 1))
    }
)
listElementoRealizacionDiagramEntity36: BinaryAssociation = BinaryAssociation(
    name="listElementoRealizacionDiagramEntity36",
    ends={
        Property(name="ElementoRealizacionDiagramEntity37", type=gestionmodelosconsultas_entitymodel_RealizacionDiagramEntity, multiplicity=Multiplicity(1, 1)),
        Property(name="RealizacionDiagramEntity", type=ElementoRealizacionDiagramEntity, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
target22: BinaryAssociation = BinaryAssociation(
    name="target22",
    ends={
        Property(name="Entity24", type=gestionmodelosconsultas_entitymodel_EntityRelation, multiplicity=Multiplicity(1, 1)),
        Property(name="gestionmodelosconsultas_entitymodel_EntityRelation23", type=Entity, multiplicity=Multiplicity(1, 1))
    }
)
modelElementEntity43: BinaryAssociation = BinaryAssociation(
    name="modelElementEntity43",
    ends={
        Property(name="ModelElementEntity", type=gestionmodelosconsultas_entitymodel_ElementoRealizacionDiagramEntity, multiplicity=Multiplicity(1, 1)),
        Property(name="ElementoRealizacionDiagramEntity44", type=ModelElementEntity, multiplicity=Multiplicity(1, 1))
    }
)
RealizacionDiagramEntity45: BinaryAssociation = BinaryAssociation(
    name="RealizacionDiagramEntity45",
    ends={
        Property(name="RealizacionDiagramEntity46", type=gestionmodelosconsultas_entitymodel_ElementoRealizacionDiagramEntity, multiplicity=Multiplicity(1, 1)),
        Property(name="listElementoRealizacionDiagramEntity", type=RealizacionDiagramEntity, multiplicity=Multiplicity(0, 1))
    }
)
listElementoRealizacionAttribute47: BinaryAssociation = BinaryAssociation(
    name="listElementoRealizacionAttribute47",
    ends={
        Property(name="ElementoRealizacionValueAttribute49", type=gestionmodelosconsultas_entitymodel_ElementoRealizacionDiagramEntity, multiplicity=Multiplicity(1, 1)),
        Property(name="ElementoRealizacionDiagramEntity48", type=ElementoRealizacionValueAttribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
valueAttribute50: BinaryAssociation = BinaryAssociation(
    name="valueAttribute50",
    ends={
        Property(name="Attribute52", type=gestionmodelosconsultas_entitymodel_ElementoRealizacionValueAttribute, multiplicity=Multiplicity(1, 1)),
        Property(name="ElementoRealizacionValueAttribute51", type=Attribute, multiplicity=Multiplicity(0, 9999))
    }
)
ElementoRealizacionDiagramEntity53: BinaryAssociation = BinaryAssociation(
    name="ElementoRealizacionDiagramEntity53",
    ends={
        Property(name="ElementoRealizacionDiagramEntity54", type=gestionmodelosconsultas_entitymodel_ElementoRealizacionValueAttribute, multiplicity=Multiplicity(1, 1)),
        Property(name="listElementoRealizacionAttribute", type=ElementoRealizacionDiagramEntity, multiplicity=Multiplicity(0, 1))
    }
)
realizacionVisibleAttribute38: BinaryAssociation = BinaryAssociation(
    name="realizacionVisibleAttribute38",
    ends={
        Property(name="ElementoRealizacionVisibleAttribute40", type=gestionmodelosconsultas_entitymodel_RealizacionDiagramEntity, multiplicity=Multiplicity(1, 1)),
        Property(name="RealizacionDiagramEntity39", type=ElementoRealizacionVisibleAttribute, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
listValues41: BinaryAssociation = BinaryAssociation(
    name="listValues41",
    ends={
        Property(name="Value", type=gestionmodelosconsultas_entitymodel_RealizacionDiagramEntity, multiplicity=Multiplicity(1, 1)),
        Property(name="RealizacionDiagramEntity42", type=Value, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
RealizacionDiagramEntity58: BinaryAssociation = BinaryAssociation(
    name="RealizacionDiagramEntity58",
    ends={
        Property(name="RealizacionDiagramEntity59", type=gestionmodelosconsultas_entitymodel_ElementoRealizacionVisibleAttribute, multiplicity=Multiplicity(1, 1)),
        Property(name="realizacionVisibleAttribute", type=RealizacionDiagramEntity, multiplicity=Multiplicity(0, 1))
    }
)
visibleAttribute60: BinaryAssociation = BinaryAssociation(
    name="visibleAttribute60",
    ends={
        Property(name="Attribute62", type=gestionmodelosconsultas_entitymodel_ElementoRealizacionVisibleAttribute, multiplicity=Multiplicity(1, 1)),
        Property(name="ElementoRealizacionVisibleAttribute61", type=Attribute, multiplicity=Multiplicity(0, 9999))
    }
)
ElementoRealizacionValueAttribute63: BinaryAssociation = BinaryAssociation(
    name="ElementoRealizacionValueAttribute63",
    ends={
        Property(name="ElementoRealizacionValueAttribute64", type=gestionmodelosconsultas_entitymodel_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="values", type=ElementoRealizacionValueAttribute, multiplicity=Multiplicity(0, 9999))
    }
)
RealizacionDiagramEntity65: BinaryAssociation = BinaryAssociation(
    name="RealizacionDiagramEntity65",
    ends={
        Property(name="RealizacionDiagramEntity66", type=gestionmodelosconsultas_entitymodel_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="listValues", type=RealizacionDiagramEntity, multiplicity=Multiplicity(0, 1))
    }
)
realizacionDiagramEntity67: BinaryAssociation = BinaryAssociation(
    name="realizacionDiagramEntity67",
    ends={
        Property(name="RealizacionDiagramEntity69", type=gestionmodelosconsultas_modeloconsultas_ModeloConsulta, multiplicity=Multiplicity(1, 1)),
        Property(name="ModeloConsulta68", type=RealizacionDiagramEntity, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
FactoryModeloConsulta70: BinaryAssociation = BinaryAssociation(
    name="FactoryModeloConsulta70",
    ends={
        Property(name="FactoryModeloConsulta71", type=gestionmodelosconsultas_modeloconsultas_ModeloConsulta, multiplicity=Multiplicity(1, 1)),
        Property(name="listModeloConsulta", type=FactoryModeloConsulta, multiplicity=Multiplicity(0, 1))
    }
)
listEADiagram72: BinaryAssociation = BinaryAssociation(
    name="listEADiagram72",
    ends={
        Property(name="EADiagram", type=gestionmodelosconsultas_modeloconsultas_ModeloConsulta, multiplicity=Multiplicity(1, 1)),
        Property(name="ModeloConsulta73", type=model_EADiagram, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
listResultado74: BinaryAssociation = BinaryAssociation(
    name="listResultado74",
    ends={
        Property(name="Resultado", type=gestionmodelosconsultas_modeloconsultas_ModeloConsulta, multiplicity=Multiplicity(1, 1)),
        Property(name="ModeloConsulta75", type=resultset_Resultado, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ModelFactory76: BinaryAssociation = BinaryAssociation(
    name="ModelFactory76",
    ends={
        Property(name="ModelFactory77", type=gestionmodelosconsultas_modeloconsultas_FactoryModeloConsulta, multiplicity=Multiplicity(1, 1)),
        Property(name="factoryModeloConsultas", type=modeloconsultas_gestionmodelosconsultas_ModelFactory, multiplicity=Multiplicity(0, 1))
    }
)
listModeloConsulta78: BinaryAssociation = BinaryAssociation(
    name="listModeloConsulta78",
    ends={
        Property(name="ModeloConsulta80", type=gestionmodelosconsultas_modeloconsultas_FactoryModeloConsulta, multiplicity=Multiplicity(1, 1)),
        Property(name="FactoryModeloConsulta79", type=ModeloConsulta, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
EADiagram81: BinaryAssociation = BinaryAssociation(
    name="EADiagram81",
    ends={
        Property(name="EADiagram82", type=gestionmodelosconsultas_model_Relacion, multiplicity=Multiplicity(1, 1)),
        Property(name="listRelacion", type=model_EADiagram, multiplicity=Multiplicity(0, 1))
    }
)
values55: BinaryAssociation = BinaryAssociation(
    name="values55",
    ends={
        Property(name="Value57", type=gestionmodelosconsultas_entitymodel_ElementoRealizacionValueAttribute, multiplicity=Multiplicity(1, 1)),
        Property(name="ElementoRealizacionValueAttribute56", type=Value, multiplicity=Multiplicity(0, 9999))
    }
)
ownedElementoConsulta87: BinaryAssociation = BinaryAssociation(
    name="ownedElementoConsulta87",
    ends={
        Property(name="ElementoConsulta", type=gestionmodelosconsultas_model_Campo, multiplicity=Multiplicity(1, 1)),
        Property(name="listCampos", type=model_ElementoConsulta, multiplicity=Multiplicity(0, 1))
    }
)
target83: BinaryAssociation = BinaryAssociation(
    name="target83",
    ends={
        Property(name="model_ElementoConsulta", type=gestionmodelosconsultas_model_Relacion, multiplicity=Multiplicity(1, 1)),
        Property(name="gestionmodelosconsultas_model_Relacion", type=model_ElementoConsulta, multiplicity=Multiplicity(1, 1))
    }
)
source84: BinaryAssociation = BinaryAssociation(
    name="source84",
    ends={
        Property(name="model_ElementoConsulta86", type=gestionmodelosconsultas_model_Relacion, multiplicity=Multiplicity(1, 1)),
        Property(name="gestionmodelosconsultas_model_Relacion85", type=model_ElementoConsulta, multiplicity=Multiplicity(1, 1))
    }
)
EADiagram95: BinaryAssociation = BinaryAssociation(
    name="EADiagram95",
    ends={
        Property(name="EADiagram96", type=gestionmodelosconsultas_model_ElementoConsulta, multiplicity=Multiplicity(1, 1)),
        Property(name="listElementoConsulta", type=model_EADiagram, multiplicity=Multiplicity(0, 1))
    }
)
listCampos97: BinaryAssociation = BinaryAssociation(
    name="listCampos97",
    ends={
        Property(name="Campo", type=gestionmodelosconsultas_model_ElementoConsulta, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedElementoConsulta", type=model_Campo, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
from_98: BinaryAssociation = BinaryAssociation(
    name="from_98",
    ends={
        Property(name="ElementoModelo", type=gestionmodelosconsultas_model_ElementoModelo, multiplicity=Multiplicity(1, 1)),
        Property(name="to", type=model_ElementoModelo, multiplicity=Multiplicity(0, 9999))
    }
)
to99: BinaryAssociation = BinaryAssociation(
    name="to99",
    ends={
        Property(name="ElementoModelo100", type=gestionmodelosconsultas_model_ElementoModelo, multiplicity=Multiplicity(1, 1)),
        Property(name="from_", type=model_ElementoModelo, multiplicity=Multiplicity(0, 9999))
    }
)
ModeloConsulta101: BinaryAssociation = BinaryAssociation(
    name="ModeloConsulta101",
    ends={
        Property(name="ModeloConsulta102", type=gestionmodelosconsultas_resultset_Resultado, multiplicity=Multiplicity(1, 1)),
        Property(name="listResultado", type=ModeloConsulta, multiplicity=Multiplicity(0, 1))
    }
)
listResultElement103: BinaryAssociation = BinaryAssociation(
    name="listResultElement103",
    ends={
        Property(name="ResultElement", type=gestionmodelosconsultas_resultset_Resultado, multiplicity=Multiplicity(1, 1)),
        Property(name="Resultado104", type=resultset_ResultElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
listElementoModeloResultado105: BinaryAssociation = BinaryAssociation(
    name="listElementoModeloResultado105",
    ends={
        Property(name="ElementoModeloResultado106", type=gestionmodelosconsultas_resultset_ElementoModeloResultado, multiplicity=Multiplicity(1, 1)),
        Property(name="ElementoModeloResultado", type=resultset_ElementoModeloResultado, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ElementoModeloResultado107: BinaryAssociation = BinaryAssociation(
    name="ElementoModeloResultado107",
    ends={
        Property(name="ElementoModeloResultado108", type=gestionmodelosconsultas_resultset_ElementoModeloResultado, multiplicity=Multiplicity(1, 1)),
        Property(name="listElementoModeloResultado", type=resultset_ElementoModeloResultado, multiplicity=Multiplicity(0, 1))
    }
)
listRelacion88: BinaryAssociation = BinaryAssociation(
    name="listRelacion88",
    ends={
        Property(name="Relacion", type=gestionmodelosconsultas_model_EADiagram, multiplicity=Multiplicity(1, 1)),
        Property(name="EADiagram89", type=model_Relacion, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ModeloConsulta90: BinaryAssociation = BinaryAssociation(
    name="ModeloConsulta90",
    ends={
        Property(name="ModeloConsulta91", type=gestionmodelosconsultas_model_EADiagram, multiplicity=Multiplicity(1, 1)),
        Property(name="listEADiagram", type=ModeloConsulta, multiplicity=Multiplicity(0, 1))
    }
)
listElementoConsulta92: BinaryAssociation = BinaryAssociation(
    name="listElementoConsulta92",
    ends={
        Property(name="ElementoConsulta94", type=gestionmodelosconsultas_model_EADiagram, multiplicity=Multiplicity(1, 1)),
        Property(name="EADiagram93", type=model_ElementoConsulta, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Resultado109: BinaryAssociation = BinaryAssociation(
    name="Resultado109",
    ends={
        Property(name="Resultado110", type=gestionmodelosconsultas_resultset_ResultElement, multiplicity=Multiplicity(1, 1)),
        Property(name="listResultElement", type=resultset_Resultado, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_gestionmodelosconsultas_factoryrules_EntityName_ChildRule = Generalization(general=ChildRule, specific=gestionmodelosconsultas_factoryrules_EntityName)
gen_gestionmodelosconsultas_factoryrules_RelationName_ChildRule = Generalization(general=ChildRule, specific=gestionmodelosconsultas_factoryrules_RelationName)
gen_gestionmodelosconsultas_entitymodel_Entity_ModelElementEntity = Generalization(general=ModelElementEntity, specific=gestionmodelosconsultas_entitymodel_Entity)
gen_gestionmodelosconsultas_entitymodel_EntityRelation_ModelElementEntity = Generalization(general=ModelElementEntity, specific=gestionmodelosconsultas_entitymodel_EntityRelation)
gen_gestionmodelosconsultas_entitymodel_SimpleRelation_EntityRelation = Generalization(general=EntityRelation, specific=gestionmodelosconsultas_entitymodel_SimpleRelation)
gen_gestionmodelosconsultas_entitymodel_AssociativeEntity_Entity = Generalization(general=Entity, specific=gestionmodelosconsultas_entitymodel_AssociativeEntity)
gen_gestionmodelosconsultas_model_Relacion_ElementoModelo = Generalization(general=ElementoModelo, specific=gestionmodelosconsultas_model_Relacion)
gen_gestionmodelosconsultas_model_ViewModel_EADiagram = Generalization(general=EADiagram, specific=gestionmodelosconsultas_model_ViewModel)
gen_gestionmodelosconsultas_model_ElementoConsulta_ElementoModelo = Generalization(general=ElementoModelo, specific=gestionmodelosconsultas_model_ElementoConsulta)
gen_gestionmodelosconsultas_model_Proyeccion_EADiagram = Generalization(general=EADiagram, specific=gestionmodelosconsultas_model_Proyeccion)
gen_gestionmodelosconsultas_resultset_ElementoModeloResultado_ResultElement = Generalization(general=ResultElement, specific=gestionmodelosconsultas_resultset_ElementoModeloResultado)
gen_gestionmodelosconsultas_resultcotracir_Transaccion_ElementoModeloResultado = Generalization(general=ElementoModeloResultado, specific=gestionmodelosconsultas_resultcotracir_Transaccion)
gen_gestionmodelosconsultas_resultcotracir_Trama_ElementoModeloResultado = Generalization(general=ElementoModeloResultado, specific=gestionmodelosconsultas_resultcotracir_Trama)
gen_gestionmodelosconsultas_resultcotracir_Consolidado_ElementoModeloResultado = Generalization(general=ElementoModeloResultado, specific=gestionmodelosconsultas_resultcotracir_Consolidado)
gen_gestionmodelosconsultas_resultcotracir_Propietario_ElementoModeloResultado = Generalization(general=ElementoModeloResultado, specific=gestionmodelosconsultas_resultcotracir_Propietario)
gen_gestionmodelosconsultas_resultcotracir_Planilla_ElementoModeloResultado = Generalization(general=ElementoModeloResultado, specific=gestionmodelosconsultas_resultcotracir_Planilla)
gen_gestionmodelosconsultas_resultcotracir_Detallado_ElementoModeloResultado = Generalization(general=ElementoModeloResultado, specific=gestionmodelosconsultas_resultcotracir_Detallado)
gen_gestionmodelosconsultas_cotracir_Transaccion_ElementoConsulta = Generalization(general=ElementoConsulta, specific=gestionmodelosconsultas_cotracir_Transaccion)
gen_gestionmodelosconsultas_cotracir_Trama_ElementoConsulta = Generalization(general=ElementoConsulta, specific=gestionmodelosconsultas_cotracir_Trama)
gen_gestionmodelosconsultas_cotracir_Propietario_ElementoConsulta = Generalization(general=ElementoConsulta, specific=gestionmodelosconsultas_cotracir_Propietario)
gen_gestionmodelosconsultas_cotracir_Detallado_ElementoConsulta = Generalization(general=ElementoConsulta, specific=gestionmodelosconsultas_cotracir_Detallado)
gen_gestionmodelosconsultas_cotracir_Planilla_ElementoConsulta = Generalization(general=ElementoConsulta, specific=gestionmodelosconsultas_cotracir_Planilla)
gen_gestionmodelosconsultas_cotracir_Consolidado_ElementoConsulta = Generalization(general=ElementoConsulta, specific=gestionmodelosconsultas_cotracir_Consolidado)

# Domain Model
domain_model = DomainModel(
    name="gestionmodelosconsultas",
    types={gestionmodelosconsultas_ModelFactory, factoryrules_RulesFactory, FactoryModeloConsulta, DiagramEntity, gestionmodelosconsultas_factoryrules_RulesFactory, factoryrules_gestionmodelosconsultas_ModelFactory, factoryrules_Rule, factoryrules_ChildRule, gestionmodelosconsultas_factoryrules_ChildRule, gestionmodelosconsultas_factoryrules_EntityName, ChildRule, gestionmodelosconsultas_factoryrules_RelationName, gestionmodelosconsultas_entitymodel_Entity, ModelElementEntity, Attribute, gestionmodelosconsultas_entitymodel_EntityRelation, Entity, gestionmodelosconsultas_factoryrules_Rule, ElementoRealizacionValueAttribute, ElementoRealizacionVisibleAttribute, gestionmodelosconsultas_entitymodel_ModelElementEntity, ElementoRealizacionDiagramEntity, gestionmodelosconsultas_entitymodel_DiagramEntity, entitymodel_gestionmodelosconsultas_ModelFactory, gestionmodelosconsultas_entitymodel_RealizacionDiagramEntity, ModeloConsulta, gestionmodelosconsultas_entitymodel_SimpleRelation, EntityRelation, gestionmodelosconsultas_entitymodel_AssociativeEntity, gestionmodelosconsultas_entitymodel_Attribute, RealizacionDiagramEntity, gestionmodelosconsultas_entitymodel_ElementoRealizacionValueAttribute, Value, gestionmodelosconsultas_entitymodel_ElementoRealizacionDiagramEntity, gestionmodelosconsultas_entitymodel_Value, gestionmodelosconsultas_modeloconsultas_ModeloConsulta, model_EADiagram, resultset_Resultado, gestionmodelosconsultas_modeloconsultas_FactoryModeloConsulta, modeloconsultas_gestionmodelosconsultas_ModelFactory, gestionmodelosconsultas_model_Relacion, ElementoModelo, gestionmodelosconsultas_entitymodel_ElementoRealizacionVisibleAttribute, gestionmodelosconsultas_model_Campo, gestionmodelosconsultas_model_EADiagram, model_ElementoConsulta, gestionmodelosconsultas_model_ViewModel, EADiagram, gestionmodelosconsultas_model_ElementoConsulta, model_Campo, gestionmodelosconsultas_model_Proyeccion, gestionmodelosconsultas_model_ElementoModelo, model_ElementoModelo, gestionmodelosconsultas_resultset_Resultado, resultset_ResultElement, gestionmodelosconsultas_resultset_ElementoModeloResultado, ResultElement, resultset_ElementoModeloResultado, model_Relacion, ElementoModeloResultado, gestionmodelosconsultas_resultcotracir_Trama, gestionmodelosconsultas_resultcotracir_Consolidado, gestionmodelosconsultas_resultcotracir_Propietario, gestionmodelosconsultas_resultcotracir_Planilla, gestionmodelosconsultas_resultset_ResultElement, gestionmodelosconsultas_resultcotracir_Transaccion, gestionmodelosconsultas_resultcotracir_NewClass, gestionmodelosconsultas_resultcotracir_Detallado, gestionmodelosconsultas_cotracir_Planilla, gestionmodelosconsultas_cotracir_Transaccion, gestionmodelosconsultas_cotracir_Trama, gestionmodelosconsultas_cotracir_Propietario, gestionmodelosconsultas_cotracir_Detallado, ElementoConsulta, gestionmodelosconsultas_cotracir_Consolidado, AttributeType, Multiplicity_enum, TipoModelElementEntity, Type, NombreCampo},
    associations={rulesFactory0, factoryModeloConsultas1, diagramEntity3, ModelFactory5, listRuleDiagramEntity7, listChildRule11, Rule13, ownedByFactoryEntity15, listAttributes17, theFactoryEntity18, source20, RulesFactory9, Entity25, ElementoRealizacionValueAttribute27, ElementoRealizacionVisibleAttribute28, ElementoRealizacionDiagramEntity29, ModelFactory30, listEntity32, listEntityRelation34, ModeloConsulta35, listElementoRealizacionDiagramEntity36, target22, modelElementEntity43, RealizacionDiagramEntity45, listElementoRealizacionAttribute47, valueAttribute50, ElementoRealizacionDiagramEntity53, realizacionVisibleAttribute38, listValues41, RealizacionDiagramEntity58, visibleAttribute60, ElementoRealizacionValueAttribute63, RealizacionDiagramEntity65, realizacionDiagramEntity67, FactoryModeloConsulta70, listEADiagram72, listResultado74, ModelFactory76, listModeloConsulta78, EADiagram81, values55, ownedElementoConsulta87, target83, source84, EADiagram95, listCampos97, from_98, to99, ModeloConsulta101, listResultElement103, listElementoModeloResultado105, ElementoModeloResultado107, listRelacion88, ModeloConsulta90, listElementoConsulta92, Resultado109},
    generalizations={gen_gestionmodelosconsultas_factoryrules_EntityName_ChildRule, gen_gestionmodelosconsultas_factoryrules_RelationName_ChildRule, gen_gestionmodelosconsultas_entitymodel_Entity_ModelElementEntity, gen_gestionmodelosconsultas_entitymodel_EntityRelation_ModelElementEntity, gen_gestionmodelosconsultas_entitymodel_SimpleRelation_EntityRelation, gen_gestionmodelosconsultas_entitymodel_AssociativeEntity_Entity, gen_gestionmodelosconsultas_model_Relacion_ElementoModelo, gen_gestionmodelosconsultas_model_ViewModel_EADiagram, gen_gestionmodelosconsultas_model_ElementoConsulta_ElementoModelo, gen_gestionmodelosconsultas_model_Proyeccion_EADiagram, gen_gestionmodelosconsultas_resultset_ElementoModeloResultado_ResultElement, gen_gestionmodelosconsultas_resultcotracir_Transaccion_ElementoModeloResultado, gen_gestionmodelosconsultas_resultcotracir_Trama_ElementoModeloResultado, gen_gestionmodelosconsultas_resultcotracir_Consolidado_ElementoModeloResultado, gen_gestionmodelosconsultas_resultcotracir_Propietario_ElementoModeloResultado, gen_gestionmodelosconsultas_resultcotracir_Planilla_ElementoModeloResultado, gen_gestionmodelosconsultas_resultcotracir_Detallado_ElementoModeloResultado, gen_gestionmodelosconsultas_cotracir_Transaccion_ElementoConsulta, gen_gestionmodelosconsultas_cotracir_Trama_ElementoConsulta, gen_gestionmodelosconsultas_cotracir_Propietario_ElementoConsulta, gen_gestionmodelosconsultas_cotracir_Detallado_ElementoConsulta, gen_gestionmodelosconsultas_cotracir_Planilla_ElementoConsulta, gen_gestionmodelosconsultas_cotracir_Consolidado_ElementoConsulta},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)