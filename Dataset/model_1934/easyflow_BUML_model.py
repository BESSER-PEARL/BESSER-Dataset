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
DataFormat: Enumeration = Enumeration(
    name="DataFormat",
    literals={
            EnumerationLiteral(name="CSV"),
			EnumerationLiteral(name="BAI"),
			EnumerationLiteral(name="SAI"),
			EnumerationLiteral(name="VCF_IDX"),
			EnumerationLiteral(name="FASTA"),
			EnumerationLiteral(name="BWT"),
			EnumerationLiteral(name="None"),
			EnumerationLiteral(name="FASTQ"),
			EnumerationLiteral(name="SAM"),
			EnumerationLiteral(name="BAM"),
			EnumerationLiteral(name="VCF"),
			EnumerationLiteral(name="BCF"),
			EnumerationLiteral(name="TXT"),
			EnumerationLiteral(name="DICT"),
			EnumerationLiteral(name="FAI"),
			EnumerationLiteral(name="IntervalList")
    }
)

DataCriterion: Enumeration = Enumeration(
    name="DataCriterion",
    literals={
            EnumerationLiteral(name="None"),
			EnumerationLiteral(name="Readgroup"),
			EnumerationLiteral(name="Sample"),
			EnumerationLiteral(name="Library")
    }
)

TraversalCriterion: Enumeration = Enumeration(
    name="TraversalCriterion",
    literals={
            EnumerationLiteral(name="IntervalList"),
			EnumerationLiteral(name="Contig"),
			EnumerationLiteral(name="Readgroup"),
			EnumerationLiteral(name="Library"),
			EnumerationLiteral(name="Sample"),
			EnumerationLiteral(name="ReadEnd"),
			EnumerationLiteral(name="Readpair"),
			EnumerationLiteral(name="SplitRead"),
			EnumerationLiteral(name="Locus"),
			EnumerationLiteral(name="None"),
			EnumerationLiteral(name="Read"),
			EnumerationLiteral(name="ReadMappingFlag")
    }
)

# Classes
easyflow_Workflow = Class(name="easyflow::Workflow")
easyflow_Task = Class(name="easyflow::Task")
easyflow_EasyFlowTemplate = Class(name="easyflow::EasyFlowTemplate")
easyflow_EasyFlowConfiguration = Class(name="easyflow::EasyFlowConfiguration")
easyflow_EasyFlowMetadata = Class(name="easyflow::EasyFlowMetadata")
easyflow_EasyFlowImplementationTemplate = Class(name="easyflow::EasyFlowImplementationTemplate")
easyflow_DataProcessingType = Class(name="easyflow::DataProcessingType")
easyflow_DataProcessingTypeToTask = Class(name="easyflow::DataProcessingTypeToTask")
easyflow_TaskToDataProcessingType = Class(name="easyflow::TaskToDataProcessingType")
easyflow_DataFormatToTaskList = Class(name="easyflow::DataFormatToTaskList")
easyflow_StringToToolMap = Class(name="easyflow::StringToToolMap")
easyflow_StringToTaskMap = Class(name="easyflow::StringToTaskMap")
easyflow_StringToGroupingCriterionMap = Class(name="easyflow::StringToGroupingCriterionMap")
easyflow_StringToTraversalCriterionMap = Class(name="easyflow::StringToTraversalCriterionMap")
easyflow_StringToGroupMap = Class(name="easyflow::StringToGroupMap")
easyflow_IWorkflowUtil = Class(name="easyflow::IWorkflowUtil", is_abstract=True)
easyflow_Tool = Class(name="easyflow::Tool")
easyflow_CommandArgument = Class(name="easyflow::CommandArgument")
easyflow_GroupingCriterion = Class(name="easyflow::GroupingCriterion")
easyflow_Interpreter = Class(name="easyflow::Interpreter")
easyflow_Argument = Class(name="easyflow::Argument")
easyflow_StringToLibraryMap = Class(name="easyflow::StringToLibraryMap")
easyflow_StringToRecordMap = Class(name="easyflow::StringToRecordMap")
easyflow_Group = Class(name="easyflow::Group")
GroupingCriterion = Class(name="GroupingCriterion")
easyflow_StringToSampleMap = Class(name="easyflow::StringToSampleMap")
easyflow_StringToReadgroupMap = Class(name="easyflow::StringToReadgroupMap")
easyflow_Library = Class(name="easyflow::Library")
easyflow_Sample = Class(name="easyflow::Sample")
easyflow_Readgroup = Class(name="easyflow::Readgroup")
easyflow_Record = Class(name="easyflow::Record")
easyflow_EasyFlowMetadataReader = Class(name="easyflow::EasyFlowMetadataReader")
EasyFlowMetadata = Class(name="EasyFlowMetadata")
easyflow_Job = Class(name="easyflow::Job")
easyflow_ITraversal = Class(name="easyflow::ITraversal", is_abstract=True)
easyflow_Traversal = Class(name="easyflow::Traversal")
ITraversal = Class(name="ITraversal")
easyflow_StringToChunkMap = Class(name="easyflow::StringToChunkMap")
easyflow_GenericTraversalCriterion = Class(name="easyflow::GenericTraversalCriterion")
Traversal = Class(name="Traversal")
easyflow_ReadEnd = Class(name="easyflow::ReadEnd")
easyflow_Contig = Class(name="easyflow::Contig")
easyflow_Locus = Class(name="easyflow::Locus")
easyflow_SplittingEvent = Class(name="easyflow::SplittingEvent")
easyflow_GroupingEvent = Class(name="easyflow::GroupingEvent")
easyflow_Chunk = Class(name="easyflow::Chunk")

# easyflow_Workflow class attributes and methods
easyflow_Workflow_graph: Property = Property(name="graph", type=StringType)
easyflow_Workflow_name: Property = Property(name="name", type=StringType)
easyflow_Workflow_dag: Property = Property(name="dag", type=StringType)
easyflow_Workflow_jobDag: Property = Property(name="jobDag", type=StringType)
easyflow_Workflow_m_writeMakeflow: Method = Method(name="writeMakeflow", parameters={})
easyflow_Workflow_m_resolveStaticDependencies: Method = Method(name="resolveStaticDependencies", parameters={})
easyflow_Workflow_m_getNextSplittingEvent: Method = Method(name="getNextSplittingEvent", parameters={Parameter(name='processedTasks')})
easyflow_Workflow_m_writeAWSCloudFormation: Method = Method(name="writeAWSCloudFormation", parameters={})
easyflow_Workflow_m_processMetadata: Method = Method(name="processMetadata", parameters={Parameter(name='task'), Parameter(name='metadata')})
easyflow_Workflow_m_processMetadataSet: Method = Method(name="processMetadataSet", parameters={Parameter(name='task')})
easyflow_Workflow_m_checkDag: Method = Method(name="checkDag", parameters={})
easyflow_Workflow_m_createTaskDag: Method = Method(name="createTaskDag", parameters={})
easyflow_Workflow_m_createJobDag: Method = Method(name="createJobDag", parameters={})
easyflow_Workflow_m_getTasksFromLastTaskClass: Method = Method(name="getTasksFromLastTaskClass", parameters={Parameter(name='dataFormatIn'), Parameter(name='dataFormatOut'), Parameter(name='strategy')}, type=StringType)
easyflow_Workflow_m_iterateByGroup: Method = Method(name="iterateByGroup", parameters={Parameter(name='group'), Parameter(name='task'), Parameter(name='dataCriterion'), Parameter(name='dag')}, type=StringType)
easyflow_Workflow_m_getTasksFromLastTaskClassMap: Method = Method(name="getTasksFromLastTaskClassMap", parameters={Parameter(name='strategy'), Parameter(name='dataProcessingTypeIn')})
easyflow_Workflow_m_printLastTaskClassMap: Method = Method(name="printLastTaskClassMap", parameters={})
easyflow_Workflow_m_updateLastTaskClass: Method = Method(name="updateLastTaskClass", parameters={Parameter(name='task'), Parameter(name='dataFormatIn'), Parameter(name='dataFormatOut')})
easyflow_Workflow_m_printLastTaskMap: Method = Method(name="printLastTaskMap", parameters={})
easyflow_Workflow_m_updateLastTaskClassMap: Method = Method(name="updateLastTaskClassMap", parameters={Parameter(name='task'), Parameter(name='dataProcessingType')})
easyflow_Workflow.attributes={easyflow_Workflow_name, easyflow_Workflow_dag, easyflow_Workflow_graph, easyflow_Workflow_jobDag}
easyflow_Workflow.methods={easyflow_Workflow_m_getTasksFromLastTaskClassMap, easyflow_Workflow_m_processMetadata, easyflow_Workflow_m_updateLastTaskClassMap, easyflow_Workflow_m_iterateByGroup, easyflow_Workflow_m_createJobDag, easyflow_Workflow_m_getTasksFromLastTaskClass, easyflow_Workflow_m_getNextSplittingEvent, easyflow_Workflow_m_writeAWSCloudFormation, easyflow_Workflow_m_printLastTaskMap, easyflow_Workflow_m_processMetadataSet, easyflow_Workflow_m_printLastTaskClassMap, easyflow_Workflow_m_writeMakeflow, easyflow_Workflow_m_updateLastTaskClass, easyflow_Workflow_m_createTaskDag, easyflow_Workflow_m_checkDag, easyflow_Workflow_m_resolveStaticDependencies}

