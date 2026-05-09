





import java.util.List;
import java.util.ArrayList;

public class UML2_ActivityPartition extends ActivityGroup, NamedElement {

    private boolean isDimension;
    private boolean isExternal;





    private List<UML2_ActivityNode> uml2_activitynodes;




    private UML2_ActivityNode uml2_activitynode;




    private List<UML2_ActivityEdge> uml2_activityedges;




    private UML2_ActivityPartition uml2_activitypartition;




    private UML2_ActivityEdge uml2_activityedge;




    private UML2_ActivityPartition uml2_activitypartition;


    public UML2_ActivityPartition(
        boolean isDimension,        boolean isExternal    ) {
        super(
        );
        this.isDimension = isDimension;
        this.isExternal = isExternal;
        this.uml2_activitynodes = new ArrayList<>();
        this.uml2_activityedges = new ArrayList<>();
    }

    public UML2_ActivityPartition(
        boolean isDimension,        boolean isExternal        ArrayList<UML2_ActivityNode> uml2_activitynodes,        ArrayList<UML2_ActivityEdge> uml2_activityedges    ) {
        this.isDimension = isDimension;
        this.isExternal = isExternal;
        this.uml2_activitynodes = uml2_activitynodes;
        this.uml2_activityedges = uml2_activityedges;
    }

    public boolean getIsdimension() {
        return isDimension;
    }

    public void setIsdimension(boolean isDimension) {
        this.isDimension = isDimension;
    }
    public boolean getIsexternal() {
        return isExternal;
    }

    public void setIsexternal(boolean isExternal) {
        this.isExternal = isExternal;
    }

    public List<UML2_ActivityNode> getUml2_activitynodes() {
        return uml2_activitynodes;
    }

    public void addUml2_activitynode(Uml2_activitynode uml2_activitynode) {
        this.uml2_activitynodes.add(uml2_activitynode);
    }
    public UML2_ActivityNode getUml2_activitynode() {
        return uml2_activitynode;
    }

    public void setUml2_activitynode(UML2_ActivityNode uml2_activitynode) {
        this.uml2_activitynode = uml2_activitynode;
    }
    public List<UML2_ActivityEdge> getUml2_activityedges() {
        return uml2_activityedges;
    }

    public void addUml2_activityedge(Uml2_activityedge uml2_activityedge) {
        this.uml2_activityedges.add(uml2_activityedge);
    }
    public UML2_ActivityPartition getUml2_activitypartition() {
        return uml2_activitypartition;
    }

    public void setUml2_activitypartition(UML2_ActivityPartition uml2_activitypartition) {
        this.uml2_activitypartition = uml2_activitypartition;
    }
    public UML2_ActivityEdge getUml2_activityedge() {
        return uml2_activityedge;
    }

    public void setUml2_activityedge(UML2_ActivityEdge uml2_activityedge) {
        this.uml2_activityedge = uml2_activityedge;
    }
    public UML2_ActivityPartition getUml2_activitypartition() {
        return uml2_activitypartition;
    }

    public void setUml2_activitypartition(UML2_ActivityPartition uml2_activitypartition) {
        this.uml2_activitypartition = uml2_activitypartition;
    }

}