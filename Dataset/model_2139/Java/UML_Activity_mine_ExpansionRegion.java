





import java.util.List;
import java.util.ArrayList;

public class UML_Activity_mine_ExpansionRegion extends Action {






    private List<UML_Activity_mine_ActivityNode> uml_activity_mine_activitynodes;




    private List<UML_Activity_mine_ActivityEdge> uml_activity_mine_activityedges;




    private List<UML_Activity_mine_ExpansionNode> uml_activity_mine_expansionnodes;




    private List<UML_Activity_mine_ExpansionNode> uml_activity_mine_expansionnodes;


    public UML_Activity_mine_ExpansionRegion(
    ) {
        super(
        );
        this.uml_activity_mine_activitynodes = new ArrayList<>();
        this.uml_activity_mine_activityedges = new ArrayList<>();
        this.uml_activity_mine_expansionnodes = new ArrayList<>();
        this.uml_activity_mine_expansionnodes = new ArrayList<>();
    }

    public UML_Activity_mine_ExpansionRegion(
        ArrayList<UML_Activity_mine_ActivityNode> uml_activity_mine_activitynodes,        ArrayList<UML_Activity_mine_ActivityEdge> uml_activity_mine_activityedges,        ArrayList<UML_Activity_mine_ExpansionNode> uml_activity_mine_expansionnodes,        ArrayList<UML_Activity_mine_ExpansionNode> uml_activity_mine_expansionnodes    ) {
        this.uml_activity_mine_activitynodes = uml_activity_mine_activitynodes;
        this.uml_activity_mine_activityedges = uml_activity_mine_activityedges;
        this.uml_activity_mine_expansionnodes = uml_activity_mine_expansionnodes;
        this.uml_activity_mine_expansionnodes = uml_activity_mine_expansionnodes;
    }


    public List<UML_Activity_mine_ActivityNode> getUml_activity_mine_activitynodes() {
        return uml_activity_mine_activitynodes;
    }

    public void addUml_activity_mine_activitynode(Uml_activity_mine_activitynode uml_activity_mine_activitynode) {
        this.uml_activity_mine_activitynodes.add(uml_activity_mine_activitynode);
    }
    public List<UML_Activity_mine_ActivityEdge> getUml_activity_mine_activityedges() {
        return uml_activity_mine_activityedges;
    }

    public void addUml_activity_mine_activityedge(Uml_activity_mine_activityedge uml_activity_mine_activityedge) {
        this.uml_activity_mine_activityedges.add(uml_activity_mine_activityedge);
    }
    public List<UML_Activity_mine_ExpansionNode> getUml_activity_mine_expansionnodes() {
        return uml_activity_mine_expansionnodes;
    }

    public void addUml_activity_mine_expansionnode(Uml_activity_mine_expansionnode uml_activity_mine_expansionnode) {
        this.uml_activity_mine_expansionnodes.add(uml_activity_mine_expansionnode);
    }
    public List<UML_Activity_mine_ExpansionNode> getUml_activity_mine_expansionnodes() {
        return uml_activity_mine_expansionnodes;
    }

    public void addUml_activity_mine_expansionnode(Uml_activity_mine_expansionnode uml_activity_mine_expansionnode) {
        this.uml_activity_mine_expansionnodes.add(uml_activity_mine_expansionnode);
    }

}