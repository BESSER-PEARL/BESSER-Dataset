





import java.util.List;
import java.util.ArrayList;

public class workflow_TaskO extends TaskAspect {

    private String name;





    private workflow_TaskO workflow_tasko;


    public workflow_TaskO(
        String name    ) {
        super(
        );
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public workflow_TaskO getWorkflow_tasko() {
        return workflow_tasko;
    }

    public void setWorkflow_tasko(workflow_TaskO workflow_tasko) {
        this.workflow_tasko = workflow_tasko;
    }

}