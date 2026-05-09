





import java.util.List;
import java.util.ArrayList;

public class uml3_0_0_ActivityNode extends RedefinableElement {






    private List<uml3_0_0_ActivityPartition> uml3_0_0_activitypartitions;




    private uml3_0_0_StructuredActivityNode uml3_0_0_structuredactivitynode;




    private List<uml3_0_0_ActivityEdge> uml3_0_0_activityedges;




    private uml3_0_0_ActivityEdge uml3_0_0_activityedge;




    private List<uml3_0_0_ActivityGroup> uml3_0_0_activitygroups;




    private uml3_0_0_ActivityPartition uml3_0_0_activitypartition;




    private List<uml3_0_0_ActivityEdge> uml3_0_0_activityedges;




    private uml3_0_0_ActivityEdge uml3_0_0_activityedge;




    private uml3_0_0_ActivityGroup uml3_0_0_activitygroup;




    private uml3_0_0_StructuredActivityNode uml3_0_0_structuredactivitynode;




    private List<uml3_0_0_ActivityNode> uml3_0_0_activitynodes;


    public uml3_0_0_ActivityNode(
    ) {
        super(
        );
        this.uml3_0_0_activitypartitions = new ArrayList<>();
        this.uml3_0_0_activityedges = new ArrayList<>();
        this.uml3_0_0_activitygroups = new ArrayList<>();
        this.uml3_0_0_activityedges = new ArrayList<>();
        this.uml3_0_0_activitynodes = new ArrayList<>();
    }

    public uml3_0_0_ActivityNode(
        ArrayList<uml3_0_0_ActivityPartition> uml3_0_0_activitypartitions,        ArrayList<uml3_0_0_ActivityEdge> uml3_0_0_activityedges,        ArrayList<uml3_0_0_ActivityGroup> uml3_0_0_activitygroups,        ArrayList<uml3_0_0_ActivityEdge> uml3_0_0_activityedges,        ArrayList<uml3_0_0_ActivityNode> uml3_0_0_activitynodes    ) {
        this.uml3_0_0_activitypartitions = uml3_0_0_activitypartitions;
        this.uml3_0_0_activityedges = uml3_0_0_activityedges;
        this.uml3_0_0_activitygroups = uml3_0_0_activitygroups;
        this.uml3_0_0_activityedges = uml3_0_0_activityedges;
        this.uml3_0_0_activitynodes = uml3_0_0_activitynodes;
    }


    public List<uml3_0_0_ActivityPartition> getUml3_0_0_activitypartitions() {
        return uml3_0_0_activitypartitions;
    }

    public void addUml3_0_0_activitypartition(Uml3_0_0_activitypartition uml3_0_0_activitypartition) {
        this.uml3_0_0_activitypartitions.add(uml3_0_0_activitypartition);
    }
    public uml3_0_0_StructuredActivityNode getUml3_0_0_structuredactivitynode() {
        return uml3_0_0_structuredactivitynode;
    }

    public void setUml3_0_0_structuredactivitynode(uml3_0_0_StructuredActivityNode uml3_0_0_structuredactivitynode) {
        this.uml3_0_0_structuredactivitynode = uml3_0_0_structuredactivitynode;
    }
    public List<uml3_0_0_ActivityEdge> getUml3_0_0_activityedges() {
        return uml3_0_0_activityedges;
    }

    public void addUml3_0_0_activityedge(Uml3_0_0_activityedge uml3_0_0_activityedge) {
        this.uml3_0_0_activityedges.add(uml3_0_0_activityedge);
    }
    public uml3_0_0_ActivityEdge getUml3_0_0_activityedge() {
        return uml3_0_0_activityedge;
    }

    public void setUml3_0_0_activityedge(uml3_0_0_ActivityEdge uml3_0_0_activityedge) {
        this.uml3_0_0_activityedge = uml3_0_0_activityedge;
    }
    public List<uml3_0_0_ActivityGroup> getUml3_0_0_activitygroups() {
        return uml3_0_0_activitygroups;
    }

    public void addUml3_0_0_activitygroup(Uml3_0_0_activitygroup uml3_0_0_activitygroup) {
        this.uml3_0_0_activitygroups.add(uml3_0_0_activitygroup);
    }
    public uml3_0_0_ActivityPartition getUml3_0_0_activitypartition() {
        return uml3_0_0_activitypartition;
    }

    public void setUml3_0_0_activitypartition(uml3_0_0_ActivityPartition uml3_0_0_activitypartition) {
        this.uml3_0_0_activitypartition = uml3_0_0_activitypartition;
    }
    public List<uml3_0_0_ActivityEdge> getUml3_0_0_activityedges() {
        return uml3_0_0_activityedges;
    }

    public void addUml3_0_0_activityedge(Uml3_0_0_activityedge uml3_0_0_activityedge) {
        this.uml3_0_0_activityedges.add(uml3_0_0_activityedge);
    }
    public uml3_0_0_ActivityEdge getUml3_0_0_activityedge() {
        return uml3_0_0_activityedge;
    }

    public void setUml3_0_0_activityedge(uml3_0_0_ActivityEdge uml3_0_0_activityedge) {
        this.uml3_0_0_activityedge = uml3_0_0_activityedge;
    }
    public uml3_0_0_ActivityGroup getUml3_0_0_activitygroup() {
        return uml3_0_0_activitygroup;
    }

    public void setUml3_0_0_activitygroup(uml3_0_0_ActivityGroup uml3_0_0_activitygroup) {
        this.uml3_0_0_activitygroup = uml3_0_0_activitygroup;
    }
    public uml3_0_0_StructuredActivityNode getUml3_0_0_structuredactivitynode() {
        return uml3_0_0_structuredactivitynode;
    }

    public void setUml3_0_0_structuredactivitynode(uml3_0_0_StructuredActivityNode uml3_0_0_structuredactivitynode) {
        this.uml3_0_0_structuredactivitynode = uml3_0_0_structuredactivitynode;
    }
    public List<uml3_0_0_ActivityNode> getUml3_0_0_activitynodes() {
        return uml3_0_0_activitynodes;
    }

    public void addUml3_0_0_activitynode(Uml3_0_0_activitynode uml3_0_0_activitynode) {
        this.uml3_0_0_activitynodes.add(uml3_0_0_activitynode);
    }

}