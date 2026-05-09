





import java.util.List;
import java.util.ArrayList;

public class UML2_ActivityEdge extends RedefinableElement {






    private List<UML2_ActivityPartition> uml2_activitypartitions;




    private UML2_StructuredActivityNode uml2_structuredactivitynode;




    private UML2_ActivityEdge uml2_activityedge;




    private List<UML2_ActivityGroup> uml2_activitygroups;




    private UML2_ValueSpecification uml2_valuespecification;




    private UML2_StructuredActivityNode uml2_structuredactivitynode;




    private UML2_ValueSpecification uml2_valuespecification;




    private UML2_ActivityPartition uml2_activitypartition;


    public UML2_ActivityEdge(
    ) {
        super(
        );
        this.uml2_activitypartitions = new ArrayList<>();
        this.uml2_activitygroups = new ArrayList<>();
    }

    public UML2_ActivityEdge(
        ArrayList<UML2_ActivityPartition> uml2_activitypartitions,        ArrayList<UML2_ActivityGroup> uml2_activitygroups    ) {
        this.uml2_activitypartitions = uml2_activitypartitions;
        this.uml2_activitygroups = uml2_activitygroups;
    }


    public List<UML2_ActivityPartition> getUml2_activitypartitions() {
        return uml2_activitypartitions;
    }

    public void addUml2_activitypartition(Uml2_activitypartition uml2_activitypartition) {
        this.uml2_activitypartitions.add(uml2_activitypartition);
    }
    public UML2_StructuredActivityNode getUml2_structuredactivitynode() {
        return uml2_structuredactivitynode;
    }

    public void setUml2_structuredactivitynode(UML2_StructuredActivityNode uml2_structuredactivitynode) {
        this.uml2_structuredactivitynode = uml2_structuredactivitynode;
    }
    public UML2_ActivityEdge getUml2_activityedge() {
        return uml2_activityedge;
    }

    public void setUml2_activityedge(UML2_ActivityEdge uml2_activityedge) {
        this.uml2_activityedge = uml2_activityedge;
    }
    public List<UML2_ActivityGroup> getUml2_activitygroups() {
        return uml2_activitygroups;
    }

    public void addUml2_activitygroup(Uml2_activitygroup uml2_activitygroup) {
        this.uml2_activitygroups.add(uml2_activitygroup);
    }
    public UML2_ValueSpecification getUml2_valuespecification() {
        return uml2_valuespecification;
    }

    public void setUml2_valuespecification(UML2_ValueSpecification uml2_valuespecification) {
        this.uml2_valuespecification = uml2_valuespecification;
    }
    public UML2_StructuredActivityNode getUml2_structuredactivitynode() {
        return uml2_structuredactivitynode;
    }

    public void setUml2_structuredactivitynode(UML2_StructuredActivityNode uml2_structuredactivitynode) {
        this.uml2_structuredactivitynode = uml2_structuredactivitynode;
    }
    public UML2_ValueSpecification getUml2_valuespecification() {
        return uml2_valuespecification;
    }

    public void setUml2_valuespecification(UML2_ValueSpecification uml2_valuespecification) {
        this.uml2_valuespecification = uml2_valuespecification;
    }
    public UML2_ActivityPartition getUml2_activitypartition() {
        return uml2_activitypartition;
    }

    public void setUml2_activitypartition(UML2_ActivityPartition uml2_activitypartition) {
        this.uml2_activitypartition = uml2_activitypartition;
    }

}