





import java.util.List;
import java.util.ArrayList;

public class workflow_Place  {

    private String name;





    private workflow_PetriNet workflow_petrinet;




    private workflow_Arc workflow_arc;




    private workflow_Arc workflow_arc;




    private List<workflow_Arc> workflow_arcs;




    private List<workflow_Arc> workflow_arcs;




    private workflow_PetriNet workflow_petrinet;




    private workflow_PetriNet workflow_petrinet;


    public workflow_Place(
        String name    ) {
        this.name = name;
        this.workflow_arcs = new ArrayList<>();
        this.workflow_arcs = new ArrayList<>();
    }

    public workflow_Place(
        String name        ArrayList<workflow_Arc> workflow_arcs,        ArrayList<workflow_Arc> workflow_arcs    ) {
        this.name = name;
        this.workflow_arcs = workflow_arcs;
        this.workflow_arcs = workflow_arcs;
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
    public workflow_Arc getWorkflow_arc() {
        return workflow_arc;
    }

    public void setWorkflow_arc(workflow_Arc workflow_arc) {
        this.workflow_arc = workflow_arc;
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
    public workflow_PetriNet getWorkflow_petrinet() {
        return workflow_petrinet;
    }

    public void setWorkflow_petrinet(workflow_PetriNet workflow_petrinet) {
        this.workflow_petrinet = workflow_petrinet;
    }
    public workflow_PetriNet getWorkflow_petrinet() {
        return workflow_petrinet;
    }

    public void setWorkflow_petrinet(workflow_PetriNet workflow_petrinet) {
        this.workflow_petrinet = workflow_petrinet;
    }

}