





import java.util.List;
import java.util.ArrayList;

public class Activities_StructuredActivities_StructuredActivityNode extends FundamentalActivities_Namespace, FundamentalActivities_ActivityGroup, FundamentalActivities_Action, StructuredActivities_ExecutableNode {

    private boolean mustIsolate;





    private List<ActivityEdge> activityedges;




    private List<ActivityNode> activitynodes;




    private List<OutputPin> outputpins;




    private List<Variable> variables;




    private List<InputPin> inputpins;




    private Activity activity;


    public Activities_StructuredActivities_StructuredActivityNode(
        boolean mustIsolate    ) {
        super(
        );
        this.mustIsolate = mustIsolate;
        this.activityedges = new ArrayList<>();
        this.activitynodes = new ArrayList<>();
        this.outputpins = new ArrayList<>();
        this.variables = new ArrayList<>();
        this.inputpins = new ArrayList<>();
    }

    public Activities_StructuredActivities_StructuredActivityNode(
        boolean mustIsolate        ArrayList<ActivityEdge> activityedges,        ArrayList<ActivityNode> activitynodes,        ArrayList<OutputPin> outputpins,        ArrayList<Variable> variables,        ArrayList<InputPin> inputpins    ) {
        this.mustIsolate = mustIsolate;
        this.activityedges = activityedges;
        this.activitynodes = activitynodes;
        this.outputpins = outputpins;
        this.variables = variables;
        this.inputpins = inputpins;
    }

    public boolean getMustisolate() {
        return mustIsolate;
    }

    public void setMustisolate(boolean mustIsolate) {
        this.mustIsolate = mustIsolate;
    }

    public List<ActivityEdge> getActivityedges() {
        return activityedges;
    }

    public void addActivityedge(Activityedge activityedge) {
        this.activityedges.add(activityedge);
    }
    public List<ActivityNode> getActivitynodes() {
        return activitynodes;
    }

    public void addActivitynode(Activitynode activitynode) {
        this.activitynodes.add(activitynode);
    }
    public List<OutputPin> getOutputpins() {
        return outputpins;
    }

    public void addOutputpin(Outputpin outputpin) {
        this.outputpins.add(outputpin);
    }
    public List<Variable> getVariables() {
        return variables;
    }

    public void addVariable(Variable variable) {
        this.variables.add(variable);
    }
    public List<InputPin> getInputpins() {
        return inputpins;
    }

    public void addInputpin(Inputpin inputpin) {
        this.inputpins.add(inputpin);
    }
    public Activity getActivity() {
        return activity;
    }

    public void setActivity(Activity activity) {
        this.activity = activity;
    }

}