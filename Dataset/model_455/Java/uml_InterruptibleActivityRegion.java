





import java.util.List;
import java.util.ArrayList;

public class uml_InterruptibleActivityRegion extends ActivityGroup {






    private List<uml_ActivityEdge> uml_activityedges;




    private List<uml_ActivityNode> uml_activitynodes;




    private uml_ActivityNode uml_activitynode;




    private uml_ActivityEdge uml_activityedge;


    public uml_InterruptibleActivityRegion(
    ) {
        super(
        );
        this.uml_activityedges = new ArrayList<>();
        this.uml_activitynodes = new ArrayList<>();
    }

    public uml_InterruptibleActivityRegion(
        ArrayList<uml_ActivityEdge> uml_activityedges,        ArrayList<uml_ActivityNode> uml_activitynodes    ) {
        this.uml_activityedges = uml_activityedges;
        this.uml_activitynodes = uml_activitynodes;
    }


    public List<uml_ActivityEdge> getUml_activityedges() {
        return uml_activityedges;
    }

    public void addUml_activityedge(Uml_activityedge uml_activityedge) {
        this.uml_activityedges.add(uml_activityedge);
    }
    public List<uml_ActivityNode> getUml_activitynodes() {
        return uml_activitynodes;
    }

    public void addUml_activitynode(Uml_activitynode uml_activitynode) {
        this.uml_activitynodes.add(uml_activitynode);
    }
    public uml_ActivityNode getUml_activitynode() {
        return uml_activitynode;
    }

    public void setUml_activitynode(uml_ActivityNode uml_activitynode) {
        this.uml_activitynode = uml_activitynode;
    }
    public uml_ActivityEdge getUml_activityedge() {
        return uml_activityedge;
    }

    public void setUml_activityedge(uml_ActivityEdge uml_activityedge) {
        this.uml_activityedge = uml_activityedge;
    }

}