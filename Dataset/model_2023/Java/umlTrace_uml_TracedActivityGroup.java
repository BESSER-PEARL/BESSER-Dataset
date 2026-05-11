





import java.util.List;
import java.util.ArrayList;

public class umlTrace_uml_TracedActivityGroup extends uml_TracedNamedElement, ActivityContent {






    private uml_TracedActivity uml_tracedactivity;




    private List<uml_TracedActivityNode> uml_tracedactivitynodes;




    private List<uml_TracedActivityEdge> uml_tracedactivityedges;


    public umlTrace_uml_TracedActivityGroup(
    ) {
        super(
        );
        this.uml_tracedactivitynodes = new ArrayList<>();
        this.uml_tracedactivityedges = new ArrayList<>();
    }

    public umlTrace_uml_TracedActivityGroup(
        ArrayList<uml_TracedActivityNode> uml_tracedactivitynodes,        ArrayList<uml_TracedActivityEdge> uml_tracedactivityedges    ) {
        this.uml_tracedactivitynodes = uml_tracedactivitynodes;
        this.uml_tracedactivityedges = uml_tracedactivityedges;
    }


    public uml_TracedActivity getUml_tracedactivity() {
        return uml_tracedactivity;
    }

    public void setUml_tracedactivity(uml_TracedActivity uml_tracedactivity) {
        this.uml_tracedactivity = uml_tracedactivity;
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

}