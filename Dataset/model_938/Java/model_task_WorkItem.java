




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class model_task_WorkItem extends Annotation {

    private int priority;
    private int effort;
    private LocalDate dueDate;
    private int estimate;
    private boolean resolved;



    public model_task_WorkItem(
        int priority,        int effort,        LocalDate dueDate,        int estimate,        boolean resolved    ) {
        super(
        );
        this.priority = priority;
        this.effort = effort;
        this.dueDate = dueDate;
        this.estimate = estimate;
        this.resolved = resolved;
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
    public int getEstimate() {
        return estimate;
    }

    public void setEstimate(int estimate) {
        this.estimate = estimate;
    }
    public boolean getResolved() {
        return resolved;
    }

    public void setResolved(boolean resolved) {
        this.resolved = resolved;
    }


}