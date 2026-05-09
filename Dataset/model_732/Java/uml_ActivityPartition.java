





import java.util.List;
import java.util.ArrayList;

public class uml_ActivityPartition extends ActivityGroup, NamedElement {






    private List<uml_ActivityNode> uml_activitynodes;




    private List<uml_ActivityEdge> uml_activityedges;


    public uml_ActivityPartition(
    ) {
        super(
        );
        this.uml_activitynodes = new ArrayList<>();
        this.uml_activityedges = new ArrayList<>();
    }

    public uml_ActivityPartition(
        ArrayList<uml_ActivityNode> uml_activitynodes,        ArrayList<uml_ActivityEdge> uml_activityedges    ) {
        this.uml_activitynodes = uml_activitynodes;
        this.uml_activityedges = uml_activityedges;
    }


    public List<uml_ActivityNode> getUml_activitynodes() {
        return uml_activitynodes;
    }

    public void addUml_activitynode(Uml_activitynode uml_activitynode) {
        this.uml_activitynodes.add(uml_activitynode);
    }
    public List<uml_ActivityEdge> getUml_activityedges() {
        return uml_activityedges;
    }

    public void addUml_activityedge(Uml_activityedge uml_activityedge) {
        this.uml_activityedges.add(uml_activityedge);
    }

}