# easyflow_Task class attributes and methods
easyflow_Task_name: Property = Property(name="name", type=StringType)
easyflow_Task_dataFormatIn: Property = Property(name="dataFormatIn", type=StringType)
easyflow_Task_dataFormatOut: Property = Property(name="dataFormatOut", type=StringType)
easyflow_Task_splitCriterion: Property = Property(name="splitCriterion", type=StringType)
easyflow_Task_contrast: Property = Property(name="contrast", type=BooleanType)
easyflow_Task_static: Property = Property(name="static", type=BooleanType)
easyflow_Task_cardinalityIn: Property = Property(name="cardinalityIn", type=StringType)
easyflow_Task_util: Property = Property(name="util", type=BooleanType)
easyflow_Task_jexlString: Property = Property(name="jexlString", type=StringType)
easyflow_Task_cardinalityOut: Property = Property(name="cardinalityOut", type=StringType)
easyflow_Task_dataCriterion: Property = Property(name="dataCriterion", type=StringType)
easyflow_Task_isMultipleInstancesOfDataCriterion: Property = Property(name="isMultipleInstancesOfDataCriterion", type=StringType)
easyflow_Task_mergeCriterion: Property = Property(name="mergeCriterion", type=StringType)
easyflow_Task_traversalCriterion: Property = Property(name="traversalCriterion", type=StringType)
easyflow_Task_skipGroupingCriterion: Property = Property(name="skipGroupingCriterion", type=StringType)
easyflow_Task_depricated: Property = Property(name="depricated", type=BooleanType)
easyflow_Task_m_readTask: Method = Method(name="readTask", parameters={Parameter(name='wtplLine')})
easyflow_Task_m_getSampleUniqueString: Method = Method(name="getSampleUniqueString", parameters={}, type=StringType)
easyflow_Task_m_evaluateJexlExp: Method = Method(name="evaluateJexlExp", parameters={Parameter(name='map')}, type=BooleanType)
easyflow_Task_m_getParentForTask: Method = Method(name="getParentForTask", parameters={Parameter(name='graph')}, type=StringType)
easyflow_Task_m_copy: Method = Method(name="copy", parameters={}, type=StringType)
easyflow_Task_m_getUniqueString: Method = Method(name="getUniqueString", parameters={}, type=StringType)
easyflow_Task_m_fitsToGroupingCriterionOf: Method = Method(name="fitsToGroupingCriterionOf", parameters={Parameter(name='task')}, type=BooleanType)
easyflow_Task_m_isConvertableTo: Method = Method(name="isConvertableTo", parameters={Parameter(name='dataFormat')}, type=BooleanType)
easyflow_Task_m_isMarkedToSkip: Method = Method(name="isMarkedToSkip", parameters={}, type=BooleanType)
easyflow_Task_m_getParentForTask: Method = Method(name="getParentForTask", parameters={Parameter(name='dag')}, type=StringType)
easyflow_Task.attributes={easyflow_Task_splitCriterion, easyflow_Task_name, easyflow_Task_dataFormatOut, easyflow_Task_util, easyflow_Task_static, easyflow_Task_cardinalityOut, easyflow_Task_dataCriterion, easyflow_Task_isMultipleInstancesOfDataCriterion, easyflow_Task_jexlString, easyflow_Task_contrast, easyflow_Task_mergeCriterion, easyflow_Task_depricated, easyflow_Task_skipGroupingCriterion, easyflow_Task_traversalCriterion, easyflow_Task_cardinalityIn, easyflow_Task_dataFormatIn}
easyflow_Task.methods={easyflow_Task_m_fitsToGroupingCriterionOf, easyflow_Task_m_readTask, easyflow_Task_m_getParentForTask, easyflow_Task_m_getUniqueString, easyflow_Task_m_copy, easyflow_Task_m_getParentForTask, easyflow_Task_m_isMarkedToSkip, easyflow_Task_m_evaluateJexlExp, easyflow_Task_m_isConvertableTo, easyflow_Task_m_getSampleUniqueString}

# easyflow_EasyFlowTemplate class attributes and methods
easyflow_EasyFlowTemplate_fileName: Property = Property(name="fileName", type=StringType)
easyflow_EasyFlowTemplate_m_generateDAGFromTemplateFile: Method = Method(name="generateDAGFromTemplateFile", parameters={}, type=StringType)
easyflow_EasyFlowTemplate_m_generateGraphFromTemplateFile: Method = Method(name="generateGraphFromTemplateFile", parameters={}, type=StringType)
easyflow_EasyFlowTemplate.attributes={easyflow_EasyFlowTemplate_fileName}
easyflow_EasyFlowTemplate.methods={easyflow_EasyFlowTemplate_m_generateDAGFromTemplateFile, easyflow_EasyFlowTemplate_m_generateGraphFromTemplateFile}

# easyflow_EasyFlowConfiguration class attributes and methods
easyflow_EasyFlowConfiguration_fileName: Property = Property(name="fileName", type=StringType)
easyflow_EasyFlowConfiguration_configMap: Property = Property(name="configMap", type=StringType)
easyflow_EasyFlowConfiguration_m_configFileReader: Method = Method(name="configFileReader", parameters={})
easyflow_EasyFlowConfiguration.attributes={easyflow_EasyFlowConfiguration_fileName, easyflow_EasyFlowConfiguration_configMap}
easyflow_EasyFlowConfiguration.methods={easyflow_EasyFlowConfiguration_m_configFileReader}

# easyflow_EasyFlowMetadata class attributes and methods
easyflow_EasyFlowMetadata_name: Property = Property(name="name", type=StringType)
easyflow_EasyFlowMetadata_contrast: Property = Property(name="contrast", type=BooleanType)
easyflow_EasyFlowMetadata_refData: Property = Property(name="refData", type=StringType)
easyflow_EasyFlowMetadata.attributes={easyflow_EasyFlowMetadata_contrast, easyflow_EasyFlowMetadata_name, easyflow_EasyFlowMetadata_refData}

