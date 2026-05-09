





import java.util.List;
import java.util.ArrayList;

public class easyflow_EasyFlowConfiguration  {

    private String fileName;
    private String configMap;





    private easyflow_Workflow easyflow_workflow;


    public easyflow_EasyFlowConfiguration(
        String fileName,        String configMap    ) {
        this.fileName = fileName;
        this.configMap = configMap;
    }


    public String getFilename() {
        return fileName;
    }

    public void setFilename(String fileName) {
        this.fileName = fileName;
    }
    public String getConfigmap() {
        return configMap;
    }

    public void setConfigmap(String configMap) {
        this.configMap = configMap;
    }

    public easyflow_Workflow getEasyflow_workflow() {
        return easyflow_workflow;
    }

    public void setEasyflow_workflow(easyflow_Workflow easyflow_workflow) {
        this.easyflow_workflow = easyflow_workflow;
    }

}