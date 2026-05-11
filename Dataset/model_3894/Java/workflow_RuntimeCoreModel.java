





import java.util.List;
import java.util.ArrayList;

public class workflow_RuntimeCoreModel  {






    private workflow_Case workflow_case;




    private List<workflow_Case> workflow_cases;


    public workflow_RuntimeCoreModel(
    ) {
        this.workflow_cases = new ArrayList<>();
    }

    public workflow_RuntimeCoreModel(
        ArrayList<workflow_Case> workflow_cases    ) {
        this.workflow_cases = workflow_cases;
    }


    public workflow_Case getWorkflow_case() {
        return workflow_case;
    }

    public void setWorkflow_case(workflow_Case workflow_case) {
        this.workflow_case = workflow_case;
    }
    public List<workflow_Case> getWorkflow_cases() {
        return workflow_cases;
    }

    public void addWorkflow_case(Workflow_case workflow_case) {
        this.workflow_cases.add(workflow_case);
    }

}