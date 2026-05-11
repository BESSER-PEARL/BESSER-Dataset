





import java.util.List;
import java.util.ArrayList;

public class activitydiagram_Activity extends NamedElement {






    private List<activitydiagram_Variable> activitydiagram_variables;




    private List<activitydiagram_Variable> activitydiagram_variables;




    private activitydiagram_Trace activitydiagram_trace;


    public activitydiagram_Activity(
    ) {
        super(
        );
        this.activitydiagram_variables = new ArrayList<>();
        this.activitydiagram_variables = new ArrayList<>();
    }

    public activitydiagram_Activity(
        ArrayList<activitydiagram_Variable> activitydiagram_variables,        ArrayList<activitydiagram_Variable> activitydiagram_variables    ) {
        this.activitydiagram_variables = activitydiagram_variables;
        this.activitydiagram_variables = activitydiagram_variables;
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
    public activitydiagram_Trace getActivitydiagram_trace() {
        return activitydiagram_trace;
    }

    public void setActivitydiagram_trace(activitydiagram_Trace activitydiagram_trace) {
        this.activitydiagram_trace = activitydiagram_trace;
    }

}