# easyflow_EasyFlowImplementationTemplate class attributes and methods
easyflow_EasyFlowImplementationTemplate_fileName: Property = Property(name="fileName", type=StringType)
easyflow_EasyFlowImplementationTemplate_parameterConfigFileName: Property = Property(name="parameterConfigFileName", type=StringType)
easyflow_EasyFlowImplementationTemplate_parameterConfigMap: Property = Property(name="parameterConfigMap", type=StringType)
easyflow_EasyFlowImplementationTemplate_jsonRootNode: Property = Property(name="jsonRootNode", type=StringType)
easyflow_EasyFlowImplementationTemplate_globalOptions: Property = Property(name="globalOptions", type=StringType)
easyflow_EasyFlowImplementationTemplate_m_templateFileParser: Method = Method(name="templateFileParser", parameters={Parameter(name='dag')})
easyflow_EasyFlowImplementationTemplate_m_readParameterConfig: Method = Method(name="readParameterConfig", parameters={Parameter(name='toolName')})
easyflow_EasyFlowImplementationTemplate_m_initJsonRootNode: Method = Method(name="initJsonRootNode", parameters={})
easyflow_EasyFlowImplementationTemplate.attributes={easyflow_EasyFlowImplementationTemplate_fileName, easyflow_EasyFlowImplementationTemplate_globalOptions, easyflow_EasyFlowImplementationTemplate_jsonRootNode, easyflow_EasyFlowImplementationTemplate_parameterConfigMap, easyflow_EasyFlowImplementationTemplate_parameterConfigFileName}
easyflow_EasyFlowImplementationTemplate.methods={easyflow_EasyFlowImplementationTemplate_m_readParameterConfig, easyflow_EasyFlowImplementationTemplate_m_initJsonRootNode, easyflow_EasyFlowImplementationTemplate_m_templateFileParser}

# easyflow_DataProcessingType class attributes and methods
easyflow_DataProcessingType_dataFormatIn: Property = Property(name="dataFormatIn", type=StringType)
easyflow_DataProcessingType_dataFormatOut: Property = Property(name="dataFormatOut", type=StringType)
easyflow_DataProcessingType_m_isConvertableTo: Method = Method(name="isConvertableTo", parameters={Parameter(name='dataProcessingTypeOut')}, type=BooleanType)
easyflow_DataProcessingType.attributes={easyflow_DataProcessingType_dataFormatOut, easyflow_DataProcessingType_dataFormatIn}
easyflow_DataProcessingType.methods={easyflow_DataProcessingType_m_isConvertableTo}

# easyflow_DataProcessingTypeToTask class attributes and methods

# easyflow_TaskToDataProcessingType class attributes and methods

# easyflow_DataFormatToTaskList class attributes and methods
easyflow_DataFormatToTaskList_key: Property = Property(name="key", type=StringType)
easyflow_DataFormatToTaskList.attributes={easyflow_DataFormatToTaskList_key}

# easyflow_StringToToolMap class attributes and methods
easyflow_StringToToolMap_key: Property = Property(name="key", type=StringType)
easyflow_StringToToolMap.attributes={easyflow_StringToToolMap_key}

# easyflow_StringToTaskMap class attributes and methods
easyflow_StringToTaskMap_key: Property = Property(name="key", type=StringType)
easyflow_StringToTaskMap.attributes={easyflow_StringToTaskMap_key}

# easyflow_StringToGroupingCriterionMap class attributes and methods
easyflow_StringToGroupingCriterionMap_key: Property = Property(name="key", type=StringType)
easyflow_StringToGroupingCriterionMap.attributes={easyflow_StringToGroupingCriterionMap_key}

# easyflow_StringToTraversalCriterionMap class attributes and methods
easyflow_StringToTraversalCriterionMap_key: Property = Property(name="key", type=StringType)
easyflow_StringToTraversalCriterionMap_value: Property = Property(name="value", type=StringType)
easyflow_StringToTraversalCriterionMap.attributes={easyflow_StringToTraversalCriterionMap_key, easyflow_StringToTraversalCriterionMap_value}

# easyflow_StringToGroupMap class attributes and methods
easyflow_StringToGroupMap_key: Property = Property(name="key", type=StringType)
easyflow_StringToGroupMap.attributes={easyflow_StringToGroupMap_key}

# easyflow_IWorkflowUtil class attributes and methods
easyflow_IWorkflowUtil_m_writeDagToDot: Method = Method(name="writeDagToDot", parameters={Parameter(name='fileName'), Parameter(name='dag')})
easyflow_IWorkflowUtil_m_addTaskListToGraph: Method = Method(name="addTaskListToGraph", parameters={Parameter(name='lastTasks'), Parameter(name='graph'), Parameter(name='curTask')})
easyflow_IWorkflowUtil_m_getAllTasks: Method = Method(name="getAllTasks", parameters={}, type=StringType)
easyflow_IWorkflowUtil_m_addTaskListToDAG: Method = Method(name="addTaskListToDAG", parameters={Parameter(name='curTask'), Parameter(name='dag'), Parameter(name='lastTasks')})
easyflow_IWorkflowUtil_m_getTaskByName: Method = Method(name="getTaskByName", parameters={Parameter(name='tasks'), Parameter(name='taskNames')})
easyflow_IWorkflowUtil_m_getGroupingCriterion: Method = Method(name="getGroupingCriterion", parameters={Parameter(name='dataCriterion'), Parameter(name='group'), Parameter(name='key')}, type=StringType)
easyflow_IWorkflowUtil_m_getKeysForGroupingCriterion: Method = Method(name="getKeysForGroupingCriterion", parameters={Parameter(name='dataCriterion'), Parameter(name='group')})
easyflow_IWorkflowUtil_m_convertDagToGraph: Method = Method(name="convertDagToGraph", parameters={Parameter(name='dag'), Parameter(name='graph')}, type=StringType)
easyflow_IWorkflowUtil_m_convertGraphToDag: Method = Method(name="convertGraphToDag", parameters={Parameter(name='graph')}, type=StringType)
easyflow_IWorkflowUtil.methods={easyflow_IWorkflowUtil_m_getAllTasks, easyflow_IWorkflowUtil_m_getKeysForGroupingCriterion, easyflow_IWorkflowUtil_m_writeDagToDot, easyflow_IWorkflowUtil_m_addTaskListToDAG, easyflow_IWorkflowUtil_m_getTaskByName, easyflow_IWorkflowUtil_m_getGroupingCriterion, easyflow_IWorkflowUtil_m_addTaskListToGraph, easyflow_IWorkflowUtil_m_convertGraphToDag, easyflow_IWorkflowUtil_m_convertDagToGraph}

# easyflow_Tool class attributes and methods
easyflow_Tool_toolName: Property = Property(name="toolName", type=StringType)
easyflow_Tool_source: Property = Property(name="source", type=StringType)
easyflow_Tool_subCmd: Property = Property(name="subCmd", type=StringType)
easyflow_Tool_subCmdPrefix: Property = Property(name="subCmdPrefix", type=StringType)
easyflow_Tool_type: Property = Property(name="type", type=StringType)
easyflow_Tool_category: Property = Property(name="category", type=StringType)
easyflow_Tool_pattern: Property = Property(name="pattern", type=StringType)
easyflow_Tool_refData: Property = Property(name="refData", type=StringType)
easyflow_Tool_m_applyGlobalOptions: Method = Method(name="applyGlobalOptions", parameters={Parameter(name='globalOptions')})
easyflow_Tool_m_createJob: Method = Method(name="createJob", parameters={Parameter(name='groupingId')}, type=StringType)
easyflow_Tool.attributes={easyflow_Tool_subCmdPrefix, easyflow_Tool_category, easyflow_Tool_pattern, easyflow_Tool_toolName, easyflow_Tool_refData, easyflow_Tool_subCmd, easyflow_Tool_type, easyflow_Tool_source}
easyflow_Tool.methods={easyflow_Tool_m_applyGlobalOptions, easyflow_Tool_m_createJob}

