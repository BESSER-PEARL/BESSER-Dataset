





import java.util.List;
import java.util.ArrayList;

public class UML2WithID_ActivityPartition extends NamedElement, ActivityGroup {

    private boolean isDimension;
    private boolean isExternal;





    private List<UML2WithID_ActivityPartition> uml2withid_activitypartitions;




    private UML2WithID_ActivityEdge uml2withid_activityedge;




    private List<UML2WithID_ActivityNode> uml2withid_activitynodes;




    private UML2WithID_ActivityNode uml2withid_activitynode;




    private UML2WithID_ActivityPartition uml2withid_activitypartition;




    private List<UML2WithID_ActivityEdge> uml2withid_activityedges;


    public UML2WithID_ActivityPartition(
        boolean isDimension,        boolean isExternal    ) {
        super(
        );
        this.isDimension = isDimension;
        this.isExternal = isExternal;
        this.uml2withid_activitypartitions = new ArrayList<>();
        this.uml2withid_activitynodes = new ArrayList<>();
        this.uml2withid_activityedges = new ArrayList<>();
    }

    public UML2WithID_ActivityPartition(
        boolean isDimension,        boolean isExternal        ArrayList<UML2WithID_ActivityPartition> uml2withid_activitypartitions,        ArrayList<UML2WithID_ActivityNode> uml2withid_activitynodes,        ArrayList<UML2WithID_ActivityEdge> uml2withid_activityedges    ) {
        this.isDimension = isDimension;
        this.isExternal = isExternal;
        this.uml2withid_activitypartitions = uml2withid_activitypartitions;
        this.uml2withid_activitynodes = uml2withid_activitynodes;
        this.uml2withid_activityedges = uml2withid_activityedges;
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

    public List<UML2WithID_ActivityPartition> getUml2withid_activitypartitions() {
        return uml2withid_activitypartitions;
    }

    public void addUml2withid_activitypartition(Uml2withid_activitypartition uml2withid_activitypartition) {
        this.uml2withid_activitypartitions.add(uml2withid_activitypartition);
    }
    public UML2WithID_ActivityEdge getUml2withid_activityedge() {
        return uml2withid_activityedge;
    }

    public void setUml2withid_activityedge(UML2WithID_ActivityEdge uml2withid_activityedge) {
        this.uml2withid_activityedge = uml2withid_activityedge;
    }
    public List<UML2WithID_ActivityNode> getUml2withid_activitynodes() {
        return uml2withid_activitynodes;
    }

    public void addUml2withid_activitynode(Uml2withid_activitynode uml2withid_activitynode) {
        this.uml2withid_activitynodes.add(uml2withid_activitynode);
    }
    public UML2WithID_ActivityNode getUml2withid_activitynode() {
        return uml2withid_activitynode;
    }

    public void setUml2withid_activitynode(UML2WithID_ActivityNode uml2withid_activitynode) {
        this.uml2withid_activitynode = uml2withid_activitynode;
    }
    public UML2WithID_ActivityPartition getUml2withid_activitypartition() {
        return uml2withid_activitypartition;
    }

    public void setUml2withid_activitypartition(UML2WithID_ActivityPartition uml2withid_activitypartition) {
        this.uml2withid_activitypartition = uml2withid_activitypartition;
    }
    public List<UML2WithID_ActivityEdge> getUml2withid_activityedges() {
        return uml2withid_activityedges;
    }

    public void addUml2withid_activityedge(Uml2withid_activityedge uml2withid_activityedge) {
        this.uml2withid_activityedges.add(uml2withid_activityedge);
    }

}