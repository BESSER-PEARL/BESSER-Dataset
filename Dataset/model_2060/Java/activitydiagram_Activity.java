





import java.util.List;
import java.util.ArrayList;

public class activitydiagram_Activity extends NamedElement {






    private List<activitydiagram_ActivityNode> activitydiagram_activitynodes;




    private List<activitydiagram_Variable> activitydiagram_variables;




    private activitydiagram_ActivityNode activitydiagram_activitynode;




    private List<activitydiagram_ActivityEdge> activitydiagram_activityedges;


    public activitydiagram_Activity(
    ) {
        super(
        );
        this.activitydiagram_activitynodes = new ArrayList<>();
        this.activitydiagram_variables = new ArrayList<>();
        this.activitydiagram_activityedges = new ArrayList<>();
    }

    public activitydiagram_Activity(
        ArrayList<activitydiagram_ActivityNode> activitydiagram_activitynodes,        ArrayList<activitydiagram_Variable> activitydiagram_variables,        ArrayList<activitydiagram_ActivityEdge> activitydiagram_activityedges    ) {
        this.activitydiagram_activitynodes = activitydiagram_activitynodes;
        this.activitydiagram_variables = activitydiagram_variables;
        this.activitydiagram_activityedges = activitydiagram_activityedges;
    }


    public List<activitydiagram_ActivityNode> getActivitydiagram_activitynodes() {
        return activitydiagram_activitynodes;
    }

    public void addActivitydiagram_activitynode(Activitydiagram_activitynode activitydiagram_activitynode) {
        this.activitydiagram_activitynodes.add(activitydiagram_activitynode);
    }
    public List<activitydiagram_Variable> getActivitydiagram_variables() {
        return activitydiagram_variables;
    }

    public void addActivitydiagram_variable(Activitydiagram_variable activitydiagram_variable) {
        this.activitydiagram_variables.add(activitydiagram_variable);
    }
    public activitydiagram_ActivityNode getActivitydiagram_activitynode() {
        return activitydiagram_activitynode;
    }

    public void setActivitydiagram_activitynode(activitydiagram_ActivityNode activitydiagram_activitynode) {
        this.activitydiagram_activitynode = activitydiagram_activitynode;
    }
    public List<activitydiagram_ActivityEdge> getActivitydiagram_activityedges() {
        return activitydiagram_activityedges;
    }

    public void addActivitydiagram_activityedge(Activitydiagram_activityedge activitydiagram_activityedge) {
        this.activitydiagram_activityedges.add(activitydiagram_activityedge);
    }

}