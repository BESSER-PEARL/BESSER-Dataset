





import java.util.List;
import java.util.ArrayList;

public class easyflow_DataFormatToTaskList  {

    private String key;





    private easyflow_Workflow easyflow_workflow;


    public easyflow_DataFormatToTaskList(
        String key    ) {
        this.key = key;
    }


    public String getKey() {
        return key;
    }

    public void setKey(String key) {
        this.key = key;
    }

    public easyflow_Workflow getEasyflow_workflow() {
        return easyflow_workflow;
    }

    public void setEasyflow_workflow(easyflow_Workflow easyflow_workflow) {
        this.easyflow_workflow = easyflow_workflow;
    }

}