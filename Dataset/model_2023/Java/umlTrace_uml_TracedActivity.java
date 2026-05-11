





import java.util.List;
import java.util.ArrayList;

public class umlTrace_uml_TracedActivity extends TracedBehavior {






    private List<uml_TracedActivityPartition> uml_tracedactivitypartitions;




    private List<uml_TracedActivityNode> uml_tracedactivitynodes;




    private List<uml_TracedVariable> uml_tracedvariables;




    private List<uml_TracedActivityNode> uml_tracedactivitynodes;




    private List<uml_TracedActivityEdge> uml_tracedactivityedges;




    private List<uml_TracedStructuredActivityNode> uml_tracedstructuredactivitynodes;


    public umlTrace_uml_TracedActivity(
    ) {
        super(
        );
        this.uml_tracedactivitypartitions = new ArrayList<>();
        this.uml_tracedactivitynodes = new ArrayList<>();
        this.uml_tracedvariables = new ArrayList<>();
        this.uml_tracedactivitynodes = new ArrayList<>();
        this.uml_tracedactivityedges = new ArrayList<>();
        this.uml_tracedstructuredactivitynodes = new ArrayList<>();
    }

    public umlTrace_uml_TracedActivity(
        ArrayList<uml_TracedActivityPartition> uml_tracedactivitypartitions,        ArrayList<uml_TracedActivityNode> uml_tracedactivitynodes,        ArrayList<uml_TracedVariable> uml_tracedvariables,        ArrayList<uml_TracedActivityNode> uml_tracedactivitynodes,        ArrayList<uml_TracedActivityEdge> uml_tracedactivityedges,        ArrayList<uml_TracedStructuredActivityNode> uml_tracedstructuredactivitynodes    ) {
        this.uml_tracedactivitypartitions = uml_tracedactivitypartitions;
        this.uml_tracedactivitynodes = uml_tracedactivitynodes;
        this.uml_tracedvariables = uml_tracedvariables;
        this.uml_tracedactivitynodes = uml_tracedactivitynodes;
        this.uml_tracedactivityedges = uml_tracedactivityedges;
        this.uml_tracedstructuredactivitynodes = uml_tracedstructuredactivitynodes;
    }


    public List<uml_TracedActivityPartition> getUml_tracedactivitypartitions() {
        return uml_tracedactivitypartitions;
    }

    public void addUml_tracedactivitypartition(Uml_tracedactivitypartition uml_tracedactivitypartition) {
        this.uml_tracedactivitypartitions.add(uml_tracedactivitypartition);
    }
    public List<uml_TracedActivityNode> getUml_tracedactivitynodes() {
        return uml_tracedactivitynodes;
    }

    public void addUml_tracedactivitynode(Uml_tracedactivitynode uml_tracedactivitynode) {
        this.uml_tracedactivitynodes.add(uml_tracedactivitynode);
    }
    public List<uml_TracedVariable> getUml_tracedvariables() {
        return uml_tracedvariables;
    }

    public void addUml_tracedvariable(Uml_tracedvariable uml_tracedvariable) {
        this.uml_tracedvariables.add(uml_tracedvariable);
    }
    public List<uml_TracedActivityNode> getUml_tracedactivitynodes() {
        return uml_tracedactivitynodes;
    }

    public void addUml_tracedactivitynode(Uml_tracedactivitynode uml_tracedactivitynode) {
        this.uml_tracedactivitynodes.add(uml_tracedactivitynode);
    }
    public List<uml_TracedActivityEdge> getUml_tracedactivityedges() {
        return uml_tracedactivityedges;
    }

    public void addUml_tracedactivityedge(Uml_tracedactivityedge uml_tracedactivityedge) {
        this.uml_tracedactivityedges.add(uml_tracedactivityedge);
    }
    public List<uml_TracedStructuredActivityNode> getUml_tracedstructuredactivitynodes() {
        return uml_tracedstructuredactivitynodes;
    }

    public void addUml_tracedstructuredactivitynode(Uml_tracedstructuredactivitynode uml_tracedstructuredactivitynode) {
        this.uml_tracedstructuredactivitynodes.add(uml_tracedstructuredactivitynode);
    }

}