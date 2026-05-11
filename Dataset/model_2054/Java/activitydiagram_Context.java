





import java.util.List;
import java.util.ArrayList;

public class activitydiagram_Context  {






    private activitydiagram_Context activitydiagram_context;




    private List<activitydiagram_InputValue> activitydiagram_inputvalues;




    private activitydiagram_Activity activitydiagram_activity;




    private activitydiagram_JoinNode activitydiagram_joinnode;


    public activitydiagram_Context(
    ) {
        this.activitydiagram_inputvalues = new ArrayList<>();
    }

    public activitydiagram_Context(
        ArrayList<activitydiagram_InputValue> activitydiagram_inputvalues    ) {
        this.activitydiagram_inputvalues = activitydiagram_inputvalues;
    }


    public activitydiagram_Context getActivitydiagram_context() {
        return activitydiagram_context;
    }

    public void setActivitydiagram_context(activitydiagram_Context activitydiagram_context) {
        this.activitydiagram_context = activitydiagram_context;
    }
    public List<activitydiagram_InputValue> getActivitydiagram_inputvalues() {
        return activitydiagram_inputvalues;
    }

    public void addActivitydiagram_inputvalue(Activitydiagram_inputvalue activitydiagram_inputvalue) {
        this.activitydiagram_inputvalues.add(activitydiagram_inputvalue);
    }
    public activitydiagram_Activity getActivitydiagram_activity() {
        return activitydiagram_activity;
    }

    public void setActivitydiagram_activity(activitydiagram_Activity activitydiagram_activity) {
        this.activitydiagram_activity = activitydiagram_activity;
    }
    public activitydiagram_JoinNode getActivitydiagram_joinnode() {
        return activitydiagram_joinnode;
    }

    public void setActivitydiagram_joinnode(activitydiagram_JoinNode activitydiagram_joinnode) {
        this.activitydiagram_joinnode = activitydiagram_joinnode;
    }

}