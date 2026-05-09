





import java.util.List;
import java.util.ArrayList;

public class easyflow_EasyFlowImplementationTemplate  {

    private String globalOptions;
    private String parameterConfigMap;
    private String fileName;
    private String parameterConfigFileName;
    private String jsonRootNode;





    private easyflow_Workflow easyflow_workflow;


    public easyflow_EasyFlowImplementationTemplate(
        String globalOptions,        String parameterConfigMap,        String fileName,        String parameterConfigFileName,        String jsonRootNode    ) {
        this.globalOptions = globalOptions;
        this.parameterConfigMap = parameterConfigMap;
        this.fileName = fileName;
        this.parameterConfigFileName = parameterConfigFileName;
        this.jsonRootNode = jsonRootNode;
    }


    public String getGlobaloptions() {
        return globalOptions;
    }

    public void setGlobaloptions(String globalOptions) {
        this.globalOptions = globalOptions;
    }
    public String getParameterconfigmap() {
        return parameterConfigMap;
    }

    public void setParameterconfigmap(String parameterConfigMap) {
        this.parameterConfigMap = parameterConfigMap;
    }
    public String getFilename() {
        return fileName;
    }

    public void setFilename(String fileName) {
        this.fileName = fileName;
    }
    public String getParameterconfigfilename() {
        return parameterConfigFileName;
    }

    public void setParameterconfigfilename(String parameterConfigFileName) {
        this.parameterConfigFileName = parameterConfigFileName;
    }
    public String getJsonrootnode() {
        return jsonRootNode;
    }

    public void setJsonrootnode(String jsonRootNode) {
        this.jsonRootNode = jsonRootNode;
    }

    public easyflow_Workflow getEasyflow_workflow() {
        return easyflow_workflow;
    }

    public void setEasyflow_workflow(easyflow_Workflow easyflow_workflow) {
        this.easyflow_workflow = easyflow_workflow;
    }

}