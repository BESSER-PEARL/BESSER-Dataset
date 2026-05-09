




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class model_task_WorkPackage extends WorkItem {

    private LocalDate startDate;
    private LocalDate endDate;





    private List<task_WorkItem> task_workitems;


    public model_task_WorkPackage(
        LocalDate startDate,        LocalDate endDate    ) {
        super(
        );
        this.startDate = startDate;
        this.endDate = endDate;
        this.task_workitems = new ArrayList<>();
    }

    public model_task_WorkPackage(
        LocalDate startDate,        LocalDate endDate        ArrayList<task_WorkItem> task_workitems    ) {
        this.startDate = startDate;
        this.endDate = endDate;
        this.task_workitems = task_workitems;
    }

    public LocalDate getStartdate() {
        return startDate;
    }

    public void setStartdate(LocalDate startDate) {
        this.startDate = startDate;
    }
    public LocalDate getEnddate() {
        return endDate;
    }

    public void setEnddate(LocalDate endDate) {
        this.endDate = endDate;
    }

    public List<task_WorkItem> getTask_workitems() {
        return task_workitems;
    }

    public void addTask_workitem(Task_workitem task_workitem) {
        this.task_workitems.add(task_workitem);
    }

}