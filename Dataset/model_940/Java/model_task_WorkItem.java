




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class model_task_WorkItem extends Annotation {

    private boolean resolved;
    private int estimate;
    private int priority;
    private int effort;
    private LocalDate dueDate;



    public model_task_WorkItem(
        boolean resolved,        int estimate,        int priority,        int effort,        LocalDate dueDate    ) {
        super(
        );
        this.resolved = resolved;
        this.estimate = estimate;
        this.priority = priority;
        this.effort = effort;
        this.dueDate = dueDate;
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
    public int getPriority() {
        return priority;
    }

    public void setPriority(int priority) {
        this.priority = priority;
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


}