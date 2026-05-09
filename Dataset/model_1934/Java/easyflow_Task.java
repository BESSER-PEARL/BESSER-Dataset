





import java.util.List;
import java.util.ArrayList;

public class easyflow_Task  {

    private String dataFormatIn;
    private boolean static;
    private String traversalCriterion;
    private String splitCriterion;
    private boolean contrast;
    private String jexlString;
    private String skipGroupingCriterion;
    private boolean depricated;
    private String dataCriterion;
    private String cardinalityIn;
    private String isMultipleInstancesOfDataCriterion;
    private String dataFormatOut;
    private boolean util;
    private String name;
    private String mergeCriterion;
    private String cardinalityOut;





    private easyflow_TaskToDataProcessingType easyflow_tasktodataprocessingtype;




    private easyflow_TaskToDataProcessingType easyflow_tasktodataprocessingtype;




    private easyflow_DataFormatToTaskList easyflow_dataformattotasklist;


    public easyflow_Task(
        String dataFormatIn,        boolean static,        String traversalCriterion,        String splitCriterion,        boolean contrast,        String jexlString,        String skipGroupingCriterion,        boolean depricated,        String dataCriterion,        String cardinalityIn,        String isMultipleInstancesOfDataCriterion,        String dataFormatOut,        boolean util,        String name,        String mergeCriterion,        String cardinalityOut    ) {
        this.dataFormatIn = dataFormatIn;
        this.static = static;
        this.traversalCriterion = traversalCriterion;
        this.splitCriterion = splitCriterion;
        this.contrast = contrast;
        this.jexlString = jexlString;
        this.skipGroupingCriterion = skipGroupingCriterion;
        this.depricated = depricated;
        this.dataCriterion = dataCriterion;
        this.cardinalityIn = cardinalityIn;
        this.isMultipleInstancesOfDataCriterion = isMultipleInstancesOfDataCriterion;
        this.dataFormatOut = dataFormatOut;
        this.util = util;
        this.name = name;
        this.mergeCriterion = mergeCriterion;
        this.cardinalityOut = cardinalityOut;
    }


    public String getDataformatin() {
        return dataFormatIn;
    }

    public void setDataformatin(String dataFormatIn) {
        this.dataFormatIn = dataFormatIn;
    }
    public boolean getStatic() {
        return static;
    }

    public void setStatic(boolean static) {
        this.static = static;
    }
    public String getTraversalcriterion() {
        return traversalCriterion;
    }

    public void setTraversalcriterion(String traversalCriterion) {
        this.traversalCriterion = traversalCriterion;
    }
    public String getSplitcriterion() {
        return splitCriterion;
    }

    public void setSplitcriterion(String splitCriterion) {
        this.splitCriterion = splitCriterion;
    }
    public boolean getContrast() {
        return contrast;
    }

    public void setContrast(boolean contrast) {
        this.contrast = contrast;
    }
    public String getJexlstring() {
        return jexlString;
    }

    public void setJexlstring(String jexlString) {
        this.jexlString = jexlString;
    }
    public String getSkipgroupingcriterion() {
        return skipGroupingCriterion;
    }

    public void setSkipgroupingcriterion(String skipGroupingCriterion) {
        this.skipGroupingCriterion = skipGroupingCriterion;
    }
    public boolean getDepricated() {
        return depricated;
    }

    public void setDepricated(boolean depricated) {
        this.depricated = depricated;
    }
    public String getDatacriterion() {
        return dataCriterion;
    }

    public void setDatacriterion(String dataCriterion) {
        this.dataCriterion = dataCriterion;
    }
    public String getCardinalityin() {
        return cardinalityIn;
    }

    public void setCardinalityin(String cardinalityIn) {
        this.cardinalityIn = cardinalityIn;
    }
    public String getIsmultipleinstancesofdatacriterion() {
        return isMultipleInstancesOfDataCriterion;
    }

    public void setIsmultipleinstancesofdatacriterion(String isMultipleInstancesOfDataCriterion) {
        this.isMultipleInstancesOfDataCriterion = isMultipleInstancesOfDataCriterion;
    }
    public String getDataformatout() {
        return dataFormatOut;
    }

    public void setDataformatout(String dataFormatOut) {
        this.dataFormatOut = dataFormatOut;
    }
    public boolean getUtil() {
        return util;
    }

    public void setUtil(boolean util) {
        this.util = util;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getMergecriterion() {
        return mergeCriterion;
    }

    public void setMergecriterion(String mergeCriterion) {
        this.mergeCriterion = mergeCriterion;
    }
    public String getCardinalityout() {
        return cardinalityOut;
    }

    public void setCardinalityout(String cardinalityOut) {
        this.cardinalityOut = cardinalityOut;
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
    public easyflow_DataFormatToTaskList getEasyflow_dataformattotasklist() {
        return easyflow_dataformattotasklist;
    }

    public void setEasyflow_dataformattotasklist(easyflow_DataFormatToTaskList easyflow_dataformattotasklist) {
        this.easyflow_dataformattotasklist = easyflow_dataformattotasklist;
    }

}