# easyflow_CommandArgument class attributes and methods
easyflow_CommandArgument_name: Property = Property(name="name", type=StringType)
easyflow_CommandArgument_arg: Property = Property(name="arg", type=StringType)
easyflow_CommandArgument_sep: Property = Property(name="sep", type=StringType)
easyflow_CommandArgument_named: Property = Property(name="named", type=BooleanType)
easyflow_CommandArgument_required: Property = Property(name="required", type=BooleanType)
easyflow_CommandArgument_m_setGlobalCmdProperties: Method = Method(name="setGlobalCmdProperties", parameters={Parameter(name='parameterConfigMap')})
easyflow_CommandArgument_m_setCmdProperties: Method = Method(name="setCmdProperties", parameters={Parameter(name='parameterConfigMap')})
easyflow_CommandArgument_m_printArgument: Method = Method(name="printArgument", parameters={Parameter(name='fileName')}, type=StringType)
easyflow_CommandArgument_m_printStaticArg: Method = Method(name="printStaticArg", parameters={}, type=StringType)
easyflow_CommandArgument_m_printGenericArg: Method = Method(name="printGenericArg", parameters={Parameter(name='generica')}, type=StringType)
easyflow_CommandArgument.attributes={easyflow_CommandArgument_sep, easyflow_CommandArgument_name, easyflow_CommandArgument_arg, easyflow_CommandArgument_required, easyflow_CommandArgument_named}
easyflow_CommandArgument.methods={easyflow_CommandArgument_m_setCmdProperties, easyflow_CommandArgument_m_printStaticArg, easyflow_CommandArgument_m_printGenericArg, easyflow_CommandArgument_m_printArgument, easyflow_CommandArgument_m_setGlobalCmdProperties}

# easyflow_GroupingCriterion class attributes and methods
easyflow_GroupingCriterion_id: Property = Property(name="id", type=StringType)
easyflow_GroupingCriterion_m_getMap: Method = Method(name="getMap", parameters={Parameter(name='groupCritMap')})
easyflow_GroupingCriterion_m_getLibraryString: Method = Method(name="getLibraryString", parameters={Parameter(name='groupingCriterion')})
easyflow_GroupingCriterion_m_getKeysForGroupingCriterion: Method = Method(name="getKeysForGroupingCriterion", parameters={Parameter(name='group'), Parameter(name='dataCriterion')})
easyflow_GroupingCriterion_m_getGroupingCriterion: Method = Method(name="getGroupingCriterion", parameters={Parameter(name='key'), Parameter(name='group'), Parameter(name='dataCriterion')}, type=StringType)
easyflow_GroupingCriterion_m_getGroupString: Method = Method(name="getGroupString", parameters={Parameter(name='groupingCriterion')})
easyflow_GroupingCriterion_m_getSampleString: Method = Method(name="getSampleString", parameters={Parameter(name='groupingCriterion')})
easyflow_GroupingCriterion_m_getRecordString: Method = Method(name="getRecordString", parameters={Parameter(name='groupingCriterion')})
easyflow_GroupingCriterion_m_getReadgroupString: Method = Method(name="getReadgroupString", parameters={Parameter(name='groupingCriterion')})
easyflow_GroupingCriterion_m_getUniqueStringForParent: Method = Method(name="getUniqueStringForParent", parameters={Parameter(name='parentGroupingCriterion')})
easyflow_GroupingCriterion_m_equalsParent: Method = Method(name="equalsParent", parameters={Parameter(name='map')}, type=BooleanType)
easyflow_GroupingCriterion.attributes={easyflow_GroupingCriterion_id}
easyflow_GroupingCriterion.methods={easyflow_GroupingCriterion_m_equalsParent, easyflow_GroupingCriterion_m_getLibraryString, easyflow_GroupingCriterion_m_getRecordString, easyflow_GroupingCriterion_m_getMap, easyflow_GroupingCriterion_m_getUniqueStringForParent, easyflow_GroupingCriterion_m_getKeysForGroupingCriterion, easyflow_GroupingCriterion_m_getSampleString, easyflow_GroupingCriterion_m_getReadgroupString, easyflow_GroupingCriterion_m_getGroupString, easyflow_GroupingCriterion_m_getGroupingCriterion}

# easyflow_Interpreter class attributes and methods
easyflow_Interpreter_name: Property = Property(name="name", type=StringType)
easyflow_Interpreter_exe: Property = Property(name="exe", type=StringType)
easyflow_Interpreter_subCmd: Property = Property(name="subCmd", type=StringType)
easyflow_Interpreter_options: Property = Property(name="options", type=StringType)
easyflow_Interpreter.attributes={easyflow_Interpreter_options, easyflow_Interpreter_name, easyflow_Interpreter_subCmd, easyflow_Interpreter_exe}

# easyflow_Argument class attributes and methods
easyflow_Argument_name: Property = Property(name="name", type=StringType)
easyflow_Argument_arg: Property = Property(name="arg", type=StringType)
easyflow_Argument_sep: Property = Property(name="sep", type=StringType)
easyflow_Argument.attributes={easyflow_Argument_sep, easyflow_Argument_name, easyflow_Argument_arg}

# easyflow_StringToLibraryMap class attributes and methods
easyflow_StringToLibraryMap_key: Property = Property(name="key", type=StringType)
easyflow_StringToLibraryMap.attributes={easyflow_StringToLibraryMap_key}

# easyflow_StringToRecordMap class attributes and methods
easyflow_StringToRecordMap_key: Property = Property(name="key", type=StringType)
easyflow_StringToRecordMap.attributes={easyflow_StringToRecordMap_key}

# easyflow_Group class attributes and methods
easyflow_Group_name: Property = Property(name="name", type=StringType)
easyflow_Group.attributes={easyflow_Group_name}

# GroupingCriterion class attributes and methods

# easyflow_StringToSampleMap class attributes and methods
easyflow_StringToSampleMap_key: Property = Property(name="key", type=StringType)
easyflow_StringToSampleMap.attributes={easyflow_StringToSampleMap_key}

# easyflow_StringToReadgroupMap class attributes and methods
easyflow_StringToReadgroupMap_key: Property = Property(name="key", type=StringType)
easyflow_StringToReadgroupMap.attributes={easyflow_StringToReadgroupMap_key}

# easyflow_Library class attributes and methods
easyflow_Library_name: Property = Property(name="name", type=StringType)
easyflow_Library_insertSize: Property = Property(name="insertSize", type=IntegerType)
easyflow_Library_readLength: Property = Property(name="readLength", type=IntegerType)
easyflow_Library.attributes={easyflow_Library_readLength, easyflow_Library_insertSize, easyflow_Library_name}

# easyflow_Sample class attributes and methods
easyflow_Sample_name: Property = Property(name="name", type=StringType)
easyflow_Sample.attributes={easyflow_Sample_name}

# easyflow_Readgroup class attributes and methods
easyflow_Readgroup_name: Property = Property(name="name", type=StringType)
easyflow_Readgroup_platform: Property = Property(name="platform", type=StringType)
easyflow_Readgroup_platformUnit: Property = Property(name="platformUnit", type=StringType)
easyflow_Readgroup_description: Property = Property(name="description", type=StringType)
easyflow_Readgroup.attributes={easyflow_Readgroup_platform, easyflow_Readgroup_description, easyflow_Readgroup_platformUnit, easyflow_Readgroup_name}

# easyflow_Record class attributes and methods
easyflow_Record_refData: Property = Property(name="refData", type=StringType)
easyflow_Record_fileNames: Property = Property(name="fileNames", type=StringType)
easyflow_Record.attributes={easyflow_Record_fileNames, easyflow_Record_refData}

