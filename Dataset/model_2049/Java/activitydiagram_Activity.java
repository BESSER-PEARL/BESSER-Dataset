





import java.util.List;
import java.util.ArrayList;

public class activitydiagram_Activity extends NamedElement {

    private String inputValuePath;





    private activitydiagram_Trace activitydiagram_trace;




    private activitydiagram_ActivityNode activitydiagram_activitynode;




    private List<activitydiagram_ActivityEdge> activitydiagram_activityedges;




    private List<activitydiagram_Signal> activitydiagram_signals;




    private List<activitydiagram_ActivityNode> activitydiagram_activitynodes;




    private List<activitydiagram_Variable> activitydiagram_variables;




    private List<activitydiagram_Variable> activitydiagram_variables;


    public activitydiagram_Activity(
        String inputValuePath    ) {
        super(
        );
        this.inputValuePath = inputValuePath;
        this.activitydiagram_activityedges = new ArrayList<>();
        this.activitydiagram_signals = new ArrayList<>();
        this.activitydiagram_activitynodes = new ArrayList<>();
        this.activitydiagram_variables = new ArrayList<>();
        this.activitydiagram_variables = new ArrayList<>();
    }

    public activitydiagram_Activity(
        String inputValuePath        ArrayList<activitydiagram_ActivityEdge> activitydiagram_activityedges,        ArrayList<activitydiagram_Signal> activitydiagram_signals,        ArrayList<activitydiagram_ActivityNode> activitydiagram_activitynodes,        ArrayList<activitydiagram_Variable> activitydiagram_variables,        ArrayList<activitydiagram_Variable> activitydiagram_variables    ) {
        this.inputValuePath = inputValuePath;
        this.activitydiagram_activityedges = activitydiagram_activityedges;
        this.activitydiagram_signals = activitydiagram_signals;
        this.activitydiagram_activitynodes = activitydiagram_activitynodes;
        this.activitydiagram_variables = activitydiagram_variables;
        this.activitydiagram_variables = activitydiagram_variables;
    }

    public String getInputvaluepath() {
        return inputValuePath;
    }

    public void setInputvaluepath(String inputValuePath) {
        this.inputValuePath = inputValuePath;
    }

    public activitydiagram_Trace getActivitydiagram_trace() {
        return activitydiagram_trace;
    }

    public void setActivitydiagram_trace(activitydiagram_Trace activitydiagram_trace) {
        this.activitydiagram_trace = activitydiagram_trace;
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
    public List<activitydiagram_Signal> getActivitydiagram_signals() {
        return activitydiagram_signals;
    }

    public void addActivitydiagram_signal(Activitydiagram_signal activitydiagram_signal) {
        this.activitydiagram_signals.add(activitydiagram_signal);
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
    public List<activitydiagram_Variable> getActivitydiagram_variables() {
        return activitydiagram_variables;
    }

    public void addActivitydiagram_variable(Activitydiagram_variable activitydiagram_variable) {
        this.activitydiagram_variables.add(activitydiagram_variable);
    }

}