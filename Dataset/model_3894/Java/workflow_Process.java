





import java.util.List;
import java.util.ArrayList;

public class workflow_Process  {

    private String name;





    private workflow_Case workflow_case;


    public workflow_Process(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public workflow_Case getWorkflow_case() {
        return workflow_case;
    }

    public void setWorkflow_case(workflow_Case workflow_case) {
        this.workflow_case = workflow_case;
    }

}