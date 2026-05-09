





import java.util.List;
import java.util.ArrayList;

public class easyflow_EasyFlowConfiguration  {

    private String configMap;
    private String fileName;





    private easyflow_Workflow easyflow_workflow;


    public easyflow_EasyFlowConfiguration(
        String configMap,        String fileName    ) {
        this.configMap = configMap;
        this.fileName = fileName;
    }


    public String getConfigmap() {
        return configMap;
    }

    public void setConfigmap(String configMap) {
        this.configMap = configMap;
    }
    public String getFilename() {
        return fileName;
    }

    public void setFilename(String fileName) {
        this.fileName = fileName;
    }

    public easyflow_Workflow getEasyflow_workflow() {
        return easyflow_workflow;
    }

    public void setEasyflow_workflow(easyflow_Workflow easyflow_workflow) {
        this.easyflow_workflow = easyflow_workflow;
    }

}