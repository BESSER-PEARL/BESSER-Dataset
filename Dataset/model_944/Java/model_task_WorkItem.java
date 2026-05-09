




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class model_task_WorkItem extends Annotation {

    private int effort;
    private LocalDate dueDate;
    private int priority;
    private boolean resolved;
    private int estimate;



    public model_task_WorkItem(
        int effort,        LocalDate dueDate,        int priority,        boolean resolved,        int estimate    ) {
        super(
        );
        this.effort = effort;
        this.dueDate = dueDate;
        this.priority = priority;
        this.resolved = resolved;
        this.estimate = estimate;
    }


    public int getEffort() {
        return effort;
    }

    public void setEffort(int effort) {
        this.effort = effort;
    }
    public LocalDate getDuedate() {
        return dueDate;
    }

    public void setDuedate(LocalDate dueDate) {
        this.dueDate = dueDate;
    }
    public int getPriority() {
        return priority;
    }

    public void setPriority(int priority) {
        this.priority = priority;
    }
    public boolean getResolved() {
        return resolved;
    }

    public void setResolved(boolean resolved) {
        this.resolved = resolved;
    }
    public int getEstimate() {
        return estimate;
    }

    public void setEstimate(int estimate) {
        this.estimate = estimate;
    }


}