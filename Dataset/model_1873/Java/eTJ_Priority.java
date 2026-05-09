





import java.util.List;
import java.util.ArrayList;

public class eTJ_Priority extends TaskTimesheetAttribute, NewTaskAttribute {

    private int priority;



    public eTJ_Priority(
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