





import java.util.List;
import java.util.ArrayList;

public class model_rationale_Issue extends Annotation, task_WorkItem, task_Checkable {

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