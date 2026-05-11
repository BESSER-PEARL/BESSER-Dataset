





import java.util.List;
import java.util.ArrayList;

public class workflow_CoreModel  {

    private String name;





    private workflow_Process workflow_process;




    private workflow_ModelRegistry workflow_modelregistry;




    private workflow_Process workflow_process;




    private workflow_RuntimeCoreModel workflow_runtimecoremodel;




    private workflow_ModelRegistry workflow_modelregistry;


    public workflow_CoreModel(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public workflow_Process getWorkflow_process() {
        return workflow_process;
    }

    public void setWorkflow_process(workflow_Process workflow_process) {
        this.workflow_process = workflow_process;
    }
    public workflow_ModelRegistry getWorkflow_modelregistry() {
        return workflow_modelregistry;
    }

    public void setWorkflow_modelregistry(workflow_ModelRegistry workflow_modelregistry) {
        this.workflow_modelregistry = workflow_modelregistry;
    }
    public workflow_Process getWorkflow_process() {
        return workflow_process;
    }

    public void setWorkflow_process(workflow_Process workflow_process) {
        this.workflow_process = workflow_process;
    }
    public workflow_RuntimeCoreModel getWorkflow_runtimecoremodel() {
        return workflow_runtimecoremodel;
    }

    public void setWorkflow_runtimecoremodel(workflow_RuntimeCoreModel workflow_runtimecoremodel) {
        this.workflow_runtimecoremodel = workflow_runtimecoremodel;
    }
    public workflow_ModelRegistry getWorkflow_modelregistry() {
        return workflow_modelregistry;
    }

    public void setWorkflow_modelregistry(workflow_ModelRegistry workflow_modelregistry) {
        this.workflow_modelregistry = workflow_modelregistry;
    }

}