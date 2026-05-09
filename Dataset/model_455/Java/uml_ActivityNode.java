





import java.util.List;
import java.util.ArrayList;

public class uml_ActivityNode extends RedefinableElement {






    private List<uml_ActivityEdge> uml_activityedges;




    private uml_ActivityPartition uml_activitypartition;




    private uml_StructuredActivityNode uml_structuredactivitynode;




    private uml_ActivityEdge uml_activityedge;




    private List<uml_ActivityPartition> uml_activitypartitions;




    private uml_ActivityNode uml_activitynode;




    private List<uml_ActivityEdge> uml_activityedges;




    private uml_ActivityEdge uml_activityedge;




    private uml_ActivityGroup uml_activitygroup;




    private uml_StructuredActivityNode uml_structuredactivitynode;




    private List<uml_ActivityGroup> uml_activitygroups;


    public uml_ActivityNode(
    ) {
        super(
        );
        this.uml_activityedges = new ArrayList<>();
        this.uml_activitypartitions = new ArrayList<>();
        this.uml_activityedges = new ArrayList<>();
        this.uml_activitygroups = new ArrayList<>();
    }

    public uml_ActivityNode(
        ArrayList<uml_ActivityEdge> uml_activityedges,        ArrayList<uml_ActivityPartition> uml_activitypartitions,        ArrayList<uml_ActivityEdge> uml_activityedges,        ArrayList<uml_ActivityGroup> uml_activitygroups    ) {
        this.uml_activityedges = uml_activityedges;
        this.uml_activitypartitions = uml_activitypartitions;
        this.uml_activityedges = uml_activityedges;
        this.uml_activitygroups = uml_activitygroups;
    }


    public List<uml_ActivityEdge> getUml_activityedges() {
        return uml_activityedges;
    }

    public void addUml_activityedge(Uml_activityedge uml_activityedge) {
        this.uml_activityedges.add(uml_activityedge);
    }
    public uml_ActivityPartition getUml_activitypartition() {
        return uml_activitypartition;
    }

    public void setUml_activitypartition(uml_ActivityPartition uml_activitypartition) {
        this.uml_activitypartition = uml_activitypartition;
    }
    public uml_StructuredActivityNode getUml_structuredactivitynode() {
        return uml_structuredactivitynode;
    }

    public void setUml_structuredactivitynode(uml_StructuredActivityNode uml_structuredactivitynode) {
        this.uml_structuredactivitynode = uml_structuredactivitynode;
    }
    public uml_ActivityEdge getUml_activityedge() {
        return uml_activityedge;
    }

    public void setUml_activityedge(uml_ActivityEdge uml_activityedge) {
        this.uml_activityedge = uml_activityedge;
    }
    public List<uml_ActivityPartition> getUml_activitypartitions() {
        return uml_activitypartitions;
    }

    public void addUml_activitypartition(Uml_activitypartition uml_activitypartition) {
        this.uml_activitypartitions.add(uml_activitypartition);
    }
    public uml_ActivityNode getUml_activitynode() {
        return uml_activitynode;
    }

    public void setUml_activitynode(uml_ActivityNode uml_activitynode) {
        this.uml_activitynode = uml_activitynode;
    }
    public List<uml_ActivityEdge> getUml_activityedges() {
        return uml_activityedges;
    }

    public void addUml_activityedge(Uml_activityedge uml_activityedge) {
        this.uml_activityedges.add(uml_activityedge);
    }
    public uml_ActivityEdge getUml_activityedge() {
        return uml_activityedge;
    }

    public void setUml_activityedge(uml_ActivityEdge uml_activityedge) {
        this.uml_activityedge = uml_activityedge;
    }
    public uml_ActivityGroup getUml_activitygroup() {
        return uml_activitygroup;
    }

    public void setUml_activitygroup(uml_ActivityGroup uml_activitygroup) {
        this.uml_activitygroup = uml_activitygroup;
    }
    public uml_StructuredActivityNode getUml_structuredactivitynode() {
        return uml_structuredactivitynode;
    }

    public void setUml_structuredactivitynode(uml_StructuredActivityNode uml_structuredactivitynode) {
        this.uml_structuredactivitynode = uml_structuredactivitynode;
    }
    public List<uml_ActivityGroup> getUml_activitygroups() {
        return uml_activitygroups;
    }

    public void addUml_activitygroup(Uml_activitygroup uml_activitygroup) {
        this.uml_activitygroups.add(uml_activitygroup);
    }

}