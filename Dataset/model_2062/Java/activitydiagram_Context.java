





import java.util.List;
import java.util.ArrayList;

public class activitydiagram_Context  {






    private activitydiagram_Activity activitydiagram_activity;




    private activitydiagram_Trace activitydiagram_trace;




    private List<activitydiagram_InputValue> activitydiagram_inputvalues;




    private activitydiagram_JoinNode activitydiagram_joinnode;


    public activitydiagram_Context(
    ) {
        this.activitydiagram_inputvalues = new ArrayList<>();
    }

    public activitydiagram_Context(
        ArrayList<activitydiagram_InputValue> activitydiagram_inputvalues    ) {
        this.activitydiagram_inputvalues = activitydiagram_inputvalues;
    }


    public activitydiagram_Activity getActivitydiagram_activity() {
        return activitydiagram_activity;
    }

    public void setActivitydiagram_activity(activitydiagram_Activity activitydiagram_activity) {
        this.activitydiagram_activity = activitydiagram_activity;
    }
    public activitydiagram_Trace getActivitydiagram_trace() {
        return activitydiagram_trace;
    }

    public void setActivitydiagram_trace(activitydiagram_Trace activitydiagram_trace) {
        this.activitydiagram_trace = activitydiagram_trace;
    }
    public List<activitydiagram_InputValue> getActivitydiagram_inputvalues() {
        return activitydiagram_inputvalues;
    }

    public void addActivitydiagram_inputvalue(Activitydiagram_inputvalue activitydiagram_inputvalue) {
        this.activitydiagram_inputvalues.add(activitydiagram_inputvalue);
    }
    public activitydiagram_JoinNode getActivitydiagram_joinnode() {
        return activitydiagram_joinnode;
    }

    public void setActivitydiagram_joinnode(activitydiagram_JoinNode activitydiagram_joinnode) {
        this.activitydiagram_joinnode = activitydiagram_joinnode;
    }

}