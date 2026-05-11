





import java.util.List;
import java.util.ArrayList;

public class workflow_WorkflowEngine  {






    private workflow_ModelRegistry workflow_modelregistry;




    private List<workflow_RuntimeCoreModel> workflow_runtimecoremodels;




    private workflow_ModelRegistry workflow_modelregistry;


    public workflow_WorkflowEngine(
    ) {
        this.workflow_runtimecoremodels = new ArrayList<>();
    }

    public workflow_WorkflowEngine(
        ArrayList<workflow_RuntimeCoreModel> workflow_runtimecoremodels    ) {
        this.workflow_runtimecoremodels = workflow_runtimecoremodels;
    }


    public workflow_ModelRegistry getWorkflow_modelregistry() {
        return workflow_modelregistry;
    }

    public void setWorkflow_modelregistry(workflow_ModelRegistry workflow_modelregistry) {
        this.workflow_modelregistry = workflow_modelregistry;
    }
    public List<workflow_RuntimeCoreModel> getWorkflow_runtimecoremodels() {
        return workflow_runtimecoremodels;
    }

    public void addWorkflow_runtimecoremodel(Workflow_runtimecoremodel workflow_runtimecoremodel) {
        this.workflow_runtimecoremodels.add(workflow_runtimecoremodel);
    }
    public workflow_ModelRegistry getWorkflow_modelregistry() {
        return workflow_modelregistry;
    }

    public void setWorkflow_modelregistry(workflow_ModelRegistry workflow_modelregistry) {
        this.workflow_modelregistry = workflow_modelregistry;
    }

}