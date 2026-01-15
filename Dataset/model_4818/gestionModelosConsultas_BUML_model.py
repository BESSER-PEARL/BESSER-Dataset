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

Multiplicity: Enumeration = Enumeration(
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
gestionmodelosconsultas_factoryrules_Rule = Class(name="gestionmodelosconsultas::factoryrules::Rule")
factoryrules_ChildRule = Class(name="factoryrules::ChildRule")
gestionmodelosconsultas_factoryrules_ChildRule = Class(name="gestionmodelosconsultas::factoryrules::ChildRule", is_abstract=True)
gestionmodelosconsultas_factoryrules_EntityName = Class(name="gestionmodelosconsultas::factoryrules::EntityName")
ChildRule = Class(name="ChildRule")
gestionmodelosconsultas_factoryrules_RelationName = Class(name="gestionmodelosconsultas::factoryrules::RelationName")
gestionmodelosconsultas_entitymodel_Entity = Class(name="gestionmodelosconsultas::entitymodel::Entity")
ModelElementEntity = Class(name="ModelElementEntity")
Attribute = Class(name="Attribute")
gestionmodelosconsultas_entitymodel_EntityRelation = Class(name="gestionmodelosconsultas::entitymodel::EntityRelation")
gestionmodelosconsultas_ModelFactory = Class(name="gestionmodelosconsultas::ModelFactory")
factoryrules_RulesFactory = Class(name="factoryrules::RulesFactory")
FactoryModeloConsulta = Class(name="FactoryModeloConsulta")
DiagramEntity = Class(name="DiagramEntity")
gestionmodelosconsultas_factoryrules_RulesFactory = Class(name="gestionmodelosconsultas::factoryrules::RulesFactory")
factoryrules_gestionmodelosconsultas_ModelFactory = Class(name="factoryrules::gestionmodelosconsultas::ModelFactory")
factoryrules_Rule = Class(name="factoryrules::Rule")
ElementoRealizacionValueAttribute = Class(name="ElementoRealizacionValueAttribute")
ElementoRealizacionVisibleAttribute = Class(name="ElementoRealizacionVisibleAttribute")
gestionmodelosconsultas_entitymodel_ModelElementEntity = Class(name="gestionmodelosconsultas::entitymodel::ModelElementEntity", is_abstract=True)
ElementoRealizacionDiagramEntity = Class(name="ElementoRealizacionDiagramEntity")
gestionmodelosconsultas_entitymodel_DiagramEntity = Class(name="gestionmodelosconsultas::entitymodel::DiagramEntity")
entitymodel_gestionmodelosconsultas_ModelFactory = Class(name="entitymodel::gestionmodelosconsultas::ModelFactory")
gestionmodelosconsultas_entitymodel_RealizacionDiagramEntity = Class(name="gestionmodelosconsultas::entitymodel::RealizacionDiagramEntity")
ModeloConsulta = Class(name="ModeloConsulta")
Entity = Class(name="Entity")
gestionmodelosconsultas_entitymodel_SimpleRelation = Class(name="gestionmodelosconsultas::entitymodel::SimpleRelation")
EntityRelation = Class(name="EntityRelation")
gestionmodelosconsultas_entitymodel_AssociativeEntity = Class(name="gestionmodelosconsultas::entitymodel::AssociativeEntity")
gestionmodelosconsultas_entitymodel_Attribute = Class(name="gestionmodelosconsultas::entitymodel::Attribute")
gestionmodelosconsultas_entitymodel_ElementoRealizacionVisibleAttribute = Class(name="gestionmodelosconsultas::entitymodel::ElementoRealizacionVisibleAttribute")
gestionmodelosconsultas_entitymodel_Value = Class(name="gestionmodelosconsultas::entitymodel::Value")
gestionmodelosconsultas_modeloconsultas_ModeloConsulta = Class(name="gestionmodelosconsultas::modeloconsultas::ModeloConsulta")
model_EADiagram = Class(name="model::EADiagram")
resultset_Resultado = Class(name="resultset::Resultado")
Value = Class(name="Value")
gestionmodelosconsultas_entitymodel_ElementoRealizacionDiagramEntity = Class(name="gestionmodelosconsultas::entitymodel::ElementoRealizacionDiagramEntity")
RealizacionDiagramEntity = Class(name="RealizacionDiagramEntity")
gestionmodelosconsultas_entitymodel_ElementoRealizacionValueAttribute = Class(name="gestionmodelosconsultas::entitymodel::ElementoRealizacionValueAttribute")
gestionmodelosconsultas_modeloconsultas_FactoryModeloConsulta = Class(name="gestionmodelosconsultas::modeloconsultas::FactoryModeloConsulta")
modeloconsultas_gestionmodelosconsultas_ModelFactory = Class(name="modeloconsultas::gestionmodelosconsultas::ModelFactory")
gestionmodelosconsultas_model_Relacion = Class(name="gestionmodelosconsultas::model::Relacion")
ElementoModelo = Class(name="ElementoModelo")
model_ElementoConsulta = Class(name="model::ElementoConsulta")
gestionmodelosconsultas_model_Campo = Class(name="gestionmodelosconsultas::model::Campo")
model_ElementoModelo = Class(name="model::ElementoModelo")
gestionmodelosconsultas_resultset_Resultado = Class(name="gestionmodelosconsultas::resultset::Resultado")
resultset_ResultElement = Class(name="resultset::ResultElement")
gestionmodelosconsultas_resultset_ElementoModeloResultado = Class(name="gestionmodelosconsultas::resultset::ElementoModeloResultado", is_abstract=True)
ResultElement = Class(name="ResultElement")
resultset_ElementoModeloResultado = Class(name="resultset::ElementoModeloResultado")
gestionmodelosconsultas_resultset_ResultElement = Class(name="gestionmodelosconsultas::resultset::ResultElement", is_abstract=True)
gestionmodelosconsultas_resultcotracir_Transaccion = Class(name="gestionmodelosconsultas::resultcotracir::Transaccion")
ElementoModeloResultado = Class(name="ElementoModeloResultado")
gestionmodelosconsultas_model_EADiagram = Class(name="gestionmodelosconsultas::model::EADiagram", is_abstract=True)
model_Relacion = Class(name="model::Relacion")
gestionmodelosconsultas_model_ViewModel = Class(name="gestionmodelosconsultas::model::ViewModel")
EADiagram = Class(name="EADiagram")
gestionmodelosconsultas_model_ElementoConsulta = Class(name="gestionmodelosconsultas::model::ElementoConsulta", is_abstract=True)
model_Campo = Class(name="model::Campo")
gestionmodelosconsultas_model_Proyeccion = Class(name="gestionmodelosconsultas::model::Proyeccion")
gestionmodelosconsultas_model_ElementoModelo = Class(name="gestionmodelosconsultas::model::ElementoModelo")
gestionmodelosconsultas_resultcotracir_Planilla = Class(name="gestionmodelosconsultas::resultcotracir::Planilla")
gestionmodelosconsultas_resultcotracir_NewClass = Class(name="gestionmodelosconsultas::resultcotracir::NewClass")
gestionmodelosconsultas_resultcotracir_Detallado = Class(name="gestionmodelosconsultas::resultcotracir::Detallado")
gestionmodelosconsultas_resultcotracir_Trama = Class(name="gestionmodelosconsultas::resultcotracir::Trama")
gestionmodelosconsultas_resultcotracir_Consolidado = Class(name="gestionmodelosconsultas::resultcotracir::Consolidado")
gestionmodelosconsultas_resultcotracir_Propietario = Class(name="gestionmodelosconsultas::resultcotracir::Propietario")
gestionmodelosconsultas_cotracir_Planilla = Class(name="gestionmodelosconsultas::cotracir::Planilla")
ElementoConsulta = Class(name="ElementoConsulta")
gestionmodelosconsultas_cotracir_Consolidado = Class(name="gestionmodelosconsultas::cotracir::Consolidado")
gestionmodelosconsultas_cotracir_Transaccion = Class(name="gestionmodelosconsultas::cotracir::Transaccion")
gestionmodelosconsultas_cotracir_Trama = Class(name="gestionmodelosconsultas::cotracir::Trama")
gestionmodelosconsultas_cotracir_Propietario = Class(name="gestionmodelosconsultas::cotracir::Propietario")
gestionmodelosconsultas_cotracir_Detallado = Class(name="gestionmodelosconsultas::cotracir::Detallado")

# gestionmodelosconsultas_factoryrules_Rule class attributes and methods
gestionmodelosconsultas_factoryrules_Rule_name: Property = Property(name="name", type=StringType)
gestionmodelosconsultas_factoryrules_Rule.attributes={gestionmodelosconsultas_factoryrules_Rule_name}

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
gestionmodelosconsultas_entitymodel_EntityRelation.attributes={gestionmodelosconsultas_entitymodel_EntityRelation_multiplicityTarget, gestionmodelosconsultas_entitymodel_EntityRelation_atributtePrimaryKeyTarget, gestionmodelosconsultas_entitymodel_EntityRelation_multiplicitySource, gestionmodelosconsultas_entitymodel_EntityRelation_atributteForeingKeySource}

# gestionmodelosconsultas_ModelFactory class attributes and methods
gestionmodelosconsultas_ModelFactory_m_cargar: Method = Method(name="cargar", parameters={}, type=StringType)
gestionmodelosconsultas_ModelFactory_m_salvar: Method = Method(name="salvar", parameters={})
gestionmodelosconsultas_ModelFactory.methods={gestionmodelosconsultas_ModelFactory_m_salvar, gestionmodelosconsultas_ModelFactory_m_cargar}

# factoryrules_RulesFactory class attributes and methods

# FactoryModeloConsulta class attributes and methods

# DiagramEntity class attributes and methods

# gestionmodelosconsultas_factoryrules_RulesFactory class attributes and methods

# factoryrules_gestionmodelosconsultas_ModelFactory class attributes and methods

# factoryrules_Rule class attributes and methods

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

# Entity class attributes and methods

# gestionmodelosconsultas_entitymodel_SimpleRelation class attributes and methods

# EntityRelation class attributes and methods

# gestionmodelosconsultas_entitymodel_AssociativeEntity class attributes and methods

# gestionmodelosconsultas_entitymodel_Attribute class attributes and methods
gestionmodelosconsultas_entitymodel_Attribute_name: Property = Property(name="name", type=StringType)
gestionmodelosconsultas_entitymodel_Attribute_type: Property = Property(name="type", type=StringType)
gestionmodelosconsultas_entitymodel_Attribute_value: Property = Property(name="value", type=StringType)
gestionmodelosconsultas_entitymodel_Attribute_visible: Property = Property(name="visible", type=BooleanType)
gestionmodelosconsultas_entitymodel_Attribute_attributeType: Property = Property(name="attributeType", type=StringType)
gestionmodelosconsultas_entitymodel_Attribute.attributes={gestionmodelosconsultas_entitymodel_Attribute_attributeType, gestionmodelosconsultas_entitymodel_Attribute_value, gestionmodelosconsultas_entitymodel_Attribute_type, gestionmodelosconsultas_entitymodel_Attribute_name, gestionmodelosconsultas_entitymodel_Attribute_visible}

# gestionmodelosconsultas_entitymodel_ElementoRealizacionVisibleAttribute class attributes and methods
gestionmodelosconsultas_entitymodel_ElementoRealizacionVisibleAttribute_nombre: Property = Property(name="nombre", type=StringType)
gestionmodelosconsultas_entitymodel_ElementoRealizacionVisibleAttribute.attributes={gestionmodelosconsultas_entitymodel_ElementoRealizacionVisibleAttribute_nombre}

# gestionmodelosconsultas_entitymodel_Value class attributes and methods
gestionmodelosconsultas_entitymodel_Value_value: Property = Property(name="value", type=StringType)
gestionmodelosconsultas_entitymodel_Value.attributes={gestionmodelosconsultas_entitymodel_Value_value}

# gestionmodelosconsultas_modeloconsultas_ModeloConsulta class attributes and methods
gestionmodelosconsultas_modeloconsultas_ModeloConsulta_nombre: Property = Property(name="nombre", type=StringType)
gestionmodelosconsultas_modeloconsultas_ModeloConsulta.attributes={gestionmodelosconsultas_modeloconsultas_ModeloConsulta_nombre}

# model_EADiagram class attributes and methods

# resultset_Resultado class attributes and methods

# Value class attributes and methods

# gestionmodelosconsultas_entitymodel_ElementoRealizacionDiagramEntity class attributes and methods
gestionmodelosconsultas_entitymodel_ElementoRealizacionDiagramEntity_tipo: Property = Property(name="tipo", type=StringType)
gestionmodelosconsultas_entitymodel_ElementoRealizacionDiagramEntity_nombreModelElementEntity: Property = Property(name="nombreModelElementEntity", type=StringType)
gestionmodelosconsultas_entitymodel_ElementoRealizacionDiagramEntity.attributes={gestionmodelosconsultas_entitymodel_ElementoRealizacionDiagramEntity_tipo, gestionmodelosconsultas_entitymodel_ElementoRealizacionDiagramEntity_nombreModelElementEntity}

# RealizacionDiagramEntity class attributes and methods

# gestionmodelosconsultas_entitymodel_ElementoRealizacionValueAttribute class attributes and methods
gestionmodelosconsultas_entitymodel_ElementoRealizacionValueAttribute_nombre: Property = Property(name="nombre", type=StringType)
gestionmodelosconsultas_entitymodel_ElementoRealizacionValueAttribute.attributes={gestionmodelosconsultas_entitymodel_ElementoRealizacionValueAttribute_nombre}

# gestionmodelosconsultas_modeloconsultas_FactoryModeloConsulta class attributes and methods

# modeloconsultas_gestionmodelosconsultas_ModelFactory class attributes and methods

# gestionmodelosconsultas_model_Relacion class attributes and methods
gestionmodelosconsultas_model_Relacion_estereotipo: Property = Property(name="estereotipo", type=StringType)
gestionmodelosconsultas_model_Relacion_order: Property = Property(name="order", type=StringType)
gestionmodelosconsultas_model_Relacion.attributes={gestionmodelosconsultas_model_Relacion_order, gestionmodelosconsultas_model_Relacion_estereotipo}

# ElementoModelo class attributes and methods

# model_ElementoConsulta class attributes and methods

# gestionmodelosconsultas_model_Campo class attributes and methods
gestionmodelosconsultas_model_Campo_nombreCampo: Property = Property(name="nombreCampo", type=StringType)
gestionmodelosconsultas_model_Campo_criterio: Property = Property(name="criterio", type=StringType)
gestionmodelosconsultas_model_Campo_seleccion: Property = Property(name="seleccion", type=BooleanType)
gestionmodelosconsultas_model_Campo.attributes={gestionmodelosconsultas_model_Campo_nombreCampo, gestionmodelosconsultas_model_Campo_criterio, gestionmodelosconsultas_model_Campo_seleccion}

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

# gestionmodelosconsultas_resultset_ResultElement class attributes and methods

# gestionmodelosconsultas_resultcotracir_Transaccion class attributes and methods
gestionmodelosconsultas_resultcotracir_Transaccion_ESTADO_TRANSACCION: Property = Property(name="ESTADO_TRANSACCION", type=StringType)
gestionmodelosconsultas_resultcotracir_Transaccion_HORA: Property = Property(name="HORA", type=StringType)
gestionmodelosconsultas_resultcotracir_Transaccion_TIPO: Property = Property(name="TIPO", type=StringType)
gestionmodelosconsultas_resultcotracir_Transaccion_DESCRIPCION: Property = Property(name="DESCRIPCION", type=StringType)
gestionmodelosconsultas_resultcotracir_Transaccion_CATEGORIA: Property = Property(name="CATEGORIA", type=StringType)
gestionmodelosconsultas_resultcotracir_Transaccion_ID: Property = Property(name="ID", type=StringType)
gestionmodelosconsultas_resultcotracir_Transaccion_VALOR: Property = Property(name="VALOR", type=StringType)
gestionmodelosconsultas_resultcotracir_Transaccion.attributes={gestionmodelosconsultas_resultcotracir_Transaccion_ID, gestionmodelosconsultas_resultcotracir_Transaccion_TIPO, gestionmodelosconsultas_resultcotracir_Transaccion_VALOR, gestionmodelosconsultas_resultcotracir_Transaccion_DESCRIPCION, gestionmodelosconsultas_resultcotracir_Transaccion_ESTADO_TRANSACCION, gestionmodelosconsultas_resultcotracir_Transaccion_HORA, gestionmodelosconsultas_resultcotracir_Transaccion_CATEGORIA}

# ElementoModeloResultado class attributes and methods

# gestionmodelosconsultas_model_EADiagram class attributes and methods
gestionmodelosconsultas_model_EADiagram_nombre: Property = Property(name="nombre", type=StringType)
gestionmodelosconsultas_model_EADiagram.attributes={gestionmodelosconsultas_model_EADiagram_nombre}

# model_Relacion class attributes and methods

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

# gestionmodelosconsultas_resultcotracir_Planilla class attributes and methods
gestionmodelosconsultas_resultcotracir_Planilla_ID: Property = Property(name="ID", type=StringType)
gestionmodelosconsultas_resultcotracir_Planilla_NUMERO_MOVIL: Property = Property(name="NUMERO_MOVIL", type=StringType)
gestionmodelosconsultas_resultcotracir_Planilla_FECHA: Property = Property(name="FECHA", type=StringType)
gestionmodelosconsultas_resultcotracir_Planilla_CEDULA_CONDUCTOR: Property = Property(name="CEDULA_CONDUCTOR", type=StringType)
gestionmodelosconsultas_resultcotracir_Planilla_CONDUCTOR: Property = Property(name="CONDUCTOR", type=StringType)
gestionmodelosconsultas_resultcotracir_Planilla_TOTAL: Property = Property(name="TOTAL", type=StringType)
gestionmodelosconsultas_resultcotracir_Planilla_TOTAL_RECAUDO_BRUTO: Property = Property(name="TOTAL_RECAUDO_BRUTO", type=StringType)
gestionmodelosconsultas_resultcotracir_Planilla_TOTAL_RECAUDO_NETO: Property = Property(name="TOTAL_RECAUDO_NETO", type=StringType)
gestionmodelosconsultas_resultcotracir_Planilla_TOTAL_DEPOSITO: Property = Property(name="TOTAL_DEPOSITO", type=StringType)
gestionmodelosconsultas_resultcotracir_Planilla_TOTAL_GASTOS: Property = Property(name="TOTAL_GASTOS", type=StringType)
gestionmodelosconsultas_resultcotracir_Planilla_LIQUIDADO: Property = Property(name="LIQUIDADO", type=StringType)
gestionmodelosconsultas_resultcotracir_Planilla_USUARIO: Property = Property(name="USUARIO", type=StringType)
gestionmodelosconsultas_resultcotracir_Planilla_NOMBRE_PERSONA: Property = Property(name="NOMBRE_PERSONA", type=StringType)
gestionmodelosconsultas_resultcotracir_Planilla_APELLIDO: Property = Property(name="APELLIDO", type=StringType)
gestionmodelosconsultas_resultcotracir_Planilla_CEDULA: Property = Property(name="CEDULA", type=StringType)
gestionmodelosconsultas_resultcotracir_Planilla_HORA_MODIFICACION: Property = Property(name="HORA_MODIFICACION", type=StringType)
gestionmodelosconsultas_resultcotracir_Planilla.attributes={gestionmodelosconsultas_resultcotracir_Planilla_TOTAL_DEPOSITO, gestionmodelosconsultas_resultcotracir_Planilla_USUARIO, gestionmodelosconsultas_resultcotracir_Planilla_APELLIDO, gestionmodelosconsultas_resultcotracir_Planilla_TOTAL_RECAUDO_NETO, gestionmodelosconsultas_resultcotracir_Planilla_NOMBRE_PERSONA, gestionmodelosconsultas_resultcotracir_Planilla_NUMERO_MOVIL, gestionmodelosconsultas_resultcotracir_Planilla_ID, gestionmodelosconsultas_resultcotracir_Planilla_TOTAL, gestionmodelosconsultas_resultcotracir_Planilla_TOTAL_RECAUDO_BRUTO, gestionmodelosconsultas_resultcotracir_Planilla_FECHA, gestionmodelosconsultas_resultcotracir_Planilla_HORA_MODIFICACION, gestionmodelosconsultas_resultcotracir_Planilla_TOTAL_GASTOS, gestionmodelosconsultas_resultcotracir_Planilla_CEDULA, gestionmodelosconsultas_resultcotracir_Planilla_CEDULA_CONDUCTOR, gestionmodelosconsultas_resultcotracir_Planilla_LIQUIDADO, gestionmodelosconsultas_resultcotracir_Planilla_CONDUCTOR}

# gestionmodelosconsultas_resultcotracir_NewClass class attributes and methods

# gestionmodelosconsultas_resultcotracir_Detallado class attributes and methods
gestionmodelosconsultas_resultcotracir_Detallado_ID: Property = Property(name="ID", type=StringType)
gestionmodelosconsultas_resultcotracir_Detallado_NOMBRE: Property = Property(name="NOMBRE", type=StringType)
gestionmodelosconsultas_resultcotracir_Detallado_REGISTRO: Property = Property(name="REGISTRO", type=StringType)
gestionmodelosconsultas_resultcotracir_Detallado_TOTAL_RECAUDO_TARIFA: Property = Property(name="TOTAL_RECAUDO_TARIFA", type=StringType)
gestionmodelosconsultas_resultcotracir_Detallado_REGISTRO_RECAUDO: Property = Property(name="REGISTRO_RECAUDO", type=StringType)
gestionmodelosconsultas_resultcotracir_Detallado_COSTO_TARIFA: Property = Property(name="COSTO_TARIFA", type=StringType)
gestionmodelosconsultas_resultcotracir_Detallado.attributes={gestionmodelosconsultas_resultcotracir_Detallado_REGISTRO_RECAUDO, gestionmodelosconsultas_resultcotracir_Detallado_COSTO_TARIFA, gestionmodelosconsultas_resultcotracir_Detallado_ID, gestionmodelosconsultas_resultcotracir_Detallado_TOTAL_RECAUDO_TARIFA, gestionmodelosconsultas_resultcotracir_Detallado_NOMBRE, gestionmodelosconsultas_resultcotracir_Detallado_REGISTRO}

# gestionmodelosconsultas_resultcotracir_Trama class attributes and methods
gestionmodelosconsultas_resultcotracir_Trama_ID: Property = Property(name="ID", type=StringType)
gestionmodelosconsultas_resultcotracir_Trama_CADENA_TRAMA: Property = Property(name="CADENA_TRAMA", type=StringType)
gestionmodelosconsultas_resultcotracir_Trama.attributes={gestionmodelosconsultas_resultcotracir_Trama_CADENA_TRAMA, gestionmodelosconsultas_resultcotracir_Trama_ID}

# gestionmodelosconsultas_resultcotracir_Consolidado class attributes and methods
gestionmodelosconsultas_resultcotracir_Consolidado_ID: Property = Property(name="ID", type=StringType)
gestionmodelosconsultas_resultcotracir_Consolidado_RUTA_DESPACHO: Property = Property(name="RUTA_DESPACHO", type=StringType)
gestionmodelosconsultas_resultcotracir_Consolidado_HORA_DESPACHO: Property = Property(name="HORA_DESPACHO", type=StringType)
gestionmodelosconsultas_resultcotracir_Consolidado_REGISTRO_CONSOLIDADO: Property = Property(name="REGISTRO_CONSOLIDADO", type=StringType)
gestionmodelosconsultas_resultcotracir_Consolidado_TOTAL_RECAUDO_BRUTO: Property = Property(name="TOTAL_RECAUDO_BRUTO", type=StringType)
gestionmodelosconsultas_resultcotracir_Consolidado_TOTAL_RECAUDO_DESPACHO: Property = Property(name="TOTAL_RECAUDO_DESPACHO", type=StringType)
gestionmodelosconsultas_resultcotracir_Consolidado_ESTADO_CONSOLIDADO: Property = Property(name="ESTADO_CONSOLIDADO", type=StringType)
gestionmodelosconsultas_resultcotracir_Consolidado_ESTADO_IMPRESION: Property = Property(name="ESTADO_IMPRESION", type=StringType)
gestionmodelosconsultas_resultcotracir_Consolidado.attributes={gestionmodelosconsultas_resultcotracir_Consolidado_HORA_DESPACHO, gestionmodelosconsultas_resultcotracir_Consolidado_RUTA_DESPACHO, gestionmodelosconsultas_resultcotracir_Consolidado_ESTADO_CONSOLIDADO, gestionmodelosconsultas_resultcotracir_Consolidado_ESTADO_IMPRESION, gestionmodelosconsultas_resultcotracir_Consolidado_ID, gestionmodelosconsultas_resultcotracir_Consolidado_REGISTRO_CONSOLIDADO, gestionmodelosconsultas_resultcotracir_Consolidado_TOTAL_RECAUDO_DESPACHO, gestionmodelosconsultas_resultcotracir_Consolidado_TOTAL_RECAUDO_BRUTO}

# gestionmodelosconsultas_resultcotracir_Propietario class attributes and methods
gestionmodelosconsultas_resultcotracir_Propietario_CEDULA: Property = Property(name="CEDULA", type=StringType)
gestionmodelosconsultas_resultcotracir_Propietario_ID: Property = Property(name="ID", type=StringType)
gestionmodelosconsultas_resultcotracir_Propietario_NOMBRE: Property = Property(name="NOMBRE", type=StringType)
gestionmodelosconsultas_resultcotracir_Propietario.attributes={gestionmodelosconsultas_resultcotracir_Propietario_ID, gestionmodelosconsultas_resultcotracir_Propietario_CEDULA, gestionmodelosconsultas_resultcotracir_Propietario_NOMBRE}

# gestionmodelosconsultas_cotracir_Planilla class attributes and methods

# ElementoConsulta class attributes and methods

# gestionmodelosconsultas_cotracir_Consolidado class attributes and methods

# gestionmodelosconsultas_cotracir_Transaccion class attributes and methods

# gestionmodelosconsultas_cotracir_Trama class attributes and methods

# gestionmodelosconsultas_cotracir_Propietario class attributes and methods

# gestionmodelosconsultas_cotracir_Detallado class attributes and methods

# Relationships
RulesFactory7: BinaryAssociation = BinaryAssociation(
    name="RulesFactory7",
    ends={
        Property(name="rules9", type=gestionmodelosconsultas_factoryrules_Rule, multiplicity=Multiplicity(1, 1)),
        Property(name="factoryrules8", type=factoryrules_RulesFactory, multiplicity=Multiplicity(0, 1))
    }
)
listChildRule10: BinaryAssociation = BinaryAssociation(
    name="listChildRule10",
    ends={
        Property(name="rules12", type=gestionmodelosconsultas_factoryrules_Rule, multiplicity=Multiplicity(1, 1)),
        Property(name="factoryrules11", type=factoryrules_ChildRule, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Rule13: BinaryAssociation = BinaryAssociation(
    name="Rule13",
    ends={
        Property(name="rules15", type=gestionmodelosconsultas_factoryrules_ChildRule, multiplicity=Multiplicity(1, 1)),
        Property(name="factoryrules14", type=factoryrules_Rule, multiplicity=Multiplicity(0, 1))
    }
)
ownedByFactoryEntity16: BinaryAssociation = BinaryAssociation(
    name="ownedByFactoryEntity16",
    ends={
        Property(name="entitymodel18", type=gestionmodelosconsultas_entitymodel_Entity, multiplicity=Multiplicity(1, 1)),
        Property(name="DiagramEntity17", type=DiagramEntity, multiplicity=Multiplicity(0, 1))
    }
)
listAttributes19: BinaryAssociation = BinaryAssociation(
    name="listAttributes19",
    ends={
        Property(name="entitymodel20", type=gestionmodelosconsultas_entitymodel_Entity, multiplicity=Multiplicity(1, 1)),
        Property(name="Attribute", type=Attribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
rulesFactory0: BinaryAssociation = BinaryAssociation(
    name="rulesFactory0",
    ends={
        Property(name="rules", type=gestionmodelosconsultas_ModelFactory, multiplicity=Multiplicity(1, 1)),
        Property(name="factoryrules", type=factoryrules_RulesFactory, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
factoryModeloConsultas1: BinaryAssociation = BinaryAssociation(
    name="factoryModeloConsultas1",
    ends={
        Property(name="modeloconsultas", type=gestionmodelosconsultas_ModelFactory, multiplicity=Multiplicity(1, 1)),
        Property(name="FactoryModeloConsulta", type=FactoryModeloConsulta, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
diagramEntity2: BinaryAssociation = BinaryAssociation(
    name="diagramEntity2",
    ends={
        Property(name="entitymodel", type=gestionmodelosconsultas_ModelFactory, multiplicity=Multiplicity(1, 1)),
        Property(name="DiagramEntity", type=DiagramEntity, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
ModelFactory3: BinaryAssociation = BinaryAssociation(
    name="ModelFactory3",
    ends={
        Property(name="ModelFactory", type=gestionmodelosconsultas_factoryrules_RulesFactory, multiplicity=Multiplicity(1, 1)),
        Property(name="rulesFactory", type=factoryrules_gestionmodelosconsultas_ModelFactory, multiplicity=Multiplicity(0, 1))
    }
)
listRuleDiagramEntity4: BinaryAssociation = BinaryAssociation(
    name="listRuleDiagramEntity4",
    ends={
        Property(name="rules6", type=gestionmodelosconsultas_factoryrules_RulesFactory, multiplicity=Multiplicity(1, 1)),
        Property(name="factoryrules5", type=factoryrules_Rule, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ElementoRealizacionValueAttribute31: BinaryAssociation = BinaryAssociation(
    name="ElementoRealizacionValueAttribute31",
    ends={
        Property(name="entitymodel32", type=gestionmodelosconsultas_entitymodel_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="ElementoRealizacionValueAttribute", type=ElementoRealizacionValueAttribute, multiplicity=Multiplicity(0, 9999))
    }
)
ElementoRealizacionVisibleAttribute33: BinaryAssociation = BinaryAssociation(
    name="ElementoRealizacionVisibleAttribute33",
    ends={
        Property(name="entitymodel34", type=gestionmodelosconsultas_entitymodel_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="ElementoRealizacionVisibleAttribute", type=ElementoRealizacionVisibleAttribute, multiplicity=Multiplicity(0, 9999))
    }
)
ElementoRealizacionDiagramEntity35: BinaryAssociation = BinaryAssociation(
    name="ElementoRealizacionDiagramEntity35",
    ends={
        Property(name="entitymodel36", type=gestionmodelosconsultas_entitymodel_ModelElementEntity, multiplicity=Multiplicity(1, 1)),
        Property(name="ElementoRealizacionDiagramEntity", type=ElementoRealizacionDiagramEntity, multiplicity=Multiplicity(0, 9999))
    }
)
ModelFactory37: BinaryAssociation = BinaryAssociation(
    name="ModelFactory37",
    ends={
        Property(name="ModelFactory38", type=gestionmodelosconsultas_entitymodel_DiagramEntity, multiplicity=Multiplicity(1, 1)),
        Property(name="diagramEntity", type=entitymodel_gestionmodelosconsultas_ModelFactory, multiplicity=Multiplicity(0, 1))
    }
)
listEntity39: BinaryAssociation = BinaryAssociation(
    name="listEntity39",
    ends={
        Property(name="entitymodel41", type=gestionmodelosconsultas_entitymodel_DiagramEntity, multiplicity=Multiplicity(1, 1)),
        Property(name="Entity40", type=Entity, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
listEntityRelation42: BinaryAssociation = BinaryAssociation(
    name="listEntityRelation42",
    ends={
        Property(name="entitymodel43", type=gestionmodelosconsultas_entitymodel_DiagramEntity, multiplicity=Multiplicity(1, 1)),
        Property(name="EntityRelation", type=EntityRelation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ModeloConsulta44: BinaryAssociation = BinaryAssociation(
    name="ModeloConsulta44",
    ends={
        Property(name="modeloconsultas45", type=gestionmodelosconsultas_entitymodel_RealizacionDiagramEntity, multiplicity=Multiplicity(1, 1)),
        Property(name="ModeloConsulta", type=ModeloConsulta, multiplicity=Multiplicity(0, 1))
    }
)
listElementoRealizacionDiagramEntity46: BinaryAssociation = BinaryAssociation(
    name="listElementoRealizacionDiagramEntity46",
    ends={
        Property(name="entitymodel48", type=gestionmodelosconsultas_entitymodel_RealizacionDiagramEntity, multiplicity=Multiplicity(1, 1)),
        Property(name="ElementoRealizacionDiagramEntity47", type=ElementoRealizacionDiagramEntity, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
theFactoryEntity21: BinaryAssociation = BinaryAssociation(
    name="theFactoryEntity21",
    ends={
        Property(name="entitymodel23", type=gestionmodelosconsultas_entitymodel_EntityRelation, multiplicity=Multiplicity(1, 1)),
        Property(name="DiagramEntity22", type=DiagramEntity, multiplicity=Multiplicity(0, 1))
    }
)
source24: BinaryAssociation = BinaryAssociation(
    name="source24",
    ends={
        Property(name="Entity", type=gestionmodelosconsultas_entitymodel_EntityRelation, multiplicity=Multiplicity(1, 1)),
        Property(name="gestionmodelosconsultas_entitymodel_EntityRelation", type=Entity, multiplicity=Multiplicity(1, 1))
    }
)
target25: BinaryAssociation = BinaryAssociation(
    name="target25",
    ends={
        Property(name="Entity27", type=gestionmodelosconsultas_entitymodel_EntityRelation, multiplicity=Multiplicity(1, 1)),
        Property(name="gestionmodelosconsultas_entitymodel_EntityRelation26", type=Entity, multiplicity=Multiplicity(1, 1))
    }
)
Entity28: BinaryAssociation = BinaryAssociation(
    name="Entity28",
    ends={
        Property(name="entitymodel30", type=gestionmodelosconsultas_entitymodel_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="Entity29", type=Entity, multiplicity=Multiplicity(0, 1))
    }
)
ElementoRealizacionDiagramEntity64: BinaryAssociation = BinaryAssociation(
    name="ElementoRealizacionDiagramEntity64",
    ends={
        Property(name="entitymodel66", type=gestionmodelosconsultas_entitymodel_ElementoRealizacionValueAttribute, multiplicity=Multiplicity(1, 1)),
        Property(name="ElementoRealizacionDiagramEntity65", type=ElementoRealizacionDiagramEntity, multiplicity=Multiplicity(0, 1))
    }
)
values67: BinaryAssociation = BinaryAssociation(
    name="values67",
    ends={
        Property(name="entitymodel69", type=gestionmodelosconsultas_entitymodel_ElementoRealizacionValueAttribute, multiplicity=Multiplicity(1, 1)),
        Property(name="Value68", type=Value, multiplicity=Multiplicity(0, 9999))
    }
)
RealizacionDiagramEntity70: BinaryAssociation = BinaryAssociation(
    name="RealizacionDiagramEntity70",
    ends={
        Property(name="entitymodel72", type=gestionmodelosconsultas_entitymodel_ElementoRealizacionVisibleAttribute, multiplicity=Multiplicity(1, 1)),
        Property(name="RealizacionDiagramEntity71", type=RealizacionDiagramEntity, multiplicity=Multiplicity(0, 1))
    }
)
visibleAttribute73: BinaryAssociation = BinaryAssociation(
    name="visibleAttribute73",
    ends={
        Property(name="entitymodel75", type=gestionmodelosconsultas_entitymodel_ElementoRealizacionVisibleAttribute, multiplicity=Multiplicity(1, 1)),
        Property(name="Attribute74", type=Attribute, multiplicity=Multiplicity(0, 9999))
    }
)
ElementoRealizacionValueAttribute76: BinaryAssociation = BinaryAssociation(
    name="ElementoRealizacionValueAttribute76",
    ends={
        Property(name="entitymodel78", type=gestionmodelosconsultas_entitymodel_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="ElementoRealizacionValueAttribute77", type=ElementoRealizacionValueAttribute, multiplicity=Multiplicity(0, 9999))
    }
)
RealizacionDiagramEntity79: BinaryAssociation = BinaryAssociation(
    name="RealizacionDiagramEntity79",
    ends={
        Property(name="entitymodel81", type=gestionmodelosconsultas_entitymodel_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="RealizacionDiagramEntity80", type=RealizacionDiagramEntity, multiplicity=Multiplicity(0, 1))
    }
)
realizacionDiagramEntity82: BinaryAssociation = BinaryAssociation(
    name="realizacionDiagramEntity82",
    ends={
        Property(name="entitymodel84", type=gestionmodelosconsultas_modeloconsultas_ModeloConsulta, multiplicity=Multiplicity(1, 1)),
        Property(name="RealizacionDiagramEntity83", type=RealizacionDiagramEntity, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
FactoryModeloConsulta85: BinaryAssociation = BinaryAssociation(
    name="FactoryModeloConsulta85",
    ends={
        Property(name="modeloconsultas87", type=gestionmodelosconsultas_modeloconsultas_ModeloConsulta, multiplicity=Multiplicity(1, 1)),
        Property(name="FactoryModeloConsulta86", type=FactoryModeloConsulta, multiplicity=Multiplicity(0, 1))
    }
)
listEADiagram88: BinaryAssociation = BinaryAssociation(
    name="listEADiagram88",
    ends={
        Property(name="modeloconsultas89", type=gestionmodelosconsultas_modeloconsultas_ModeloConsulta, multiplicity=Multiplicity(1, 1)),
        Property(name="model", type=model_EADiagram, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
listResultado90: BinaryAssociation = BinaryAssociation(
    name="listResultado90",
    ends={
        Property(name="modeloconsultas91", type=gestionmodelosconsultas_modeloconsultas_ModeloConsulta, multiplicity=Multiplicity(1, 1)),
        Property(name="resultset", type=resultset_Resultado, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
realizacionVisibleAttribute49: BinaryAssociation = BinaryAssociation(
    name="realizacionVisibleAttribute49",
    ends={
        Property(name="entitymodel51", type=gestionmodelosconsultas_entitymodel_RealizacionDiagramEntity, multiplicity=Multiplicity(1, 1)),
        Property(name="ElementoRealizacionVisibleAttribute50", type=ElementoRealizacionVisibleAttribute, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
listValues52: BinaryAssociation = BinaryAssociation(
    name="listValues52",
    ends={
        Property(name="entitymodel53", type=gestionmodelosconsultas_entitymodel_RealizacionDiagramEntity, multiplicity=Multiplicity(1, 1)),
        Property(name="Value", type=Value, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
modelElementEntity54: BinaryAssociation = BinaryAssociation(
    name="modelElementEntity54",
    ends={
        Property(name="entitymodel55", type=gestionmodelosconsultas_entitymodel_ElementoRealizacionDiagramEntity, multiplicity=Multiplicity(1, 1)),
        Property(name="ModelElementEntity", type=ModelElementEntity, multiplicity=Multiplicity(1, 1))
    }
)
RealizacionDiagramEntity56: BinaryAssociation = BinaryAssociation(
    name="RealizacionDiagramEntity56",
    ends={
        Property(name="entitymodel57", type=gestionmodelosconsultas_entitymodel_ElementoRealizacionDiagramEntity, multiplicity=Multiplicity(1, 1)),
        Property(name="RealizacionDiagramEntity", type=RealizacionDiagramEntity, multiplicity=Multiplicity(0, 1))
    }
)
listElementoRealizacionAttribute58: BinaryAssociation = BinaryAssociation(
    name="listElementoRealizacionAttribute58",
    ends={
        Property(name="entitymodel60", type=gestionmodelosconsultas_entitymodel_ElementoRealizacionDiagramEntity, multiplicity=Multiplicity(1, 1)),
        Property(name="ElementoRealizacionValueAttribute59", type=ElementoRealizacionValueAttribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
valueAttribute61: BinaryAssociation = BinaryAssociation(
    name="valueAttribute61",
    ends={
        Property(name="entitymodel63", type=gestionmodelosconsultas_entitymodel_ElementoRealizacionValueAttribute, multiplicity=Multiplicity(1, 1)),
        Property(name="Attribute62", type=Attribute, multiplicity=Multiplicity(0, 9999))
    }
)
ownedElementoConsulta104: BinaryAssociation = BinaryAssociation(
    name="ownedElementoConsulta104",
    ends={
        Property(name="modeloconsultas106", type=gestionmodelosconsultas_model_Campo, multiplicity=Multiplicity(1, 1)),
        Property(name="model105", type=model_ElementoConsulta, multiplicity=Multiplicity(0, 1))
    }
)
ModelFactory92: BinaryAssociation = BinaryAssociation(
    name="ModelFactory92",
    ends={
        Property(name="ModelFactory93", type=gestionmodelosconsultas_modeloconsultas_FactoryModeloConsulta, multiplicity=Multiplicity(1, 1)),
        Property(name="factoryModeloConsultas", type=modeloconsultas_gestionmodelosconsultas_ModelFactory, multiplicity=Multiplicity(0, 1))
    }
)
listModeloConsulta94: BinaryAssociation = BinaryAssociation(
    name="listModeloConsulta94",
    ends={
        Property(name="modeloconsultas96", type=gestionmodelosconsultas_modeloconsultas_FactoryModeloConsulta, multiplicity=Multiplicity(1, 1)),
        Property(name="ModeloConsulta95", type=ModeloConsulta, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
EADiagram97: BinaryAssociation = BinaryAssociation(
    name="EADiagram97",
    ends={
        Property(name="modeloconsultas99", type=gestionmodelosconsultas_model_Relacion, multiplicity=Multiplicity(1, 1)),
        Property(name="model98", type=model_EADiagram, multiplicity=Multiplicity(0, 1))
    }
)
target100: BinaryAssociation = BinaryAssociation(
    name="target100",
    ends={
        Property(name="model_ElementoConsulta", type=gestionmodelosconsultas_model_Relacion, multiplicity=Multiplicity(1, 1)),
        Property(name="gestionmodelosconsultas_model_Relacion", type=model_ElementoConsulta, multiplicity=Multiplicity(1, 1))
    }
)
source101: BinaryAssociation = BinaryAssociation(
    name="source101",
    ends={
        Property(name="model_ElementoConsulta103", type=gestionmodelosconsultas_model_Relacion, multiplicity=Multiplicity(1, 1)),
        Property(name="gestionmodelosconsultas_model_Relacion102", type=model_ElementoConsulta, multiplicity=Multiplicity(1, 1))
    }
)
from122: BinaryAssociation = BinaryAssociation(
    name="from122",
    ends={
        Property(name="modeloconsultas124", type=gestionmodelosconsultas_model_ElementoModelo, multiplicity=Multiplicity(1, 1)),
        Property(name="model123", type=model_ElementoModelo, multiplicity=Multiplicity(0, 9999))
    }
)
to125: BinaryAssociation = BinaryAssociation(
    name="to125",
    ends={
        Property(name="modeloconsultas127", type=gestionmodelosconsultas_model_ElementoModelo, multiplicity=Multiplicity(1, 1)),
        Property(name="model126", type=model_ElementoModelo, multiplicity=Multiplicity(0, 9999))
    }
)
ModeloConsulta128: BinaryAssociation = BinaryAssociation(
    name="ModeloConsulta128",
    ends={
        Property(name="modeloconsultas130", type=gestionmodelosconsultas_resultset_Resultado, multiplicity=Multiplicity(1, 1)),
        Property(name="ModeloConsulta129", type=ModeloConsulta, multiplicity=Multiplicity(0, 1))
    }
)
listResultElement131: BinaryAssociation = BinaryAssociation(
    name="listResultElement131",
    ends={
        Property(name="modeloconsultas133", type=gestionmodelosconsultas_resultset_Resultado, multiplicity=Multiplicity(1, 1)),
        Property(name="resultset132", type=resultset_ResultElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
listElementoModeloResultado134: BinaryAssociation = BinaryAssociation(
    name="listElementoModeloResultado134",
    ends={
        Property(name="modeloconsultas136", type=gestionmodelosconsultas_resultset_ElementoModeloResultado, multiplicity=Multiplicity(1, 1)),
        Property(name="resultset135", type=resultset_ElementoModeloResultado, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ElementoModeloResultado137: BinaryAssociation = BinaryAssociation(
    name="ElementoModeloResultado137",
    ends={
        Property(name="modeloconsultas139", type=gestionmodelosconsultas_resultset_ElementoModeloResultado, multiplicity=Multiplicity(1, 1)),
        Property(name="resultset138", type=resultset_ElementoModeloResultado, multiplicity=Multiplicity(0, 1))
    }
)
Resultado140: BinaryAssociation = BinaryAssociation(
    name="Resultado140",
    ends={
        Property(name="modeloconsultas142", type=gestionmodelosconsultas_resultset_ResultElement, multiplicity=Multiplicity(1, 1)),
        Property(name="resultset141", type=resultset_Resultado, multiplicity=Multiplicity(0, 1))
    }
)
listRelacion107: BinaryAssociation = BinaryAssociation(
    name="listRelacion107",
    ends={
        Property(name="modeloconsultas109", type=gestionmodelosconsultas_model_EADiagram, multiplicity=Multiplicity(1, 1)),
        Property(name="model108", type=model_Relacion, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ModeloConsulta110: BinaryAssociation = BinaryAssociation(
    name="ModeloConsulta110",
    ends={
        Property(name="modeloconsultas112", type=gestionmodelosconsultas_model_EADiagram, multiplicity=Multiplicity(1, 1)),
        Property(name="ModeloConsulta111", type=ModeloConsulta, multiplicity=Multiplicity(0, 1))
    }
)
listElementoConsulta113: BinaryAssociation = BinaryAssociation(
    name="listElementoConsulta113",
    ends={
        Property(name="modeloconsultas115", type=gestionmodelosconsultas_model_EADiagram, multiplicity=Multiplicity(1, 1)),
        Property(name="model114", type=model_ElementoConsulta, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
EADiagram116: BinaryAssociation = BinaryAssociation(
    name="EADiagram116",
    ends={
        Property(name="modeloconsultas118", type=gestionmodelosconsultas_model_ElementoConsulta, multiplicity=Multiplicity(1, 1)),
        Property(name="model117", type=model_EADiagram, multiplicity=Multiplicity(0, 1))
    }
)
listCampos119: BinaryAssociation = BinaryAssociation(
    name="listCampos119",
    ends={
        Property(name="modeloconsultas121", type=gestionmodelosconsultas_model_ElementoConsulta, multiplicity=Multiplicity(1, 1)),
        Property(name="model120", type=model_Campo, multiplicity=Multiplicity(0, 9999), is_composite=True)
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
gen_gestionmodelosconsultas_resultset_ElementoModeloResultado_ResultElement = Generalization(general=ResultElement, specific=gestionmodelosconsultas_resultset_ElementoModeloResultado)
gen_gestionmodelosconsultas_resultcotracir_Transaccion_ElementoModeloResultado = Generalization(general=ElementoModeloResultado, specific=gestionmodelosconsultas_resultcotracir_Transaccion)
gen_gestionmodelosconsultas_model_ViewModel_EADiagram = Generalization(general=EADiagram, specific=gestionmodelosconsultas_model_ViewModel)
gen_gestionmodelosconsultas_model_ElementoConsulta_ElementoModelo = Generalization(general=ElementoModelo, specific=gestionmodelosconsultas_model_ElementoConsulta)
gen_gestionmodelosconsultas_model_Proyeccion_EADiagram = Generalization(general=EADiagram, specific=gestionmodelosconsultas_model_Proyeccion)
gen_gestionmodelosconsultas_resultcotracir_Planilla_ElementoModeloResultado = Generalization(general=ElementoModeloResultado, specific=gestionmodelosconsultas_resultcotracir_Planilla)
gen_gestionmodelosconsultas_resultcotracir_Detallado_ElementoModeloResultado = Generalization(general=ElementoModeloResultado, specific=gestionmodelosconsultas_resultcotracir_Detallado)
gen_gestionmodelosconsultas_resultcotracir_Trama_ElementoModeloResultado = Generalization(general=ElementoModeloResultado, specific=gestionmodelosconsultas_resultcotracir_Trama)
gen_gestionmodelosconsultas_resultcotracir_Consolidado_ElementoModeloResultado = Generalization(general=ElementoModeloResultado, specific=gestionmodelosconsultas_resultcotracir_Consolidado)
gen_gestionmodelosconsultas_resultcotracir_Propietario_ElementoModeloResultado = Generalization(general=ElementoModeloResultado, specific=gestionmodelosconsultas_resultcotracir_Propietario)
gen_gestionmodelosconsultas_cotracir_Planilla_ElementoConsulta = Generalization(general=ElementoConsulta, specific=gestionmodelosconsultas_cotracir_Planilla)
gen_gestionmodelosconsultas_cotracir_Consolidado_ElementoConsulta = Generalization(general=ElementoConsulta, specific=gestionmodelosconsultas_cotracir_Consolidado)
gen_gestionmodelosconsultas_cotracir_Transaccion_ElementoConsulta = Generalization(general=ElementoConsulta, specific=gestionmodelosconsultas_cotracir_Transaccion)
gen_gestionmodelosconsultas_cotracir_Trama_ElementoConsulta = Generalization(general=ElementoConsulta, specific=gestionmodelosconsultas_cotracir_Trama)
gen_gestionmodelosconsultas_cotracir_Propietario_ElementoConsulta = Generalization(general=ElementoConsulta, specific=gestionmodelosconsultas_cotracir_Propietario)
gen_gestionmodelosconsultas_cotracir_Detallado_ElementoConsulta = Generalization(general=ElementoConsulta, specific=gestionmodelosconsultas_cotracir_Detallado)

# Domain Model
domain_model = DomainModel(
    name="gestionmodelosconsultas",
    types={gestionmodelosconsultas_factoryrules_Rule, factoryrules_ChildRule, gestionmodelosconsultas_factoryrules_ChildRule, gestionmodelosconsultas_factoryrules_EntityName, ChildRule, gestionmodelosconsultas_factoryrules_RelationName, gestionmodelosconsultas_entitymodel_Entity, ModelElementEntity, Attribute, gestionmodelosconsultas_entitymodel_EntityRelation, gestionmodelosconsultas_ModelFactory, factoryrules_RulesFactory, FactoryModeloConsulta, DiagramEntity, gestionmodelosconsultas_factoryrules_RulesFactory, factoryrules_gestionmodelosconsultas_ModelFactory, factoryrules_Rule, ElementoRealizacionValueAttribute, ElementoRealizacionVisibleAttribute, gestionmodelosconsultas_entitymodel_ModelElementEntity, ElementoRealizacionDiagramEntity, gestionmodelosconsultas_entitymodel_DiagramEntity, entitymodel_gestionmodelosconsultas_ModelFactory, gestionmodelosconsultas_entitymodel_RealizacionDiagramEntity, ModeloConsulta, Entity, gestionmodelosconsultas_entitymodel_SimpleRelation, EntityRelation, gestionmodelosconsultas_entitymodel_AssociativeEntity, gestionmodelosconsultas_entitymodel_Attribute, gestionmodelosconsultas_entitymodel_ElementoRealizacionVisibleAttribute, gestionmodelosconsultas_entitymodel_Value, gestionmodelosconsultas_modeloconsultas_ModeloConsulta, model_EADiagram, resultset_Resultado, Value, gestionmodelosconsultas_entitymodel_ElementoRealizacionDiagramEntity, RealizacionDiagramEntity, gestionmodelosconsultas_entitymodel_ElementoRealizacionValueAttribute, gestionmodelosconsultas_modeloconsultas_FactoryModeloConsulta, modeloconsultas_gestionmodelosconsultas_ModelFactory, gestionmodelosconsultas_model_Relacion, ElementoModelo, model_ElementoConsulta, gestionmodelosconsultas_model_Campo, model_ElementoModelo, gestionmodelosconsultas_resultset_Resultado, resultset_ResultElement, gestionmodelosconsultas_resultset_ElementoModeloResultado, ResultElement, resultset_ElementoModeloResultado, gestionmodelosconsultas_resultset_ResultElement, gestionmodelosconsultas_resultcotracir_Transaccion, ElementoModeloResultado, gestionmodelosconsultas_model_EADiagram, model_Relacion, gestionmodelosconsultas_model_ViewModel, EADiagram, gestionmodelosconsultas_model_ElementoConsulta, model_Campo, gestionmodelosconsultas_model_Proyeccion, gestionmodelosconsultas_model_ElementoModelo, gestionmodelosconsultas_resultcotracir_Planilla, gestionmodelosconsultas_resultcotracir_NewClass, gestionmodelosconsultas_resultcotracir_Detallado, gestionmodelosconsultas_resultcotracir_Trama, gestionmodelosconsultas_resultcotracir_Consolidado, gestionmodelosconsultas_resultcotracir_Propietario, gestionmodelosconsultas_cotracir_Planilla, ElementoConsulta, gestionmodelosconsultas_cotracir_Consolidado, gestionmodelosconsultas_cotracir_Transaccion, gestionmodelosconsultas_cotracir_Trama, gestionmodelosconsultas_cotracir_Propietario, gestionmodelosconsultas_cotracir_Detallado, AttributeType, Multiplicity, TipoModelElementEntity, Type, NombreCampo},
    associations={RulesFactory7, listChildRule10, Rule13, ownedByFactoryEntity16, listAttributes19, rulesFactory0, factoryModeloConsultas1, diagramEntity2, ModelFactory3, listRuleDiagramEntity4, ElementoRealizacionValueAttribute31, ElementoRealizacionVisibleAttribute33, ElementoRealizacionDiagramEntity35, ModelFactory37, listEntity39, listEntityRelation42, ModeloConsulta44, listElementoRealizacionDiagramEntity46, theFactoryEntity21, source24, target25, Entity28, ElementoRealizacionDiagramEntity64, values67, RealizacionDiagramEntity70, visibleAttribute73, ElementoRealizacionValueAttribute76, RealizacionDiagramEntity79, realizacionDiagramEntity82, FactoryModeloConsulta85, listEADiagram88, listResultado90, realizacionVisibleAttribute49, listValues52, modelElementEntity54, RealizacionDiagramEntity56, listElementoRealizacionAttribute58, valueAttribute61, ownedElementoConsulta104, ModelFactory92, listModeloConsulta94, EADiagram97, target100, source101, from122, to125, ModeloConsulta128, listResultElement131, listElementoModeloResultado134, ElementoModeloResultado137, Resultado140, listRelacion107, ModeloConsulta110, listElementoConsulta113, EADiagram116, listCampos119},
    generalizations={gen_gestionmodelosconsultas_factoryrules_EntityName_ChildRule, gen_gestionmodelosconsultas_factoryrules_RelationName_ChildRule, gen_gestionmodelosconsultas_entitymodel_Entity_ModelElementEntity, gen_gestionmodelosconsultas_entitymodel_EntityRelation_ModelElementEntity, gen_gestionmodelosconsultas_entitymodel_SimpleRelation_EntityRelation, gen_gestionmodelosconsultas_entitymodel_AssociativeEntity_Entity, gen_gestionmodelosconsultas_model_Relacion_ElementoModelo, gen_gestionmodelosconsultas_resultset_ElementoModeloResultado_ResultElement, gen_gestionmodelosconsultas_resultcotracir_Transaccion_ElementoModeloResultado, gen_gestionmodelosconsultas_model_ViewModel_EADiagram, gen_gestionmodelosconsultas_model_ElementoConsulta_ElementoModelo, gen_gestionmodelosconsultas_model_Proyeccion_EADiagram, gen_gestionmodelosconsultas_resultcotracir_Planilla_ElementoModeloResultado, gen_gestionmodelosconsultas_resultcotracir_Detallado_ElementoModeloResultado, gen_gestionmodelosconsultas_resultcotracir_Trama_ElementoModeloResultado, gen_gestionmodelosconsultas_resultcotracir_Consolidado_ElementoModeloResultado, gen_gestionmodelosconsultas_resultcotracir_Propietario_ElementoModeloResultado, gen_gestionmodelosconsultas_cotracir_Planilla_ElementoConsulta, gen_gestionmodelosconsultas_cotracir_Consolidado_ElementoConsulta, gen_gestionmodelosconsultas_cotracir_Transaccion_ElementoConsulta, gen_gestionmodelosconsultas_cotracir_Trama_ElementoConsulta, gen_gestionmodelosconsultas_cotracir_Propietario_ElementoConsulta, gen_gestionmodelosconsultas_cotracir_Detallado_ElementoConsulta},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)