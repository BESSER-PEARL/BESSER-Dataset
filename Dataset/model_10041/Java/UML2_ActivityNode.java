





import java.util.List;
import java.util.ArrayList;

public class UML2_ActivityNode extends RedefinableElement {






    private UML2_ActivityEdge uml2_activityedge;




    private List<UML2_ActivityEdge> uml2_activityedges;




    private List<UML2_ActivityGroup> uml2_activitygroups;




    private UML2_ActivityNode uml2_activitynode;




    private UML2_StructuredActivityNode uml2_structuredactivitynode;




    private UML2_ActivityEdge uml2_activityedge;




    private UML2_Clause uml2_clause;




    private UML2_Clause uml2_clause;




    private List<UML2_ActivityEdge> uml2_activityedges;




    private UML2_ActivityPartition uml2_activitypartition;




    private UML2_StructuredActivityNode uml2_structuredactivitynode;




    private List<UML2_ActivityPartition> uml2_activitypartitions;


    public UML2_ActivityNode(
    ) {
        super(
        );
        this.uml2_activityedges = new ArrayList<>();
        this.uml2_activitygroups = new ArrayList<>();
        this.uml2_activityedges = new ArrayList<>();
        this.uml2_activitypartitions = new ArrayList<>();
    }

    public UML2_ActivityNode(
        ArrayList<UML2_ActivityEdge> uml2_activityedges,        ArrayList<UML2_ActivityGroup> uml2_activitygroups,        ArrayList<UML2_ActivityEdge> uml2_activityedges,        ArrayList<UML2_ActivityPartition> uml2_activitypartitions    ) {
        this.uml2_activityedges = uml2_activityedges;
        this.uml2_activitygroups = uml2_activitygroups;
        this.uml2_activityedges = uml2_activityedges;
        this.uml2_activitypartitions = uml2_activitypartitions;
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
    public List<UML2_ActivityGroup> getUml2_activitygroups() {
        return uml2_activitygroups;
    }

    public void addUml2_activitygroup(Uml2_activitygroup uml2_activitygroup) {
        this.uml2_activitygroups.add(uml2_activitygroup);
    }
    public UML2_ActivityNode getUml2_activitynode() {
        return uml2_activitynode;
    }

    public void setUml2_activitynode(UML2_ActivityNode uml2_activitynode) {
        this.uml2_activitynode = uml2_activitynode;
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
    public UML2_Clause getUml2_clause() {
        return uml2_clause;
    }

    public void setUml2_clause(UML2_Clause uml2_clause) {
        this.uml2_clause = uml2_clause;
    }
    public UML2_Clause getUml2_clause() {
        return uml2_clause;
    }

    public void setUml2_clause(UML2_Clause uml2_clause) {
        this.uml2_clause = uml2_clause;
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
    public UML2_StructuredActivityNode getUml2_structuredactivitynode() {
        return uml2_structuredactivitynode;
    }

    public void setUml2_structuredactivitynode(UML2_StructuredActivityNode uml2_structuredactivitynode) {
        this.uml2_structuredactivitynode = uml2_structuredactivitynode;
    }
    public List<UML2_ActivityPartition> getUml2_activitypartitions() {
        return uml2_activitypartitions;
    }

    public void addUml2_activitypartition(Uml2_activitypartition uml2_activitypartition) {
        this.uml2_activitypartitions.add(uml2_activitypartition);
    }

}