# easyflow_EasyFlowMetadataReader class attributes and methods
easyflow_EasyFlowMetadataReader_fileName: Property = Property(name="fileName", type=StringType)
easyflow_EasyFlowMetadataReader_m_metadataFileReader: Method = Method(name="metadataFileReader", parameters={})
easyflow_EasyFlowMetadataReader.attributes={easyflow_EasyFlowMetadataReader_fileName}
easyflow_EasyFlowMetadataReader.methods={easyflow_EasyFlowMetadataReader_m_metadataFileReader}

# EasyFlowMetadata class attributes and methods

# easyflow_Job class attributes and methods
easyflow_Job_interpreterOption: Property = Property(name="interpreterOption", type=StringType)
easyflow_Job_dependencies: Property = Property(name="dependencies", type=StringType)
easyflow_Job_targets: Property = Property(name="targets", type=StringType)
easyflow_Job_inputArgs: Property = Property(name="inputArgs", type=StringType)
easyflow_Job_name: Property = Property(name="name", type=StringType)
easyflow_Job_exe: Property = Property(name="exe", type=StringType)
easyflow_Job_outputArgs: Property = Property(name="outputArgs", type=StringType)
easyflow_Job_genericArgs: Property = Property(name="genericArgs", type=StringType)
easyflow_Job_staticArgs: Property = Property(name="staticArgs", type=StringType)
easyflow_Job_targetPlatform: Property = Property(name="targetPlatform", type=StringType)
easyflow_Job_targetPlatformOptions: Property = Property(name="targetPlatformOptions", type=StringType)
easyflow_Job_subCmd: Property = Property(name="subCmd", type=StringType)
easyflow_Job_source: Property = Property(name="source", type=StringType)
easyflow_Job_m_writeMakeflowRule: Method = Method(name="writeMakeflowRule", parameters={}, type=StringType)
easyflow_Job.attributes={easyflow_Job_staticArgs, easyflow_Job_targets, easyflow_Job_outputArgs, easyflow_Job_genericArgs, easyflow_Job_subCmd, easyflow_Job_inputArgs, easyflow_Job_targetPlatform, easyflow_Job_source, easyflow_Job_targetPlatformOptions, easyflow_Job_interpreterOption, easyflow_Job_exe, easyflow_Job_dependencies, easyflow_Job_name}
easyflow_Job.methods={easyflow_Job_m_writeMakeflowRule}

# easyflow_ITraversal class attributes and methods
easyflow_ITraversal_m_readChunks: Method = Method(name="readChunks", parameters={Parameter(name='fileName')})
easyflow_ITraversal_m_readChunks: Method = Method(name="readChunks", parameters={})
easyflow_ITraversal_m_getChunksAsString: Method = Method(name="getChunksAsString", parameters={}, type=StringType)
easyflow_ITraversal_m_readTemplate: Method = Method(name="readTemplate", parameters={Parameter(name='fileName')})
easyflow_ITraversal.methods={easyflow_ITraversal_m_getChunksAsString, easyflow_ITraversal_m_readChunks, easyflow_ITraversal_m_readTemplate, easyflow_ITraversal_m_readChunks}

# easyflow_Traversal class attributes and methods
easyflow_Traversal_tarversalCriterion: Property = Property(name="tarversalCriterion", type=StringType)
easyflow_Traversal.attributes={easyflow_Traversal_tarversalCriterion}

# ITraversal class attributes and methods

# easyflow_StringToChunkMap class attributes and methods
easyflow_StringToChunkMap_key: Property = Property(name="key", type=StringType)
easyflow_StringToChunkMap.attributes={easyflow_StringToChunkMap_key}

# easyflow_GenericTraversalCriterion class attributes and methods

# Traversal class attributes and methods

# easyflow_ReadEnd class attributes and methods
easyflow_ReadEnd_m_readChunks: Method = Method(name="readChunks", parameters={})
easyflow_ReadEnd.methods={easyflow_ReadEnd_m_readChunks}

# easyflow_Contig class attributes and methods
easyflow_Contig_m_readChunks: Method = Method(name="readChunks", parameters={})
easyflow_Contig.methods={easyflow_Contig_m_readChunks}

# easyflow_Locus class attributes and methods
easyflow_Locus_m_readChunks: Method = Method(name="readChunks", parameters={})
easyflow_Locus.methods={easyflow_Locus_m_readChunks}

# easyflow_SplittingEvent class attributes and methods
easyflow_SplittingEvent_traversalCriterion: Property = Property(name="traversalCriterion", type=StringType)
easyflow_SplittingEvent_traversalChunks: Property = Property(name="traversalChunks", type=StringType)
easyflow_SplittingEvent_dag: Property = Property(name="dag", type=StringType)
easyflow_SplittingEvent_processedTask: Property = Property(name="processedTask", type=StringType)
easyflow_SplittingEvent_traversalImplDir: Property = Property(name="traversalImplDir", type=StringType)
easyflow_SplittingEvent_m_getTraversalImplementation: Method = Method(name="getTraversalImplementation", parameters={Parameter(name='metadata')}, type=ITraversal)
easyflow_SplittingEvent_m_removePath: Method = Method(name="removePath", parameters={})
easyflow_SplittingEvent_m_insertPathToDag: Method = Method(name="insertPathToDag", parameters={Parameter(name='chunks')})
easyflow_SplittingEvent_m_applyTraversalCriterion: Method = Method(name="applyTraversalCriterion", parameters={Parameter(name='metadata')})
easyflow_SplittingEvent.attributes={easyflow_SplittingEvent_processedTask, easyflow_SplittingEvent_traversalCriterion, easyflow_SplittingEvent_traversalImplDir, easyflow_SplittingEvent_dag, easyflow_SplittingEvent_traversalChunks}
easyflow_SplittingEvent.methods={easyflow_SplittingEvent_m_getTraversalImplementation, easyflow_SplittingEvent_m_applyTraversalCriterion, easyflow_SplittingEvent_m_removePath, easyflow_SplittingEvent_m_insertPathToDag}

# easyflow_GroupingEvent class attributes and methods
easyflow_GroupingEvent_dagOut: Property = Property(name="dagOut", type=StringType)
easyflow_GroupingEvent_dagIn: Property = Property(name="dagIn", type=StringType)
easyflow_GroupingEvent_m_applyGroupingCriterion: Method = Method(name="applyGroupingCriterion", parameters={Parameter(name='metadata')}, type=StringType)
easyflow_GroupingEvent.attributes={easyflow_GroupingEvent_dagOut, easyflow_GroupingEvent_dagIn}
easyflow_GroupingEvent.methods={easyflow_GroupingEvent_m_applyGroupingCriterion}

# easyflow_Chunk class attributes and methods
easyflow_Chunk_name: Property = Property(name="name", type=StringType)
easyflow_Chunk_tool: Property = Property(name="tool", type=StringType)
easyflow_Chunk_argument: Property = Property(name="argument", type=StringType)
easyflow_Chunk.attributes={easyflow_Chunk_argument, easyflow_Chunk_name, easyflow_Chunk_tool}

