





import java.util.List;
import java.util.ArrayList;

public class UML_Activity_mine_ActivityNode extends Element {






    private List<UML_Activity_mine_ActivityEdge> uml_activity_mine_activityedges;




    private UML_Activity_mine_ActivityEdge uml_activity_mine_activityedge;




    private UML_Activity_mine_Activity uml_activity_mine_activity;




    private UML_Activity_mine_ActivityEdge uml_activity_mine_activityedge;




    private List<UML_Activity_mine_ActivityEdge> uml_activity_mine_activityedges;


    public UML_Activity_mine_ActivityNode(
    ) {
        super(
        );
        this.uml_activity_mine_activityedges = new ArrayList<>();
        this.uml_activity_mine_activityedges = new ArrayList<>();
    }

    public UML_Activity_mine_ActivityNode(
        ArrayList<UML_Activity_mine_ActivityEdge> uml_activity_mine_activityedges,        ArrayList<UML_Activity_mine_ActivityEdge> uml_activity_mine_activityedges    ) {
        this.uml_activity_mine_activityedges = uml_activity_mine_activityedges;
        this.uml_activity_mine_activityedges = uml_activity_mine_activityedges;
    }


    public List<UML_Activity_mine_ActivityEdge> getUml_activity_mine_activityedges() {
        return uml_activity_mine_activityedges;
    }

    public void addUml_activity_mine_activityedge(Uml_activity_mine_activityedge uml_activity_mine_activityedge) {
        this.uml_activity_mine_activityedges.add(uml_activity_mine_activityedge);
    }
    public UML_Activity_mine_ActivityEdge getUml_activity_mine_activityedge() {
        return uml_activity_mine_activityedge;
    }

    public void setUml_activity_mine_activityedge(UML_Activity_mine_ActivityEdge uml_activity_mine_activityedge) {
        this.uml_activity_mine_activityedge = uml_activity_mine_activityedge;
    }
    public UML_Activity_mine_Activity getUml_activity_mine_activity() {
        return uml_activity_mine_activity;
    }

    public void setUml_activity_mine_activity(UML_Activity_mine_Activity uml_activity_mine_activity) {
        this.uml_activity_mine_activity = uml_activity_mine_activity;
    }
    public UML_Activity_mine_ActivityEdge getUml_activity_mine_activityedge() {
        return uml_activity_mine_activityedge;
    }

    public void setUml_activity_mine_activityedge(UML_Activity_mine_ActivityEdge uml_activity_mine_activityedge) {
        this.uml_activity_mine_activityedge = uml_activity_mine_activityedge;
    }
    public List<UML_Activity_mine_ActivityEdge> getUml_activity_mine_activityedges() {
        return uml_activity_mine_activityedges;
    }

    public void addUml_activity_mine_activityedge(Uml_activity_mine_activityedge uml_activity_mine_activityedge) {
        this.uml_activity_mine_activityedges.add(uml_activity_mine_activityedge);
    }

}