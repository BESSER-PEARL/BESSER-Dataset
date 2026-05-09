





import java.util.List;
import java.util.ArrayList;

public class UML2WithID_ActivityEdge extends RedefinableElement {






    private List<UML2WithID_ActivityGroup> uml2withid_activitygroups;




    private UML2WithID_Activity uml2withid_activity;




    private UML2WithID_ValueSpecification uml2withid_valuespecification;




    private UML2WithID_StructuredActivityNode uml2withid_structuredactivitynode;




    private UML2WithID_StructuredActivityNode uml2withid_structuredactivitynode;




    private List<UML2WithID_ActivityEdge> uml2withid_activityedges;




    private List<UML2WithID_ActivityPartition> uml2withid_activitypartitions;




    private UML2WithID_Activity uml2withid_activity;




    private UML2WithID_ActivityPartition uml2withid_activitypartition;




    private UML2WithID_ValueSpecification uml2withid_valuespecification;


    public UML2WithID_ActivityEdge(
    ) {
        super(
        );
        this.uml2withid_activitygroups = new ArrayList<>();
        this.uml2withid_activityedges = new ArrayList<>();
        this.uml2withid_activitypartitions = new ArrayList<>();
    }

    public UML2WithID_ActivityEdge(
        ArrayList<UML2WithID_ActivityGroup> uml2withid_activitygroups,        ArrayList<UML2WithID_ActivityEdge> uml2withid_activityedges,        ArrayList<UML2WithID_ActivityPartition> uml2withid_activitypartitions    ) {
        this.uml2withid_activitygroups = uml2withid_activitygroups;
        this.uml2withid_activityedges = uml2withid_activityedges;
        this.uml2withid_activitypartitions = uml2withid_activitypartitions;
    }


    public List<UML2WithID_ActivityGroup> getUml2withid_activitygroups() {
        return uml2withid_activitygroups;
    }

    public void addUml2withid_activitygroup(Uml2withid_activitygroup uml2withid_activitygroup) {
        this.uml2withid_activitygroups.add(uml2withid_activitygroup);
    }
    public UML2WithID_Activity getUml2withid_activity() {
        return uml2withid_activity;
    }

    public void setUml2withid_activity(UML2WithID_Activity uml2withid_activity) {
        this.uml2withid_activity = uml2withid_activity;
    }
    public UML2WithID_ValueSpecification getUml2withid_valuespecification() {
        return uml2withid_valuespecification;
    }

    public void setUml2withid_valuespecification(UML2WithID_ValueSpecification uml2withid_valuespecification) {
        this.uml2withid_valuespecification = uml2withid_valuespecification;
    }
    public UML2WithID_StructuredActivityNode getUml2withid_structuredactivitynode() {
        return uml2withid_structuredactivitynode;
    }

    public void setUml2withid_structuredactivitynode(UML2WithID_StructuredActivityNode uml2withid_structuredactivitynode) {
        this.uml2withid_structuredactivitynode = uml2withid_structuredactivitynode;
    }
    public UML2WithID_StructuredActivityNode getUml2withid_structuredactivitynode() {
        return uml2withid_structuredactivitynode;
    }

    public void setUml2withid_structuredactivitynode(UML2WithID_StructuredActivityNode uml2withid_structuredactivitynode) {
        this.uml2withid_structuredactivitynode = uml2withid_structuredactivitynode;
    }
    public List<UML2WithID_ActivityEdge> getUml2withid_activityedges() {
        return uml2withid_activityedges;
    }

    public void addUml2withid_activityedge(Uml2withid_activityedge uml2withid_activityedge) {
        this.uml2withid_activityedges.add(uml2withid_activityedge);
    }
    public List<UML2WithID_ActivityPartition> getUml2withid_activitypartitions() {
        return uml2withid_activitypartitions;
    }

    public void addUml2withid_activitypartition(Uml2withid_activitypartition uml2withid_activitypartition) {
        this.uml2withid_activitypartitions.add(uml2withid_activitypartition);
    }
    public UML2WithID_Activity getUml2withid_activity() {
        return uml2withid_activity;
    }

    public void setUml2withid_activity(UML2WithID_Activity uml2withid_activity) {
        this.uml2withid_activity = uml2withid_activity;
    }
    public UML2WithID_ActivityPartition getUml2withid_activitypartition() {
        return uml2withid_activitypartition;
    }

    public void setUml2withid_activitypartition(UML2WithID_ActivityPartition uml2withid_activitypartition) {
        this.uml2withid_activitypartition = uml2withid_activitypartition;
    }
    public UML2WithID_ValueSpecification getUml2withid_valuespecification() {
        return uml2withid_valuespecification;
    }

    public void setUml2withid_valuespecification(UML2WithID_ValueSpecification uml2withid_valuespecification) {
        this.uml2withid_valuespecification = uml2withid_valuespecification;
    }

}