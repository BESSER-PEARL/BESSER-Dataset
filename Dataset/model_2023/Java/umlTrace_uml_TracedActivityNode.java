





import java.util.List;
import java.util.ArrayList;

public class umlTrace_uml_TracedActivityNode extends uml_TracedRedefinableElement, ActivityContent {






    private List<uml_TracedActivityEdge> uml_tracedactivityedges;




    private List<uml_TracedActivityEdge> uml_tracedactivityedges;




    private uml_TracedStructuredActivityNode uml_tracedstructuredactivitynode;




    private List<uml_TracedActivityPartition> uml_tracedactivitypartitions;




    private List<uml_TracedInterruptibleActivityRegion> uml_tracedinterruptibleactivityregions;




    private uml_TracedActivity uml_tracedactivity;




    private List<uml_TracedActivityNode> uml_tracedactivitynodes;


    public umlTrace_uml_TracedActivityNode(
    ) {
        super(
        );
        this.uml_tracedactivityedges = new ArrayList<>();
        this.uml_tracedactivityedges = new ArrayList<>();
        this.uml_tracedactivitypartitions = new ArrayList<>();
        this.uml_tracedinterruptibleactivityregions = new ArrayList<>();
        this.uml_tracedactivitynodes = new ArrayList<>();
    }

    public umlTrace_uml_TracedActivityNode(
        ArrayList<uml_TracedActivityEdge> uml_tracedactivityedges,        ArrayList<uml_TracedActivityEdge> uml_tracedactivityedges,        ArrayList<uml_TracedActivityPartition> uml_tracedactivitypartitions,        ArrayList<uml_TracedInterruptibleActivityRegion> uml_tracedinterruptibleactivityregions,        ArrayList<uml_TracedActivityNode> uml_tracedactivitynodes    ) {
        this.uml_tracedactivityedges = uml_tracedactivityedges;
        this.uml_tracedactivityedges = uml_tracedactivityedges;
        this.uml_tracedactivitypartitions = uml_tracedactivitypartitions;
        this.uml_tracedinterruptibleactivityregions = uml_tracedinterruptibleactivityregions;
        this.uml_tracedactivitynodes = uml_tracedactivitynodes;
    }


    public List<uml_TracedActivityEdge> getUml_tracedactivityedges() {
        return uml_tracedactivityedges;
    }

    public void addUml_tracedactivityedge(Uml_tracedactivityedge uml_tracedactivityedge) {
        this.uml_tracedactivityedges.add(uml_tracedactivityedge);
    }
    public List<uml_TracedActivityEdge> getUml_tracedactivityedges() {
        return uml_tracedactivityedges;
    }

    public void addUml_tracedactivityedge(Uml_tracedactivityedge uml_tracedactivityedge) {
        this.uml_tracedactivityedges.add(uml_tracedactivityedge);
    }
    public uml_TracedStructuredActivityNode getUml_tracedstructuredactivitynode() {
        return uml_tracedstructuredactivitynode;
    }

    public void setUml_tracedstructuredactivitynode(uml_TracedStructuredActivityNode uml_tracedstructuredactivitynode) {
        this.uml_tracedstructuredactivitynode = uml_tracedstructuredactivitynode;
    }
    public List<uml_TracedActivityPartition> getUml_tracedactivitypartitions() {
        return uml_tracedactivitypartitions;
    }

    public void addUml_tracedactivitypartition(Uml_tracedactivitypartition uml_tracedactivitypartition) {
        this.uml_tracedactivitypartitions.add(uml_tracedactivitypartition);
    }
    public List<uml_TracedInterruptibleActivityRegion> getUml_tracedinterruptibleactivityregions() {
        return uml_tracedinterruptibleactivityregions;
    }

    public void addUml_tracedinterruptibleactivityregion(Uml_tracedinterruptibleactivityregion uml_tracedinterruptibleactivityregion) {
        this.uml_tracedinterruptibleactivityregions.add(uml_tracedinterruptibleactivityregion);
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

}