# Relationships
lastTaskMap13: BinaryAssociation = BinaryAssociation(
    name="lastTaskMap13",
    ends={
        Property(name="easyflow_Workflow14", type=easyflow_DataFormatToTaskList, multiplicity=Multiplicity(0, 9999), is_composite=True),
        Property(name="easyflow_DataFormatToTaskList", type=easyflow_Workflow, multiplicity=Multiplicity(1, 1))
    }
)
WorkflowTemplate0: BinaryAssociation = BinaryAssociation(
    name="WorkflowTemplate0",
    ends={
        Property(name="easyflow_EasyFlowTemplate", type=easyflow_Workflow, multiplicity=Multiplicity(1, 1)),
        Property(name="easyflow_Workflow", type=easyflow_EasyFlowTemplate, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
Configuration1: BinaryAssociation = BinaryAssociation(
    name="Configuration1",
    ends={
        Property(name="easyflow_EasyFlowConfiguration", type=easyflow_Workflow, multiplicity=Multiplicity(1, 1)),
        Property(name="easyflow_Workflow2", type=easyflow_EasyFlowConfiguration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
metadata3: BinaryAssociation = BinaryAssociation(
    name="metadata3",
    ends={
        Property(name="easyflow_EasyFlowMetadata", type=easyflow_Workflow, multiplicity=Multiplicity(1, 1)),
        Property(name="easyflow_Workflow4", type=easyflow_EasyFlowMetadata, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
ImplementationTemplate5: BinaryAssociation = BinaryAssociation(
    name="ImplementationTemplate5",
    ends={
        Property(name="easyflow_EasyFlowImplementationTemplate", type=easyflow_Workflow, multiplicity=Multiplicity(1, 1)),
        Property(name="easyflow_Workflow6", type=easyflow_EasyFlowImplementationTemplate, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
DataProcessingType7: BinaryAssociation = BinaryAssociation(
    name="DataProcessingType7",
    ends={
        Property(name="easyflow_DataProcessingType", type=easyflow_Workflow, multiplicity=Multiplicity(1, 1)),
        Property(name="easyflow_Workflow8", type=easyflow_DataProcessingType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
LastTaskClassMap9: BinaryAssociation = BinaryAssociation(
    name="LastTaskClassMap9",
    ends={
        Property(name="easyflow_DataProcessingTypeToTask", type=easyflow_Workflow, multiplicity=Multiplicity(1, 1)),
        Property(name="easyflow_Workflow10", type=easyflow_DataProcessingTypeToTask, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
taskMap11: BinaryAssociation = BinaryAssociation(
    name="taskMap11",
    ends={
        Property(name="easyflow_TaskToDataProcessingType", type=easyflow_Workflow, multiplicity=Multiplicity(1, 1)),
        Property(name="easyflow_Workflow12", type=easyflow_TaskToDataProcessingType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
tool15: BinaryAssociation = BinaryAssociation(
    name="tool15",
    ends={
        Property(name="easyflow_StringToToolMap", type=easyflow_Task, multiplicity=Multiplicity(1, 1)),
        Property(name="easyflow_Task", type=easyflow_StringToToolMap, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parentTasks16: BinaryAssociation = BinaryAssociation(
    name="parentTasks16",
    ends={
        Property(name="easyflow_StringToTaskMap", type=easyflow_Task, multiplicity=Multiplicity(1, 1)),
        Property(name="easyflow_Task17", type=easyflow_StringToTaskMap, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
groupingCriterionMap18: BinaryAssociation = BinaryAssociation(
    name="groupingCriterionMap18",
    ends={
        Property(name="easyflow_StringToGroupingCriterionMap", type=easyflow_Task, multiplicity=Multiplicity(1, 1)),
        Property(name="easyflow_Task19", type=easyflow_StringToGroupingCriterionMap, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
key25: BinaryAssociation = BinaryAssociation(
    name="key25",
    ends={
        Property(name="easyflow_TaskToDataProcessingType27", type=easyflow_Task, multiplicity=Multiplicity(1, 1)),
        Property(name="easyflow_Task26", type=easyflow_TaskToDataProcessingType, multiplicity=Multiplicity(0, 1))
    }
)
workflow28: BinaryAssociation = BinaryAssociation(
    name="workflow28",
    ends={
        Property(name="easyflow_Workflow30", type=easyflow_EasyFlowTemplate, multiplicity=Multiplicity(1, 1)),
        Property(name="easyflow_EasyFlowTemplate29", type=easyflow_Workflow, multiplicity=Multiplicity(0, 1))
    }
)
chunks20: BinaryAssociation = BinaryAssociation(
    name="chunks20",
    ends={
        Property(name="easyflow_StringToTraversalCriterionMap", type=easyflow_Task, multiplicity=Multiplicity(1, 1)),
        Property(name="easyflow_Task21", type=easyflow_StringToTraversalCriterionMap, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
groups31: BinaryAssociation = BinaryAssociation(
    name="groups31",
    ends={
        Property(name="easyflow_StringToGroupMap", type=easyflow_EasyFlowMetadata, multiplicity=Multiplicity(1, 1)),
        Property(name="easyflow_EasyFlowMetadata32", type=easyflow_StringToGroupMap, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
sortOrder22: BinaryAssociation = BinaryAssociation(
    name="sortOrder22",
    ends={
        Property(name="easyflow_StringToTraversalCriterionMap24", type=easyflow_Task, multiplicity=Multiplicity(1, 1)),
        Property(name="easyflow_Task23", type=easyflow_StringToTraversalCriterionMap, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
key33: BinaryAssociation = BinaryAssociation(
    name="key33",
    ends={
        Property(name="easyflow_DataProcessingType35", type=easyflow_DataProcessingTypeToTask, multiplicity=Multiplicity(1, 1)),
        Property(name="easyflow_DataProcessingTypeToTask34", type=easyflow_DataProcessingType, multiplicity=Multiplicity(0, 1))
    }
)
value36: BinaryAssociation = BinaryAssociation(
    name="value36",
    ends={
        Property(name="easyflow_Task38", type=easyflow_DataProcessingTypeToTask, multiplicity=Multiplicity(1, 1)),
        Property(name="easyflow_DataProcessingTypeToTask37", type=easyflow_Task, multiplicity=Multiplicity(0, 9999))
    }
)
argIn39: BinaryAssociation = BinaryAssociation(
    name="argIn39",
    ends={
        Property(name="easyflow_CommandArgument", type=easyflow_Tool, multiplicity=Multiplicity(1, 1)),
        Property(name="easyflow_Tool", type=easyflow_CommandArgument, multiplicity=Multiplicity(0, 9999))
    }
)
argOut40: BinaryAssociation = BinaryAssociation(
    name="argOut40",
    ends={
        Property(name="easyflow_CommandArgument42", type=easyflow_Tool, multiplicity=Multiplicity(1, 1)),
        Property(name="easyflow_Tool41", type=easyflow_CommandArgument, multiplicity=Multiplicity(0, 9999))
    }
)
staticArg43: BinaryAssociation = BinaryAssociation(
    name="staticArg43",
    ends={
        Property(name="easyflow_CommandArgument45", type=easyflow_Tool, multiplicity=Multiplicity(1, 1)),
        Property(name="easyflow_Tool44", type=easyflow_CommandArgument, multiplicity=Multiplicity(0, 9999))
    }
)
genericArg46: BinaryAssociation = BinaryAssociation(
    name="genericArg46",
    ends={
        Property(name="easyflow_CommandArgument48", type=easyflow_Tool, multiplicity=Multiplicity(1, 1)),
        Property(name="easyflow_Tool47", type=easyflow_CommandArgument, multiplicity=Multiplicity(0, 9999))
    }
)
interpreter49: BinaryAssociation = BinaryAssociation(
    name="interpreter49",
    ends={
        Property(name="easyflow_Interpreter", type=easyflow_Tool, multiplicity=Multiplicity(1, 1)),
        Property(name="easyflow_Tool50", type=easyflow_Interpreter, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
task51: BinaryAssociation = BinaryAssociation(
    name="task51",
    ends={
        Property(name="easyflow_Task53", type=easyflow_Tool, multiplicity=Multiplicity(1, 1)),
        Property(name="easyflow_Tool52", type=easyflow_Task, multiplicity=Multiplicity(0, 1))
    }
)
libraries59: BinaryAssociation = BinaryAssociation(
    name="libraries59",
    ends={
        Property(name="easyflow_StringToLibraryMap", type=easyflow_Group, multiplicity=Multiplicity(1, 1)),
        Property(name="easyflow_Group60", type=easyflow_StringToLibraryMap, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
records61: BinaryAssociation = BinaryAssociation(
    name="records61",
    ends={
        Property(name="easyflow_StringToRecordMap", type=easyflow_Group, multiplicity=Multiplicity(1, 1)),
        Property(name="easyflow_Group62", type=easyflow_StringToRecordMap, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
metadata54: BinaryAssociation = BinaryAssociation(
    name="metadata54",
    ends={
        Property(name="easyflow_EasyFlowMetadata55", type=easyflow_GroupingCriterion, multiplicity=Multiplicity(1, 1)),
        Property(name="easyflow_GroupingCriterion", type=easyflow_EasyFlowMetadata, multiplicity=Multiplicity(0, 1))
    }
)
samples56: BinaryAssociation = BinaryAssociation(
    name="samples56",
    ends={
        Property(name="easyflow_StringToSampleMap", type=easyflow_Group, multiplicity=Multiplicity(1, 1)),
        Property(name="easyflow_Group", type=easyflow_StringToSampleMap, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
readgroups57: BinaryAssociation = BinaryAssociation(
    name="readgroups57",
    ends={
        Property(name="easyflow_StringToReadgroupMap", type=easyflow_Group, multiplicity=Multiplicity(1, 1)),
        Property(name="easyflow_Group58", type=easyflow_StringToReadgroupMap, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
samples71: BinaryAssociation = BinaryAssociation(
    name="samples71",
    ends={
        Property(name="easyflow_Readgroup", type=easyflow_StringToSampleMap, multiplicity=Multiplicity(0, 9999), is_composite=True),
        Property(name="easyflow_StringToSampleMap72", type=easyflow_Readgroup, multiplicity=Multiplicity(1, 1))
    }
)
libraries73: BinaryAssociation = BinaryAssociation(
    name="libraries73",
    ends={
        Property(name="easyflow_StringToLibraryMap75", type=easyflow_Readgroup, multiplicity=Multiplicity(1, 1)),
        Property(name="easyflow_Readgroup74", type=easyflow_StringToLibraryMap, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
libraries63: BinaryAssociation = BinaryAssociation(
    name="libraries63",
    ends={
        Property(name="easyflow_StringToLibraryMap64", type=easyflow_Sample, multiplicity=Multiplicity(1, 1)),
        Property(name="easyflow_Sample", type=easyflow_StringToLibraryMap, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
records65: BinaryAssociation = BinaryAssociation(
    name="records65",
    ends={
        Property(name="easyflow_StringToRecordMap67", type=easyflow_Sample, multiplicity=Multiplicity(1, 1)),
        Property(name="easyflow_Sample66", type=easyflow_StringToRecordMap, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
readgroups68: BinaryAssociation = BinaryAssociation(
    name="readgroups68",
    ends={
        Property(name="easyflow_StringToReadgroupMap70", type=easyflow_Sample, multiplicity=Multiplicity(1, 1)),
        Property(name="easyflow_Sample69", type=easyflow_StringToReadgroupMap, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
library89: BinaryAssociation = BinaryAssociation(
    name="library89",
    ends={
        Property(name="easyflow_Library91", type=easyflow_Record, multiplicity=Multiplicity(1, 1)),
        Property(name="easyflow_Record90", type=easyflow_Library, multiplicity=Multiplicity(0, 1))
    }
)
samples76: BinaryAssociation = BinaryAssociation(
    name="samples76",
    ends={
        Property(name="easyflow_StringToSampleMap77", type=easyflow_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="easyflow_Library", type=easyflow_StringToSampleMap, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
records78: BinaryAssociation = BinaryAssociation(
    name="records78",
    ends={
        Property(name="easyflow_StringToRecordMap80", type=easyflow_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="easyflow_Library79", type=easyflow_StringToRecordMap, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
readgroups81: BinaryAssociation = BinaryAssociation(
    name="readgroups81",
    ends={
        Property(name="easyflow_StringToReadgroupMap83", type=easyflow_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="easyflow_Library82", type=easyflow_StringToReadgroupMap, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
sample84: BinaryAssociation = BinaryAssociation(
    name="sample84",
    ends={
        Property(name="easyflow_Sample85", type=easyflow_Record, multiplicity=Multiplicity(1, 1)),
        Property(name="easyflow_Record", type=easyflow_Sample, multiplicity=Multiplicity(0, 1))
    }
)
readgroup86: BinaryAssociation = BinaryAssociation(
    name="readgroup86",
    ends={
        Property(name="easyflow_Readgroup88", type=easyflow_Record, multiplicity=Multiplicity(1, 1)),
        Property(name="easyflow_Record87", type=easyflow_Readgroup, multiplicity=Multiplicity(0, 1))
    }
)
value101: BinaryAssociation = BinaryAssociation(
    name="value101",
    ends={
        Property(name="easyflow_Library103", type=easyflow_StringToLibraryMap, multiplicity=Multiplicity(1, 1)),
        Property(name="easyflow_StringToLibraryMap102", type=easyflow_Library, multiplicity=Multiplicity(0, 1))
    }
)
value104: BinaryAssociation = BinaryAssociation(
    name="value104",
    ends={
        Property(name="easyflow_Tool106", type=easyflow_StringToToolMap, multiplicity=Multiplicity(1, 1)),
        Property(name="easyflow_StringToToolMap105", type=easyflow_Tool, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
value92: BinaryAssociation = BinaryAssociation(
    name="value92",
    ends={
        Property(name="easyflow_Group94", type=easyflow_StringToGroupMap, multiplicity=Multiplicity(1, 1)),
        Property(name="easyflow_StringToGroupMap93", type=easyflow_Group, multiplicity=Multiplicity(0, 1))
    }
)
value95: BinaryAssociation = BinaryAssociation(
    name="value95",
    ends={
        Property(name="easyflow_Sample97", type=easyflow_StringToSampleMap, multiplicity=Multiplicity(1, 1)),
        Property(name="easyflow_StringToSampleMap96", type=easyflow_Sample, multiplicity=Multiplicity(0, 1))
    }
)
value98: BinaryAssociation = BinaryAssociation(
    name="value98",
    ends={
        Property(name="easyflow_Readgroup100", type=easyflow_StringToReadgroupMap, multiplicity=Multiplicity(1, 1)),
        Property(name="easyflow_StringToReadgroupMap99", type=easyflow_Readgroup, multiplicity=Multiplicity(0, 1))
    }
)
value107: BinaryAssociation = BinaryAssociation(
    name="value107",
    ends={
        Property(name="easyflow_Task109", type=easyflow_StringToTaskMap, multiplicity=Multiplicity(1, 1)),
        Property(name="easyflow_StringToTaskMap108", type=easyflow_Task, multiplicity=Multiplicity(0, 1))
    }
)
value110: BinaryAssociation = BinaryAssociation(
    name="value110",
    ends={
        Property(name="easyflow_Record112", type=easyflow_StringToRecordMap, multiplicity=Multiplicity(1, 1)),
        Property(name="easyflow_StringToRecordMap111", type=easyflow_Record, multiplicity=Multiplicity(0, 1))
    }
)
value113: BinaryAssociation = BinaryAssociation(
    name="value113",
    ends={
        Property(name="easyflow_GroupingCriterion115", type=easyflow_StringToGroupingCriterionMap, multiplicity=Multiplicity(1, 1)),
        Property(name="easyflow_StringToGroupingCriterionMap114", type=easyflow_GroupingCriterion, multiplicity=Multiplicity(0, 1))
    }
)
metadata116: BinaryAssociation = BinaryAssociation(
    name="metadata116",
    ends={
        Property(name="easyflow_EasyFlowMetadata117", type=easyflow_Job, multiplicity=Multiplicity(1, 1)),
        Property(name="easyflow_Job", type=easyflow_EasyFlowMetadata, multiplicity=Multiplicity(0, 1))
    }
)
splittingTask118: BinaryAssociation = BinaryAssociation(
    name="splittingTask118",
    ends={
        Property(name="easyflow_Task119", type=easyflow_ITraversal, multiplicity=Multiplicity(1, 1)),
        Property(name="easyflow_ITraversal", type=easyflow_Task, multiplicity=Multiplicity(0, 1))
    }
)
chunks120: BinaryAssociation = BinaryAssociation(
    name="chunks120",
    ends={
        Property(name="easyflow_StringToChunkMap", type=easyflow_Traversal, multiplicity=Multiplicity(1, 1)),
        Property(name="easyflow_Traversal", type=easyflow_StringToChunkMap, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parentTask121: BinaryAssociation = BinaryAssociation(
    name="parentTask121",
    ends={
        Property(name="easyflow_Task122", type=easyflow_SplittingEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="easyflow_SplittingEvent", type=easyflow_Task, multiplicity=Multiplicity(0, 1))
    }
)
splittingTask123: BinaryAssociation = BinaryAssociation(
    name="splittingTask123",
    ends={
        Property(name="easyflow_Task125", type=easyflow_SplittingEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="easyflow_SplittingEvent124", type=easyflow_Task, multiplicity=Multiplicity(0, 1))
    }
)
mergingChildTask126: BinaryAssociation = BinaryAssociation(
    name="mergingChildTask126",
    ends={
        Property(name="easyflow_Task128", type=easyflow_SplittingEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="easyflow_SplittingEvent127", type=easyflow_Task, multiplicity=Multiplicity(0, 1))
    }
)
value129: BinaryAssociation = BinaryAssociation(
    name="value129",
    ends={
        Property(name="easyflow_DataProcessingType131", type=easyflow_TaskToDataProcessingType, multiplicity=Multiplicity(1, 1)),
        Property(name="easyflow_TaskToDataProcessingType130", type=easyflow_DataProcessingType, multiplicity=Multiplicity(0, 1))
    }
)
key132: BinaryAssociation = BinaryAssociation(
    name="key132",
    ends={
        Property(name="easyflow_Task134", type=easyflow_TaskToDataProcessingType, multiplicity=Multiplicity(1, 1)),
        Property(name="easyflow_TaskToDataProcessingType133", type=easyflow_Task, multiplicity=Multiplicity(0, 1))
    }
)
value135: BinaryAssociation = BinaryAssociation(
    name="value135",
    ends={
        Property(name="easyflow_Task137", type=easyflow_DataFormatToTaskList, multiplicity=Multiplicity(1, 1)),
        Property(name="easyflow_DataFormatToTaskList136", type=easyflow_Task, multiplicity=Multiplicity(0, 9999))
    }
)
value138: BinaryAssociation = BinaryAssociation(
    name="value138",
    ends={
        Property(name="easyflow_Chunk", type=easyflow_StringToChunkMap, multiplicity=Multiplicity(1, 1)),
        Property(name="easyflow_StringToChunkMap139", type=easyflow_Chunk, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_easyflow_Group_GroupingCriterion = Generalization(general=GroupingCriterion, specific=easyflow_Group)
gen_easyflow_Library_GroupingCriterion = Generalization(general=GroupingCriterion, specific=easyflow_Library)
gen_easyflow_Sample_GroupingCriterion = Generalization(general=GroupingCriterion, specific=easyflow_Sample)
gen_easyflow_Readgroup_GroupingCriterion = Generalization(general=GroupingCriterion, specific=easyflow_Readgroup)
gen_easyflow_Record_GroupingCriterion = Generalization(general=GroupingCriterion, specific=easyflow_Record)
gen_easyflow_EasyFlowMetadataReader_EasyFlowMetadata = Generalization(general=EasyFlowMetadata, specific=easyflow_EasyFlowMetadataReader)
gen_easyflow_Traversal_ITraversal = Generalization(general=ITraversal, specific=easyflow_Traversal)
gen_easyflow_GenericTraversalCriterion_Traversal = Generalization(general=Traversal, specific=easyflow_GenericTraversalCriterion)
gen_easyflow_ReadEnd_Traversal = Generalization(general=Traversal, specific=easyflow_ReadEnd)
gen_easyflow_Contig_Traversal = Generalization(general=Traversal, specific=easyflow_Contig)
gen_easyflow_Locus_Traversal = Generalization(general=Traversal, specific=easyflow_Locus)

# Domain Model
domain_model = DomainModel(
    name="easyflow",
    types={easyflow_Workflow, easyflow_Task, easyflow_EasyFlowTemplate, easyflow_EasyFlowConfiguration, easyflow_EasyFlowMetadata, easyflow_EasyFlowImplementationTemplate, easyflow_DataProcessingType, easyflow_DataProcessingTypeToTask, easyflow_TaskToDataProcessingType, easyflow_DataFormatToTaskList, easyflow_StringToToolMap, easyflow_StringToTaskMap, easyflow_StringToGroupingCriterionMap, easyflow_StringToTraversalCriterionMap, easyflow_StringToGroupMap, easyflow_IWorkflowUtil, easyflow_Tool, easyflow_CommandArgument, easyflow_GroupingCriterion, easyflow_Interpreter, easyflow_Argument, easyflow_StringToLibraryMap, easyflow_StringToRecordMap, easyflow_Group, GroupingCriterion, easyflow_StringToSampleMap, easyflow_StringToReadgroupMap, easyflow_Library, easyflow_Sample, easyflow_Readgroup, easyflow_Record, easyflow_EasyFlowMetadataReader, EasyFlowMetadata, easyflow_Job, easyflow_ITraversal, easyflow_Traversal, ITraversal, easyflow_StringToChunkMap, easyflow_GenericTraversalCriterion, Traversal, easyflow_ReadEnd, easyflow_Contig, easyflow_Locus, easyflow_SplittingEvent, easyflow_GroupingEvent, easyflow_Chunk, DataFormat, DataCriterion, TraversalCriterion},
    associations={lastTaskMap13, WorkflowTemplate0, Configuration1, metadata3, ImplementationTemplate5, DataProcessingType7, LastTaskClassMap9, taskMap11, tool15, parentTasks16, groupingCriterionMap18, key25, workflow28, chunks20, groups31, sortOrder22, key33, value36, argIn39, argOut40, staticArg43, genericArg46, interpreter49, task51, libraries59, records61, metadata54, samples56, readgroups57, samples71, libraries73, libraries63, records65, readgroups68, library89, samples76, records78, readgroups81, sample84, readgroup86, value101, value104, value92, value95, value98, value107, value110, value113, metadata116, splittingTask118, chunks120, parentTask121, splittingTask123, mergingChildTask126, value129, key132, value135, value138},
    generalizations={gen_easyflow_Group_GroupingCriterion, gen_easyflow_Library_GroupingCriterion, gen_easyflow_Sample_GroupingCriterion, gen_easyflow_Readgroup_GroupingCriterion, gen_easyflow_Record_GroupingCriterion, gen_easyflow_EasyFlowMetadataReader_EasyFlowMetadata, gen_easyflow_Traversal_ITraversal, gen_easyflow_GenericTraversalCriterion_Traversal, gen_easyflow_ReadEnd_Traversal, gen_easyflow_Contig_Traversal, gen_easyflow_Locus_Traversal},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)