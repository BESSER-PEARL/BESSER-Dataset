





import java.util.List;
import java.util.ArrayList;

public class model_task_ActionItem extends task_Checkable, task_WorkItem {

    private String activity;
    private boolean done;



    public model_task_ActionItem(
        String activity,        boolean done    ) {
        super(
        );
        this.activity = activity;
        this.done = done;
    }


    public String getActivity() {
        return activity;
    }

    public void setActivity(String activity) {
        this.activity = activity;
    }
    public boolean getDone() {
        return done;
    }

    public void setDone(boolean done) {
        this.done = done;
    }


}