





import java.util.List;
import java.util.ArrayList;

public class UML2WithID_InterruptibleActivityRegion extends ActivityGroup {






    private UML2WithID_ActivityNode uml2withid_activitynode;




    private List<UML2WithID_ActivityNode> uml2withid_activitynodes;




    private UML2WithID_ActivityEdge uml2withid_activityedge;




    private List<UML2WithID_ActivityEdge> uml2withid_activityedges;


    public UML2WithID_InterruptibleActivityRegion(
    ) {
        super(
        );
        this.uml2withid_activitynodes = new ArrayList<>();
        this.uml2withid_activityedges = new ArrayList<>();
    }

    public UML2WithID_InterruptibleActivityRegion(
        ArrayList<UML2WithID_ActivityNode> uml2withid_activitynodes,        ArrayList<UML2WithID_ActivityEdge> uml2withid_activityedges    ) {
        this.uml2withid_activitynodes = uml2withid_activitynodes;
        this.uml2withid_activityedges = uml2withid_activityedges;
    }


    public UML2WithID_ActivityNode getUml2withid_activitynode() {
        return uml2withid_activitynode;
    }

    public void setUml2withid_activitynode(UML2WithID_ActivityNode uml2withid_activitynode) {
        this.uml2withid_activitynode = uml2withid_activitynode;
    }
    public List<UML2WithID_ActivityNode> getUml2withid_activitynodes() {
        return uml2withid_activitynodes;
    }

    public void addUml2withid_activitynode(Uml2withid_activitynode uml2withid_activitynode) {
        this.uml2withid_activitynodes.add(uml2withid_activitynode);
    }
    public UML2WithID_ActivityEdge getUml2withid_activityedge() {
        return uml2withid_activityedge;
    }

    public void setUml2withid_activityedge(UML2WithID_ActivityEdge uml2withid_activityedge) {
        this.uml2withid_activityedge = uml2withid_activityedge;
    }
    public List<UML2WithID_ActivityEdge> getUml2withid_activityedges() {
        return uml2withid_activityedges;
    }

    public void addUml2withid_activityedge(Uml2withid_activityedge uml2withid_activityedge) {
        this.uml2withid_activityedges.add(uml2withid_activityedge);
    }

}