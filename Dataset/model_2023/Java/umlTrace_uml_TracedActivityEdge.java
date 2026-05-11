





import java.util.List;
import java.util.ArrayList;

public class umlTrace_uml_TracedActivityEdge extends TracedRedefinableElement {






    private uml_TracedValueSpecification uml_tracedvaluespecification;




    private List<uml_TracedActivityEdge> uml_tracedactivityedges;




    private uml_TracedActivityNode uml_tracedactivitynode;




    private uml_TracedActivityNode uml_tracedactivitynode;




    private uml_TracedStructuredActivityNode uml_tracedstructuredactivitynode;




    private uml_TracedInterruptibleActivityRegion uml_tracedinterruptibleactivityregion;




    private List<uml_TracedActivityPartition> uml_tracedactivitypartitions;




    private uml_TracedValueSpecification uml_tracedvaluespecification;




    private uml_TracedActivity uml_tracedactivity;


    public umlTrace_uml_TracedActivityEdge(
    ) {
        super(
        );
        this.uml_tracedactivityedges = new ArrayList<>();
        this.uml_tracedactivitypartitions = new ArrayList<>();
    }

    public umlTrace_uml_TracedActivityEdge(
        ArrayList<uml_TracedActivityEdge> uml_tracedactivityedges,        ArrayList<uml_TracedActivityPartition> uml_tracedactivitypartitions    ) {
        this.uml_tracedactivityedges = uml_tracedactivityedges;
        this.uml_tracedactivitypartitions = uml_tracedactivitypartitions;
    }


    public uml_TracedValueSpecification getUml_tracedvaluespecification() {
        return uml_tracedvaluespecification;
    }

    public void setUml_tracedvaluespecification(uml_TracedValueSpecification uml_tracedvaluespecification) {
        this.uml_tracedvaluespecification = uml_tracedvaluespecification;
    }
    public List<uml_TracedActivityEdge> getUml_tracedactivityedges() {
        return uml_tracedactivityedges;
    }

    public void addUml_tracedactivityedge(Uml_tracedactivityedge uml_tracedactivityedge) {
        this.uml_tracedactivityedges.add(uml_tracedactivityedge);
    }
    public uml_TracedActivityNode getUml_tracedactivitynode() {
        return uml_tracedactivitynode;
    }

    public void setUml_tracedactivitynode(uml_TracedActivityNode uml_tracedactivitynode) {
        this.uml_tracedactivitynode = uml_tracedactivitynode;
    }
    public uml_TracedActivityNode getUml_tracedactivitynode() {
        return uml_tracedactivitynode;
    }

    public void setUml_tracedactivitynode(uml_TracedActivityNode uml_tracedactivitynode) {
        this.uml_tracedactivitynode = uml_tracedactivitynode;
    }
    public uml_TracedStructuredActivityNode getUml_tracedstructuredactivitynode() {
        return uml_tracedstructuredactivitynode;
    }

    public void setUml_tracedstructuredactivitynode(uml_TracedStructuredActivityNode uml_tracedstructuredactivitynode) {
        this.uml_tracedstructuredactivitynode = uml_tracedstructuredactivitynode;
    }
    public uml_TracedInterruptibleActivityRegion getUml_tracedinterruptibleactivityregion() {
        return uml_tracedinterruptibleactivityregion;
    }

    public void setUml_tracedinterruptibleactivityregion(uml_TracedInterruptibleActivityRegion uml_tracedinterruptibleactivityregion) {
        this.uml_tracedinterruptibleactivityregion = uml_tracedinterruptibleactivityregion;
    }
    public List<uml_TracedActivityPartition> getUml_tracedactivitypartitions() {
        return uml_tracedactivitypartitions;
    }

    public void addUml_tracedactivitypartition(Uml_tracedactivitypartition uml_tracedactivitypartition) {
        this.uml_tracedactivitypartitions.add(uml_tracedactivitypartition);
    }
    public uml_TracedValueSpecification getUml_tracedvaluespecification() {
        return uml_tracedvaluespecification;
    }

    public void setUml_tracedvaluespecification(uml_TracedValueSpecification uml_tracedvaluespecification) {
        this.uml_tracedvaluespecification = uml_tracedvaluespecification;
    }
    public uml_TracedActivity getUml_tracedactivity() {
        return uml_tracedactivity;
    }

    public void setUml_tracedactivity(uml_TracedActivity uml_tracedactivity) {
        this.uml_tracedactivity = uml_tracedactivity;
    }

}