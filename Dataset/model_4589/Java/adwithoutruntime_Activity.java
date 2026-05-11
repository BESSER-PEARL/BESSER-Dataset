





import java.util.List;
import java.util.ArrayList;

public class adwithoutruntime_Activity extends NamedElement {






    private adwithoutruntime_ActivityNode adwithoutruntime_activitynode;




    private List<adwithoutruntime_Variable> adwithoutruntime_variables;




    private List<adwithoutruntime_ActivityNode> adwithoutruntime_activitynodes;




    private List<adwithoutruntime_ActivityEdge> adwithoutruntime_activityedges;




    private List<adwithoutruntime_Variable> adwithoutruntime_variables;


    public adwithoutruntime_Activity(
    ) {
        super(
        );
        this.adwithoutruntime_variables = new ArrayList<>();
        this.adwithoutruntime_activitynodes = new ArrayList<>();
        this.adwithoutruntime_activityedges = new ArrayList<>();
        this.adwithoutruntime_variables = new ArrayList<>();
    }

    public adwithoutruntime_Activity(
        ArrayList<adwithoutruntime_Variable> adwithoutruntime_variables,        ArrayList<adwithoutruntime_ActivityNode> adwithoutruntime_activitynodes,        ArrayList<adwithoutruntime_ActivityEdge> adwithoutruntime_activityedges,        ArrayList<adwithoutruntime_Variable> adwithoutruntime_variables    ) {
        this.adwithoutruntime_variables = adwithoutruntime_variables;
        this.adwithoutruntime_activitynodes = adwithoutruntime_activitynodes;
        this.adwithoutruntime_activityedges = adwithoutruntime_activityedges;
        this.adwithoutruntime_variables = adwithoutruntime_variables;
    }


    public adwithoutruntime_ActivityNode getAdwithoutruntime_activitynode() {
        return adwithoutruntime_activitynode;
    }

    public void setAdwithoutruntime_activitynode(adwithoutruntime_ActivityNode adwithoutruntime_activitynode) {
        this.adwithoutruntime_activitynode = adwithoutruntime_activitynode;
    }
    public List<adwithoutruntime_Variable> getAdwithoutruntime_variables() {
        return adwithoutruntime_variables;
    }

    public void addAdwithoutruntime_variable(Adwithoutruntime_variable adwithoutruntime_variable) {
        this.adwithoutruntime_variables.add(adwithoutruntime_variable);
    }
    public List<adwithoutruntime_ActivityNode> getAdwithoutruntime_activitynodes() {
        return adwithoutruntime_activitynodes;
    }

    public void addAdwithoutruntime_activitynode(Adwithoutruntime_activitynode adwithoutruntime_activitynode) {
        this.adwithoutruntime_activitynodes.add(adwithoutruntime_activitynode);
    }
    public List<adwithoutruntime_ActivityEdge> getAdwithoutruntime_activityedges() {
        return adwithoutruntime_activityedges;
    }

    public void addAdwithoutruntime_activityedge(Adwithoutruntime_activityedge adwithoutruntime_activityedge) {
        this.adwithoutruntime_activityedges.add(adwithoutruntime_activityedge);
    }
    public List<adwithoutruntime_Variable> getAdwithoutruntime_variables() {
        return adwithoutruntime_variables;
    }

    public void addAdwithoutruntime_variable(Adwithoutruntime_variable adwithoutruntime_variable) {
        this.adwithoutruntime_variables.add(adwithoutruntime_variable);
    }

}