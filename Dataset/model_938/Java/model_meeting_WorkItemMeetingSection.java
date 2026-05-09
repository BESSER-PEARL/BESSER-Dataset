





import java.util.List;
import java.util.ArrayList;

public class model_meeting_WorkItemMeetingSection extends MeetingSection {






    private List<task_WorkItem> task_workitems;


    public model_meeting_WorkItemMeetingSection(
    ) {
        super(
        );
        this.task_workitems = new ArrayList<>();
    }

    public model_meeting_WorkItemMeetingSection(
        ArrayList<task_WorkItem> task_workitems    ) {
        this.task_workitems = task_workitems;
    }


    public List<task_WorkItem> getTask_workitems() {
        return task_workitems;
    }

    public void addTask_workitem(Task_workitem task_workitem) {
        this.task_workitems.add(task_workitem);
    }

}