





import java.util.List;
import java.util.ArrayList;

public class uml_UML_ActivityNode  {

    private String name;





    private uml_UML_Activity uml_uml_activity;




    private uml_UML_ActivityEdge uml_uml_activityedge;




    private List<uml_UML_ActivityEdge> uml_uml_activityedges;




    private uml_UML_ActivityEdge uml_uml_activityedge;




    private uml_UML_ActivityNode uml_uml_activitynode;


    public uml_UML_ActivityNode(
        String name    ) {
        this.name = name;
        this.uml_uml_activityedges = new ArrayList<>();
    }

    public uml_UML_ActivityNode(
        String name        ArrayList<uml_UML_ActivityEdge> uml_uml_activityedges    ) {
        this.name = name;
        this.uml_uml_activityedges = uml_uml_activityedges;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public uml_UML_Activity getUml_uml_activity() {
        return uml_uml_activity;
    }

    public void setUml_uml_activity(uml_UML_Activity uml_uml_activity) {
        this.uml_uml_activity = uml_uml_activity;
    }
    public uml_UML_ActivityEdge getUml_uml_activityedge() {
        return uml_uml_activityedge;
    }

    public void setUml_uml_activityedge(uml_UML_ActivityEdge uml_uml_activityedge) {
        this.uml_uml_activityedge = uml_uml_activityedge;
    }
    public List<uml_UML_ActivityEdge> getUml_uml_activityedges() {
        return uml_uml_activityedges;
    }

    public void addUml_uml_activityedge(Uml_uml_activityedge uml_uml_activityedge) {
        this.uml_uml_activityedges.add(uml_uml_activityedge);
    }
    public uml_UML_ActivityEdge getUml_uml_activityedge() {
        return uml_uml_activityedge;
    }

    public void setUml_uml_activityedge(uml_UML_ActivityEdge uml_uml_activityedge) {
        this.uml_uml_activityedge = uml_uml_activityedge;
    }
    public uml_UML_ActivityNode getUml_uml_activitynode() {
        return uml_uml_activitynode;
    }

    public void setUml_uml_activitynode(uml_UML_ActivityNode uml_uml_activitynode) {
        this.uml_uml_activitynode = uml_uml_activitynode;
    }

}