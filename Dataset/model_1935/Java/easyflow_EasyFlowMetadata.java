





import java.util.List;
import java.util.ArrayList;

public class easyflow_EasyFlowMetadata  {

    private String name;
    private String refData;
    private boolean contrast;





    private easyflow_Workflow easyflow_workflow;


    public easyflow_EasyFlowMetadata(
        String name,        String refData,        boolean contrast    ) {
        this.name = name;
        this.refData = refData;
        this.contrast = contrast;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getRefdata() {
        return refData;
    }

    public void setRefdata(String refData) {
        this.refData = refData;
    }
    public boolean getContrast() {
        return contrast;
    }

    public void setContrast(boolean contrast) {
        this.contrast = contrast;
    }

    public easyflow_Workflow getEasyflow_workflow() {
        return easyflow_workflow;
    }

    public void setEasyflow_workflow(easyflow_Workflow easyflow_workflow) {
        this.easyflow_workflow = easyflow_workflow;
    }

}