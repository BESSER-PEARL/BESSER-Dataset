




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class model_task_WorkItem extends Annotation {

    private boolean resolved;
    private int effort;
    private int priority;
    private int estimate;
    private LocalDate dueDate;





    private List<task_WorkItem> task_workitems;




    private List<task_WorkItem> task_workitems;


    public model_task_WorkItem(
        boolean resolved,        int effort,        int priority,        int estimate,        LocalDate dueDate    ) {
        super(
        );
        this.resolved = resolved;
        this.effort = effort;
        this.priority = priority;
        this.estimate = estimate;
        this.dueDate = dueDate;
        this.task_workitems = new ArrayList<>();
        this.task_workitems = new ArrayList<>();
    }

    public model_task_WorkItem(
        boolean resolved,        int effort,        int priority,        int estimate,        LocalDate dueDate        ArrayList<task_WorkItem> task_workitems,        ArrayList<task_WorkItem> task_workitems    ) {
        this.resolved = resolved;
        this.effort = effort;
        this.priority = priority;
        this.estimate = estimate;
        this.dueDate = dueDate;
        this.task_workitems = task_workitems;
        this.task_workitems = task_workitems;
    }

    public boolean getResolved() {
        return resolved;
    }

    public void setResolved(boolean resolved) {
        this.resolved = resolved;
    }
    public int getEffort() {
        return effort;
    }

    public void setEffort(int effort) {
        this.effort = effort;
    }
    public int getPriority() {
        return priority;
    }

    public void setPriority(int priority) {
        this.priority = priority;
    }
    public int getEstimate() {
        return estimate;
    }

    public void setEstimate(int estimate) {
        this.estimate = estimate;
    }
    public LocalDate getDuedate() {
        return dueDate;
    }

    public void setDuedate(LocalDate dueDate) {
        this.dueDate = dueDate;
    }

    public List<task_WorkItem> getTask_workitems() {
        return task_workitems;
    }

    public void addTask_workitem(Task_workitem task_workitem) {
        this.task_workitems.add(task_workitem);
    }
    public List<task_WorkItem> getTask_workitems() {
        return task_workitems;
    }

    public void addTask_workitem(Task_workitem task_workitem) {
        this.task_workitems.add(task_workitem);
    }

}