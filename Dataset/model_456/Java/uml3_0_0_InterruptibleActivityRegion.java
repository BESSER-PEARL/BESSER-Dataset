





import java.util.List;
import java.util.ArrayList;

public class uml3_0_0_InterruptibleActivityRegion extends ActivityGroup {






    private uml3_0_0_ActivityEdge uml3_0_0_activityedge;




    private List<uml3_0_0_ActivityEdge> uml3_0_0_activityedges;




    private uml3_0_0_ActivityNode uml3_0_0_activitynode;




    private List<uml3_0_0_ActivityNode> uml3_0_0_activitynodes;


    public uml3_0_0_InterruptibleActivityRegion(
    ) {
        super(
        );
        this.uml3_0_0_activityedges = new ArrayList<>();
        this.uml3_0_0_activitynodes = new ArrayList<>();
    }

    public uml3_0_0_InterruptibleActivityRegion(
        ArrayList<uml3_0_0_ActivityEdge> uml3_0_0_activityedges,        ArrayList<uml3_0_0_ActivityNode> uml3_0_0_activitynodes    ) {
        this.uml3_0_0_activityedges = uml3_0_0_activityedges;
        this.uml3_0_0_activitynodes = uml3_0_0_activitynodes;
    }


    public uml3_0_0_ActivityEdge getUml3_0_0_activityedge() {
        return uml3_0_0_activityedge;
    }

    public void setUml3_0_0_activityedge(uml3_0_0_ActivityEdge uml3_0_0_activityedge) {
        this.uml3_0_0_activityedge = uml3_0_0_activityedge;
    }
    public List<uml3_0_0_ActivityEdge> getUml3_0_0_activityedges() {
        return uml3_0_0_activityedges;
    }

    public void addUml3_0_0_activityedge(Uml3_0_0_activityedge uml3_0_0_activityedge) {
        this.uml3_0_0_activityedges.add(uml3_0_0_activityedge);
    }
    public uml3_0_0_ActivityNode getUml3_0_0_activitynode() {
        return uml3_0_0_activitynode;
    }

    public void setUml3_0_0_activitynode(uml3_0_0_ActivityNode uml3_0_0_activitynode) {
        this.uml3_0_0_activitynode = uml3_0_0_activitynode;
    }
    public List<uml3_0_0_ActivityNode> getUml3_0_0_activitynodes() {
        return uml3_0_0_activitynodes;
    }

    public void addUml3_0_0_activitynode(Uml3_0_0_activitynode uml3_0_0_activitynode) {
        this.uml3_0_0_activitynodes.add(uml3_0_0_activitynode);
    }

}