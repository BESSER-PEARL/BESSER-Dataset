





import java.util.List;
import java.util.ArrayList;

public class workflow_Arc  {

    private String name;





    private workflow_PetriNet workflow_petrinet;


    public workflow_Arc(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public workflow_PetriNet getWorkflow_petrinet() {
        return workflow_petrinet;
    }

    public void setWorkflow_petrinet(workflow_PetriNet workflow_petrinet) {
        this.workflow_petrinet = workflow_petrinet;
    }

}