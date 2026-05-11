





import java.util.List;
import java.util.ArrayList;

public class activitydiagram_Activity extends NamedElement {

    private String inputValuePath;





    private activitydiagram_Trace activitydiagram_trace;


    public activitydiagram_Activity(
        String inputValuePath    ) {
        super(
        );
        this.inputValuePath = inputValuePath;
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

}