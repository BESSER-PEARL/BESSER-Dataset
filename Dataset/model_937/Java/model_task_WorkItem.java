




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class model_task_WorkItem extends Annotation {

    private LocalDate dueDate;
    private int effort;
    private int estimate;
    private boolean resolved;
    private int priority;



    public model_task_WorkItem(
        LocalDate dueDate,        int effort,        int estimate,        boolean resolved,        int priority    ) {
        super(
        );
        this.dueDate = dueDate;
        this.effort = effort;
        this.estimate = estimate;
        this.resolved = resolved;
        this.priority = priority;
    }


    public LocalDate getDuedate() {
        return dueDate;
    }

    public void setDuedate(LocalDate dueDate) {
        this.dueDate = dueDate;
    }
    public int getEffort() {
        return effort;
    }

    public void setEffort(int effort) {
        this.effort = effort;
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
    public int getPriority() {
        return priority;
    }

    public void setPriority(int priority) {
        this.priority = priority;
    }


}