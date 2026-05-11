





import java.util.List;
import java.util.ArrayList;

public class umlTrace_uml_TracedActivityPartition extends TracedActivityGroup {






    private List<uml_TracedActivityNode> uml_tracedactivitynodes;




    private List<uml_TracedActivityEdge> uml_tracedactivityedges;




    private uml_TracedActivityPartition uml_tracedactivitypartition;




    private List<uml_TracedActivityPartition> uml_tracedactivitypartitions;




    private uml_TracedElement uml_tracedelement;


    public umlTrace_uml_TracedActivityPartition(
    ) {
        super(
        );
        this.uml_tracedactivitynodes = new ArrayList<>();
        this.uml_tracedactivityedges = new ArrayList<>();
        this.uml_tracedactivitypartitions = new ArrayList<>();
    }

    public umlTrace_uml_TracedActivityPartition(
        ArrayList<uml_TracedActivityNode> uml_tracedactivitynodes,        ArrayList<uml_TracedActivityEdge> uml_tracedactivityedges,        ArrayList<uml_TracedActivityPartition> uml_tracedactivitypartitions    ) {
        this.uml_tracedactivitynodes = uml_tracedactivitynodes;
        this.uml_tracedactivityedges = uml_tracedactivityedges;
        this.uml_tracedactivitypartitions = uml_tracedactivitypartitions;
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
    public uml_TracedActivityPartition getUml_tracedactivitypartition() {
        return uml_tracedactivitypartition;
    }

    public void setUml_tracedactivitypartition(uml_TracedActivityPartition uml_tracedactivitypartition) {
        this.uml_tracedactivitypartition = uml_tracedactivitypartition;
    }
    public List<uml_TracedActivityPartition> getUml_tracedactivitypartitions() {
        return uml_tracedactivitypartitions;
    }

    public void addUml_tracedactivitypartition(Uml_tracedactivitypartition uml_tracedactivitypartition) {
        this.uml_tracedactivitypartitions.add(uml_tracedactivitypartition);
    }
    public uml_TracedElement getUml_tracedelement() {
        return uml_tracedelement;
    }

    public void setUml_tracedelement(uml_TracedElement uml_tracedelement) {
        this.uml_tracedelement = uml_tracedelement;
    }

}