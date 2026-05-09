




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class model_task_WorkItem extends Annotation {

    private boolean resolved;
    private LocalDate dueDate;
    private int estimate;
    private int priority;
    private int effort;





    private List<organization_OrgUnit> organization_orgunits;




    private organization_OrgUnit organization_orgunit;




    private List<task_WorkItem> task_workitems;




    private List<task_WorkItem> task_workitems;


    public model_task_WorkItem(
        boolean resolved,        LocalDate dueDate,        int estimate,        int priority,        int effort    ) {
        super(
        );
        this.resolved = resolved;
        this.dueDate = dueDate;
        this.estimate = estimate;
        this.priority = priority;
        this.effort = effort;
        this.organization_orgunits = new ArrayList<>();
        this.task_workitems = new ArrayList<>();
        this.task_workitems = new ArrayList<>();
    }

    public model_task_WorkItem(
        boolean resolved,        LocalDate dueDate,        int estimate,        int priority,        int effort        ArrayList<organization_OrgUnit> organization_orgunits,        ArrayList<task_WorkItem> task_workitems,        ArrayList<task_WorkItem> task_workitems    ) {
        this.resolved = resolved;
        this.dueDate = dueDate;
        this.estimate = estimate;
        this.priority = priority;
        this.effort = effort;
        this.organization_orgunits = organization_orgunits;
        this.task_workitems = task_workitems;
        this.task_workitems = task_workitems;
    }

    public boolean getResolved() {
        return resolved;
    }

    public void setResolved(boolean resolved) {
        this.resolved = resolved;
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

    public List<organization_OrgUnit> getOrganization_orgunits() {
        return organization_orgunits;
    }

    public void addOrganization_orgunit(Organization_orgunit organization_orgunit) {
        this.organization_orgunits.add(organization_orgunit);
    }
    public organization_OrgUnit getOrganization_orgunit() {
        return organization_orgunit;
    }

    public void setOrganization_orgunit(organization_OrgUnit organization_orgunit) {
        this.organization_orgunit = organization_orgunit;
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