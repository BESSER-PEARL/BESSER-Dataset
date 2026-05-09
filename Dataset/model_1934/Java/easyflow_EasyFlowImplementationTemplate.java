





import java.util.List;
import java.util.ArrayList;

public class easyflow_EasyFlowImplementationTemplate  {

    private String jsonRootNode;
    private String fileName;
    private String parameterConfigMap;
    private String parameterConfigFileName;
    private String globalOptions;





    private easyflow_Workflow easyflow_workflow;


    public easyflow_EasyFlowImplementationTemplate(
        String jsonRootNode,        String fileName,        String parameterConfigMap,        String parameterConfigFileName,        String globalOptions    ) {
        this.jsonRootNode = jsonRootNode;
        this.fileName = fileName;
        this.parameterConfigMap = parameterConfigMap;
        this.parameterConfigFileName = parameterConfigFileName;
        this.globalOptions = globalOptions;
    }


    public String getJsonrootnode() {
        return jsonRootNode;
    }

    public void setJsonrootnode(String jsonRootNode) {
        this.jsonRootNode = jsonRootNode;
    }
    public String getFilename() {
        return fileName;
    }

    public void setFilename(String fileName) {
        this.fileName = fileName;
    }
    public String getParameterconfigmap() {
        return parameterConfigMap;
    }

    public void setParameterconfigmap(String parameterConfigMap) {
        this.parameterConfigMap = parameterConfigMap;
    }
    public String getParameterconfigfilename() {
        return parameterConfigFileName;
    }

    public void setParameterconfigfilename(String parameterConfigFileName) {
        this.parameterConfigFileName = parameterConfigFileName;
    }
    public String getGlobaloptions() {
        return globalOptions;
    }

    public void setGlobaloptions(String globalOptions) {
        this.globalOptions = globalOptions;
    }

    public easyflow_Workflow getEasyflow_workflow() {
        return easyflow_workflow;
    }

    public void setEasyflow_workflow(easyflow_Workflow easyflow_workflow) {
        this.easyflow_workflow = easyflow_workflow;
    }

}