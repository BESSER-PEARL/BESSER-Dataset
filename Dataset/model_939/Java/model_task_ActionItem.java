





import java.util.List;
import java.util.ArrayList;

public class model_task_ActionItem extends task_WorkItem, task_Checkable {

    private boolean done;
    private String activity;



    public model_task_ActionItem(
        boolean done,        String activity    ) {
        super(
        );
        this.done = done;
        this.activity = activity;
    }


    public boolean getDone() {
        return done;
    }

    public void setDone(boolean done) {
        this.done = done;
    }
    public String getActivity() {
        return activity;
    }

    public void setActivity(String activity) {
        this.activity = activity;
    }


}