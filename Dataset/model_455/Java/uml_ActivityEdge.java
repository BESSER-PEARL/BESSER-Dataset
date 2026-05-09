





import java.util.List;
import java.util.ArrayList;

public class uml_ActivityEdge extends RedefinableElement {






    private uml_ActivityGroup uml_activitygroup;




    private uml_ValueSpecification uml_valuespecification;




    private uml_InformationFlow uml_informationflow;




    private List<uml_ActivityPartition> uml_activitypartitions;




    private uml_StructuredActivityNode uml_structuredactivitynode;




    private uml_ValueSpecification uml_valuespecification;




    private List<uml_ActivityEdge> uml_activityedges;




    private List<uml_ActivityGroup> uml_activitygroups;




    private uml_ActivityPartition uml_activitypartition;




    private uml_StructuredActivityNode uml_structuredactivitynode;


    public uml_ActivityEdge(
    ) {
        super(
        );
        this.uml_activitypartitions = new ArrayList<>();
        this.uml_activityedges = new ArrayList<>();
        this.uml_activitygroups = new ArrayList<>();
    }

    public uml_ActivityEdge(
        ArrayList<uml_ActivityPartition> uml_activitypartitions,        ArrayList<uml_ActivityEdge> uml_activityedges,        ArrayList<uml_ActivityGroup> uml_activitygroups    ) {
        this.uml_activitypartitions = uml_activitypartitions;
        this.uml_activityedges = uml_activityedges;
        this.uml_activitygroups = uml_activitygroups;
    }


    public uml_ActivityGroup getUml_activitygroup() {
        return uml_activitygroup;
    }

    public void setUml_activitygroup(uml_ActivityGroup uml_activitygroup) {
        this.uml_activitygroup = uml_activitygroup;
    }
    public uml_ValueSpecification getUml_valuespecification() {
        return uml_valuespecification;
    }

    public void setUml_valuespecification(uml_ValueSpecification uml_valuespecification) {
        this.uml_valuespecification = uml_valuespecification;
    }
    public uml_InformationFlow getUml_informationflow() {
        return uml_informationflow;
    }

    public void setUml_informationflow(uml_InformationFlow uml_informationflow) {
        this.uml_informationflow = uml_informationflow;
    }
    public List<uml_ActivityPartition> getUml_activitypartitions() {
        return uml_activitypartitions;
    }

    public void addUml_activitypartition(Uml_activitypartition uml_activitypartition) {
        this.uml_activitypartitions.add(uml_activitypartition);
    }
    public uml_StructuredActivityNode getUml_structuredactivitynode() {
        return uml_structuredactivitynode;
    }

    public void setUml_structuredactivitynode(uml_StructuredActivityNode uml_structuredactivitynode) {
        this.uml_structuredactivitynode = uml_structuredactivitynode;
    }
    public uml_ValueSpecification getUml_valuespecification() {
        return uml_valuespecification;
    }

    public void setUml_valuespecification(uml_ValueSpecification uml_valuespecification) {
        this.uml_valuespecification = uml_valuespecification;
    }
    public List<uml_ActivityEdge> getUml_activityedges() {
        return uml_activityedges;
    }

    public void addUml_activityedge(Uml_activityedge uml_activityedge) {
        this.uml_activityedges.add(uml_activityedge);
    }
    public List<uml_ActivityGroup> getUml_activitygroups() {
        return uml_activitygroups;
    }

    public void addUml_activitygroup(Uml_activitygroup uml_activitygroup) {
        this.uml_activitygroups.add(uml_activitygroup);
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

}