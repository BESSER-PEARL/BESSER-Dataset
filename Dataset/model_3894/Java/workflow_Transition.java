





import java.util.List;
import java.util.ArrayList;

public class workflow_Transition extends TaskC {






    private workflow_Arc workflow_arc;




    private List<workflow_Arc> workflow_arcs;




    private List<workflow_Arc> workflow_arcs;




    private workflow_Arc workflow_arc;


    public workflow_Transition(
    ) {
        super(
        );
        this.workflow_arcs = new ArrayList<>();
        this.workflow_arcs = new ArrayList<>();
    }

    public workflow_Transition(
        ArrayList<workflow_Arc> workflow_arcs,        ArrayList<workflow_Arc> workflow_arcs    ) {
        this.workflow_arcs = workflow_arcs;
        this.workflow_arcs = workflow_arcs;
    }


    public workflow_Arc getWorkflow_arc() {
        return workflow_arc;
    }

    public void setWorkflow_arc(workflow_Arc workflow_arc) {
        this.workflow_arc = workflow_arc;
    }
    public List<workflow_Arc> getWorkflow_arcs() {
        return workflow_arcs;
    }

    public void addWorkflow_arc(Workflow_arc workflow_arc) {
        this.workflow_arcs.add(workflow_arc);
    }
    public List<workflow_Arc> getWorkflow_arcs() {
        return workflow_arcs;
    }

    public void addWorkflow_arc(Workflow_arc workflow_arc) {
        this.workflow_arcs.add(workflow_arc);
    }
    public workflow_Arc getWorkflow_arc() {
        return workflow_arc;
    }

    public void setWorkflow_arc(workflow_Arc workflow_arc) {
        this.workflow_arc = workflow_arc;
    }

}