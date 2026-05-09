





import java.util.List;
import java.util.ArrayList;

public class project_Priority extends TaskTimesheetAttribute, TaskAttribute, NewTaskAttribute {

    private int priority;



    public project_Priority(
        int priority    ) {
        super(
        );
        this.priority = priority;
    }


    public int getPriority() {
        return priority;
    }

    public void setPriority(int priority) {
        this.priority = priority;
    }


}