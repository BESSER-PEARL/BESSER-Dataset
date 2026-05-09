





import java.util.List;
import java.util.ArrayList;

public class UML2_InterruptibleActivityRegion extends ActivityGroup {






    private UML2_ActivityNode uml2_activitynode;




    private UML2_ActivityEdge uml2_activityedge;




    private List<UML2_ActivityEdge> uml2_activityedges;




    private List<UML2_ActivityNode> uml2_activitynodes;


    public UML2_InterruptibleActivityRegion(
    ) {
        super(
        );
        this.uml2_activityedges = new ArrayList<>();
        this.uml2_activitynodes = new ArrayList<>();
    }

    public UML2_InterruptibleActivityRegion(
        ArrayList<UML2_ActivityEdge> uml2_activityedges,        ArrayList<UML2_ActivityNode> uml2_activitynodes    ) {
        this.uml2_activityedges = uml2_activityedges;
        this.uml2_activitynodes = uml2_activitynodes;
    }


    public UML2_ActivityNode getUml2_activitynode() {
        return uml2_activitynode;
    }

    public void setUml2_activitynode(UML2_ActivityNode uml2_activitynode) {
        this.uml2_activitynode = uml2_activitynode;
    }
    public UML2_ActivityEdge getUml2_activityedge() {
        return uml2_activityedge;
    }

    public void setUml2_activityedge(UML2_ActivityEdge uml2_activityedge) {
        this.uml2_activityedge = uml2_activityedge;
    }
    public List<UML2_ActivityEdge> getUml2_activityedges() {
        return uml2_activityedges;
    }

    public void addUml2_activityedge(Uml2_activityedge uml2_activityedge) {
        this.uml2_activityedges.add(uml2_activityedge);
    }
    public List<UML2_ActivityNode> getUml2_activitynodes() {
        return uml2_activitynodes;
    }

    public void addUml2_activitynode(Uml2_activitynode uml2_activitynode) {
        this.uml2_activitynodes.add(uml2_activitynode);
    }

}