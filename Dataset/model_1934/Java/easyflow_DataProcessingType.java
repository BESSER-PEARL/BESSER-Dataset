





import java.util.List;
import java.util.ArrayList;

public class easyflow_DataProcessingType  {

    private String dataFormatOut;
    private String dataFormatIn;





    private easyflow_TaskToDataProcessingType easyflow_tasktodataprocessingtype;




    private easyflow_Workflow easyflow_workflow;


    public easyflow_DataProcessingType(
        String dataFormatOut,        String dataFormatIn    ) {
        this.dataFormatOut = dataFormatOut;
        this.dataFormatIn = dataFormatIn;
    }


    public String getDataformatout() {
        return dataFormatOut;
    }

    public void setDataformatout(String dataFormatOut) {
        this.dataFormatOut = dataFormatOut;
    }
    public String getDataformatin() {
        return dataFormatIn;
    }

    public void setDataformatin(String dataFormatIn) {
        this.dataFormatIn = dataFormatIn;
    }

    public easyflow_TaskToDataProcessingType getEasyflow_tasktodataprocessingtype() {
        return easyflow_tasktodataprocessingtype;
    }

    public void setEasyflow_tasktodataprocessingtype(easyflow_TaskToDataProcessingType easyflow_tasktodataprocessingtype) {
        this.easyflow_tasktodataprocessingtype = easyflow_tasktodataprocessingtype;
    }
    public easyflow_Workflow getEasyflow_workflow() {
        return easyflow_workflow;
    }

    public void setEasyflow_workflow(easyflow_Workflow easyflow_workflow) {
        this.easyflow_workflow = easyflow_workflow;
    }

}