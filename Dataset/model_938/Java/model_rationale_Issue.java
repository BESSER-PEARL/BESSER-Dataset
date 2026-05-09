





import java.util.List;
import java.util.ArrayList;

public class model_rationale_Issue extends task_Checkable, task_WorkItem, Annotation {

    private String activity;



    public model_rationale_Issue(
        String activity    ) {
        super(
        );
        this.activity = activity;
    }


    public String getActivity() {
        return activity;
    }

    public void setActivity(String activity) {
        this.activity = activity;
    }


}