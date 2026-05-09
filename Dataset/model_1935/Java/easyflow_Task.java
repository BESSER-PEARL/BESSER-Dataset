





import java.util.List;
import java.util.ArrayList;

public class easyflow_Task  {

    private boolean contrast;
    private String dataFormatOut;
    private String traversalCriterion;
    private String isMultipleInstancesOfDataCriterion;
    private String dataFormatIn;
    private String cardinalityOut;
    private boolean static;
    private boolean depricated;
    private String jexlString;
    private boolean util;
    private String mergeCriterion;
    private String name;
    private String cardinalityIn;
    private String splitCriterion;
    private String skipGroupingCriterion;
    private String dataCriterion;





    private easyflow_DataFormatToTaskList easyflow_dataformattotasklist;




    private easyflow_TaskToDataProcessingType easyflow_tasktodataprocessingtype;




    private easyflow_TaskToDataProcessingType easyflow_tasktodataprocessingtype;




    private easyflow_DataProcessingTypeToTask easyflow_dataprocessingtypetotask;


    public easyflow_Task(
        boolean contrast,        String dataFormatOut,        String traversalCriterion,        String isMultipleInstancesOfDataCriterion,        String dataFormatIn,        String cardinalityOut,        boolean static,        boolean depricated,        String jexlString,        boolean util,        String mergeCriterion,        String name,        String cardinalityIn,        String splitCriterion,        String skipGroupingCriterion,        String dataCriterion    ) {
        this.contrast = contrast;
        this.dataFormatOut = dataFormatOut;
        this.traversalCriterion = traversalCriterion;
        this.isMultipleInstancesOfDataCriterion = isMultipleInstancesOfDataCriterion;
        this.dataFormatIn = dataFormatIn;
        this.cardinalityOut = cardinalityOut;
        this.static = static;
        this.depricated = depricated;
        this.jexlString = jexlString;
        this.util = util;
        this.mergeCriterion = mergeCriterion;
        this.name = name;
        this.cardinalityIn = cardinalityIn;
        this.splitCriterion = splitCriterion;
        this.skipGroupingCriterion = skipGroupingCriterion;
        this.dataCriterion = dataCriterion;
    }


    public boolean getContrast() {
        return contrast;
    }

    public void setContrast(boolean contrast) {
        this.contrast = contrast;
    }
    public String getDataformatout() {
        return dataFormatOut;
    }

    public void setDataformatout(String dataFormatOut) {
        this.dataFormatOut = dataFormatOut;
    }
    public String getTraversalcriterion() {
        return traversalCriterion;
    }

    public void setTraversalcriterion(String traversalCriterion) {
        this.traversalCriterion = traversalCriterion;
    }
    public String getIsmultipleinstancesofdatacriterion() {
        return isMultipleInstancesOfDataCriterion;
    }

    public void setIsmultipleinstancesofdatacriterion(String isMultipleInstancesOfDataCriterion) {
        this.isMultipleInstancesOfDataCriterion = isMultipleInstancesOfDataCriterion;
    }
    public String getDataformatin() {
        return dataFormatIn;
    }

    public void setDataformatin(String dataFormatIn) {
        this.dataFormatIn = dataFormatIn;
    }
    public String getCardinalityout() {
        return cardinalityOut;
    }

    public void setCardinalityout(String cardinalityOut) {
        this.cardinalityOut = cardinalityOut;
    }
    public boolean getStatic() {
        return static;
    }

    public void setStatic(boolean static) {
        this.static = static;
    }
    public boolean getDepricated() {
        return depricated;
    }

    public void setDepricated(boolean depricated) {
        this.depricated = depricated;
    }
    public String getJexlstring() {
        return jexlString;
    }

    public void setJexlstring(String jexlString) {
        this.jexlString = jexlString;
    }
    public boolean getUtil() {
        return util;
    }

    public void setUtil(boolean util) {
        this.util = util;
    }
    public String getMergecriterion() {
        return mergeCriterion;
    }

    public void setMergecriterion(String mergeCriterion) {
        this.mergeCriterion = mergeCriterion;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getCardinalityin() {
        return cardinalityIn;
    }

    public void setCardinalityin(String cardinalityIn) {
        this.cardinalityIn = cardinalityIn;
    }
    public String getSplitcriterion() {
        return splitCriterion;
    }

    public void setSplitcriterion(String splitCriterion) {
        this.splitCriterion = splitCriterion;
    }
    public String getSkipgroupingcriterion() {
        return skipGroupingCriterion;
    }

    public void setSkipgroupingcriterion(String skipGroupingCriterion) {
        this.skipGroupingCriterion = skipGroupingCriterion;
    }
    public String getDatacriterion() {
        return dataCriterion;
    }

    public void setDatacriterion(String dataCriterion) {
        this.dataCriterion = dataCriterion;
    }

    public easyflow_DataFormatToTaskList getEasyflow_dataformattotasklist() {
        return easyflow_dataformattotasklist;
    }

    public void setEasyflow_dataformattotasklist(easyflow_DataFormatToTaskList easyflow_dataformattotasklist) {
        this.easyflow_dataformattotasklist = easyflow_dataformattotasklist;
    }
    public easyflow_TaskToDataProcessingType getEasyflow_tasktodataprocessingtype() {
        return easyflow_tasktodataprocessingtype;
    }

    public void setEasyflow_tasktodataprocessingtype(easyflow_TaskToDataProcessingType easyflow_tasktodataprocessingtype) {
        this.easyflow_tasktodataprocessingtype = easyflow_tasktodataprocessingtype;
    }
    public easyflow_TaskToDataProcessingType getEasyflow_tasktodataprocessingtype() {
        return easyflow_tasktodataprocessingtype;
    }

    public void setEasyflow_tasktodataprocessingtype(easyflow_TaskToDataProcessingType easyflow_tasktodataprocessingtype) {
        this.easyflow_tasktodataprocessingtype = easyflow_tasktodataprocessingtype;
    }
    public easyflow_DataProcessingTypeToTask getEasyflow_dataprocessingtypetotask() {
        return easyflow_dataprocessingtypetotask;
    }

    public void setEasyflow_dataprocessingtypetotask(easyflow_DataProcessingTypeToTask easyflow_dataprocessingtypetotask) {
        this.easyflow_dataprocessingtypetotask = easyflow_dataprocessingtypetotask;
    }

}