





import java.util.List;
import java.util.ArrayList;

public class workflow_Statement  {

    private int exec_order;





    private workflow_Recipe workflow_recipe;


    public workflow_Statement(
        int exec_order    ) {
        this.exec_order = exec_order;
    }


    public int getExec_order() {
        return exec_order;
    }

    public void setExec_order(int exec_order) {
        this.exec_order = exec_order;
    }

    public workflow_Recipe getWorkflow_recipe() {
        return workflow_recipe;
    }

    public void setWorkflow_recipe(workflow_Recipe workflow_recipe) {
        this.workflow_recipe = workflow_recipe;
    }

}