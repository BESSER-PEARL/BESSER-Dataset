





import java.util.List;
import java.util.ArrayList;

public class uml3_0_0_ActivityEdge extends RedefinableElement {






    private uml3_0_0_ActivityEdge uml3_0_0_activityedge;




    private uml3_0_0_ActivityGroup uml3_0_0_activitygroup;




    private uml3_0_0_ValueSpecification uml3_0_0_valuespecification;




    private uml3_0_0_ActivityPartition uml3_0_0_activitypartition;




    private List<uml3_0_0_ActivityGroup> uml3_0_0_activitygroups;




    private uml3_0_0_ValueSpecification uml3_0_0_valuespecification;




    private uml3_0_0_InformationFlow uml3_0_0_informationflow;




    private uml3_0_0_StructuredActivityNode uml3_0_0_structuredactivitynode;




    private uml3_0_0_StructuredActivityNode uml3_0_0_structuredactivitynode;




    private List<uml3_0_0_ActivityPartition> uml3_0_0_activitypartitions;


    public uml3_0_0_ActivityEdge(
    ) {
        super(
        );
        this.uml3_0_0_activitygroups = new ArrayList<>();
        this.uml3_0_0_activitypartitions = new ArrayList<>();
    }

    public uml3_0_0_ActivityEdge(
        ArrayList<uml3_0_0_ActivityGroup> uml3_0_0_activitygroups,        ArrayList<uml3_0_0_ActivityPartition> uml3_0_0_activitypartitions    ) {
        this.uml3_0_0_activitygroups = uml3_0_0_activitygroups;
        this.uml3_0_0_activitypartitions = uml3_0_0_activitypartitions;
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
    public uml3_0_0_ValueSpecification getUml3_0_0_valuespecification() {
        return uml3_0_0_valuespecification;
    }

    public void setUml3_0_0_valuespecification(uml3_0_0_ValueSpecification uml3_0_0_valuespecification) {
        this.uml3_0_0_valuespecification = uml3_0_0_valuespecification;
    }
    public uml3_0_0_ActivityPartition getUml3_0_0_activitypartition() {
        return uml3_0_0_activitypartition;
    }

    public void setUml3_0_0_activitypartition(uml3_0_0_ActivityPartition uml3_0_0_activitypartition) {
        this.uml3_0_0_activitypartition = uml3_0_0_activitypartition;
    }
    public List<uml3_0_0_ActivityGroup> getUml3_0_0_activitygroups() {
        return uml3_0_0_activitygroups;
    }

    public void addUml3_0_0_activitygroup(Uml3_0_0_activitygroup uml3_0_0_activitygroup) {
        this.uml3_0_0_activitygroups.add(uml3_0_0_activitygroup);
    }
    public uml3_0_0_ValueSpecification getUml3_0_0_valuespecification() {
        return uml3_0_0_valuespecification;
    }

    public void setUml3_0_0_valuespecification(uml3_0_0_ValueSpecification uml3_0_0_valuespecification) {
        this.uml3_0_0_valuespecification = uml3_0_0_valuespecification;
    }
    public uml3_0_0_InformationFlow getUml3_0_0_informationflow() {
        return uml3_0_0_informationflow;
    }

    public void setUml3_0_0_informationflow(uml3_0_0_InformationFlow uml3_0_0_informationflow) {
        this.uml3_0_0_informationflow = uml3_0_0_informationflow;
    }
    public uml3_0_0_StructuredActivityNode getUml3_0_0_structuredactivitynode() {
        return uml3_0_0_structuredactivitynode;
    }

    public void setUml3_0_0_structuredactivitynode(uml3_0_0_StructuredActivityNode uml3_0_0_structuredactivitynode) {
        this.uml3_0_0_structuredactivitynode = uml3_0_0_structuredactivitynode;
    }
    public uml3_0_0_StructuredActivityNode getUml3_0_0_structuredactivitynode() {
        return uml3_0_0_structuredactivitynode;
    }

    public void setUml3_0_0_structuredactivitynode(uml3_0_0_StructuredActivityNode uml3_0_0_structuredactivitynode) {
        this.uml3_0_0_structuredactivitynode = uml3_0_0_structuredactivitynode;
    }
    public List<uml3_0_0_ActivityPartition> getUml3_0_0_activitypartitions() {
        return uml3_0_0_activitypartitions;
    }

    public void addUml3_0_0_activitypartition(Uml3_0_0_activitypartition uml3_0_0_activitypartition) {
        this.uml3_0_0_activitypartitions.add(uml3_0_0_activitypartition);
    }

}