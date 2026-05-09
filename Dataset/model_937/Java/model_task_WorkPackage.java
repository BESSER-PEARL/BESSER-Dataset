




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class model_task_WorkPackage extends WorkItem {

    private LocalDate endDate;
    private LocalDate startDate;





    private List<task_WorkItem> task_workitems;


    public model_task_WorkPackage(
        LocalDate endDate,        LocalDate startDate    ) {
        super(
        );
        this.endDate = endDate;
        this.startDate = startDate;
        this.task_workitems = new ArrayList<>();
    }

    public model_task_WorkPackage(
        LocalDate endDate,        LocalDate startDate        ArrayList<task_WorkItem> task_workitems    ) {
        this.endDate = endDate;
        this.startDate = startDate;
        this.task_workitems = task_workitems;
    }

    public LocalDate getEnddate() {
        return endDate;
    }

    public void setEnddate(LocalDate endDate) {
        this.endDate = endDate;
    }
    public LocalDate getStartdate() {
        return startDate;
    }

    public void setStartdate(LocalDate startDate) {
        this.startDate = startDate;
    }

    public List<task_WorkItem> getTask_workitems() {
        return task_workitems;
    }

    public void addTask_workitem(Task_workitem task_workitem) {
        this.task_workitems.add(task_workitem);
    }

}